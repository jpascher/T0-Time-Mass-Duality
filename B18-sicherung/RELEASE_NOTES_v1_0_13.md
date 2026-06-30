# T0 Theory / FFGFT v1.0.13 – Quantum-Mechanical Bridge, Methodological Status, Plain-Language Translation

**Release Date:** 2026-05-05
**Version:** 1.0.13
**DOI:** 10.5281/zenodo.20022166
**GitHub:** https://github.com/jpascher/T0-Time-Mass-Duality

---

## 1. Overview

This release consolidates and clarifies the FFGFT field-theoretic formulation along three lines:

1. **Doc. 202 (Complete Field Theory)** is substantially extended: the field-theoretic formulation now connects explicitly to the standard quantum-mechanical equations of motion (Schrödinger, Dirac, Bell correlations, qubit mappings), receives a new section on the methodological status of the verification condition, and the renormalisation-group section is renamed and reframed as FFGFT-native scale-structure language.
2. **Doc. 190 (Corrections Register)** is extended with two new binding terminology rules (R7, R8) on renormalisation-group language and fractal renormalisation.
3. **Doc. 205 (NEW)** is a complete plain-language translation of the central Lagrangian formulations into everyday German/English, with an explicit symbol-explanation block for every formula. Eleven chapters, Kindle 6×9 format, no hallucinations: every metaphor used is taken from the corpus itself.

No existing predictions, derivations, or numerical results have been changed. All terminology corrections are documented in Doc. 190 (see Section 4).

---

## 2. New and Substantially Extended Documents

### 2.1 Doc. 202 — Complete Field Theory (substantially extended)

**Files:** `202_FFGFT_Feldtheorie_Gesamt_De.pdf` / `202_FFGFT_Feldtheorie_Gesamt_En.pdf`
**Page count:** 28/25 pages (was 18/15)

The v1.0.12 release introduced Doc. 202 as the unified synthesis of the FFGFT field theory. The v1.0.13 release extends it along four axes:

#### 2.1.1 Extended grey box at §8 (Free Lagrangian)

The cross-reference to Doc. 201 (DVFT adaptation) is extended with two paragraphs:

- A pointer to Doc. 201 §2.6 (simplified Dirac equation from T0) and §6.6 (Schrödinger equation derivation from T0) as the bridge to non-relativistic and relativistic quantum mechanics, with a vorgriff on the new §15.
- A note on the terminology "renormalisation group": §19 of Doc. 202 had referred to the scale running in standard QFT language as the renormalisation group; in FFGFT this scale structure follows directly from the recursion operator $\mathcal{R}$ (Doc. 203) on the fractal torus geometry, not from a renormalisation procedure. Doc. 201 consequently uses FFGFT-native language; Doc. 190 R7 records the binding convention.

#### 2.1.2 New §15 — Connection to the Quantum Mechanical Equations of Motion

A complete bridge from the Doc. 202 mode picture to the standard quantum-mechanical formalism. Five subsections:

**Bridge 202 ↔ 201** (eq. 202.QM-1)
The mode sum $\Phi(x) = \sum m_{n,l,j}\phi_{n,l,j}(x) P_{n,l,j}$ maps in the low-energy limit to the DVFT polar decomposition $\sqrt{\rho(x,t)}\,e^{i\theta(x,t)}$. Cross-references to Doc. 020, 035.

**Simplified Dirac equation (from Doc. 201 §2.6)** (eq. 202.QM-2/3)
The fundamental structure is the Clifford algebra $\mathbf{e}_\mu\mathbf{e}_\nu + \mathbf{e}_\nu\mathbf{e}_\mu = 2g_{\mu\nu}$ (Doc. 050, 051), not a specific matrix representation. The 4×4 γ-matrices remain **as a representation** of the Clifford generators and are not eliminated, just reduced to their geometric meaning. Spin manifests on the fractal torus as a topological vacuum-phase winding consistent with $j = l \pm \tfrac12$. Cross-references: Doc. 020 §"T0-modified Dirac equation", Doc. 067 §"Modified Dirac equation", Doc. 095 §"Simplified Dirac equation (T0 version)", Doc. 053.

