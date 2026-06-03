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

## Revision Juni 2026 (2. Update): z-Korrektur (P15/R15) + Dok 263

Ergaenzend zur ersten Juni-Revision:

5. **P15/R15 - kosmologisches z als LambdaCDM-Vergleichsgroesse.** Das statische
   xi-Universum kennt kein kosmologisches z im Expansionssinn (FFGFT-Rotverschiebung
   = fraktale Wegverlaengerung). Unmarkierte z-Rechnungen, die wie FFGFT-eigene
   Ergebnisse aussahen, wurden ausdruecklich als LambdaCDM-Vergleichsrechnungen
   markiert: Dok. 061 (Rekombinations-Abschnitt als Vergleichsrahmen gerahmt;
   Abstract/Zusammenfassung auf "ohne Entkopplung bei irgendeinem z" umgestellt)
   und Dok. 041 (z=1100-Werte als "(LambdaCDM)" gekennzeichnet). Registriert als
   P15/R15 in Dok. 190. Die CMB entsteht in FFGFT durch stationaere Thermalisierung
   in einem unendlich alten Universum. Hinweis: weitere unmarkierte Pipeline-
   Vergleiche im Korpus sind separat zu pruefen (laufend).

6. **Dok. 263 - Fraktale Holografie** (neu, DE+EN). Verortet FFGFT gegenueber dem
   holografischen Prinzip: belegte Beruehrungspunkte (Flaechengesetz aus
   Knotenzaehlung), offene Skalierungsfrage (Flaeche vs. Volumen, Reduktionsschicht),
   Hologramm-Analogie (Metapher), Reversibilitaet (FFGFT leitet Zeit-Asymmetrie ab,
   Dok. 157), Verankerung am beschraenkten Kern (keine Singularitaet), und die
   offene Feststellung: keine exakte Uebersetzungsgroesse gefunden. Liegt als
   Einzeldokument (A4, DE+EN) bei; noch keinem Buchband zugeordnet.

**Neu gebaute Baende in diesem Update:** Teil 1 (enthaelt Dok. 041), Teil 3
(enthaelt Dok. 061) und Teil 5 (enthaelt Dok. 190), je in allen drei Formaten
und beiden Sprachen. Teil 2 und Teil 4 unveraendert.

## Revision Juni 2026 (P14 / Rotverschiebung + ch-Konsolidierung)

Diese überarbeitete Auslieferung ergänzt das Mai/Juni-Update um folgende
inhaltliche und strukturelle Korrekturen:

1. **P14 / R14 — Rotverschiebung in Dok. 041.** Die Beschreibung
   "Photon energy loss through xi-field" wurde ersetzt durch
   **fraktale Wegverlaengerung** (geometrische Wegstreckung; ein
   "Energieverlust" ist nur ein scheinbares Artefakt, das entstuende,
   wenn man die Wegverlaengerung weglaesst; die Weglaengen-Abhaengigkeit
   bleibt). Eingearbeitet in **Dok. 041** (DE+EN) umgesetzt und in **Dok. 190** als erledigt
   verbucht (Status: P1--P14 / R1--R14 eingearbeitet; DE: P14, EN: R14;
   EN-Uebersichtstabelle um R12/R13 vervollstaendigt).

2. **ch-Konsolidierung.** Die bisher getrennten Quellverzeichnisse `ch`
   und `ch_modifications` wurden zu **einem einzigen** Verzeichnis
   `Sources/ch/` zusammengefuehrt (vollstaendiger aktueller Stand,
   391 Dateien inkl. der Teil-Einleitungen 1-5). Praezedenz: In-Session-
   Edits (041/190) > layout-gepatchte Fassung (adjustbox-Tabellen) > Basis.
   `ch_modifications` entfaellt.

3. **Buch-Preamble-Patches.** `Sources/pri-end/T0_preamble_patches.tex`
   definiert nun zusaetzlich den Seitenstil `firstpage`, laedt `nicefrac`
   und stellt `\blacksquare`/`\square` bereit — Befehle, die einige
   Kapitel nutzen, die im Buch-Preamble bislang fehlten. Dadurch bauen
   die betroffenen Baende sauber (zuvor stillschweigend fehlerhaft
   gerendert).

**Neu gebaute PDFs in dieser Revision:** Einzeldokumente 041 und 190
(DE+EN) sowie die Baende **Teil 1** (enthaelt Dok. 041) und **Teil 5**
(enthaelt Dok. 190) in allen drei Formaten und beiden Sprachen. Alle
uebrigen PDFs sind inhaltlich unveraendert uebernommen.

4. **Zitationsbefehle in Dok. 248 bereinigt.** Dok. 248 (Epistemologie,
   DE+EN) nutzte `\citeauthor`/`\citeyear` ohne geladenes Zitationspaket
   (nicht-fatale Warnung, auch im Original). Lokal ersetzt durch Klartext
   (Autor/Jahr: Shannon 1948, Bateson 1972) -- kein globaler Preamble-
   Eingriff, daher ohne Nebenwirkung auf die 164 anderen Dokumente mit
   `thebibliography`. Damit bauen Dok. 248 und Teil 5 jetzt ohne
   undefinierte Befehle.

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
    └── ch/  (konsolidiert, 391 Dateien)             218 modifizierte ch-Dateien
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
