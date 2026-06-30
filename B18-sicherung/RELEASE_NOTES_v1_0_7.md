# T0 Theory v1.0.7 – g-2 Koide Bridge & Arrow of Time

**Release Date:** 2026-02-21  
**Version:** 1.0.7  
**DOI (unchanged):** 10.5281/zenodo.17522475

---

## 1. Overview

This release contains two major additions: a new document on the arrow of time (Doc 157) and a substantial revision of the g-2 anomalous magnetic moment document (Doc 018, Rev. 12). The g-2 update integrates the Koide-to-g-2 bridge formula from the companion document Doc 158, corrects experimental input values, and adds an α-derivation and SM circularity analysis. The tau prediction changes from 1.277×10⁻³ to 1.282×10⁻³.

---

## 2. New Document: Arrow of Time (Doc 157)

### 2.1 Files

- **German:** `2/pdf/157_Zeitpfeil_De.pdf`  
- **English:** `2/pdf/157_Zeitpfeil_En.pdf`

### 2.2 Content

Why is time directed? All fundamental equations (Newton, Maxwell, Schrödinger, Dirac, Einstein) are time-reversal invariant — yet we experience directed time. T0 theory resolves this through four geometric arguments:

1. **Algebraic:** T·m = const with m > 0 forces T > 0 everywhere.
2. **Topological:** Torus winding modes define a protected direction.
3. **Fractal:** D_f = 3 − ξ < 3 breaks mirror symmetry.
4. **Emergent:** Time direction arises irreversibly from symmetry breaking.

The document also clarifies antimatter: positrons have positive mass, positive T, and reversed charge (C symmetry), not reversed time.

---

## 3. Major Update: g-2 Document (Doc 018, Rev. 12)

### 3.1 Files

- **German:** `2/pdf/018_T0_Anomale-g2-10_De.pdf` (wrapper/PDF name unchanged)
- **English:** `2/pdf/018_T0_Anomale-g2-10_En.pdf`
- **Chapter files:** `018_T0_Anomale-g2-12_De_ch.tex` / `018_T0_Anomale-g2-12_En_ch.tex`

### 3.2 New: Koide-to-g-2 Bridge Formula

The central addition is the bridge formula connecting experimentally known mass ratios directly to g-2 ratio predictions:

$$\frac{\Delta a(\tau-e)}{\Delta a(\mu-e)} = \frac{144}{125} \cdot \frac{m_\tau}{m_\mu}$$

This follows from the common factor f^(1/3) appearing in both the mass hierarchy (m_τ/m_μ = (125/144)·f^(1/3)) and the g-2 hierarchy (Δa(τ-e)/Δa(μ-e) = f^(1/3)). The parameter f cancels out completely.

### 3.3 New Section: "The Bridge Formula: Three Numbers, One Prediction"

The tau prediction requires only:
1. a_e, a_μ (measured) → Δa(μ-e) = 6.269 × 10⁻⁶
2. m_τ/m_μ = 16.817 (measured)
3. The rational factor 144/125 from T0 geometry

Result: **a_τ = 1.282 × 10⁻³** (previously 1.277 with rounded inputs).

No α, no k_eff, no K_frak, no perturbation theory.

### 3.4 Correction: 1/3-Step Applies Only to μ→τ

The mass exponents p_e = 3/2, p_μ = 1, p_τ = 2/3 have step sizes:
- Δp(μ→τ) = 1/3 = 1/D (torus geometry)
- Δp(e→μ) = 1/2 (electron special status near E₀)

The bridge formula uses only the μ-τ transition where the 1/3 structure holds exactly. All equations updated with μ→τ subscripts.

### 3.5 New: α Derivation and SM Circularity Argument

- **T0 derives α:** α = ξ·E₀² with E₀ = 7.398 MeV → 1/α = 137.035 (0.0005% from experiment).
- **SM circularity:** The SM extracts α from the a_e measurement, then uses it to compute a_e — a circular fit, not an independent prediction. T0 derives α independently from ξ.
- **Where theories diverge:** Not at e or μ, but at **tau**: T0 predicts 1.282×10⁻³, SM predicts 1.177×10⁻³ — a 9% difference, testable at Belle II.

### 3.6 Corrected Experimental Values

| Quantity | Old (Rev. 11) | New (Rev. 12) |
|----------|--------------|---------------|
| Δa(μ-e) | 6.000 × 10⁻⁶ | 6.269 × 10⁻⁶ |
| a_τ (from ratio) | 1.277 × 10⁻³ | 1.282 × 10⁻³ |
| SM comparison | 6–9% | 9% |

---

## 4. New Companion Document: Koide-to-g-2 Bridge (Doc 158)

### 4.1 Files

- **German:** `2/pdf/158_T0_Koide-zu-g2-1_De.pdf`
- **English:** `2/pdf/158_T0_Koide-zu-g2-1_En.pdf`

### 4.2 Content

A focused, standalone derivation of the Koide-to-g-2 connection:

1. The Koide formula (Q = 2/3 at 0.001%) and its T0 explanation via exponent structure.
2. The same 1/3-step in both mass and g-2 hierarchies.
3. The bridge formula: mass ratios → g-2 ratios.
4. Tau prediction: 1.281 × 10⁻³ (bridge) / 1.245 × 10⁻³ (T0-internal).
5. SM comparison: ratio 2.80 (SM) vs 19.4 (T0) — factor 7.
6. Feynman diagram count analysis (12,672 diagrams for SM 5th-order a_e).

The key content of Doc 158 has been integrated into Doc 018 Rev. 12.

---

## 5. README Updates

Both `README.md` and `README_de.md` have been updated:

- New "February 2026" section for g-2 Koide bridge update.
- Updated document list entry for Doc 018 with Rev. 12 description.
- Arrow of Time entry (Doc 157) already present from prior update.

---

## 6. Impact on Existing Predictions

| Prediction | Before | After | Change |
|-----------|--------|-------|--------|
| a_τ (ratio method) | 1.277 × 10⁻³ | 1.282 × 10⁻³ | Corrected experimental inputs |
| a_τ (T0-internal) | 1.245 × 10⁻³ | 1.245 × 10⁻³ | Unchanged |
| a_τ (SM) | 1.177 × 10⁻³ | 1.177 × 10⁻³ | Unchanged |
| T0 vs SM difference | 6–9% | 9% | Now single clear value |
| Δp(e→μ) | 1/3 (implied) | 1/2 (corrected) | Important clarification |
| 1/α from T0 | not stated | 137.035 | New derivation |

No other predictions, derivations, or numerical results have been changed.
