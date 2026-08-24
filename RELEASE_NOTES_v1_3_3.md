# Release Notes — v1.3.3 (August 2026)

**DOI:** to be assigned on Zenodo publication — supersedes v1.3.1 and v1.3.2  
Running corrections: **[2/pdf/190_T0_Korrekturen_En.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_En.pdf)**  
Archived register: **[2/pdf/190_T0_Korrekturen_Archiv_En.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_Archiv_En.pdf)**  
Change log: **[000_FFGFT_Changelog_De.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/000_FFGFT_Changelog_De.md)**  
A-series log: **[A_Serie_Export/A_SERIE_CHANGELOG.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/A_Serie_Export/A_SERIE_CHANGELOG.md)**

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows: all Standard Model
constants follow from a single dimensionless parameter **ξ = 4/30000** on a compact
4D torus T⁴. The foundational relation is **T̃ · m = 1** — intrinsic time and mass
are inversely coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

This release consolidates the work since v1.3.1: four new documents (324–327),
the restructuring of the correction register, and the correction of the neutrino
sector. Register entries R84 through R87 are included.

**The focus lies on two closed bridges.**

Doc. 325 works out the **microscopic Hawking mechanism** entirely from
FFGFT-native building blocks — Doc. 313 (Ch. G) had laid the thermodynamic frame
but booked the emission side as a sketch [S]. The central finding: the Hawking
quantum is the system-dependent bit of the horizon scale,
k_B·T_H = ħc/(4π·r_s) = E_bit(4π·r_s) exactly. No universal bit value is needed
anywhere (R85).

Doc. 327 proves the **self-adjointness of the fundamental fractal operator F̂** —
the question open since Doc. 322 (R82), on which the well-posedness of
ξ = λ_min(F̂) depended. The proof introduces no new axioms and leaves **no
remaining cases**: the deficiency-index classification does not arise under FFGFT
structures at all, because L₀ = ξ·ℓ_P makes the scale ladder finite. There are no
infinities in FFGFT (R86).

Both results share one algebraic root: the ℤ₃ sector pairing (k,−k) that carries
the Hawking information in Doc. 325 generates the symmetry F̂ = F̂† in Doc. 327 —
there it is not a requirement but a consequence of the orbifold structure.

Alongside, Docs. 324 and 326 compare Douglas Matzke's algebra frameworks with
FFGFT: Doc. 324 closes with the Casimir derivation ξ = C₂(SU(3))/N_Fourier (R84),
Doc. 326 works out the bit-value divergence — universal (Matzke, Landauer at T_P)
vs. system-dependent (FFGFT, E_bit = ħc/L).

**Doc. 190 has been restructured**: with 87 entries and 69 pages the register had
become unwieldy. The extended edition is frozen as Doc. 190-Archive; the new
compact register lists all entries in tabular form and closes with the
consolidated list of open bridges. The append-only principle remains unchanged.

**The neutrino sector has been corrected** (R87): in Doc. 320 the evaluation of
ξ^(9/5) was faulty; the mass formula and exponents were always correct. The
deviation in Δm²₃₂ is +16.0 % instead of the −22 % booked previously.

## Entry point for new readers

Doc. 205 "FFGFT in Simple Language" (DE+EN, 13–14 pages) remains the recommended
entry point. The single open falsification test is unchanged and explicitly named:
m_τ = 1776.97 MeV, to be decided by Belle II, with no escape route.

## What has not changed

ξ, the foundational relation T̃ · m = 1, and all derivation chains are unchanged.
Doc. 327 secures well-posedness; it changes no numerical value.

---

## New documents since v1.3.1

### Doc. 324 — G(6,ℤ₃C) vacuum structure and FFGFT (DE+EN, 9 pp. each)

Numerical investigation of the connection questions between Matzke's
G(6,ℤ₃C) vacuum structure and FFGFT spectral theory.

