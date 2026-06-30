#!/usr/bin/env python3
"""
T0 Hardware Validation — Stage 1: Bell State Repeatability
============================================================
Open-Plan budget-aware version (10-minute monthly QPU runtime)

Replicates and extends the June 2025 Bell-state generation test on IBM Quantum
hardware. Sized for the free Open Plan (10 min QPU runtime per 28-day window).

  - 10 runs × 2048 shots ≈ 0.3–1 min QPU runtime (well under 10 min budget)
  - Identical transpilation across all runs (seed_transpiler fixed)
  - Full per-run logging: job IDs, UTC timestamps, all 4 counts
  - CSV output, no hidden post-processing

Scale-up: if you have the 180-min promotion (active Open Plan users), increase
NUM_RUNS to 20 or 30 — the script structure is the same.

T0 prediction (deterministic evolution):
  P(|00>) = 0.500, P(|11>) = 0.500, P(|01>) = P(|10>) = 0
  Repeatability variance: lower than standard shot-noise

Author: Johann Pascher
Theory: FFGFT (Fundamentale Fraktale Geometrische Feldtheorie)
"""

import csv
import sys
import time
from datetime import datetime, timezone

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

# ────────────────────────────────────────────────────────────────
# CONFIGURATION — edit only this block
# ────────────────────────────────────────────────────────────────

# Two options:
#   (a) Leave as None and run `QiskitRuntimeService.save_account(...)` once
#       beforehand — see stage1_anleitung.md. Then this script loads it
#       automatically. RECOMMENDED — token never sits in this file.
#   (b) Paste your token here as a string. Do NOT commit this file then.
IBM_TOKEN = None

# Your Open Plan instance CRN. The connection warning showed:
#   crn:v1:bluemix:public:quantum-computing:us-east:a/<acct>:<instance>::
# Passing it explicitly fixes the intermittent "instance not set" / empty-list
# problem. Verify/replace from https://quantum.cloud.ibm.com → your instance
# details if this exact string does not work.
IBM_INSTANCE = "crn:v1:bluemix:public:quantum-computing:us-east:a/83f00ce3abce4277a68003abd180a50a:82206642-740e-4d61-8c2b-95a33e63413c::"

NUM_RUNS = 50                # statistical power for the chi-square test
SHOTS_PER_RUN = 2048         # same as the June 2025 test
SLEEP_BETWEEN_RUNS = 2.0     # courtesy delay between job submits, seconds

# Backend selection — confirmed available to this Open Plan account (May 2026):
#   ibm_kingston  (Heron r2, 156 qubits) — shortest queue, first choice
#   ibm_marrakesh (Heron r2, 156 qubits) — fallback
# Order = preference. The script tries each in turn; if neither is available,
# it falls back to least_busy on any operational QPU.
BACKEND_CANDIDATES = ["ibm_kingston", "ibm_marrakesh"]

OUTPUT_CSV = "bell_repeatability_2026.csv"


# ────────────────────────────────────────────────────────────────
# T0 PREDICTION and JUNE 2025 REFERENCE
# ────────────────────────────────────────────────────────────────

T0_PREDICTION = {"00": 0.5, "01": 0.0, "10": 0.0, "11": 0.5}
JUNE_2025_VARIANCE = 0.000248       # observed variance(P(00)) across 3 runs
JUNE_2025_FIDELITY = 0.9717         # observed Bell fidelity, Brisbane

# Shot-noise reference for Bin(N=SHOTS, p=0.5) / N
def shot_noise_variance(shots: int, p: float = 0.5) -> float:
    return p * (1 - p) / shots


# ────────────────────────────────────────────────────────────────
# BELL STATE CIRCUIT
# ────────────────────────────────────────────────────────────────

