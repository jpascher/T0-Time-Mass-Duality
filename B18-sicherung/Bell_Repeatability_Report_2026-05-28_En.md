# Bell-State Repeatability on IBM Quantum Hardware

**Validation Report — 28 May 2026**
Johann Pascher · FFGFT (T0 / Time-Mass Duality)
ORCID 0009-0000-6518-4064

---

## Summary

50 independent Bell-state measurements were carried out on IBM
`ibm_kingston` (Heron r2, 156 qubits) to test the side-prediction made
in the June 2025 report: that the run-to-run variance of the Bell
measurement lies **below** the level of ordinary quantum shot-noise
(the signature of deterministic evolution in the T0 picture).

**Result:** The repeatability variance is statistically **indistinguishable**
from ordinary shot-noise. The "deterministically reduced variance"
side-prediction is **not supported** by this measurement. Bell-state
generation itself succeeds with high and stable fidelity (98.76 %).

This finding **supersedes** the repeatability claim of the June 2025
report (see Section 5). The central ξ-prediction is **unaffected** by
this result (see Section 6).

---

## 1. Setup

| Parameter | Value |
|-----------|-------|
| Backend | `ibm_kingston` (IBM Heron r2, 156 qubits, heavy-hex) |
| Circuit | Bell state \|Φ+⟩ = (\|00⟩+\|11⟩)/√2 (H, CNOT, measure_all) |
| Transpilation | optimization_level=3, seed_transpiler=42 (identical across all runs) |
| Transpiled depth | 7 (rz×5, sx×3, cz×1, measure×2) |
| Runs | 50 independent, sequential |
| Shots per run | 2048 |
| Total QPU time | ~200 s (wall-clock 743 s incl. queue) |
| Date | 28 May 2026, 14:15–14:28 UTC |
| Job IDs | d8c4s047… (run 1) to d8c51o38… (run 50), fully in CSV |

Identical transpilation across all runs is methodologically essential:
only then does the run-to-run variance measure *hardware repeatability*
rather than random transpilation differences.

---

## 2. Results

| Quantity | Mean | Variance | Ratio to shot-noise |
|----------|------|----------|---------------------|
| P(\|00⟩) | 0.509072 | 1.249·10⁻⁴ | **1.023** |
| P(\|11⟩) | 0.478535 | 1.184·10⁻⁴ | **0.970** |
| Bell fidelity | 0.987607 | — | sd = 0.002804 |

Shot-noise reference for Bin(N=2048, p=0.5)/N: 1.221·10⁻⁴.
Error outcomes (leakage): P(\|01⟩)+P(\|10⟩) = 1.24 %.
Fidelity range across 50 runs: 0.9785 – 0.9927.

---

## 3. Statistical test of the core hypothesis

**Hypothesis (June 2025):** Var(P) < shot-noise variance (deterministic
evolution reduces run-to-run scatter).

**Test:** χ² test on the sample variance. Under the null hypothesis
(pure shot-noise), (n−1)·s²/σ₀² ~ χ²(n−1).

| Quantity | χ² (df=49) | Ratio s²/σ₀² | p (two-sided) |
|----------|-----------|--------------|---------------|
| P(\|00⟩) | 50.14 | 1.023 | 0.856 |
| P(\|11⟩) | 47.52 | 0.970 | 0.933 |

Both p-values are large (≫ 0.05). The observed variance is **fully
consistent** with pure shot-noise. There is **no** statistically
significant evidence for sub-shot-noise determinism.

The distribution of P(\|00⟩) values is normal (Shapiro-Wilk W=0.977,
p=0.42) — no outliers, no drift pattern, a clean dataset.

---

## 4. Why the 10-run preliminary result did not hold

A preceding 10-run measurement (same hardware, same day) gave a variance
ratio of **0.69** — apparently in the T0 direction. Even then this value
was **not significant** (χ² p = 0.57). With 50 runs the ratio has
regressed to **1.02**.

This is the expected behaviour of a **small-sample fluctuation**:
variances estimated from 10 points scatter broadly; a ratio of 0.69 was
still well within the chance range. The larger sample stabilises the
estimate and reveals the true value ≈ 1.0. This underlines why the
original **three** runs (June 2025) were insufficient to support a
variance claim.

---

## 5. Relation to the June 2025 report

