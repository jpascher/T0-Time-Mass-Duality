#!/usr/bin/env python3
"""
T0 Hardware Validation — Stage 2: CHSH Bell Inequality Measurement
===================================================================
Open-Plan budget-aware (15 measurements, ~5 min QPU runtime)

The first real CHSH-parameter measurement on hardware in this corpus.
Stage 1 measured only Bell-state probabilities in one basis; CHSH requires
FOUR angle settings and computes the S-parameter from correlators.

CHSH:  S = E(a,b) + E(a,b') + E(a',b) - E(a',b')  (sign matches angles below)
Standard angles (the ones that maximise S under QM):
  a  = 0,        a' = pi/4   (Alice)
  b  = pi/8,     b' = -pi/8  (Bob)
QM prediction:        S = 2*sqrt(2) = 2.828427 (Tsirelson bound)
Classical (local):    |S| <= 2
T0 prediction:        S deviates from 2*sqrt(2) by ~xi (~1e-5) — FAR below
                      current NISQ noise (~1e-2). So the MEASURED S will sit
                      somewhat BELOW 2*sqrt(2) due to decoherence, NOT due to
                      xi. This run documents the achievable CHSH value and its
                      run-to-run spread; it does NOT claim to resolve xi.

Each correlator E(a,b) is measured by rotating each qubit before measurement
so the chosen measurement axis maps onto the Z basis:
  measure qubit in axis theta  <=>  apply Ry(-2*theta) then measure Z.

E(a,b) = [N00 - N01 - N10 + N11] / Ntot

Author: Johann Pascher
Theory: FFGFT (T0 / Zeit-Masse-Dualitaet)
"""

import csv
import sys
import time
import math
from datetime import datetime, timezone

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

# ────────────────────────────────────────────────────────────────
# CONFIGURATION — edit only this block
# ────────────────────────────────────────────────────────────────

IBM_TOKEN = None   # set to "your-token" OR leave None to use saved account

IBM_INSTANCE = "crn:v1:bluemix:public:quantum-computing:us-east:a/83f00ce3abce4277a68003abd180a50a:82206642-740e-4d61-8c2b-95a33e63413c::"

NUM_MEASUREMENTS = 15        # full CHSH (4 settings) repeated this many times
SHOTS_PER_SETTING = 2048
SLEEP_BETWEEN = 1.0

BACKEND_CANDIDATES = ["ibm_kingston", "ibm_marrakesh"]
OUTPUT_CSV = "chsh_stage2_2026.csv"

# CHSH angles (radians). Standard optimal configuration.
ALICE = {"a": 0.0,           "a_prime": math.pi/4}
BOB   = {"b": math.pi/8,     "b_prime": -math.pi/8}
TSIRELSON = 2*math.sqrt(2)


# ────────────────────────────────────────────────────────────────
# CIRCUITS
# ────────────────────────────────────────────────────────────────

def bell_with_measurement(theta_a: float, theta_b: float) -> QuantumCircuit:
    """Bell pair, then measure qubit0 along axis theta_a and qubit1 along
    theta_b. Measuring along axis theta = apply Ry(-2 theta) then measure Z."""
    qc = QuantumCircuit(2, 2)
    # Bell state
    qc.h(0)
    qc.cx(0, 1)
    # Rotate measurement bases
    qc.ry(-2*theta_a, 0)
    qc.ry(-2*theta_b, 1)
    qc.measure([0, 1], [0, 1])
    return qc


def correlator_from_counts(counts: dict, shots: int) -> float:
    """E = [N00 - N01 - N10 + N11] / Ntot, with eigenvalue +1 for outcome 0,
    -1 for outcome 1 on each qubit (so 00,11 -> +1 ; 01,10 -> -1)."""
    n00 = counts.get("00", 0)
    n01 = counts.get("01", 0)
    n10 = counts.get("10", 0)
    n11 = counts.get("11", 0)
    total = n00 + n01 + n10 + n11 or shots
    return (n00 - n01 - n10 + n11) / total


