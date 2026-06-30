# T0 Theory / FFGFT v1.1.0 — Hilbert-Space Bridge: A Consolidated Release

**Release Date:** 2026-05-11
**Version:** 1.1.0 (consolidated)
**DOI:** [10.5281/zenodo.20117635](https://doi.org/10.5281/zenodo.20117635)
**GitHub:** https://github.com/jpascher/T0-Time-Mass-Duality
**Author:** Johann Pascher (ORCID: [0009-0000-6518-4064](https://orcid.org/0009-0000-6518-4064))
**Predecessors:** v1.0.14 ([10.5281/zenodo.20041543](https://doi.org/10.5281/zenodo.20041543)); v1.0.13 ([10.5281/zenodo.20041529](https://doi.org/10.5281/zenodo.20041529)); v1.0.12 ([10.5281/zenodo.20022166](https://doi.org/10.5281/zenodo.20022166)); v1.0.11 ([10.5281/zenodo.18834145](https://doi.org/10.5281/zenodo.18834145))

---

## About this repository

**T0/FFGFT (Fundamental Fractal-Geometric Field Theory)** is a unified geometric framework for quantum mechanics, relativity, and cosmology, developed by Johann Pascher (independent theoretical physicist and HTL-trained technician, Austria). The framework derives all Standard-Model constants from a single dimensionless parameter $\xi = 4/30000 = (4/3) \times 10^{-4}$, anchored by the foundational relation

$$\tilde{T} \cdot m = 1$$

between an intrinsic time field $\tilde{T}$ and mass $m$.

The repository (https://github.com/jpascher/T0-Time-Mass-Duality) contains the complete corpus:

- **220+ PDF documents** in parallel German and English (`2/pdf/`)
- **191+ LaTeX source files** (`2/tex/ch/` for chapter content, `2/tex/build/` for wrappers)
- **19 interactive HTML tools** for fine-structure constant, particle masses, quantum computing, sub-Planck geometry, RSA factorisation
- **Python implementations** including the 13-script verification suite for Doc. 206 (`2/python/bridge/`)
- **Published books** (Kindle 6×9 and A4 formats) covering different audience levels
- **Audio podcasts and YouTube channel** ([@Time-MassDuality](https://www.youtube.com/@Time-MassDuality))
- **44-chapter narrative edition** using the "cosmic brain" metaphor for general audiences
- **The Harmonikabau documentation series** (Docs. 0000–0024, structurally complete) as an applied counterpart to the theoretical work

**What FFGFT delivers:**
- All physical constants ($G$, $c$, $\hbar$, $\ell_P$, $\alpha \approx 1/137.036$) from $\xi$
- 12 fermion masses with ~1 % structural accuracy, *not* fitted
- Muon $g-2$ anomaly to 0.05 $\sigma$ precision
- Hubble tension resolution (FFGFT prefers Planck-67)
- Alternative to dark energy and MOND
- Deterministic quantum mechanics with testable Bell-correlation deviations
- Sub-Planck length scale $L_0 = \xi \cdot \ell_P$ as universal lower bound

**Zero free parameters beyond $\xi$.** This is the central methodological commitment: the framework derives, it does not fit.

---

## 1. Why this is a major release

The four point releases v1.0.11 through v1.0.14 each added substantial material in a focused direction. v1.1.0 consolidates them into a single major release, with one new result in the foreground:

**FFGFT has a carried-out bijection to standard Hilbert-space quantum mechanics on the qubit sector** (Doc. 230). This changes FFGFT's position in the theoretical landscape. Where earlier releases established FFGFT as an internally complete framework that *derives* the Standard-Model constants from $\xi$, v1.1.0 establishes that FFGFT is also **compatible with the existing Hilbert-space formalism**: every quantum-mechanical statement on the qubit sector translates into FFGFT mode language, with a small quantifiable residual that is itself a testable FFGFT prediction.

This bijection upgrades FFGFT from "an alternative formulation" to "a framework that contains the standard formalism as a subset and extends it natively." Two companion documents complete the picture:

- **Doc. 231** identifies the four established mathematical structures ($SU_q(2)$, Kac–Moody winding states, spinor bundles, Kaluza-Klein) that must be added to the standard Hilbert space to recover full FFGFT.
- **Doc. 232** sketches Quantum Graphity (Konopka, Markopoulou, Severini 2008) as a hypothetical subset of FFGFT — explicitly marked as plausibility sketch, not proved theorem.

The three documents together yield a coherent picture: FFGFT *demonstrably* contains Hilbert-space QM as a subset, and *plausibly* contains the discrete-geometry programmes as further special cases. The methodological asymmetry between "demonstrably" and "plausibly" is itself one of the methodological points of v1.1.0.

---

## 2. The Hilbert-Space Triptych (Docs. 230, 231, 232)

This is the centrepiece of v1.1.0.

### 2.1 Doc. 230 — Translatability FFGFT $\leftrightarrow$ Hilbert-space QM

**Status: carried-out bijection.**

A complete bijection between the FFGFT mode formalism and the standard Hilbert-space qubit formalism:

$$\alpha = \sqrt{\tfrac{1+z}{2}}\, e^{i\theta/2}, \qquad \beta = \sqrt{\tfrac{1-z}{2}}\, e^{-i\theta/2}.$$

Includes the geometric reduction hierarchy ($T^4 \to T^3 \to T^2 \to$ cylinder $\to S^2$), a full operator translation table (Pauli matrices, gates, CNOT), and the FFGFT-specific $K_{\text{frak}} \approx 0.9867$ correction in $\sigma_x$ rotations. Multi-qubit tensor products give a predicted $\Delta\text{CHSH} \approx 10^{-5}$ — a small, FFGFT-specific deviation that is in principle testable in loophole-free Bell experiments. The Schrödinger equation emerges as the low-energy limit of FFGFT mode evolution.

**Practical consequence:** any quantum-mechanical analysis written in standard Hilbert-space language has a direct FFGFT counterpart, and vice versa.

### 2.2 Doc. 231 — Hilbert-space extensions for full FFGFT

**Status: established extensions.**

The reverse direction. To carry full FFGFT natively in Hilbert-space language, four established mathematical structures are needed:

| Extension | Mathematical model | Established since |
|-----------|-------------------|-------------------|
| Deformed $SU_q(2)$ algebra | Quantum groups | Drinfeld/Jimbo, 1985 |
| Cyclic winding quantum number | Kac–Moody algebras, string winding | 1980s |
| Bundle structure $L^2(T^3, S)$ | Spinor bundles | 1950s |
| Temporal winding $k_t$ | Kaluza-Klein, compact extra dimensions | 1921/1926 |

FFGFT is the specific combination of these four well-known structures with a single geometric source ($T^4$ with $\xi_0 = 4/30000$). The combined Hilbert space $\mathcal{H}^{\text{FFGFT}} = L^2(T^4, S) \otimes SU_q(2)$ recovers all FFGFT predictions: masses from $k_t$-windings, $\alpha$ from $SU_q(2)$ Casimir, spin-orbit from bundle structure, $K_{\text{frak}}$ from quantum-group deformation with $q = e^{i\pi(1-K_{\text{frak}})} = e^{i\pi/75}$.

**Practical consequence:** FFGFT is not exotic. It uses only mathematical structures that have been part of theoretical physics for between forty and one hundred years.

### 2.3 Doc. 232 — Quantum Graphity as a (hypothetical) subset of FFGFT

**Status: plausibility sketch, *not* a proved theorem.**

A five-step reduction sketch from full FFGFT to Quantum Graphity (Konopka, Markopoulou, Severini, *Phys. Rev. D* 77, 104029, 2008):

1. Discretisation: continuous $T^4$ → discrete graph $K_N$ (sketched as triangulation).
2. Topology forgetting: $T^4$ topology → abstract complete graph.
3. Quantum-number generalisation: $(n_x, n_y, n_z, k_t)$ → fermionic occupation $n_{ab}$ or $(j, m)$ labels.
4. Parameter generalisation: $\xi_0 = 4/30000$ → free couplings $g_V, g_B, g_C, g_D, g_\pm, v_0$.
5. Matter dropping: 12 fermion masses + $\alpha$ → no counterpart.

Doc. 232 §10.4 explicitly distinguishes:

- *what holds:* methodological kinship with QG/LQG/CDT/Wolfram; the plausibility of the reduction sketch on the basis of standard differential topology (simplicial approximation); the internal FFGFT tetrahedron geometry (4/3 factor in $\xi_0$, Doc. 180);
- *what remains open:* a rigorous convergence proof for the $T^4$ triangulation; a Hamiltonian translation theorem between $\mathcal{D}_{T^4}$ and $H_V + H_B + \cdots$; a recovery theorem from the QG low-temperature phase to an effective $T^4$.

Doc. 232 §11 makes the asymmetry to Doc. 230 explicit: Hilbert-space QM is *substantial* (matter, masses, gauge groups, predictions, a century of experimental confirmation); Quantum Graphity is *programmatic* ($U(1)$ only in extended version, qualitative predictions, no direct experiments, 17 years old). The reduction loss against FFGFT is small and quantifiable in Doc. 230, massive in Doc. 232 — and this asymmetry is the methodological point.

### 2.4 Combined statement

FFGFT shares with Hilbert-space QM a *carried-out bijection* (Doc. 230) and a path of *established extensions* (Doc. 231). It shares with the discrete-geometry programmes (Quantum Graphity, LQG, CDT, Wolfram hypergraphs) a *methodological kinship* whose precise mathematical realisation is an open research task (Doc. 232 §10.4). FFGFT is therefore not a competitor to either family, but its relationship to them is *not symmetric* — and the asymmetry is itself an honest methodological statement.

---

## 3. Earlier consolidation milestones (summary)

This section briefly summarises what entered the corpus through v1.0.11–v1.0.14. For full detail, see the individual release notes files retained in the repository.

### 3.1 Field theory and methodological status (v1.0.13)

Doc. 202 (Complete Field Theory) was extended in three ways: §15 added an explicit bridge to the standard quantum-mechanical equations of motion (Schrödinger, Dirac, Bell, qubit mappings); §17 added the methodological status of the verification condition (PDG-circularity of cross-section comparisons); the renormalisation-group section was renamed to FFGFT-native scale-structure language. Doc. 190 (Corrections Register) gained R7 (renormalisation-group terminology) and R8 (fractal renormalisation). Doc. 205 (FFGFT in Plain Language) was added as a stand-alone, non-technical entry document.

### 3.2 Algebraic completeness: non-closure theorem (v1.0.12)

Docs. 192–193 stated and proved the FFGFT non-closure theorem: FFGFT mode composition has irreducible algebraic limits at $\xi > 0$ — full closure is incompatible with $\xi$-positivity. This is the algebraic counterpart to FFGFT's geometric statement that $\xi > 0$ means "the universe cannot close completely on itself."

### 3.3 Field theory and operator formalism (v1.0.12)

Docs. 202–204 introduced the FFGFT field theory as a complete formulation: Doc. 202 (the field theory itself), Doc. 203 (recursion operator $\mathcal{R}$), Doc. 204 (fractal boundary condition). These three documents together replace the older mode-by-mode treatment with a unified operator formalism.

### 3.4 Quantum-computing series (v1.0.11)

Docs. 170–176, 178–179 treated FFGFT's relationship to quantum computation: discrete complexity thresholds, qubit state spaces, single-clock metrology, spin-qubit treatment, RSA precision barrier (a physical, not computational, limit), and the Google Willow / p-bit / photonics / Gemini analyses.

### 3.5 Lagrangian derivations and torus structure (v1.0.11)

Docs. 180–182 derived $L_0 = \xi \cdot \ell_P$ from the Lagrangian, justified the 4D torus geometry, and gave the cosmological maximum-scale interpretation. Every mass scale carries its own torus $R_{\text{torus}}(m) = \hbar/(mc)$, all sharing $L_0$ as common lower bound.

### 3.6 Torsion geometry and biological analogies (v1.0.11)

Docs. 149–156, 158–159 covered the torsion-geometric formulation, ontology of the FFGFT framework, structural biological analogies (cortex, DNA folding), the Koide–$g-2$ bridge formula (Doc. 158, $Q = 2/3$ as a geometric ratio), and the harmonic torus structure.

### 3.7 Periodic table as $\xi$-geometry (v1.0.11)

Docs. 168–169 derived the structure of the periodic table from FFGFT geometric quantisation, recovering electron-shell filling order from $\xi$-scaling without separately fitted quantum numbers.

### 3.8 Triangle–matrix reduction and consciousness bridges (v1.0.14)

Doc. 206 proved the Triangle–Matrix Reduction Theorem: every consistent geometric description of physical structures in FFGFT's scale regime maps onto two equivalent representations — a $\mathbb{Z}_3$ triangle connection and a $3 \times 3$ matrix algebra. Six bridges to other formulations (Austin, Tekermen, Phillips, Porter, Chekanov–Hakan, Moseley) were tested; five hold algebraically, one is identified as a regime separation rather than a contradiction. Doc. 207 established three structural bridges from this algebraic skeleton to the existing FFGFT consciousness discussion (Doc. 100, Doc. 170), with four falsifiable qualitative predictions under the discreteness hypothesis. Thirteen reproducible Python scripts (`2/python/bridge/`) implement every Doc. 206 proof.

### 3.9 Winding-structure clarification (v1.0.14)

Doc. 210 (Corrections Register II) separated three previously conflated winding levels per fermion: the universal base winding $f = 1/(4\xi) = 7500$, the spin winding $(n_\theta, n_\phi)$ on the $T^4$ spin fibration, and the generation winding as fractal ramification with Hausdorff dimension $p_{g\text{-}2}$. All numerical predictions remain unchanged; later merge with Doc. 190 is foreseen.

### 3.10 Falsification trilogy (v1.0.14)

Docs. 220–222 stated explicit, quantitative falsification criteria for FFGFT in three regimes:

- **Doc. 220 — Casimir:** $\rho^{\text{FFGFT}}(d) = \rho^{\text{std}}(d) \cdot 1/(1+(d/L_\xi)^4)$ with $L_\xi = 100.24\,\mu$m. Falsification regime at $d = 10$–$100\,\mu$m, where no precision measurements currently exist.
- **Doc. 221 — Redshift:** four observational signatures (frequency independence, Hubble-tension systematic with FFGFT preferring Planck-67, SN time dilation $T_{\text{obs}}/T_0 = e^{\xi x}$ at $z > 2$, Tolman test $(1+z)^{-4}$ from three combined effects).
- **Doc. 222 — Lithium:** in the static FFGFT universe there is no BBN phase, so the BBN prediction $5 \times 10^{-10}$ is not the correct reference point. Five falsification criteria, ranked as the weakest of the three (model-dependent on cosmological history).

---

## 4. Status of the corpus at v1.1.0

The FFGFT corpus now consists of three layers, each with a distinct methodological status:

| Layer | Status | Key documents |
|-------|--------|---------------|
| Core derivations | Proven from $\xi = 4/30000$ | 003 ($\tilde{T} \cdot m = 1$), 049 (Lagrangian), 158 (Koide-$g-2$), 168 (periodic table), 174 (spin qubit), 180 ($L_0$ from Lagrangian), 202 (field theory) |
| External bridges | Algebraically or structurally proven | 172 (Avi correspondences), 206 (six bridges, Z₃ skeleton), 230 (Hilbert-space bijection), 231 (four extensions) |
| Hypothetical reductions | Plausibility sketches, open theorems | 232 (Quantum Graphity reduction) |

**What v1.1.0 does *not* claim:**

- No derivation of $\Omega_\Lambda$ from $\xi$ (Doc. 206 §12 numerology filter rejects the candidate fit).
- No derivation of consciousness from $\xi$ (Doc. 207 §6 explicitly excludes five common fallacies).
- No proved theorem of "Quantum Graphity $\subset$ FFGFT" (Doc. 232 §10.4 retains the status as plausibility sketch).
- No precision matching of cross-sections via PDG-pipelined data (Doc. 202 §17).
- No $\xi$-derived CMB parameters without an independent (non-ΛCDM-pipelined) cosmological pipeline (Doc. 206 §11).

This three-layer presentation is itself a v1.1.0 commitment: the corpus is honest about which results are derived, which are bridged, and which are open.

---

## 5. Repository structure

```
T0-Time-Mass-Duality/
├── README.md / README_de.md         — full project overview (EN/DE)
├── RELEASE_NOTES_v1_1_0.md          — this file (consolidated v1.1.0)
├── RELEASE_NOTES_v1_0_{11..14}.md   — historical point-release detail
└── 2/
    ├── pdf/                          — 220+ compiled PDFs (DE/EN)
    ├── tex/
    │   ├── ch/                       — chapter content (NNN_Title_{De|En}_ch.tex)
    │   ├── build/                    — wrapper documents (NNN_Title_{De|En}.tex)
    │   ├── pri-end/                  — shared preambles
    │   └── ipi/                      — IPI mailing-list outreach material
    ├── html/                         — 19 interactive tools
    ├── python/
    │   └── bridge/                   — 13-script verification suite for Doc. 206
    └── audio/                        — podcast episodes
```

LaTeX builds use XeLaTeX / LuaLaTeX with a Kindle 6×9 page geometry for the recent (≥ 200) document series, and A4 for the earlier (< 200) corpus.

---

## 6. Reading recommendations

For different audiences:

- **First-time readers without prior FFGFT background** — Doc. 205 (FFGFT in Plain Language, added in v1.0.13) is the recommended entry. Then Doc. 201 (Unified Synthesis) and Doc. 230 (Hilbert-space bijection).
- **Hilbert-space practitioners, QM theorists, quantum-information researchers** — Start with Doc. 230. The bijection on the qubit sector and the testable $K_{\text{frak}}$ correction ($\Delta\text{CHSH} \approx 10^{-5}$ in loophole-free Bell tests) are the relevant entry points. Doc. 231 §7 gives the combined extended formulation.
- **Mathematical physicists** — Doc. 231 lists the four established mathematical structures and identifies $q = e^{i\pi/75}$ explicitly. The geometric reduction hierarchy $T^4 \to T^3 \to T^2 \to$ cylinder $\to S^2$ in Doc. 230 is the structural anchor.
- **Researchers in foundations of physics and emergent geometry** — Doc. 232 sketches the relationship to Quantum Graphity (and methodologically: LQG, CDT, Wolfram). The status section §10.4 is the recommended entry point — it makes explicit what holds, what is open, and how FFGFT relates honestly to other emergent-geometry programmes.
- **Experimental physicists** — Docs. 220–222 (Falsification Trilogy) give quantitative criteria in three regimes (Casimir, redshift, lithium). Doc. 230 adds a fourth: loophole-free CHSH at the $10^{-5}$ level.
- **Researchers in the IPI / consciousness / algebraic-bridge discussions** — Doc. 206 (Triangle–Matrix Reduction Theorem) and Doc. 207 (algebraic bridges with four falsifiable predictions). The 13 reproducible Python scripts run every Doc. 206 proof in about one minute via `2/python/bridge/master_uebersicht.py`.
- **Critics** — Doc. 202 §17 (PDG-circularity), Doc. 206 §11 (ΛCDM-circularity), Doc. 206 §12 (numerology filter), Doc. 207 §6 (five consciousness-related fallacies explicitly avoided), and Doc. 232 §10.4 (Quantum-Graphity status as hypothesis, not proof) are the authoritative statements of FFGFT's epistemic discipline at v1.1.0.

---

## 7. Next steps

The following items are open for v1.2.0 or later:

- **Rigorous Quantum-Graphity triangulation:** the plausibility sketch in Doc. 232 leaves three open theorems — $T^4$ triangulation convergence, Hamiltonian translation, and recovery from the QG low-temperature phase.
- **Experimental precision targets:** Casimir at $d = 10$–$100\,\mu$m (Doc. 220 falsification regime); high-precision $\pi$-gate experiments testing $K_{\text{frak}} \approx 0.9867$ (Doc. 230 §3); loophole-free CHSH at $10^{-5}$ (Doc. 230 §6).
- **Independent CMB pipeline:** a true FFGFT-compliant cosmological test on raw CMB data without ΛCDM-pipelined parameters (cf. Doc. 206 §11).
- **Merge of Doc. 210 into Doc. 190:** consolidation of the winding clarifications into the binding corrections register.
- **Outreach to bridge counterparts:** continued engagement with the *Information Physics Institute* mailing list (Austin, Tekermen, Phillips, Porter, Chekanov–Hakan) following the Doc. 206 group announcement.
- **Quantitative formalisation of the consciousness predictions:** under what additional assumptions does the qualitative falsifiability of Doc. 207 §7 sharpen to quantitative values? Left explicitly open.

---

## 8. Version history

| Version | Date | DOI | Headline contribution |
|---------|------|-----|----------------------|
| 1.0.11 | 2026-05-04 | [18834145](https://doi.org/10.5281/zenodo.18834145) | Quantum-computing series, periodic table, RSA precision barrier, corrections register |
| 1.0.12 | 2026-05-05 | [20022166](https://doi.org/10.5281/zenodo.20022166) | Non-closure theorem (Docs. 192–193); field theory and operator formalism (Docs. 202–204) |
| 1.0.13 | 2026-05-05 | [20041529](https://doi.org/10.5281/zenodo.20041529) | Doc. 202 §15 (QM bridge), §17 (PDG-circularity); Doc. 205 (Plain Language); Doc. 190 R7/R8 |
| 1.0.14 | 2026-05-10 | [20041543](https://doi.org/10.5281/zenodo.20041543) | Triangle–Matrix Reduction (206), consciousness bridges (207), winding clarification (210), falsification trilogy (220–222), Hilbert-space triptych (230–232) |
| **1.1.0** | **2026-05-11** | **[10.5281/zenodo.20117635](https://doi.org/10.5281/zenodo.20117635)** | **Consolidated release: Hilbert-space bijection as centrepiece** |

The earlier point-release notes (`RELEASE_NOTES_v1_0_11.md` through `RELEASE_NOTES_v1_0_14.md`) are retained in the repository for full historical detail. v1.1.0 supersedes them as the entry point.

---

## How to cite

> Pascher, J. (2026). *T0-Time-Mass-Duality / FFGFT v1.1.0: Hilbert-Space Bridge — A Consolidated Release.* Zenodo. DOI: [10.5281/zenodo.20117635](https://doi.org/10.5281/zenodo.20117635).

For the v1.0.14 corpus state with all individual document references:

> Pascher, J. (2026). *T0-Time-Mass-Duality / FFGFT v1.0.14.* Zenodo. DOI: [10.5281/zenodo.20041543](https://doi.org/10.5281/zenodo.20041543).

---

## License and contact

- **Author:** Johann Pascher (Austria); ORCID [0009-0000-6518-4064](https://orcid.org/0009-0000-6518-4064)
- **Outreach contact:** [johann.pascher@gmail.com](mailto:johann.pascher@gmail.com) (please CC on all FFGFT-related correspondence)
- **YouTube channel:** [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality)
- **GitHub:** https://github.com/jpascher/T0-Time-Mass-Duality

---

*Document version: RELEASE_NOTES_v1_1_0.md, 2026-05-11.*
*Zenodo DOI assigned: 10.5281/zenodo.20117635.*
