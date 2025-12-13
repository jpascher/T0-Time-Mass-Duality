# Copilot Instructions for LaTeX Table Overflow Fixes

## Workflow Decision - Final and Binding

**User Decision (2025-12-13):** Proceed with systematic recursive table overflow fixes WITHOUT asking for confirmation or clarification.

## Systematic Recursive Workflow

### 1. Environment Setup
- **LaTeX Installation**: Use `sudo apt-get install` for minimal configuration
- **Required Packages**:
  - `texlive-latex-base`
  - `texlive-latex-extra`
  - `texlive-fonts-recommended`
  - `texlive-science` (physics package)
  - `texlive-lang-german` (ngerman support)
- **Compilation Tool**: `pdflatex` (3 passes per document)

### 2. Phase 1: Standalone Documents
**Fix ALL standalone documents FIRST before touching chapter files or books**

1. Compile each standalone individually: `pdflatex standalone.tex`
2. Capture and analyze Overfull \hbox warnings
3. Fix tables that overflow (convert to list format if >10pt overfull)
4. Recompile to verify fix
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

1. Compile book: `pdflatex BookName.tex` (3 passes)
2. Analyze Overfull \hbox warnings
3. If warnings exist:
   - Identify problematic chapter
   - Fix in chapter file (NOT standalone - standalone is already clean)
   - Recompile book
   - Repeat until zero warnings
4. Move to next book

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

1. ✅ ALL standalone documents compile with ZERO Overfull warnings
2. ✅ ALL chapter files generated from clean standalones
3. ✅ ALL 8 books compile with ZERO Overfull warnings
4. ✅ Books maintain KDP compliance (fonts ≥7pt, no overflow)
5. ✅ Expected page increase: +5-10% per book (acceptable)

---

**Last Updated**: 2025-12-13 by @copilot
**User Directive**: Execute without interruption, no questions
