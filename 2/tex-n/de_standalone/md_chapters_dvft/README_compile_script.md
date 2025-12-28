# DVFT LaTeX Compilation Script

## Overview

The `compile_all_dvft.sh` script is an automated LaTeX compilation tool designed for the T0 Theory DVFT (Dynamic Vacuum Field Theory) chapter files. It recursively compiles all LaTeX chapter files (`kapitel_00.tex` to `kapitel_43.tex`) and `main.tex` using `pdflatex` with built-in error detection and automatic fixing capabilities.

## Features

- **Recursive Compilation**: Compiles all chapter files (kapitel_00.tex through kapitel_43.tex) and main.tex
- **Multiple Passes**: Runs up to 3 compilation passes per file by default (configurable)
- **Automatic Error Fixing**: Detects and attempts to fix common LaTeX errors including:
  - Missing packages (physics, amsmath, graphicx, hyperref, siunitx, geometry)
  - Undefined control sequences
  - Font issues
  - UTF-8 encoding problems
  - Package-specific command errors
- **Physics Package Support**: Full support for the `physics` package commonly used in quantum mechanics notation
- **Comprehensive Logging**: Logs all errors and fixes to a dedicated log file
- **Color-coded Output**: Clear visual feedback with color-coded success/failure messages
- **Dry-run Mode**: Test what the script would do without making actual changes
- **Verbose Mode**: Detailed output for debugging

## Requirements

- **Root/sudo access**: Required for installing missing packages automatically
- **TeX Live or another LaTeX distribution**: Must have `pdflatex` installed
- **Bash shell**: Unix/Linux environment

## Installation

1. The script is located in: `2/tex-n/de_standalone/md_chapters_dvft/compile_all_dvft.sh`
2. Ensure it has execute permissions:
   ```bash
   chmod +x compile_all_dvft.sh
   ```

## Usage

### Basic Usage

```bash
sudo ./compile_all_dvft.sh
```

### Advanced Options

```bash
sudo ./compile_all_dvft.sh [OPTIONS]
```

#### Options:

- `-p, --passes NUM` : Number of compilation passes per file (default: 3)
- `-l, --log FILE` : Error log file name (default: dvft_compilation_errors.log)
- `-v, --verbose` : Enable verbose output
- `-h, --help` : Show help message
- `--no-fix` : Disable automatic error fixing
- `--dry-run` : Show what would be done without making changes

### Examples

1. **Compile all files with default settings**:
   ```bash
   sudo ./compile_all_dvft.sh
   ```

2. **Verbose mode with 4 passes per file**:
   ```bash
   sudo ./compile_all_dvft.sh -v -p 4
   ```

3. **Compile without automatic error fixing**:
   ```bash
   sudo ./compile_all_dvft.sh --no-fix
   ```

4. **Dry-run to see what would happen**:
   ```bash
   ./compile_all_dvft.sh --dry-run
   ```

5. **Custom log file location**:
   ```bash
   sudo ./compile_all_dvft.sh -l /tmp/custom_log.log
   ```

## Automatic Error Fixes

The script can automatically detect and fix the following common LaTeX errors:

### 1. Missing Physics Package
- **Error**: `physics.sty not found`
- **Fix**: Installs the physics package via tlmgr or apt-get

### 2. Undefined Quantum Notation Commands
- **Error**: Undefined commands like `\bra`, `\ket`, `\braket`
- **Fix**: Adds `\usepackage{physics}` to the document

### 3. Missing siunitx Package
- **Error**: Undefined commands like `\SI`, `\qty`
- **Fix**: Adds `\usepackage{siunitx}` and installs the package

### 4. Missing Font Packages
- **Error**: Font not found errors
- **Fix**: Installs `texlive-fonts-recommended` and `texlive-fonts-extra`

### 5. Missing amsmath Commands
- **Error**: Undefined environments like `align`, `equation`, `split`
- **Fix**: Adds `\usepackage{amsmath}`

### 6. Missing graphicx Package
- **Error**: `\includegraphics` command not found
- **Fix**: Adds `\usepackage{graphicx}`

### 7. UTF-8 Encoding Issues
- **Error**: Unicode or inputenc errors
- **Fix**: Adds `\usepackage[utf8]{inputenc}`

### 8. Missing hyperref Package
- **Error**: `\href` command not found
- **Fix**: Adds `\usepackage{hyperref}`

## Output

The script provides:

1. **Console Output**: Color-coded status messages for each file
   - Green: Successful compilation
   - Red: Failed compilation
   - Yellow: Skipped files or warnings
   - Cyan: Information messages

2. **Log File**: Detailed error log saved to `dvft_compilation_errors.log` (or custom location)
   - Timestamps
   - Full error details from LaTeX log files
   - List of automatic fixes applied

3. **Summary**: Final statistics including:
   - Total files processed
   - Successful compilations
   - Failed compilations
   - Number of auto-fixes applied

## Expected Files

The script looks for the following files in the current directory:

- `kapitel_00.tex` through `kapitel_43.tex` (44 chapter files)
- `main.tex` (optional master document)

Files must contain `\begin{document}` to be compiled.

## Notes

- **Current Directory**: The script currently contains Markdown files (.md) that may need to be converted to LaTeX format first
- **Sudo Required**: Many automatic fixes require root access to install packages
- **Multiple Attempts**: The script will attempt up to 3 fix attempts per file before giving up
- **Package Installation**: Uses `tlmgr` if available, otherwise falls back to `apt-get` on Debian/Ubuntu systems

## Troubleshooting

### "This script requires root privileges"
- Run the script with `sudo`: `sudo ./compile_all_dvft.sh`

### "pdflatex is not installed"
- Install TeX Live: `sudo apt-get install texlive-full`
- Or a minimal installation: `sudo apt-get install texlive-latex-base texlive-latex-extra`

### "No LaTeX files found to compile"
- Ensure .tex files exist in the directory
- Check that files are named correctly (kapitel_XX.tex format)
- The directory may contain only .md files that need conversion

### Compilation still fails after fixes
- Check the log file for detailed error messages
- Some errors may require manual intervention
- Use verbose mode (`-v`) for more information

## Author

Johann Pascher - T0 Theory Project

## Date

Created: 2025-12-28

## License

Part of the T0 Time-Mass Duality Theory project.