**Schrödinger equation (from Doc. 201 §6.6)** (eq. 202.QM-4)
The phase equation reduces in the non-relativistic limit to the standard Schrödinger equation. The Schrödinger equation is therefore not fundamental but an effective equation for slow non-relativistic knot excitations. Cross-references: Doc. 020 §"T0-modified Schrödinger equation", Doc. 067 §"Modified Schrödinger equation", Doc. 095, Doc. 129, Doc. 037.

**Bell correlations (from Doc. 023, 074)** (eq. 202.QM-5/6)
$$\mathrm{CHSH}^{\mathrm{FFGFT}} = 2\sqrt{2}\cdot K_{\text{frak}}^{D_f}\cdot\left(1 - \xi_0\cdot\tfrac{\Delta\theta}{\pi}\right)$$
with $\Delta\mathrm{CHSH} \sim \mathcal{O}(\xi_0) \approx 10^{-4}$. Bell correlations do **not** follow directly from $\mathcal{L} = \mathcal{L}_0 + \Delta\mathcal{L}_{\text{Torus}}$ but from the topology of the mode configurations; the Lagrangian supplies the constants $\xi_0$, $D_f$, $K_{\text{frak}}$ entering (202.QM-5). Bell tests thereby become an *indirect* probe of the Lagrangian structure via the $\xi_0$ scale constant. Comprehensive cross-references organised by category (dedicated Bell series, quantum computing application, locality & non-locality, cross-cutting): Doc. 023, 023a×2, 147, 074, 131, 055, 022, 035, 175.

**Qubit mappings (from Doc. 175, 034)** (eq. 202.QM-7)
A qubit state is a specific configuration of the mode structure: $\alpha\Phi_0 + \beta\Phi_1$ with $\Phi_i = \rho_i e^{i\theta_i}$. The cylindrical phase space $(z, r, \theta)$ from Doc. 034/175 replaces the Bloch sphere; quantum gates become geometric transformations in real space (Hadamard exchanges $z\leftrightarrow r$ with $\pi/2$ phase rotation, Z-phase is rotation about cylinder axis). The basis states $|0\rangle, |1\rangle$ are two specific mode excitations $\phi_{n,l,j}$ from the Doc. 202 mode catalogue; the mode-function geometry arises from $\mathcal{L} = \mathcal{L}_0 + \Delta\mathcal{L}_{\text{Torus}}$. Spin qubits sit at $\xi$-level $N\approx 8$; photonic resonators at a different level. Cross-references organised by category: Doc. 034, 175, 173, 174, 178, 147, 176, 161, 183.

**Consequence for the verification condition**
Both equations of motion (202.QM-2) and (202.QM-4) are contained in the mode picture as different low-energy limits of the same spectral structure. Bell correlation (202.QM-5) and qubit mapping (202.QM-7) provide independent consistency tests of the same $\xi_0$ constant.

#### 2.1.3 New §17 — Methodological Status of the Verification Condition

Four subsections clarifying how to read the agreement between FFGFT mass formulas and PDG values:

**Reduction is not precision improvement**
The FFGFT Lagrangian $\mathcal{L} = \mathcal{L}_0 + \Delta\mathcal{L}_{\text{Torus}} + \mathcal{L}_{\text{Yukawa}}$ contains the Standard-Model Lagrangian as a limiting case: for $\xi_0 \to 0$, both $\Delta\mathcal{L}_{\text{Torus}}$ and the Yukawa term vanish. Where standard calculations are confirmed (e.g. QED scattering amplitudes to $10^{-12}$), FFGFT can only reproduce these and add $\xi_0$ corrections of order $10^{-4}$, not surpass them qualitatively. The reduction of $\sim 25$ free Standard-Model parameters to a single $\xi_0$ is the quantifiable claim — not the numerical agreement of individual masses.

**Predictions beyond the Standard Model**
Bell-CHSH correction $\sim 10^{-4}$ in loophole-free tests; $\Delta$CHSH $\sim 10^{-3}$ in 73-qubit systems (Doc. 147); modified dispersion at near-Planck energies; dark matter and dark energy without separate components (DVFT line, Doc. 201); CMB homogeneity without inflation (Doc. 140, 201); hierarchy problem as geometric consequence (Doc. 003, 049).

