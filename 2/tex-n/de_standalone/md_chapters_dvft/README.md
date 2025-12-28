# DVFT Chapter Compilation

This directory contains Markdown source files for the Dynamic Vacuum Field Theory (DVFT) chapters and a comprehensive compilation script.

## Files

- `00_Vorspann.md` - Preface chapter
- `Kapitel_01.md` to `Kapitel_43.md` - Main chapters (1-43)
- `compile_all_dvft_final.sh` - Automated conversion and compilation script

## Script: compile_all_dvft_final.sh

This script automates the conversion of Markdown files to LaTeX format and compiles them to PDF documents.

### Features

1. **Markdown to LaTeX Conversion**
   - Converts all Markdown files to LaTeX format
   - Handles physical notation (φ→\varphi, ρ→\rho, θ→\theta, and many more Unicode symbols)
   - Preserves document structure and formatting
   - Creates proper \section{} headers

2. **Dual Output Format**
   - **Input files** (`kapitel_XX.tex`): Designed to be included in main.tex via \input
   - **Standalone files** (`kapitel_XX_standalone.tex`): Complete documents that can be compiled individually

3. **Main Document**
   - Generates `main.tex` that includes all chapters in order
   - Includes table of contents
   - Uses book document class for proper chapter formatting

4. **Compilation**
   - Compiles with pdflatex (up to 3 passes per file for cross-references)
   - Automatically fixes common LaTeX errors
   - Continues processing even if some files fail

5. **Logging**
   - Detailed logs in `compilation.log`
   - Error-specific logs in `compilation_errors.log`
   - Color-coded console output for easy monitoring

### Usage

#### Basic Usage

```bash
./compile_all_dvft_final.sh
```

#### With sudo (if pdflatex requires elevated privileges)

```bash
sudo ./compile_all_dvft_final.sh
```

### Requirements

#### For Conversion Only
- Bash shell (available on all Unix-like systems)
- No additional dependencies needed

#### For Full Compilation (Conversion + PDF Generation)
- pdflatex (from TeX Live, MiKTeX, or similar LaTeX distribution)
- Required LaTeX packages:
  - inputenc
  - fontenc
  - amsmath
  - amssymb
  - physics
  - graphicx
  - hyperref
  - geometry

### Installing LaTeX (if needed)

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install texlive-full
```

#### CentOS/RHEL
```bash
sudo yum install texlive texlive-latex
```

#### macOS (with Homebrew)
```bash
brew install --cask mactex
```

### Output Files

After running the script, the following files will be generated:

1. **Chapter files for \input** (44 files)
   - `kapitel_00.tex` (from 00_Vorspann.md)
   - `kapitel_01.tex` through `kapitel_43.tex`

2. **Standalone chapter files** (44 files)
   - `kapitel_00_standalone.tex`
   - `kapitel_01_standalone.tex` through `kapitel_43_standalone.tex`

3. **Main document**
   - `main.tex` - Master document including all chapters

4. **PDF files** (if pdflatex is available)
   - `kapitel_XX_standalone.pdf` - Individual chapter PDFs
   - `main.pdf` - Complete book with all chapters

5. **Log files**
   - `compilation.log` - Detailed execution log
   - `compilation_errors.log` - Error-specific log (if errors occur)

### Mathematical Notation Conversion

The script automatically converts Unicode mathematical symbols to LaTeX commands:

| Unicode | LaTeX |
|---------|-------|
| φ, 𝜙 | \varphi, \Phi |
| ρ, 𝜌 | \rho |
| θ | \theta |
| ∇ | \nabla |
| ∂ | \partial |
| μ | \mu |
| λ | \lambda |
| And 30+ more symbols... |

### Error Handling

The script includes automatic error fixing for common LaTeX issues:
- Missing packages (automatically adds them)
- Font shape issues
- Multiple compilation passes for cross-references

If compilation fails for specific files, the script continues processing remaining files and reports all errors at the end.

### Customization

The script can be customized by editing the following variables at the top:

```bash
MAX_PASSES=3          # Number of pdflatex passes per file
LOG_FILE="compilation.log"
ERROR_LOG="compilation_errors.log"
```

### Troubleshooting

**Problem**: Script reports "pdflatex not found"
- **Solution**: Install a LaTeX distribution (see "Installing LaTeX" above) or run conversion-only mode

**Problem**: Compilation fails with package errors
- **Solution**: Install texlive-full for all packages, or install specific missing packages

**Problem**: Permission denied
- **Solution**: Run with `sudo ./compile_all_dvft_final.sh` or make the script executable with `chmod +x compile_all_dvft_final.sh`

**Problem**: Some characters not converting properly
- **Solution**: Check that your Markdown files are UTF-8 encoded

### Support

For issues or questions:
1. Check the log files: `compilation.log` and `compilation_errors.log`
2. Verify all Markdown files are present and readable
3. Ensure LaTeX distribution is properly installed
4. Check that the physics package is available in your LaTeX distribution

## Directory Structure

```
md_chapters_dvft/
├── 00_Vorspann.md              # Source Markdown files
├── Kapitel_01.md to Kapitel_43.md
├── compile_all_dvft_final.sh   # Compilation script
├── README.md                    # This file
├── kapitel_*.tex                # Generated LaTeX files (for \input)
├── kapitel_*_standalone.tex     # Generated standalone LaTeX files
├── main.tex                     # Generated main document
└── *.pdf                        # Generated PDF files (if compiled)
```

## License

Part of the T0 Time-Mass Duality Theory repository.
