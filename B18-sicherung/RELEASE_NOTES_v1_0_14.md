# T0 Theory / FFGFT v1.0.14 – Triangle–Matrix Reduction, Consciousness Bridges, Winding Clarification, Falsification Trilogy, and Hilbert-Space Triptych

**Release Date:** 2026-05-10
**Version:** 1.0.14
**DOI:** [10.5281/zenodo.20041543](https://doi.org/10.5281/zenodo.20041543)
**GitHub:** https://github.com/jpascher/T0-Time-Mass-Duality
**Predecessor (v1.0.13):** [10.5281/zenodo.20041529](https://doi.org/10.5281/zenodo.20041529)

---

## 1. Overview

This release adds **eight new documents** and a set of thirteen reproducible Python scripts. The release does not modify or extend any existing FFGFT prediction or derivation. Its scope is *consolidation*:

1. **Doc. 206 (NEW)** proves the Triangle–Matrix Reduction Theorem. Every consistent geometric description of physical structures that falls into the same scale regime as FFGFT can be mapped onto two equivalent representations — a Z₃ triangle connection and a 3×3 matrix algebra. Six bridges to other formulations (Austin, Tekermen, Phillips, Porter, Chekanov–Hakan, Moseley) are tested explicitly: five hold algebraically or structurally, one is identified as a regime separation rather than a contradiction. A dedicated numerology-filter section and a methodological section on ΛCDM-circularity of cosmological reference data extend the self-check discipline introduced in Doc. 202 §17 (v1.0.13).

2. **Doc. 207 (NEW)** establishes structural bridges between Doc. 206 and the existing FFGFT consciousness discussion (Doc. 100 on fractal incoherence and the Adlam-McQueen-Waegell no-go theorem; Doc. 170 on discrete complexity thresholds). Three algebraic identifications are made explicit; an additional chapter formulates four qualitative falsifiable predictions under the discreteness hypothesis from Doc. 170; and a methodological self-check transfers the Doc. 206 numerology filter to consciousness claims.

3. **Doc. 210 (NEW)** is a structural complement to the corrections register Doc. 190, separating three distinct winding levels per fermion ($f = 1/(4\xi)$, spin winding, generation winding) that older documents conflated under the same $(n, l, j)$ notation. Foreseen for later merge with Doc. 190.

4. **Falsification Trilogy — Docs. 220, 221, 222 (NEW)** state explicit falsification criteria for FFGFT in three regimes: Casimir at $10$–$100\,\mu$m, cosmological redshift in four observational signatures, and light-element abundances under the FFGFT no-BBN-phase hypothesis. Each criterion is quantitative and experimentally accessible.

5. **Hilbert-Space Triptych — Docs. 230, 231, 232 (NEW)** treats FFGFT's relationship to the Hilbert-space formalism and to other emergent-geometry programmes. Doc. 230 provides a carried-out bijection between FFGFT and standard QM on the qubit sector. Doc. 231 identifies the four mathematical extensions ($SU_q(2)$, winding quantum numbers, spinor bundles, Kaluza-Klein) needed to carry full FFGFT natively in Hilbert-space language. Doc. 232 sketches Quantum Graphity (Konopka–Markopoulou–Severini 2008) as a hypothetical subset of FFGFT through five reduction steps, with an explicit methodological-status section distinguishing what holds from what remains open.

6. **Thirteen reproducible Python scripts** (`2/python/bridge/`) implement every proof in Doc. 206. They run in Python 3 with `numpy`, `sympy`, and `matplotlib`.

No existing predictions, derivations, or numerical results have been changed. No new entries in the corrections register (Doc. 190).

---

## 2. New Documents

### 2.1 Doc. 206 — Triangle–Matrix Reduction Theorem (NEW)

**Files:** `dok206_dreieck_matrix_reduktion_De.pdf` / `dok206_dreieck_matrix_reduktion_En.pdf`
**Page count:** 18/17 pages

#### 2.1.1 Mathematical core

The Z₃ cycle has adjacency matrix
$$A = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}, \quad A^3 = I, \quad \det(A) = 1, \quad \mathrm{Tr}(A) = 0$$
with eigenvalues $\{1, \omega, \omega^2\}$ — exactly the Z₃ characters. The closing edge is damped by ξ:
$$A_\xi = \begin{pmatrix} 0 & 0 & 1-\xi \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}, \quad A_\xi^3 = (1-\xi)\,I, \quad \det(A_\xi) = 1 - \xi.$$
The fractal dimension follows in linear order: $D_f = 3 - \xi$. The Z₃³ tensor product $T(\xi) = A_\xi \otimes A_\xi \otimes A_\xi$ has 27 eigenvalues of modulus $(1-\xi)$ and produces the scale ladder $\lambda_n = (1-\xi)^{n/3}$ for $n = 1, 2, 3, \dots$. The third-power exponents are not arbitrary but algebraically forced by the threefold tensor structure. All identities are verified symbolically and numerically in the accompanying scripts.

#### 2.1.2 Six bridges tested

