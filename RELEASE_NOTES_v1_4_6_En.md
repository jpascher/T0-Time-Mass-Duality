# Release Notes — v1.4.6 (10 October 2026)

**DOI:** assigned on Zenodo publication — supersedes v1.4.5
Running corrections: **[2/pdf/190_T0_Korrekturen_En.pdf](2/pdf/190_T0_Korrekturen_En.pdf)**
Changelog (German): **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**
Summary of the corpus: **[2/pdf/384_FFGFT_Kurzfassung_En.pdf](2/pdf/384_FFGFT_Kurzfassung_En.pdf)** (also as [HTML](2/html/384_FFGFT_Kurzfassung_En.html))

**FFGFT — Fundamental Fractal-Geometric Field Theory** is first of all a ratio-based
theory. In natural units (Heaviside-Lorentz, ħ = c = ε₀ = 1) with α = 1 there is a
single dimensionless parameter **ξ = 4/30000** on a compact 4D torus T⁴/ℤ₃; the
foundational relation is **T̃·m = 1** — intrinsic time and mass are inversely coupled.
Only the translation into SI needs a measured value as anchor.

**Author:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Overview

v1.4.6 archives the analysis behind the revision of the article "Galois-Informed HRV
Preprocessing" (Smart Wearable Technology, submission #12080). The revised manuscript
cites this release as the citable source of its scripts and results. The theory itself
is unchanged; ξ and T̃·m = 1 are untouched, and no corpus document is added.

---

## Revision scripts for the SWT article

The new folder `2/python/Dok360_Skripte/SWT_Revision/` contains the check script
`pruef_swt_revision.py`, which recomputes every number used in the revised manuscript
from the raw data in `2/python/Dok360_Skripte/` (24/24 assertions), the figure script
`swt_revision_figures.py`, the result file `pruef_swt_revision_ergebnis.json`, the three
figures and a README. The scripts need numpy, scipy and neurokit2 and are run from this
folder.

The check covers the null model for grid proximity (how often an arbitrary value lies
close to a grid element by chance), the unit dependence of the HRV band limits, the
corrected resolution condition Δf/f ≤ 100ξ with the resulting minimum window length,
the re-analysis of the Polar H10 recordings, the test–retest and sliding-window
variability of LF/HF, and the sample size of the prospective test proposed in the
article.

## Re-analysis of the Polar H10 recordings

The R-peak detector in `polar_h10_atemfrequenz_scan.py` missed 35–47 % of the beats in
every paced-breathing recording of 10 September 2026. Because the remaining RR
intervals were then joined end to end, the time axis shrank to 49–61 % of the true
recording time, and all spectral frequencies were shifted upwards by a factor of
1.6–2.0. With a validated detector (NeuroKit2) and the true time axis, the dominant
spectral peak at 4, 5 and 6 breaths/min lies within one frequency bin of the metronome
frequency, and the HF peak is its second harmonic. The Galois grid hits reported
earlier (88/35, 39/35) no longer stand; LF/HF values close to grid elements occur only
as often as the null model predicts for chance. In the spontaneous recording a single
missed beat had raised RMSSD from 19.0 ms to 36.3 ms. The files
`PolarH10_4min_A1_ECG.jsonl` and `PolarH10_4min_A2_ECG.jsonl` are byte-identical, so
there is only one recording at 4 breaths/min.

The original script and the result files of September are kept unchanged for
traceability; their Polar figures are superseded by the values in
`SWT_Revision/pruef_swt_revision_ergebnis.json`. The Polar results in Doc. 360 are
affected in the same way and will be corrected in the document and booked in Doc. 190.

## What has not changed

ξ and T̃·m = 1 are unchanged. All results of v1.4.5 continue to hold; the re-analysis
concerns only the measured HRV data of Doc. 360, not the theory.
