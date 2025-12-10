# Chapter Generation Scripts Documentation

## Overview

This directory contains scripts to generate chapter files from standalone LaTeX documents. These scripts are crucial for converting individual standalone documents into chapters that can be included in multi-chapter books.

## Purpose

The chapter generation process is needed because:

1. **Standalone documents** use `\documentclass{article}` and contain complete LaTeX structure including preamble, title, abstract, and `\maketitle`
2. **Chapter files** for books need only the content between `\begin{document}` and `\end{document}`, with a `\chapter{}` command instead of `\title{}` and `\maketitle`
3. **Book class compatibility**: Abstract environments and certain commands don't work in book chapters

## Available Scripts

### 1. `generate_chapter_exact.py` - Primary Script

**Purpose**: Generate chapter files with EXACT content preservation from standalone documents.

**Features**:
- Extracts content between `\begin{document}` and `\end{document}` WITHOUT ANY modifications
- Preserves ALL LaTeX commands including `\resizebox`, table structures, and formatting
- Converts `\title{}` to `\chapter{}`
- Does NOT remove `\maketitle` or `\tableofcontents` (use `generate_chapter_clean.py` for that)

**Usage**:
```bash
# Generate specific files (recommended)
python generate_chapter_exact.py De 018 041 054 103
python generate_chapter_exact.py En 018 041 054 103

# Generate all files (processes all standalone documents)
python generate_chapter_exact.py De --all
python generate_chapter_exact.py En --all
```

**Arguments**:
- `<language>`: Either `De` (German) or `En` (English)
- `<file_numbers>`: Space-separated list of file numbers (e.g., `018 041 103`)
- `--all`: Process all standalone files for the specified language

**Example**:
```bash
# Generate chapter files for landscape-fixed documents
cd /path/to/T0-Time-Mass-Duality/2/tex
python generate_chapter_exact.py De 018 041 054 103
python generate_chapter_exact.py En 018 041 054 103
```

### 2. `generate_chapter_clean.py` - Cleanup Script

**Purpose**: Generate chapter files with content cleaning (removes `\maketitle` and `\tableofcontents`).

**Features**:
- Extracts content between `\begin{document}` and `\end{document}`
- **Removes** `\maketitle` command (not needed in book chapters)
- **Removes** `\tableofcontents` command (book has its own TOC)
- Preserves ALL other content exactly (tables, resizebox, formatting)
- Converts `\title{}` to `\chapter{}`

**Usage**:
```bash
# Run without arguments - processes hardcoded list of landscape-fixed documents
python generate_chapter_clean.py
```

**Hardcoded documents**:
- `018_T0_Anomale-g2-9` (DE + EN)
- `041_parameterherleitung` (DE + EN)
- `054_Elimination_Of_Mass_Dirac_Tabelle` (DE + EN)
- `103_T0_Anomale-g2-6` (DE + EN)

## Workflow for Landscape-Fixed Documents

### Step 1: User Cleans Standalone Documents Locally

User modifies these 8 files locally:
- `de_standalone/018_T0_Anomale-g2-9_De.tex`
- `de_standalone/041_parameterherleitung_De.tex`
- `de_standalone/054_Elimination_Of_Mass_Dirac_Tabelle_De.tex`
- `de_standalone/103_T0_Anomale-g2-6_De.tex`
- `en_standalone/018_T0_Anomale-g2-9_En.tex`
- `en_standalone/041_parameterherleitung_En.tex`
- `en_standalone/054_Elimination_Of_Mass_Dirac_Tabelle_En.tex`
- `en_standalone/103_T0_Anomale-g2-6_En.tex`

**Changes made**:
- Remove `\begin{landscape}...\end{landscape}` environments
- Convert landscape tables to portrait mode using `\resizebox{\textwidth}{!}{...}`
- Adjust longtable column widths for portrait mode
- Keep all other content EXACTLY as is

### Step 2: Commit and Push Standalone Documents

