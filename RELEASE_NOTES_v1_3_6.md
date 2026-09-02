# Release Notes — v1.3.6 (September 2026)

**DOI:** to be assigned on Zenodo publication — supersedes v1.3.5  
Running corrections: **[2/pdf/190_T0_Korrekturen_En.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_En.pdf)**  
Archived register: **[2/pdf/190_T0_Korrekturen_Archiv_En.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_Archiv_En.pdf)**  
Change log: **[001_FFGFT_Changelog_De.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/001_FFGFT_Changelog_De.md)**  
A-series log: **[A_Serie_Export/A_SERIE_CHANGELOG.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/A_Serie_Export/A_SERIE_CHANGELOG.md)**

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows: all Standard Model
constants follow from a single dimensionless parameter **ξ = 4/30000** on a compact
4D torus T⁴. The foundational relation is **T̃ · m = 1** — intrinsic time and mass
are inversely coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

This release adds Doc. 341 (GF(27) in GALG — algebraic bridge FFGFT↔GALG),
the retrospective marker certification R105 for nine pre-marker-system documents,
and a complete verified Galois bundle covering Docs. 317–341 with 23 check scripts
all passing.

**The focus lies on two areas.**

Doc. 341 closes the algebraic comparison between FFGFT and Doug Matzke's GALG
framework. The central result: Doug's search result "Attempted 6561 with 0 found"
is algebraically necessary — GF(27) cannot appear in G(3) because 13 ∤ |GF(81)*|.
In G(6), elements of order 26 exist and are demonstrated explicitly in GALG blade
notation, directly checkable. The vacuum structure analysis confirms that GALG's
Witt-pair vacuum matches the FFGFT Frobenius separation from Doc. 339.

R105 completes the audit trail for the Galois programme: nine documents written
before the marker system (Docs. 006, 011, 070, 182, 231, 257, 285, 306, 307) are
retrospectively certified [K] or [B] via Doc. 190, so that dependent documents
(336, 338, 339, 340, 341) can treat their results as auditable chain links.

---

## Entry point for new readers

Doc. 205 "FFGFT in Simple Language" (DE+EN, 13–14 pages) remains the recommended
entry point. The single open falsification test is unchanged: m_τ = 1776.97 MeV,
to be decided by Belle II, with no escape route.

## What has not changed

ξ, the foundational relation T̃ · m = 1, and all derivation chains from v1.3.5
are unchanged. R105 specifies what was already operatively practised; it changes
no numerical value.

---

## New document since v1.3.5

### Doc. 341 — GF(27) in GALG: algebraic bridge FFGFT↔GALG (DE+EN)

Central question: can GF(27) structure appear in Doug Matzke's GALG framework
G(6,ℤ₃ℂ), and if so, where?

**Theorem A [B]:** G(3) ≅ M₂(GF(9)) ⊕ M₂(GF(9)) — orders divide 80·3.
Since 13 ∤ |GF(81)*| = 80, order-26 elements are algebraically impossible in G(3).
Doug's "Attempted 6561 with 0 found" is not a search failure — it is a structural
necessity.

**Theorem B [B]:** In G(6) ≅ M₈(GF(9)), elements of order 26 exist.
Explicit construction via the companion matrix of f(x) = x³+2x+1 over GF(3),
which is irreducible and primitive (order 26 = |GF(27)*|). A concrete 5-blade
element in GALG notation is supplied for direct verification:

    X = −(1+i)·(e1∧e2) + (1+i)·(e1∧e2∧e3∧e6) + (1−i)·(e1∧e2∧e5∧e6)
        + (1+i)·(e1∧e4∧e5∧e6) − (e1∧e2∧e3∧e4∧e6);   X^26 = 1, X^13 ≠ 1

Order-26 elements require at least 5 blades; they are absent from sparse
(2–4 blade) elements but appear in ~18–37% of invertible elements with ≥6 blades.

**Theorem C [B]:** GF(27) embeds as a subfield in M_n(GF(9)) if and only if 3 | n.
Since G(3) → n=2 and G(6) → n=8, neither carries GF(27) as a subfield. GF(27)
is present in G(6) as an order structure, not as a subfield.

**Consequence:** α = 1/(137.037) is formulable at the G(3)/GF(9) level; the
lepton mass layer requires G(6) with order-26 elements. Doug's statement "not
working on mass" and his search result are both consistent with this separation.

**Vacuum structure analysis [B]:** GALG's Witt-pair vacuum structure under ℤ₃
matches the FFGFT Frobenius separation from Doc. 339 exactly:
- Even vacua [0,2,4]: ℤ₃ fixed points (massive sector analogue)
- Odd vacua [1,3,5]: one ℤ₃ three-orbit (gluon sector analogue)
- Bilaterals ap_i·ap_j shift N-sector by ±1 mod 3 (gluon role)

Verification scripts: `pruef_341_gf27_in_galg.py` (6/6 [B] assertions),
`pruef_341_vakuum_witt_z3.py` (7/7 [B] assertions).

→ [DE](2/pdf/341_GF27_GALG_FFGFT_De.pdf) · [EN](2/pdf/341_GF27_GALG_FFGFT_En.pdf)

---

## Marker system — specification additions

### R105 — Retrospective marker certification for pre-marker-system documents
### (1 September 2026)

Nine documents written before the introduction of the marker system (A010) carry
no markers of their own but serve as necessary chain links for the Galois programme
(Docs. 336, 338, 339, 340, 341). Retrospective status:

