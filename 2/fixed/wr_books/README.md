# FFGFT v1.1.2 — Komplett-Auslieferung (Mai 2026, Update Juni 2026)

**DOI:** [10.5281/zenodo.20474821](https://doi.org/10.5281/zenodo.20474821)

Diese Auslieferung enthält den vollständigen Stand des FFGFT-Korpus
nach Release v1.1.2:

- **30 Bücher** (5 Bände × 2 Sprachen × 3 KDP-Formate) — derzeit auf
  Amazon KDP im Genehmigungsverfahren.
- **368 Einzeldokumente** als A4-PDFs (184 DE + 184 EN) für
  wissenschaftliche Nutzung, Referenz, Druck auf A4-Papier.
- **Vollständige LaTeX-Sourcen** für alle Wrapper, Präambeln und
  modifizierten ch-Dateien.

## Was sich in diesem Update geändert hat (Juni 2026)

Frühere A4-Build (Mai 2026) hatte zwei Mängel — beide jetzt behoben:

1. **Überschriften und Titel fehlten in den A4-PDFs.** Die ursprünglichen
   Wrapper-Dateien enthielten `\title{...}` mit dem konkreten
   Dokumenttitel, `\maketitle` und `\tableofcontents`. Bei der ersten
   A4-Konvertierung wurden diese Wrapper verloren — die jetzigen
   Wrapper sind die Originalwrapper, nur mit angepasster A4-Präambel.
2. **Dateinamen hatten unnötiges `_A4_`-Suffix.** Jetzt: Dateinamen
   wie `001a_T0_Book_Abstract_De.pdf`, ohne `_A4_`. Die Unterscheidung
   zur Buch-Sammlung erfolgt **nur über das Verzeichnis**
   (`Einzeldokumente_A4/Deutsch/` vs. `Buecher/PDFs/`).

## Struktur

```
FFGFT_v1_1_2_Komplett/
├── README.md                         (diese Datei)
├── Buecher/
│   └── PDFs/
│       ├── eBook_6x9/                Kindle eBook 6×9 Zoll
│       │   ├── Deutsch/              5 Bände
│       │   └── English/              5 Bände
│       ├── Paperback_8.5x11/         KDP Print Paperback 8.5×11 Zoll
│       │   ├── Deutsch/              5 Bände
│       │   └── English/              5 Bände
│       └── Hardcover_8.25x11/        KDP Print Hardcover 8.25×11 Zoll
│           ├── Deutsch/              5 Bände
│           └── English/              5 Bände
├── Einzeldokumente_A4/
│   ├── Deutsch/                      184 deutsche A4-PDFs
│   │   ├── 001_T0_Book_Abstract_De.pdf
│   │   ├── 001a_T0_Book_Abstract_De.pdf
│   │   ├── ...
│   │   └── 262_AkzeptanzOhneAnschauung_De.pdf
│   └── English/                      184 englische A4-PDFs
│       └── (parallele Namen mit _En)
└── Sources/
    ├── wr_books/                     30 Buch-Wrapper
    ├── wr_standalone_A4/             ~371 A4-Standalone-Wrapper
    │                                 (Originalwrapper mit Titel+ToC,
    │                                 nur Präambel auf A4 umgestellt)
    ├── pri-end/                      Alle Präambeln (inkl. neuer A4)
    └── ch_modifications/             218 modifizierte ch-Dateien
```

## Bücher (5 Bände × 3 KDP-Formate)

### Aufteilung

| Band | Inhalt | Dok.-Anzahl |
|------|--------|-------------|
| Teil 1 | Grundlagen, ξ-Parameter, Konstanten, Einheiten | 40 |
| Teil 2 | Lagrangian-Formalismus, QFT, QM-Tests, Photonenchip | 36 |
| Teil 3 | Kosmologie, CMB, Bewusstsein, FFGFT-Narrativ | 35 |
| Teil 4 | Vom Photon zum p-bit (bis Dok. 184) | 37 |
| Teil 5 | Die Hilbertraum-Brücke (ab Dok. 185) | 37 |

### Seitenzahlen

| Band | eBook DE | Paperback DE | Hardcover DE | eBook EN | Paperback EN | Hardcover EN |
|------|----------|--------------|--------------|----------|--------------|--------------|
| Teil 1 | 531 | 451 | 457 | 489 | 422 | 426 |
| Teil 2 | 505 | 423 | 427 | 454 | 388 | 393 |
| Teil 3 | 487 | 412 | 415 | 461 | 386 | 392 |
| Teil 4 | 473 | 407 | 414 | 406 | 357 | 362 |
| Teil 5 | 506 | 436 | 438 | 480 | 414 | 419 |

KDP-Limits: eBook ≤550, Paperback ≤828, Hardcover ≤550 — alle Bände
innerhalb.

## Einzeldokumente A4

**368 PDFs** im DIN-A4-Format (210 × 297 mm) für wissenschaftliche
Distribution, Drucken auf A4-Papier, Referenz. Jede PDF hat:

- **Titel-Seite** mit dem konkreten Dokumenttitel (`\maketitle`)
- **Inhaltsverzeichnis** (`\tableofcontents`) wenn im Original-Wrapper
  vorgesehen
- **Kopfzeile/Fußzeile** entsprechend dem Original-Wrapper-Stil
- **A4-Geometrie:** innen 25 mm, außen 20 mm, oben/unten 25 mm

### A4-Geometrie (Präambel)

```latex
\usepackage[
  a4paper,
  inner=25mm,
  outer=20mm,
  top=25mm,
  bottom=25mm,
  headheight=14pt,
  footskip=12mm
]{geometry}
```

Datei: `Sources/pri-end/T0_preamble_standalone_A4_{De,En}.tex`

### Dateinamen-Konvention

Saubere Namen ohne Format-Suffix:

- `001a_T0_Book_Abstract_De.pdf`
- `230_Hilbertraum_Uebersetzung_De.pdf`
- `230_Hilbertraum_Uebersetzung_En.pdf`

Die Sprache steht im Dateinamen (`_De` / `_En`); der A4-Status ergibt
sich aus dem Verzeichnis `Einzeldokumente_A4/`.

## Korrekturen seit dem ursprünglichen v1.1.0

### Inhaltlich
- 29 DOI-Verweise in 21 ch-Dateien aktualisiert auf v1.1.2.
- Alle Korrekturen aus Dok. 190 und Dok. 210 integriert.

### Typografie und Layout
- **Tabellen-Wrap (206 ch-Dateien):** 650 Tabellen in
  `\adjustbox{max width=\textwidth}{...}` für Kindle-Breite.
- **Dok 041 EN:** Zwei monolithische Tabellen jeweils in 3 Teile
  gesplittet (verhindert Margin-Überlauf im Paperback).
- **Dok 054:** Verifikations-Tabellen mit
  `\scriptsize\setlength{\tabcolsep}{3pt}\adjustbox{max width=\textwidth}`.
- **Dok 057:** Algorithm- und lstlisting-Blöcke mit `frame=none`,
  `breaklines=true`, `\scriptsize`.

### Build-Infrastruktur
- **`T0_preamble_patches.tex`:** Ergänzt fehlende Environments
  und Farb-Aliase.
- **`T0_preamble_standalone_A4_{De,En}.tex`** (NEU): A4-Variante
  der Standalone-Präambel.
- **Typo-Fix `Teil2-end`:** `023a_Bell-video` → `023b_Bell-video`.

## Eigener Rebuild

```bash
# Bücher
cd Sources/wr_books
for w in Teil*_*.tex; do
  lualatex -interaction=nonstopmode "$w"
  lualatex -interaction=nonstopmode "$w"
done

# A4-Einzeldokumente
cd Sources/wr_standalone_A4
for w in *.tex; do
  lualatex -interaction=nonstopmode "$w"
done
```

Voraussetzung: LuaLaTeX (TeX Live 2023+), Schriften Inter, JetBrains
Mono, Libertinus Math installiert.

## Lizenz

© 2025–2026 Johann Pascher. Lizenziert unter CC BY 4.0.