The June 2025 hardware validation report cited a run-to-run variance of
0.000248 (three runs, `ibm_brisbane`, Eagle) and interpreted it as
"deterministically reduced" relative to the QM expectation.

> ⚠️ **Superseded:** This repeatability claim is not supported by the
> present 50-run measurement. With sufficient sample size and on newer
> hardware the variance is consistent with ordinary shot-noise (ratio
> 1.02; p = 0.86). The three June 2025 runs were statistically too few to
> support a variance claim. The June report is retained as historical
> record; for repeatability the present finding holds.

What the June report **confirms**: the high Bell fidelity and the
runnability of T0 circuits on production hardware. Fidelity here is even
better (98.76 % vs. 97.17 %), consistent with Heron r2 being a newer,
lower-error generation than the 2025 Eagle.

---

## 6. What this test does NOT say about the central ξ-prediction

The central T0 prediction is a deviation of the CHSH value from the
Tsirelson bound of order ξ ≈ 10⁻⁵ (≈ 10 ppm). The current NISQ noise
level (~2–3 %) is about **280×** larger. This Bell-repeatability test was
therefore **never** able to measure the ξ-effect itself — it tested only
the *side-prediction* about repeatability.

The negative repeatability finding leaves the ξ-prediction **untouched**.
It remains untestable with current hardware and requires error-corrected
qubits (sub-ppm precision) or zero-noise extrapolation.

---

## 7. Systematic side-finding: NISQ readout asymmetry

P(\|00⟩) = 0.509 lies significantly **above**, P(\|11⟩) = 0.479
significantly **below** the ideal value 0.5 (t = +5.7, p = 6·10⁻⁷ and
t = −14.0, p = 1·10⁻¹⁸ respectively). This is the known NISQ readout
asymmetry (the state \|0⟩ is measured more reliably than \|1⟩), a
hardware artifact — **not** a T0 effect. Notably, this asymmetry
(~1–2 %) is itself orders of magnitude larger than any predicted ξ-effect,
underscoring the need for error-corrected hardware for the actual test.

---

## 8. Assessment

- **Methodology:** clean. 50/50 runs successful, identical transpilation,
  full job-ID logging, normally distributed data, reproducible via the
  job IDs stored in the CSV.
- **Core hypothesis (repeatability):** not supported. Variance =
  shot-noise.
- **Bell fidelity:** 98.76 %, better than June 2025.
- **ξ-prediction:** untouched, not testable with this method.

A negative finding for a side-prediction, honestly documented, is a
contribution — it delimits what FFGFT can and cannot claim on today's
hardware.

---

## Appendix A: Reproduction

Script: `t0_bell_repeatability_stage1.py` (50 runs, NUM_RUNS=50).
Raw data: `bell_repeatability_2026.csv` (50 rows, all job IDs).
Backend: `ibm_kingston`. Each run is verifiable via its job ID in the
IBM Quantum dashboard.

Independent reproduction explicitly welcome: same script, any IBM Quantum
account, ~3–4 min QPU time for 50 runs.

---

# Appendix B: CHSH Parameter Measurement (Stage 2)

**28 May 2026 · ibm_kingston (Heron r2, 156 qubits)**

## B.1 Setup

The first real CHSH-parameter measurement on hardware in this corpus.
Unlike Bell repeatability (one measurement basis), CHSH uses four angle
settings and computes the S-parameter from correlators.

| Parameter | Value |
|-----------|-------|
| Alice angles | a = 0°, a' = 45° |
| Bob angles | b = 22.5°, b' = −22.5° |
| Measurements | 15 (each 4 settings × 2048 shots) |
| Correlator | E = [N₀₀ − N₀₁ − N₁₀ + N₁₁]/N |
| S combination | S = E(a,b) + E(a,b') + E(a',b) − E(a',b') |
| Job IDs | fully in chsh_stage2_2026.csv (60 jobs) |

## B.2 Result

| Quantity | Value |
|----------|-------|
| **Mean S** | **2.7396 ± 0.0071** |
| Standard deviation | 0.0274 |
| Range (min/max) | 2.6855 / 2.7891 |
| Tsirelson bound 2√2 | 2.8284 |
| Classical bound | 2.0000 |
| Fraction of Tsirelson reached | **96.9 %** |
| Deviation from 2√2 | −3.14 % |
| Mean correlator magnitude | 0.685 (ideal: 0.707) |

