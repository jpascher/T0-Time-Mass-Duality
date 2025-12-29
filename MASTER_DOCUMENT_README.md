# DVFT Master Document - Complete Combined Version

This directory contains the master document that compiles all 42 combined DVFT chapters into a single, publication-ready PDF.

## Files

### Main Document
- **DVFT_Complete_Combined.tex** - Master LaTeX document (book class)
  - Includes all 42 combined chapters (1-16, 18-43)
  - Chapters 17 and 44 are not included (no merged versions available)
  - Uses book class with proper chapter formatting
  - Includes table of contents, abstract, and conclusion

### Build Scripts
- **compile_dvft_master.sh** - Bash script to compile the master document
  - Prepares chapter content files
  - Runs pdflatex three times for proper cross-references and TOC
  - Displays compilation statistics

- **prepare_chapters_for_master.py** - Python script to extract chapter content
  - Removes preambles and document environments from combined chapters
  - Creates *_content.tex files for inclusion in master document
  - Processes all 42 available combined chapters

### Chapter Content Files
- **2/tex-n/de_DVFT/combined_chapters/kapitel_XX_combined_content.tex** (42 files)
  - Content-only versions of combined chapters
  - Generated automatically by prepare_chapters_for_master.py
  - Included in master document via `\input` commands

## How to Compile

### Prerequisites
Install a full TeX distribution:
- **Ubuntu/Debian**: `sudo apt-get install texlive-full texlive-lang-german`
- **Fedora/RHEL**: `sudo dnf install texlive-scheme-full`
- **macOS**: Install MacTeX from https://www.tug.org/mactex/
- **Windows**: Install MiKTeX from https://miktex.org/

### Compilation

```bash
# Make script executable (first time only)
chmod +x compile_dvft_master.sh

# Run compilation
./compile_dvft_master.sh
```

The script will:
1. Extract content from all combined chapters
2. Run pdflatex three times to generate proper cross-references
3. Create **DVFT_Complete_Combined.pdf**

### Manual Compilation

If you prefer to compile manually:

```bash
# Prepare chapter content files
python3 prepare_chapters_for_master.py

# Compile with pdflatex (run 3 times)
pdflatex DVFT_Complete_Combined.tex
pdflatex DVFT_Complete_Combined.tex
pdflatex DVFT_Complete_Combined.tex
```

## Document Structure

The master document is organized into 5 parts:

### Part I: Grundlagen (Chapters 1-11)
- T0-Theorie fundamentals
- Fractal geometry and spacetime structure
- Dynamic vacuum field mathematical formulation
- Elementary particle masses
- Leptons, quarks, gauge bosons, Higgs mechanism
- Gravity as emergent phenomenon
- Dark matter and MOND from DVFT
- Unification of QFT and gravity
- Black hole internal structure

### Part II: Kosmologie (Chapters 12-15)
- Cosmology and Friedmann equations
- CMB anisotropies and structure formation
- Inflation without inflaton
- Baryogenesis and leptogenesis

### Part III: Gravitationsphänomene (Chapters 16, 18-19)
- Mercury perihelion precession
- Gravitational waves
- Shapiro delay

### Part IV: Quantenfeldtheorie (Chapters 20-32)
- Yang-Mills mass gap
- QCD and electroweak unification
- Neutrino masses and oscillations
- Lepton masses (extended analysis)
- CP violation, anomalous magnetic moment
- Proton radius puzzle
- Higgs boson and electroweak symmetry breaking
- Top quark mass
- B-meson anomalies
- Muon g-2 anomaly
- Neutron lifetime anomaly

### Part V: Fortgeschrittene Themen (Chapters 33-43)
- Supersymmetry without superpartners
- Dark energy as vacuum effect
- Hubble tension
- Galaxy rotation curves without dark matter
- Globular cluster dynamics
- Gravitational lensing
- Bullet cluster
- Lithium problem
- Quantum gravity and Planck scale
- Black hole information paradox
- Hawking radiation

## Features

### Combined Content
Each chapter combines:
- **Narrative introduction** from merged version (accessible overview)
- **Detailed mathematical derivations** from individual version (rigorous proofs)
- **Unified formulas** with consistent notation
- **No contradictory statements** - all content verified for consistency

### Document Class
- Uses **book** class for professional multi-chapter layout
- Proper chapter, section, and subsection formatting
- Fancy headers with chapter/section names and page numbers
- Comprehensive table of contents
- PDF bookmarks for easy navigation

### Mathematical Typesetting
- Full AMS-LaTeX support (amsmath, amssymb, amsthm)
- Physics package for bra-ket notation and derivatives
- Theorem, lemma, corollary, and definition environments
- Consistent formatting across all chapters

## Output

The compiled PDF will contain:
- Title page
- Abstract (German)
- Table of contents
- 42 chapters organized into 5 parts
- Conclusion

Expected page count: ~200-300 pages (depending on content)

## Notes

- **Missing Chapters**: Chapters 17 and 44 are not included because no merged versions are available
- **Language**: Document is in German (ngerman babel package)
- **Encoding**: UTF-8 input encoding, T1 font encoding
- **Hyperlinks**: PDF includes clickable cross-references and bookmarks
- **Compilation Time**: First compilation may take 2-5 minutes depending on system

## Troubleshooting

### LaTeX Errors
If compilation fails, check:
1. All required LaTeX packages are installed (texlive-full recommended)
2. Chapter content files were generated (`*_content.tex` files exist)
3. Check the .log file for specific error messages

### Missing Content
If chapters appear empty:
1. Verify combined chapter files exist in `2/tex-n/de_DVFT/combined_chapters/`
2. Re-run `prepare_chapters_for_master.py`
3. Check that content files are non-empty

### Compilation Hangs
If pdflatex hangs on errors:
1. Use `-interaction=nonstopmode` flag (already in script)
2. Check .log file for the specific error
3. Fix the error in the source .tex files

## Cleaning Up

To remove auxiliary files:
```bash
rm -f DVFT_Complete_Combined.{aux,log,toc,out,lof,lot}
rm -f texput.log
```

To remove all generated files including PDF:
```bash
rm -f DVFT_Complete_Combined.{aux,log,toc,out,lof,lot,pdf}
rm -f 2/tex-n/de_DVFT/combined_chapters/*_content.tex
```

## License

This document is part of the T0-Time-Mass-Duality project.
See the main repository README for license information.
