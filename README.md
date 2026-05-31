# T0 Time-Mass Duality · FFGFT

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20474821.svg)](https://doi.org/10.5281/zenodo.20474821)

**FFGFT (Fundamental Fractal-Geometric Field Theory)** derives all Standard Model constants — particle masses, α, G, ℏ, c — from a single dimensionless parameter **ξ = 4/3 × 10⁻⁴** on a 4D identification torus T⁴. The foundational relation is **T̃ · m = 1** (time-mass duality). No free parameters. All constants are geometric consequences.

**Author:** Johann Pascher · johann.pascher@gmail.com  
**ORCID:** 0009-0000-6518-4064

---

## Platforms

| Resource | Link |
|----------|------|
| 🔬 Interactive Portal (Hugging Face) | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages (Tools & HTML) | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📦 Zenodo Archive v1.1.2 | [DOI 10.5281/zenodo.20474821](https://doi.org/10.5281/zenodo.20474821) |
| 🎵 Audio Library (Spotify) | [T0 Podcast](https://creators.spotify.com/pod/show/0PwnOIqjFepxA7NQ5i3fwR/episodes) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

## Core Results

- **Zero free parameters:** All 20+ Standard Model parameters derived from ξ
- **Particle masses:** 98% average accuracy from single formula
- **Fine structure constant:** α⁻¹ = 137.036 from fractal dimension D_f = 3 − ξ
- **Muon g-2:** 0.05σ agreement with experiment
- **Hubble tension:** ℏH₀/mₑc² = (π/2)·ξ¹⁰, 0.000% deviation
- **Hilbert-space bijection:** Full FFGFT ↔ standard QM translation (Doc. 230)
- **Falsification criteria:** Casimir (Doc. 220), Redshift (Doc. 221), Lithium (Doc. 222)

---

## Getting Started

| Step | Document |
|------|----------|
| 1. Conceptual overview | [T0_SI_En.pdf](2/pdf/013_T0_SI_En.pdf) — SI Reform 2019 and ξ |
| 2. Interactive exploration | [T0 Parameter Explorer](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 3. Field theory | [202_FFGFT_Feldtheorie_Gesamt_En.pdf](2/pdf/202_FFGFT_Feldtheorie_Gesamt_En.pdf) |
| 4. Hilbert-space bridge | [230_Hilbertraum_Uebersetzung_En.pdf](2/pdf/230_Hilbertraum_Uebersetzung_En.pdf) |
| 5. Plain language | [205_FFGFT_Narrativ_En.pdf](2/pdf/205_FFGFT_Narrativ_En.pdf) |
| 6. Python | `2/python/authentic_t0_quantum.py` |

---

## Current Release: v1.1.2 (May 2026)

**Focus: complete Kindle book series re-edition.** The book collection
is expanded from three to **five volumes** and now exists in three KDP
formats: eBook 6×9, Paperback 8.5×11, and Hardcover 8.25×11 — in both
German and English. Full details: **[RELEASE_NOTES_v1_1_2.md](RELEASE_NOTES_v1_1_2.md)**

What's new compared to v1.1.1:

- **Volumes 1–3 rebuilt** with all corrections since February 2026
  (HW147 correction in Doc. 147 §8, follow-up document updates, Doc. 230
  extended).
- **Volumes 4 and 5 added**, extending the collection by 74 documents
  added since the original three-volume conception — Hilbert-space
  bijection, falsification trilogy, layers/scale ladder, IPI bridges,
  black-hole information, dual ordering principles, epistemic
  self-positioning.
- **Each volume now in three KDP formats** (eBook + Paperback + Hardcover),
  in German and English: 30 PDFs in total.
- **Technical improvements:** all 650 tables in 206 ch files wrapped in
  `\adjustbox{max width=\textwidth}{...}` for Kindle width;
  `T0_preamble_patches.tex` adds missing environments; typo correction
  in `Teil2-end`.

---

## Previous Release: v1.1.1 (May 2026)

Adds 11 new documents across five clusters. Full details: **[RELEASE_NOTES_v1_1_1.md](RELEASE_NOTES_v1_1_1.md)**

**IPI Methodological Analysis**
- [240] KI-Detektoren und Ad-hominem-Argumentation (14/15 pp.) — manipulation patterns in scientific discourse

**FFGFT vs. External Frameworks**
- [245] FFGFT ↔ RA 2.1 (José Guevara) — layer-by-layer structural comparison
- [246] FFGFT ↔ RSG (Peter Austin) — convergences and divergences
- [247] Category Error Revisited — constructive reframing

**Black Hole Information**
- [250] Information and Black Holes — Hawking paradox via ontology/epistemology distinction; lattice dispersion correction ΔE/E = −(E/E_max)²/24
- [251] FFGFT ↔ Vopson Infodynamics — phenomenological convergence, not identity

**Number Theory & Signal Analysis**
- [252] Phillips sigma-orphan primes and FFGFT — {2,5,11} in 13-smooth ambient
- [253] Xi number-space dependence — ξ_num vs. ξ_FFGFT: unproven conjecture, facts stated

**Dual Ordering Principles**
- [254] Two Ordering Principles and the Area-Bound Theorem — resonance and entropy causally connected; Vopson's Second Law reproduced geometrically

---

## Previous Release: v1.1.0 (May 2026)

Centrepiece: **Hilbert-space bijection** (Docs. 230–232). Full details: **[RELEASE_NOTES_v1_1_0.md](RELEASE_NOTES_v1_1_0.md)**

Key documents:
- [230] FFGFT ↔ Hilbert-space QM — concrete bijection on qubit sector; ΔCHSH ~ 10⁻⁵ testable
- [231] Hilbert-space extensions for full FFGFT — four established mathematical structures
- [232] Quantum Graphity as hypothetical FFGFT subset — plausibility sketch
- [206] Triangle–matrix reduction theorem — six external frameworks tested
- [220–222] Falsification trilogy: Casimir / Redshift / Lithium

---

## Repository Structure

```
T0-Time-Mass-Duality/
├── 2/
│   ├── pdf/          # 250+ documents (DE/EN pairs)
│   ├── html/         # Interactive tools (21 files)
│   ├── python/       # Python implementations
│   └── fixed/
│       ├── ch/       # LaTeX chapter sources (*_ch.tex)
│       ├── wrapper/  # Standalone LaTeX wrappers
│       └── pri-end/  # Shared LaTeX preambles
├── books/            # NEW: KDP-ready PDFs (5 volumes × 2 langs × 3 formats)
├── rsa/              # RSA factorization demos
└── sig/              # Signal analysis tools
```

LaTeX structure: wrapper files in `2/fixed/wrapper/` reference `../pri-end/T0_preamble_standalone_De/En`. Chapter content in `2/fixed/ch/` as `NNN_..._De/En_ch.tex`.

---

## Published Books — Amazon KDP (v1.1.2)

The book collection is now a **five-volume series** in **three KDP formats**:

| Format | Size | KDP type | Page limit |
|--------|------|----------|------------|
| eBook | 6 × 9 in | Kindle eBook | ≤ 550 |
| Paperback | 8.5 × 11 in | KDP Print Paperback | ≤ 828 |
| Hardcover | 8.25 × 11 in | KDP Print Hardcover | ≤ 550 |

Each volume is available in both German and English.

| Volume | Content | Docs | eBook DE | Paperback DE | Hardcover DE |
|--------|---------|------|----------|--------------|--------------|
| Teil 1 | Foundations, ξ, constants, units | 40 | 533 | 452 | 459 |
| Teil 2 | Lagrangian, QFT, QM tests | 36 | 505 | 423 | 427 |
| Teil 3 | Cosmology, consciousness | 35 | 487 | 412 | 415 |
| Teil 4 | Early extensions (up to Doc. 184) | 37 | 473 | 407 | 414 |
| Teil 5 | Layers, Hilbert bridge, recent | 37 | 506 | 436 | 438 |

All page counts within KDP limits. PDF versions in `books/`.

Additional standalone editions (FFGFT Narrative Master "The Cosmic Brain",
T0 Anwendungen "Seven Mysteries of Physics", Von α=1 zur vollständigen
Physik) in `2/tex-n/completed/`.

---

## Version History

| Version | DOI | Key Content |
|---------|-----|-------------|
| v1.1.2 | [20474821](https://doi.org/10.5281/zenodo.20474821) | Complete book series re-edition (5 volumes × 3 KDP formats) |
| v1.1.1 | [20355305](https://doi.org/10.5281/zenodo.20355305) | IPI bridges, black hole information, dual ordering |
| v1.1.0 | [20117635](https://doi.org/10.5281/zenodo.20117635) | Hilbert-space bijection (centrepiece) |
| v1.0.14 | [20041543](https://doi.org/10.5281/zenodo.20041543) | Triangle–matrix reduction, falsification trilogy |
| v1.0.13 | [20041529](https://doi.org/10.5281/zenodo.20041529) | QM bridge, recursion operator |
| v1.0.12 | [20022166](https://doi.org/10.5281/zenodo.20022166) | Complete field theory |
| v1.0.11 | [18834145](https://doi.org/10.5281/zenodo.18834145) | Quantum computing series |

Full release notes available as `RELEASE_NOTES_*.md` files.

---

## License

© 2025–2026 Johann Pascher. Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

*Established results are documented in the corpus; open predictions are subject to experimental verification.*
