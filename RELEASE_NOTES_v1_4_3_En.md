# Release Notes — v1.4.3 (2 October 2026)

**DOI:** assigned upon Zenodo release — supersedes v1.4.2
Running corrections: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Change log: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**
Summary of the corpus: **[2/pdf/384_FFGFT_Kurzfassung_En.pdf](2/pdf/384_FFGFT_Kurzfassung_En.pdf)** (also as [HTML](2/html/384_FFGFT_Kurzfassung_En.html))

**FFGFT — Fundamental Fractal-Geometric Field Theory** is first and foremost a
ratio-based theory. In natural units with α = 1 there is a single dimensionless
parameter **ξ = 4/30000** on a compact 4D torus T⁴/ℤ₃; the foundational relation is
**T̃ · m = 1** — intrinsic time and mass are inversely coupled. Only the translation
into SI needs a measured value as anchor.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

This release collects the work from 28 September to 2 October 2026. Its centre is the
**complete recalculation of the corpus**: all documents up to No. 300 and the A series
were recalculated; about 235 documents now carry a correction box, and every corrected
passage has a dated note with the previous value (R133, R140, R142). In addition there
are **nine new documents (Docs. 379–387)**, among them the **summary of the entire
corpus (Doc. 384)**, the **A series v1.5** with the new document **A125 (φ skeleton)**,
and twenty register entries (R128–R147).

The recalculation has withdrawn several earlier claims; they are collected in Doc. 384
in the section "What no longer holds". The foundational relation and ξ are unchanged.

---

## The recalculation (R133–R146)

From 29 September to 1 October 2026 the corpus was recalculated. Since R133 the source
documents themselves are corrected instead of recording the corrections only in the
register. The main consequences for the classification:

- **α, E₀ and K_frak (R135):** the agreement of the SI value of α is a property of the
  chosen anchor, not an independent prediction. The value K_frak = 74/75 remains
  confirmed; a residual of 1.7·10⁻⁴ remains between the factor 0.98650 required by α
  and 74/75.
- **Precision tables (R138):** tables of older documents in which prefactors had been
  fitted to measured values are not evidence.
- **Gravitational constant (R132, R141):** calculations corrected; the agreement with
  CODATA to 0.003 % arises only with the residual of the one-anchor chain in C_conv
  and is not precision evidence in its own right.
- **Quantum mechanics (R142, R143):** the Bell violation remains; a ξ effect
  measurable with present-day hardware does not exist. Unsupported CHSH data and a ξ
  fitted to them have been removed.
- **Cosmos (R136, R137):** the Casimir-CMB connection is an identity, not measurement
  evidence; CMB temperature, redshift, H₀ and Λ are classified more precisely.
- **Form of K_frak (R139):** the form (additive 1 − 100ξ or multiplicative) is open
  again; the icosahedral leak is not compatible with δ*.
- **Refinements (R144–R146):** black holes (R93/R94), self-adjointness of F̂ only on
  the ℤ₃-invariant sector, Gell-Mann–Nishijima not fully closed (hypercharge of the
  charged leptons open).

---

## New documents (Docs. 379–387)

| Doc. | Title | Pages De/En | Verification script |
|------|-------|-------------|---------------------|
| 379 | The acoustic plenum and the photon — Lien (2026) as a case study | 8/8 | 20/20 |
| 380 | Why D₄ — specificity of the carrier against fitted comparison lattices | 7/7 | 13/13 |
| 381 | The running recursion summed exactly | 7/7 | 14/14 |
| 382 | Muon g−2: status 2025 | 8/8 | 21/21 |
| 383 | Masses and Planck scale without v — one chain, one anchor | 8/8 | 20/20 |
| 384 | FFGFT in brief — foundations, results and status after the calculation review | 20/19 | 93/93 |
| 385 | The Higgs–vacuum route to ξ | 8/8 | 17/17 |
| 386 | Where α hides — charge unit, two spheres and ξ as an area | 8/8 | 25/25 |
| 387 | The deviations at a glance — ratios, SI translation and correction quantities | 8/8 | 27/27 |

