# DVFT Chapter Comparison Tool

## Purpose

This tool compares two versions of DVFT (Dynamic Vacuum Field Theory) chapters to identify differences in theoretical content, particularly focusing on mathematical equations and derivations.

## Usage

```bash
python3 compare_dvft_chapters.py
```

The script will:
1. Compare individual chapter files (`tex_DVFT_T0/kapitel_XX.tex`) with merged chapter files (`202_XX-YY_De.tex`)
2. Extract and compare equations from both versions
3. Calculate similarity metrics
4. Generate a detailed report showing differences

## Output

The tool produces a console report showing:
- Similarity percentage for each chapter
- Number of equations in each version
- List of equations missing from either version
- Categorization of differences (critical, moderate, minor)
- Summary statistics

## Files Analyzed

### Individual Chapters
- **Location:** `2/tex-n/de_DVFT/tex_DVFT_T0/`
- **Files:** `kapitel_01.tex` through `kapitel_44.tex`
- **Characteristics:** Detailed mathematical derivations, complete proofs, technical presentations

### Merged Chapters
- **Location:** `2/tex-n/de_DVFT/`
- **Files:** 
  - `202_12-15_De.tex` (Chapters 12-15)
  - `202_16-19_De.tex` (Chapters 16-19)
  - `202_20-32_De.tex` (Chapters 20-32)
  - `202_33-43_De.tex` (Chapters 33-43)
  - `202_43-44_De.tex` (Chapters 43-44)
- **Characteristics:** Narrative summaries, conceptual explanations, philosophical emphasis

## Methodology

1. **Text Extraction:** Reads LaTeX files and extracts content
2. **Equation Detection:** Identifies equations using regex patterns for:
   - `\begin{equation}...\end{equation}`
   - `\[...\]` display math
3. **Normalization:** Removes whitespace variations for comparison
4. **Similarity Calculation:** Uses SequenceMatcher for text similarity
5. **Equation Matching:** Checks if equations from one version appear in the other

## Similarity Thresholds

- **Critical:** < 50% similarity - Major differences in content
- **Moderate:** 50-80% similarity - Noticeable differences
- **Minor:** 80-95% similarity - Small differences
- **Perfect:** > 95% similarity - Nearly identical

## Reports Generated

After running the script, review:
- **DVFT_CHAPTER_COMPARISON_REPORT.md** - Detailed English report
- **DVFT_KAPITELVERGLEICH_ZUSAMMENFASSUNG_DE.md** - German summary

## Key Findings

The analysis revealed that:
1. Individual chapters contain detailed mathematical content (5-22 equations per chapter)
2. Merged chapters contain narrative summaries (0-3 equations per chapter)
3. Both versions are theoretically consistent
4. No contradictory claims were found
5. The versions serve different audiences (technical vs. general)

## Dependencies

- Python 3.6+
- Standard library only (no external packages required):
  - `os`, `re`, `pathlib`, `difflib`

## Maintenance

To update or extend the tool:
1. Modify equation pattern matching in `extract_equations_from_text()`
2. Adjust similarity thresholds in the main analysis loop
3. Add new comparison metrics as needed

## Author

Created as part of the T0-Time-Mass-Duality repository analysis (2025-12-29)

## License

Same as parent repository
