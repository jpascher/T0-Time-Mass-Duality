# LaTeX Compilation Status

## Current Status (2026-02-05)

### Summary
- **Total LaTeX documents found**: 600 files with `\documentclass`
- **Successfully compiled**: 251 documents (41.8%)
- **Failed compilation**: 209 documents (34.8%)
- **Not yet attempted**: 140 documents (23.3%)
- **PDFs generated**: 255 in `2/pdf/`

### Infrastructure
✅ Complete LaTeX environment installed (texlive-luatex, latexmk, fonts)
✅ Compilation script created: `compile_all.sh`
✅ Error tracking files: `tex_compile_errors.txt`, `tex_compile_success.txt`

### Successful Compilations
- All main books: Teil1, Teil2, Teil3 (DE/EN, ebook/normal formats)
- T0 Anwendungen books (DE/EN)
- Xi Narrative Masters (DE/EN, ebook/normal)
- Many FFGFT chapter documents
- Most standalone documents in `2/tex-n/de_standalone` and `2/tex-n/en_standalone`

### Known Issues

#### 1. Standalone Chapters (152 de_standalone, 49 en_standalone failures)
Main issue: Article class documents using `\counterwithout{section}{chapter}` without chapter counter.
**Status**: Preamble fix applied in `T0_preamble_shared_De.tex` and `T0_preamble_shared_En.tex`
- Changed to: `\@ifundefined{c@chapter}{}{\counterwithout{section}{chapter}}`

#### 2. Narrative Master Documents (3 failures)
- `FFGFT_Narrative_Master_De.tex`
- `FFGFT_Narrative_Master_En.tex`
- `FFGFT_Xi_Narrative_Master_De.tex`

#### 3. Missing Dependencies
Some documents reference files that don't exist (e.g., xi_de_chapters/)

### Next Steps for Full Compilation

1. **Recompile with preamble fix**: Run `./compile_all.sh` again
2. **Analyze remaining errors**: Check `.log` files in source directories
3. **Fix categories**:
   - Missing include files
   - Encoding issues
   - Broken LaTeX environments
   - Undefined control sequences
4. **Iterative correction**: Fix minimal LaTeX errors until all 600 documents compile

### g-2 Content Policy
✅ Detailed g-2 formulas and numerical predictions must only appear in:
- `018_T0_Anomale-g2-10_De.tex`
- `018_T0_Anomale-g2-10_En.tex`

Other documents may mention g-2 qualitatively or reference these documents.

### Commands

```bash
# Recompile all documents
./compile_all.sh

# Check status
wc -l tex_compile_success.txt tex_compile_errors.txt
ls -1 2/pdf/*.pdf | wc -l

# View first errors
head -20 tex_compile_errors.txt

# Compile single file (from source directory)
cd 2/narrative/de_standalone
latexmk -lualatex -interaction=nonstopmode -halt-on-error Kapitel_01a_Narrative_De.tex
```

## File Locations

- **Source files**: `2/tex-n/`, `2/narrative/`
- **PDF output**: `2/pdf/`
- **Tracking files**: Root directory
  - `tex_master_files.txt` - All 600 source files
  - `tex_compile_success.txt` - Successfully compiled
  - `tex_compile_errors.txt` - Failed compilations
  - `tex_documentclass_files.txt` - Raw find results
