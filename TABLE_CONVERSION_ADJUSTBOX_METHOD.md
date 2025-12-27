# Table Conversion: Adjustbox Method (VERIFIED & PROVEN)

**Status:** Successfully tested on file 018_T0_Anomale-g2-9_De.tex (29→0 Overfull warnings)

**Date:** 2025-12-13

## Method Overview

This method converts wide tables that cause Overfull warnings by:
1. Wrapping tables in `\begin{adjustbox}{max width=\textwidth}`
2. Using percentage-based column widths (`p{0.XX\textwidth}`)
3. Adding proper spacing between columns (`@{\hspace{2mm}}`)
4. Ensuring automatic text wrapping within cells

## Why This Works

- **adjustbox**: Scales table ONLY if it exceeds \textwidth (rarely needed with correct percentages)
- **p{0.XX\textwidth}**: Columns are flexible, adjust to page width, paragraph type = automatic wrapping
- **@{\hspace{2mm}}**: Prevents column overlap, adds clean visual separation
- **Total < 100%**: Leave 4-8% for spacing, prevents overflow

## Step-by-Step Conversion

### 1. Identify Tables to Convert

Compile with pdflatex and check for Overfull warnings:
```bash
pdflatex -interaction=nonstopmode file.tex 2>&1 | grep "Overfull"
```

### 2. Wrap Table in adjustbox

**Before:**
```latex
\begin{table}[htbp]
\centering
\begin{tabular}{|l|c|c|c|}
...
\end{tabular}
\caption{Caption}
\end{table}
```

**After:**
```latex
\begin{table}[htbp]
\centering
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{@{} p{0.25\textwidth} @{\hspace{2mm}} p{0.25\textwidth} @{\hspace{2mm}} p{0.25\textwidth} @{\hspace{2mm}} p{0.15\textwidth} @{}}
...
\end{tabular}
\end{adjustbox}
\caption{Caption}
\label{tab:label}
\end{table}
```

### 3. Calculate Column Widths

**Formula:** Total columns × desired_width + (columns-1) × spacing ≤ 0.96

**Examples:**
- **3 columns:** 0.30 + 0.30 + 0.30 = 0.90 (6% for spacing)
- **4 columns:** 0.22 + 0.22 + 0.22 + 0.22 = 0.88 (12% for spacing)
- **5 columns:** 0.18 + 0.18 + 0.18 + 0.18 + 0.18 = 0.90 (10% for spacing)
- **6 columns:** 0.15 + 0.15 + 0.15 + 0.15 + 0.15 + 0.15 = 0.90 (10% for spacing)
- **7 columns:** 0.12 + 0.12 + 0.12 + 0.12 + 0.15 + 0.15 + 0.15 = 0.93 (7% for spacing)

**Adjust widths based on content:**
- Narrow columns (indices, numbers): 0.10-0.12
- Medium columns (short text): 0.15-0.20
- Wide columns (long descriptions): 0.25-0.30

### 4. Add Column Spacing

Insert `@{\hspace{2mm}}` between each column:
```latex
p{0.15\textwidth} @{\hspace{2mm}} p{0.20\textwidth} @{\hspace{2mm}} p{0.25\textwidth}
```

**Remove edge padding** with `@{}`:
```latex
@{} p{0.15\textwidth} ... p{0.25\textwidth} @{}
```

### 5. Test Compilation

**CRITICAL:** Test after EVERY table conversion:
```bash
cd /path/to/standalone
pdflatex -interaction=nonstopmode filename.tex
grep "Overfull" filename.log
grep "^!" filename.log
```

**Expected result:**
- ✅ 0 compilation errors
- ✅ 0 Overfull warnings (or significantly reduced)
- ✅ PDF generated successfully

## Complete Examples

### Example 1: 6-Column Comparison Table (File 018, Table 2)

**Before (203pt overflow):**
```latex
\begin{tabular}{|p{1.2cm}|p{2.5cm}|p{1.4cm}|p{2.8cm}|p{3.0cm}|p{2.0cm}|}
\hline
Lepton & Perspektive & T0-Wert & SM-Wert & Total/Exp. & Abweichung \\
\hline
Elektron (e) & Hybrid (Pre-2025) & 0.0036 & 115965218.046(18) & 115965218.046 & 0 $\sigma$ \\
\hline
\end{tabular}
```

