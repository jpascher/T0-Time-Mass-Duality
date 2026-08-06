# Release Notes — v1.2.5 (July 2026)

**DOI:** *(to be assigned on Zenodo upload)* (supersedes v1.2.4 · [10.5281/zenodo.21496379](https://doi.org/10.5281/zenodo.21496379))

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

## What is new in v1.2.5

v1.2.5 extends Block 3 of the A-Series by the **thermodynamics of
computation**: A271 revised, A272 and A273 new. All three documents
declare explicitly **contact with FFGFT: none** — they argue at the
level of statistical mechanics; the ξ scheme is untouched (its own
level, its own accounting, analogous to P20/P39). A new layer marker
for external evidence is added.

### The bound attaches to the region, not to the description — A271 (revised)

Landauer's principle is developed as a statement about **regions in
phase space**, not about information. The chain is short: region
reduction shrinks the volume; Liouville forbids volume shrinkage in a
closed system; hence a bath must absorb the volume, and the price is
heat Q ≥ k_B·T·ln(W_before/W_after) — the ln2 is the binary special
case, not the physics. Counting proceeds by **distinguishability**
(orthogonality), not by energy; the absolute base discretisation is
supplied by h^f.

**Content neutrality** follows immediately: thermodynamics counts
regions and does not read them. A processor computing 2+2=4 and one
computing 2+2=5 switch the same regions and pay the same bill to the
bath. There is no thermodynamic detector of truth.

Made precise relative to the earlier edition: what is sufficient for
heat production is the **non-bijectivity of the region map** — not
logical irreversibility. The latter coincides with the region map only
under a realisation assumption that has to be declared explicitly
(disjoint regions, no region carried along); without it, it carries
nothing, because Bennett executes any logically irreversible function
as a sequence of volume-preserving maps.

Three levels are kept strictly apart — construction (engineer), state
transition (clock), description (program). From this it follows that a
real computer does not erase bits discretely but carries a continuous
entropy current (DRAM refresh, qubit decoherence): the computer pays
entropy for existing, not only for computing.

The epistemic caveat is booked explicitly: not measurable does not mean
not present. Landauer holds because of the mechanics (Liouville), not
because of ignorance; the irreversibility is statistical, not
ontologically absolute (Maxwell's demon, Bennett's resolution).

Check script `a271_landauer.py` (checks 1–10).

### Carrier and information — A272 (new)

Textual criticism accompanying A271. What Landauer's 1961 paper proves
is a lower bound on **carrier operations** over a thermal equilibrium
ensemble — not a universal statement about abstract information. Two
propositions carry this:

- **Proposition 1** (multiple realisability): no energy can be assigned
  to a bit of information, only to its carrier. The same information
  content can be realised by 5 V, by 1 V, by a spin or by a photon; the
  energy varies, the content does not.
- **Proposition 2**: a purely interpretive erasure does not shrink the
  carrier state space — and therefore costs nothing.

Framed explicitly as a **finding about jurisdiction**, not as a
refutation: for the physical operation Landauer considers, his result
is correct. What is contested is the jurisdiction of that result over a
subject matter about which it makes no statement.

In addition: Landauer's **own ensemble restriction** from the original
paper is documented, and the reception history of the generalisation is
traced (Lairez, Norton, Earman/Norton, Hemmo/Shenker); a critique of
the language of digital technology (table: carrier versus information);
hypostatisation as an interpretive frame [S]. Feedback bound
Q_min = kT(ln2 − I) with I dimensionless in nats; the knowledge I is
itself carrier-bound, so the price is displaced, not avoided.

Contains the binding **dictionary A271 ↔ A272** (region = carrier,
description = information), so that the corpus does not end up carrying
two parallel terminologies for one matter.

### The reckoning bead — A273 (new)

Token computation (abacus, shells, coins) as the limiting case in which
Landauer's argument comes apart into its **two independent halves**.

The **accounting** holds there exactly and is for once visible: the
stock from which the tokens come and into which they flow back is a
bath one can point at; tokens are conserved (Liouville analogue,
countable); ΔS/k_B = N·ln2 carrier-independent.

The **thermal conversion** ΔS → Q = T·ΔS does not hold there: an abacus
bead costs about 5.1×10¹⁵ times the Landauer bound to move, its
positional bit carries 3.8×10⁻²³ of its own thermal entropy, and its
positional barrier stands at 3.6×10¹⁵ k_B·T. The token computer
therefore falls squarely under the very restriction Landauer stated
himself.

From this follows an ordering that runs against intuition:
**visibility of the structure and binding force of the number run in
opposite directions.** The cruder the carrier, the clearer the
accounting and the more irrelevant the bound.

Two floors are separated: the thermal k_B·T and the quantum-geometric
ħc/L; the larger of the two governs. For massive mechanical carriers,
ħ²/(2mL²) is the relevant quantum scale and is irrelevant (bead
2.7×10⁻⁴¹ k_B·T, colloid 1.6×10⁻²² k_B·T); at 300 K the two floors
cross at 7.6 µm; for the qubit the quantum-geometric floor leads
(hf/k_B·T = 24 at 5 GHz and 10 mK). The passage back is continuous and
computable: critical token mass k_B·T/(μ·g·d) = 1.4×10⁻¹⁹ kg.

In addition, the **token stock as a cost category of its own**: a
material bound with no lower limit in k_B·T, a standing inventory
rather than a running current. With semiconductors it drops out of
view, because the stock is cast in silicon [S].

Check script `a273_rechenkugel.py` (checks 1–14, all PASSED).

### New layer marker [Q]

Elsewhere the A-Series argues throughout from within ξ and therefore
needed no category for external evidence. A271–A273 are the first
documents citing outside literature and measured values. Hence:

| Marker | Meaning |
|--------|---------|
| **[Q]** | Source — external primary source or measured value |

**[K]** (core — derived from ξ, numerically verified) keeps its
corpus-wide meaning and does not occur in A271–A273.

---

## The A-Series at a glance

| Block | Documents | Topic |
|-------|-----------|-------|
| 0 | A010–A095 (13) | Foundation: stipulations, geometry, units, time |
| 1 | A100–A192 (16) | Sectors: leptons, constants, gravitation, QM, SM |
| 2 | A200–A250 (6) | Method: layers, falsifiability, open points |
| 3 | A260–A273 (12) | Extensions: Casimir, scale hierarchy, Dirac, Z₃ sector, thermodynamics of computation |

47 documents × 2 languages = 94 sources + 94 PDFs + 47 verification
scripts. All files in **[A_Serie_Export/](A_Serie_Export/)**.

---

## Correction register entries (this release)

None. The changes concern A-Series documents without ξ contact; the
correction register (Doc. 190) remains at R60.

---

## Version History

| Version | DOI | Focus |
|---------|-----|-------|
| v1.2.5 | *(on upload)* | **Thermodynamics of computation:** A271 (bound attaches to the region, not the description); A272 (carrier versus information); A273 (token computation as the limiting case); new marker [Q] |
| v1.2.4 | [21496379](https://doi.org/10.5281/zenodo.21496379) | **A-Series:** 43 canonical documents; A095 (g_R=0 [B]); A192 (U(1), SU(3) [B]); A060 R50; CHSH ξ/(2π) [B] |
| v1.2.3 | [21396624](https://doi.org/10.5281/zenodo.21396624) | Information question (Dok. 301/302); native T·E=1 (Dok. 306, R50–R53); time in state space (Dok. 307) |
| v1.2.2 | [21266963](https://doi.org/10.5281/zenodo.21266963) | SM as decompactified projection (Dok. 298); K_frak = 74/75 (Dok. 300) |
| v1.2.1 | [21203746](https://doi.org/10.5281/zenodo.21203746) | Time-winding as Hilbert-space memory kernel (Dok. 283/295/296/297) |
| v1.1.9 | [21193007](https://doi.org/10.5281/zenodo.21193007) | θ=2/9 as C₃-in-A₅ geometric invariant (Dok. 293/294/295) |
| v1.1.7 | [21158441](https://doi.org/10.5281/zenodo.21158441) | Lepton sector audit; α two-route overdetermination (Dok. 291/292) |
| v1.1.0 | [20117635](https://doi.org/10.5281/zenodo.20117635) | Hilbert-space bijection (Dok. 230/231/232) |

---

*Responsibility for content and errors rests entirely with the author.*
