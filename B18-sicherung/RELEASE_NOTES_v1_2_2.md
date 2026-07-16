# Release Notes — v1.2.2 (July 2026)

**DOI:** assigned on Zenodo upload (supersedes v1.2.1 · [10.5281/zenodo.21203746](https://doi.org/10.5281/zenodo.21203746))

Running corrections: **[2/PDFs/190_T0_Korrekturen_En.pdf](2/PDFs/190_T0_Korrekturen_En.pdf)**
Change log: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**

---

**FFGFT — Fractal Field-Geometric Fundamental Theory** shows:
all Standard-Model constants follow from a single dimensionless
parameter **ξ = 4/30000** on a compact 4D torus T⁴. The base
relation is **T̃ · m = 1** — intrinsic time and mass are inversely
coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## What is new in v1.2.2

v1.2.2 gathers **FFGFT-internal clarifications** around the compact projection
and the fractal correction factor. No new scaffolding — sharpening of existing
derivations.

### The Standard Model as a decompactified projection (Doc. 298)

The Standard-Model content appears as a **decompactified projection** of the
compact T⁴ structure: winding number and fractal comma live on the rolled-out
level, the projected level sees the closed approximation. This places the
SI/measurement level consistently under the compact picture (connects to
Doc. 270, projection chain).

### The correction factor K_frak = 1 − 100ξ, read from the closure comma (Doc. 300)

The rolled-out recursion closes only after **75 = 1/(100ξ₀)** equal pieces. The
approximation "one turn closes" neglects a small **closure comma** ε = 100ξ =
1/75; the per-step factor of the scale recursion ξ_{n+1} = ξ_n(1−100ξ_n) is
therefore

  **K_frak = 1 − 100ξ = 74/75 = 0.9867.**

Important (P35): 75 and K_frak are **both** just 100ξ — the comma
*re-expresses* the already-anchored 100ξ, it does not derive it. The actual
anchor remains **Doc. 133**: the factor 100 emerges from the RG running of
D_f = 3−ξ (effectively D_f^eff ≈ 2.973; geometrically 100 = 4·5², Doc. 042),
and K_frak is fixed by the consistency of two independent derivations of the
mass ratio m_e/m_μ; ξ itself via Higgs/α/Koide. This is a **clarification of an
existing corpus value**, not a new number.

### ι embedding protocol (Doc. 299) — FFGFT-internal

The protocol fixes domain, target space H = L²(T⁴)⊗ℂ³ and the test nulls
**before** the work (P35). The FFGFT-relevant finding: the test uses a
**derived** witness (BLP back-flow 5.125, Doc. 283), not a copy of the object
under test — self-reference through a derivation, not through a copy. Result in
the time sector: **admitted, not forced**, conditional on the winding angle of
the native carrier.

---

## Relation to HLV (external, secondary)

The clarifications above arose at the contact point with HLV (Marcel Krüger,
Information Physics Institute) but are stated **FFGFT-internally**. Because FFGFT
holds the absolute scale (reference point E₀) and HLV does not, the test
direction is one-sided, FFGFT→HLV; the correction factor 1−100ξ is
independently anchored (Doc. 133), not chosen from the external framework. HLV
remains a secondary cross-check, not a load-bearing part.

---

## Core derivations (as of v1.2.2)

| Result | Document |
|--------|----------|
| Derivation chain ξ → G → ℓ_P → L₀ | [Doc. 180](2/pdf/180_T0_L0_Herleitung_En.pdf) |
| Lepton masses from rational invariants | [Doc. 006](2/pdf/006_T0_Teilchenmassen_En.pdf) / [046](2/pdf/046_Teilchenmassen_En.pdf) |
| Koide scalar Q = 2/3 (computed) | [Doc. 258](2/pdf/258_Koide_2-3_En.pdf) |
| θ = 2/9 as Z₃-circulant phase / parameter-free invariant | [Doc. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_En.pdf) / [293](2/PDFs/293_Ikosaeder_Theta_2_9_En.pdf) |
| Fractal correction K_frak = 1 − 100ξ (RG running, m_e/m_μ consistency) | [Doc. 133](2/pdf/133_Fraktale_Korrektur_Herleitung_En.pdf) / [300](2/PDFs/300_ZweiRollen_Kfrak_En.pdf) |
| Standard Model as decompactified projection | [Doc. 298](2/PDFs/298_SM_Projektion_En.pdf) |
| α⁻¹ = 137.036, two independent E₀ routes | [Doc. 011](2/pdf/011_T0_Feinstruktur_En.pdf) / [292](2/PDFs/292_Leptonen_Empirie_Check_En.pdf) |
| Hilbert-space bijection FFGFT ↔ QM (time included) | [Doc. 230](2/pdf/230_Hilbertraum_Uebersetzung_En.pdf) / [282](2/PDFs/282_FFGFT_HLV_CP_Teilbarkeit_En.pdf) |
| SI bridge | [Doc. 013](2/pdf/013_T0_SI_En.pdf) |

---

## Reproducibility

`2/Dok300_Skripte/` — closure-comma check (K_frak = 1−100ξ), numpy-only.
`2/Dok299_Skripte/` — time-sector counter-run with a derived witness (BLP back-flow 5.125), numpy-only.
`2/Dok295_Skripte/` — time-winding: 75-closure, log spiral, numpy-only.
`2/Dok283_Skripte/` — memory kernel, revivals, numpy-only.
`2/Dok292_Skripte/` — lepton empirical check (Parts A–L).

---

## Platforms

| Resource | Link |
|----------|------|
| 🔬 Interactive portal | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
