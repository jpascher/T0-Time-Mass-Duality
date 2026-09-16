# Release Notes — v1.4.0 (15 September 2026)

**DOI:** https://doi.org/10.5281/zenodo.22739112 — supersedes v1.3.9
Running corrections: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Change log: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows: all Standard Model
constants follow from a single dimensionless parameter **ξ = 4/30000** on a compact
4D torus T⁴/ℤ₃. The foundational relation is **T̃ · m = 1** — intrinsic time and mass
are inversely coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

This release introduces the new narrative book *Quantum Mechanics is Deterministic*
(DE+EN, 107/105 pp.) with full LaTeX sources, 10 Python verification scripts, and
a deterministic PC implementation of all quantum logic building blocks. The book is
available on Amazon Kindle and as a free PDF on Zenodo and GitHub.
No algebraic results from v1.3.9 are changed. No register entry required.

---

## New book: Quantum Mechanics is Deterministic

### *Quantenmechanik ist deterministisch / Quantum Mechanics is Deterministic*
*(DE+EN, 107/105 pp., 4 parts, 15 chapters, 3 appendices)*

**DOI:** https://doi.org/10.5281/zenodo.22739112
**GitHub sources:** https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/Sources/qmb-ch/
**Verification scripts:** https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/python/QMB_Skripte/

A narrative-format book covering the geometric reading of quantum mechanics through
FFGFT. Written for readers with basic knowledge of linear algebra and quantum
mechanics; no differential geometry required.

**Structure:**

| Part | Chapters | Content |
|------|----------|---------|
| I — Foundations | 1–3 | Carrier T⁴/ℤ₃, state space, time operator, entanglement as torus property |
| II — Bell | 4–7 | Bell's theorem, CHSH, no-go theorems (KS, PBR, Hardy, GHZ), CHSH resolution floor |
| III — Quantum Computing | 8–12 | Qubit formalism, algorithms, spin/QD, hardware, limits |
| IV — State Space | 13–15 | FFGFT↔Hilbert bridge, D₄ lattice, spectral theory, time and superposition |

**Appendices:** Symbol glossary (5 groups, all status markers) · Source list
(Docs. 022–365 + 20 external references with annotations) · AI assistance note.

---

## Key new results documented in the book

### Deterministic single-pass implementation [K]
The state bridge (z,r,θ)↔(α,β) is bijective. All quantum logic building blocks —
gates, Deutsch, Grover, Bell states, period finding, factor extraction — are
fully realized on a normal PC in a single deterministic pass. No quantum substrate,
no repetitions, no shot averaging required.

Verified by `pruef_logikbausteine.py`: H, X, Z, CNOT, X_frak (K_frak deviation
1.333%), Deutsch (constant/balanced, one run each), Grover (n=3..10, P>0.94),
Bell state (P(00)=P(11)=0.5 exact), period finding N=15..323 — all correct,
all deterministic.

IBM Kingston comparison (28 May 2026): Bell fidelity 0.9876±0.0028 over
50×2048 shots. PC result: identical in one single run.

### PC faster than QC — except QFT in superposition [K]
Modular exponentiation is demonstrably more expensive on a quantum circuit
(reversibility, uncomputation, Toffoli gates) than on a PC. The only genuine
quantum advantage is the QFT reading the period over all x simultaneously in
superposition: O((log N)³) vs O(N). This advantage exists in theory; it is
not technically RSA-relevant as of 2026 (RSA-2048 requires 4.1×10⁶ physical
qubits, 8.6×10⁹ gates). Gottesman-Knill: entanglement alone does not carry
the advantage.

### Mathematics analogy for instantaneity [K]
In standard mathematics, 2+2=4 holds instantaneously for all parts of the
expression — no one infers a physical nonlocality from that. The wave function
is a structural description, not a propagating process. In FFGFT: T̃·m=1 is a
local constraint at the same point in space, not a signal between distant points.
This is the precise reason apparent instantaneity in QM is not a causal problem.

### Bijective state bridge [K]
α = √((1+z)/2)·e^{iθ/2}, β = √((1-z)/2)·e^{-iθ/2}.
Inverse: z = |α|²−|β|², r = 2|αβ|, θ = arg(α)−arg(β).
Verified for 8 test points including poles, equatorial states, general points.
σ_z gate: θ→θ−π (not +π). Hadamard: H²=I verified. [K]

---

## Verification scripts (new): QMB_Skripte/

