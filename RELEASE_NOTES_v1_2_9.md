# Release Notes — v1.2.9 (August 2026)

**DOI:** *to be assigned on Zenodo publication*

This release supersedes **v1.2.8**
([21821995](https://doi.org/10.5281/zenodo.21821995)).

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

Since v1.2.8, **one new corpus document** has been added: **Doc. 315
"The Form of K_frak: Additive or Multiplicative?"** (DE+EN, 10 pages
each, four verification scripts). It examines, for the first time,
whether the corpus discriminates the *form* of the fractal correction
factor — additive 1 − 100ξ = 74/75 against multiplicative
(1 − ξ)¹⁰⁰ — rather than merely its value.

No change to ξ, to the foundational relation, or to any derivation
chain. Source documents remain unchanged (append-only).

---

## Doc. 315 — The Form of K_frak (new)

**The question.** The two forms differ by exactly the second binomial
term, 4950ξ² ≈ 8.9×10⁻⁵. A corpus location can decide the form only
if its own uncertainty is smaller than this distance (amplified at
power-law locations).

**Control case.** Euler's musical spiral (5/7-limit): exact closure is
impossible by prime factorisation; the best near-closures are the
schisma (1.95 cents) and, in the 7-limit, the ragisma 4375/4374
(0.40 cents). Closure arises only through temperament —
rationalisation of the step size — precisely the rationality the ξ
cycle (1/75, gcd(74,75) = 1) carries by stipulation.

**Three witnesses.**
- **A130 two-route ratio:** m_μ cancels completely; with the
  undeclared identity p = −(2−√3) the location discriminates 7.5:1
  additive. New open items P-315-1 (derivation of the identity) and
  P-315-2 (a real residual of ≈ 7 eV in m_e, 45,000× the measurement
  floor — the same item as the n = 101.3 excess booked in R72).
- **A270 high-power location:** K⁻³⁶ ≈ 16/π²; the ×36 amplifier makes
  the form distance 0.32 %. Additive hits to 1.0×10⁻⁴, multiplicative
  misses by 3.1×10⁻³ — **31:1 additive**. The reference is upgraded
  via Doc. 314: **16/π² = 1/Δ(D4)**, the reciprocal packing density
  of the D4 lattice; **P35 narrows** from "where does the constant
  come from?" to "why does the bulk exponent 36 couple to Δ(D4)?".
- **A040 power form:** tends additive but cannot resolve
  (D_eff four digits only).

**Structural argument.** The additive form is the exact winding
bookkeeping of the rolled-up domain (75(1−ε) = 74 as an identity);
the multiplicative one is the stepwise composition of the unrolled
scale domain. Tied to the closure fork (Docs. 295/313, per
Doc. 314 Ch. D2): case B (frozen ξ) *is* the additive bookkeeping,
case C (running ξ, equiangular spiral) *is* the
multiplicative–logarithmic one; all corpus uses book case B.

**Status.** Value [K]; form additive [B], twice conditionally
confirmed; the multiplicative alternative is consistently disfavoured
by both conditional witnesses and supported by none, and remains
logically possible only while both conditions stay open.
Unconditional decision line: the A270 baryon location (K³⁸ level,
form distance 0.34 %) — simultaneously a test of the fork assignment
and of the primacy of the rolled-up geometry.

Verification: `2/python/315_Skripte/` — `euler_spirale_7limit.py`,
`pruefrechnung_kfrak_form.py`, `pruefrechnung_p_identitaet.py`,
`pruefrechnung_rest_0p1xi.py` (standard library only, exact fraction
arithmetic, assertions carry the target values).

Documents: [DE](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/315_Kfrak_Form_De.pdf) · [EN](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/315_Kfrak_Form_En.pdf)

---

## New and narrowed open items

- **P-315-1:** derivation or declaration of p = −(2−√3) in
  A130/route 2 (the only way to make witness A resolution-capable
  after R72).
- **P-315-2:** the real ≈ 7 eV residual in m_e (no simple correction
  term among ten F(ξ) families; QED self-energy order of magnitude).
- **P-315-3:** n sharpness — form discrimination requires
  Δn ≤ 0.66; the sector ladder (n = 100.27) is the most promising
  candidate.
- **P35 (narrowed):** forward derivation of
  K_frak⁻³⁶ = 1/Δ(D4), in particular the role of the bulk
  exponent 36.