Verification scripts in `2/python/DokNNN_Skripte/`.

---

## Main new results

### Summary of the corpus (Doc. 384)
The whole corpus (Docs. 001–387, A series) as of the state after the recalculation,
built up from the basic form: first the ratios in natural units, then the translation
into SI. For every result the formula, numerical value, comparison value, status and
carrying documents; in addition tables of the testable statements, a status balance,
the open bridges and a section "What no longer holds". Reformatted with coloured status
markers and boxes for the core formulas; also available as a stand-alone HTML page.
Recommended entry point to the current state.

### φ skeleton of the lepton masses [B]/[K] (Doc. 384, A125)
The weights of the icosahedral fivefold rotation stand exactly as p₁/p₂ = φ⁸ and
p₀/p₂ = 2φ⁴ [B]. With this, **m_τ/m_e = (74 + 1/45)·φ⁸ = 3477.469** agrees with the
measured value 3477.37 ± 0.18 to 3·10⁻⁵ (0.6σ) [K] — as precise as the Koide formula,
as a pure ratio without an anchor. The factors 74 and 1/45 are observed, not derived
[S]; the 37 in 74 demonstrably does not come from the icosahedron. For m_μ/m_e there
is no φ route at this level.

### Where α hides [B] (Doc. 386)
With ħ = c = ε₀ = 1 and α = 1 one has e = √(4π); α moves into the charge unit,
α = (e_hist/e_geo)² = r_e/λ_C, the ratio of the Coulomb and Compton spheres of the
electron. In the basic form the bridge reads ξE₀² = 1, i.e. E₀² = 1/ξ = 7500, and
geometrically ξ = λ_e·λ_μ is the area spanned by the Compton spheres of electron and
muon. The fractal correction enters only in the SI translation; the MeV is a unit of
the SI chain [Q].

### One chain, one anchor (Doc. 383)
v is an intermediate quantity: v/E_P = ξ⁴/(5π) and m_i/E_P = r_i/(5π)·ξ^{p_i+4} [B].
With a single measured value as anchor, E_P, G, ℓ_P and L₀ follow; the spread depending
on the choice of anchor is the known residual of the ladder [K]. The factor 10 in the
formula for v is fitted to the measured value (Doc. 387).

### The deviations at a glance (Doc. 387)
All deviations with their measurement uncertainties in one place: the ratios of the
basic form, the SI translation, β_T (already in the earliest documents with α = 1 next
to β_T = 1), the variants of K_frak (74/75 as the only one with an integer number of
turns) and the factor 10 (with the bare v of the ladder it becomes 10·K_frak ≈ π² [S]).
Measurement precision contributes only minimally for leptons, α and v/E_P.

### Higgs–vacuum route (Doc. 385)
Origin of the formula ξ_EFT = m_h²/(64π³v²) = 1.30·10⁻⁴ from the vacuum formula of
2025; written out it is ξ_EFT·α, with α = 1 the same expression [B]. Against 4/30000
about −2.3 % (PDG 2024): a consistency check to within a few per cent, not an exact
derivation.

### Recursion, carrier and g−2 (Docs. 380–382)
Telescoping product of the recursion exact [B], rotation number 74/75; among the
comparison carriers tested, D₄ has the lowest lattice energy [K] but remains a
motivated choice [S]. Muon g−2 as of 2025: the anomaly has shrunk to about 0.6σ, a
fixed FFGFT addition Δa_μ = 251·10⁻¹¹ is superseded [X]; the ratio line for a_τ
remains.

---

## A series v1.5

- **New: A125 — The φ skeleton: from the weights to the mass ratios** (De/En, 6 pages
  each, verification script 32/32). Closes the edge left open in A120 between the
  icosahedral weights and the mass ratios, as far as the corpus closes it today;
  incorporates Docs. 364 and 367–370.
- **A120:** notes (the leak (7−3φ)/9 is not compatible with δ*, R139; reference to
  A125). A010, A230, A250, README and CHANGELOG updated; now 49 documents.
- Since the recalculation the A series carries dated notes in the text (R140).

---

## Notation f (R147)

