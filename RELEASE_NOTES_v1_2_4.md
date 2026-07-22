# Release Notes — v1.2.4 (July 2026)

**DOI:** (to be assigned upon Zenodo upload — supersedes v1.2.3 · [10.5281/zenodo.21396624](https://doi.org/10.5281/zenodo.21396624))

Running corrections: **[2/pdf/190_T0_Korrekturen_En.pdf](2/pdf/190_T0_Korrekturen_En.pdf)**  
Change log: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**  
A-Series log: **[A_Serie_Export/A_SERIE_CHANGELOG.md](A_Serie_Export/A_SERIE_CHANGELOG.md)**

---

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows:
all Standard Model constants follow from a single dimensionless
parameter **ξ = 4/30000** on a compact 4D torus T⁴. The foundational
relation is **T̃ · m = 1** — intrinsic time and mass are inversely
coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## What is new in v1.2.4

v1.2.4 introduces the **A-Series** — the canonical, topic-ordered edition
of FFGFT. All 43 documents carry explicit epistemic layer markers
([STIPULATION] / [K] / [B] / [S]); every computable statement has a
verification script. Three theoretical advances are the substantive core
of this release.

### Chirality g_R = 0 proved algebraically — A095 (new)

The left-handedness of the weak interaction was previously a [S] sketch.
**A095** raises it to [B]: the Fourier projector P₊ on the compact torus
annihilates the |1,−1⟩ winding state. Its kernel is non-trivial and
g_R = ⟨0|H|0⟩ = 0 follows directly — no free parameter, no additional
assumption beyond the torus geometry. Verification: `a095_torus_chiralitaet.py`.

### Gauge sector from torus topology — A192 (new)

Two of the three Standard Model gauge groups are now derived at [B] level:

- **U(1)_EM:** flux quantisation Φ = n · h/e on the compact torus forces
  the Aharonov–Bohm phase and yields the electromagnetic gauge group.
- **SU(3)_C:** three strands with linking number 3 generate exactly
  6 + 2 = 8 Gell-Mann generators; dim(su(3)) = 8 is proved geometrically
  from the winding structure, without input from the Standard Model.
- **SU(2)_L:** from the chiral projection of A095.

The remaining edge: the covariant derivatives D_μ = ∂_μ + igA_μ^aT^a
are not yet written out explicitly. Verification: `a192_eichsektor.py`.

### Native time–energy reciprocity — A060, register entry R50

The earlier argument against a singular beginning (Dok. 025/063) borrowed
from the Heisenberg energy–time uncertainty relation. Three defects were
identified: an inverted implication (finite Δt yields a *finite* bound,
not ΔE → ∞); a misapplication (Pauli: no self-adjoint time operator;
Mandelstam–Tamm Δt is an observable's change time, not a cosmic age);
and a breach of ledger style. The replacing chain is fully native:

T̃ · m = 1, hence **T · E = 1** (an equation, not an inequality).  
E → ∞ ⟺ T → 0; but FFGFT time carries a minimal increment
**d₁ = 100ξ₁ = 1/75**, fixed by ξ alone. Hence E is bounded above and
an infinite energy density is structurally excluded — the conclusion of
Dok. 025/063 is unchanged, the derivation is now native.

Booked as **R50** in Dok. 190. Dok. 025/063 are no longer authoritative
for this point; the native chain in A060 supersedes them.

### CHSH prefactor ξ/(2π) geometrically derived — A160

The factor 2π is the circumference of the unit circle — the natural
conversion between the torus winding phase and the measurement angle.
The cumulative formula CHSH(n) = 2√2 · exp(−ξ ln n / D_f) integrates
over D_f fractal dimensions; ln(n) counts the entanglement depth
logarithmically; D_f in the denominator encodes fractal self-consistency.
Both the per-measurement prefactor and the cumulative formula are now [B].

Hardware status: IBM Heron r2 (May 2026) confirms Bell violation
(S = 2.74, 96.9 % of the Tsirelson bound). The ξ effect (~10⁻⁵) is
below the device-to-device variation (~1.4 %) by a factor of ~1400 —
not resolvable with present NISQ hardware in principle (A165).

### Higgs-EFT deviation explained — A130

The 2.3 % gap between the ξ-derived α and the electroweak precision value
is explained structurally [S]: SI values are scheme-dependent (1-loop),
and fractal corrections in v are not cleanly separable from the loop
structure. ξ_EFT / K_frak^(3/2) ≈ 1.330 × 10⁻⁴; the remaining residual
is 0.3 %. This is a structural account, not a proof.

---

## The A-Series at a Glance

| Block | Documents | Theme |
|-------|-----------|-------|
| 0 | A010–A095 (13) | Foundation: stipulations, geometry, units, time |
| 1 | A100–A192 (16) | Sectors: leptons, constants, gravitation, QM, SM |
| 2 | A200–A250 (6) | Method: layers, falsifiability, open points |
| 3 | A260–A267 (8) | Extensions: Casimir, scale hierarchy, Dirac |

43 documents × 2 languages = 86 source files + 86 PDFs + 44 verification
scripts. All files in **[A_Serie_Export/](A_Serie_Export/)**.

---

## Correction Register Entries (this release)

| Entry | Affects | Description |
|-------|---------|-------------|
| R50 | Dok. 025/063/061/064/078 | Heisenberg singularity argument replaced by native T·E = 1 chain (A060) |

---

## Version History

| Version | DOI | Focus |
|---------|-----|-------|
| v1.2.4 | (pending) | **A-Series:** 43 canonical documents; A095 (g_R=0 [B]); A192 (U(1), SU(3) [B]); A060 R50; CHSH ξ/(2π) [B] |
| v1.2.3 | [21396624](https://doi.org/10.5281/zenodo.21396624) | Information question (Dok. 301/302); native T·E=1 (Dok. 306, R50–R53); time in state space (Dok. 307) |
| v1.2.2 | [21266963](https://doi.org/10.5281/zenodo.21266963) | SM as decompactified projection (Dok. 298); K_frak = 74/75 (Dok. 300) |
| v1.2.1 | [21203746](https://doi.org/10.5281/zenodo.21203746) | Time-winding as Hilbert-space memory kernel (Dok. 283/295/296/297) |
| v1.1.9 | [21193007](https://doi.org/10.5281/zenodo.21193007) | θ=2/9 as C₃-in-A₅ geometric invariant (Dok. 293/294/295) |
| v1.1.7 | [21158441](https://doi.org/10.5281/zenodo.21158441) | Lepton sector audit; α two-route overdetermination (Dok. 291/292) |
| v1.1.0 | [20117635](https://doi.org/10.5281/zenodo.20117635) | Hilbert-space bijection (Dok. 230/231/232) |

---

*Responsibility for content and errors rests entirely with the author.*
