# Release Notes — v1.2.8 (August 2026)

**DOI:** *(to be added on publication)* — supersedes v1.2.7 ([10.5281/zenodo.21628364](https://doi.org/10.5281/zenodo.21628364))

Running corrections: **[2/pdf/190_T0_Korrekturen_En.pdf](2/pdf/190_T0_Korrekturen_En.pdf)**  
Change log: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**  
A-series log: **[A_Serie_Export/A_SERIE_CHANGELOG.md](A_Serie_Export/A_SERIE_CHANGELOG.md)**

---

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows:
all Standard Model constants follow from a single dimensionless
parameter **ξ = 4/30000** on a compact 4D torus T⁴. The foundational
relation is **T̃ · m = 1** — intrinsic time and mass are inversely
coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## New in v1.2.8

Two documents of the cosmological–geometric block revised. No change
to the A-series, no change to ξ or to any derivation chain.

### Doc. 314 "Lattice in Hilbert Space" — extended (DE 26 / EN 25 pp.)

The document is now **self-contained**: all back-references to earlier
versions have been removed. The change history lives in the Git
history and in the changelog, not in the document.

**The perturbation calculation is carried out** (Ch. J.3, status from
"open" to **[K]**). Multiplet sizes follow the **irrep dimensions** of
the respected symmetry, not the orbits:

| Perturbation respects | Splitting of the 24 |
|---|---|
| full Aut(D4) | 9 + 8 + 4 + 2 + 1 |
| triality (Z₃) | 8×1 + 8×2 |
| only −1 / neither | 24×1 |

Reason: every position-dependent perturbation breaks
**translation** invariance — and that carried the 24-fold degeneracy,
not the point symmetry. Z₃ is abelian, all irreps one-dimensional; the
doublets are the antiunitary χ₁/χ₂ pairing. Three independent seeds
per symmetry class, seed-independent result.

**New chapter D1 "Time from the mass circle" [K].** T_k = 2πR₄/k₄ is
an **arc length**, hence a place interval — λ₄·m = 2π is the
**de Broglie relation** along the mass direction, not a statement
about time. Duration arises only in the unrolled coordinate
t = w·2πR₄ + x₄ (revolution count plus place on the cycle). Three
statements in three directions:

| Reading | Relation | Equality for |
|---|---|---|
| place (de Broglie) | = 2π | always |
| time, moving mode | = 2π/γ ≤ 2π | p_space = 0 |
| mass mixture (Jensen) | ≥ 2π | sharp shell |

The relation becomes exact only for the **resting, sharp** mode;
motion pushes the product down, mass spread lifts it up.

**New chapter D2 "The closure fork is spectrally invisible" [K].**
In the rolled-up state there are **no fractal corrections**:
single-valuedness of the mode forces k₄ ∈ ℤ, a winding number is
topological and has no room for 1/75. Corrections require
accumulation, and only a traversed path can accumulate. The obvious
twist reading (Scherk–Schwarz, k₄ → k₄ + 1/75) is therefore **wrong**.
Consequence: cases A/B/C of Docs. 313/295 leave the mode spectrum
untouched, and Chapters E–H are **case-independent**.

**Chapter J recast: "What is still bare here — and what is not" [K].**
D_f and K_frak are **different things** (Doc. 133):

| Quantity | Character | Effect |
|---|---|---|
| D_f^space = 3 − ξ | local | 6.67 × 10⁻⁵ |
| K_frak = 1 − 100ξ | cumulative (RG run) | 1.33 × 10⁻² |

Ratio exactly 200. Two clarifications: the corpus knows no quantity
D_f = 4 − ξ (Doc. 133 defines the **spatial** dimension 3 − ξ; the
exponent 3/2 in K_frak^{3/2} is likewise half the **spatial**
dimension), and O(100ξ) is ruled out as a perturbation strength,
because a cumulative quantity does not belong on a local operator.
The perturbation therefore lies **two orders of magnitude below**
what an estimate via K_frak would give. **Balance: bare are only the
SI absolute values, and via the anchor, not via the operator** —
degeneracies, ratios, congruences, containers, and Casimir and
heat-kernel ratios are not bare but correct.

**Verification:** `2/python/Dok314_Skripte/` — four scripts with a
README, all target values as assertions, deterministic:
`d4_skript_1_spektrum_deformation.py` (theta series, 24 = 12+12,
exact crossing map at r = √2 and √3),
`d4_skript_2_trialitaet_orbifold_phasen.py` (|Aut(D4)| = 1152,
5 ∤ 1152, |det(1−A)| = 9, circulant, denominator spectrum {1,2,3,6}
without 2/9, 24 = 4×6),
`d4_skript_3_schalen_casimir.py` (shell theorems, Epstein zeta at
s = −1/2 with double verification, heat kernel),
`d4_skript_4_stoerung_reziprozitaet.py` (perturbation multiplets,
reciprocity).

### Doc. 313 "No Beginning" — two corrections, two extensions (DE 25 / EN 24 pp.)

**Correction 1 (π versus 2π).** Condensing from Doc. 295 had lost a
qualification: 313 wrote "a winding that should advance by **2π per
revolution** advances only by **π·K_frak**" — this mixes two reference
quantities and reads like a defect of ~50 %, while d = 1/75 follows
immediately after. Doc. 295 has the **half turn**. Corrected after the
wording of 295, with source reference; the transition to units of a
revolution is now explicit.

**Correction 2 (gcd).** "The 75 drops out exactly" was asserted, not
justified. Added: **gcd(74, 75) = 1**, hence the smallest n with
n·74/75 ∈ ℤ is exactly n = 75 — closure does not occur earlier.

**Extension 1 — Section F.4 "Reach: equilibria at other places on the
cycle" [K].** The usual backward extrapolation T(z) = T₀(1+z)
presupposes **one** continuous thermodynamic chain — precisely the
coarse-grained chaining that D(ii) leaves open. In the place reading,
an early epoch is not an earlier state of the same system but a
location with a different local structure (smaller masses, slower
clocks) and its own locally fixed equilibrium. The corpus demonstrates
this on itself: T₀ is not extrapolated but obtained structurally from
ξ (k_BT₀ = (16/9)ξ, Doc. 061). **Delimitation:** the Ω_m* chain runs
through ξ, H₀ and K_frak, not through an adiabatic back-calculation,
and is unaffected.

**Extension 2 — "Which quantities then remain meaningful?" [K].**
Criterion in three parts: **no scale bridge, no duration, same
level.**

| Class | Examples | Status |
|---|---|---|
| counts | \|Aut(D4)\| = 1152, kissing number 24, 9 fixed points | exact; theorems, not measurements |
| same-level ratios | α, m_μ/m_e, Koide Q | robust; testable at 10⁻¹⁰ to 10⁻⁵ |
| with scale bridge | E₀, G, H₀, T₀, absolute masses | only with an anchor; ratios thereof free again (A040) |
| number and duration | η, window durations, time spans | not transferable |

**All three BBN observables fall into the lower two classes —
including Y_p:** it does depend on the dimensionless quantities Q/T_f
and t/τ_n, but T_f is **not measured** (it follows from a rate
equation involving H, hence from the cosmological model), and t/τ_n
contains a **duration**. The cancellation argument is an
**implication**, not a test surface. **Consequence for the ⁷Li
position:** the corpus booking (Docs. 025/063, nucleosynthesis without
a fixed time limit) remains consistent but is **no quantitative
prediction**. **Counter-check:** the same classification applies to
ΛCDM equally — Doc. 267 already records: "none is circle-free". The
classification does not exempt FFGFT; it places both sides under the
same criterion.

**Verification:** `2/python/Dok313_Skripte/ffgft_bbn_skaleninvarianz.py`
— scaling exponents under mass scaling (classified as a change of
units), Y_p sensitivity, ξ drift as the single remaining break point,
parametrised by p = dln(Q/T_f)/dln ξ. Explicitly booked as a
**non-finding**: G = ξ²/(4 m_char) (Doc. 012) and α = ξE₀²
(Doc. 011) are **derived** from ξ, not independent scales — their SI
values require an anchor, and anchoring is conversion, not fitting
(A040, R72). They therefore do not serve as independent break points.

---

## No register entry required

Docs. 313 and 314 are **current** documents of the same cycle; their
corrections and extensions are incorporated directly. The correction
register (Doc. 190) admits only entries that refine **older**,
already-released documents — none is affected here. The change history
is in the changelog and in the Git history.

---

## Statistics (v1.2.8)

| | Count |
|---|---|
| A-series documents (DE + EN) | 48 × 2 = 96 (unchanged) |
| revised documents | 2 (313, 314) × 2 languages |
| new verification scripts | 2 (`d4_skript_4_…`, `ffgft_bbn_skaleninvarianz`) |
| new READMEs | 1 (`python/Dok314_Skripte/README.md`) |
| correction register | K1–K7, R1–R73 |
