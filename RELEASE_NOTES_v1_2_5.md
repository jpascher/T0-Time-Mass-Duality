# Release Notes — v1.2.5 (July 2026)

**DOI:** [10.5281/zenodo.XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX) (supersedes v1.2.4 · [10.5281/zenodo.21496379](https://doi.org/10.5281/zenodo.21496379))
<!-- Replace XXXXXXXX with the new version DOI before publication -->

Running corrections: `2/pdf/190_T0_Korrekturen_De.pdf`  
Changelog: `000_FFGFT_Changelog_De.md`  
A-Series log: `A_Serie_Export/A_SERIE_CHANGELOG.md`

---

**FFGFT — Fundamental Fractal-Geometric Field Theory** shows:
all Standard Model constants follow from a single dimensionless
parameter **ξ = 4/30000** on a compact 4D torus T⁴. The foundational
relation is **T̃ · m = 1** — intrinsic time and mass are inversely
coupled.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## What is new in v1.2.5

v1.2.5 is a correction and precision release. It contains no new
theoretical results. Its content is the incorporation of two external
corrections (S. Vossen, 2026-07-23) into the A-Series, and the
withdrawal of one legacy-corpus parameter following a consistency
check against the canonical A-Series (R61). Both are the A-Series
supersession mechanism in operation: corrections are named, booked,
and remain traceable — they do not disappear.

### A-Series v1.1 — external corrections incorporated (CL-01 to CL-03)

Both points were raised by S. Vossen as feedback on the A-Series and
were accepted as corrections — not as suggestions.

**CL-01 — Verifiability claim made precise.** The shorthand
"Everything is verifiable" claimed more than the verification scripts
deliver: scripts verify computability — not the stipulations, not the
physical reading of a bridge, not empirical adequacy. The series' claim
now reads:

> Every computable claim is independently executable and checkable,
> and every substantive statement carries an explicit declared
> epistemic status. *(Wording due to Stefaan Vossen, 2026)*

**CL-02 — [K] and [B] are not external certifications.** Added to
A010 §6 (De + En), booked as [STIPULATION]: the markers [K] and [B]
are internal claim-state markers. [K] states that a claim follows
within the declared core; [B] states that a bridge is algebraically
established under its stated conditions. Neither marker by itself
establishes empirical truth, external physical validity, or a unique
ontology.

**CL-03 — DOI alignment.** A_SERIE_README.md (header and citation
recommendation) carried the v1.1.0 legacy DOI (20117635) instead of
the canonical record (21496379); the Zenodo description still listed
the DOI as pending. Both corrected. For a series whose subject is
documentary succession, this was not a small blemish.

### R61 — second parameter ξ_Higgs withdrawn (Docs 174/175)

Docs 174/175 introduced a second parameter,
ξ_Higgs = λ_h²v²/(16π³m_h²) ≈ 1.038 × 10⁻⁵, and based on it a
decoherence-rate scaling together with a T₂-ratio finding. The
consistency check against the canonical A-Series showed: **the same
expression is the Higgs matching of ξ itself.** With standard inputs
(v = 246.22 GeV, m_h = 125.25 GeV) it evaluates to
1.304 × 10⁻⁴ ≈ ξ = 4/30000 (deviation 2.2 %; cf. R59 on scheme
dependence) — booked canonically in A142 [K]. The value 1.038 × 10⁻⁵
follows from no input convention declared anywhere in the corpus and
does not appear in the A-Series.

Consequence: the T₂ finding of Doc 174 loses its numerical basis (with
the single ξ, the measured window of 9–11 decades matches no integer
stage count) and was moreover formed after the data were known,
unbooked under P35 in any case — it is thus doubly void. Unaffected:
the stage-coupling law C ∝ ξ^|ΔN| with the single fundamental
parameter (R57). Authoritative form for future use: Γ ∝ ξ^(2ΔN)·ω —
declared and sealed in the SDCR Stage-2 pre-registration note v1.1
(SHA-256 c47d73ce…3992, 23 July 2026), before any stage-2 data exist.
Entered as **R61** in Doc 190; source documents are not revised
(append-only). Check script: `python/Dok190_Skripte/r61_xi_higgs_matching.py`.

---

## Changes to the file tree

| File | Change |
|------|--------|
| A_Serie_Export/Sources/ch/A010_Zweck_Aufbau_De_ch.tex | CL-02: [SETZUNG] paragraph on [K]/[B] |
| A_Serie_Export/Sources/ch/A010_Zweck_Aufbau_En_ch.tex | CL-02: [STIPULATION] paragraph on [K]/[B] |
| A_Serie_Export/pdf/A010_Zweck_Aufbau_{De,En}.pdf | rebuilt |
| A_Serie_Export/A_SERIE_README.md | CL-01, CL-03; version 1.1 |
| A_Serie_Export/A_SERIE_CHANGELOG.md | v1.1 section (append-only) |
| 2/pdf/190_T0_Korrekturen_{De,En}.pdf | R61 |
| python/Dok190_Skripte/r61_xi_higgs_matching.py | new (check script R61) |

All other documents, scripts, and results are unchanged from v1.2.4.

---

## Correction register entries (this release)

| Entry | Concerns | Description |
|-------|----------|-------------|
| R61 | Docs 174/175 (cf. A142, 147, 162; R57, P35) | Second parameter ξ_Higgs withdrawn — the same expression is the Higgs matching of ξ itself (A142 [K]); T₂ finding doubly void (basis + P35); authoritative: Γ ∝ ξ^(2ΔN)·ω |

---

## Version history

| Version | DOI | Focus |
|---------|-----|-------|
| v1.2.5 | [XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX) | **Correction release:** A-Series v1.1 (CL-01–03, Vossen corrections); R61 (ξ_Higgs withdrawn) |
| v1.2.4 | [21496379](https://doi.org/10.5281/zenodo.21496379) | **A-Series:** 43 canonical documents; A095 (g_R=0 [B]); A192 (U(1), SU(3) [B]); A060 R50; CHSH ξ/(2π) [B] |
| v1.2.3 | [21396624](https://doi.org/10.5281/zenodo.21396624) | Information question (Docs 301/302); native T·E=1 (Doc 306, R50–R53); time in state space (Doc 307) |
| v1.2.2 | [21266963](https://doi.org/10.5281/zenodo.21266963) | SM as decompactified projection (Doc 298); K_frak = 74/75 (Doc 300) |
| v1.2.1 | [21203746](https://doi.org/10.5281/zenodo.21203746) | Time winding as Hilbert-space memory kernel (Docs 283/295/296/297) |
| v1.1.9 | [21193007](https://doi.org/10.5281/zenodo.21193007) | θ=2/9 as C₃-in-A₅ geometry invariant (Docs 293/294/295) |
| v1.1.7 | [21158441](https://doi.org/10.5281/zenodo.21158441) | Lepton-sector audit; α two-way overdetermination (Docs 291/292) |
| v1.1.0 | [20117635](https://doi.org/10.5281/zenodo.20117635) | Hilbert-space bijection (Docs 230/231/232) |

---

## Note on the frozen corpus

This version is designated as the frozen source corpus for an external
methodological study (AI-assisted scientific synthesis, S. Vossen).
Authoritative are the version DOI of this release and the SHA-256 hash
of the release archive; both will be recorded in the accompanying
correspondence after publication. The frozen corpus explicitly
includes the correction register and the changelogs.

---

*Responsibility for content and errors rests entirely with the author.*  
*These release notes were prepared using AI-assisted tools.*