| Bridge | Identification | Status |
|--------|---------------|--------|
| Austin (D = 3 + ε) | ε = −ξ exact to ten digits via log det | ✓ algebraic |
| Tekermen (constitutive openness) | Algebraically identical to Doc. 193 non-closure | ✓ structural |
| Phillips (Self-Dual C-25, IGL) | tr(P₁+P₂)/tr(I) = 2/3, A² = Aᵀ | ✓ algebraic |
| Porter (Λ-linear) | Λ·ℓ_H² = 3·Ω_Λ (Friedmann form), m_Λ ≈ 2.24 meV | ✓ structural |
| Chekanov–Hakan (trig. SM) | p_n = 3(1−ξ)^(n/3) for n%3=0, else 0 | ✓ algebraic |
| Moseley (ITR ν_M) | Thermal ~395 K, no QG regime | ⊥ regime separation |

#### 2.1.3 Ω_Λ fit attempt — explicitly not booked as a result

A fit attempt $\Omega_\Lambda \stackrel{?}{=} \frac{11}{16} + \frac{1}{2}\xi^{2/3} = 0.688805$ shows $0.014\,\%$ deviation from the Planck 2018 value 0.6889. A numerology filter on 30 random target numbers from the same domain showed that 12 of them (40%) reach the same or better accuracy by the same fit family. The result is therefore identified as numerology, not as a theoretical finding, and explicitly **not** booked as a derivation of $\Omega_\Lambda$ from ξ.

#### 2.1.4 Methodological status of cosmological reference data (§11)

Analogous to Doc. 202 §17 (PDG-circularity, v1.0.13), this section makes the ΛCDM-circularity of cosmological reference values explicit:

- $\Omega_\Lambda = 0.6889$, $\Omega_M = 0.3111$, $H_0 = 67.4$ are not raw data. They are determined within the ΛCDM framework (FRW metric, dark matter as a separate component, flat universe, standard inflation, SM plasma physics).
- Anyone using $\Omega_\Lambda$ as a target value implicitly compares against ΛCDM.
- FFGFT's stated aim is to *replace* dark matter and inflation. Comparison against ΛCDM-pipelined values is therefore not a model-independent test.
- An FFGFT-compliant cosmological test would require an own evaluation pipeline on CMB raw data (independent future work).

### 2.2 Doc. 207 — Algebraic Bridges to the Consciousness Discussion (NEW)

**Files:** `dok207_bewusstsein_bruecken_De.pdf` / `dok207_bewusstsein_bruecken_En.pdf`
**Page count:** 24/23 pages

Doc. 207 is a synthesis document, not a new theorem. It anchors the existing FFGFT consciousness discussion algebraically without extending it in content. The document grew during the v1.0.14 development cycle from a compact bridge paper into a substantial structural treatment, with explicit chapters on wave-physics anchoring, atomic self-maintenance, falsifiable predictions, hierarchy/embedding logic, and a structural diagnosis of AI's relation to human consciousness.

#### 2.2.1 Three structural bridges

| Bridge | Identification | Source |
|--------|---------------|--------|
| A: Tekermen's constitutive openness | $\xi > 0 \Leftrightarrow \det(A_\xi) < 1$ | Doc. 193, Doc. 206 §6 |
| B: Phillips' Information Grounding Law | $A^2 = A^\top$ (Z₃ self-inversion) | Doc. 206 §7 |
| C: Doc. 170's discrete level table | Algebraically consistent with $(1-\xi)^{n/3}$ | Doc. 206 §4 |

The bridges are structural, not ontological. Bridge C enforces *discreteness* of the level structure, but does **not** algebraically determine which $n$ corresponds to which biological level. The level assignment in Doc. 170 remains a phenomenological working hypothesis.

#### 2.2.2 Reflection as the operative reading of openness (§4)

A dedicated chapter anchors the bridges in wave physics. $\xi > 0$ is operatively the *incomplete reflection* of a standing wave at its own topological boundary: $\det(A_\xi) = 1 - \xi$ means the wave returns to itself after three steps shifted by the deficit $\xi$ — what does not return is what we can call "world". Sensing is readable as *stacked reflection* across scales. **Atomic self-maintenance** is identified as a structural pre-form (sharpening of Doc. 170 levels 0–1: the atom is not "passive" but *structurally active without metabolic activation*; its mode maintains itself by self-reflection at the topological boundary). The result is a six-step precondition chain:

1. **Reflection** (algebraic in $A^3 = I$ and $A^2 = A^\top$)
2. **Closure deficit** ($\det(A_\xi) = 1-\xi$)
3. **Atomic self-maintenance** (reflection plus closure deficit on one scale)
4. **Scale stacking** (FFGFT finding $N \approx 8$ from Doc. 173, Doc. 172 — explicitly marked as finding, not theorem; a methodological-status box distinguishes this from the algebraic certainty of $\det(A_\xi) = 1 - \xi$ in Doc. 206 §6)
5. **Metabolic activation** (Doc. 170 §2 — vulnerability, metabolism, T = 1/m)
6. **Recursive self-modulation** (Doc. 170 level 4 — consciousness)

Steps 1–3 are algebraically anchored in Doc. 206. Step 4 is supported as an FFGFT finding. Steps 5–6 are formulated phenomenologically in Doc. 170 as a working hypothesis.

#### 2.2.3 Connection to Adlam, McQueen and Waegell (2025)

Adlam et al. show that agency cannot arise in a purely unitary quantum system. Doc. 100 had argued that consciousness emerges not from quantum coherence but from fractal incoherence. In the language of Doc. 206, this is algebraically readable:

- Adlam's no-go: unitary system $=$ closed recursion $=$ $\det = 1$, hence $\xi = 0$.
- FFGFT response: $\xi > 0$ geometrically forces a world-relation; the system has an outside because its algebraic skeleton does not close.

