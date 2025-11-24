# Kompilierung der T0 Bücher / Compiling the T0 Books

Dieses Dokument erklärt, wie die T0-Theorie-Bücher kompiliert werden können.
This document explains how to compile the T0 theory books.

---

## Deutsch

### Voraussetzungen

1. **LaTeX-Distribution installieren:**
   - **Windows:** MiKTeX (https://miktex.org/) oder TeX Live (https://tug.org/texlive/)
   - **macOS:** MacTeX (https://www.tug.org/mactex/)
   - **Linux:** TeX Live über Paketmanager (z.B. `sudo apt-get install texlive-full`)

2. **Erforderliche LaTeX-Pakete:**
   Die Bücher benötigen folgende Pakete (die meisten sind in vollständigen Distributionen enthalten):
   - amsmath, amssymb, amsthm
   - graphicx
   - hyperref
   - booktabs, longtable
   - siunitx
   - fancyhdr
   - float
   - tikz
   - setspace
   - enumitem
   - adjustbox
   - xcolor

### Methode 1: Manuelle Kompilierung (Kommandozeile)

#### Für das englische Buch (T0_Book_En.tex):

```bash
cd /pfad/zum/repository
pdflatex T0_Book_En.tex
pdflatex T0_Book_En.tex  # Zweimal ausführen für korrekte Referenzen
```

#### Für das deutsche Buch (T0_Book_De.tex):

```bash
cd /pfad/zum/repository
pdflatex T0_Book_De.tex
pdflatex T0_Book_De.tex  # Zweimal ausführen für korrekte Referenzen
```

**Hinweis:** Es wird empfohlen, pdflatex zweimal auszuführen, um das Inhaltsverzeichnis und alle Querverweise korrekt zu generieren.

### Methode 2: Mit LaTeX-Editor

1. Öffnen Sie `T0_Book_En.tex` oder `T0_Book_De.tex` in Ihrem LaTeX-Editor:
   - **TeXstudio** (empfohlen): https://www.texstudio.org/
   - **TeXmaker**: https://www.xm1math.net/texmaker/
   - **Overleaf**: https://www.overleaf.com/ (Online-Editor)

2. Klicken Sie auf den "Build" oder "Kompilieren" Button (normalerweise F5 oder F1)

3. Der Editor führt automatisch pdflatex aus und erstellt die PDF-Datei

### Methode 3: Mit PowerShell-Skript (nur Windows)

Für einzelne Dokumente im `2/tex/` Verzeichnis:

```powershell
cd 2\tex
.\compile_latex.ps1
```

**Hinweis:** Dieses Skript ist für einzelne Dokumente im `2/tex` Verzeichnis gedacht, nicht für die Hauptbücher.

### Ausgabedateien

Nach erfolgreicher Kompilierung finden Sie:
- `T0_Book_En.pdf` - Das komplette englische Buch
- `T0_Book_De.pdf` - Das komplette deutsche Buch

### Fehlerbehebung

**Problem:** "File not found" Fehler für Dateien in `2/tex/`
- **Lösung:** Stellen Sie sicher, dass Sie den Befehl im Hauptverzeichnis des Repositories ausführen, nicht im `2/tex/` Unterverzeichnis.

**Problem:** Fehlende Pakete
- **Lösung:** Installieren Sie die fehlenden Pakete mit dem Paketmanager Ihrer LaTeX-Distribution:
  - MiKTeX: Öffnen Sie MiKTeX Console → Packages → Suchen und installieren
  - TeX Live: `tlmgr install <paketname>`

**Problem:** Zu viele Fehler beim Kompilieren
- **Lösung:** Führen Sie pdflatex mit `-interaction=nonstopmode` aus:
  ```bash
  pdflatex -interaction=nonstopmode T0_Book_En.tex
  ```

**Problem:** Unvollständiges Inhaltsverzeichnis oder fehlende Referenzen
- **Lösung:** Führen Sie pdflatex mehrmals aus (mindestens zweimal)

---

## English

### Prerequisites

1. **Install LaTeX distribution:**
   - **Windows:** MiKTeX (https://miktex.org/) or TeX Live (https://tug.org/texlive/)
   - **macOS:** MacTeX (https://www.tug.org/mactex/)
   - **Linux:** TeX Live via package manager (e.g., `sudo apt-get install texlive-full`)

2. **Required LaTeX packages:**
   The books require the following packages (most are included in full distributions):
   - amsmath, amssymb, amsthm
   - graphicx
   - hyperref
   - booktabs, longtable
   - siunitx
   - fancyhdr
   - float
   - tikz
   - setspace
   - enumitem
   - adjustbox
   - xcolor

### Method 1: Manual Compilation (Command Line)

#### For the English book (T0_Book_En.tex):

```bash
cd /path/to/repository
pdflatex T0_Book_En.tex
pdflatex T0_Book_En.tex  # Run twice for correct references
```

#### For the German book (T0_Book_De.tex):

```bash
cd /path/to/repository
pdflatex T0_Book_De.tex
pdflatex T0_Book_De.tex  # Run twice for correct references
```

**Note:** It's recommended to run pdflatex twice to correctly generate the table of contents and all cross-references.

### Method 2: Using LaTeX Editor

1. Open `T0_Book_En.tex` or `T0_Book_De.tex` in your LaTeX editor:
   - **TeXstudio** (recommended): https://www.texstudio.org/
   - **TeXmaker**: https://www.xm1math.net/texmaker/
   - **Overleaf**: https://www.overleaf.com/ (online editor)

2. Click the "Build" or "Compile" button (usually F5 or F1)

3. The editor will automatically run pdflatex and create the PDF file

### Method 3: Using PowerShell Script (Windows only)

For individual documents in the `2/tex/` directory:

```powershell
cd 2\tex
.\compile_latex.ps1
```

**Note:** This script is for individual documents in the `2/tex` directory, not for the main books.

### Output Files

After successful compilation, you will find:
- `T0_Book_En.pdf` - The complete English book
- `T0_Book_De.pdf` - The complete German book

### Troubleshooting

**Issue:** "File not found" errors for files in `2/tex/`
- **Solution:** Make sure you run the command from the repository's root directory, not from the `2/tex/` subdirectory.

**Issue:** Missing packages
- **Solution:** Install missing packages using your LaTeX distribution's package manager:
  - MiKTeX: Open MiKTeX Console → Packages → Search and install
  - TeX Live: `tlmgr install <packagename>`

**Issue:** Too many errors during compilation
- **Solution:** Run pdflatex with `-interaction=nonstopmode`:
  ```bash
  pdflatex -interaction=nonstopmode T0_Book_En.tex
  ```

**Issue:** Incomplete table of contents or missing references
- **Solution:** Run pdflatex multiple times (at least twice)

---

## Struktur / Structure

Die Bücher enthalten alle T0-Theorie Dokumente aus dem `2/tex/` Verzeichnis:
The books include all T0 theory documents from the `2/tex/` directory:

- **83 Dokumente pro Buch** / **83 documents per book**
- **Organisiert in logischen Abschnitten** / **Organized in logical sections**:
  - Grundlagen und Übersicht / Foundation and Overview
  - Energie, Konstanten und SI-Einheiten / Energy, Constants and SI Units
  - Anomale magnetische Momente und Quantentheorie / Anomalous Magnetic Moments and Quantum Theory
  - Bell, Netzwerke und Kosmologie / Bell, Networks and Cosmology
  - Spezielle Themen / Special Topics
  - Quantenmechanik / Quantum Mechanics
  - Lagrange und Dirac / Lagrangian and Dirac
  - CMB und Herleitungen / CMB and Derivations
  - Weitere Themen / Additional Topics
  - Formeln und detaillierte Berechnungen / Formulas and Detailed Calculations
  - Systeme und RSA / Systems and RSA
  - Massenelimination / Mass Elimination
  - Deterministische QM / Deterministic QM
  - Zusammenfassung und Photonenchip / Summary and Photon Chip
