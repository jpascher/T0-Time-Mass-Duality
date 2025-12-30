# DVFT LaTeX Documentation

## Überblick / Overview

Dieses Verzeichnis enthält die vollständige Dokumentation der Dynamischen Vakuum-Feld-Theorie (DVFT) in deutscher und englischer Sprache.

This directory contains the complete documentation of the Dynamic Vacuum Field Theory (DVFT) in German and English.

## Struktur / Structure

```
2/tex-n/
├── de_DVFT/                          # Deutsche Version / German version
│   ├── DVFT_Hauptdokument_De.tex    # Hauptdokument (alle Kapitel) / Main document (all chapters)
│   └── tex_kapitel/                  # Kapitel-Dateien / Chapter files
│       ├── 202a_1-11_De.tex         # Standalone-Version
│       ├── 202a_1-11_De_section.tex # Für Einbindung / For inclusion
│       ├── kapitel_12a_De.tex       # Standalone-Version
│       ├── kapitel_12a_De_section.tex # Für Einbindung / For inclusion
│       └── ...                       # (34 Kapitel insgesamt / 34 chapters total)
│
└── en_DVFT/                          # Englische Version / English version
    ├── DVFT_MainDocument_En.tex     # Main document (all chapters)
    └── tex_kapitel/                  # Chapter files
        ├── 202a_1-11_En.tex         # Standalone version
        ├── 202a_1-11_En_section.tex # For inclusion
        ├── kapitel_12a_En.tex       # Standalone version
        ├── kapitel_12a_En_section.tex # For inclusion
        └── ...                       # (34 chapters total)
```

## Kompilierung / Compilation

### Gesamtes Dokument kompilieren / Compile Complete Document

**Deutsch / German:**
```bash
cd 2/tex-n/de_DVFT
pdflatex DVFT_Hauptdokument_De.tex
pdflatex DVFT_Hauptdokument_De.tex  # Zweiter Durchlauf für Referenzen / Second pass for references
```

**Englisch / English:**
```bash
cd 2/tex-n/en_DVFT
pdflatex DVFT_MainDocument_En.tex
pdflatex DVFT_MainDocument_En.tex  # Second pass for references
```

### Einzelne Kapitel kompilieren / Compile Individual Chapters

Jedes Kapitel kann auch einzeln kompiliert werden:

Each chapter can also be compiled individually:

```bash
cd 2/tex-n/de_DVFT/tex_kapitel
pdflatex kapitel_12a_De.tex
```

```bash
cd 2/tex-n/en_DVFT/tex_kapitel
pdflatex kapitel_12a_En.tex
```

## Kapitel-Übersicht / Chapter Overview

