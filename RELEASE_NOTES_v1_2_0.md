# Release Notes — v1.2.0 (July 2026)

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

## What is new in v1.2.0

v1.2.0 **closes a thread** that v1.1.9 had opened. The FFGFT-internal core of
[Doc. 295](2/PDFs/295_Zeit_Logspirale_En.pdf) — the time-winding as a
**logarithmic spiral with ratio e** — was already in v1.1.9. There Doc. 295
itself posed the sharp test question of whether the natural identification
with HLV's \enquote{spiral time} holds on the **e-criterion**. v1.2.0 carries
out that check and answers it — with a **clear negative** — and adds the
corresponding delimitation in
[Doc. 294](2/PDFs/294_HLV_Pruefrichtung_En.pdf).

The finding is an **FFGFT-internal closure**, not a new external claim: the
time-winding as a log spiral with e stands on its own; the comparison only
shows that the identification with the external framework does not hold. HLV
remains subordinate for FFGFT (cf. the negative BD17A verdict in v1.1.7) —
only a load-bearing bridge would have been of interest; here the result is a
clean negative plus a category clarification.

### Two disjoint "spiral times" — the category clarification

\enquote{Spiral time} in HLV denotes not one object but **two**, sharing only
the name:

- the **geometric** time from the factorisation T⁷ = T⁴ × T³ (Doc. 285):
  an A₅ singlet on the S¹ factor, decoupled and separable;
- the **temporal-dynamic** spiral time — the object HLV *calls* by that name:
  a non-Markov operator Ψ(t) = (t, φ(t), χ(t)) with a memory channel,
  **without** A₅, singlet or S¹ factor.

FFGFT, unlike both, does not factorise; its spiral is the projection of an
inseparable whole (T̃·m = 1). The e-test question targets a **geometrically
self-similar** object — the named HLV object is not of that category.

### The e-criterion: FFGFT carries e, no HLV strand does

The e-criterion is necessary and sufficient via the pitch decay: a winding is
equiangular (a log spiral, ratio e per 2π) exactly when the defect per step
decays like **1/n** and the cumulative defect grows logarithmically; a
constant defect gives an **Archimedean** winding with ratio → 1.

- **FFGFT** carries e: with d_n = 100 ξ_n one has d_n·(n+75) → 1 (the 1/n
  decay), and the spiral fit gives e^{2πa} = 2.71947 ≈ e.
- **Marcel's temporal-dynamic spiral time** does not: a linear phason phase
  and bounded window memory give a **constant** defect, D(k) grows linearly
  rather than logarithmically (D(10⁵) = 1333 against ln(1+k/75) = 7.2),
  measured ratio 1.0011 — on its own definitions not a log spiral, but a
  winding of constant pitch.
- The **φ geometry** HLV actually carries points to φ, not e: an equiangular
  spiral from the τ = φ cut-and-project would have factor φ = 1.618 per turn,
  or φ⁴ = 6.854 per 2π.

**No HLV strand, then, carries e.** As a bridge condition (P35): HLV's spiral
time would carry e only if its phase law contained a 1/n scale run; the given
definitions do not contain it. That is a candidate, not a derivation — and
**not a verdict on Marcel's framework**: the temporal-dynamic object is (per
his spiral-time paper) a cleanly defined object of open quantum dynamics
(unitary dilation on H_S ⊗ H_M, tested by process tensor, CP-divisibility,
hard reset, finite-bath comparison), hence belonging to the **dynamical**,
not the geometric category.

**FFGFT's time is not bound to one picture.** The non-closure exists
equivalently in two representations: geometrically as a log spiral (Doc. 295)
and in the Hilbert space as a **memory kernel** — the Fourier transform of the
discrete spectral density of the T⁴ connection-Laplacian (Doc. 283), a lossless
bijection H = L²(T⁴)⊗ℂ³ (Doc. 230/282). This is representational robustness, not
additional evidence (*translation is not justification*) — but it lets the
comparison be run in **kernel language**: FFGFT's kernel oscillatory /
discrete-spectral (revivals, BLP backflow 5.125), Marcel's decaying — the same
class, a different form (Doc. 283); precisely the 1/n scale run that carries e
is what the decaying kernel lacks.

