# Release Notes — v1.5.1 (26 November 2026)

**DOI:** assigned on Zenodo publication — supersedes v1.4.6 (v1.4.7 to v1.5.0 were created on GitHub only; their archiving on Zenodo failed, the content is the same)
Running corrections: **[2/pdf/190_T0_Korrekturen_En.pdf](2/pdf/190_T0_Korrekturen_En.pdf)**
Changelog (German): **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**
Summary of the corpus: **[2/pdf/384_FFGFT_Kurzfassung_En.pdf](2/pdf/384_FFGFT_Kurzfassung_En.pdf)** (also as [HTML](2/html/384_FFGFT_Kurzfassung_En.html))

**FFGFT — Fundamental Fractal Geometric Field Theory** is first of all a ratio-based
theory. In natural units (Heaviside-Lorentz, ħ = c = ε₀ = 1) with α = 1 there is a single
dimensionless parameter **ξ = 4/30000** on a compact 4D torus T⁴/ℤ₃; the fundamental
relation is **T̃·m = 1** — intrinsic time and mass are inversely coupled. Only the
translation into SI needs a measured value as an anchor.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

v1.5.1 brings formal proofs into the corpus. The algebraic cores of Docs. 339, 340, 342
and 343 are now additionally proved in the proof assistant Lean 4; the Lean kernel has
checked every step, and a GitHub Action re-checks the proofs on every change. A new
status marker, **[L]**, records this. The formal check also produced a clarification of
the Majorana assignment, which has been worked into Docs. 340, 343, 346 and the
correction register (R164). ξ and T̃·m = 1 are unchanged, and no new corpus document is
added. For all other changes since v1.4.6, see the change log and Doc. 190.

---

## Formal proofs in Lean 4

The new folder `2/lean/` holds the Lean project `Dok339_Pilot` with three modules. It
does not need the Mathlib library: the field GF(27) is constructed explicitly as
GF(3)[x]/(x³+2x+1), and every statement about finite structures is computed in full by
the kernel. The Action `.github/workflows/lean.yml` builds the project on every push
that touches `2/lean/`; a green run means that all theorems are proved. Nothing needs to
be installed locally. The README in `2/lean/` describes the modules in detail.

The module `GF27.lean` secures Doc. 339: the model is a field with 27 elements, GF(27)*
is cyclic of order 26, exactly +1 and −1 are fixed by the Frobenius x ↦ x³, and the
remaining 24 units split into exactly eight three-orbits. This also proves the
cyclicity that the Python check script of Doc. 339 only assumes.

The module `Dok342.lean` secures Theorem A of Doc. 342 and Theorem E of Doc. 343. There
are exactly eight irreducible cubics over GF(3), and they are exactly the polynomials in
the table of Doc. 342; f₁–f₄ are the stated Frobenius classes with roots of order 26,
g₁–g₄ their sign partners with order 13. For the entry rule it is proved that 13, 5, 11
and 7 are the only primes with ord_p(3) = 3, 4, 5 and 6, respectively, for all natural
numbers and without an upper bound.

The module `Dok340.lean` secures the orbit algebra of Doc. 340 (sums, products,
Orbit₄ = 2⁻¹·Orbit₁, table of inverses) and settles the role of the generator in
Theorem D‴ of Doc. 343.

## New status marker [L]

The binding legend `2/Sources/ch/000_Statusmarker_Legende_De/En_ch.tex` has a new row:
[L] means that a [B] statement is additionally proved formally in Lean 4. The marker
applies to the mathematical statement only, not to its physical identification. The
corpus check script `pruef_statusmarker.py` and the De/En check script for Doc. 190
know the marker; both report 0 findings. Docs. 339, 340, 342 and 343 carry [L] at the
proved statements and a "Formal check" note pointing to the relevant module. The other
documents that include the legend will show the new row the next time their PDF is
built.

## Clarification of the Majorana assignment (R164)

The Majorana criterion of Doc. 340 — an orbit is closed under k ↦ k⁻¹ (mod 13) — works
with exponents and therefore depends on the chosen generator of GF(27)*. Lean shows for
all twelve generators: only the split of the four primitive classes into the layers
{f₁, f₂} and {f₃, f₄} is independent of the generator. Which layer is called Majorana
follows from the class of the generator; with a generator from f₃ or f₄ the labels swap.
The assignment in the corpus rests on the convention of Doc. 342 to choose the generator
as a root of f₁; it is now marked as [SETZUNG]. Doc. 343 (Theorem D‴) carries the
clarification in full, Docs. 340 and 346 as a note, and R164 in Doc. 190 refines the
earlier wording of R108, which had called the Majorana layer canonical.

## Status of the Riemann hypothesis

On 20 November 2026 a formal Lean 4 proof of the Riemann hypothesis was presented, which
also covers the generalised hypothesis for Dirichlet L-functions (L. Alpöge); expert
review is still ongoing. Doc. 343 therefore no longer lists the non-trivial zeros of
L(s, χ₀) as "assumed" but cites the source [Q]; this also covers L(s, χ₁) mod 3.
Doc. 316 has an addendum: the proof is arithmetic and needs neither the torus nor ξ,
which confirms the assessment of that document; the geometric approaches it excludes
remain excluded.

## What has not changed

ξ and T̃·m = 1 are unchanged. The calculations and results of v1.4.6 remain valid; the
clarification of the Majorana assignment changes no number but makes a previously tacit
choice visible as a postulate.