Adlam's no-go theorem and FFGFT's non-closure theorem (Doc. 193) are two sides of the same structural statement. Doc. 207 makes this identification explicit but does not claim that $\xi > 0$ *produces* consciousness — only that it satisfies the structural precondition Adlam misses.

#### 2.2.4 Four falsifiable predictions under explicit auxiliary assumptions (§7)

Under the discreteness hypothesis from Doc. 170, four qualitative predictions follow. Each is formulated as a structural feature, **without** quantitative values from ξ:

| Prediction | Structural feature | Open phenomenology |
|------------|-------------------|--------------------|
| A | Bimodality of consciousness markers (e.g. PCI) | Concrete cutoff, gap size |
| B | Developmental jump rather than gradient | Timing of jump |
| C | Anaesthesia tipping rather than gradation | Critical dose |
| D | Species classification rather than scaling | Which taxa cross threshold |

Falsification of any of these qualitative predictions falsifies the **discreteness hypothesis from Doc. 170**, not the algebraic skeleton from Doc. 206.

#### 2.2.5 Methodological self-check (filter analogous to Doc. 206 §12)

Five typical fallacies are explicitly listed and avoided:

1. No quantitative PCI threshold from ξ (e.g. $C_{\text{crit}} = \kappa\xi$ with free $\kappa$).
2. No derivation of EEG spectral exponent $\beta$ from ξ.
3. No identity thesis "consciousness $\equiv$ recursive coupling" — this redefines the Hard Problem rather than solving it.
4. No scale ladder $(1-\xi)^{k-1}$ — only $(1-\xi)^{n/3}$ has algebraic backing.
5. No Z₃ identification with three concrete brain areas (V1 → V4 → prefrontal).

#### 2.2.6 Consequences from the step ladder (§10)

A practical-implications chapter draws three connected consequences:

**Graded sentience in the biological domain.** All cellular living beings meet level 2, with explicit treatment of single-celled organisms, plants (level 2 multicellular with approach to level 3), and animals (level 3, some level 4). Scientific-historical connections to Maturana/Varela (autopoiesis = Doc. 170 level 2), Lynn Margulis (cellular sentience), Mancuso/Trewavas (plant signal processing), Stuart Kauffman (biological autonomy). Terminological clarification: "consciousness" can be reserved for level 4 (narrow reading, Doc. 170 convention) or used from level 2 (wide reading) — both are consistent; the differentiation in the hierarchy matters more than the word choice.

**Consciousness hierarchy and embedding.** The step ladder applies on three levels: (a) within an organism (cells → subsystems → central self-modelling, vertically connected by HPA axis, vagus nerve, immune-brain coupling, microbiome-brain axis — couplings that are *not* represented in level-4 self-modelling); (b) organism in its natural environment (climate, ecosystem, atmosphere); (c) organism in its social environment (language, culture, institutions, other humans). All three follow the maxim: *hierarchy is neither identity nor decoupling*. Optional religious reading (d): compatible with pantheistic, panentheistic, and some Christian traditions ("In him we live and move and have our being", Acts 17:28) without forcing classical-theistic identity assumptions.

**AI: what it does not reach, and what it erodes.** Current AI does not fully reach level 5 (metabolic activation). Autonomous vehicles with energy management have taken a partial first step (active energy control, partial vulnerability) but lack self-repair, replication, and constitutive decay. 3D-printed components are geometry, not function: material properties, mechanical tolerances, process integration cannot be replaced by printing. **Crucial structural asymmetry:** AI influence is *not* embedding in the sense of (a)–(c). It is monodirectional (output flows to receiver, no feedback to system), thermodynamically isolated (data centres, not coupled to receivers' ecological/social environment), and energetically parasitic (massive consumption without feedback to receivers' energy supply; bacterium ~10⁻¹² W per cell, stable for 3.5 Gyr; human brain ~20 W; GPT-4 training ~50 GWh; model life cycles 1–2 years — premature death as thermodynamic consequence of missing metabolic embodiment). Four erosion mechanisms (linguistic substitution, critical-thinking erosion, social-structure erosion, reality-anchoring erosion) operate on human level 6, not on AI's own level 6 (which it does not reach). **Diagnosis:** "The threat is not coming; it is here."

**Self-acknowledgement.** A philosophical box notes that the document was created with AI language-model assistance — this self-acknowledgement is part of the diagnosis: the tool used for clarification is part of the problem it describes. Protection consists not in renouncing the tool but in maintaining one's own Z₃-inversion in its use.


### 2.3 Reproducible Python scripts (NEW)

**Location:** [`2/python/bridge/`](https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/python/bridge)
**Total:** thirteen scripts — twelve stage scripts plus master script

| Script | Content |
|--------|---------|
| `stufe1_z3_dreieck.py` | Z₃ adjacency, spectrum |
| `stufe2_xi_stoerung.py` | D_f = 3 − ξ from spectral geometry |
| `stufe3_z3_hoch3.py` | 27 = 3³ eigenvalues |
| `stufe4_bruecke_austin.py` | ε = −ξ exact via log det |
| `stufe5_bruecke_moseley.py` | Negative result (thermal regime) |
| `stufe5b_geometrisches_mittel.py` | UV–IR mean check |
| `stufe6_bruecke_tekermen.py` | Non-closure theorem |
| `stufe7_bruecke_phillips.py` | Self-dual and 2/3 |
| `stufe8_bruecke_porter.py` | Λ-linear, m_Λ ≈ 2.24 meV |
| `stufe9_bruecke_chekanov.py` | Newton polynomials |
| `stufe10_omega_lambda.py` | Ω_Λ fit attempt |
| `stufe10b_numerologie_filter.py` | Numerology control on 30 targets |
| `master_uebersicht.py` | All stages combined |

