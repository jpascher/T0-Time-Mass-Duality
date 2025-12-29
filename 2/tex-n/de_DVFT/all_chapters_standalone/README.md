# All DVFT Chapters - Standalone Files

This directory contains all 44 DVFT chapters as standalone LaTeX files, prepared for comparison and analysis.

## Contents

### Chapters 1-11 (Foundational Theory)
- Extracted from individual files in `tex_DVFT_T0/`
- Wrapped with standalone document structure
- Files: `kapitel_01_standalone.tex` through `kapitel_11_standalone.tex`

### Chapters 12-44 (Applications)
- Copied from combined files in `combined_chapters/`
- Already in standalone format
- Files: `kapitel_12_standalone.tex` through `kapitel_44_standalone.tex`

## Usage

These files can be used for:
1. Side-by-side comparison of different chapter versions
2. Individual compilation of any chapter
3. Mathematical consistency validation
4. Content analysis and extraction

## Compilation

Each file can be compiled independently:
```bash
pdflatex kapitel_XX_standalone.tex
```

## Structure

All files follow a consistent structure:
- Document class: article (12pt, a4paper)
- Standard DVFT packages
- Title, author, date
- Chapter content
- Complete document (\begin{document} ... \end{document})
