# Copilot Instructions for LaTeX Table Overflow Fixes

## Workflow Decision - Final and Binding

**User Decision (2025-12-13):** Proceed with systematic recursive table overflow fixes WITHOUT asking for confirmation or clarification.

## Systematic Recursive Workflow

### 1. Environment Setup

**CRITICAL: Always verify LaTeX installation BEFORE any compilation**

```bash
# Check if pdflatex is installed
if ! command -v pdflatex &> /dev/null; then
    echo "Installing LaTeX environment..."
    sudo apt-get update
    sudo apt-get install -y texlive-latex-base texlive-latex-extra \
                           texlive-fonts-recommended texlive-science \
                           texlive-lang-german
else
    echo "LaTeX already installed: $(pdflatex --version | head -1)"
fi
```

- **LaTeX Installation**: Use `sudo apt-get install` for minimal configuration
- **Required Packages**:
  - `texlive-latex-base`
  - `texlive-latex-extra`
  - `texlive-fonts-recommended`
  - `texlive-science` (physics package)
  - `texlive-lang-german` (ngerman support)
- **Compilation Tool**: `pdflatex` (3 passes per document)
- **Installation Verification**: MUST verify pdflatex is available before first compilation

### 2. Phase 1: Standalone Documents
**Fix ALL standalone documents FIRST before touching chapter files or books**

**RECURSIVE & ITERATIVE COMPILATION MANDATORY:**
- Compile each document
- Check for Overfull/Underfull warnings and errors
- Fix identified issues
- **RECOMPILE until ZERO warnings and ZERO errors**
- Only then move to next document

**Compilation Loop:**
```bash
while true; do
    pdflatex -interaction=nonstopmode document.tex 2>&1 | tee compile.log
    
    # Check if compile.log is empty - don't proceed if no output was captured
    if [ ! -s compile.log ]; then
        echo "✗ ERROR: Compilation produced no output (empty log)"
        echo "  This likely means compilation failed completely or document.tex is missing"
        exit 1
    fi
    
    WARNINGS=$(grep -c "Overfull\|Underfull" compile.log)
    ERRORS=$(grep -c "^!" compile.log)
    
    if [ $WARNINGS -eq 0 ] && [ $ERRORS -eq 0 ]; then
        echo "✓ Clean compilation - proceeding to next"
        break
    else
        echo "⚠ Found $WARNINGS warnings, $ERRORS errors - fixing..."
        # Apply fixes
        # Continue loop
    fi
done
```

1. Compile each standalone individually: `pdflatex standalone.tex`
2. Capture and analyze Overfull \hbox warnings
3. Fix tables that overflow (convert to list format if >10pt overfull)
4. **Recompile iteratively until compilation is clean (0 warnings, 0 errors)**
5. Move to next standalone
6. **Do not proceed to Phase 2 until ALL standalone warnings are eliminated**

**Standalone Priority:**
- Start with German files (de_standalone/)
- Then English files (en_standalone/)
- Focus on files with removed \resizebox first (86 files known to have issues)

### 3. Phase 2: Generate Chapter Files
**Only after ALL standalones are clean**

1. Use existing script: `generate_chapters_complete.py`
2. Generate chapter files from clean standalone versions
3. Script handles:
   - `\begin{abstract}` → `\section*{Abstract/Zusammenfassung}`
   - Removes `\maketitle` and `\tableofcontents`
   - Removes `\appendix` commands
   - Preserves all content

### 4. Phase 3: Compile Books Iteratively
**Recursive process for each book**

**RECURSIVE & ITERATIVE COMPILATION MANDATORY:**

```bash
BOOK="BookName.tex"
MAX_ITERATIONS=10
iteration=0

while [ $iteration -lt $MAX_ITERATIONS ]; do
    echo "=== Iteration $((iteration+1)) for $BOOK ==="
    
    # Compile 3 passes
    for pass in 1 2 3; do
        pdflatex -interaction=nonstopmode "$BOOK" > /tmp/compile_pass${pass}.log 2>&1
    done
    
    # Check if compilation log is empty - don't proceed if no output
    if [ ! -s /tmp/compile_pass3.log ]; then
        echo "✗ ERROR: $BOOK compilation produced no output (empty log)"
        echo "  This likely means compilation failed completely or $BOOK is missing"
        exit 1
    fi
    
    # Check for warnings and errors
    WARNINGS=$(grep -c "Overfull\|Underfull" /tmp/compile_pass3.log)
    ERRORS=$(grep -c "^!" /tmp/compile_pass3.log)
    
    if [ $WARNINGS -eq 0 ] && [ $ERRORS -eq 0 ]; then
        echo "✓ $BOOK: Clean compilation achieved!"
        break
    else
        echo "⚠ $BOOK: $WARNINGS warnings, $ERRORS errors found"
        # Identify and fix problematic chapter
        # Continue loop
        iteration=$((iteration+1))
    fi
done
```