- **Trine theorem [B]:** T_k³ = 1 in the 8-dim spinor representation (δ < 6.5×10⁻¹⁶).
- **Vacuum operator V [B]:** rank-1 projector, spectrum {0⁽⁷⁾, 1⁽¹⁾}.
- **ξ not a spectral value [K]:** closed negative finding.
- **Casimir derivation [K]:** ξ = C₂(SU(3)_fund)/N_Fourier = (4/3)/10⁴ = 4/30000,
  with C₂ = 4/3 from N_c = 3 [B] (Doc. 321) and N_Fourier = 10⁴ from the T⁴
  topology. The physical Casimir effect (Doc. 009) and the algebraic Casimir
  operator independently yield the same factor 4/3. (R84)

Verification script: 16 assertions.

→ [DE](2/pdf/324_G6_Z3C_FFGFT_Vergleich_De.pdf) · [EN](2/pdf/324_G6_Z3C_FFGFT_Vergleich_En.pdf)

### Doc. 325 — The FFGFT Hawking Mechanism (DE+EN, 7 pp. each)

Closes the emission side of Doc. 313 Ch. G from FFGFT-native building blocks
(R85). The five building blocks:

1. **Temperature [K]** — KMS rule T = ħ/(k_B·τ) with membrane period
   τ = 8πGM/c³ from T̃·m = 1; one principle for Unruh, Gibbons-Hawking and
   black holes.
2. **Quantum [K]** — k_B·T_H = ħc/(4π·r_s) = E_bit(4π·r_s) exactly:
   the Hawking quantum is the bit of the horizon scale.
3. **Selection [B]** — only T_R = 0 escapes; absorption of the partner quantum
   is the ℤ₃ projector orthogonality P_j·P_k = 0 (exact, no tunnelling).
   Confinement (Doc. 321) and Hawking selection are one principle.
4. **Carrier [K]** — massless n₄=0 torus mode; massive modes fall back
   (clock compression at the membrane).
5. **Information [K]/[B]** — sector pair (k,−k) orthogonally readable
   (log₂3 ≈ 1.585 bits/quantum); area quantum −4ℓ_P²/nat from
   Bekenstein+Clausius; fine-grained entropy constant (unitarity, Doc. 322).
   No information paradox.

In addition: power correction (1−ξ·ln(M/m_P)) = 0.6–1.4 %; M* = 3.3×10¹¹ kg;
family ladder r_s = R_H/2 exactly at M = 4.66×10⁵² kg.
Open [S]: greybody factors, fixed-point back-reaction.

Verification scripts: 18 + 20 assertions.

→ [DE](2/pdf/325_Hawking_FFGFT_De.pdf) · [EN](2/pdf/325_Hawking_FFGFT_En.pdf)

### Doc. 326 — Black Holes from Hyperbits and from FFGFT (DE+EN, 11 pp. each)

Comparison with Matzke's hyperbit framework (IPI 2026) — focus on Landauer,
bit values, system-dependent bit energy. Introduced by a narrative section
"Why Matzke's algebra looks so simple", which gives the approach its due before
the detailed criticism follows: geometry as bookkeeping over distinguishability
(e_i² = +1), the three falling out of Cl(6), the Schwarzschild radius without the
Einstein equations, the 0.41-bit stability story — and where the elegance is
paid for.

- **Convergences [B]:** fermion generation = algebraic base unit; N_c = 3
  enforced; r_s without GR; both Hawking mechanisms structurally exactly
  corresponding.
- **Divergence:** universal bit value (Matzke, Landauer at T_P) vs.
  system-dependent bit energy E_bit = ħc/L (FFGFT [K]).
- **Numerically:** T_H(Matzke)/T_H(KMS) = 1.000000 — the universal bit value is
  a reparametrization of the KMS relation, not an independent physical input.
- Matzke's stability threshold n_thresh = 6.41 as a universal number: [X]
  (settled numerically in Doc. 329, R88).

Verification script: 15 assertions.

→ [DE](2/pdf/326_Matzke_FFGFT_Vergleich_De.pdf) · [EN](2/pdf/326_Matzke_FFGFT_Vergleich_En.pdf)

### Doc. 327 — Self-adjointness of F̂ (DE+EN, 6 pp. each)

