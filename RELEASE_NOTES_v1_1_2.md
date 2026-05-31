# Release Notes — v1.1.2 (May 2026)

> **Focus:** Complete re-edition of the Kindle book series as a
> five-volume collection in three KDP formats — extension to include
> all documents added since v1.1.0.

**DOI:** assigned upon Zenodo upload (placeholder in README)

---

## What changes from v1.1.1

v1.1.1 added 11 new documents to the corpus (Docs. 240, 245–254).
These had *not* yet been incorporated into the three Kindle volumes
that existed at that time. v1.1.2 closes this gap:

- The three existing volumes (Foundations, Lagrangian/QFT,
  Cosmology/Consciousness) are **rebuilt with all corrections since
  February 2026** (HW147 correction in Doc. 147 §8, follow-up
  document updates Doc. 022/035/148/202, Doc. 230 extended).
- **Two new volumes (Vol. 4 and Vol. 5)** extend the collection by
  74 additional documents added or refined since the original
  three-volume conception — including the entire Hilbert-space
  bijection (Doc. 230–232), the falsification trilogy (Doc. 220–222),
  the FFGFT-vs.-RA/RSG comparisons (Doc. 245–247), the black-hole
  information document (Doc. 250), the dual ordering principles
  (Doc. 254), and the epistemic self-positioning (Doc. 262).
- Each of the five volumes is delivered in **three KDP formats**:
  eBook 6×9 inch (Kindle), Paperback 8.5×11 inch, and Hardcover
  8.25×11 inch — in both German and English.
- **30 PDFs** in total: 5 volumes × 2 languages × 3 formats.

---

## The five volumes

| Volume | Content | Docs | eBook DE | Paperback DE | Hardcover DE |
|--------|---------|------|----------|--------------|--------------|
| Teil 1 | Foundations, ξ parameter, constants, units | 40 | 533 | 452 | 459 |
| Teil 2 | Lagrangian formalism, QFT, QM tests, photonics | 36 | 505 | 423 | 427 |
| Teil 3 | Cosmology, CMB, consciousness, FFGFT narrative | 35 | 487 | 412 | 415 |
| Teil 4 | Early extensions (up to Doc. 184 p-bit) | 37 | 473 | 407 | 414 |
| Teil 5 | Layers, Hilbert-space bridge, recent clarifications | 37 | 506 | 436 | 438 |

English versions correspondingly slightly shorter (1-2 pages less per
chapter).

**All volumes within limits:**
- eBook ≤ 550 pages (Kindle eBook limit)
- Paperback ≤ 828 pages (KDP Paperback 8.5×11 limit)
- Hardcover ≤ 550 pages (KDP Hardcover 8.25×11 limit)

---

## Vol. 4 / Vol. 5 split

Boundary at **Doc. 184 → Doc. 185**. Thematically clean:

- Up to Doc. 184 (p-bit): theory developed on Layer 1 (compact T⁴,
  correction-free description in natural units).
- From Doc. 185 (Embedding Cost): the Layer-1/Layer-2 language is used
  as an explicit descriptive grid and carried through to the epistemic
  self-positioning of Doc. 262.

---

## Three KDP formats

Both print formats (Paperback and Hardcover) use identical geometry
parameters, only the paper width differs:

```latex
\documentclass[11pt,openright,twoside]{book}
\usepackage[
  paperwidth=8.50in,   % or 8.25in for Hardcover
  paperheight=11.0in,
  top=1.0in,
  bottom=1.2in,
  inner=0.75in,
  outer=1.25in,
  bindingoffset=5mm,
  twoside
]{geometry}
```

The eBook uses symmetric margins (oneside, 0.5 in each) for digital
display.

---

## Technical improvements

### Table wrap for Kindle 6×9

650 tables in 206 ch files were automatically wrapped in
`\adjustbox{max width=\textwidth}{...}`. `max width` only scales DOWN
when the table is too wide; smaller tables keep their natural size.
Effect in Kindle 6×9 format:

- Teil 1 DE: 185 → 43 Overfull-hboxes (−77%)
- Teil 5 DE: 363 → 22 Overfull-hboxes (−94%)
- Teil 1 EN: 201 → 1 LaTeX errors (cascading table errors in Doc. 086
  documentation overview resolved)

In the print formats, the text area is wider, so most tables don't
need scaling anyway. The same ch file works for all three formats
without separate maintenance.

### `T0_preamble_patches.tex` patches file

Adds missing environments and color names used in individual ch files
but not defined in `T0_preamble_De.tex` / `T0_preamble_En.tex`:

- Environments: `avipost`, `response` (Doc. 172 Avi dialogue);
  `geminibox`, `userbox`, `videobox` (Doc. 191 Gemini dialogue);
  `infobox`, `keybox`, `predbox`, `warnbox` (Doc. 187, 188, 189).