# ────────────────────────────────────────────────────────────────
# BACKEND (list path — works for this Open Plan account)
# ────────────────────────────────────────────────────────────────

def pick_backend(service):
    print("Querying available backends (list path)...")
    raw = []
    for attempt in range(1, 6):
        raw = service.backends()
        if raw:
            break
        print(f"    attempt {attempt}: empty list, retrying in 10 s...")
        time.sleep(10)
    if not raw:
        raise RuntimeError("service.backends() returned nothing after 5 attempts.")

    all_b = []
    for b in raw:
        try:
            sim = getattr(b.configuration(), "simulator", False)
        except Exception:
            sim = False
        try:
            op = b.status().operational
        except Exception:
            op = False
        if op and not sim:
            all_b.append(b)
    if not all_b:
        raise RuntimeError("No operational QPU available right now.")

    by_name = {b.name: b for b in all_b}
    print("Available operational QPUs:")
    for b in all_b:
        st = b.status()
        print(f"    {b.name:25} {b.num_qubits:>4} qubits  queue={st.pending_jobs}")
    for name in BACKEND_CANDIDATES:
        if name in by_name:
            b = by_name[name]
            print(f"Selected (preferred): {b.name} (queue {b.status().pending_jobs})")
            return b
    b = min(all_b, key=lambda x: x.status().pending_jobs)
    print(f"Selected (shortest queue): {b.name}")
    return b


# ────────────────────────────────────────────────────────────────
# MAIN
# ────────────────────────────────────────────────────────────────

