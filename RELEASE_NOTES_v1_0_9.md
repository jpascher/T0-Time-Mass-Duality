# T0 Theory v1.0.9 – Scramblon Bridge & Cross-Platform Validation

**Release Date:** 2026-02-26  
**Version:** 1.0.9  
**DOI (unchanged):** 10.5281/zenodo.17522475

---

## 1. Overview

This release adds a new document (Doc 148) presenting a quantitative comparison between the T0 damping factor and the scramblon physics of Li, Zhou, Zhang et al. (Phys. Rev. Lett. **136**, 060403, 2026), who achieved the first experimental extraction of the quantum Lyapunov exponent in a many-body system. The analysis demonstrates that T0's parameter-free geometric correction operates at the same order of magnitude (~10⁻⁴) as the scramblon corrections, identifies a testable ln(N) scaling prediction, and validates cross-platform consistency from NMR spin systems to IBM quantum processors.

---

## 2. New Document: T0 Projection onto Scramblon Physics (Doc 148)

### 2.1 Files

- **German:** `2/pdf/148_T0_scramblons_De.pdf`
- **English:** `2/pdf/148_T0_scramblons_En.pdf`
- **Chapter files:** `148_T0_scramblons_De_ch.tex` / `148_T0_scramblons_En_ch.tex`

### 2.2 Motivation

Li et al. (2026) measured the out-of-time-ordered correlator (OTOC) in a solid-state NMR system (powdered adamantane, 16 proton spins per molecule, 9.4 T) and validated scramblon theory — a universal framework for quantum information scrambling. Their central achievement is the first experimental extraction of the quantum Lyapunov exponent κ, using a complex fitting ansatz with 4+ free parameters per Hamiltonian.

### 2.3 Key Results

**T0 projection onto the NMR number space:**

The same universal T0 damping factor D(N) = exp(−ξ·ln(N)/D_f) that describes CHSH corrections in IBM quantum processors also applies to the NMR spin system:

| System | N | D(N) | 1−D(N) (ppm) | CHSH (T0) |
|--------|---|------|---------------|-----------|
| Adamantane NMR (molecule) | 16 | 0.99987678 | 123.2 | 2.828079 |
| Adamantane NMR (cluster) | 64 | 0.99981517 | 184.8 | 2.827904 |
| IBM Brisbane (73 qubits) | 73 | 0.99980932 | 190.7 | 2.827888 |
| IBM Sherbrooke (127 qubits) | 127 | 0.99978472 | 215.3 | 2.827818 |

**Why Li et al. do not separately observe the T0 effect:**
1. The T0 correction (~1.2 × 10⁻⁴) lies at the edge of their reported 95% confidence intervals (~10⁻⁴)
2. Their 4+ parameter fitting ansatz can absorb a static correction of this magnitude
3. They did not systematically vary the effective cluster size N

### 2.4 Complementarity Thesis

The document establishes that scramblons and T0 are **complementary, not contradictory**:

| Property | Scramblon Theory | T0 Projection |
|----------|-----------------|---------------|
| Foundation | Effective field theory | Geometric correction |
| Free parameters | 4+ per Hamiltonian | 0 (from ξ alone) |
| Describes | Dynamics (chaos rate) | Geometry (fundamental limit) |
| Time-dependent? | Yes (exponential) | No (static correction) |
| Platform | NMR-specific | Universal (cross-platform) |
| Expression | Multi-step fitting | D(N) = exp(−ξ·ln(N)/D_f) [1 line] |

### 2.5 Testable Prediction

**Central prediction:** After complete scramblon error correction (extrapolation to the error-free OTOC), a residuum should remain that scales logarithmically with the cluster size N:

$$R(N) \approx \frac{\xi \cdot \ln(N)}{D_f}$$

- R(16) ≈ 1.23 × 10⁻⁴
- R(100) ≈ 2.05 × 10⁻⁴

This **ln(N) scaling** distinguishes T0 from all standard error models, which typically scale as 1/N or exp(−N). The prediction is testable using publicly available raw data (Zenodo DOI: 10.5281/zenodo.16142455).

### 2.6 Lyapunov Exponent Correction

T0 predicts that the experimentally extracted Lyapunov exponent receives a system-size correction:

$$\kappa_{\text{eff}} = \kappa_{\text{bare}} \cdot N^{-\xi/D_f}$$

with universal exponent −ξ/D_f = −4.445 × 10⁻⁵. For N=16: correction ~123 ppm; for N=10000: ~409 ppm.

---

## 3. README Updates

Both `README.md` and `README_de.md` have been updated:

- New "February 2026" section for the T0-Scramblon bridge analysis (Doc 148)
- Links to both language versions of the new document

---

## 4. Context: Connection to Existing Documents

Doc 148 builds directly on:
- **Doc 147** (Quantum Computing in T0): IBM Brisbane/Sherbrooke CHSH validation data
- **Doc 034** (T0 QM Optimization): Geometric formalism for qubit operations
- **Doc 157** (Arrow of Time): Conceptual overlap with time-reversal and scrambling

The scramblon paper (Li et al. 2026) provides independent experimental validation of exponential dynamics in many-body systems — the same regime where T0's ξ-damping operates.

---

## 5. Impact on Existing Predictions

| Prediction | Status | Note |
|-----------|--------|------|
| CHSH T0 (73 qubits) | Unchanged | 2.827888 |
| CHSH T0 (127 qubits) | Unchanged | 2.827818 |
| ξ = 4/30000 | Unchanged | Universal parameter |
| D_f = 3 − ξ | Unchanged | Fractal dimension |
| **NEW:** NMR T0 correction (N=16) | New | 1.23 × 10⁻⁴ |
| **NEW:** ln(N) residuum prediction | New | Testable with Zenodo data |
| **NEW:** Lyapunov correction | New | κ_eff = κ_bare · N^(−ξ/D_f) |

No existing predictions, derivations, or numerical results have been changed. Doc 148 extends T0's applicability to NMR scrambling experiments without modifying any prior results.