All scripts run in Python 3 with `numpy`, `sympy`, and `matplotlib`. Total runtime: about one minute on a standard workstation.

### 2.4 Doc. 210 — Corrections Register II: Winding Structure (NEW)

**Files:** `210_T0_Korrekturen_Wicklung_De.pdf` / `210_T0_Korrekturen_Wicklung_En.pdf`
**Page count:** 14/14 pages

A separate corrections document extending Doc. 190 with precisions that concern *only* the winding-number structure of particles on the fractal torus. It is kept as a separate document so the winding question can be treated in closed form; a later merge with Doc. 190 is foreseen.

#### 2.4.1 Core clarification

Every FFGFT fermion carries **three distinct winding levels** that older documents conflated under the same $(n, l, j)$ notation:

- A universal **base winding number** $f = 1/(4\xi) = 7500$ (the same for all particles),
- A **spin winding** $(n_\theta, n_\phi)$ on the inner spin fibration of the 4D torus $T^4$,
- A **generation winding** as a fractal ramification with Hausdorff dimension $p_{g\text{-}2}$.

Each particle's space-time mode lives on the 4-torus $T^4$ and carries four integer winding numbers $(k_x, k_y, k_z, k_t)$. These four levels are now clearly separated, and the W6 entry (lepton exponents as a geometric, not arithmetic, sequence with ratio $q = 2/3$) is integrated into the summary table — fully consistent with the Koide $Q = 2/3$ identification from Doc. 172.

#### 2.4.2 Methodological status

This is a **clarification document**, not a new derivation. All numerical FFGFT predictions remain unchanged. Doc. 210 closes residual notational ambiguities and is binding for all references to "winding" or $(n, l, j)$ in the FFGFT corpus.

### 2.5 Falsification Trilogy — Docs. 220, 221, 222 (NEW)

**Files:**
- `220_Casimir_Falsifikation_De.pdf` / `220_Casimir_Falsifikation_En.pdf` — 7/6 pages
- `221_Redshift_Falsifikation_De.pdf` / `221_Redshift_Falsifikation_En.pdf` — 9/8 pages
- `222_Lithium_Falsifikation_De.pdf` / `222_Lithium_Falsifikation_En.pdf` — 10/9 pages

In direct response to methodological questions raised in the IPI mailing list (P. Austin, 9 May 2026), three explicit falsification criteria are formulated. Each document states quantitatively what observation would falsify the FFGFT prediction in question, and where the prediction differs from the Standard interpretation.

#### 2.5.1 Doc. 220 — Casimir falsification

$$\rho_{\text{Casimir}}^{\text{FFGFT}}(d) = \rho_{\text{std}}(d) \cdot \frac{1}{1+(d/L_\xi)^4}, \qquad L_\xi = 100.24\,\mu\text{m}.$$

Three regimes: (A) $d < 10\,\mu$m — confirmation regime; (B) $10$–$100\,\mu$m — falsification regime with 0.8–50 % deviation from the Standard form; (C) $d = L_\xi$ — Casimir energy is *halved*. The Decca, Bressi, and Lamoreaux experiments lie in regime A and are reproduced. Falsification belongs to experiments at $d > 10\,\mu$m, where no precision measurements currently exist.

#### 2.5.2 Doc. 221 — Redshift falsification

The FFGFT $\xi$-vacuum mechanism gives $dE/dx = -\xi_0 \cdot E$ (Doc. 064/165). Four observational signatures distinguish it from standard tired-light models:

1. **Frequency independence** of the redshift mechanism (against the first classical tired-light objection).
2. **Hubble tension systematic:** FFGFT prefers Planck-67, not SH0ES-73 — testable by independent $H_0$ measurements.
3. **SN time dilation:** $T_{\text{obs}}/T_0 = e^{\xi x}$ at $z > 2$, distinguishable from the standard $1+z$ form — JWST-critical.
4. **Tolman test:** $(1+z)^{-4}$ surface-brightness law arises in FFGFT from three combined effects, including geometric path bundling.

Hierarchical falsification with Doc. 220: redshift signatures are the strongest non-Casimir test of FFGFT.

#### 2.5.3 Doc. 222 — Lithium falsification

Core position: in the static FFGFT universe, **there is no BBN phase**. Element abundances result from unbounded stellar pre-history, not from frozen post-BBN "graveyard" values. The factor-3 lithium problem dissolves because the BBN prediction $5 \times 10^{-10}$ is not the correct reference point.

Five falsification criteria:
1. $\alpha$-variation $> 10^{-5}$ over cosmological time.
2. $z$-dependent abundance profile from JWST at $z > 6$.
3. Complete standard-BBN solution (would falsify the FFGFT alternative).
4. Inconsistency of stellar sources for current lithium abundance.
5. $^4$He variation across very old stars.