Closes R82 completely, with no remaining cases. Three observations from the corpus
(no new axioms): (F1) L₀ = ξ·ℓ_P makes the rung count finite; (F2) ℤ₃-covariant
sector phases; (F3) finite 100-step recursion of the fractal measure.

**Proof chain:**

| Step | Statement | Status |
|---|---|---|
| Lemma 1 | Doc.-322 axioms = scale filtration, exactly | [B] |
| Theorem 2 | Block-diagonal; ‖F̂‖ ≤ Σr_n < ∞ ⟹ D(F̂) = H | [B] |
| Theorem 3 | ℤ₃ pairing (k,−k) ⟹ F̂ = F̂† (with counter-example) | [B] |
| Corollary 4 | Deficiency indices (0,0); exactly one realisation | [B] |
| Theorem 5 | Fractal measure preserves self-adjointness | [B] |
| Theorem 6 | ℤ₃ restriction, all three χ-twist classes s.a. | [B] |
| Corollary 7 | ξ = λ_min(F̂_D4) well-defined, truncation-stable | [B] |

Verification script: 21 assertions, all passed.

**Doc. 322 updated:** the status table, the definition passage and the concluding
box still listed self-adjointness and the deficiency-index classification as [S] —
both now stand at **[B], Doc. 327**.

→ [DE](2/pdf/327_Selbstadjungiertheit_F_De.pdf) · [EN](2/pdf/327_Selbstadjungiertheit_F_En.pdf)


### Doc. 329 — Is the stability threshold n_thresh universal? (DE+EN, 7 pp. each)

Settles numerically the question booked as [S] in Doc. 326 (R88).
**Answer: no.**

The scale-independent core stands: Compton = Schwarzschild yields
M_coll = m_P/√2 purely geometrically, without bits, Landauer, or a
temperature [B]. Everything non-geometric in n_thresh = M_coll/m_bit sits
in the denominator.

With E_bit(L) = ħc/L (Doc. 257) one obtains exactly

    n_thresh(L) = L / (√2 · ℓ_P)

— linear in the scale, not an invariant number [B]. Across the scales of the
corpus (L₀ = ξℓ_P to 1 nm) the value varies by a factor of 4.6×10²⁹.

**Matzke's scale is reconstructible:** L = 2πℓ_P/ln2 = 9.0647 ℓ_P, and there
the formula returns exactly 6.4097 [B]. The "universal" bit value *is* the
FFGFT bit energy at about nine Planck lengths.

Sensitivity: a 10 % temperature deviation shifts n_thresh by 10 % and flips
the stability claim — at 1.1·T_KMS one gets n_thresh = 5.83 < 6.000, putting
Cl(6) above the threshold.

Side finding: the temperature is not T_P but the KMS temperature T_P/(2π) —
the same 2π that generates the Hawking temperature in Doc. 325 *without* a
bit value.

Untouched [B]: Compton = Schwarzschild, r_s without field equations, the
Cl(6) structure, the Hawking correspondences.

Verification script: 12 assertions.

→ [DE](2/pdf/329_nthresh_Skalenanalyse_De.pdf) · [EN](2/pdf/329_nthresh_Skalenanalyse_En.pdf)

---

## Corrected documents

### Docs. 320 + 322 — Δm²₃₂: numerical values corrected (R87)

The evaluation of ξ^(9/5) in Doc. 320 was faulty (8.717×10⁻⁸ instead of
1.059×10⁻⁷). The mass formula m_νi = m_e·ξ^pi and the exponents
p_i ∈ {9/4, 2, 9/5} were always correct — only the computed number for ν₃ was
affected. Doc. 320 and the two inherited table rows in Doc. 322 have been
brought to the correct values:

| | before | now |
|---|---|---|
| m_ν3 | 44.51 meV | **54.11 meV** |
| Δm²₃₂ | 1.90×10⁻³ eV² | **2.846×10⁻³ eV²** |
| Deviation | −22 % | **+16.0 %** |
| Σm_ν | 54.57 meV | 64.17 meV (< 120 meV ✓) |