```bash
git add 2/tex/de_standalone/018_T0_Anomale-g2-9_De.tex
git add 2/tex/de_standalone/041_parameterherleitung_De.tex
git add 2/tex/de_standalone/054_Elimination_Of_Mass_Dirac_Tabelle_De.tex
git add 2/tex/de_standalone/103_T0_Anomale-g2-6_De.tex
git add 2/tex/en_standalone/018_T0_Anomale-g2-9_En.tex
git add 2/tex/en_standalone/041_parameterherleitung_En.tex
git add 2/tex/en_standalone/054_Elimination_Of_Mass_Dirac_Tabelle_En.tex
git add 2/tex/en_standalone/103_T0_Anomale-g2-6_En.tex
git commit -m "Remove landscape from documents - Kindle compatibility"
git push origin <branch>
```

### Step 3: Generate Chapter Files

```bash
cd 2/tex
python generate_chapter_clean.py
```

This creates/updates 8 chapter files:
- `de_chapters_new/018_T0_Anomale-g2-9_De_ch.tex`
- `de_chapters_new/041_parameterherleitung_De_ch.tex`
- `de_chapters_new/054_Elimination_Of_Mass_Dirac_Tabelle_De_ch.tex`
- `de_chapters_new/103_T0_Anomale-g2-6_De_ch.tex`
- `en_chapters_new/018_T0_Anomale-g2-9_En_ch.tex`
- `en_chapters_new/041_parameterherleitung_En_ch.tex`
- `en_chapters_new/054_Elimination_Of_Mass_Dirac_Tabelle_En_ch.tex`
- `en_chapters_new/103_T0_Anomale-g2-6_En_ch.tex`

### Step 4: Fix Abstract Environments

**Problem**: The `\begin{abstract}...\end{abstract}` environment doesn't work in book class.

**Solution**: Convert to sections:
- German: Replace with `\section*{Zusammenfassung}`
- English: Replace with `\section*{Abstract}`

This is done automatically by post-processing the chapter files after generation.

### Step 5: Fix Unclosed Chapter Commands

**Problem**: Some `\chapter{` commands have unclosed braces due to complex titles.

**Solution**: Ensure all `\chapter{...}` commands have matching closing braces `}`.

### Step 6: Compile and Test

```bash
cd 2/tex/completed

# Test individual books
pdflatex -interaction=nonstopmode Teil1_De.tex
pdflatex -interaction=nonstopmode Teil1_De.tex
pdflatex -interaction=nonstopmode Teil1_De.tex

# Test all 6 books
for book in Teil1_De Teil2_De Teil3_De Teil1_En Teil2_En Teil3_En; do
  pdflatex -interaction=nonstopmode $book.tex
  pdflatex -interaction=nonstopmode $book.tex
  pdflatex -interaction=nonstopmode $book.tex
done

# Test standalone test books with landscape chapters
pdflatex -interaction=nonstopmode Test_Landscape_De.tex
pdflatex -interaction=nonstopmode Test_Landscape_En.tex
```

## Key Principles

### 1. EXACT Content Preservation

**Critical Rule**: The content between `\begin{document}` and `\end{document}` in the standalone file must be preserved EXACTLY in the chapter file, with only these exceptions:

- Add `\chapter{title}` at the beginning
- Remove `\maketitle` command (standalone-only)
- Remove `\tableofcontents` command (standalone-only)
- Convert `\begin{abstract}` to `\section*{Zusammenfassung}` or `\section*{Abstract}`

**Must NOT be modified**:
- `\resizebox` commands
- Table structures (`tabular`, `longtable`, `tabularx`)
- Column widths
- Any other LaTeX formatting

### 2. Title Extraction

Titles are extracted from standalone documents and cleaned:
```python
# Example title extraction
\title{\textbf{Vereinheitlichte Berechnung}\\[0.5cm]
  \large Vollständiger Beitrag\\[0.3cm]
  \normalsize Erweiterte Ableitung}

# Becomes chapter:
\chapter{Vereinheitlichte Berechnung}
```