**Circularity of the comparison basis**
PDG values are not raw data: they contain assumptions about units, gauge conventions, calibrating natural constants ($c, \hbar, e$ fixed by definition in the 2019 SI reform), and loop corrections from QFT evaluations. An FFGFT calculation starting from $\xi_0$ in natural units ($\hbar = c = 1$) avoids accumulation of model assumptions but inherits the precorrections in the measured values. The agreement at $\sim 1\,\%$ is to be read in two directions: as confirmation of the structural claim and as a pointer to the latitude introduced by the circular measurement basis. Cross-references to Doc. 066 (parameter-transfer problem) and Doc. 101 (circularity of the constants).

**Consequence for the assessment**
The verification condition is to be read **structurally**, not **quantitatively**. The remaining $\sim 1\,\%$ margin is not a theoretical deficit but a reflex of the three methodological limitations above.

#### 2.1.4 §19 renamed — Scale Structure from Recursion (was: The Renormalisation Group)

The section header is renamed; the body is reframed as a direct consequence of $\mathcal{R}$ (Doc. 203) on the fractal torus geometry, not as a renormalisation procedure. The mathematical content (modified $\beta$-function with $\xi_0$ correction term, time-invariance of $\xi_0$) is unchanged. A note on terminology refers to Doc. 190 R7 and to Doc. 159 / 189 for the FFGFT-native treatment. A leftover mention of "kein Fixpunkt der Renormierungsgruppe" in §20.4 is corrected to "kein Fixpunkt der β-Funktion".

### 2.2 Doc. 190 — Corrections Register (extended)

**Files:** `190_T0_Korrekturen_De.pdf` / `190_T0_Korrekturen_En.pdf`

Two new binding terminology rules added:

#### R7 — Renormalisation-Group Terminology

The term "renormalisation group" is **not** to be used in FFGFT documents. The scale running follows from the recursion $\mathcal{R}$ (Doc. 203) on the fractal torus, not from a renormalisation procedure.

| Replace | With |
|---------|------|
| "Renormierungsgruppe" / "renormalisation group" | "Skalenstruktur aus der Rekursion" / "scale structure from recursion" |
| "RG-Fluss" / "RG flow" | "$\mathcal{R}$-induzierter Skalenfluss" / "$\mathcal{R}$-induced scale flow" |
| "RG-Fixpunkt" / "RG fixed point" | "$\mathcal{R}$-Fixpunkt" / "$\mathcal{R}$ fixed point" or "Fixpunkt der β-Funktion" |

Documents affected: Doc. 005, 008, 019, 086, 189, 202. Existing documents are not retroactively edited — the binding convention applies to all new documents and to revisions.

#### R8 — Fractal Renormalisation Terminology

The term "fractal renormalisation" is replaced by:

| Context | Use |
|---------|-----|
| Units / scale conversion (Doc. 060) | "geometrische Skalenanpassung" / "geometric scale adaptation" |
| Yukawa $K_\text{frak}$ correction | "fraktale Korrektur" / "fractal correction" |

The earlier label "fraktale Renormierung" suggested a renormalisation procedure that does not exist in FFGFT; the correct geometric interpretation is a discrete scale adaptation between $\xi$ levels.

### 2.3 Doc. 205 — FFGFT in Plain Language (NEW)

**Files:** `205_FFGFT_Narrativ_De.pdf` / `205_FFGFT_Narrativ_En.pdf`
**Page count:** 24/22 pages (Kindle 6×9 format)
**Word count:** 4776/5193 words

A complete plain-language translation of the central Lagrangian formulations. Eleven chapters:

1. **The big picture** — what FFGFT claims, and what it does not
2. **Why a fractal torus** — topology as the root of integer quantum numbers
3. **The modes — what actually oscillates** — three quantum numbers $(n, l, j)$ as "pitch, shape, rotation"
4. **The free Lagrangian — the bare oscillation** — $\mathcal{L}_0 = \tfrac12(\partial\delta m)^2$
5. **The correction term — how the fractal geometry shapes the oscillation** — piano inharmonicity from Doc. 060
6. **Where mass comes from — the binding picture** — eigenvalue residual without Higgs mechanism postulate
7. **The Yukawa coupling — matter to vacuum** — violinist analogy
8. **The recursion — self-similarity of the scales** — $\xi_0$ as fixed point of $\mathcal{R}$
9. **The bridge formula — how everything fits together** — $m_\ell = r_\ell \cdot \xi_0^{p_\ell} \cdot v$ with musical interpretation
10. **What the Lagrangian formulation achieves** — three structural claims:
    - Reduction of free parameters ($\sim 25 \to 1$)
    - Bridge between QFT and General Relativity
    - Explanation of the "unexplained residues" (hierarchy problem, dark matter/energy, CMB without inflation, values of natural constants)
