# T0 Theory - LaTeX Documents

## Quick Start

### Clone and Checkout
```bash
# In ein neues Verzeichnis klonen
mkdir T0-Books
cd T0-Books
git clone https://github.com/jpascher/T0-Time-Mass-Duality.git .
git checkout copilot/fix-latex-compilation-errors
cd 2/tex
```

## Bücher kompilieren

### T0_Book4_En (726 Seiten, vollständige Sammlung)
```bash
cd 2/tex
pdflatex T0_Book4_En.tex
pdflatex T0_Book4_En.tex  # Zweiter Durchlauf für Querverweise
```

### T0_Book5_En (439 Seiten, per-Kapitel Bibliografien)
```bash
cd 2/tex
pdflatex T0_Book5_En.tex
pdflatex T0_Book5_En.tex
```

## Standalone-Dokumente kompilieren

### Einzelnes Dokument
```bash
# Englisch
cd 2/tex/standalone/en
pdflatex 137_En.tex

# Deutsch
cd 2/tex/standalone/de
pdflatex 137_En.tex

# Französisch
cd 2/tex/standalone/fr
pdflatex 137_En.tex

# Spanisch
cd 2/tex/standalone/es
pdflatex 137_En.tex

# Italienisch
cd 2/tex/standalone/it
pdflatex 137_It.tex
```

### Alle Dokumente einer Sprache
```bash
cd 2/tex/standalone/de
for f in *.tex; do pdflatex "$f"; done
```

## Verzeichnisstruktur

```
2/tex/
├── T0_Book4_En.tex          # Vollständiges Buch (60 Kapitel)
├── T0_Book5_En.tex          # Buch mit per-Kapitel Bibliografien
├── pri.tex                  # Gemeinsame Präambel
├── chapters_en/             # Kapitel für Bücher
├── chapters_en_bib/         # Kapitel mit eingebetteten Bibliografien
├── standalone/              # Einzeldokumente
│   ├── en/                  # 95 englische Dokumente
│   ├── de/                  # 95 deutsche Dokumente
│   ├── fr/                  # 95 französische Dokumente
│   ├── es/                  # 95 spanische Dokumente
│   └── it/                  # 95 italienische Dokumente
└── pdf/                     # Vorkompilierte PDFs
    ├── books/
    │   ├── T0_Book4_En.pdf
    │   └── T0_Book5_En.pdf
    └── standalone/
        ├── en/
        ├── de/
        ├── fr/
        ├── es/
        └── it/
```

## Integration in Hauptrepo

Nach erfolgreicher lokaler Prüfung kann der Branch in `main` gemergt werden:

### Option 1: GitHub Pull Request (empfohlen)
1. Öffne GitHub: https://github.com/jpascher/T0-Time-Mass-Duality/pulls
2. Klicke auf "Merge pull request" für PR #X
3. Bestätige mit "Confirm merge"

### Option 2: Lokales Merge
```bash
git checkout main
git pull origin main
git merge copilot/fix-latex-compilation-errors
git push origin main
```

## Änderungen in diesem Branch

### Behobene Probleme
- ✅ Alle LaTeX-Kompilierungsfehler behoben
- ✅ 150+ Bibliografie-Einträge hinzugefügt
- ✅ 60 Kapitel in T0_Book4_En.tex
- ✅ Deutsche Anführungszeichen korrigiert (`„..."` statt `"..."`)
- ✅ Silbentrennung für lange deutsche Wörter
- ✅ Italienische Standalone-Dokumente hinzugefügt

### Bücher
| Buch | Seiten | Beschreibung |
|------|--------|--------------|
| T0_Book4_En.pdf | 726 | Vollständige Sammlung aller Kapitel |
| T0_Book5_En.pdf | 439 | Per-Kapitel Bibliografien |

### Standalone-Dokumente
| Sprache | Anzahl | Verzeichnis |
|---------|--------|-------------|
| Englisch | 95 | standalone/en/ |
| Deutsch | 95 | standalone/de/ |
| Französisch | 95 | standalone/fr/ |
| Spanisch | 95 | standalone/es/ |
| Italienisch | 95 | standalone/it/ |

## Autor
Johann Pascher

## Lizenz
Siehe Hauptverzeichnis des Repositories.
