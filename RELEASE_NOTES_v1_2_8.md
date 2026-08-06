# Release Notes — v1.2.8 (August 2026)

**DOI:** [10.5281/zenodo.21821995](https://doi.org/10.5281/zenodo.21821995)

This release supersedes **v1.2.6** in content; **v1.2.7**
([21628364](https://doi.org/10.5281/zenodo.21628364)) was an archive
re-upload only, with no change of content.

Running corrections: **[2/pdf/190_T0_Korrekturen_En.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_En.pdf)**
Change log: **[000_FFGFT_Changelog_De.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/000_FFGFT_Changelog_De.md)**
A-series log: **[A_Serie_Export/A_SERIE_CHANGELOG.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/A_Serie_Export/A_SERIE_CHANGELOG.md)**

---

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows:
all Standard Model constants follow from a single dimensionless
parameter **ξ = 4/30000** on a compact 4D torus T⁴. The foundational
relation is **T̃ · m = 1** — intrinsic time and mass are inversely
coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

Since v1.2.6, **seven new corpus documents** have been added
(Docs. 308 to 314, each DE+EN) together with **two A-series
documents** (A272, A273). The correction register has grown to
**R74**. The focus is the cosmological–geometric block: cosmic
sector, scale anchor, resonance geometry, the reduction from four to
three spatial dimensions, the closing scale Λ\*, the thermal history
on the time cycle, and the D4 lattice in Hilbert space.

No change to ξ, to the foundational relation, or to any derivation
chain.

---

## A-series: two new documents

**A272 "Carrier and Information"** — textual critique. What Landauer
proved in 1961 is a lower bound for **carrier operations** on a
thermal equilibrium ensemble, not a universal statement about
abstract information. Theorem 1 (multiple realisability): no energy
can be assigned to an information bit, only to its carrier.
Theorem 2: a purely interpretive erasure does not reduce the carrier
state space. Explicitly framed as a finding about scope, not as a
refutation. Binding dictionary A271 ↔ A272: region = carrier,
description = information, region reduction = carrier operation,
non-bijectivity = reduction of the carrier state space.

**A273 "The Computing Sphere"** — token accounting separates
bookkeeping from thermal conversion; verification script with 14
checks.

Both declare **FFGFT contact: none** — they live at the level of
statistical mechanics; the ξ scheme is untouched. New layer marker
**[Q]** (source: external primary source or measured value).

---

## Doc. 308 "The Cosmic Sector of FFGFT" (DE+EN, 11 pp. each)

Completely rewritten. Three cores:

**Redshift [K]:** static universe, 1+z = e^(ξx), achromatic. Λ (dark
energy) as a reading artefact — all three conditions met.

**Two-halves synthesis [K]:** K3 area invariance — T̃·m = 1 (time
half) and fractal path lengthening (space half) are complementary
halves, 0.875″ each, 1.750″ together. γ_PPN = 1 exactly (Cassini
passed).

**Inertia regime [K]/[S]:** a = √(a_N² + a_N·a₀), no free parameter;
a₀ = c²ξ¹⁰/(4λ̄ₑ) = 1.033×10⁻¹⁰ m/s². a₀ is the **transition scale of
the inertia regime**, not a gravitational parameter (G ~ ξ²,
a₀ ~ ξ¹⁰ — different mechanisms). DDO 154 ratio 1.001; Bullet Cluster
peak 10 kpc. Dark matter: "a regime, not a substance".

Verification: `2/Dok308_Skripte/` (4 scripts, no free parameters).

---

## Doc. 309 "The Scale-Anchor Problem: ΛCDM and FFGFT" (DE+EN, 9 pp. each)

Working note. Since 2019, SI reduces to a conventional anchor; only
dimensionless ratios are genuinely fixed. ΛCDM: ~6 free parameters,
H₀ circular via a four-step ladder. FFGFT: it is not ξ that is the
fit, but the **exponent 10** in H₀ = (π/2)·c·ξ¹⁰/λ̄ₑ.

**Inheritance problem (newly named):** the exponent 10 is calibrated
to H₀_ΛCDM, so FFGFT inherits the systematics of the expansion
reading; a reading-independent derivation from T⁴ geometry has not
been achieved (P20/P33). Cross-anchoring: ξ¹⁰ reproduces H₀ **and**
a₀.

---

## Doc. 310 "Resonance Geometry as the Overarching Reference" (DE+EN, 13 pp. each)

Answers the circularity objection by correcting the hierarchy: the
geometry with its resonances is overarching (dimensionless, fixes all
ratios); the measured value is only the **concert pitch** — an anchor
in SI, carrying no structure.

Three [K] statements, all checkable against measured masses: Koide
Q = 2/3 from three masses without ξ; the generation ladder as a
geometric sequence with ratio q = 2/3 (the same value as Koide Q);
the harmonic prefactors 4/3, 16/5, 25/9.

**π factors are sphere geometry, not loops:** 16π³ = S²·2S³ (T⁴
boundary geometry); the earlier version 64π⁴ counted exactly one
2-sphere too many. In natural units μ₀ and ε₀ disappear; with α = 1
only ξ remains.

Verification: `2/Dok310_Skripte/` (4 scripts).

---

## Doc. 311 "Four onto Three" (DE+EN, 22 pp. each)

Working note (not A-series). How does a 4D lattice reach three
spatial dimensions? Three routes (compactify / project / the fourth
is not space) with a cost balance; routes 1 and 3 are individually
incomplete and are closed by T̃·m = 1.

**Decomposition finding:** D4 need not be reduced — it decomposes by
itself, 24 = 12 + 12. The twelve vectors with x₄ = 0 are exactly the
FCC kissing number 12 (cuboctahedron as the neighbourhood figure of
space, Kepler/Hales uniqueness); the other twelve are six winding
neighbours per direction of circulation. This is the lattice form of
T⁴ = T³ × S¹_m — the split falls out rather than being put in.

**Consequence for counts:** whoever computes spatially with 24
implicitly asserts four spatial dimensions. The K⁻³⁶ check confirms
it: the 4D density belongs in (exponent 35.9926), the 3D density is
ruled out (22.38).

Verification: `2/python/Dok311_Skripte/ffgft_311_vier_auf_drei.py`.

---

## Doc. 312 "The Closing Scale" (DE 31 / EN 29 pp., 5 scripts)

The Λ function receives a carrier: **Λ\* := 1/R_H² = (π/2)²ξ²⁰/λ̄ₑ² =
5.218×10⁻⁵³ m⁻²**, no new parameter, dimensionless
Λ\*λ̄ₑ² = (π/2)²ξ²⁰.

**The 10¹²³ problem is resolved:** Λ\*l_P² = 10⁻¹²¹·⁸⁷ decomposes into
ξ²⁰ (−77.5 dex) · (l_P/λ̄ₑ)² (−44.8) · (π/2)² (+0.4) — the fine-tuning
reduces **entirely to P20**.

**Course setting:** the Einstein equations are adopted in full
(Lovelock enforces the form including the Λ term); what is
model-dependent is the ΛCDM triad {Λ fit, FLRW application,
expansion reading of z}, not the equation. The price: the Eddington
stability question applies and is not evaded — Appendix C1 computes
the winding–momentum balance. New conditional label **[K|P20]**.

Further chapters: time in the field equations (ADM, Wheeler–DeWitt);
statics of the relation (Okun/Selivanov/Telegdi; Wetterich 2013:
expansion ≡ mass running, a choice of frame rather than a
measurement); thinking in light paths with three hard limits at c;
**compact time direction** (τ_c = 2π/H₀ = 91.9 Gyr, quantum exactly
ħH₀; KMS → Gibbons–Hawking without a horizon; Unruh → a = cH₀
exactly); relative motion and the torus rest frame (CMB dipole as an
exact v/c reading); Einstein epilogue (four reasons why he did not
see T̃·m = 1).

Verification: `2/python/Dok312_Skripte/` (5 scripts).

---

## Doc. 313 "No Beginning: The Thermal History on the Time Cycle" (DE 25 / EN 24 pp., 4 scripts)

Answers obligation D(ii) of Doc. 312.

**Antipode finding [K|P20]:** the entire observable history fills
**one half-cycle** — with the fractal path correction the particle
horizon sits at 0.14 % from the antipode. The "Big Bang" is a
**place** on the cycle (the region of smallest masses and slowest
clocks), not an event.

**Lower bound:** E_min = ħH₀ = 2.28×10⁻⁵² J; ħH₀/(mₑc²) = (π/2)ξ¹⁰
exactly → a finite z_max = 3.59×10³⁸, no "z→∞". The singularity is
**excluded** by quantisation, not merely ill-posed.

**Entropy obstacle [K]:** Poincaré discrepancy 10¹⁰⁴ dex in the
exponent → periodicity is a boundary condition, not dynamics;
fine-grained admissible, coarse-grained closure open — the sharpened
hard core of D(ii).

**Ω_m chain from ξ alone [K|P20×E]:** H₀ → T₀ → Ω_r → antipode
condition → **Ω_m\* = 0.3136** versus Planck 0.315 ± 0.007 (−0.19σ);
no step contains a parameter fitted to Ω_m. Overdetermination:
particle sector 0.3136 versus cosmic sector 0.3139.

**The fork (after Doc. 295):** the defect d = 100ξ = 1/75 per
revolution admits three cases for the unrolled time — A (d = 0,
closure after one revolution, 91.9 Gyr), B (ξ frozen, closure after
75 revolutions, 6892 Gyr), C (ξ running, no closure, log spiral).
Case B follows from the rational rotation number 74/75; since
gcd(74, 75) = 1, the trajectory closes after **exactly** 75
revolutions.

**Section F.4 "Reach" [K]:** the usual backward extrapolation
T(z) = T₀(1+z) presupposes *one* continuous thermodynamic chain —
precisely the coarse-grained chaining that remains open. In the place
reading, an early epoch is not an earlier state of the same system
but a location with a different local structure and its own locally
fixed equilibrium. The corpus demonstrates this on itself: T₀ is
obtained structurally from ξ (k_BT₀ = (16/9)ξ), not extrapolated. The
Ω_m\* chain is unaffected.

**Robustness [K]:** criterion in three parts — no scale bridge, no
duration, same level. Four classes:

1. **Counts** — order of Aut(D4) = 1152, kissing number 24, 9 fixed
   points. Exact; theorems, not measurements.
2. **Same-level ratios** — α, m_μ/m_e, Koide Q. Robust; testable at
   10⁻¹⁰ to 10⁻⁵.
3. **With scale bridge** — E₀, G, H₀, T₀, absolute masses. Only with
   an anchor; ratios thereof free again (A040).
4. **Number and duration** — η, window durations, time spans. Not
   transferable.

All three BBN observables fall into the lower two classes —
including Y_p: it does depend on the dimensionless quantities Q/T_f
and t/τ_n, but T_f is **not measured** (it follows from a rate
equation involving H, hence from the cosmological model), and t/τ_n
contains a **duration**. The cancellation argument is an implication,
not a test surface. Counter-check: the same classification applies to
ΛCDM equally (Doc. 267: "none is circle-free").

Verification: `2/python/Dok313_Skripte/` — including
`ffgft_bbn_skaleninvarianz.py`. Explicitly booked as a
**non-finding**: G = ξ²/(4 m_char) and α = ξE₀² are **derived** from
ξ, not independent scales; their SI values require an anchor, and
anchoring is conversion, not fitting (A040, R72).

---

## Doc. 314 "Lattice in Hilbert Space" (DE 26 / EN 25 pp., 4 scripts)

What becomes of the D4 lattice under translation into Hilbert space:
the kissing number becomes the degeneracy, triality becomes the
orbifold and the fibre, the radius ratio becomes the level splitting.

**Lattice theorems [K]:** the order of Aut(D4) is 1152 = order of
W(F4); the quotient over W(D4) is 6 = order of S₃ — triality
therefore stands at the lattice, not only at the Dynkin diagram. The
trace-(−2) class satisfies: determinant of (1−A) in modulus = 9.
**The T⁴/Z₃ orbifold with 9 fixed points is a lattice symmetry of
D4**, not an added assumption. On every triple orbit the Z₃ acts as a
ℂ³ circulant with {1, ω, ω²}.

**A boundary, as a theorem [K]:** Aut(D4) has **no elements of order
5** — 1152 = 2⁷·3², and 5 does not divide it (Lagrange). The fivefold
symmetry that generates θ = 2/9 (Doc. 293) is incompatible with the
D4 lattice structure. The phase test confirms it numerically: all
invariants have denominator spectrum {1, 2, 3, 6}; 2/9 does not
occur.

**The doubling is admissible and prepared [K]:** the intersection of
element orders of A₅ and Aut(D4) is {1, 2, 3} — the only possible
interface is C₃, and triality occupies it. The −1 involution pairs
the 8 triple orbits without fixed points: **24 = 8×3 = 4×6**, four
ready containers with exactly the C₃ content that 3⊕3′ requires.
What is excluded is not 2/9 but only its derivation *from* lattice
invariants.

**Perturbation calculation [K]:** multiplet sizes follow the
**irrep dimensions** of the respected symmetry, not the orbits:

- full Aut(D4) → 9 + 8 + 4 + 2 + 1
- triality (Z₃) → 8×1 + 8×2
- only −1, or neither → 24×1

Reason: every position-dependent perturbation breaks **translation**
invariance — and that carried the 24-fold degeneracy, not the point
symmetry.

**Time from the mass circle [K]:** T_k = 2πR₄/k₄ is an **arc
length**, hence a place interval — λ₄·m = 2π is the **de Broglie
relation** along the mass direction, not a statement about time.
Duration arises only in the unrolled coordinate t = w·2πR₄ + x₄.
Three readings:

- place (de Broglie): = 2π — always
- time, moving mode: = 2π/γ ≤ 2π — equality at p_space = 0
- mass mixture (Jensen): ≥ 2π — equality for a sharp shell

The relation becomes exact only for the **resting, sharp** mode.

**Rolled up versus unrolled [K]:** winding numbers are topological;
fractal corrections require accumulation, and only a traversed path
can accumulate. The closure fork of Docs. 313/295 is therefore
**spectrally invisible**, and Chapters E–H are case-independent.
Equally to be kept apart: D_f^space = 3 − ξ (local, effect
6.67×10⁻⁵) and K_frak = 1 − 100ξ (cumulative across the RG run,
1.33×10⁻²) — ratio exactly 200. Bare are only the SI absolute values,
and via the anchor, not via the operator.

**Casimir [K]:** the Z⁴ torus lies lower than the D4 torus (−0.932
versus −0.869 at covolume 1) — the densest lattice loses, because it
has the largest spectral gap.

Verification: `2/python/Dok314_Skripte/` — four scripts with a
README, all target values as assertions.

---

## Correction register: R67 to R74

**R67** — the factor 100 in K_frak = 1−100ξ is a value averaged over
the RG run, with an accuracy of about **±2** nowhere stated; affects
A040, A270 and Doc. 133. Propagation ±0.027 % on absolute values;
ratios unaffected by construction.

**R68–R73** — clarifications arising from the work on Docs. 312/313:
Λ\* as carrier of the Λ function and full adoption of the field
equations (279/308); a₀ via the compact time direction (308); the T₀
scale gap and a notation clash (061/A085); side-taking in the Hubble
tension (309); the E₀ value bare versus fractally corrected, which
makes K_frak **overdetermined** — three independent routes give
n = 100±2, 101.3 and 100.27 (A010/A080/A265/A130); H₀ notations and
the exponent 41/4, with the resolution **L\* = 4·λ̄ₑ/ξ¹⁰** exact to
ten digits (026/279).

**R74 (new)** — Docs. 025 and 063 list the lithium problem in a table
whose third column is headed **"T0 solution"**; the entry reads
"nucleosynthesis over unlimited time". The claim level is one step
too high: the mechanism addresses the window duration and is
consistent, but from "no fixed time limit" **no numerical value** for
⁷Li/H follows — a sketch of a mechanism, not a quantitative
derivation. By the robustness classification (Doc. 313, F.4), ⁷Li/H
belongs to the number-and-duration class; the factor-3 discrepancy is
consequently no clean test *against* ΛCDM either. The same check
found that **no other older document** presents BBN observables as a
passed test. Source documents unchanged (append-only).

---

## Statistics (v1.2.8)

- A-series documents (DE + EN): 47 × 2 = 94
- New corpus documents since v1.2.6: 7 (Docs. 308–314) × 2 languages
- New A-series documents since v1.2.6: 2 (A272, A273)
- Correction register: C1–C7, R1–R74
- Layer markers: [STIPULATION] / [K] / [B] / [S] / [Q] / [H]; new [K|P20]