11. **What the theory does *not* claim** — four explicit negations:
    - No precision improvement of Standard-Model calculations (with subparagraph on the circularity of the comparison basis: PDG values include 2019 SI-fixed constants and loop corrections)
    - No replacement of QFT as a tool
    - No statement about ontological reality
    - No solution of the measurement problem

**Symbol explanations:** Each of six display formulas is accompanied by an explicit *Symbols* / *Bezeichnungen* block listing every symbol with its meaning. This includes the d'Alembert operator $\Box$ (with the explicit form $\partial_t^2 - \nabla^2$), the spinor field $\psi$ and its adjoint $\bar\psi$, the spacetime indices $\mu, \nu$ with reference to Einstein's summation convention, and the Higgs vacuum expectation value $v$.

**Anti-hallucination discipline:** Every metaphor used is grounded in the FFGFT corpus. Vibrating string from Doc. 159 (harmonic structure of the torus). Piano inharmonicity from Doc. 060 (musical parallels). Resonator-cavity and harmonica-tone-cell from Doc. 173 (quantum dot). Fractal coastline as standard image from fractal geometry. Binding picture from Doc. 202 §12. Tuned piano as self-consistency analogy linking Doc. 060 (tuning) and Doc. 203 (fixed point).

---

## 3. README Updates

Both `README.md` and `README_de.md` have been updated with a new section at the top:

- **"May 2026 (v1.0.13)"** — Quantum-mechanical bridge, methodological status, narrative translation
- The previous "May 2026" section is now labelled **"May 2026 (v1.0.12)"**
- DOI badges updated to 10.5281/zenodo.20022166

---

## 4. Corrections Register (Doc 190, binding)

Updated table for v1.0.13:

| No. | Affects | Incorrect | Correct |
|-----|---------|-----------|---------|
| C1 | Doc 049, HTML | ξ = λ²v²/(64π⁴m²) | ξ = λ²v²/(16π³m²) |
| C2 | Doc 116, table | r_τ = 8/3 | r_τ = 25/9 |
| C3 | Doc 018, Explorer | a_e = 4π/(f·k) | a_e = 2π²/(f·k) |

Refinements:

| No. | Concerns | Binding statement |
|-----|---------|------------------|
| R1 | Koide precision | ΔQ < 0.00003% = internal consistency; 0.001% for external use |
| R2 | ℏ derivation | ℏ follows from ξ via L₀ = ξ·ℓ_P; not a free constant |
| R3 | Two ξ parameters | ξ_par = 4/30000 (geometric); ξ_Higgs ≈ 1.038×10⁻⁵ (algebraic) |
| R4 | L₀ and Schwarzschild | L₀ is geometric fundamental length; Schwarzschild = consistency check only |
| R5 | Mass formulas | ~1% agreement = structural proof, not precision calculation |
| R6 | Koide application | Use only PDG-measured masses, not symbolic FFGFT terms |
| **R7** | **Renormalisation-group terminology** | **"Scale structure from recursion" replaces "renormalisation group" throughout the series** |
| **R8** | **Fractal renormalisation terminology** | **"Geometric scale adaptation" or "fractal correction" replaces "fractal renormalisation"** |

---

## 5. Impact on Existing Predictions

