# DVFT Chapter Conversion Tools

This directory contains tools to convert DVFT (Dynamic Vacuum Field Theory) chapters from Markdown to LaTeX format.

## Files Generated

The conversion creates the following structure:

```
2/tex-n/de_standalone/dvft_latex_chapters/
├── kapitel_00.tex          # Standalone LaTeX files (with full document structure)
├── kapitel_01.tex
├── ...
├── kapitel_43.tex
├── main.tex                # Placeholder main file
├── main_complete.tex       # Complete document including all chapters
└── content_only/           # Chapter content without document structure
    ├── kapitel_00.tex
    ├── kapitel_01.tex
    ├── ...
    └── kapitel_43.tex
```

## Tools

### 1. convert_dvft_md_to_latex.py

Python script that converts Markdown files to LaTeX format.

**Features:**
- Converts Markdown headers (`#`, `##`, `###`) to LaTeX sections (`\section{}`, `\subsection{}`, etc.)
- Replaces Unicode mathematical symbols with LaTeX commands:
  - Greek letters: 𝜙 → `\varphi`, 𝜌 → `\rho`, θ → `\theta`, μ → `\mu`, etc.
  - Mathematical operators: ∂ → `\partial`, ∇ → `\nabla`, ∫ → `\int`, etc.
  - Subscripts and superscripts: ₀ → `_0`, ² → `^2`, etc.
- Includes physics package integration
- References T0_preamble_shared_De.tex for consistent formatting
- Creates both standalone and includable versions

**Usage:**
```bash
python3 convert_dvft_md_to_latex.py [--input-dir DIR] [--output-dir DIR]
```

**Default directories:**
- Input: `2/tex-n/de_standalone/md_chapters_dvft/`
- Output: `2/tex-n/de_standalone/dvft_latex_chapters/`

### 2. compile_dvft_chapters.sh

Bash script for compiling LaTeX files with pdflatex.

**Features:**
- Multiple compilation passes (3 passes) for proper cross-references and TOC
- Comprehensive error handling and logging
- Colored output for easy status tracking
- Can compile individual chapters or all chapters
- Uses sudo pdflatex as specified in requirements
- Detailed logging in `/tmp/dvft_compilation_logs/`

**Usage:**
```bash
# Compile all chapters
./compile_dvft_chapters.sh --all

# Compile main document
./compile_dvft_chapters.sh --main

# Compile specific chapter (e.g., chapter 5)
./compile_dvft_chapters.sh --chapter 05

# Default (compiles all)
./compile_dvft_chapters.sh
```

**Requirements:**
- pdflatex must be installed
- sudo access (as specified in requirements)
- LaTeX packages: physics, amsmath, amssymb, etc. (listed in T0_preamble_shared_De.tex)

## Source Files

The markdown source files are located in:
```
2/tex-n/de_standalone/md_chapters_dvft/
├── 00_Vorspann.md
├── Kapitel_01.md
├── Kapitel_02.md
├── ...
└── Kapitel_43.md
```

## Output Structure

### Standalone Files (kapitel_XX.tex)
Each standalone file includes:
- Full `\documentclass` declaration
- Reference to `T0_preamble_shared_De.tex`
- `\begin{document}` ... `\end{document}`
- Can be compiled individually

### Content-only Files (content_only/kapitel_XX.tex)
Each content-only file includes:
- `\chapter{}` heading with label
- Chapter content only
- Designed to be `\input{}` into a larger document

### Main Documents
- **main.tex**: Placeholder for standalone compilation approach
- **main_complete.tex**: Complete book with all chapters included using `\input{}`

## Compilation Process

The compilation script performs:

1. **Pass 1**: Initial compilation, generates auxiliary files
2. **Pass 2**: Resolves cross-references
3. **Pass 3**: Final pass to ensure all references are resolved

For each file, the script:
- Compiles with `pdflatex -interaction=nonstopmode -halt-on-error`
- Logs output to individual log files
- Reports success/failure with colored output
- Cleans up auxiliary files (.aux, .log, .out, .toc)

## Error Handling

The compilation script:
- Captures all errors in log files
- Provides summary of failed compilations
- Shows error details from LaTeX output
- Exits with code 1 if any compilation fails

## Logs

Compilation logs are stored in:
```
/tmp/dvft_compilation_logs/
├── compilation_YYYYMMDD_HHMMSS.log    # Main summary log
└── kapitel_XX_YYYYMMDD_HHMMSS.log     # Individual chapter logs
```

## Example Workflow

```bash
# 1. Convert Markdown to LaTeX
python3 convert_dvft_md_to_latex.py

# 2. Compile a single chapter to test
./compile_dvft_chapters.sh --chapter 01

# 3. If successful, compile all chapters
./compile_dvft_chapters.sh --all

# 4. Compile the complete document
./compile_dvft_chapters.sh --main
```

## Notes

- The conversion preserves the original text structure as much as possible
- Some manual adjustments may be needed for complex mathematical expressions
- The script attempts to identify and convert common patterns, but LaTeX math mode may need refinement
- Journal headers (IJFMR) are preserved in the output
- All files use UTF-8 encoding

## Maintenance

To regenerate all LaTeX files after updating the Markdown sources:

```bash
# Remove old generated files
rm -rf 2/tex-n/de_standalone/dvft_latex_chapters

# Regenerate
python3 convert_dvft_md_to_latex.py
```

## Author

Generated for T0 Theory Project
Date: 2025-12-28