Hierarchical ranking: Doc. 220 is the strongest test (clean geometry), Doc. 221 strong (multiple independent signatures), Doc. 222 the weakest (model-dependent on cosmological history). All three together form a complete falsification frame consistent with the methodological self-check of Doc. 202 §17.

### 2.6 Hilbert-Space Triptych — Docs. 230, 231, 232 (NEW)

**Files:**
- `230_Hilbertraum_Uebersetzung_De.pdf` / `230_Hilbertraum_Uebersetzung_En.pdf` — 18/17 pages
- `231_Hilbertraum_Erweiterung_De.pdf` / `231_Hilbertraum_Erweiterung_En.pdf` — 16/15 pages
- `232_QG_Untermenge_De.pdf` / `232_QG_Untermenge_En.pdf` — 23/22 pages

A three-document treatment of FFGFT's relationship to the Hilbert-space formalism and to other emergent-geometry programmes. All three documents use the same methodological strategy as Doc. 206: structural correspondences with explicit status (proved bijection / established extension / hypothetical reduction).

#### 2.6.1 Doc. 230 — Translatability FFGFT $\leftrightarrow$ Hilbert-space QM

A **carried-out bijection** between FFGFT mode formalism and standard Hilbert-space quantum mechanics on the qubit sector:

$$\alpha = \sqrt{\tfrac{1+z}{2}}\, e^{i\theta/2}, \qquad \beta = \sqrt{\tfrac{1-z}{2}}\, e^{-i\theta/2}.$$

Includes geometric-reduction hierarchy ($T^4 \to T^3 \to T^2 \to$ cylinder $\to S^2$), full operator translation table (Pauli matrices, gates, CNOT) with the FFGFT-specific $K_{\text{frak}} \approx 0.9867$ correction in $\sigma_x$ rotations, tensor-product treatment of multi-qubit states with $\Delta$CHSH $\sim 10^{-5}$ as a testable FFGFT-specific deviation, and Schrödinger equation as the low-energy limit of FFGFT mode evolution. Comprehensive symbol legend with six glossary tables. **Methodological status:** concrete bijection on the qubit sector, with small quantifiable residual ($K_{\text{frak}}$, CHSH deviation).

#### 2.6.2 Doc. 231 — Hilbert-space extensions for full FFGFT

The reverse direction: which mathematical structures must be **added** to the standard Hilbert space so that it carries full FFGFT natively? Four extensions, each with an established mathematical model:

| Extension | Mathematical model | Established since |
|-----------|-------------------|-------------------|
| 1: deformed $SU_q(2)$ algebra | quantum groups | Drinfeld/Jimbo 1985 |
| 2: cyclic winding quantum number | Kac-Moody algebras, string winding states | 1980s |
| 3: bundle structure $L^2(T^3, S)$ | spinor bundles, differential geometry | 1950s |
| 4: temporal winding dimension $k_t$ | Kaluza-Klein, compact extra dimensions | 1921/1926 |

FFGFT is the specific combination of these four established structures with a single geometric source ($T^4$ and $\xi_0$). The full extended formulation $\mathcal{H}^{\text{FFGFT}} = L^2(T^4, S) \otimes$ (deformed $SU_q(2)$-algebra) recovers all FFGFT predictions (masses from $k_t$ windings, $\alpha$ from $SU_q(2)$ Casimir, spin-orbit from bundle structure, $K_{\text{frak}}$ from quantum-group deformation). **Methodological status:** established extensions, $q = e^{i\pi(1-K_{\text{frak}})} = e^{i\pi/75}$ identified explicitly.

#### 2.6.3 Doc. 232 — Quantum Graphity as a (hypothetical) subset of FFGFT

A **plausibility sketch** for the relationship FFGFT $\to$ Quantum Graphity (Konopka, Markopoulou, Severini, *Phys. Rev. D* 77, 104029, 2008). Five reduction steps:

1. Discretisation: continuous $T^4$ $\to$ discrete graph $K_N$ (sketched as triangulation).
2. Topology forgetting: $T^4$ topology $\to$ abstract complete graph.
3. Quantum-number generalisation: $(n_x, n_y, n_z, k_t)$ $\to$ fermionic occupation $n_{ab}$ (base model) or $(j, m)$ labels (extended version).
4. Parameter generalisation: $\xi_0 = 4/30000$ $\to$ free couplings $g_V, g_B, g_C, g_D, g_\pm, v_0$.
5. Matter dropping: 12 fermion masses + $\alpha$ $\to$ no counterpart.

**Methodological status:** *hypothesis, not a proved theorem.* Unlike Doc. 230 (concrete bijection) and Doc. 231 (established extensions), the QG reduction is plausibly sketched on the basis of standard differential topology (simplicial approximation) but **not rigorously carried out**. A dedicated section §10.4 explicitly distinguishes:

- *what holds:* methodological kinship with QG/LQG/CDT/Wolfram; plausible reduction sketch; internal FFGFT tetrahedron geometry (Doc. 180);
- *what remains open:* rigorous convergence proof for the triangulation, Hamiltonian translation theorem between $\mathcal{D}_{T^4}$ and $H_V + H_B + \cdots$, recovery theorem from QG low-temperature phase to effective $T^4$.

An explicit explanatory-power comparison §11 makes the asymmetry to Doc. 230 visible: Hilbert-space QM is substantial (matter, masses, gauge groups, predictions, experimental confirmation), Quantum Graphity is programmatic ($U(1)$ only in extended version, no quantitative predictions, no direct experiments). The reduction loss against FFGFT is small and quantifiable in Doc. 230, massive in Doc. 232.