The symbol f carries four meanings in the corpus: the base winding number f = 1/ξ, a
frequency, the structure factor f(n,l,j) and further functions. More than 80 documents
(De/En) now carry a note at the first occurrence that f is not a frequency there. In
natural units the base winding number is only another reading of the duality T·m = 1
and, as a dimensionless ratio, cannot be set to 1 with justification (A135).

---

## Corrections (Doc. 190, R128–R147)

| Entry | Concerns | Content |
|-------|----------|---------|
| R128 | Doc. 221 | No deviation of the supernova time dilation from (1+z) at high z [X] |
| R129 | Docs. 006, 046 | Unrecorded early changes to the quantum number table added |
| R130 | Doc. 343 | Theorem A: scope of the statement |
| R131 | Doc. 091 | Zeta regularisation of the mode sum for the corpus lattice closed |
| R132 | Docs. 010, 012, 013 and others | Calculations of the gravitational constant corrected |
| R133 | Docs. 003–300 (selection) | Findings of the recalculation corrected in the text |
| R134 | Docs. 000–002 | Acronym and ξ formula in introductory documents |
| R135 | Docs. 011, 041, 044 and others; A010, A130 | Classification of α, E₀ and K_frak |
| R136 | Docs. 009, 016, 025 and others; A260 | Casimir-CMB connection: identity, not measurement evidence |
| R137 | Docs. 008, 025, 026 and others | CMB temperature, redshift, H₀ and Λ classified more precisely |
| R138 | Docs. 006, 009, 012 and others | Precision tables of the mass ladder are not evidence |
| R139 | Docs. 268, 291, 293 | CMB factor 3 and form of K_frak open again |
| R140 | Continuation of R133 | Recalculation extended to all documents up to No. 300 and the A series |
| R141 | Docs. 012, 013, 016 and others; A145, A220 | Precision of G: residual of the one-anchor chain in C_conv |
| R142 | Continuation of R133 | Recalculation of the QM documents |
| R143 | Docs. 022, 035, 148; A165 | Unsupported CHSH data and a ξ fitted to them removed |
| R144 | Doc. 325 | R93 and R94 refined (black holes) |
| R145 | Docs. 327, 322, 330 | Self-adjointness of F̂ only on the ℤ₃-invariant sector |
| R146 | Docs. 347, 346, 356, 357 | Gell-Mann–Nishijima not fully closed |
| R147 | Docs. 018, 159, 186, 210 and others | Notation f: not a frequency; f = 1/ξ cannot be set to 1 |

---

## Open bridges (as of R147, selection)

| Bridge | Status |
|--------|--------|
| τ_μ directly from FFGFT (without G_F and v) | [S] (R112, Doc. 351) |
| Origin of the number 100 and of the fitted factor 10 in v/E_P | [S] (Docs. 149, 387) |
| Residual 1.7·10⁻⁴ between the K_frak required by α and 1 − 100ξ; form of the factor | [S] (R135, R139) |
| Residual of the one-anchor chain for G | [S] (R141, Doc. 383) |
| Factors 74 and 1/45 of the φ skeleton; common root of icosahedral phase and Galois order | [S] (Docs. 368, 370, A125) |
| Koide amplitude d/c = √2 from the geometry | [S] (Doc. 352 §8) |
| Hypercharge of the charged leptons | [S] (R146) |
| Self-adjointness of F̂ on the full space | [S] (R145) |
| Quark/hadron sector; K_had | open (Doc. 318, R76, R123) |
| Cosmic exponent forward (P20); CMB peaks {1,6,14,26} | open (P20, P29/P31, R139) |

## Entry point for new readers
**Doc. 384 "FFGFT in Brief"** (De/En, 20/19 pp., also as HTML) is the recommended entry
point to the current state. Doc. 205 "FFGFT in Simple Language" remains the entry point
for lay readers; the icosahedron book *The Number That Nobody Explained* remains the
entry point to the lepton masses.

## What has not changed
ξ and T̃·m = 1 are unchanged. All results from v1.4.2 continue to hold insofar as they
are not refined, restricted or withdrawn by R128–R147 or the notes of the
recalculation.