| Kapitel / Chapter | Deutsch (De) | English (En) | Thema / Topic |
|-------------------|--------------|--------------|----------------|
| 1-11 | 202a_1-11_De.tex | 202a_1-11_En.tex | Grundlagen / Foundations |
| 12 | kapitel_12a_De.tex | kapitel_12a_En.tex | Kosmologie und Big-Bang / Cosmology and Big-Bang |
| 13 | kapitel_13a_De.tex | kapitel_13a_En.tex | Chronologie der Universum-Erschaffung / Chronology of Universe Creation |
| 14 | kapitel_14a_De.tex | kapitel_14a_En.tex | Raum-Schöpfung / Space Creation |
| 15 | kapitel_15a_De.tex | kapitel_15a_En.tex | Merkur-Periheldrehung / Mercury Perihelion |
| 16 | kapitel_16a_De.tex | kapitel_16a_En.tex | Hubble-Spannung / Hubble Tension |
| 17 | kapitel_17a_De.tex | kapitel_17a_En.tex | Alternative zu GR+ΛCDM / Alternative to GR+ΛCDM |
| 18 | kapitel_18a_De.tex | kapitel_18a_En.tex | Heisenberg-Unschärfe / Heisenberg Uncertainty |
| 19 | kapitel_19a_De.tex | kapitel_19a_En.tex | Vakuumfluktuationen / Vacuum Fluctuations |
| 20 | kapitel_20a_De.tex | kapitel_20a_En.tex | Yang-Mills Mass Gap |
| 21 | kapitel_21a_De.tex | kapitel_21a_En.tex | T³ Quantengravitation / T³ Quantum Gravity |
| 22 | kapitel_22a_De.tex | kapitel_22a_En.tex | Quantensuperposition / Quantum Superposition |
| 23 | kapitel_23a_De.tex | kapitel_23a_En.tex | Neutronen-Lebensdauer / Neutron Lifetime |
| 24 | kapitel_24a_De.tex | kapitel_24a_En.tex | Koide-Massenformel / Koide Mass Formula |
| 25 | kapitel_25a_De.tex | kapitel_25a_En.tex | Neutrino-Masse / Neutrino Mass |
| 26 | kapitel_26a_De.tex | kapitel_26a_En.tex | Baryonische Asymmetrie / Baryonic Asymmetry |
| 27 | kapitel_27a_De.tex | kapitel_27a_En.tex | Massenhierarchie / Mass Hierarchy |
| 28 | kapitel_28a_De.tex | kapitel_28a_En.tex | Newtons Gesetz / Newton's Law |
| 29 | kapitel_29a_De.tex | kapitel_29a_En.tex | Delayed-Choice Experiment |
| 30 | kapitel_30a_De.tex | kapitel_30a_En.tex | Quantenprozesse im Gehirn / Quantum Processes in Brain |
| 31 | kapitel_31a_De.tex | kapitel_31a_En.tex | Photoelektrischer Effekt / Photoelectric Effect |
| 32 | kapitel_32a_De.tex | kapitel_32a_En.tex | Reaktor-Antineutrino-Anomalie / Reactor Antineutrino Anomaly |
| 33 | kapitel_33a_De.tex | kapitel_33a_En.tex | Pauli-Ausschlussprinzip / Pauli Exclusion Principle |
| 34 | kapitel_34a_De.tex | kapitel_34a_En.tex | Strong-CP-Problem / Strong CP Problem |
| 35 | kapitel_35a_De.tex | kapitel_35a_En.tex | Quantenphänomene / Quantum Phenomena |
| 36 | kapitel_36a_De.tex | kapitel_36a_En.tex | QFT und Gravitation / QFT and Gravitation |
| 37 | kapitel_37a_De.tex | kapitel_37a_En.tex | Vakuumfeld-Eigenschaften / Vacuum Field Properties |
| 38 | kapitel_38a_De.tex | kapitel_38a_En.tex | Schwarze Löcher / Black Holes |
| 39 | kapitel_39a_De.tex | kapitel_39a_En.tex | Entropie / Entropy |
| 40 | kapitel_40a_De.tex | kapitel_40a_En.tex | Alternative zu GR und QFT / Alternative to GR and QFT |
| 41 | kapitel_41a_De.tex | kapitel_41a_En.tex | Vakuumfeld (Erweitert) / Vacuum Field (Extended) |
| 42 | kapitel_42a_De.tex | kapitel_42a_En.tex | Planck-Einheiten / Planck Units |
| 43 | kapitel_43a_De.tex | kapitel_43a_En.tex | Axiome und Konstanten / Axioms and Constants |
| 44 | kapitel_44a_De.tex | kapitel_44a_En.tex | Qubits, Schrödinger, Dirac |

## Verwendete Pakete / Required Packages

Die Dokumente benötigen folgende LaTeX-Pakete:

The documents require the following LaTeX packages:

- amsmath, amsfonts, amssymb (Mathematik / Mathematics)
- geometry (Seitenlayout / Page layout)
- hyperref (Querverweise / Cross-references)
- tikz (Diagramme / Diagrams)
- tcolorbox (Boxen / Boxes)
- physics (Physik-Notation / Physics notation)
- fancyhdr (Kopf-/Fußzeilen / Headers/footers)

## Hinweise / Notes

1. **Standalone-Dateien**: Die `*_De.tex` und `*_En.tex` Dateien können einzeln kompiliert werden und enthalten eine vollständige Präambel.

   **Standalone files**: The `*_De.tex` and `*_En.tex` files can be compiled individually and contain a complete preamble.

2. **Section-Dateien**: Die `*_section.tex` Dateien enthalten nur den Inhalt (ohne Präambel) und werden vom Hauptdokument eingebunden.

   **Section files**: The `*_section.tex` files contain only the content (without preamble) and are included by the main document.

3. **Doppelte Kompilierung**: Das Hauptdokument sollte zweimal kompiliert werden, um alle Querverweise korrekt aufzulösen.

   **Double compilation**: The main document should be compiled twice to correctly resolve all cross-references.

## Lokales Checkout / Local Checkout

Um diesen Branch lokal auszuchecken:

To checkout this branch locally:

```bash
git clone https://github.com/jpascher/T0-Time-Mass-Duality.git
cd T0-Time-Mass-Duality
git checkout copilot/checkout-main-to-compare-theory-chapters
```

Oder wenn das Repository bereits geklont ist:

Or if the repository is already cloned:

```bash
git fetch origin
git checkout copilot/checkout-main-to-compare-theory-chapters
```

## Status

✅ Alle 34 Kapitel vollständig übersetzt (Deutsch → Englisch)
✅ Hauptdokumente erstellt für beide Sprachen
✅ Section-Dateien für alle Kapitel generiert

✅ All 34 chapters completely translated (German → English)
✅ Main documents created for both languages
✅ Section files generated for all chapters