| Prediction | Status | Note |
|-----------|--------|------|
| ξ = 4/30000 | Unchanged | Universal geometric parameter |
| D_f = 3 − ξ | Unchanged | Fractal dimension |
| T_min = ξ·t_P | Unchanged | Sub-Planck lower bound |
| L₀ = ξ·ℓ_P | Unchanged | Lattice constant |
| Particle masses | Unchanged | ~1% structural accuracy, not fitted |
| g-2 anomaly (0.05σ) | Unchanged | |
| CHSH T0 corrections | Unchanged | $\sim 10^{-4}$ in loophole-free tests |
| Avi: CP phase δ = 283.28° | Confirmed | Dev. 0.18°; DUNE 2028 falsification |
| Avi: sin²θ_W = 3/13 | Confirmed | Dev. 0.195% |
| Avi: η = 6.03×10⁻¹⁰ | Confirmed | Dev. 0.5% |
| RSA precision barrier | Unchanged | Physical (not computational) limit |
| **NEW (clarified):** QM equations of motion | Bridge formula 202.QM-1 to 202.QM-7 explicit | Schrödinger and Dirac as low-energy limits |
| **NEW (clarified):** Methodological status of agreement | Structural, not quantitative | Doc. 202 §17, Doc. 205 Ch. 11 |
| **NEW (clarified):** Bell correlations Lagrangian connection | Indirect via $\xi_0$, $D_f$, $K_\text{frak}$ | Doc. 202 §15.4 |

---

## 6. Context: Connection to Existing Documents

| New / Extended Doc | Builds on |
|--------------------|-----------|
| 202 §15 (QM bridge) | 020, 035, 050, 051, 053, 067, 095, 129, 037 (Schrödinger/Dirac); 023, 023a, 074, 131, 055, 022, 147, 175 (Bell); 034, 173, 174, 175, 176, 161, 178, 183 (qubits) |
| 202 §17 (methodological status) | 066 (parameter transfer), 101 (circularity), 003 (T·m=1), 049 (Lagrangian comparison) |
| 202 §19 renamed | 159 (harmonic torus), 189 (Stage-3 bottleneck), 203 (recursion operator), 190 R7 (terminology) |
| 190 R7, R8 | 005, 008, 019, 060, 086, 189, 202 (terminology cleanup) |
| 205 (NEW) | All core FFGFT documents: 002 (overview), 060 (musical parallels), 116 (Koide), 158 (g-2), 159 (harmonic torus), 173 (quantum dots), 180 (L₀ derivation), 181 (torus justification), 182 (cosmology), 188 (sub-Planck), 189 (Stage-3), 190 (corrections), 192 (Koide algebraic), 193 (non-closure), 201 (FFGFT all), 202 (field theory), 203 (recursion), 204 (fractal boundary) |

---

## 7. Reading Recommendations

For different audiences:

- **Researchers in theoretical physics** — Start with Doc. 202 (now substantially extended), Doc. 203 (recursion operator), Doc. 204 (fractal boundary). The new §15 of Doc. 202 is the fastest route from the field-theoretic formulation to the standard quantum-mechanical equations of motion. The new §17 clarifies how the structural agreement at $\sim 1\,\%$ is to be interpreted.

- **Researchers in quantum information / quantum computing** — Doc. 175 (qubit state spaces), Doc. 147 (quantum computing), Doc. 161 (Ising machines), and Doc. 202 §15.5 (qubit mappings on the cylindrical phase space). The Bell-CHSH prediction $\sim 10^{-4}$ in loophole-free tests is the principal quantitative benchmark for an experimental test.

- **Science communicators, journalists, generally interested readers** — Doc. 205 (NEW) is the recommended entry point. It contains the substance of the field theory in plain language, with explicit symbol explanations for every formula, and it states explicitly what the theory does and does not claim.

- **Critics of FFGFT** — Doc. 202 §17 (methodological status) and Doc. 205 Ch. 11 (what the theory does not claim) are the authoritative statements of FFGFT's epistemic position. Both make explicit that:
  - FFGFT does not insert additional Lagrangian terms to obtain "different" values from the SM; it contains the SM Lagrangian as the $\xi_0 \to 0$ limit.
  - The structural claim (parameter reduction $\sim 25 \to 1$ via geometry) is independent of the numerical accuracy of individual mass formulas.
  - Comparison against PDG values cannot be more accurate than the PDG values themselves, which are not raw but contain SI-2019 fixed constants and QFT loop corrections.
  - Where FFGFT delivers different statements, these are predictions in regimes where the SM is silent or where corrections are not yet experimentally resolved.
