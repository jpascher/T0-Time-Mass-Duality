# Release Notes — v1.2.6 (Juli 2026)

**DOI:** [10.5281/zenodo.21496379](https://doi.org/10.5281/zenodo.21496379) (ersetzt v1.2.5)

Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_En.pdf](2/pdf/190_T0_Korrekturen_En.pdf)**  
Änderungsprotokoll: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**  
A-Serie-Protokoll: **[A_Serie_Export/A_SERIE_CHANGELOG.md](A_Serie_Export/A_SERIE_CHANGELOG.md)**

---

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows:
all Standard Model constants follow from a single dimensionless
parameter **ξ = 4/30000** on a compact 4D torus T⁴. The foundational
relation is **T̃ · m = 1** — intrinsic time and mass are inversely
coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Neu in v1.2.6

### Nummerierungskorrektur
Ein Nummerierungskonflikt wurde behoben: A270 bleibt das Z₃-Sektor-Dokument (v1.1). Das neue Landauer-Dokument erhält die Nummer **A271**.

### Landauer und die Phasenraum-Buchhaltung — A271 (neu)

**A271** behandelt eine weit verbreitete Fehlinterpretation von Landauer 1961.
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

## A-Serie-Statistik (v1.2.6)

| | Count |
|---|---|
| Dokumente (De + En) | 45 × 2 = 90 |
| Prüfskripte | 46 |
| Layer markers | [STIPULATION] / [K] / [B] / [S] / [H] |