10 Python scripts, numpy only, no external dependencies:

| Script | Chapter | Tests | Status |
|--------|---------|-------|--------|
| pruef_hilbert_bridge.py | 13 | Bijectivity, norm, σ_z, Hadamard | ✅ all [K] |
| pruef_kfrak_gatter.py | 8 | K_frak=74/75, Δ=4/3%, infidelity, NISQ band | ✅ all [K] |
| pruef_qd_rbulk.py | 10 | N(22nm)=8.00, level ladder, E/kBT table | ✅ all [K] |
| pruef_dekohaerenz_xi.py | 10 | 9 GO span = 2·log₁₀(1/ξ_Higgs), T₂≤2T₁ | ✅ all [K] |
| pruef_kausalitaet.py | 3 | Δt=r/c, t_P≪attosecond, retarded Green's function | ✅ all [K] |
| pruef_xi_hierarchie.py | 8 | Zeeman vs kBT, photon energies, N_max=E/kBT | ✅ all [K] |
| pruef_chsh_signal.py | 12 | Δ_CHSH=ξ/2π≈2×10⁻⁵, Tsirelson, NISQ ratio | ✅ all [K/S] |
| pruef_xi_galois.py | 1 | ξ=(4/3)/10⁴, K_frak=74/75, Koide Q=3/2, Aut(D₄)=1152 | ✅ all [K/E] |
| pruef_pbit_barrier.py | 11 | Arrhenius τ=τ₀·exp(U/kBT), p-bit window at 22 nm | ✅ all [K] |
| pruef_logikbausteine.py | 8/9 | Gates, Deutsch, Grover, Bell, period finding | ✅ all [K] |

---

## Book-specific clarifications (not corrections to existing documents)

**CHSH resolution floor vs cumulative formula:**
The elementary FFGFT deviation Δ_CHSH = ξ/(2π) ≈ 2×10⁻⁵ per measurement (Ch. 12)
and the cumulative formula for N=73 qubits (Doc. 022, Doc. 147) are not directly
comparable and must not be equated (Ch. 7).

**Weyl obstruction scope:**
The Weyl obstruction (N(T)∼T ln T) applies to infinite arithmetic spectra, not to
finding a single period for a concrete N. Shor's algorithm is a finite task
requiring 2n+3 qubits; the obstruction does not apply to it (Doc. 176, [K]).

**Heron test interpretation:**
IBM Kingston Bell fidelity 0.9876±0.0028 is consistent with FFGFT and standard QM —
it is a consistency check, not a proof. The ξ-deviation lies 10³–10⁴× below
NISQ noise. Distinguishability requires N∼10⁹ measurement pairs. [K]

**Earlier 40× determinism report retracted:**
A prior evaluation over 3 runs had incorrectly reported 40× determinism versus QM.
This was a sampling artifact. The correct statement: results are identical within
measurement accuracy. [K]

---

## Amazon Kindle

The book is available as eBook, paperback, and hardcover in all markets:
- *Quantenmechanik ist deterministisch* (DE, 107 pp.)
- *Quantum Mechanics is Deterministic* (EN, 105 pp.)

---

## Corrections

None. The new book is a new document; no existing document required correction.
No register entry (R-entries apply only when older documents are corrected).

---

## Open bridges (unchanged from v1.3.9)

| Bridge | Status |
|--------|--------|
| CKM/PMNS angle values (numerical) | [S] (Doc. 348 Theorem D) |
| HRV Galois test: positive result | [S] requires controlled breathing ≥13 min, n≥5 |
| Generation assignment (ordering) | [S] (Doc. 346) |
| m_Pl and α_em(M_Z) from ξ | [S] |
| Quark/hadron sector | open (Doc. 318, R76) |
| CMB peaks {1,6,14,26}; \|n\|²=30 | open (P29/P31) |
| Δm²₃₂ mixing term F₅–F₇ | [S] |
| Torus T⁴/Z₃ as GALG polynomial | open |

## Entry point for new readers
Doc. 205 "FFGFT in Simple Language" (DE+EN, 13–14 pp.) remains the recommended
entry point for the physics. *Quantum Mechanics is Deterministic* is the recommended
entry point for the quantum mechanics and quantum computing perspective.

## What has not changed
ξ, T̃·m=1, and all algebraic results from v1.3.9 are unchanged.
All derivation chains from v1.3.6 are unchanged.