- Color aliases: `T0red`, `T0gray`, `T0blue`, `T0green`, `T0orange`,
  `T0purple`, `T0yellow` (uppercase variants of the lowercase
  versions already defined).

Loads after the main preamble; doesn't change existing definitions.

### Teil2-end typo correction

The old wrappers contained a typo in `pri-end/Teil2-end_De.tex` and
`_En.tex`: `\input{../ch/023a_Bell-video_De_ch}` (file doesn't exist) —
corrected to `023b_Bell-video_De_ch`. Without this fix, Volume 2 could
never have built in this form.

### New introductions for Vol. 4 and Vol. 5

`000_Einleitung_Teil4_{De,En}_ch.tex` and `000_Einleitung_Teil5_{De,En}_ch.tex`
with explicit description of the Vol.-4/Vol.-5 split and the Layer-1/2
vocabulary transition.

---

## What is new in content

**Added to corpus since v1.1.0** (now first time consolidated into
Vols. 4+5):

- **Hilbert-space bridge** (Doc. 230–232): concrete bijection FFGFT
  ↔ standard QM on the qubit sector; ΔCHSH ~ 10⁻⁵ testable.
- **Falsification trilogy** (Doc. 220–222): Casimir, redshift,
  lithium — three explicit falsification criteria.
- **Layers and scale ladder** (Doc. 241–253): systematic working-through
  of Layer 1 (static, compact) vs. Layer 2 (dynamic, SI-projected).
- **IPI bridges** (Doc. 245–247): FFGFT vs. RA 2.1 (Guevara),
  FFGFT vs. RSG (Austin), category-error revised.
- **Black-hole information** (Doc. 250): Hawking paradox via the
  ontology/epistemology distinction; lattice dispersion correction
  ΔE/E = −(E/E_max)²/24.
- **Dual ordering principles** (Doc. 254): resonance and entropy
  causally connected; Vopson's second infodynamics law reproduced
  geometrically.
- **Acceptance without visualisation** (Doc. 262): epistemic
  self-positioning; "three borrowed apples" as a model for T̃·m=1;
  Layer-1/2 language completed.
- Plus the HW147 correction in Doc. 147 §8 (real IBM measurement
  S = 2.74; "40×" claim refuted) with follow-up corrections in
  Doc. 022, 035, 148, 202.

---

## Build environment

- **LuaLaTeX** (TeX Live 2023+)
- **Inter** (Variable Font, main typeface)
- **JetBrains Mono** (code listings)
- **Libertinus Math** (mathematical notation)
- **babel-ngerman** for German hyphenation
- **adjustbox**, **tcolorbox**, **microtype**, **fontspec**

---

## Repository changes

### New files

```
2/tex-n/wr/
├── Teil1_ebook_De.tex                  (NEW with patch line)
├── Teil1_paperback_De.tex              (NEW)
├── Teil1_hardcover_De.tex              (NEW)
├── … analogous for Teil 2, 3, 4, 5 in DE and EN  (30 wrappers total)

2/tex-n/pri-end/
├── Teil2-end_De.tex                    (typo fix)
├── Teil2-end_En.tex                    (typo fix)
├── Teil4-end_De.tex                    (NEW)
├── Teil4-end_En.tex                    (NEW)
├── Teil5-end_De.tex                    (NEW)
├── Teil5-end_En.tex                    (NEW)
└── T0_preamble_patches.tex             (NEW)

2/fixed/ch/
├── 000_Einleitung_Teil4_De_ch.tex      (NEW)
├── 000_Einleitung_Teil4_En_ch.tex      (NEW)
├── 000_Einleitung_Teil5_De_ch.tex      (NEW)
├── 000_Einleitung_Teil5_En_ch.tex      (NEW)
└── (206 further ch files with \adjustbox wrappers around tables)

scripts/
└── wrap_tables_for_kindle.py           (NEW)

books/                                  (NEW — all print PDFs)
├── eBook_6x9/Deutsch/Teil1-5_ebook_De.pdf
├── eBook_6x9/English/Teil1-5_ebook_En.pdf
├── Paperback_8.5x11/Deutsch/Teil1-5_paperback_De.pdf
├── Paperback_8.5x11/English/Teil1-5_paperback_En.pdf
├── Hardcover_8.25x11/Deutsch/Teil1-5_hardcover_De.pdf
└── Hardcover_8.25x11/English/Teil1-5_hardcover_En.pdf
```

### DOI note

The books themselves reference earlier Zenodo DOIs in several places
(16142455, 17390358, 18834145, 20041529, 20117635). These references
are version-specific — references to "the current publication" will
be updated to the new DOI with the v1.1.2 release. References to
historical versions remain unchanged.

(The DOI update in the ch files happens after the Zenodo upload.)
