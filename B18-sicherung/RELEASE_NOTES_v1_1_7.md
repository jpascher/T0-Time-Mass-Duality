# Release Notes — v1.1.7 (July 2026)

**DOI:** [10.5281/zenodo.21158441](https://doi.org/10.5281/zenodo.21158441) (supersedes v1.1.6 · [10.5281/zenodo.21061423](https://doi.org/10.5281/zenodo.21061423))

Running corrections: **[2/PDFs/190_T0_Korrekturen_De.pdf](2/PDFs/190_T0_Korrekturen_De.pdf)**
Change log: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**

---

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows:
all Standard Model constants follow from a single dimensionless
parameter **ξ = 4/30000** on a compact 4D torus T⁴. The foundational
relation is **T̃ · m = 1** — intrinsic time and mass are inversely
coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## What is new in v1.1.7

v1.1.7 adds a detailed, honestly-declared audit of the **lepton sector**
(Doc. 292) and completes the treatment of the **Koide phase θ = 2/9**
(Doc. 291). The focus is internal to FFGFT: how far the geometry fixes the
lepton masses, where the precision lives, and how the Koide phase is
characterised as the circulant angle.

### Lepton sector — two layers, one reference point, one sharp prediction

[Doc. 292](2/PDFs/292_Leptonen_Empirie_Check_De.pdf) audits the lepton sector
from the data side (P35/P40) and cleanly separates two layers that share ξ
but must not be mixed:

- the **circulant** (Z₃-symmetric mass operator) carries the *precision* —
  it hits μ/e to a few parts per million;
- the **ξ ladder** carries the *order of magnitude* — the same ratios to
  about one percent.

Under **P42** the μ/e ratio is a *declared reference point* (analogous to
P39): once anchored it is consumed and no longer a test quantity. The one
unavoidable test that remains is the tau mass: FFGFT predicts
**m_τ = 1776.97 MeV**, which Belle-II precision will decide without evasion.

### α is not a calibration

The fine-structure constant runs through **two independent routes** to the
characteristic energy E₀ — empirical (√(m_e·m_μ)) and purely geometric
(from ξ and m_μ alone, without using m_e). The two meet to ~8·10⁻⁵:
overdetermination, not a fit. The residual is a mode-independent witness that
the measured "dressed" pole mass is not quite the geometrically fundamental
quantity — a thin dressing layer between the bare geometry and what the
experiment sees.

### A generation-linear correction law

The ξ-ladder residuals are not three independent numbers: the exponents are
multiplicatively consistent (p₃ = p₁ + p₂ exactly) and the effective factors
scale as 1 : 2 : 3 with generation number, N_g ≈ g·N₀. This is why a
*constant* correction can never close the ladder. The base unit N₀ ≈ 38.6 is
not yet derived (100/φ² = 38.20 is an admissible candidate, within the N₀
tolerance, not a proof).

### The Koide phase θ = 2/9 — the circulant phase

θ = 2/9 is **not a free parameter**: it is the phase of the Z₃-circulant, the
value the diagonalisation outputs — found, not sought (from the Hilbert-space
translation, Doc. 230/231/232 → 282). [Doc. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_De.pdf)
characterises it positively by ruling out what it is not (not a symmetric
invariant, not countable/topological — 2/(9π) transcendental, not a static
icosahedral angle): what it *is* is a dynamical, magnitude-preserving holonomy
phase (χ = π/2). The transcendence result is itself positive knowledge — 2/9
cannot come from a flat/topological source. The value is fixed and its origin
identified: the Koide phase is settled.

### Methodology — the tolerance yardstick

Made explicit throughout Doc. 292: the measure of a geometric derivation is
**not** point-exact agreement on the last decimal — that is unreachable in
principle — but consistency **within the tolerances** to which the quantities
are determinable. Completeness means no residual protruding beyond those
tolerances that is closed only by a free parameter. The narrative overview
(Doc. 205) now carries a situation report in this spirit.

### Note: external cross-check (HLV / BD17A)

The θ = 2/9 forcing question was also put to a blind cross-check against an
external holonomy mechanism (Marcel Krüger's HLV / BD17A, Information Physics
Institute), under a symmetric pre-registration. The verdict was negative
(BLOCKED / not-separated) — the anticipated direction, since a flat
determinant-line holonomy cannot carry a transcendental angle as a topological
invariant. This bears on the external framework, not on FFGFT's own results:
the 2/9 structure in FFGFT's mass circulant and Q = 2/3 are untouched. Recorded
for completeness in `2/Dok291_Skripte/` (verdict + seals).

---

## Core Derivations (as of v1.1.7)

| Result | Document |
|--------|----------|
| Chain ξ → G → ℓ_P → L₀ | [Doc. 180](2/pdf/180_T0_L0_Herleitung_En.pdf) |
| Lepton masses from rational invariants | [Doc. 006](2/pdf/006_T0_Teilchenmassen_En.pdf) / [046](2/pdf/046_Teilchenmassen_En.pdf) |
| Koide scalar Q = 2/3 (computed) | [Doc. 258](2/pdf/258_Koide_2-3_En.pdf) / [259](2/pdf/259_Koide_Kreuzterme_En.pdf) |
| α⁻¹ = 137.036, two independent E₀ routes | [Doc. 011](2/pdf/011_T0_Feinstruktur_En.pdf) / [292](2/PDFs/292_Leptonen_Empirie_Check_En.pdf) |
| SI bridge | [Doc. 013](2/pdf/013_T0_SI_En.pdf) |
| Hilbert-space bijection FFGFT ↔ QM | [Doc. 230](2/pdf/230_Hilbertraum_Uebersetzung_En.pdf) |
| Lepton empirical check, m_τ prediction, tolerance balance | [Doc. 292](2/PDFs/292_Leptonen_Empirie_Check_En.pdf) |
| θ=2/9 as the Z₃-circulant phase; dynamical characterisation | [Doc. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_En.pdf) / [286](2/pdf/286_Dynamischer_Sektor_Kinetik_En.pdf) |
| Falsification: Casimir / Redshift / Lithium | [Doc. 220](2/pdf/220_Casimir_En.pdf) / [221](2/pdf/221_Rotverschiebung_En.pdf) / [222](2/pdf/222_Lithium_En.pdf) |

---

## Reproducibility

`2/Dok292_Skripte/` — lepton empirical check (parts A–L).
`2/Dok291_Skripte/` — θ=2/9 mechanism scripts (and, for completeness, the
external cross-check verdict and seals).

---

## Platforms

| Resource | Link |
|----------|------|
| 🔬 Interactive Portal | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
