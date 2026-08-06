# Release Notes — v1.2.6 (July 2026)

**DOI:** [10.5281/zenodo.21496379](https://doi.org/10.5281/zenodo.21496379) (supersedes v1.2.5)

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

## What is new in v1.2.6

### Numbering correction
A duplicate numbering conflict was resolved: A270 remains the
Z₃-sector structure document (v1.1). The new Landauer document
is assigned **A271**.

### Landauer and the Phase-Space Accounting — A271 (new)

**A271** addresses a widespread misreading of Landauer 1961.
The standard reading — erasing a bit costs k_BT ln 2 because
information has energy — is not what Landauer wrote.

The key sentence appears in §1, before any entropy argument:

> *"a computer pushes information around in a manner that is
> independent of the exact data which are being handled, and is
> only a function of the physical circuit connections."*

And Landauer dismisses the naive energy argument himself:

> *"This argument does not make it clear that the signal energy
> must actually be dissipated."*

**Central consequence:** No energy can be assigned to an information
bit — not even to the physical bit. The formula gives the price of a
region reduction of a concrete hardware element under concrete
conditions (quasi-static, uniform distribution, two-state system with
specific switching kinetics). Which element, which kinetics, which
conditions — that is in the circuit connections, not in the bit.

**Document structure:**
- Misreading as question, Landauer's original text as answer
- Phase-space accounting: region reduction, Liouville, bath as volume receiver
- Dynamics as vehicle (coupling of information-bearing degrees of freedom to the bath)
- Many-into-one mapping (§4 direct quote)
- Realisation-dependence: single spin / DRAM capacitor / magnetic domain
- Qubit lower bound as open question [H]
- Three verbatim quotes from Landauer 1961 with section references

**Verification:** `a271_landauer.py` (Checks 1–10, all PASSED)  
**Layer status:** 15× [B] · 8× [K] · 3× [STIPULATION] · 1× [H]

---

## A-Series statistics (v1.2.6)

| | Count |
|---|---|
| Documents (De + En) | 45 × 2 = 90 |
| Verification scripts | 46 |
| Layer markers | [STIPULATION] / [K] / [B] / [S] / [H] |