def build_bell_circuit() -> QuantumCircuit:
    """Standard Bell state |Phi+> = (|00> + |11>)/sqrt(2)."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc


# ────────────────────────────────────────────────────────────────
# SINGLE RUN
# ────────────────────────────────────────────────────────────────

def run_one(sampler: SamplerV2, qc_transpiled: QuantumCircuit, shots: int) -> dict:
    submit_time = datetime.now(timezone.utc).isoformat()
    job = sampler.run([qc_transpiled], shots=shots)
    job_id = job.job_id()
    print(f"    submitted job {job_id}")

    result = job.result()
    finish_time = datetime.now(timezone.utc).isoformat()

    pub_result = result[0]
    try:
        counts = pub_result.data.meas.get_counts()
    except AttributeError:
        data_names = list(pub_result.data.keys()) if hasattr(pub_result.data, "keys") else []
        if not data_names:
            raise RuntimeError("could not locate counts in SamplerV2 result")
        counts = getattr(pub_result.data, data_names[0]).get_counts()

    return {
        "job_id": job_id,
        "submitted_utc": submit_time,
        "finished_utc": finish_time,
        "counts": counts,
    }


def to_probs(counts: dict, shots: int) -> dict:
    total = sum(counts.values()) or shots
    return {k: counts.get(k, 0) / total for k in ("00", "01", "10", "11")}


# ────────────────────────────────────────────────────────────────
# BACKEND SELECTION
# ────────────────────────────────────────────────────────────────

def pick_backend(service: QiskitRuntimeService):
    """Select a backend using the LIST path (service.backends()), which works
    for this Open Plan account — the direct service.backend(name) lookup does
    not. Prefer names in BACKEND_CANDIDATES order; otherwise shortest queue."""
    print("Querying available backends (list path)...")
    # IMPORTANT: the bare service.backends() works for this account; passing
    # operational=/simulator= filters returns an empty list. So filter here.
    # The list is sometimes empty on the first try (instance resolution / brief
    # maintenance) — retry a few times before giving up.
    raw = []
    for attempt in range(1, 6):
        raw = service.backends()
        if raw:
            break
        print(f"    attempt {attempt}: empty list, retrying in 10 s...")
        time.sleep(10)
    if not raw:
        raise RuntimeError(
            "service.backends() returned nothing after 5 attempts.\n"
            "Likely causes: (1) both QPUs in maintenance right now — check\n"
            "https://quantum.cloud.ibm.com/status ; (2) wrong IBM_INSTANCE CRN —\n"
            "verify it in your instance details on the platform.")

    # Keep real QPUs that are operational; drop simulators
    all_backends = []
    for b in raw:
        try:
            is_sim = getattr(b.configuration(), "simulator", False)
        except Exception:
            is_sim = False
        try:
            op = b.status().operational
        except Exception:
            op = False
        if op and not is_sim:
            all_backends.append(b)

    if not all_backends:
        raise RuntimeError("No operational QPU available to this account right now.")

    by_name = {b.name: b for b in all_backends}
    print("Available operational QPUs:")
    for b in all_backends:
        st = b.status()
        print(f"    {b.name:25} {b.num_qubits:>4} qubits  queue={st.pending_jobs}")

    # 1) Prefer the configured candidates, in order
    for name in BACKEND_CANDIDATES:
        if name in by_name:
            backend = by_name[name]
            st = backend.status()
            print(f"Selected (preferred): {backend.name} "
                  f"({backend.num_qubits} qubits, queue {st.pending_jobs})")
            return backend

    # 2) Otherwise: shortest queue among all operational QPUs
    backend = min(all_backends, key=lambda b: b.status().pending_jobs)
    st = backend.status()
    print(f"Selected (shortest queue): {backend.name} "
          f"({backend.num_qubits} qubits, queue {st.pending_jobs})")
    return backend

# ────────────────────────────────────────────────────────────────
# MAIN
# ────────────────────────────────────────────────────────────────

def main() -> int:
    # Validation handled when constructing the service below.

    estimated_qpu_seconds = NUM_RUNS * 4  # ~2–5 s per Bell run, 4 is a safe mean
    print("=" * 70)
    print("T0 HARDWARE VALIDATION — Stage 1: Bell repeatability")
    print("=" * 70)
    print(f"Started:           {datetime.now(timezone.utc).isoformat()}")
    print(f"Configuration:     {NUM_RUNS} runs × {SHOTS_PER_RUN} shots")
    print(f"Estimated QPU time: ~{estimated_qpu_seconds} s "
          f"(~{estimated_qpu_seconds/60:.1f} min) — Open Plan budget: 10 min/28 d")
    print()

    print("Connecting to IBM Quantum...")
    if IBM_TOKEN is None:
        # Use the saved account (recommended)
        try:
            service = QiskitRuntimeService(channel="ibm_quantum_platform", instance=IBM_INSTANCE)
        except Exception as e:
            print(f"ERROR: no saved account found ({e}).")
            print("Either set IBM_TOKEN at the top of this script, or run once:")
            print("  from qiskit_ibm_runtime import QiskitRuntimeService")
            print("  QiskitRuntimeService.save_account(")
            print("      channel='ibm_quantum_platform',")
            print("      token='<your-44-char-token>',")
            print("      set_as_default=True, overwrite=True)")
            return 1
    else:
        service = QiskitRuntimeService(channel="ibm_quantum_platform", token=IBM_TOKEN, instance=IBM_INSTANCE)
    backend = pick_backend(service)
    print()

    # Transpile ONCE so all runs use identical circuit form
    qc = build_bell_circuit()
    qc_transpiled = transpile(qc, backend, optimization_level=3, seed_transpiler=42)
    print(f"Transpiled circuit depth: {qc_transpiled.depth()}")
    print(f"Transpiled gate counts: {dict(qc_transpiled.count_ops())}")
    print()

    sampler = SamplerV2(mode=backend)

    # ────────────────────────────────────────────────────────────
    # Execute the runs
    # ────────────────────────────────────────────────────────────

    all_results = []
    for i in range(1, NUM_RUNS + 1):
        print(f"Run {i}/{NUM_RUNS}:")
        try:
            run = run_one(sampler, qc_transpiled, SHOTS_PER_RUN)
            probs = to_probs(run["counts"], SHOTS_PER_RUN)
            fidelity = probs["00"] + probs["11"]
            print(f"    P(00)={probs['00']:.6f}  P(01)={probs['01']:.6f}  "
                  f"P(10)={probs['10']:.6f}  P(11)={probs['11']:.6f}  "
                  f"F={fidelity:.4f}")

            all_results.append({
                "run": i, "job_id": run["job_id"],
                "submitted_utc": run["submitted_utc"],
                "finished_utc": run["finished_utc"],
                "backend": backend.name, "shots": SHOTS_PER_RUN,
                "P00": probs["00"], "P01": probs["01"],
                "P10": probs["10"], "P11": probs["11"],
                "bell_fidelity": fidelity,
            })
        except Exception as e:
            print(f"    !! run {i} failed: {e}")
            all_results.append({
                "run": i, "job_id": "", "submitted_utc": "", "finished_utc": "",
                "backend": backend.name, "shots": SHOTS_PER_RUN,
                "P00": "", "P01": "", "P10": "", "P11": "",
                "bell_fidelity": "", "error": str(e),
            })

        time.sleep(SLEEP_BETWEEN_RUNS)

    # ────────────────────────────────────────────────────────────
    # Save raw data
    # ────────────────────────────────────────────────────────────

    fieldnames = ["run", "job_id", "submitted_utc", "finished_utc", "backend",
                  "shots", "P00", "P01", "P10", "P11", "bell_fidelity"]
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for r in all_results:
            writer.writerow(r)
    print()
    print(f"Raw data saved to: {OUTPUT_CSV}")

    # ────────────────────────────────────────────────────────────
    # Quick analysis
    # ────────────────────────────────────────────────────────────

    P00 = np.array([r["P00"] for r in all_results if isinstance(r["P00"], float)])
    P11 = np.array([r["P11"] for r in all_results if isinstance(r["P11"], float)])
    fids = np.array([r["bell_fidelity"] for r in all_results
                     if isinstance(r["bell_fidelity"], float)])
    n_success = len(fids)

    if n_success < 2:
        print(f"\nOnly {n_success} successful run(s) — variance analysis skipped.")
        return 0

    print()
    print("=" * 70)
    print(f"ANALYSIS ({n_success} successful runs of {NUM_RUNS})")
    print("=" * 70)
    print(f"P(00):           mean = {P00.mean():.6f}   "
          f"variance = {P00.var(ddof=1):.6e}   sd = {P00.std(ddof=1):.6f}")
    print(f"P(11):           mean = {P11.mean():.6f}   "
          f"variance = {P11.var(ddof=1):.6e}   sd = {P11.std(ddof=1):.6f}")
    print(f"Bell fidelity:   mean = {fids.mean():.6f}   "
          f"variance = {fids.var(ddof=1):.6e}   sd = {fids.std(ddof=1):.6f}")
    print()

    # Comparison against shot-noise variance
    sn_var = shot_noise_variance(SHOTS_PER_RUN)
    p00_ratio = P00.var(ddof=1) / sn_var
    print(f"Shot-noise reference: variance(P) for Bin(N={SHOTS_PER_RUN}, p=0.5)/N "
          f"= {sn_var:.6e}")
    print(f"Observed variance(P(00)) / shot-noise variance = {p00_ratio:.3f}")
    print()
    print("Interpretation:")
    print("  < 1.0  → repeatability below standard shot-noise (T0 direction)")
    print("  ≈ 1.0  → consistent with standard shot-noise")
    print("  > 1.0  → run-to-run drift on top of shot-noise (calibration etc.)")
    print()

    # June 2025 comparison
    print(f"June 2025 reference (3 runs, Brisbane Eagle): "
          f"variance(P(00)) = {JUNE_2025_VARIANCE:.6e}")
    print(f"This run ({n_success} runs, {backend.name} Heron r2): "
          f"variance(P(00)) = {P00.var(ddof=1):.6e}")
    print(f"June 2025 fidelity (Brisbane): {JUNE_2025_FIDELITY:.4f}")
    print(f"This run fidelity ({backend.name}): {fids.mean():.4f}")
    print()
    print("NOTE: different hardware generation (Heron r2 vs the 2025 Eagle).")
    print("The variance-vs-shot-noise RATIO is the hardware-independent")
    print("comparison; absolute fidelity differs by device generation.")
    print()
    print(f"Finished: {datetime.now(timezone.utc).isoformat()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
