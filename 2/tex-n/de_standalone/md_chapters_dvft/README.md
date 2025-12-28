# DVFT Markdown to LaTeX Converter

This directory contains scripts to convert DVFT markdown chapters to LaTeX format.

## Files

- `convert_md_to_latex.sh` - Main bash script that orchestrates the conversion
- `convert_md_to_tex.py` - Python script that handles Unicode character replacement
- `main.tex` - Generated LaTeX main file that includes all chapters
- `kapitel_00.tex` to `kapitel_43.tex` - Generated LaTeX chapter files
- `00_Vorspann.md` to `Kapitel_43.md` - Source markdown files

## Usage

### Basic Conversion

To convert all markdown files to LaTeX:

```bash
./convert_md_to_latex.sh
```

This will:
1. Convert all .md files to .tex files with Unicode character replacements
2. Create a main.tex file with proper preamble and chapter includes
3. Show instructions for manual compilation

### With Compilation

To also attempt PDF compilation:

```bash
./convert_md_to_latex.sh --compile
```

Note: Automatic compilation may fail due to complex math expressions in the source files that require manual formatting adjustments.

## Features

The conversion script handles:

### Character Replacements

- **Greek letters**: 𝜙 → \varphi, ρ → \rho, θ → \theta, μ → \mu, λ → \lambda, etc.
- **Math symbols**: ≈ → \approx, ≠ → \neq, ∂ → \partial, ∇ → \nabla, etc.
- **Superscripts**: ² → \textsuperscript{2}, ³ → \textsuperscript{3}
- **Subscripts**: ₀ → $_0$, ₁ → $_1$, etc.
- **Special symbols**: ● → \bullet, − → -, ∗ → *

### Structure

- **Headers**: `# Title` → `\section{Title}`
- **Preamble**: Includes T0_preamble_shared_De.tex from repository root
- **Physics package**: Automatically included for physics notation

## Manual Compilation

If automatic compilation fails, you can manually compile:

```bash
cd /path/to/md_chapters_dvft
pdflatex main.tex
pdflatex main.tex  # Run twice for TOC and references
```

## Troubleshooting

### Missing Packages

If you encounter missing package errors, install them:

```bash
sudo apt-get install -y texlive-latex-extra texlive-science texlive-fonts-extra
sudo apt-get install -y texlive-lang-german  # For German language support
```

### Unicode Errors

If you see "Unicode character not set up for use with LaTeX" errors:

1. Find the character causing the issue in the error log
2. Add it to the `UNICODE_REPLACEMENTS` list in `convert_md_to_tex.py`
3. Re-run the conversion

### Math Mode Errors

The source markdown contains inline math expressions that may not be properly delimited. You may need to manually:

1. Wrap inline math in `$...$`
2. Wrap display math in `\[...\]` or `equation` environment
3. Fix equation formatting for complex expressions

## Directory Structure

```
md_chapters_dvft/
├── convert_md_to_latex.sh    # Main conversion script
├── convert_md_to_tex.py        # Unicode handling
├── README.md                   # This file
├── 00_Vorspann.md             # Source markdown
├── Kapitel_01.md ... Kapitel_43.md
├── main.tex                    # Generated main file
├── kapitel_00.tex ... kapitel_43.tex  # Generated chapters
└── .gitignore                  # Excludes build artifacts
```

## Generated LaTeX Structure

The generated `main.tex` includes:

```latex
\documentclass[12pt,a4paper]{article}
\input{../../../../T0_preamble_shared_De.tex}
\usepackage{physics}

\begin{document}
\title{Dynamic Vacuum Field Theory\\Complete Chapters}
\author{Satish B. Thorwe}
\maketitle
\tableofcontents

\input{kapitel_00.tex}
\input{kapitel_01.tex}
...
\input{kapitel_43.tex}
\end{document}
```

## Notes

- The script is designed to handle the specific Unicode characters used in DVFT papers
- Math notation conversion is best-effort; complex equations may need manual adjustment
- The T0_preamble_shared_De.tex must be present in the repository root (4 levels up)
- Build artifacts (*.aux, *.log, *.pdf) are excluded via .gitignore

## Support

For issues or improvements, please refer to the repository documentation or submit an issue.
