# T0 LaTeX Dokumenten-Standardisierung

Dieses Verzeichnis enthält die LaTeX-Quelldateien für das T0 Zeit-Masse-Dualität Framework.

## Einheitliche Vorlagen

Um Konsistenz zwischen allen Dokumenten zu gewährleisten, wurden folgende Standarddateien erstellt:

### Präambel-Vorlagen

- **`T0_Preamble_De.tex`** - Einheitliche Präambel für deutsche Dokumente
- **`T0_Preamble_En.tex`** - Einheitliche Präambel für englische Dokumente

Diese Präambeln enthalten:
- Standardisierte Paketimporte (amsmath, physics, hyperref, etc.)
- Einheitliche Seitengeometrie (A4, 2.5cm Ränder)
- Konsistente Kopf- und Fußzeilen
- Vordefinierte tcolorbox-Umgebungen (keyresult, warning, formula, etc.)
- T0-spezifische mathematische Befehle (xipar, Tfield, Planck-Einheiten, etc.)

### Bibliographie-Vorlagen

- **`T0_Bibliography_Items_De.tex`** - Deutsche Bibliographie-Einträge
- **`T0_Bibliography_Items_En.tex`** - Englische Bibliographie-Einträge

Diese Dateien können innerhalb einer `thebibliography`-Umgebung mit `\input` geladen werden.

### Dokument-Vorlagen

- **`T0_Template_De.tex`** - Vorlage für neue deutsche Dokumente
- **`T0_Template_En.tex`** - Vorlage für neue englische Dokumente

## Verwendung der Standardvorlagen

### Für neue Dokumente

Kopieren Sie die entsprechende Vorlage und passen Sie sie an:

```latex
\documentclass[12pt,a4paper]{article}

% Einheitliche T0 Präambel laden
\input{T0_Preamble_De}  % oder T0_Preamble_En für Englisch

% Dokumentspezifische Einstellungen
\hypersetup{
    pdftitle={Ihr Dokumenttitel},
}

\title{\textbf{Ihr Titel}}
\author{Johann Pascher\\...}
\date{\today}

\begin{document}
    
\maketitle
% Ihr Inhalt...

\begin{thebibliography}{99}
    \input{T0_Bibliography_Items_De}  % Lädt alle Standard-Referenzen
    % Ihre zusätzlichen Referenzen...
\end{thebibliography}

\end{document}
```

### Für bestehende Dokumente

Bestehende Dokumente können schrittweise angepasst werden, indem einzelne Elemente der Standardpräambel übernommen werden.

## Verzeichnisstruktur

```
tex/
├── T0_Preamble_De.tex          # Deutsche Präambel-Vorlage
├── T0_Preamble_En.tex          # Englische Präambel-Vorlage
├── T0_Bibliography_Items_De.tex # Deutsche Bibliographie
├── T0_Bibliography_Items_En.tex # Englische Bibliographie
├── T0_Template_De.tex          # Deutsche Dokumentvorlage
├── T0_Template_En.tex          # Englische Dokumentvorlage
├── T0_Bibliography_De.tex      # Vollständige deutsche Bibliographie
├── T0_Bibliography_En.tex      # Vollständige englische Bibliographie
├── standardize_latex.py        # Automatisierungsskript (optional)
├── README_TEMPLATES.md         # Diese Datei
└── *.tex                       # Alle anderen Dokumente
```

## Standardisierte Elemente

### Dokumentklasse
```latex
\documentclass[12pt,a4paper]{article}
```

### Sprache
- Deutsch: `\usepackage[ngerman]{babel}`
- Englisch: `\usepackage[english]{babel}`

### Seitengeometrie
```latex
\geometry{a4paper, margin=2.5cm}
```

### Kopf- und Fußzeilen
```latex
\pagestyle{fancy}
\fancyhead[L]{\textsc{T0-Theorie}}  % oder "T0 Theory" auf Englisch
\fancyhead[R]{\textsc{Johann Pascher}}
\fancyfoot[C]{\thepage}
```

### Vordefinierte Box-Umgebungen

| Umgebung | Verwendung | Farbe |
|----------|------------|-------|
| `keyresult` | Schlüsselergebnisse | Blau |
| `warning` | Wichtige Hinweise | Rot |
| `formula` | Formeln | Blau |
| `result` | Ergebnisse | Grün |
| `summary` | Zusammenfassungen | Orange |
| `important` | Wichtige Punkte | Grün |

### T0-spezifische Befehle

| Befehl | Ausgabe | Beschreibung |
|--------|---------|--------------|
| `\xipar` | ξ | Fundamentaler Parameter |
| `\Tfield` | T(x,t) | Zeitfeld |
| `\Efield` | E(x,t) | Energiefeld |
| `\lP` | ℓ_P | Planck-Länge |
| `\tP` | t_P | Planck-Zeit |
| `\mP` | m_P | Planck-Masse |
| `\EP` | E_P | Planck-Energie |
| `\LCDM` | ΛCDM | Kosmologisches Modell |

## Automatisierung

Das Skript `standardize_latex.py` kann verwendet werden, um mehrere Dokumente automatisch zu standardisieren:

```bash
# Vorschau (keine Änderungen)
python3 standardize_latex.py --dry-run --verbose

# Spezifische Dateien verarbeiten
python3 standardize_latex.py --verbose datei1.tex datei2.tex
```

**Hinweis:** Verwenden Sie die Automatisierung mit Vorsicht und prüfen Sie die Ergebnisse manuell.

## Kontakt

Johann Pascher  
HTL Leonding, Österreich  
johann.pascher@gmail.com
