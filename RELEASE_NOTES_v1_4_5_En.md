# Release Notes — v1.4.5 (8 October 2026)

**DOI:** assigned on Zenodo publication — supersedes v1.4.4
Running corrections: **[2/pdf/190_T0_Korrekturen_En.pdf](2/pdf/190_T0_Korrekturen_En.pdf)**
Changelog (German): **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**
Summary of the corpus: **[2/pdf/384_FFGFT_Kurzfassung_En.pdf](2/pdf/384_FFGFT_Kurzfassung_En.pdf)** (also as [HTML](2/html/384_FFGFT_Kurzfassung_En.html))

**FFGFT — Fundamental Fractal-Geometric Field Theory** is first of all a ratio-based
theory. In natural units (Heaviside-Lorentz, ħ = c = ε₀ = 1) with α = 1 there is a
single dimensionless parameter **ξ = 4/30000** on a compact 4D torus T⁴/ℤ₃; the
foundational relation is **T̃·m = 1** — intrinsic time and mass are inversely coupled.
Only the translation into SI needs a measured value as anchor.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

v1.4.5 is the first version without correction notes. Every document now contains only
the corrected final text; anyone who wants to trace what changed and when will find it
in Doc. 190 and in v1.4.4, the last version with dated notes. In addition there are two
supplements to the correction register (R148, R149), a complete revision of the HTML
pages with a new deterministic simulator, and the eight-volume complete edition as a
book in German and English. This version adds no new documents; the foundational
relation and ξ are unchanged.

---

## Documents without correction notes

On 6 October 2026 all documents were revised in five blocks (Docs. 001–052, 053–150,
152–241, 243–310, 311–389), together with the A-Series (A010–A284). Correction boxes,
dated notes and older addenda have been resolved: the text itself now states what
holds, and refuted statements have been rewritten so that only what is valid remains.
Abstracts, headings, tables and conclusions have been adjusted. Corrections that apply
across the corpus have also been applied where the register entry does not name the
document — for example the achromatic redshift, α as a property of the anchor E₀
(R135), the Casimir–CMB connection as an identity (R136), the precision of G (R141) and
order finding instead of a ξ resonance in factorisation (R65). The individual blocks
and the larger rewrites are listed in the changelog.

## Supplements to the correction register (R148, R149)

**R148** books what the computational review of 1 October had found for the documents
above No. 300 and a few older documents without being listed in a collective entry. The
main consequences: the Higgs route does not lead to ξ and remains a consistency check;
triality and the orbifold sector are two different ℤ₃; Theorem A in Doc. 349 and
Theorem C in Doc. 363 are not proven; the quark prefactors in Doc. 373 are determined
from measured values; the galaxy tests in Doc. 308 are open.

**R149** carries out three corrections in the documents themselves. Doc. 382 computed
the direct g−2 formulas with a rounded k_geom; the values now follow Doc. 018, and the
ratio line and the a_τ prediction are not affected. Doc. 006 now compares the quark
masses with PDG 2024, as Doc. 384 does; the deviations become larger, for the up quark
within the large uncertainty of that value, and the quark prefactors remain determined
from measured values [S]. In Doc. 073 the numerical simulation parameter is called σ
instead of ξ_num, because it is not a value of ξ (R75). Doc. 384 now refers to register
status R149.

## HTML pages

All HTML pages under `2/html/`, `rsa/` and `sig/` have been brought to the current state
of the corpus: status statements as in Doc. 384, status markers with a legend, no
outdated precision claims, α = 1 stated explicitly as Heaviside-Lorentz units. The home
page keeps its headline.

The **quantum simulator** (`2/html/quantum_simulator_deterministic.html`) has been
rebuilt and follows the deterministic measurement rule of Doc. 230: the outcome of a
measurement is A(z, λ) = sgn(z − λ), and the Born weights follow from the distribution
of λ. It comes with a new help page (`quantum_help_guide.html`) and a revised
step-by-step page (`step_by_step_modules_bilingual.html`). The Shor and factorisation
tools were checked a second time; calculation and program errors have been fixed. They
are described as what they are: a correct classical simulation of order finding, not a
separate FFGFT method (R65).

## Complete edition in eight volumes

The corpus appears as the eight-volume complete edition "FFGFT or T0 Theory: Time-Mass
Duality – Complete Works" (Amazon KDP), each as eBook, paperback (8.5 × 11 in) and
hardcover (8.25 × 11 in), in German and English. Volumes 1–3 are the original
three-volume plan, Volume 4 runs to Doc. 184, Volume 5 to Doc. 262, Volume 6 covers
Docs. 263–310, Volume 7 Docs. 311–343 and Volume 8 Docs. 344–389. The interiors are in
`2/pdf/buecher/`, the covers in `2/kdp/Gesamtserie/`.

The correction register Doc. 190 is no longer printed in Volume 5. It is maintained
continuously; the introduction to Volume 5 points to the current version in the
repository. Volume 5 is about 30 pages shorter as a result.

| Volume | Paperback De | Hardcover De | Paperback En | Hardcover En |
|--------|--------------|--------------|--------------|--------------|
| 1 | 450 | 456 | 424 | 432 |
| 2 | 415 | 419 | 383 | 386 |
| 3 | 422 | 428 | 395 | 405 |
| 4 | 365 | 368 | 347 | 350 |
| 5 | 426 | 430 | 407 | 411 |
| 6 | 361 | 372 | 346 | 355 |
| 7 | 339 | 343 | 317 | 321 |
| 8 | 340 | 346 | 322 | 329 |

## Getting started

**Doc. 384 "FFGFT in Brief"** (De/En, also as HTML) remains the recommended entry point
to the current state, Doc. 205 "FFGFT in Simple Language" the entry point for general
readers.

## What has not changed

ξ and T̃·m = 1 are unchanged. All results of v1.4.4 continue to hold unless R148 and
R149 refine or restrict them.