1. Compile book: `pdflatex BookName.tex` (3 passes)
2. Analyze Overfull \hbox warnings and errors
3. If warnings/errors exist:
   - Identify problematic chapter
   - Fix in chapter file (NOT standalone - standalone is already clean)
   - **Recompile book iteratively**
   - **Repeat until ZERO warnings and ZERO errors**
4. Only move to next book when current book is completely clean

**Book Compilation Order:**
1. Teil1_De.tex
2. Teil1_En.tex
3. Teil2_De.tex
4. Teil2_En.tex
5. Teil3_De.tex
6. Teil3_En.tex
7. T0_Anwendungen_De.tex (Kindle German)
8. T0_Applications_En.tex (Kindle English)

### 5. Table Overflow Fix Strategy

**Criteria for Fixing:**
- **CRITICAL** (>150pt overflow): Fix immediately
- **MAJOR** (100-150pt): Fix in same pass
- **IMPORTANT** (50-100pt): Fix systematically
- **MODERATE** (20-50pt): Fix if time permits
- **MINOR** (<20pt): Acceptable, may ignore

**Conversion Method: Table → List**
```latex
% BEFORE (table)
\begin{table}
\begin{tabular}{lll}
Column1 & Column2 & Column3 \\
Data1 & Data2 & Data3 \\
\end{tabular}
\end{table}

% AFTER (list format)
\noindent\textbf{Column1:}
\begin{itemize}
\item \textbf{Column1}: Data1
\item \textbf{Column2}: Data2  
\item \textbf{Column3}: Data3
\end{itemize}
\vspace{1em}
```

### 6. Error Handling

**If compilation fails:**
1. Read error message carefully
2. Fix structural errors first (missing \end{}, etc.)
3. Regenerate chapter from standalone if severely broken
4. Document fix in commit message

**If warning persists after fix:**
1. Verify fix was applied correctly
2. Check for other tables in same file
3. Consider different formatting approach
4. Document unsuccessful attempts

### 7. Progress Tracking

**Use report_progress after:**
- Every 10 standalone files fixed
- Each chapter generation batch
- Each book successfully compiled with zero warnings
- Any significant milestone

**Commit Message Format:**
```
Phase X: [Stage] - [Number] files fixed, [Status]

Details:
- Files fixed: list
- Warnings eliminated: count
- Remaining work: description
```

### 8. Documentation Requirements

**DO NOT:**
- Ask for user confirmation before proceeding
- Request clarification on workflow
- Stop for minor issues
- Create extensive documentation during work

**DO:**
- Execute systematically as described above
- Fix issues as encountered
- Report progress regularly
- Document only major changes

## Current Status Snapshot

- **Standalone Files**: 204 total (103 DE + 101 EN)
- **Books**: 8 total (6 main + 2 Kindle)
- **Known Issues**: ~20+ table overflows in Teil1_De alone
- **Estimated Total**: 100-200 tables across all books
- **Expected Duration**: 8-12 hours of systematic work

## Success Criteria

1. ✅ LaTeX environment verified/installed BEFORE any compilation
2. ✅ ALL standalone documents compile with ZERO Overfull warnings and ZERO errors (recursive/iterative)
3. ✅ ALL chapter files generated from clean standalones
4. ✅ ALL 8 books compile with ZERO Overfull warnings and ZERO errors (recursive/iterative)
5. ✅ Books maintain KDP compliance (fonts ≥7pt, no overflow)
6. ✅ Expected page increase: +5-10% per book (acceptable)

**CRITICAL: Recursive and iterative compilation is MANDATORY**
- Each document MUST be recompiled until clean (0 warnings, 0 errors)
- NO proceeding to next phase/document while warnings/errors exist
- Maximum iterations per document: 10 (if not clean after 10, escalate)

---

**Last Updated**: 2025-12-13 by @copilot
**User Directive**: Execute without interruption, no questions