Unaffected: m_ν1, m_ν2, Δm²₂₁ (+8.3 %) and the fixed-point assignment.

The deviation remains [S] but now carries the same sign as the solar one and is
about twice its size — pointing to a common cause. Doc. 320 has been extended by
a **candidate analysis**: K_frak at fixed point F₇ (+12.9 %, insufficient);
mixing term F₅–F₇ (right sign, requires the complete mass matrix — the most
promising candidate); alternative exponents (unlikely: p₃ = 1.8081 lies only
0.45 % above 9/5).

Verification script: `320_dm32_neutrino_verify.py` (10 assertions).

→ [DE](2/pdf/320_Spektraltheorie_De.pdf) · [EN](2/pdf/320_Spektraltheorie_En.pdf)

---

## Restructuring of the correction register

### Doc. 190 new — compact register (DE 10 pp. / EN 8 pp.)

Register table with **all 86 entries** (C1–C7 resp. K1–K7, P1–P44, R41–R86):
number, affected documents, subject in short form, with a pointer to the archive.
Closing with the consolidated section "Currently open bridges (as of R86)".

### Doc. 190-Archive — frozen full edition (DE 69 pp. / EN 58 pp.)

The previous extended edition with an archive notice. Contains, for every entry,
the full justification, the faulty and corrected expressions verbatim, and all
addenda. No longer continued.

The append-only principle remains unchanged (cf. R50): source documents are not
revised. New entries will henceforth be written directly in the compact register.

---

## Corrections — R84 to R88

**R84** (Aug. 23): ξ = C₂(SU(3)_fund)/N_Fourier = (4/3)/10⁴ = 4/30000 [K]
(Doc. 324). ξ is not a spectral value of any G(6) operator; the connection between
G(6,ℤ₃C) and FFGFT lies in the Casimir quotient, not in the spectrum.

**R85** (Aug. 23): Hawking mechanism closed microscopically [K]/[B] (Doc. 325).
The emission side booked as [S] in Doc. 313 Ch. G (membrane thermometer,
selection, carrier, information encoding) is raised to [K]/[B]. Greybody factors
and fixed-point back-reaction remain open [S].

**R86** (Aug. 23): Self-adjointness of F̂ closed completely [B] (Doc. 327).
The finiteness of the scale ladder is guaranteed by L₀ = ξ·ℓ_P (Doc. 180 [K]) —
no infinities in FFGFT, hence F̂ bounded and D(F̂) = H. The symmetry follows from
the ℤ₃ pairing (k,−k) (the same as in Doc. 325 [B]). Deficiency indices (0,0):
exactly one self-adjoint realisation [B]. Fractal measure, ℤ₃ restriction and all
three χ-twist classes preserve self-adjointness [B]. ξ = λ_min(F̂_D4) well-defined
and truncation-stable [B]. No remaining cases.
**R82 has been removed from the list of open bridges.**

**R87** (Aug. 23): Δm²₃₂ — corrected numerical values and candidate analysis [K].
In Doc. 320 the evaluation of ξ^(9/5) was faulty; the mass formula and exponents
were always correct. Docs. 320 and 322 brought to the correct values:
m_ν3 = 54.11 meV, Δm²₃₂ = 2.846×10⁻³ eV² (+16.0 % vs. NuFIT 5.3),
Σm_ν = 64.17 meV (within the Planck limit). Unaffected: m_ν1, m_ν2, Δm²₂₁,
fixed-point assignment. The remaining deviation stays [S]; the most promising
candidate is a mixing term F₅–F₇.

**R88** (Aug. 24): n_thresh is scale-dependent; Matzke's scale reconstructed
[B] (Doc. 329). n_thresh(L) = L/(√2·ℓ_P); Matzke's value corresponds to
L = 2πℓ_P/ln2 = 9.0647 ℓ_P. As a universal number negatively closed [X].
Untouched: Compton = Schwarzschild, r_s without field equations, Cl(6)
structure [B].

---

## Verification scripts