## B.3 Assessment

**Bell violation beyond doubt.** S = 2.74 lies **104 σ** above the
classical bound of 2. Local realism is excluded; the entanglement
generated on the device is genuine. At 96.9 % of the Tsirelson bound this
is an excellent result for NISQ hardware.

**The −3.14 % gap is decoherence, not ξ.** The mean correlator magnitude
0.685 instead of the ideal 0.707 corresponds to ~1.5 % gate and readout
error — the known NISQ characteristic. The T0 ξ-effect is ~10⁻⁵
(0.001 %), about **3000× smaller** than the measured gap. This measurement
therefore **cannot** resolve ξ, in full agreement with the known noise
analysis (NISQ ~280× above the ξ-signal).

**What this dataset provides:** the first hardware-measured CHSH value of
this corpus, fully documented with job IDs. It replaces unsubstantiated
CHSH claims of earlier internal documents with a reproducible measured
value: S = 2.74 on Heron r2, ξ-effect below it, not resolvable with
present hardware.

## B.4 Note on the analysis

The first analysis run of the script used a sign combination of the four
correlators that did **not** match the chosen angles and wrongly produced
S ≈ 0. The raw data (all four correlators per measurement) were correctly
measured and stored; correcting the combination to
S = E(a,b) + E(a,b') + E(a',b) − E(a',b') yields, from the **same
hardware data**, the reported value S = 2.7396. No new hardware run was
needed. The corrected script is t0_chsh_stage2.py.

## B.5 Budget

CHSH measurement: 4 min QPU time (60 jobs). Together with the 50-run
Bell measurement (2 min), 6 of 10 min of the 28-day cycle were used.

---

# Appendix C: Cross-Platform Comparison (Kingston vs. Marrakesh)

**28 May 2026 · two Heron r2 devices**

## C.1 Motivation

The CHSH value of Appendix B comes from a single device (Kingston). To
test device-independence, the same measurement (correct sign combination)
was repeated on a second Heron r2 chip: ibm_marrakesh, 10 measurements.

## C.2 Result

| Device | Measurements | Mean S | SE | sd | % Tsirelson | Bell violation |
|--------|--------------|--------|-----|-----|-------------|-----------------|
| ibm_kingston | 15 | 2.7396 | 0.0071 | 0.0274 | 96.9 % | 105 σ |
| ibm_marrakesh | 10 | 2.7016 | 0.0138 | 0.0435 | 95.5 % | 51 σ |
| **pooled** | **25** | **2.7244** | **0.0078** | — | **96.3 %** | — |

## C.3 Statistical comparison

Welch t-test (unequal variances): t = 2.46, **p = 0.028**.

The two devices give **statistically distinguishable** S values
(difference 0.038 ≈ 1.4 % of S). Both are Heron r2, but physically
different chips with their own calibration and noise profile; Marrakesh
was the noisier device on the measurement day (sd 0.043 vs. 0.027).

## C.4 Significance for the ξ-question — the central finding

This is the most informative observation of the whole measurement series:

> Two identical-model Heron r2 chips differ in their measured CHSH value
> by **1.4 %**, purely through calibration and noise differences. The
> sought T0 ξ-effect is ~10⁻⁵ (≈ 0.001 % of S). The **device-to-device
> variation is therefore about 1400× larger than the sought ξ-signal.**

This is a direct, empirical demonstration — not a theoretical estimate —
that the ξ-prediction is in principle not resolvable with present NISQ
hardware. Even perfect statistics on one device would not suffice,
because switching between two nominally identical devices introduces a
multiple of the ξ-effect in variation. The ξ-test requires
error-corrected qubits with sub-ppm, device-stable precision.

## C.5 What was confirmed

- **Bell violation reproduces** clearly on both independent devices
  (105 σ / 51 σ over the classical bound).
- **Heron r2 generation consistently good:** both reach 95–97 % of the
  Tsirelson bound.
- **Device variation dominates** any ξ-effect by ~3 orders of magnitude —
  measured empirically, not estimated.

## C.6 Budget

Marrakesh run: 2 min QPU (10 measurements × 4 settings). Total over both
stages and both devices: 8 of 10 min of the 28-day cycle.
Raw data: chsh_stage2_marrakesh_2026.csv (40 jobs, all IDs).
