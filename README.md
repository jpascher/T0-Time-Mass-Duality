# T0 Time-Mass Duality · FFGFT

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20640799.svg)](https://doi.org/10.5281/zenodo.20640799)

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows:
all Standard Model constants follow from a single dimensionless
parameter **ξ = 4/30000** on a compact 4D torus T⁴. The foundational
relation is **T̃ · m = 1** — intrinsic time and mass are inversely
coupled.

**Author:** Johann Pascher · johann.pascher@gmail.com  
**ORCID:** 0009-0000-6518-4064

---

## The Theory in Three Statements

**1. One parameter carries everything**  
ξ = 4/30000 is not a measured quantity but a geometric consequence
of the fractal Hausdorff dimension D_f = 3 − ξ of space. From ξ
follow lepton masses, fine-structure constant α, gravitational constant
G, and the minimal length L₀ = ξ · ℓ_P — without free parameters,
without SI adjustment at this level.

**2. Time and mass are the same object**  
T̃ · m = 1 is not a postulate about clocks but a compactification
relation on T⁴: one of four circles carries both mass and time
simultaneously. It follows that ħ and c are SI conversion factors —
not ontological primitives. E = mc² and E = m are the same statement
in different units (Doc. 077).

**3. Ratios are the actual content**  
Physics divides into two layers (Doc. 241): Layer 1 is ratio-based,
parameter-free, exact — mass and coupling ratios without units.
Layer 2 adds a single SI anchor (e.g. the electron mass) and computes
all absolute values from it. The separation makes the theory auditable:
what is input and what follows is always declared explicitly.

---

## Core Derivations

| Result | Document |
|--------|----------|
| Complete chain ξ → G → ℓ_P → L₀ | [Doc. 180](2/pdf/180_T0_L0_Herleitung_En.pdf) |
| Lagrangian with T̃·m=1; Feynman rules | [Doc. 019](2/pdf/019_T0_lagrndian_En.pdf) |
| Lepton masses from rational invariants r_i, p_i | [Doc. 006](2/pdf/006_T0_Teilchenmassen_En.pdf) / [046](2/pdf/046_Teilchenmassen_En.pdf) |
| Koide scalar Q_FFGFT = 0.6677 (computed, not fitted) | [Doc. 258](2/pdf/258_Koide_2-3_En.pdf) / [259](2/pdf/259_Koide_Kreuzterme_En.pdf) |
| α⁻¹ = 137.036 from D_f = 3 − ξ | [Doc. 011](2/pdf/011_T0_Feinstruktur_En.pdf) / [043](2/pdf/043_ResolvingTheConstantsAlfa_En.pdf) |
| SI bridge: all constants from ξ | [Doc. 013](2/pdf/013_T0_SI_En.pdf) |
| E = mc² = E = m: unit identity | [Doc. 077](2/pdf/077_E-mc2_En.pdf) |
| Natural units, static and correction-free | [Doc. 261](2/pdf/261_NatEinheiten_Statisch_En.pdf) |
| Two-layer structure (ratio / SI) | [Doc. 241](2/pdf/241_Zwei_Schichten_En.pdf) |

---

## Quantum Sector

| Result | Document |
|--------|----------|
| QFT quantisation with natural UV cutoff | [Doc. 020](2/pdf/020_T0_QM-QFT-RT_En.pdf) |
| Hilbert-space bijection FFGFT ↔ standard QM | [Doc. 230](2/pdf/230_Hilbertraum_Uebersetzung_En.pdf) |
| Four Hilbert-space extensions (deformed SU(2), …) | [Doc. 231](2/pdf/231_Hilbertraum_Erweiterung_En.pdf) |
| Bell statistics: geometrically real on T⁴, no action at distance | [Doc. 023](2/pdf/023_Bell_En.pdf) / [230](2/pdf/230_Hilbertraum_Uebersetzung_En.pdf) |
| Dimension flow d_s: 2 (UV) → 4 (IR) | [Doc. 141](2/pdf/141_Renormierung_En.pdf) |
| T0-compiled quantum computer | [Doc. 034](2/pdf/034_T0_QM-optimierung_En.pdf) |

---

## FFGFT ↔ HLV Bridge (Information Physics Institute)

A sustained structural comparison with Marcel Krüger's HLV / Spiral-Time
framework. The shared object is a **Z₃-circulant mass operator** on the
C₃ axis of a common icosahedral (A₅) geometry, where FFGFT's 3-fold and
HLV's 5-fold structures coexist.

| Result | Document |
|--------|----------|
| FFGFT↔HLV containment, CP, divisibility; Koide-phase elimination | [Doc. 282](2/pdf/282_FFGFT_HLV_CP_Teilbarkeit_En.pdf) |
| The bridge: shared Z₃-circulant, C₃<A₅, r=√2 vs 2/√5 | [Doc. 283](2/pdf/283_FFGFT_HLV_Bruecke_En.pdf) |
| Spiral-Time / neural-coherence formula analysis (claim boundaries) | [Doc. 284](2/pdf/284_FFGFT_Spiralzeit_Medin_En.pdf) |
| Dimension bridge: the 6 = 3⊕3′ doubling, T⁴→T⁷ | [Doc. 285](2/pdf/285_FFGFT_HLV_Dimensionsbruecke_En.pdf) |
| Dynamic/kinetic sector: AM-sideband ½, mode-locking, ξ¹ null-mode lift | [Doc. 286](2/pdf/286_Dynamischer_Sektor_Kinetik_En.pdf) |

Reproducibility scripts: `2/Dok286_Skripte/` (numpy-only, seeded).

### The Koide offset θ = 2/9 — localised, not derived

The charged-lepton mass operator factorises into a **radial** (magnitude)
and an **angular** (phase) sector. Everything FFGFT determines is radial —
ξ, the hierarchy, the Koide amplitude **Q = 2/3 = r√2**, the mean ⟨f⟩. The
one remaining empirical input is the **angular offset θ = 2/9** (radians).

An explicit elimination chain (reproducible) establishes what θ is **not**:

- **not a symmetric invariant** — the entire θ-dependence runs through cos 3θ, so every Z₃-invariant functional extremises at nπ/3, never 2/9 (cos 3θ theorem);
- **not counting/topological** — 2/9 rad is transcendental in 2π (Lindemann–Weierstrass), hence not a root of unity;
- **not fixed by the radial recursion** — θ does not appear in the fixed-point condition (radial–angular orthogonality);
- **not a static geometric angle** — 2/9 rad = 12.73° is not an icosahedral axis angle (strictly checked; control arccos(1/√5) = 63.43° lands exactly).

What remains is a **dynamical, angular** principle — a magnitude-preserving
(all-pass) holonomy phase — which sits structurally on the HLV side
(Krüger's BD17A boundary-holonomy mechanism). In signal terms: the mass
operator is a Z₃-circulant, DFT-diagonalised, so √2 is the magnitude and θ
the phase of the spectral coefficients — and **a magnitude spectrum does not
fix the phase spectrum**. The empirical value is settled to ~4 significant
figures; the theoretical forcing is the one open target, now precisely
circumscribed. This is an honestly declared open result, not a derivation.

---

## Projection Chain and Methodology

The reduction T⁴ → T⁰ proceeds via three clearly distinct operation
types (Doc. 270): Type I preserves mode structure, Type II is lossy,
Type III is bijective (Hilbert representation). This classification
closes a family of pseudo-paradoxes about dimensional reduction.

The **correction register** (Doc. 190, K1–K4, P1–P38) records every
correction and refinement with date and status. Nothing is silently
overwritten. Errors in earlier script versions are archived as
documented error states, not deleted.

**Three-layer methodology:** Layer 1 — proved from ξ; Layer 2 —
algebraically proved bridges; Layer 3 — plausibility sketches,
declared as such. Negative results are explicitly admitted outcomes.

---

## Falsification Criteria

Explicitly stated and testable:

- **Casimir effect** ([Doc. 220](2/pdf/220_Casimir_En.pdf)): modified force at sub-Planck distances
- **Cosmological redshift** ([Doc. 221](2/pdf/221_Rotverschiebung_En.pdf)): difference from metric expansion at high z
- **Lithium problem** ([Doc. 222](2/pdf/222_Lithium_En.pdf)): primordial abundances from FFGFT nuclear physics

ΔCHSH ~ ξ ≈ 10⁻⁴ lies below current NISQ noise but is in principle
measurable (Doc. 230).

---

## Platforms

| Resource | Link |
|----------|------|
| 🔬 Interactive Portal | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📦 Zenodo | v1.1.6 _(DOI pending)_ · last published [v1.1.3 — 10.5281/zenodo.20640799](https://doi.org/10.5281/zenodo.20640799) |
| 🎵 Spotify | [T0 Podcast](https://creators.spotify.com/pod/show/0PwnOIqjFepxA7NQ5i3fwR/episodes) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

## All Documents

A complete list of all ~286 documents with short description and direct PDF link:
**[DOCUMENTS.md](DOCUMENTS.md)**

---

## Getting Started

| Step | Document |
|------|----------|
| 1. Overview | [013_T0_SI_En.pdf](2/pdf/013_T0_SI_En.pdf) |
| 2. Interactive | [T0 Parameter Explorer](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 3. Field theory | [202_FFGFT_Feldtheorie_Gesamt_En.pdf](2/pdf/202_FFGFT_Feldtheorie_Gesamt_En.pdf) |
| 4. Hilbert space | [230_Hilbertraum_Uebersetzung_En.pdf](2/pdf/230_Hilbertraum_Uebersetzung_En.pdf) |
| 5. Plain language | [205_FFGFT_Narrativ_En.pdf](2/pdf/205_FFGFT_Narrativ_En.pdf) |
| 6. Python | `2/python/authentic_t0_quantum.py` |

---

## Repository Structure

```
T0-Time-Mass-Duality/
├── 2/
│   ├── pdf/                   # 286+ documents (DE/EN pairs)
│   ├── html/                  # Interactive tools
│   ├── python/                # Python implementations
│   ├── Sources/               # LaTeX sources
│   │   ├── ch/                # Chapter sources (*_De/En_ch.tex)
│   │   ├── wr_standalone_A4/  # Standalone document wrappers
│   │   ├── wr_books/          # Book wrappers (5 volumes × 3 formats)
│   │   └── pri-end/           # Shared preambles
│   ├── PDFs/                  # Standalone A4 documents (DE/EN)
│   ├── Dok023_230_Skripte/    # Scripts: Bell / Hilbert space
│   ├── Dok263_Skripte/        # Scripts: fractal holography
│   ├── Dok267_268_Skripte/    # Scripts: CMB peaks
│   ├── Dok271_274_Skripte/    # Scripts: HLV comparison
│   └── Dok275_Skripte/        # Scripts: ξ→φ recursion (v2/v3/v4)
├── books/                     # KDP-ready PDFs (5 vols × 2 langs × 3 formats)
├── rsa/                       # RSA factorisation demos
├── sig/                       # Signal analysis tools
├── 000_FFGFT_Changelog_De.md
├── README_de.md
└── README.md
```

LaTeX structure: wrappers in `2/Sources/wr_standalone_A4/` and `2/Sources/wr_books/`
reference preambles from `2/Sources/pri-end/`. Chapter content in
`2/Sources/ch/` as `NNN_..._De/En_ch.tex`.

---

## Correction Register & Changelog

The **correction register** [Doc. 190](2/pdf/190_T0_Korrekturen_De.pdf)
documents every correction and refinement with date, status, and
affected documents — K1–K4 (errors) and P1–P38 (refinements).
Nothing is silently overwritten.

The **changelog** [`000_FFGFT_Changelog_De.md`](000_FFGFT_Changelog_De.md)
records all running changes to the corpus chronologically.

---

## Books (Amazon KDP)

The FFGFT book series is available on Amazon KDP as a **five-volume series** —
in three formats (Kindle eBook / Paperback 8.5×11 / Hardcover 8.25×11)
in both German and English (30 PDFs total).

| Volume | Content | Docs |
|--------|---------|------|
| Teil 1 | Foundations, ξ, constants, units | 40 |
| Teil 2 | Lagrangian, QFT, QM tests | 36 |
| Teil 3 | Cosmology, consciousness | 35 |
| Teil 4 | Early extensions (up to Doc. 184) | 37 |
| Teil 5 | Layers, Hilbert bridge, recent clarifications | 37 |

PDF versions of all volumes also in the repository under `books/`.

Additional standalone editions: *FFGFT Narrative — The Cosmic Brain*,
*T0 Applications — Seven Mysteries of Physics*,
*From α=1 to Complete Physics* (in `2/tex-n/completed/`).

---

## Version History

| Version | DOI | Focus |
|---------|-----|-------|
| v1.1.6 | _(pending Zenodo upload)_ | FFGFT↔HLV bridge (Doc. 282–286), Koide-phase θ=2/9 elimination, dynamic/kinetic sector |
| v1.1.3 | [20640799](https://doi.org/10.5281/zenodo.20640799) | Koide sector, projection chain, CMB, ξ→φ revised |
| v1.1.2 | [20474821](https://doi.org/10.5281/zenodo.20474821) | Book series (5 volumes, 3 KDP formats) |
| v1.1.1 | [20355305](https://doi.org/10.5281/zenodo.20355305) | Black hole information, dual ordering |
| v1.1.0 | [20117635](https://doi.org/10.5281/zenodo.20117635) | Hilbert-space bijection |
| v1.0.14 | [20041543](https://doi.org/10.5281/zenodo.20041543) | Triangle–matrix reduction |

---

## License

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

*Established results are documented in the corpus; open predictions
are subject to experimental verification.*
