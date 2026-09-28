# Release Notes — v1.4.1 (28 September 2026)

**DOI:** assigned upon Zenodo release — supersedes v1.4.0 (https://doi.org/10.5281/zenodo.22790191)
Running corrections: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Change log: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows: all Standard Model
constants follow from a single dimensionless parameter **ξ = 4/30000** on a compact
4D torus T⁴/ℤ₃. The foundational relation is **T̃ · m = 1** — intrinsic time and mass
are inversely coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

This release collects the work from 18 to 28 September 2026: thirteen new documents
(Docs. 366–378), three new popular-science books, and seven register entries
(R121–R127). The main themes are the lepton masses via the icosahedron (Koide phase
θ = 2/9 as a matrix element), the electroweak boson spectrum from v (Weinberg angle 2/9,
trace rule for the Higgs mass), and the bridges to other frameworks, in particular
Observer Patch Holography (OPH). The foundational relation and ξ are unchanged;
corrections to older documents are recorded in Doc. 190 (see "Corrections").

---

## New books

### *The Number That Nobody Explained / Die Zahl, die niemand erklärte*
*(Icosahedron book, EN/DE, 73/75 pp., 6×9 in, prologue, 8 chapters, appendix)*

**Sources:** https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/kdp/IKO_Ikosaeder_Leptonmassen/

A popular-science account of the findings in Docs. 285, 293, 338, 352, 364 and
367–370: why the Koide formula with θ = 2/9 works, how three (ℤ₃) and five (φ) meet in
the icosahedron, and where the open edge lies. No new FFGFT result.

### *Fields in FFGFT / Felder in der FFGFT*
*(Book edition of Doc. 366, EN/DE, 38 pp. each, 6×9 in)*

**Sources:** https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/kdp/366_Feldstruktur_FFGFT/

Energy, flux and geometry, using the Goubau line as the example; the Poynting and Ohm
views as reciprocal projections, analogous to time-mass duality.

### *Dark Matter — an Illusion / Dunkle Materie — eine Illusion*
*(EN/DE, 18/20 pp., 6×9 in, 10 chapters)*

**Sources:** `2/Sources/wr_narrativ/FFGFT_Dunkle_Materie_De/En.tex`, PDFs in `2/Sources/wr_narrativ/pdf/`

Rotation curves from T̃·m = 1 in the inertial regime (a ≪ a₀) without dark matter as a
substance; the Bullet Cluster and gravitational lensing are assessed critically,
explicitly without claiming a conclusive proof.

---

## New documents (Docs. 366–378)

| Doc. | Title | Pages DE/EN | Verification script |
|------|-------|-------------|---------------------|
| 366 | Fields in FFGFT: Energy, Flux and Geometry | 26/25 | 14/14 |
| 367 | Why θ = p₀ = 2/9 — probability and phase as two readings of one quotient | 9/9 | 18/18 |
| 368 | From p₀, p₁, p₂ to lepton masses — φ skeleton and Galois correction factors | 8/8 | 18/18 |
| 369 | Four routes to the lepton masses — an inventory | 9/9 | 25/25 |
| 370 | Why the icosahedron — three, five and non-commutation | 10/9 | — (explanatory document) |
| 371 | The factor 4/3 — sphere volume, Casimir operators, electromagnetic mass, (3,4,5) | 12/12 | 28/28 |
| 372 | The matrix-element principle and its reach | 12/12 | 45/45 |
| 373 | The Yukawa mechanism as a consequence of T̃·m = 1 | 11/11 | 35/35 |
| 374 | Common anchor — bridge equations to OPH | 9/8 | 30/30 |
| 375 | The hierarchy v/E_P — FFGFT and OPH compared | 6/6 | 11/11 |
| 376 | The coefficient 8π and the status of Issue 740 | 6/6 | 9/9 |
| 377 | Interfaces of FFGFT with other frameworks | 6/6 | 20/20 |
| 378 | Peer review under present-day conditions | 12/12 | 25/25 |

Verification scripts in `2/python/DokNNN_Skripte/`.

---

## Key new results

### Koide phase as a ℤ₃ quotient [B]/[K] (Docs. 367, 370)
The Koide angle θ and the icosahedral transition probability p₀ = |⟨v₀|R₅ vₑ⟩|² are the
same quotient 2/3² = (non-trivial ℤ₃ modes)/(ℤ₃ order)². The relation θ = |A|² has the
structure of the Born rule. The full matrix |⟨v_j|R₅|v_k⟩|² is doubly stochastic; the row
of the symmetric mode is (5, 2, 2)/9, trace R₅ = φ. The icosahedron acts on the unrolled
ℝ³, not on the compact T⁴ (5 ∤ 1152); the five enters as a phase ζ₅ ∈ GF(81).

### φ skeleton of the lepton masses [B] (Doc. 368)
New exact identities: p₁/p₂ = φ⁸, p₀/p₂ = 2φ⁴, p₁/p₀ = φ⁴/2.
Approximations m_τ/m_e ≈ 74·φ⁸ (0.03%) and m_μ/m_e ≈ 30·φ⁴ (0.56%) [K] — the first link
between Doc. 293 and Doc. 338.

### Four routes to the lepton masses (Doc. 369)
T0 ladder, Koide with θ = 2/9, Galois GF(3ⁿ) and the φ skeleton compared directly against
PDG 2024. Two accuracy classes: percent and 10⁻³ %. FFGFT predicts the shape of the
spectrum without parameters (dimensionless ratios); absolute values in MeV need one
declared anchor. A second reading of the fractal correction without QED (R121).

### Matrix-element principle [B]/[K] (Doc. 372)
In the ℤ₃ mode basis, A₅ generates exactly eight squared matrix elements, all with
denominator 9. Consequences: on-shell Weinberg angle 1 − M_W²/M_Z² = 2/9, prediction
M_W = M_Z·√(7/9) = 80.420 GeV [K]; atmospheric mixing sin²θ₂₃ ∈ {4/9, 5/9}, maximal mixing
excluded [K]. Negative results stated: θ₁₂, θ₁₃ and α_s are not in the set of eight [X].

### Yukawa mechanism and trace rule [B]/[K] (Doc. 373)
y_i = m_i/v follows from T̃·m = 1 under the fluctuation v → v + h(x), for all fermions at
once [B]. The Higgs particle is the vibration quantum of the lattice scale.
Trace rule M_W² + M_Z² + m_h² = v²/2 to 0.45% [K]; together with 2/9 and 11/8 this gives
M_Z²/v² = 288/2113 and hence the electroweak boson spectrum from v alone at tree level
(0.17–0.31%). Galois chain M_Z : m_h : m_t = 1 : 11/8 : (11/8)² [K].
Inventory of the particle zoo (as of 21 September 2026).

### The factor 4/3 [B]/[E] (Doc. 371)
The factor 4/3 in the electromagnetic electron mass (Abraham/Lorentz) is an effect of
three-dimensionality, 4/3 = 2·(1 − 1/3). C₂(SU(2)) = 3/4 and C₂(SU(3)) = 4/3 are
reciprocals; N = 2 is the only case with C₂(N)·C₂(N+1) = 1 [B].

### Bridge to Observer Patch Holography [B]/[K] (Docs. 374–376)
Bridge equations B1–B4: cell energy = bit energy E_bit = ħc/L, collapse threshold at the
cell edge, cell clock T̃ = √P·t_P, L_cell/L₀ = √P/ξ ≈ 9578. FFGFT's own chain
ξ → G → ℓ_P → E_P: v/E_P = 2.0389·10⁻¹⁷ (+1.10%, fully attributed to the bare residual of
the lepton ladder). The coefficient 8π is derived on the OPH side; the statement that
Issue 740 was closed has been withdrawn (R124).

### Interface overview (Doc. 377)
Eleven frameworks with comparison and bridge documents, seven overlapping quantities with
their derivation routes. Only α⁻¹ and v/E_P are quantified by more than one framework;
the hadron sector appears in no comparison.

### Peer review under present-day conditions (Doc. 378)
A methodological inventory: what the FFGFT bookkeeping (status markers, Doc. 190,
verification scripts, negative results), IPI audit practice and Dot Theory governance
already provide for a review framework; ten building blocks and graded review depth.
No physical claims.

---

## Corrections (Doc. 190, R121–R127)

| Entry | Concerns | Content |
|-------|----------|---------|
| R121 | Doc. 352 §10, 369 | Origin of ε_i: second reading without a QED bridge; R113 bridge needed only in reading A |
| R122 | Docs. 041, 005; 372, 373 | Higgs mass and Λ_QCD in Docs. 041/005 not tenable [X]; candidates via Galois chain and trace rule (Doc. 373) |
| R123 | Doc. 160 | K_frak naming conflict: in Doc. 160 to be read as the hadronic factor K_had |
| R124 | Doc. 374 | Withdrawal of the Issue 740 statement; Doc. 374 corrected directly |
| R125 | Docs. 085, 176, 179, 186 | Literature references and one standard statement in the photonics documents |
| R126 | Doc. 230 | Cylinder representation of the qubit: placement in the literature, justification of Born statistics |
| R127 | Docs. 043, 044, 261 | α = 1 is not a choice of units [X]; α is derived dimensionlessly from ξ |

---

## Open bridges (as of R127)

| Bridge | Status |
|--------|--------|
| τ_μ directly from FFGFT (without G_F and v) | [S] (R112, Doc. 351) |
| Why the rational approximation carries the GF(3ⁿ) winding numbers | [S] (Doc. 369 §4, R121) |
| Koide amplitude d/c = √2 from the geometry | [S] (Doc. 352 §8) |
| Hadronic factor K_had | [S] (R123) |
| Λ_QCD from ξ | [X] (R122, Doc. 372) |
| Higgs potential V(h) | [S] (Doc. 373) |
| m_Pl and α_em(M_Z) from ξ | [S] |
| Quark/hadron sector | open (Doc. 318, R76) |
| CMB peaks {1,6,14,26}; \|n\|²=30 | open (P29/P31) |
| Icosahedral phases (GF(81)) and Galois orders (GF(3ⁿ)): common root | [S] (Doc. 370) |

## Entry point for new readers
Doc. 205 "FFGFT in Simple Language" (DE+EN, 13–14 pp.) remains the recommended entry
point for the physics. *Quantum Mechanics is Deterministic* remains the recommended entry
point for the quantum mechanics and quantum computing perspective. The icosahedron book
*The Number That Nobody Explained* is the recommended entry point for the lepton masses.

## What has not changed
ξ and T̃·m = 1 are unchanged. All results from v1.4.0 remain valid unless refined or
corrected by R121–R127.
All derivation chains from v1.3.6 are unchanged.
