# DVFT Chapters - Markdown to LaTeX Compilation

This directory contains Markdown source files for the Dynamic Vacuum Field Theory (DVFT) chapters and a compilation script to convert them to LaTeX and generate PDFs.

## Contents

- `00_Vorspann.md` - `Kapitel_43.md`: Source Markdown files (44 chapters total)
- `compile_dvft_full.sh`: Compilation script that converts Markdown to LaTeX and generates PDFs
- Generated `.tex` files: LaTeX versions of each chapter (auto-generated)
- `main.tex`: Master document that includes all chapters (auto-generated)

## Requirements

Before running the compilation script, ensure you have the following LaTeX packages installed:

### Ubuntu/Debian:
```bash
sudo apt-get install texlive-latex-base texlive-latex-extra \
                     texlive-fonts-recommended texlive-lang-german \
                     texlive-science texlive-pictures
```

### Fedora/RHEL:
```bash
sudo dnf install texlive-scheme-medium texlive-babel-german \
                 texlive-physics texlive-pgfplots
```

## Usage

### Compile All Chapters

To convert all Markdown files to LaTeX and compile them to PDF:

```bash
./compile_dvft_full.sh
```

The script will:
1. Convert all 44 Markdown chapters to LaTeX format
2. Apply physics notation conversions (φ → \varphi, ρ → \rho, θ → \theta, etc.)
3. Create a `main.tex` file that includes all chapters
4. Compile each chapter individually
5. Compile the main document 3 times (for cross-references)
6. Log all output and errors

### Output Files

After successful compilation, you'll find:
- `kapitel_00.pdf` through `kapitel_43.pdf`: Individual chapter PDFs
- `main.pdf`: Combined PDF with all chapters
- `compilation.log`: Detailed compilation log
- `errors.log`: Error messages (if any)

### What the Script Does

1. **Markdown to LaTeX Conversion:**
   - Converts headers (`#`, `##`, `###`) to LaTeX sections
   - Converts Greek letters and mathematical symbols to LaTeX commands
   - Escapes special LaTeX characters
   - Uses the shared T0 preamble for consistent formatting

2. **Error Handling:**
   - Automatically retries compilation up to 5 times
   - Attempts to fix common LaTeX errors
   - Logs all errors for review

3. **Structure:**
   - Each chapter is a standalone document
   - Content is also extracted for inclusion in the master document
   - The master document uses the book class for better chapter organization

## Troubleshooting

### Compilation Fails

Check the error log:
```bash
cat errors.log
```

Common issues:
- Missing LaTeX packages: Install required packages as listed above
- File permission issues: Ensure the script is executable (`chmod +x compile_dvft_full.sh`)
- Preamble not found: The script expects `T0_preamble_shared_De.tex` at `../../../../T0_preamble_shared_De.tex`

### Clean Up Generated Files

To remove all generated files and start fresh:
```bash
rm -f kapitel_*.tex kapitel_*.pdf kapitel_*_content.tex \
      main.tex main.pdf *.log *.aux *.out *.toc
```

## Customization

### Modify Conversion Rules

Edit the `convert_md_to_tex()` function in `compile_dvft_full.sh` to adjust:
- Greek letter mappings
- Mathematical symbol conversions
- Special character escaping

### Change Compilation Options

Edit the `compile_tex()` function to modify pdflatex options or retry behavior.

## Notes

- The conversion is optimized for the DVFT chapter format
- Some complex mathematical expressions may need manual adjustment
- The script is designed to be idempotent - you can run it multiple times safely
- Generated files (.tex, .pdf, logs) are excluded from version control

## Author

Johann Pascher / GitHub Copilot  
Date: 2025-12-28
