# Kindle/KDP Optimization Guide for FFGFT Narrative

## Overview
This guide provides detailed instructions for creating Kindle Direct Publishing (KDP) compliant LaTeX documents for the FFGFT Narrative series.

## Document Structure

### Preamble Template
The standard Kindle-optimized preamble should include:
- Document class: `\documentclass[12pt,a4paper]{article}`
- Geometry: 6in x 9in paper with specific margins
- Text wrapping optimization settings
- Math display optimization
- Custom units for siunitx

### Page Layout
- Paper size: 6in x 9in (Kindle standard)
- Inner margin: 0.625in
- Outer margin: 0.625in
- Top margin: 0.625in
- Bottom margin: 1.0in
- Two-sided layout

## KDP Compliance Rules

### 1. Text Overflow Prevention
**Critical**: No overfull or underfull `\hbox` warnings that extend beyond page margins.

**Solutions**:
- Long section titles: Break with `\\`
- Long formulas: Use `align*`, `split`, or `\allowbreak`
- Set text wrapping parameters:
  ```latex
  \sloppy
  \emergencystretch=3em
  \hyphenpenalty=500
  \tolerance=2000
  \hbadness=2000
  ```

### 2. Table Optimization
**Rule**: All tables must fit within text width.

**Solution**: Wrap oversized tables with `\resizebox`:
```latex
\resizebox{\textwidth}{!}{
  \begin{tabular}{...}
  ...
  \end{tabular}
}
```

### 3. Font Size Requirements
**Critical**: All text, including math, must be ≥7pt for KDP approval.

**Implementation**:
```latex
\DeclareMathSizes{11}{11}{9}{8}
\DeclareMathSizes{10.95}{11}{9}{8}
```

**Never** use local font size overrides that create text smaller than 7pt.

### 4. Math Display Optimization
```latex
\everymath{\displaystyle}
\everydisplay{\displaystyle}
\relpenalty=10
\binoppenalty=10
```

### 5. Hyperref Configuration
- Avoid `\\` in section titles for PDF bookmarks
- Use optional shorter titles: `\section[Short]{Long Title \\ with Break}`

## Compilation Process

### Required Passes
Compile **4 times** to ensure:
1. First pass: Process content
2. Second pass: Resolve references
3. Third pass: Stabilize TOC
4. Fourth pass: Final PDF with stable bookmarks

### Command
```bash
for i in {1..4}; do
  sudo pdflatex -interaction=nonstopmode Kapitel_XXa_Narrative_En.tex
done
```

### Log File Review
After compilation, check `.log` file for:
- [ ] Overfull/underfull boxes
- [ ] Font size warnings (<7pt)
- [ ] Hyperref warnings
- [ ] Missing references
- [ ] Package warnings

**Action**: Fix all layout-critical warnings before considering chapter complete.

## Translation Guidelines

### Manual Translation Required
- **DO**: Manually translate all narrative text, section titles, captions
- **DON'T**: Use automated translation tools
- **PRESERVE**: All mathematical formulas, symbols, labels, and references unchanged

### Content to Translate
- Document title and subtitle
- Section headings
- Narrative introductions and conclusions
- Figure and table captions
- Explanatory text around equations

### Content to Keep Unchanged
- Equation numbers and labels
- Mathematical symbols and expressions
- Cross-references (`\ref`, `\label`)
- Citation keys

## Quality Checklist

Before committing a chapter:
- [ ] Compiled successfully 4 times without errors
- [ ] No overfull boxes exceeding page margins
- [ ] All tables fit within text width
- [ ] No font sizes below 7pt
- [ ] Hyperref warnings resolved
- [ ] Translation is accurate and natural English
- [ ] Mathematical content unchanged from German source

## TODO
- Add specific examples of problematic cases and their solutions
- Include before/after screenshots of common fixes
- Document special cases for complex mathematical expressions
- Add section on handling figures and graphics
