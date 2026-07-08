# Release Notes — v1.2.1 (July 2026)

**DOI:** to be assigned on Zenodo upload (supersedes v1.1.9 · [10.5281/zenodo.21193007](https://doi.org/10.5281/zenodo.21193007))

Running corrections: **[2/PDFs/190_T0_Korrekturen_En.pdf](2/PDFs/190_T0_Korrekturen_En.pdf)**
Changelog: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**

---

**FFGFT — Fractal Field-Geometric Fundamental Theory** shows:
all Standard Model constants follow from a single dimensionless
parameter **ξ = 4/30000** on a compact 4-torus T⁴. The foundational
relation is **T̃ · m = 1** — intrinsic time and mass are inversely
coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## What is new in v1.2.1

v1.2.1 is an **FFGFT-internal clarification of the time-winding**. In v1.1.9,
[Doc. 295](2/PDFs/295_Zeit_Logspirale_En.pdf) established that the K_frak
recursion ξ_{n+1} = ξ_n(1−100ξ_n) forces the time-winding to be a
**logarithmic spiral with self-similarity ratio e**. v1.2.1 records that this
result is **not bound to one picture** — the same non-closure exists in two
equivalent representations.

### Two equivalent representations — time is described too

- **Geometric:** as a log spiral ρ = 75·e^{β/2π} from the recursion; frozen,
  the winding closes after exactly 75 turns (75 = 1/(100ξ₀)); running,
  ξ_n ≈ 1/(100(n+75)), the cumulative defect grows logarithmically (Doc. 295).
- **In the Hilbert space:** as a **memory kernel** — the Fourier transform of
  the discrete spectral density Σ_k g_k²·δ(ω−ω_k) of the T⁴ connection-Laplacian
  (Doc. 283); an oscillatory, discrete-spectral kernel with revivals (BLP
  backflow 5.125).

Both are **the same inseparable object** on the **lossless bijection**
H = L²(T⁴)⊗ℂ³ (Doc. 230/282, Type III of the projection chain Doc. 270). The
Hilbert-space translation of FFGFT thereby **describes time too** — there are
several equivalent routes to the same result, time included.

### What this is and what it is not (P35)

Equivalent representations *must* agree — the same object in T⁴, in different
clothing. This is **representational robustness, not additional evidence**:
*translation is not justification.* The generative original remains T⁴
(Doc. 206/270/287); the other forms are computational forms. The actual
evidential weight sits with the **independent witnesses** — different methods,
the same value, as with θ = 2/9 from Koide (from the masses) **and** from the
geometry (parameter-free, without a 2/9 input, Doc. 293) — not with equivalent
translations.

---

## Core derivations (as of v1.2.1)

| Result | Document |
|--------|----------|
| Derivation chain ξ → G → ℓ_P → L₀ | [Doc. 180](2/pdf/180_T0_L0_Herleitung_En.pdf) |
| Lepton masses from rational invariants | [Doc. 006](2/pdf/006_T0_Teilchenmassen_En.pdf) / [046](2/pdf/046_Teilchenmassen_En.pdf) |
| Koide scalar Q = 2/3 (computed) | [Doc. 258](2/pdf/258_Koide_2-3_En.pdf) / [259](2/pdf/259_Koide_Kreuzterme_En.pdf) |
| θ = 2/9 as Z₃-circulant phase | [Doc. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_En.pdf) |
| θ = 2/9 as a parameter-free C₃-in-A₅ geometry invariant (second witness) | [Doc. 293](2/PDFs/293_Ikosaeder_Theta_2_9_En.pdf) |
| Time-winding as a log spiral with ratio e (geometric + Hilbert-space memory kernel) | [Doc. 295](2/PDFs/295_Zeit_Logspirale_En.pdf) / [283](2/PDFs/283_FFGFT_HLV_Bruecke_En.pdf) |
| α⁻¹ = 137.036, two independent E₀ routes | [Doc. 011](2/pdf/011_T0_Feinstruktur_En.pdf) / [292](2/PDFs/292_Leptonen_Empirie_Check_En.pdf) |
| SI bridge | [Doc. 013](2/pdf/013_T0_SI_En.pdf) |
| Hilbert-space bijection FFGFT ↔ QM (time described too) | [Doc. 230](2/pdf/230_Hilbertraum_Uebersetzung_En.pdf) / [282](2/PDFs/282_FFGFT_HLV_CP_Teilbarkeit_En.pdf) |
| Lepton empirics check, m_τ prediction, tolerance balance | [Doc. 292](2/PDFs/292_Leptonen_Empirie_Check_En.pdf) |
| Falsification: Casimir / redshift / lithium | [Doc. 220](2/pdf/220_Casimir_En.pdf) / [221](2/pdf/221_Rotverschiebung_En.pdf) / [222](2/pdf/222_Lithium_En.pdf) |

---

## Reproducibility

`2/Dok295_Skripte/` — time-winding: 75-closure, log spiral (ratio e), dual
time↔mass projection (factor 100 axis-symmetric), numpy-only.
`2/Dok283_Skripte/` — memory kernel as the Fourier transform of the discrete
spectral density of the T⁴ connection-Laplacian (revivals, BLP backflow 5.125),
numpy-only.
`2/Dok293_Skripte/` — icosahedral redistribution (p₀ = 2/9 exact, robustness
over random axes and the n-fold series), numpy-only.
`2/Dok292_Skripte/` — lepton empirics check (parts A–L).
`2/Dok291_Skripte/` — θ = 2/9 mechanism scripts.

---

## Platforms

| Resource | Link |
|----------|------|
| 🔬 Interactive portal | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
