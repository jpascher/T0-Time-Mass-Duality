# T0-Time-Mass-Duality / FFGFT — Release Notes v1.1.1

**DOI:** [10.5281/zenodo.20355305](https://doi.org/10.5281/zenodo.20355305)  
**Date:** 2026-05-23  
**Predecessor:** [10.5281/zenodo.20117635](https://doi.org/10.5281/zenodo.20117635) (v1.1.0)  
**Repository:** https://github.com/jpascher/T0-Time-Mass-Duality

---

## This is a point release — the main reference remains v1.1.0

The consolidated entry point for the entire FFGFT corpus is **v1.1.0** (DOI: 10.5281/zenodo.20117635), whose centrepiece is the **Hilbert-Space Triptych** (Docs. 230, 231, 232): a carried-out bijection between FFGFT mode formalism and standard Hilbert-space quantum mechanics, with a testable Δ_CHSH ≈ 10⁻⁵ deviation.

v1.1.1 adds eleven new documents produced in the context of active IPI mailing-list correspondence and new theoretical development. No existing derivations or predictions have been changed.

The foundational framework remains unchanged:

- **Single parameter:** ξ = 4/30000 = 1.333×10⁻⁴  
- **Foundational relation:** T̃·m = 1  
- **Minimal length:** L₀ = ξ·ℓ_P ≈ 2.155×10⁻³⁹ m  
- **Methodological levels:** (1) core derivations proved from ξ, (2) bridges algebraically proved, (3) reductions as plausibility sketches

---

## New Documents in v1.1.1 (Docs. 240, 245–254)

### IPI Methodological Analysis

**Doc. 240 — KI-Detektoren und Ad-hominem-Argumentation** (14/15 pages DE/EN)  
Structural analysis of manipulation patterns in scientific discourse: classical ad-hominem and AI-detector-based dismissal. Key sources: Liang et al. 2023, OpenAI classifier shutdown July 2023, Festinger 1956/1957. A methodological document, not FFGFT physics.

### FFGFT Compared to External IPI Frameworks

**Doc. 245 — FFGFT and RA 2.1** (José Guevara)  
Structural comparison of FFGFT's ξ-recursion and winding-number architecture with Guevara's Recursive Abstraction 2.1. Layer-by-layer correspondence table; convergences and irreducible differences explicitly identified.

**Doc. 246 — FFGFT and RSG** (Peter Austin)  
Systematic comparison of FFGFT's topological invariants with Austin's Recursive Survival Grammar. Convergence on constraint-first architecture (UC Layer 0); divergence on ontological commitments clearly stated.

**Doc. 247 — Category Error — Revised Framing**  
Replaces the earlier sharp "category error" framing in IPI bridge discussions with a more constructive "admissibility condition" framing, consistent with Doc. 206.

### Black Hole Information and Hawking Radiation

**Doc. 250 — FFGFT — Information and Black Holes** (7/6 pages DE/EN)  
Resolves the Hawking information paradox through the ontology/epistemology distinction: topological winding numbers are preserved as topological charge (not epistemically recoverable). Core derivation: the **spectrum modification from lattice dispersion** (Debye-analog):

    E(k) = (2ℏc/L₀) sin(kL₀/2)    →    ΔE/E = −(E/E_max)²/24

Derived, not assumed. Honest scale assessment: ~10⁻⁸⁶ for real black holes, significant only at the remnant scale M_crit ≈ 10⁻¹³ kg. Algebraic protection T̃·m = 1 (Doc. 078). Python-verified key numbers. **Methodological status: core derivation (Level 1) for the algebraic protection; Level 2 bridge for the lattice-dispersion spectrum modification.**

**Doc. 251 — FFGFT and Vopson's Infodynamics — Comparison**  
FFGFT's node-count account and Vopson's particle-state account count different things; they converge in phenomenology but not in identity. Honest translation, not merger.

### Number Theory and Signal Analysis

**Doc. 252 — Phillips sigma-Orphan Primes and FFGFT**  
Python-verified finding: sigma-orphan primes in the 13-smooth ambient ⟨2,3,5,7,11,13⟩ are exactly {2,5,11} — and 5,11 are precisely the middle terms of the cubic sequence 3→5→11→1321. Connection to ξ⁻¹ = 7500 = 3·2²·5⁴; σ(15) = σ(14) = 24 = 4! = |S₄|. Cubical formula unknown; open questions explicitly stated.

**Doc. 253 — Xi Number-Space Dependence**  
Unresolved question documented: ξ_num(N) = λ(N)/N lies in [0.008–0.49], fully determined by gcd(p−1,q−1); geometric ξ_FFGFT = 1.333×10⁻⁴ lies far outside. Factorisation number-space dependence is real classical number theory; the connection to FFGFT geometry remains an unproven conjecture. **The facts are what they are.** Missing: algebraic bridge proof.

### Dual Ordering Principles

**Doc. 254 — Two Ordering Principles and the Area-Bound Theorem** (5/5 pages DE/EN)  
Resolves the apparent contradiction between the resonance principle (ξ-recursion selects stable configurations) and the thermodynamic principle (entropy maximises). The **area-bound theorem** derives — not postulates:

    N_max ∝ A  +  A ∝ M² (Hawking)  +  L₀ lower bound  →  capacity necessarily decreases

The entropic principle drives evaporation, thereby forcing the resonant concentration of preserved topological charge: the two principles are causally connected, not opposed. Vopson's Second Law of Infodynamics reproduced phenomenologically through geometry rather than postulated as a new law. Python-verified (infodynamik.py, kapazitaet.py).

**Three open proof gaps explicitly named:**
1. Correct topological charge Q — must scale ≤ M² to remain consistent with N_max
2. Extremal principle — ξ fixed point as minimum of an information functional (not yet derived)
3. Definition of information entropy in FFGFT (not yet precisely stated)

---

## Version History

| Version | DOI | Date | Key Addition |
|---------|-----|------|-------------|
| v1.1.1 | **[10.5281/zenodo.20355305](https://doi.org/10.5281/zenodo.20355305)** | 2026-05-23 | Docs. 240, 245–254: IPI bridges, black hole information, dual ordering principles |
| **v1.1.0** | **[10.5281/zenodo.20117635](https://doi.org/10.5281/zenodo.20117635)** | **2026-05-11** | **Hilbert-Space Triptych (Docs. 230–232) — main consolidated release** |
| v1.0.14 | [10.5281/zenodo.20041543](https://doi.org/10.5281/zenodo.20041543) | 2026-05 | Triangle-Matrix Reduction, Falsification Trilogy, Docs. 206–210, 220–222 |
| v1.0.13 | [10.5281/zenodo.20041529](https://doi.org/10.5281/zenodo.20041529) | 2026-05 | QM bridge, narrative translation, Doc. 205 |
| v1.0.12 | [10.5281/zenodo.20022166](https://doi.org/10.5281/zenodo.20022166) | 2026-05 | Complete field theory, recursion operator, Docs. 202–204 |
| v1.0.11 | [10.5281/zenodo.18834145](https://doi.org/10.5281/zenodo.18834145) | 2026-03 | Initial corpus release |

**Recommended citation target: v1.1.0** (10.5281/zenodo.20117635) as the consolidated main release.

---

## How to Cite

For the framework:
> Pascher, J. (2026). T0-Time-Mass-Duality / FFGFT v1.1.0 — Hilbert-Space Bridge: A Consolidated Release. Zenodo. DOI: [10.5281/zenodo.20117635](https://doi.org/10.5281/zenodo.20117635).

For this point release:
> Pascher, J. (2026). T0-Time-Mass-Duality / FFGFT v1.1.1 — IPI Bridges, Black Hole Information, Dual Ordering Principles. Zenodo. DOI: [10.5281/zenodo.20355305](https://doi.org/10.5281/zenodo.20355305).

---

*Zenodo DOI assigned: 10.5281/zenodo.20355305.*
