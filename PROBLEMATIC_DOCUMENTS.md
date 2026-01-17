# Problematic LaTeX Documents

These 2 documents have issues that cannot be fixed in the shared preambles and require manual content changes:

## 1. 065_redshift_deflection_En.tex
**Location:** `2/tex-n/en_standalone/065_redshift_deflection_En.tex`

**Issues:**
- Uses `\documentclass{article}` but contains `\chapter` command (line 22)
- `\chapter` is only available in `book` and `report` document classes
- Contains undefined command `\xiconst` (line 29)

**Possible fixes:**
1. Change `\documentclass{article}` to `\documentclass{report}` OR
2. Change `\chapter{...}` to `\section{...}` OR  
3. Define `\xiconst` command in the document or preamble

## 2. 075_RSA_En.tex  
**Location:** `2/tex-n/en_standalone/075_RSA_En.tex`

**Issues:**
- Contains PDF bookmark errors with `\mitepsilon` and `\mitmu` symbols (line 258)
- These symbols are already defined in the preamble, but may be used incorrectly in the document

**Possible fix:**
- Check usage of `\mitepsilon` and `\mitmu` around line 258
- May need to wrap in proper math mode or adjust bookmark generation

---

**Note:** These issues require changes to the document content itself, which is outside the scope of preamble-only fixes.