`python/Dok320_321_322_Skripte/`:
- `324_G6_FFGFT_verify.py` — trine theorem, vacuum operator, Casimir derivation (16)
- `320_dm32_neutrino_verify.py` — neutrino masses, Δm²₂₁, Δm²₃₂, mass sum,
  K_frak candidate, exponent comparison (10)

`python/Dok325_Skripte/`:
- `325_hawking_ffgft_mechanismus.py` — KMS, membrane thermometer, horizon bit,
  area bookkeeping, evaporation, family ladder (18)
- `325_hawking_z3_selektion.py` — ℤ₃ projectors, absorption, triality selection,
  sector information (20)

`python/Dok326_Skripte/`:
- `326_Matzke_FFGFT_verify.py` — bit values, stability threshold, Bekenstein,
  Weinberg angle, T_H equivalence (15)
- `326_nthresh_skalenabhaengigkeit.py` — Matzke's chain, collapse mass,
  n_thresh(L), scale reconstruction, temperature sensitivity (12)

`python/Dok327_Skripte/`:
- `327_selbstadjungiertheit_F_verify.py` — filtration lemma, diagonal form,
  boundedness, ℤ₃ symmetry with counter-example, deficiency indices, fractal
  measure, ℤ₃ restriction, χ-twists, λ_min stability (21)

Total: 112 assertions, all passing.

## Bridges closed in this release

| Bridge | before | after | Doc. |
|--------|--------|-------|------|
| ξ as spectral value of a G(6) operator? | open | **[K]** No (negatively closed) | 324 |
| ξ = C₂(SU(3))/N_Fourier | — | **[K]** | 324 |
| Hawking: quantum = horizon bit | [S] | **[K]** | 325 |
| Hawking: ℤ₃ selection (T_R = 0) | [S] | **[B]** | 325 |
| Hawking: absorption P_jP_k = 0 | [S] | **[B]** | 325 |
| Hawking: carrier n₄ = 0 | [S] | **[K]** | 325 |
| Hawking: sector-pair encoding | [S] | **[B]** | 325 |
| Area quantum −4ℓ_P²/nat | [S] | **[B]** | 325 |
| Self-adjointness of F̂ (R82) | [S] | **[B]** complete | 327 |
| Deficiency-index classification | [S] | **[B]** (0,0), trivial | 327 |
| ξ = λ_min(F̂_D4) well-defined | implicit | **[B]** min-max | 327 |
| Fractal measure and self-adjointness | open | **[B]** preserves it | 327 |
| χ-twist classes self-adjoint | open | **[B]** all three | 327 |
| Δm²₃₂: numerical values corrected | −22 % | **+16.0 %** [K] | 320/322 |
| n_thresh: universal or scale-dependent? | [S] | **[B]** scale-dependent | 329 |
| n_thresh = 6.41 as a universal number | open | **[X]** negatively closed | 329 |

## Remaining open bridges

| Bridge | Status |
|--------|--------|
| Δm²₃₂ (+16.0 % after R87; mixing term F₅–F₇) | [S] |
| 2-loop corrections to α_s(M_Z) | [S] |
| m_Pl and α_em(M_Z) from ξ | [S] |
| Quark/hadron sector | open bridge (Doc. 318, R76) |
| Greybody factors; fixed-point back-reaction | [S] (R85) |
| Forward derivation of cosmic exponent 41/4 (P20) | open — largest leverage |
| CMB peak selection {1,6,14,26}; \|n\|²=30 | open (P29/P31) |
| C_ℓ source/window function | open (P30) |
| Ω_DM quantitatively, model-neutral | open (P17) |
| Spectral dimension d_s = 1.86 vs. ≈ 2 | open |
| H₀ language cleanup; rework Doc. 026 | open (P34/P16) |
| ξ as line width; ι embedding HLV ⊂ FFGFT | pre-registered (P44, Doc. 297) |

The particle and spectral sectors are thus largely closed; the substantive open
questions now lie predominantly in the cosmological sector, where most of them
converge on P20.

---

## License

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

*Established results are documented in the corpus; open predictions are subject to
experimental verification.*