### 3. Error Prevention

Common errors to avoid:
1. **Modifying table content** - Tables with `\resizebox` must be preserved exactly
2. **Removing too much** - Only remove `\maketitle` and `\tableofcontents`
3. **Unclosed braces** - Ensure `\chapter{...}` has closing `}`
4. **Abstract environment** - Must convert to section, not remove

## Directory Structure

```
2/tex/
├── de_standalone/          # German standalone documents
│   ├── 018_T0_Anomale-g2-9_De.tex
│   ├── 041_parameterherleitung_De.tex
│   └── ...
├── en_standalone/          # English standalone documents
│   ├── 018_T0_Anomale-g2-9_En.tex
│   └── ...
├── de_chapters_new/        # Generated German chapter files
│   ├── 018_T0_Anomale-g2-9_De_ch.tex
│   └── ...
├── en_chapters_new/        # Generated English chapter files
│   ├── 018_T0_Anomale-g2-9_En_ch.tex
│   └── ...
├── completed/              # Book compilation directory
│   ├── Teil1_De.tex       # Book 1 German
│   ├── Teil1_En.tex       # Book 1 English
│   ├── Teil2_De.tex       # Book 2 German
│   ├── Teil2_En.tex       # Book 2 English
│   ├── Teil3_De.tex       # Book 3 German
│   ├── Teil3_En.tex       # Book 3 English
│   ├── Test_Landscape_De.tex  # Test book with landscape chapters
│   └── Test_Landscape_En.tex  # Test book with landscape chapters
├── generate_chapter_exact.py   # Main generation script
├── generate_chapter_clean.py   # Cleanup generation script
└── README_CHAPTER_GENERATION.md  # This file
```

## Verification

After generating chapter files, verify:

1. **Content preservation**: Compare content between standalone and chapter files
2. **Resizebox intact**: Check that all `\resizebox{\textwidth}{!}{...}` are present
3. **Table structures**: Verify longtable column specifications are unchanged
4. **Compilation**: Books must compile with 0 errors

```bash
# Verify a specific chapter file
diff <(sed -n '/\\begin{document}/,/\\end{document}/p' de_standalone/018_T0_Anomale-g2-9_De.tex) \
     <(tail -n +5 de_chapters_new/018_T0_Anomale-g2-9_De_ch.tex | head -n -1)
```

## Troubleshooting

### Issue: "File ended while scanning use of \@xdblarg"

**Cause**: Unclosed `\chapter{` command

**Solution**: Check for missing `}` in chapter title
```latex
% Wrong:
\chapter{Title with {nested braces}

% Correct:
\chapter{Title with {nested braces}}
```

### Issue: "Abstract environment not defined"

**Cause**: Using `\begin{abstract}` in book class

**Solution**: Replace with section:
```latex
% Wrong:
\begin{abstract}
Text here
\end{abstract}

% Correct (German):
\section*{Zusammenfassung}
Text here

% Correct (English):
\section*{Abstract}
Text here
```

### Issue: Tables overflow page

**Cause**: Landscape tables not converted or resizebox removed

**Solution**: Ensure `\resizebox{\textwidth}{!}{...}` wraps tables

### Issue: "Extra alignment tab has been changed to \cr"

**Cause**: Too many column separators (`&`) in table

**Solution**: Check table column specification matches number of `&` separators

## Version History

- **v66-v67**: Fixed abstract environments, unclosed chapter commands, integrated all landscape chapters into main books
- **v62**: Added `generate_chapter_clean.py` to remove `\maketitle` and `\tableofcontents`
- **v60**: Created `generate_chapter_exact.py` for exact content preservation
- **v55-v56**: Initial chapter file generation with user's landscape-cleaned documents

## Contact

For issues or questions about chapter generation, refer to the main PR discussion:
- PR: "Add GitHub Action to build LaTeX documents, standardize preambles, generate PDFs"
- Repository: jpascher/T0-Time-Mass-Duality
