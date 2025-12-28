# DVFT LaTeX Chapter Compilation

This directory contains the LaTeX compilation script for DVFT (Dynamic Vacuum Field Theory) chapters.

## Files

- `compile_all.sh` - Main compilation script
- `kapitel_00.tex` to `kapitel_43.tex` - Individual chapter files (to be created)
- `main.tex` - Main document file (to be created)
- `compile_logs/` - Directory for compilation logs (auto-generated)

## Usage

### Basic Compilation

```bash
./compile_all.sh
```

This will compile all chapter files (kapitel_00.tex to kapitel_43.tex) and main.tex using sudo pdflatex.

### Options

- `-h, --help` - Show help message
- `-v, --verbose` - Verbose output showing detailed compilation progress
- `-c, --clean` - Clean auxiliary files after compilation
- `-n, --no-sudo` - Don't use sudo for pdflatex (useful for testing)

### Examples

```bash
# Compile with verbose output
./compile_all.sh -v

# Compile and clean auxiliary files
./compile_all.sh -c

# Compile without sudo (for testing)
./compile_all.sh -n

# Combine options
./compile_all.sh -v -c
```

## Features

The script automatically:

1. **Multiple Passes**: Runs pdflatex up to 3 times to resolve cross-references and citations
2. **Error Detection**: Detects and reports compilation errors
3. **Package Management**: Attempts to install missing LaTeX packages automatically (with retry limits)
4. **Physics Package**: Includes support for the physics package and its commands
5. **Logging**: Creates detailed logs in `compile_logs/` directory
6. **Summary Report**: Provides compilation summary with success/failure counts
7. **Security**: Runs without shell-escape for improved security

## Requirements

- TeX Live or another LaTeX distribution with pdflatex
- sudo access (unless using `-n` flag)
- Required LaTeX packages:
  - physics
  - inputenc
  - babel
  - (other packages will be auto-detected and installed if missing)

## Installation

If pdflatex is not installed, install TeX Live:

### Ubuntu/Debian
```bash
sudo apt-get install texlive-full
```

### Other Systems
Visit: https://www.tug.org/texlive/

## Common Issues

### Permission Denied
Make sure the script is executable:
```bash
chmod +x compile_all.sh
```

### Missing Packages
The script will attempt to install missing packages automatically. If this fails, install manually:
```bash
sudo tlmgr install <package-name>
```

### Compilation Errors
Check the log files in `compile_logs/` directory for detailed error messages.

## Workflow

1. Create or convert markdown files to LaTeX (kapitel_XX.tex)
2. Create main.tex if needed
3. Run `./compile_all.sh -v` to compile all files
4. Check `compile_logs/` for any errors
5. PDFs will be created in the same directory

## Notes

- The script uses the `physics` package by default for mathematical notation
- Compilation logs are preserved for debugging
- Auxiliary files can be cleaned with the `-c` option
- The script will skip compilation if no .tex files are found

## Author

Generated for T0 Theory - Johann Pascher
Date: 2025
