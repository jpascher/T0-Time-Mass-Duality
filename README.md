# T0 Time-Mass Duality · FFGFT

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21821995.svg)](https://doi.org/10.5281/zenodo.21821995)

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


## The A-Series — Canonical Edition

The **A-Series** is the topic-ordered, fully auditable edition of FFGFT:
47 documents, every statement carrying an explicit epistemic layer marker.

| Marker | Meaning |
|--------|---------|
| **[STIPULATION]** | Axiom — declared, not derived |
| **[K]** | Core — derived from ξ, numerically verified |
| **[B]** | Bridge — algebraically proved |
| **[S]** | Sketch — plausible, not fully executed |
| **[Q]** | Source — external primary source or measured value |

```
Block 0  A010–A095   Foundation: stipulations, geometry, units, time, Hilbert space
Block 1  A100–A192   Sectors: leptons, constants, gravitation, QM, Standard Model
Block 2  A200–A250   Method: layers, falsifiability, open points, reference table
Block 3  A260–A273   Extensions: Casimir, scale hierarchy, Dirac, unit checks,
                     Z₃ sector, thermodynamics of computation
```

**New in the A-Series (July 2026):**

- **A095** — Chirality: g_R = 0 proved algebraically [B] from the torus projector P₊
- **A192** — Gauge sector: U(1)_EM from flux quantisation, SU(3)_C from linking
  number — both [B] from torus topology
- **A060** — Native time–energy reciprocity T·E = 1 replaces the earlier
  Heisenberg-based singularity argument (register entry R50)
- **A130** — Higgs-EFT 2.3 % deviation structurally explained
- **A160** — CHSH prefactor ξ/(2π) geometrically derived [B]
- **A271** — Landauer and phase-space accounting: the thermodynamic bound attaches
  to the region in phase space, not to the description; what is sufficient is the
  non-bijectivity of the region map [B]
- **A272** — Carrier and information: Landauer's proof holds for carrier operations
  over an equilibrium ensemble, not for abstract information
- **A273** — The reckoning bead: token computation separates accounting from thermal
  conversion; check script with 14 checks

All 47 documents with verification scripts:
**[A_Serie_Export/](A_Serie_Export/)** · **[A_SERIE_README.md](A_Serie_Export/A_SERIE_README.md)**

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

## Lepton Sector — masses, α, and the Koide phase

The charged-lepton mass operator is a **Z₃-circulant**, and diagonalising it
splits the sector cleanly into a **radial** (magnitude) and an **angular**
(phase) part. Everything FFGFT determines is radial: ξ, the hierarchy, the
Koide amplitude **Q = 2/3 = r√2**, the mean ⟨f⟩. The lepton empirical check
([Doc. 292](2/pdf/292_Leptonen_Empirie_Check_En.pdf)) audits this from the
data side and separates two layers that share ξ but must not be mixed: the
**circulant** carries the precision (μ/e to a few parts per million), the
**ξ ladder** carries the order of magnitude (~1%). Under **P42** the μ/e ratio
is a declared reference point; the one unavoidable test that remains is the
tau mass — FFGFT predicts **m_τ = 1776.97 MeV**, which Belle-II will decide.

**α is not a calibration.** It runs through two independent routes to the
characteristic energy E₀ — empirical (√(m_e·m_μ)) and purely geometric (from ξ
and m_μ alone, without m_e). The two meet to ~8·10⁻⁵: overdetermination, not a
fit. The ξ-ladder residuals follow a **generation-linear correction law**
(N_g ≈ g·N₀, exponents multiplicatively consistent), which is why a constant
correction cannot close the ladder; the base unit N₀ ≈ 38.6 is not yet derived.

### The Koide phase θ = 2/9 — the circulant phase

The angular offset **θ = 2/9** (radians) is **not a free parameter and not an
empirical fit**: it is the phase of the Z₃-circulant, the value the
diagonalisation *outputs* — found, not sought
([Doc. 291](2/pdf/291_Dynamischer_Ort_Theta_2_9_En.pdf)). It arises from the
Hilbert-space translation (Doc. 230/231/232 → 282), where the three lepton
masses appear as the spectrum of a Z₃-circulant and 2/9 falls out as the
diagonalisation angle.

An explicit, reproducible elimination chain then **characterises** it
positively — what 2/9 *is* by ruling out what it is not: not a symmetric
invariant (cos 3θ theorem), not countable/topological (2/9 rad transcendental
in 2π, Lindemann–Weierstrass), not fixed by the radial recursion, not a static
icosahedral angle. What it *is* is a **dynamical, magnitude-preserving holonomy
phase** with selector χ = π/2. The transcendence result is itself positive
knowledge: it proves 2/9 cannot come from any flat/topological source, so the
principle behind it is dynamical. The value is fixed and its origin
identified — the Koide phase is settled.

A **second, independent witness** of the same value comes from geometry
([Doc. 293](2/pdf/293_Ikosaeder_Theta_2_9_En.pdf)): embed the electron mode
of the C₃ fibre in the icosahedral group A₅ (C₃ < A₅) and apply the five-fold
rotation — the electron redistributes with denominator-9 weights, and the
weight into the trivial mode is **exactly 2/9**, with no 2/9 input, from
five-foldness alone (icosahedron-specific: 0/200 random axes hit the value).
Koide-2/9 (from the masses) and geometry-2/9 (from the redistribution) thus hit
the same value as a **convergence of two witnesses**; 2/9 is a
model-independent translation invariant. What remains open is only a direct
mechanism coupling the redistribution weights to the mass ratios without the
Koide detour — the value itself is doubly witnessed. **No** new particle
follows from the scale-free pattern (occupation is scale-bound, emptiness
theorem).

Reproducibility: `2/python/Dok292_Skripte/` (lepton check, parts A–L),
`2/python/Dok291_Skripte/` (θ=2/9 mechanism scripts),
`2/python/Dok293_Skripte/` (icosahedral redistribution, p₀=2/9 exact + robustness).

### Internal representations and computational routes

| Result | Document |
|--------|----------|
| Internal representation map — identity / bijection / projection; the Doc. 265 operator turned inward | [Doc. 287](2/pdf/287_Interne_Darstellungen_En.pdf) |
| Signal-engineering routes — Z₃-circulant DFT diagonalisation, Parseval, operator functions, convolution theorem, filter pole | [Doc. 288](2/pdf/288_NT_Rechenwege_En.pdf) |
| Magnitude/phase map of the four fermion sectors — leptons, quarks, neutrinos as the all-pass sector | [Doc. 289](2/pdf/289_Magnitude_Phase_Sektoren_En.pdf) |

The T⁴ geometry is the generative core; other representations relate to it by
identity (matrix algebra), lossless bijection (Hilbert space) or lossy
projection (information formalism). Because the mass operator is a Z₃-circulant,
the DFT diagonalises it — making eigenvalues a 3-point DFT, Koide Q a Parseval
one-liner and operator functions trivial — and the four fermion sectors sit on
one magnitude/phase map, with neutrinos as the pure phase (all-pass) sector.
Computational leverage and diagnosis, not new derivations.

Reproducibility scripts: `2/python/Dok288_Skripte/`, `2/python/Dok289_Skripte/`.

---

## Projection Chain and Methodology

The reduction T⁴ → T⁰ proceeds via three clearly distinct operation
types (Doc. 270): Type I preserves mode structure, Type II is lossy,
Type III is bijective (Hilbert representation). This classification
closes a family of pseudo-paradoxes about dimensional reduction.

The **correction register** (Doc. 190, K1–K6, P1–P44) records every
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
| 📦 Zenodo v1.2.8 | [DOI 10.5281/zenodo.21821995](https://doi.org/10.5281/zenodo.21821995) (supersedes v1.2.7 · [21628364](https://doi.org/10.5281/zenodo.21628364)) |
| 🎵 Spotify | [T0 Podcast](https://creators.spotify.com/pod/show/0PwnOIqjFepxA7NQ5i3fwR/episodes) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

## All Documents

A complete list of all ~289 documents with short description and direct PDF link:
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
│   └── pdf/                   # ~100 standalone A4 PDFs (selected key documents, De+En)
├── A_Serie_Export/            # A-Series canonical edition (43 docs × 2 languages)
│   ├── Sources/
│   │   ├── ch/                # 86 source files (43 De + 43 En, *_ch.tex)
│   │   ├── pri-end/           # 3 preamble files
│   │   └── wr_standalone_A4/  # 86 wrappers (43 De + 43 En)
│   ├── pdf/                   # 86 PDFs (43 De + 43 En, A???_*.pdf)
│   ├── python/
│   │   └── A_Serie_Skripte/   # 44 verification scripts
│   ├── A_SERIE_README.md
│   ├── A_SERIE_CHANGELOG.md
│   └── A_SERIE_WORKFLOW.md
├── Sources/                   # Recent LaTeX sources (latest documents)
│   ├── ch/                    # Chapter sources (*_De/En_ch.tex)
│   └── wr_standalone_A4/      # Standalone wrappers + PDFs
├── B18-sicherung/             # Archive / backup
├── Mails_Forscher_T0/         # Research correspondence
├── rsa/                       # RSA factorisation demos and signal tools
├── sig/                       # Signal analysis tools
├── 000_FFGFT_Changelog_De.md
├── DOCUMENTS.md               # complete document index
├── RELEASE_NOTES_v1_2_3.md
├── RELEASE_NOTES_v1_2_3_de.md
├── README_de.md
└── README.md
```

LaTeX: chapter sources in `Sources/ch/` as `NNN_..._De/En_ch.tex`;
wrappers in `Sources/wr_standalone_A4/`. A-Series fully compiled in
`A_Serie_Export/`.

---


## Docs. 308–310 — Cosmic Sector, Scale-Anchor Problem, Resonance Geometry (July 2026, DE+EN)

### Doc. 308 — The Cosmic Sector of FFGFT

Completely rewritten. Three cores, computed and proved:

**Redshift [K]:** Static universe, 1+z = e^(ξx), achromatic (all wavelengths same factor).
Degeneracy of SNe/BAO/CMB data between expansion and static reading (Doc. 267).
Λ (dark energy): reading artefact — all three conditions met, no reading-independent referent.

**Two-Halves Synthesis [K]:** K3 area invariance: T̃·m=1 (time half) and fractal path elongation
(space half) are complementary halves — each 0.875″, together 1.750″. γ_PPN=1 exactly (Cassini passed).
The same K3 structure carries the inertia transition: time cycle + space cycle = 4πR_H.

**Inertia regime [K]/[S]:** Force law a=√(a_N²+a_N·a₀), no free parameter.
a₀ = c²ξ¹⁰/(4λ̄ₑ) = 1.033×10⁻¹⁰ m/s² from ξ¹⁰ chain + Unruh + K3 cycles.
Note: a₀ is the **inertia transition scale** (T̃·m=1 + Unruh), not a gravitational parameter.
DDO 154 ratio 1.001; Bullet Cluster peak 10 kpc from galaxies.
Dark matter: "a regime, not a substance" — findings real, no particles required.

Verification: `2/Dok308_Skripte/ffgft_308_p44_stufe*.py` (4 scripts, no free parameters).
Documents: [DE](2/pdf/308_Lambda_Lesart_Artefakt_De.pdf) · [EN](2/pdf/308_Lambda_Lesart_Artefakt_En.pdf)

### Doc. 309 — The Scale-Anchor Problem

New document (not A-series). 9 pages DE+EN.

Both theories need a scale anchor — but differently:
- **ΛCDM:** ~6 free parameters, H₀ measured circularly (4-rung distance ladder), fine-tuning 10¹²³.
- **FFGFT:** ξ structure [K], magnitude 5⁴ [POSIT, P33]. Exponent 10 in H₀=(π/2)·c·ξ¹⁰/λ̄ₑ is the actual fit [POSIT, P20].
- **Inheritance (newly identified):** Exponent 10 calibrated to H₀_ΛCDM → FFGFT inherits the systematics of the expansion reading.
- **Cross-anchoring:** ξ¹⁰ reproduces both H₀ and a₀ — not expected from a pure H₀ fit.

Documents: [DE](2/pdf/309_Skalenanker_LCDM_FFGFT_De.pdf) · [EN](2/pdf/309_Skalenanker_LCDM_FFGFT_En.pdf)

### Doc. 310 — Resonance Geometry as the Overarching Reference

New document (not A-series). 13 pages DE+EN.

Answers the "ξ is fitted to the masses, hence circular" objection by correcting the hierarchy:
- **Overarching:** the geometry that possesses resonances — dimensionless, fixes all ratios.
- **Anchor:** a single measured value (one mass in SI) — carries no structure, only the scale (the tuning pitch, not the music).
- **Three [K] statements:** Koide Q=2/3 (from three masses, no ξ); the generation ladder as geometric sequence with ratio q=2/3 (same value as Koide Q); the harmonic prefactors 4/3, 16/5, 25/9. All verifiable against the measured masses.
- **π factors are geometry, not loops:** 16π³ = S²·2S³ (sphere surfaces of the T⁴ boundary); μ₀=4π×10⁻⁷ separates geometry (S²) from unit; in natural units μ₀,ε₀ vanish, and with α=1 (charge redefined, e=1) only ξ remains.
- **Mixing QM and RT is legitimate:** ℏ,c are both unit bridges; T·m=1 is the mixing itself; the conflict is interpretational, not formal (Doc. 230).

Verification: `2/Dok310_Skripte/ffgft_310_*.py` (4 scripts, no free parameters).
Documents: [DE](2/pdf/310_Resonanzgeometrie_Referenz_De.pdf) · [EN](2/pdf/310_Resonanzgeometrie_Referenz_En.pdf)

## Docs. 313 and 314 — Time Cycle and Lattice in Hilbert Space (August 2026, DE+EN)

### Doc. 314 — Lattice in Hilbert Space

Working document (not A-series). 26 pages DE / 25 EN, four verification
scripts.

What becomes of the D4 lattice under translation into Hilbert space:
the kissing number becomes the degeneracy, triality becomes the
orbifold and the fibre, the radius ratio becomes the level splitting.

- **Lattice theorems [K]:** |Aut(D4)| = 1152 = |W(F4)|, quotient over
  W(D4) is 6 = |S₃| (triality at the lattice, not only at the Dynkin
  diagram); the trace-(−2) class satisfies |det(1−A)| = 9 → **the
  T⁴/Z₃ orbifold with 9 fixed points is a lattice symmetry of D4**,
  not an added assumption; on every triple orbit the Z₃ acts as a
  ℂ³ circulant with {1, ω, ω²}.
- **A boundary, as a theorem [K]:** Aut(D4) has **no elements of order
  5** — 1152 = 2⁷·3², and 5 does not divide it (Lagrange). The
  fivefold symmetry that generates θ = 2/9 (Doc. 293) is incompatible
  with the D4 lattice structure. The phase test confirms it
  numerically: all invariants have denominator spectrum {1, 2, 3, 6};
  2/9 does not occur.
- **The doubling is admissible and prepared [K]:** the intersection of
  element orders of A₅ and Aut(D4) is {1, 2, 3} — the only possible
  interface is C₃, and triality occupies it. The −1 involution pairs
  the 8 triple orbits without fixed points: **24 = 8×3 = 4×6**, four
  ready containers with exactly the C₃ content that 3⊕3′ requires.
  What is excluded is not 2/9 but only its derivation *from* lattice
  invariants.
- **Time from the mass circle [K]:** λ₄·m = 2π is the de Broglie
  relation along the mass direction (a place relation, always exact);
  in time, T_osc·m = 2π/γ ≤ 2π, and for mass mixtures ≥ 2π by Jensen —
  exact only for the resting, sharp mode.
- **Rolled up versus unrolled [K]:** winding numbers are topological
  and fractal corrections require accumulation — the closure fork of
  Docs. 313/295 is therefore **spectrally invisible**, and
  D_f^space = 3 − ξ (local, 6.7×10⁻⁵) must be kept apart from
  K_frak = 1 − 100ξ (cumulative across the RG run, 1.33 %). Bare are
  only the SI absolute values via the anchor, not the rolled-up
  spectrum.
- **Casimir [K]:** the Z⁴ torus lies lower than the D4 torus
  (−0.932 versus −0.869 at covolume 1) — the densest lattice loses,
  because it has the largest spectral gap.

Verification: `2/python/Dok314_Skripte/` (4 scripts + README, all
target values as assertions).
Documents: [DE](2/pdf/314_Gitter_im_Hilbertraum_De.pdf) · [EN](2/pdf/314_Gitter_im_Hilbertraum_En.pdf)

### Doc. 313 — No Beginning (revised)

Two corrections (π/half turn as a condensate from Doc. 295;
gcd(74,75) = 1 as the reason closure occurs at exactly 75) and two
extensions:

- **Reach (F.4) [K]:** the usual backward extrapolation
  T(z) = T₀(1+z) presupposes *one* continuous thermodynamic chain —
  precisely the coarse-grained chaining that D(ii) leaves open. In the
  place reading, an early epoch has its own locally fixed equilibrium.
  The corpus demonstrates this on itself: T₀ is obtained structurally
  from ξ, not extrapolated. The Ω_m* chain is unaffected.
- **Robustness [K]:** criterion — no scale bridge, no duration, same
  level. Robust are counts (1152, 24, 9) and same-level ratios
  (α, m_μ/m_e, Koide Q). **The BBN observables are not**, including
  Y_p: T_f is not measured but follows from the model, and t/τ_n is a
  duration. Counter-check: the same classification applies to ΛCDM
  equally (Doc. 267, "none is circle-free").

Verification: `2/python/Dok313_Skripte/ffgft_bbn_skaleninvarianz.py`
Documents: [DE](2/pdf/313_Kein_Anfang_De.pdf) · [EN](2/pdf/313_Kein_Anfang_En.pdf)

---

## Doc. 315 — The Form of K_frak: Additive or Multiplicative? (August 2026, DE+EN)

Working document (not A-series). 10 pages DE / 10 EN, four verification
scripts (standard library only, exact fraction arithmetic).

The corpus confirms the **value** K_frak = 1 − 100ξ = 74/75 several
times independently (A040, A130, A270); whether this also
discriminates the **form** — additive against multiplicative
(1 − ξ)¹⁰⁰ — had remained unexamined. The two forms differ by exactly
the second binomial term 4950ξ² ≈ 8.9×10⁻⁵.

- **Control case Euler's musical spiral (5/7-limit):** exact closure is
  impossible (prime factorisation); best near-closures are the schisma
  (1.95 cents, 5-limit) and the ragisma 4375/4374 (0.40 cents,
  7-limit). Closure only through temperament = rationalising the step
  — precisely the rationality the ξ cycle (1/75, gcd(74,75) = 1)
  carries from the outset.
- **Three witnesses:** the A130 two-route ratio discriminates 7.5:1
  additive, conditional on the undeclared identity p = −(2−√3)
  (P-315-1, real residual ≈ 7 eV in m_e → P-315-2); the A270
  high-power location K⁻³⁶ ≈ 16/π² discriminates **31:1 additive**,
  with the reference upgraded via Doc. 314: **16/π² = 1/Δ(D4)**, the
  reciprocal D4 packing density (P35 narrowed to the coupling of the
  bulk exponent 36); the A040 power form tends additive but cannot
  resolve.
- **Structural argument:** the additive form is the exact winding
  bookkeeping of the rolled-up domain; the multiplicative one is the
  stepwise composition of the unrolled scale domain. Tied to the
  closure fork (Docs. 295/313/314): case B (frozen ξ) *is* the
  additive bookkeeping, case C (running ξ, equiangular spiral) *is*
  the multiplicative–logarithmic one — the Euler spiral is case C's
  picture.
- **Status:** value [K]; form additive [B], twice conditionally
  confirmed; the multiplicative alternative is consistently
  disfavoured by both conditional witnesses and supported by none.
  Unconditional decision line: the A270 baryon location (K³⁸ level,
  form distance 0.34 %).

Verification: `2/python/315_Skripte/` (4 scripts).
Documents: [DE](2/pdf/315_Kfrak_Form_De.pdf) · [EN](2/pdf/315_Kfrak_Form_En.pdf)

---

## Correction Register & Changelog

The **correction register** [Doc. 190](2/pdf/190_T0_Korrekturen_De.pdf)
documents every correction and refinement with date, status, and
affected documents — K1–K7 (corrections) and R1–R74 (refinements/programme, as of 6 August 2026).
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

The full version history with DOIs is given in the release notes:
**[RELEASE_NOTES_v1_2_8.md](RELEASE_NOTES_v1_2_8.md)** · change log:
**[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**

---

## License

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

*Established results are documented in the corpus; open predictions
are subject to experimental verification.*
