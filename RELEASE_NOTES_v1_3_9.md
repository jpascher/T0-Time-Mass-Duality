# Release Notes — v1.3.9 (14 September 2026)

**DOI:** to be assigned on Zenodo publication — supersedes v1.3.8
Running corrections: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Change log: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows: all Standard Model
constants follow from a single dimensionless parameter **ξ = 4/30000** on a compact
4D torus T⁴. The foundational relation is **T̃ · m = 1** — intrinsic time and mass
are inversely coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

This release brings two new books to Amazon Kindle, substantially extends Doc. 341
(algebraic bridge FFGFT↔GALG) through a productive exchange with Doug Matzke,
and adds three new documents (Docs. 361–363). No algebraic results from Docs. 342–360
are changed; one downgrade (Doc. 355 heptagonal phases [B]→[S]) and one correction
(Hyperbit book ch07 citation style) are included.

---

## New books on Amazon Kindle

### Bits, Hyperbits and Landauer (DE+EN, 93 pp. each)

Available as Kindle eBook, paperback and hardcover on Amazon KDP (all markets).
The book compares the information physics of Matzke's Hyperbit framework with FFGFT
and develops the Landauer bound thermodynamically.
Core statement: an information bit cannot be assigned any energy — only its carrier can.
In the Hyperbit framework the 6 generators in G(6) are the carrier;
in FFGFT it is the winding mode on the T⁴/Z₃ torus.

---

## New and extended documents since v1.3.8

### Doc. 341 — GF(27) in GALG: algebraic bridge FFGFT↔GALG (DE+EN, 15 pp. each)
*(substantially extended — was 9 pp. in v1.3.8)*

**§5 Vacuum structure (new):** Vss[0..5] in Cl(6)/GF(9), Witt pairs {13,26,45},
ℤ₃ separation — even vacua = fixed points, odd = three-orbit = Frobenius split [B].
Neutrino = Vss[0], bilateral sector-changers as gluon role.

**§6 Higher roots of unity (new):** Entry scale ord_p(3): 13 (k=3), 5 (k=4),
11 (k=5), 7 (k=6) [K]. No root7 with Z3C coefficients (cos(2π/7) ∉ GF(3^k));
order-7 element X₇ = C_Φ₇ ⊕ I₂ in G(6), compact: Y (6 blades, ord 182=2·7·13),
X = Y²⁶ [K/B]. X²⁷=X ⟺ spectrum ⊂ GF(27): field-tower N→r₂₆→X₇ [K].
Coefficient purity: root26 with pure coefficients (5 blades) [B].
E�� convention: E₇=−(e₁…e₆) explains Matzke's p27 finding [K].
Jordan decomposition X=S·U: r₂₇₃, r₅₄₆, r₂₁₈₄ in G(6) via 6-dim block ⊕ J₂ [K].
r₇₂₉ only from Cl(16)=M₂₅₆; unrelated to GF(729) [K].
Euler's φ: φ(80)=32, φ(182)=72 [K].

**Tool note (new):** Clear separation of roles — authorship Pascher+Matzke,
AI as computational tool (verification scripts, blade searches, LaTeX typesetting,
iteration); methodology for prevention of fabricated content (assertions + targeted instructions).

Verification scripts: pruef_341_gf27_in_galg · vakuum_witt_z3 · primordnung ·
root7_gf9 · r26_rein_p27 · unipotent_jordan · inverse_minpoly (all 100%).

### Doc. 355 — SSB on T⁴/Z₃
Heptagonal phases k·360°/7 downgraded from [B] to [S] — characteristic 3 has no
angles, cos(2π/7) ∉ GF(3^k). Reference added to Doc. 341 §6.

### Doc. 361 — Kagome RVB polarons and Frobenius structure (DE+EN)
Case study on Pei et al. (PRL 137, 106702, 31 Aug. 2026, open access):
singly-doped Hubbard model on the Kagome lattice. Four structural parallels
with FFGFT (all [S]): Frobenius orbits, three-state Potts=GF(3),
mass=frozen kinetic energy, π-flux=winding number.
Verification script: pruef_361_kagome_frobenius.py — 20/20.

### Doc. 362 — BAW Ising machine as resonance computer (DE+EN, 9 pp. each)
Case study on Vadde et al. (Commun. Phys. 9:290, 8 Sept. 2026, CC-BY):
time-multiplexed Ising machine with 2048 spins on two BAW delay lines;
MAX-CUT, Number Partitioning, Sudoku. Five structural mappings [S]:
spin=phase 0/π, Barkhausen winding, Z₂ fixed points, pumping at 3ω→Z₃ machine.

### Doc. 363 — Hodge Theory on T⁴/Z₃ within FFGFT (DE 9 pp., EN 8 pp.)
**Main Theorem [B]:** All Hodge classes on T⁴/Z₃ are rational linear combinations
of algebraic cycles. Proof from five sub-theorems (A–E):
9 Z₃ fixed points as algebraic 0-cycles [B], Frobenius on GF(27)* [K],
sector pairing as Hodge symmetry [B], χ-classes as algebraic basis [B].
Clear boundary: the Millennium Problem for general varieties remains open.
Verification scripts: pruef_363_hodge_t4z3.py (23/23), pruef_363b_luecken.py (38/38).

---

## Corrections

- **R115:** Higher roots of unity (Doc. 341 §6), E₇ convention, heptagon [S] (Doc. 355)
- **Doc. 190:** R115 in changelog only (new documents require no corrections to existing ones)
- Hyperbit book ch07: `\cite{Hatcher/Bredon}` → book style [T1]/[T2]
- Hyperbit wrapper: duplicate `ch:` labels removed (0 warnings)

---

## Register
R115 added (higher roots of unity, Jordan decomposition, E₇ convention, Doc. 355 correction).
R100–R114 unchanged from v1.3.8.

---

## Bridges updated since v1.3.8

| Bridge | v1.3.8 | v1.3.9 |
|--------|--------|--------|
| GALG↔FFGFT algebraic correspondence | [B] partial | [B] extended: vacuum split, all roots of unity in G(6), Jordan decomposition |
| Heptagonal phases k·360°/7 | [B] | [S] — characteristic 3 has no angles |
| Hodge conjecture for T⁴/Z₃ | — | [B] proven from FFGFT structure |

## Remaining open bridges (unchanged from v1.3.8)

| Bridge | Status |
|--------|--------|
| CKM/PMNS angle values (numerical) | [S] (Doc. 348 Theorem D); GF(3⁶)=GF(729) candidate |
| HRV Galois test: positive result | [S] requires controlled breathing ≥13 min, n≥5 |
| Generation assignment (ordering) | [S] (Doc. 346) |
| m_Pl and α_em(M_Z) from ξ | [S] |
| Quark/hadron sector | open (Doc. 318, R76) |
| CMB peaks {1,6,14,26}; \|n\|²=30 | open (P29/P31) |
| Δm²₃₂ mixing term F₅–F₇ | [S] |
| Torus T⁴/Z₃ as GALG polynomial | open |

## Entry point for new readers
Doc. 205 "FFGFT in Simple Language" (DE+EN, 13–14 pages) remains the recommended
entry point. The SWT manuscript (`SWT_Galois_HRV_v2.docx`) is the recommended
entry point for the HRV application of FFGFT.

## What has not changed
ξ, T̃·m=1, and all algebraic results from v1.3.7/v1.3.8 are unchanged.
All derivation chains from v1.3.6 are unchanged.