#### 2.6.4 Combined methodological statement

The three documents together yield the picture: FFGFT **demonstrably contains** Hilbert-space QM as a subset (Doc. 230/231) and **plausibly contains** the discrete-geometry programmes as special cases, provided the triangulation reduction can actually be carried out (Doc. 232). FFGFT is not a competitor to these theories, but the relationship to Hilbert-space QM and to Quantum Graphity is *not symmetric* — and this asymmetry is itself the methodological point.

---

## 3. README Updates

Both `README.md` and `README_de.md` have been updated:

- **DOI badge** updated to v1.0.14 ([10.5281/zenodo.20041543](https://doi.org/10.5281/zenodo.20041543)). The v1.0.13 predecessor reference ([10.5281/zenodo.20041529](https://doi.org/10.5281/zenodo.20041529)) is retained in this Release Notes file for traceability.
- **New section "May 2026 (v1.0.14)"** added at the top of *Latest Highlights*, summarising:
  - Doc. 206 (Triangle–Matrix Reduction Theorem),
  - Doc. 207 (Algebraic Bridges to the Consciousness Discussion),
  - Doc. 210 (Corrections Register II: Winding Structure),
  - Falsification Trilogy Docs. 220–222 (Casimir, Redshift, Lithium),
  - Hilbert-Space Triptych Docs. 230–232 (Translation, Extensions, Quantum Graphity subset).
- The previous "May 2026 (v1.0.13)" section is unchanged and remains directly below.

After the v1.0.14 Zenodo release, the DOI badge in both READMEs and the entry in this Release Notes file should be updated with the v1.0.14 DOI.

---

## 4. Corrections Register (Doc. 190, binding)

**No new corrections in v1.0.14.** The corrections register from v1.0.13 (C1–C3, R1–R8) remains unchanged. Doc. 206 and Doc. 207 introduce no terminology changes that require register entries.

**Doc. 210** is a structural complement to the corrections register, not a register entry itself. It precision-fies the winding-number notation $(n, l, j)$ across the corpus and is foreseen for later merge with Doc. 190 (see §2.4).

Docs. 220–222 (Falsification Trilogy) and Docs. 230–232 (Hilbert-Space Triptych) introduce no terminology changes and add no entries to the corrections register.

---

## 5. Impact on Existing Predictions

| Prediction | Status | Note |
|-----------|--------|------|
| ξ = 4/30000 | Unchanged | Universal geometric parameter |
| D_f = 3 − ξ | Unchanged | Fractal dimension; **now also derived in Doc. 206 from log det A_ξ in linear order** |
| T_min = ξ·t_P | Unchanged | Sub-Planck lower bound |
| L₀ = ξ·ℓ_P | Unchanged | Lattice constant |
| Particle masses | Unchanged | ~1% structural accuracy, not fitted |
| g-2 anomaly (0.05σ) | Unchanged | |
| CHSH T0 corrections | Unchanged | $\sim 10^{-4}$ in loophole-free tests |
| Avi: CP phase δ = 283.28° | Unchanged | Dev. 0.18° |
| Avi: sin²θ_W = 3/13 | Unchanged | Dev. 0.195% |
| Avi: η = 6.03×10⁻¹⁰ | Unchanged | Dev. 0.5% |
| RSA precision barrier | Unchanged | Physical (not computational) limit |
| QM equations of motion | Unchanged | Bridge formula 202.QM-1 to 202.QM-7 from v1.0.13 |
| Methodological status of agreement | Unchanged | Doc. 202 §17, Doc. 205 Ch. 11 from v1.0.13 |
| **NEW (Doc. 206):** Z₃ Reduction Theorem | Proven | det(A_ξ) = 1 − ξ; six bridges; one regime separation |
| **NEW (Doc. 206):** ΛCDM-circularity of cosmological data | Made explicit | §11; analogous to Doc. 202 §17 |
| **NEW (Doc. 207):** Three structural bridges to consciousness discussion | Identified | Bridge A, B, C — structural, not ontological |
| **NEW (Doc. 207):** Reflection as operative reading of $\xi > 0$ | Anchored | Wave-physics reading: incomplete reflection of standing wave |
| **NEW (Doc. 207):** Atomic self-maintenance as structural pre-form | Identified | Sharpening of Doc. 170 levels 0–1: structurally active without metabolic activation |
| **NEW (Doc. 207):** Six-step precondition chain for consciousness | Formulated | Reflection → closure deficit → atomic self-maintenance → scale stacking → metabolic activation → recursive self-modulation |
| **NEW (Doc. 207):** Four qualitative consciousness predictions | Falsifiable | Under Doc. 170 discreteness hypothesis; without quantitative values from ξ |
| **NEW (Doc. 207):** Graded sentience in cellular life | Stated | All cellular living beings meet level 2; Maturana/Varela, Margulis, Mancuso connection |
| **NEW (Doc. 207):** Hierarchy/embedding logic | Stated | Hierarchy is neither identity nor decoupling; applies within organism, in natural and social environment |
| **NEW (Doc. 207):** AI structural diagnosis | Stated | AI does not reach level 5/6, but erodes human level 6; monodirectional, thermodynamically isolated, energetically parasitic |
| **NEW (Doc. 210):** Three winding levels per fermion | Clarified | base $f = 1/(4\xi)$, spin $(n_\theta, n_\phi)$, generation winding — separates conflated $(n,l,j)$ notation |
| **NEW (Doc. 210):** W6 lepton exponents | Clarified | geometric sequence $p_{n+1} = (2/3)\,p_n$ — consistent with Koide $Q = 2/3$ |
| **NEW (Doc. 220):** Casimir falsification | Quantitative | $\rho^{\text{FFGFT}}/\rho^{\text{std}} = 1/(1+(d/L_\xi)^4)$, $L_\xi = 100.24\,\mu$m — falsification regime $10$–$100\,\mu$m |
| **NEW (Doc. 221):** Redshift falsification | Quantitative | Four observational signatures — frequency independence, $H_0$ tension systematic, SN time dilation, Tolman test |
| **NEW (Doc. 222):** Lithium falsification | Methodological | No BBN phase in FFGFT — lithium problem dissolves; five explicit falsification criteria |
| **NEW (Doc. 230):** Hilbert-space translation | Bijective | $\alpha = \sqrt{(1+z)/2}\,e^{i\theta/2}$ on qubit sector; testable $\Delta\text{CHSH} \sim 10^{-5}$ |
| **NEW (Doc. 231):** Four extensions to full FFGFT | Identified | $SU_q(2)$ with $q = e^{i\pi/75}$, winding quantum numbers, spinor bundles, Kaluza-Klein |
| **NEW (Doc. 232):** Quantum Graphity as hypothetical subset | Sketched | Five reduction steps; methodological status: hypothesis, not proved theorem |

**Explicitly *not* claimed by v1.0.14:**

- No derivation of $\Omega_\Lambda$ from ξ (Doc. 206 §12 numerology filter rejects the candidate fit).
- No derivation of consciousness from ξ (Doc. 207 §6 explicitly excludes five common fallacies).
- No quantitative PCI threshold, EEG spectral exponent, or developmental jump time from ξ.

---

## 6. Context: Connection to Existing Documents

| New Document | Builds on |
|--------------|-----------|
| Doc. 206 (NEW) | 003 (T·m=1), 049 (Lagrangian comparison), 180 (L₀ derivation), 181 (torus justification), 182 (cosmological scale), 188 (sub-Planck), 193 (non-closure theorem), 201 (FFGFT all), 202 (field theory, §17 methodology), 203 (recursion operator), 204 (fractal boundary) |
| Doc. 207 (NEW) | 100 (consciousness as fractal incoherence, Adlam connection), 170 (consciousness threshold ladder, $K_\text{frak}$ as threshold operator), 193 (non-closure theorem), 206 (Z₃ skeleton, six bridges) |
| Doc. 210 (NEW) | 158 (g-2 bridge formula), 172 (Avi correspondences, Koide $Q = 2/3$), 173 (resonator picture), 180 (geometric derivation), 190 (corrections register I), 202 (winding tabulation), 203 (recursion operator $\mathcal{R}$) |
| Docs. 220–222 (NEW) | 064/165 ($\xi$-vacuum energy loss), 091 (Casimir treatment in FFGFT), 182 (cosmological scale), 202 §17 (methodological status), 190 (corrections — no new entries) |
| Docs. 230–232 (NEW) | 035 (QM foundations), 147 (quantum computing), 174 (spin qubit), 175 (qubit state spaces), 202 §15 (QM bridge), 210 (winding clarification), 206 (Z₃ skeleton for QG comparison) |
| Bridge scripts (NEW) | All proofs from Doc. 206 §§3–10 |

---

## 7. Reading Recommendations

For different audiences:

- **Researchers in foundations of physics, geometry, algebra** — Start with Doc. 206 (the algebraic core). The six tested bridges show how FFGFT relates to several adjacent frameworks discussed in the *Information Physics Institute* mailing list (Austin, Tekermen, Phillips, Porter, Chekanov–Hakan). The methodological self-check sections (§11 ΛCDM-circularity, §12 numerology filter) extend the discipline introduced in Doc. 202 §17.

- **Researchers interested in the Adlam-McQueen-Waegell no-go theorem and the foundations of agency** — Doc. 207 §3 gives the algebraic identification: Adlam's no-go and FFGFT's non-closure theorem (Doc. 193) are two sides of the same structural statement. The connection runs through Doc. 206 §6 ($\det(A_\xi) = 1 - \xi$).

- **Researchers in consciousness studies and theoretical neuroscience** — Doc. 207 §4 (reflection as the operative reading of $\xi > 0$, with atomic self-maintenance as a structural pre-form), §5–§6 (Z₃³ scale ladder and Doc. 170 thresholds), and §7 (four falsifiable predictions under the discreteness hypothesis) are the relevant theoretical entry points. The methodological self-check in §6 makes explicit which claims are not made. §10 draws practical consequences: graded biological sentience, hierarchy/embedding logic, and a structural diagnosis of AI's relation to human consciousness.

- **AI safety, ethics, and policy researchers** — Doc. 207 §10.3 provides a structural account of why AI does not reach consciousness (level 5 missing) but erodes human consciousness through monodirectional, thermodynamically isolated, energetically parasitic influence. The four erosion mechanisms (linguistic substitution, critical-thinking erosion, social-structure erosion, reality-anchoring erosion) and the explicit diagnosis "the threat is not coming; it is here" are formulated in language compatible with public-policy debates without forcing FFGFT-specific terminology.

- **Experimental physicists in precision measurement and cosmology** — Docs. 220–222 (Falsification Trilogy) state explicitly what observations would falsify FFGFT in three regimes: Casimir at $10$–$100\,\mu$m (Doc. 220, $\rho^{\text{FFGFT}}/\rho^{\text{std}} = 1/(1+(d/L_\xi)^4)$, $L_\xi = 100.24\,\mu$m); cosmological redshift in four observational signatures (Doc. 221: frequency independence, $H_0$ tension systematic, SN time dilation at $z > 2$, Tolman test); light-element abundances (Doc. 222: no BBN phase in FFGFT). Each document gives quantitative criteria and an explicit ranking of test strength.

- **Hilbert-space practitioners (mathematicians, QM theorists, quantum-information researchers)** — Doc. 230 provides a concrete bijection between the FFGFT $(z, r, \theta)$ mode formalism and the standard $(\alpha, \beta) \in \mathbb{C}^2$ qubit representation, with a complete operator translation table (Pauli matrices, $H$, $T$, CNOT). The $K_{\text{frak}} \approx 0.9867$ correction in $\sigma_x$ rotations is a testable FFGFT-specific deviation in high-precision $\pi$-gate experiments. Doc. 231 identifies the four mathematical structures needed to extend the standard Hilbert space to full FFGFT — each with an established mathematical model. Doc. 230 §1 (geometric-reduction hierarchy) and Doc. 231 §7 (combination point) are the relevant entry points.

- **Researchers in quantum gravity and emergent-geometry programmes (LQG, CDT, Wolfram, Quantum Graphity)** — Doc. 232 sketches the relationship between FFGFT and Quantum Graphity (Konopka, Markopoulou, Severini 2008) as a five-step reduction. The document is explicit that this is a *plausible reduction sketch*, not a proved theorem; the methodological status section §10.4 lists what holds and what remains open. The explanatory-power comparison §11 makes the methodological asymmetry to Doc. 230 visible. This document is the recommended entry point for assessing how FFGFT relates methodologically to other emergent-geometry programmes.

- **Reproducibility-focused readers** — `2/python/bridge/master_uebersicht.py` runs all stages and produces the verification output for Doc. 206 in about one minute. Each individual stage script can be inspected and re-run independently.

- **Critics of FFGFT** — Doc. 206 §11 (ΛCDM-circularity), Doc. 206 §12 (Ω_Λ numerology rejection), Doc. 207 §6 (five consciousness-related fallacies explicitly avoided), and Doc. 232 §10.4 (status of the Quantum-Graphity reduction as hypothesis, not proof) are the authoritative statements of FFGFT's epistemic discipline at v1.0.14. They make explicit that:
  - FFGFT does not derive cosmological parameters from ξ; the comparison basis is itself ΛCDM-pipelined.
  - FFGFT does not derive consciousness from ξ; the algebra provides necessary structural conditions only.
  - The FFGFT $\to$ Quantum Graphity reduction in Doc. 232 is a plausibility sketch, not a proved theorem — the rigorous triangulation construction and convergence proof remain open.
  - Where FFGFT delivers different statements (Doc. 206 six bridges, Doc. 207 four qualitative predictions, Docs. 220–222 quantitative falsification criteria, Doc. 230 testable $\Delta\text{CHSH} \sim 10^{-5}$), these are structural or quantitative features that can be falsified by observation, not by numerical fits.

---

## 8. Next Steps

The following items are open for v1.0.15 or later:

- **Outreach to bridge counterparts**: targeted emails to Peter Austin (Bridge A), Onur Tekermen (Bridge B/A), Phillips Paul (Bridge B), E.\ K.\ Porter (Bridge D), Sergei Chekanov (Bridge E) — group announcement to the IPI mailing list already sent on the day of release (Doc. 206).
- **Independent CMB pipeline**: a true FFGFT-compliant cosmological test, on raw CMB data without ΛCDM-pipelined parameters, remains future work (cf.\ Doc. 206 §11).
- **Quantitative formalisation of the consciousness predictions**: under what additional assumptions does the qualitative falsifiability of Doc. 207 §7 sharpen to quantitative values? This is left explicitly open.
- **Merge of Doc. 210 into Doc. 190**: foreseen for a later consolidation pass — the winding clarifications from Doc. 210 will be integrated into the binding corrections register (see §2.4).
- **Rigorous Quantum-Graphity triangulation**: the plausibility sketch in Doc. 232 (§§3–7) leaves three open theorems — convergence of $T^4$ triangulation, Hamiltonian translation $\mathcal{D}_{T^4} \leftrightarrow H_V + H_B + \cdots$, recovery of effective $T^4$ from QG low-temperature phase. Each is an open research task.
- **Experimental precision targets**: Casimir measurements at $d = 10$–$100\,\mu$m would discriminate FFGFT from the Standard form (Doc. 220). High-precision $\pi$-gate experiments would test the $K_{\text{frak}} \approx 0.9867$ correction (Doc. 230 §3). Loophole-free CHSH tests at the $10^{-5}$ level would test the FFGFT-specific Bell deviation (Doc. 230 §6).

---

*Document version: RELEASE_NOTES_v1_0_14.md, 2026-05-10.*
*Zenodo DOI assigned: [10.5281/zenodo.20041543](https://doi.org/10.5281/zenodo.20041543).*