### Basis and dimensions: same numbers, different meaning

The dimension counts coincide in **number**, not in meaning. FFGFT's *three*
is the internal ℂ³ / the Z₃ order on T⁴/Z₃ (a mode index); Marcel's *three*
is the triadic time (t, φ, χ). What is shared is the **Z₃** alone (C₃ < A₅),
not a common coordinate space. FFGFT's *six* is not native (only via the
embedding T⁷ = T⁴ × T³; FFGFT itself is 4D); Marcel's *six* is the Z⁶ parent
lattice of the cut-and-project (3 + 3). The only concretely established
overlap remains the φ-icosahedral shared object — one-sidedly verified
(FFGFT → HLV, Doc. 294) and filtration-sensitive.

### Status of the comparison

On the e-criterion the comparison is **negative**: the temporal-dynamic
object carries no ratio e, but golden-ratio / phason quasiperiodicity; the
basis question reduces to the shared Z₃. The category separation and the
dimension-by-dimension comparison are secured findings; the identification
remains a **bridge candidate**, currently **blocked** on the e-criterion. The
sharp residual question shifts to the *geometric* HLV object — whether the
factorised layer (A₅ singlet on S¹) knows a scale-invariant object testable
against e; in the available sources no such object is exhibited.

---

## Core derivations (as of v1.2.0)

| Result | Document |
|--------|----------|
| Derivation chain ξ → G → ℓ_P → L₀ | [Doc. 180](2/pdf/180_T0_L0_Herleitung_En.pdf) |
| Lepton masses from rational invariants | [Doc. 006](2/pdf/006_T0_Teilchenmassen_En.pdf) / [046](2/pdf/046_Teilchenmassen_En.pdf) |
| Koide scalar Q = 2/3 (computed) | [Doc. 258](2/pdf/258_Koide_2-3_En.pdf) / [259](2/pdf/259_Koide_Kreuzterme_En.pdf) |
| θ = 2/9 as Z₃-circulant phase | [Doc. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_En.pdf) |
| θ = 2/9 as a parameter-free C₃-in-A₅ geometry invariant (second witness) | [Doc. 293](2/PDFs/293_Ikosaeder_Theta_2_9_En.pdf) |
| Time-winding as a log spiral with ratio e | [Doc. 295](2/PDFs/295_Zeit_Logspirale_En.pdf) |
| α⁻¹ = 137.036, two independent E₀ routes | [Doc. 011](2/pdf/011_T0_Feinstruktur_En.pdf) / [292](2/PDFs/292_Leptonen_Empirie_Check_En.pdf) |
| SI bridge | [Doc. 013](2/pdf/013_T0_SI_En.pdf) |
| Hilbert-space bijection FFGFT ↔ QM | [Doc. 230](2/pdf/230_Hilbertraum_Uebersetzung_En.pdf) |
| Lepton empirics check, m_τ prediction, tolerance balance | [Doc. 292](2/PDFs/292_Leptonen_Empirie_Check_En.pdf) |
| Falsification: Casimir / redshift / lithium | [Doc. 220](2/pdf/220_Casimir_En.pdf) / [221](2/pdf/221_Rotverschiebung_En.pdf) / [222](2/pdf/222_Lithium_En.pdf) |

---

## Reproducibility

`2/Dok293_Skripte/` — icosahedral redistribution (p₀ = 2/9 exact, robustness
over random axes and the n-fold series), numpy-only.
`2/Dok294_Skripte/` — angle-spectrum discrimination of the shared object
(RMS-distance metric), numpy-only.
`2/Dok295_Skripte/` — time-winding: 75-closure, log spiral (ratio e), dual
time↔mass projection (factor 100 axis-symmetric); **new in v1.2.0:**
`spiralzeit_verhaeltnis_probe.py` (e-criterion: FFGFT carries e, Marcel's
spiral time carries 1, φ geometry carries φ⁴) and `basis_6d_achsen_probe.py`
(the six projected axes equiangular only at τ = φ), numpy-only.
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