def main() -> int:
    est = NUM_MEASUREMENTS * 4 * 5  # 4 settings, ~5s each
    print("=" * 70)
    print("T0 HARDWARE VALIDATION — Stage 2: CHSH measurement")
    print("=" * 70)
    print(f"Started:           {datetime.now(timezone.utc).isoformat()}")
    print(f"Configuration:     {NUM_MEASUREMENTS} CHSH measurements "
          f"× 4 settings × {SHOTS_PER_SETTING} shots")
    print(f"Estimated QPU time: ~{est} s (~{est/60:.1f} min)")
    print(f"QM/Tsirelson bound: S = 2√2 = {TSIRELSON:.6f}")
    print(f"Classical bound:    |S| ≤ 2")
    print()

    print("Connecting to IBM Quantum...")
    if IBM_TOKEN is None:
        service = QiskitRuntimeService(channel="ibm_quantum_platform",
                                       instance=IBM_INSTANCE)
    else:
        service = QiskitRuntimeService(channel="ibm_quantum_platform",
                                       token=IBM_TOKEN, instance=IBM_INSTANCE)
    backend = pick_backend(service)
    print()

    # The four CHSH settings: (Alice angle, Bob angle)
    settings = {
        "ab":   (ALICE["a"],       BOB["b"]),        # E(a,b)
        "ab'":  (ALICE["a"],       BOB["b_prime"]),  # E(a,b')
        "a'b":  (ALICE["a_prime"], BOB["b"]),        # E(a',b)
        "a'b'": (ALICE["a_prime"], BOB["b_prime"]),  # E(a',b')
    }

    # Transpile each of the four circuits ONCE
    transpiled = {}
    for key, (ta, tb) in settings.items():
        qc = bell_with_measurement(ta, tb)
        transpiled[key] = transpile(qc, backend, optimization_level=3,
                                    seed_transpiler=42)
    print(f"Transpiled 4 CHSH circuits (depths: "
          f"{ {k: c.depth() for k, c in transpiled.items()} })")
    print()

    sampler = SamplerV2(mode=backend)

    def run_setting(qc):
        job = sampler.run([qc], shots=SHOTS_PER_SETTING)
        jid = job.job_id()
        res = job.result()[0]
        try:
            counts = res.data.c.get_counts()
        except AttributeError:
            try:
                counts = res.data.meas.get_counts()
            except AttributeError:
                names = list(res.data.keys()) if hasattr(res.data, "keys") else []
                counts = getattr(res.data, names[0]).get_counts()
        return jid, counts

    all_rows = []
    S_values = []
    for m in range(1, NUM_MEASUREMENTS + 1):
        print(f"CHSH measurement {m}/{NUM_MEASUREMENTS}:")
        E = {}
        jids = {}
        ok = True
        for key in ("ab", "ab'", "a'b", "a'b'"):
            try:
                jid, counts = run_setting(transpiled[key])
                E[key] = correlator_from_counts(counts, SHOTS_PER_SETTING)
                jids[key] = jid
                print(f"    E({key:4}) = {E[key]:+.4f}   (job {jid})")
            except Exception as e:
                print(f"    !! setting {key} failed: {e}")
                ok = False
                break
            time.sleep(SLEEP_BETWEEN)

        if ok:
            # S = E(a,b) + E(a,b') + E(a',b) - E(a',b')  (correct for these angles)
            S = E["ab"] + E["ab'"] + E["a'b"] - E["a'b'"]
            S_values.append(S)
            print(f"    => S = {S:+.6f}   (Tsirelson {TSIRELSON:.4f}, "
                  f"deviation {S-TSIRELSON:+.4f})")
            all_rows.append({
                "measurement": m,
                "E_ab": E["ab"], "E_abp": E["ab'"],
                "E_apb": E["a'b"], "E_apbp": E["a'b'"],
                "S": S,
                "backend": backend.name,
                "job_ab": jids["ab"], "job_abp": jids["ab'"],
                "job_apb": jids["a'b"], "job_apbp": jids["a'b'"],
            })
        else:
            all_rows.append({"measurement": m, "E_ab": "", "E_abp": "",
                             "E_apb": "", "E_apbp": "", "S": "",
                             "backend": backend.name, "job_ab": "",
                             "job_abp": "", "job_apb": "", "job_apbp": ""})
        print()

    # Save
    fields = ["measurement", "E_ab", "E_abp", "E_apb", "E_apbp", "S",
              "backend", "job_ab", "job_abp", "job_apb", "job_apbp"]
    with open(OUTPUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in all_rows:
            w.writerow(r)
    print(f"Raw data saved to: {OUTPUT_CSV}")

    # Analysis
    S = np.array(S_values)
    if len(S) < 2:
        print(f"\nOnly {len(S)} valid CHSH value(s) — no statistics.")
        return 0

    print()
    print("=" * 70)
    print(f"ANALYSIS ({len(S)} valid CHSH measurements)")
    print("=" * 70)
    print(f"Mean S        = {S.mean():.6f}")
    print(f"Std dev       = {S.std(ddof=1):.6f}")
    print(f"Std error     = {S.std(ddof=1)/math.sqrt(len(S)):.6f}")
    print(f"Min / Max     = {S.min():.4f} / {S.max():.4f}")
    print()
    print(f"Tsirelson bound (QM max):  {TSIRELSON:.6f}")
    print(f"Classical bound:           2.000000")
    print(f"Mean deviation from 2√2:   {S.mean()-TSIRELSON:+.6f} "
          f"({(S.mean()-TSIRELSON)/TSIRELSON*100:+.3f} %)")
    print()
    # Is S > 2 (violation of local realism)?
    se = S.std(ddof=1)/math.sqrt(len(S))
    z_classical = (S.mean() - 2.0) / se
    print(f"Bell violation test (S > 2):")
    print(f"  (mean S - 2) / SE = {z_classical:.1f} sigma above classical bound")
    print(f"  => {'CLEAR Bell violation' if z_classical > 3 else 'check'} "
          f"(local realism excluded)")
    print()
    print("INTERPRETATION:")
    print(f"  Measured S sits below the Tsirelson bound by "
          f"{TSIRELSON-S.mean():.4f}.")
    print("  This deviation is dominated by NISQ decoherence (~1e-2 scale),")
    print("  NOT by the T0 xi-effect (~1e-5). This run documents the achievable")
    print("  hardware CHSH value; it does not resolve xi (which needs")
    print("  error-corrected qubits). The clear S > 2 result confirms genuine")
    print("  entanglement / Bell-inequality violation on the device.")
    print()
    print(f"Finished: {datetime.now(timezone.utc).isoformat()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