**After (0 overflow):**
```latex
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{@{} p{0.11\textwidth} @{\hspace{2mm}} p{0.17\textwidth} @{\hspace{2mm}} p{0.11\textwidth} @{\hspace{2mm}} p{0.19\textwidth} @{\hspace{2mm}} p{0.19\textwidth} @{\hspace{2mm}} p{0.15\textwidth} @{}}
\toprule
Lepton & Perspektive & T0-Wert ($\times 10^{-11}$) & SM-Wert (Beitrag, $\times 10^{-11}$) & Total/Exp.-Wert ($\times 10^{-11}$) & Abweichung ($\sigma$) \\
\midrule
Elektron (e) & Hybrid (additiv zu SM) (Pre-2025) & 0.0036 & 115965218.046(18) (QED-dom.) & 115965218.046 $\approx$ Exp. 115965218.046(18) & 0 $\sigma$ \\
\bottomrule
\end{tabular}
\end{adjustbox}
```

**Widths:** 0.11 + 0.17 + 0.11 + 0.19 + 0.19 + 0.15 = 0.92 (8% for spacing)

### Example 2: 7-Column Data Table (File 018, Table 3)

**Before (large overflow):**
```latex
\begin{tabular}{|c|c|c|c|c|c|c|}
\hline
Lepton & Perspective & T0 & SM(QED) & SM(Weak) & SM(Had) & Total \\
\hline
...
\end{tabular}
```

**After (0 overflow):**
```latex
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{@{} p{0.11\textwidth} @{\hspace{2mm}} p{0.11\textwidth} @{\hspace{2mm}} p{0.11\textwidth} @{\hspace{2mm}} p{0.18\textwidth} @{\hspace{2mm}} p{0.18\textwidth} @{\hspace{2mm}} p{0.12\textwidth} @{\hspace{2mm}} p{0.15\textwidth} @{}}
\toprule
Lepton & Perspektive & T0-Beitrag & SM (QED) & SM (Weak) & SM (Hadronic) & Total \\
\midrule
...
\bottomrule
\end{tabular}
\end{adjustbox}
```

**Widths:** 0.11 + 0.11 + 0.11 + 0.18 + 0.18 + 0.12 + 0.15 = 0.96 (4% for spacing)

## Required Packages

Ensure preamble includes:
```latex
\usepackage{adjustbox}  % For max width wrapping
\usepackage{array}      % Enhanced column types
\usepackage{booktabs}   % For \toprule, \midrule, \bottomrule
\usepackage{tabularx}   % Optional: for X columns
```

**Note:** All packages already present in T0_preamble_shared_De.tex and T0_preamble_shared_En.tex (verified 2025-12-13)

## Common Issues & Solutions

### Issue 1: Columns Still Overlap
**Solution:** Increase `@{\hspace{2mm}}` to `@{\hspace{3mm}}` or `@{\hspace{4mm}}`

### Issue 2: Table Still Overflows
**Solution:** Reduce column widths by 1-2%, ensure total ≤ 0.94

### Issue 3: Text Not Wrapping
**Solution:** Ensure using `p{}` not `l`, `c`, or `r` columns

### Issue 4: Compilation Errors
**Solution:** Check:
- adjustbox correctly closed: `\end{adjustbox}` before `\end{table}`
- All column separators present: `&` between columns
- Proper escaping of special characters

## Testing Checklist

After converting each table:
- [ ] Compile with pdflatex (3 passes)
- [ ] Check log for errors: `grep "^!" file.log`
- [ ] Check log for Overfull: `grep "Overfull" file.log`
- [ ] Verify PDF generated
- [ ] Visually inspect table in PDF:
  - [ ] No overlapping columns
  - [ ] Text wraps within cells
  - [ ] Clean spacing between columns
  - [ ] All content visible and readable

## Workflow for 37 Files

1. **Compile file** to identify Overfull warnings
2. **Identify tables** causing overflows (check line numbers from warnings)
3. **Convert tables** one by one using adjustbox method
4. **Test after EACH table conversion** (not after all tables)
5. **Commit when file is clean** (0 errors, 0 Overfull warnings)
6. **Move to next file**
7. **Report progress** after each file completion

**DO NOT:**
- Skip compilation testing
- Convert multiple files without testing
- Continue if compilation errors occur
- Proceed to next file before current file is clean

## Success Criteria

**Per File:**
- ✅ 0 compilation errors
- ✅ 0 Overfull warnings (or acceptable: <5pt, <3 warnings)
- ✅ PDF generated successfully
- ✅ Visual inspection confirms readability

**Overall (37 Files):**
- ✅ All files compile cleanly
- ✅ Significant reduction in total Overfull warnings
- ✅ All tables fit within page margins
- ✅ Ready for Phase 2 (chapter generation)