| Document | Content | Status |
|----------|---------|--------|
| Doc. 006 | Particle masses, winding numbers r_i, p_i | **[K]** |
| Doc. 011 | Fine structure α, E₀, fundamental relations | **[K]** |
| Doc. 070 | Mathematical structure: K_frak cancels in ratios | **[B]** |
| Doc. 182 | Maximum universe scale from ξ | **[K]** |
| Doc. 231 | Hilbert space extension, L² structure | **[B]** |
| Doc. 257 | Information unit, bit-energy scale | **[K]** |
| Doc. 285 | FFGFT-HLV dimension bridge | **[K]** |
| Doc. 306 | Native time-energy reciprocity from T̃·m=1 | **[K]** |
| Doc. 307 | Time in state space | **[K]** |

Dependent documents may treat these results as certified chain links by citing
R105, without modifying the original documents.

---

## Complete marker register (as of v1.3.6)

| Marker | Meaning | Introduced |
|--------|---------|------------|
| [SETZUNG] | Declared starting point or axiom | A010 |
| [B] | Algebraically/mathematically proved from declared foundations | A010 |
| [K] | Derived from ξ, numerically verified, closure condition satisfied | A010 |
| [S] | Plausibility sketch, not yet fully worked out | A010 |
| [Q] | Corpus-external primary source or measured/proven value | A271, Doc. 315+ |
| [H] | Open research question | A270 |
| [X] | Excluded at theorem level / closed negative | Doc. 316+ |
| [E] | Context-dependent: external physics as basis (Doc. 328) or externally failed test (Doc. 330) | Doc. 328+ |

---

## Corrections — R104 to R105

**R104** (Aug. 2026): v = m_e/((4/3)ξ^(3/2)) = 248.3 GeV [K]; G_F [K];
τ_n [K]; Δm [K]: QCD contribution from r_d, r_u, r_e (Doc. 006); EM contribution
from α = 27/3700 (R102), Λ_QCD = ħc/fm (Doc. 319), 5 = |A₅:A₄| (Doc. 340),
6 = r_u (Doc. 006). Check script: pruef_319 (7/7).

**R105** (1 Sept. 2026): Retrospective [K]/[B] certification for Docs. 006, 011,
070, 182, 231, 257, 285, 306, 307. Pre-marker-system documents, derivations
internally consistent. See marker specification section above.

---

## Galois bundle — complete verified package

All documents and scripts of the Galois programme are collected in the Galois
bundle (v2, SHA-256:
`a946e9871ea5a38808b54b83dfcc8b250a1f75a1aba2d393cdcfef0219af0354`).

**23/23 check scripts passed, 0 failures.**

Documents: 317, 321, 323, 324, 336, 337, 338, 339, 340, 341 (Galois core)
+ 006, 011, 070, 182, 231, 257, 285, 306, 307, 332, 333 (dependency chain, R105)

Scripts by folder:

| Folder | Scripts | Assertions |
|--------|---------|------------|
| Dok320_321_322_Skripte | pruef_324–329, pruef_341, pruef_342 | all OK |
| Dok328_Skripte | pruef_328_4, pruef_328_5 | all OK |
| Dok330_Skripte | pruef_330_1, pruef_330_2 | all OK |
| Dok332_Skripte | pruef_332_krueger, pruef_339, pruef_340, pruef_340b, sicc_kappa | all OK |
| Dok338_Skripte | pruef_330_galois, pruef_331_xi, pruef_332_alpha | all OK |
| Dok341_Skripte | pruef_341_gf27, pruef_341_vakuum | all OK |
| Dok342_Skripte | pruef_342_vakuum | all OK |

---

## Bridges closed in this release

| Bridge | before | after | Doc. |
|--------|--------|-------|------|
| GF(27) absence in GALG G(3) algebraically proved | — | **[B]** | 341 |
| GF(27) order structure present in GALG G(6) | — | **[B]** | 341 |
| GALG vacuum = FFGFT Frobenius separation | — | **[B]** | 341 |
| Pre-marker-system documents auditable | unverified | **R105** | 190 |

## Remaining open bridges

| Bridge | Status |
|--------|--------|
| Δm²₃₂ mixing term F₅–F₇ | [S] |
| 2-loop corrections to α_s(M_Z) | [S] |
| m_Pl and α_em(M_Z) from ξ | [S] |
| Quark/hadron sector | open (Doc. 318, R76) |
| Greybody factors; fixed-point back-reaction | [S] (R85) |
| Forward derivation of cosmic exponent 41/4 (P20) | open |
| CMB peaks {1,6,14,26}; \|n\|²=30 | open (P29/P31) |
| D₄ geometric connection to Kissing(D₄) = 24 | [S] (Doc. 339) |
| GF(27) as subfield in G(6) | structurally impossible (Doc. 341, Theorem C) |

---

## Verification scripts (new in this release)

`python/Dok341_Skripte/`:
- `pruef_341_gf27_in_galg.py` — GF(27) structure in GALG G(3)/G(6); Theorems A–C; order-26 elements (6 [B] assertions)
- `pruef_341_vakuum_witt_z3.py` — Witt-pair vacuum, triality, ℤ₃ separation, bilaterals (7 [B] assertions)

`python/Dok342_Skripte/`:
- `pruef_342_vakuum_witt_z3.py` — independent verification of vacuum structure (7 [B] assertions)

---

## License

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
