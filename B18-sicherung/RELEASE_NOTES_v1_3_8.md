# Release Notes — v1.3.8 (10 September 2026)

**DOI:** to be assigned on Zenodo publication — supersedes v1.3.7
Running corrections: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Change log: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows: all Standard Model
constants follow from a single dimensionless parameter **ξ = 4/30000** on a compact
4D torus T⁴. The foundational relation is **T̃ · m = 1** — intrinsic time and mass
are inversely coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

This release extends Doc. 360 with a complete respiratory frequency scan using
a Polar H10 chest strap (7 recordings, 5–6 min each, controlled breathing at
2, 4, 5, and 6 breaths/min), a corrected RMSSD analysis with mandatory artefact
filtering, and a first complete journal manuscript draft (Smart Wearable Technology,
SWT). No algebraic results in Docs. 342–360 are changed.

---

## Extensions to Doc. 360 since v1.3.7

### Polar H10 self-test — spontaneous breathing baseline
Recording: `PolarRecording_20260910_125832`, 21.9 min supine, spontaneous breathing,
130 Hz ECG + HR JSONL export. Results: HF 69.2 bpm, RMSSD 33.6 ms (HR-derived),
LF-peak 0.073 Hz, LF/HF → 56/45 (distance 0.14%, k=6). Confirms Fantasia
finding: LF-peak CV >> 1.33% at spontaneous breathing.

### Polar H10 respiratory frequency scan
Seven seated recordings with metronome-controlled breathing
(click = change: inhale OR exhale):

| Condition | Metronome | Breaths/min | LF Hz | RMSSD ms | Artefacts | LF/HF | Galois p/q | k |
|---|---|---|---|---|---|---|---|---|
| 4/min | 8 bpm | 4.0 | 0.105 | 33.6 | 0 | 4.43 | — | — |
| 6/min | 12 bpm | 6.0 | 0.040 | 36.1 | 0 | 1.12 | 39/35 | 6 |
| 5/min rec.1 | 10 bpm | 5.1 | 0.144 | 29.5 | 2 | 4.05 | — | — |
| **5/min rec.2** | **10 bpm** | **5.0** | **0.132** | **39.9** | **0** | **2.51** | **88/35** | **6** |
| 2/min rec.1 | 4 bpm | 2.0 | 0.071 | 27.7 | 2 | 7.94 | 4 | 1 |
| 2/min rec.2 | 4 bpm | 2.0 | 0.075 | 30.5 | 0 | 9.31 | 4 | 1 |

All raw JSONL files (ECG + ACC) included in repository under
`2/python/Dok360_Skripte/PolarH10_*.jsonl`.
Analysis script: `polar_h10_atemfrequenz_scan.py` — reproduces table above
from raw files with a single command.

### Artefact correction — methodological finding

An apparent RMSSD maximum at 5/min rec.1 (67.2 ms raw) was traced to
2 missed R-peaks (|ΔRR|_max = 662 ms) caused by ECG amplitude modulation
at slow breathing rates. After Median ±30% artefact filtering: RMSSD
29.5 ms — no resonance effect. This correction is documented as a
**methodological finding** (M1) in Doc. 360 and in the SWT manuscript.

Three methodological findings are now documented in Doc. 360:
- **M1:** Artefact filtering (Median ±30%) is mandatory at ≤4 breaths/min.
- **M2:** Subharmonic detection at ≤2 breaths/min — verify via full amplitude spectrum.
- **M3:** Spontaneous breathing makes the Galois test structurally inapplicable.

### Findings summary (Doc. 360, final)

1. **No RMSSD resonance effect** after artefact correction (27–40 ms at all conditions).
2. **LF-peak tracks respiratory rate** (0.040–0.144 Hz across conditions) — no stable resting position, no LF = respiratory rate coincidence.
3. **Galois grid hit at 5/min rec.2** (88/35, 0.02%) and **6/min** (39/35, 0.06%), both k=6.
4. **Three negative validations** (BIDMC-01, Fantasia, Polar H10 spontaneous) confirm structural finding [B].

---

## SWT journal manuscript (new)

First complete draft of:
**"Galois-Informed HRV Preprocessing: Algebraic Constraints for Wearable
Frequency Analysis"**
Target journal: *Smart Wearable Technology* (SWT, Bon View Publishing,
APC-free until 31 December 2026, acceptance rate 31%).

Files:
- `SWT_Galois_HRV_v2.docx` — manuscript (~4,660 words, 10 pages, Times New Roman 12pt A4)
- `SWT_CoverLetter.docx` — cover letter

Key contributions in manuscript beyond Doc. 360:
- **§4.5 Fundamental limits of the Galois test:** three limits formally defined —
  ECG amplitude modulation boundary (≤4 breaths/min), resolution floor as system
  boundary (1.33%, not measurement precision), spontaneous breathing as
  epistemological boundary (with reference to Eckberg 1997, Karemaker 2017).
- **§4.6 Prior knowledge and algebraic constraints in spectral estimation:**
  Galois admissibility as algebraically necessary prior (harder than Bayesian);
  lattice-constrained periodogram as future implementation target;
  connection to AR, MUSIC, ESPRIT, harmonic spectral analysis.
- **Data availability statement**, funding statement, conflict of interest
  declaration, AI assistance declaration (COPE-compliant), author biography.

Status: ready for submission pending Zenodo DOI for v1.3.7.

---

## Register
R106–R119 unchanged from v1.3.7. No new register entries.

---

## Bridges updated since v1.3.7

| Bridge | v1.3.7 | v1.3.8 |
|--------|--------|--------|
| Galois-informed HRV: resonance frequency protocol | [S] pending | [S] tested (n=1, negative); applicability envelope defined |
| SWT manuscript | — | first complete draft ready |

## Remaining open bridges (unchanged from v1.3.7)

| Bridge | Status |
|--------|--------|
| CKM/PMNS angle values (numerical) | [S] (Doc. 348 Theorem D); GF(3⁶)=GF(729) candidate |
| HRV Galois test: positive result | [S] requires controlled breathing ≥13 min, n≥5 |
| Generation assignment (ordering) | [S] (Doc. 346) |
| m_Pl and α_em(M_Z) from ξ | [S] |
| Quark/hadron sector | open (Doc. 318, R76) |
| CMB peaks {1,6,14,26}; \|n\|²=30 | open (P29/P31) |
| Δm²₃₂ mixing term F₅–F₇ | [S] |

## Entry point for new readers
Doc. 205 "FFGFT in Simple Language" (DE+EN, 13–14 pages) remains the recommended
entry point. The SWT manuscript (`SWT_Galois_HRV_v2.docx`) is the recommended
entry point for the HRV application of FFGFT.

## What has not changed
ξ, T̃·m=1, and all algebraic results from v1.3.7 are unchanged.
All derivation chains from v1.3.6 are unchanged.
