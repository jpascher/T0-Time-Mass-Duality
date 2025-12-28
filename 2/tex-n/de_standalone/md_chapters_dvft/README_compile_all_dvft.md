# DVFT LaTeX Compilation Script Documentation

## Overview

The `compile_all_dvft.sh` script is a comprehensive LaTeX compilation tool that automatically compiles all DVFT chapter files (kapitel_00.tex to kapitel_43.tex) and main.tex using pdflatex with automatic error detection and fixing capabilities.

## Features

### Core Functionality
- **Recursive Compilation**: Automatically finds and compiles kapitel_00.tex through kapitel_43.tex and main.tex
- **Sudo Support**: Uses `sudo pdflatex` for compilation to handle system-wide package installations
- **Multi-Pass Compilation**: Runs up to 5 compilation passes per file to resolve cross-references and complex errors
- **Error Logging**: All errors are logged to `compile_errors.log` for detailed review

### Automatic Error Fixing
The script can automatically detect and fix the following types of LaTeX errors:

1. **Missing Packages**
   - Detects when a LaTeX package is not found
   - Attempts to install it using `sudo tlmgr install`
   - Falls back to `apt-get` if tlmgr fails
   - Adds `\usepackage` statements to files if needed

2. **Undefined Commands**
   - Detects undefined control sequences
   - Automatically adds required packages:
     - `\bra`, `\ket`, `\braket` → adds `physics` package
     - `\mathbb`, `\mathcal`, `\mathfrak` → adds `amssymb` package
     - `\includegraphics` → adds `graphicx` package

3. **Font Issues**
   - Detects font errors and attempts to continue compilation

4. **Physics Package Integration**
   - Automatically ensures the `physics` package is included in all LaTeX files
   - Installs the package system-wide if not present

### Package Management
- Checks for and installs the `physics` package before compilation
- Verifies common packages: `amsmath`, `amssymb`, `graphicx`, `hyperref`, `geometry`, `xcolor`
- Uses multiple installation methods (tlmgr, apt-get) for maximum compatibility

## Usage

### Basic Usage

```bash
cd /path/to/2/tex-n/de_standalone/md_chapters_dvft
./compile_all_dvft.sh
```

### Requirements

The script requires:
- Bash shell
- LaTeX distribution (TeX Live recommended)
- `pdflatex` command
- `sudo` privileges for package installation
- `kpsewhich` for package detection

### What the Script Does

1. **Initialization**
   - Creates an error log file: `compile_errors.log`
   - Checks for required LaTeX packages
   - Installs missing packages automatically

2. **File Discovery**
   - Searches for files matching `kapitel_00.tex` to `kapitel_43.tex`
   - Looks for `main.tex`
   - Falls back to finding any `.tex` files if specific files are not found

3. **Compilation Loop**
   For each file:
   - Ensures the physics package is in the preamble
   - Attempts up to 5 compilation passes
   - After each failed pass:
     - Analyzes the log file for errors
     - Attempts to fix detected errors
     - Retries compilation
   - Logs all errors and fixes to `compile_errors.log`

4. **Summary Report**
   - Total files processed
   - Number of successful compilations
   - Number of files that were fixed and compiled
   - Number of failed compilations

## Output

### Console Output
The script provides colored, real-time feedback:
- 🔵 Blue: Headers and processing information
- 🟢 Green: Successful operations
- 🟡 Yellow: Warnings and fix attempts
- 🔴 Red: Errors and failures
- 🟦 Cyan: Status messages

### Error Log
All compilation errors are logged to `compile_errors.log` with:
- Timestamp for each file
- Complete LaTeX error messages
- Descriptions of attempted fixes
- Final status

### Generated Files
For each successfully compiled `.tex` file:
- `.pdf` file (the compiled document)
- `.log` file (LaTeX compilation log)
- `.aux` file (auxiliary information)

## Example Output

```
==============================================================================
  DVFT LaTeX Compilation Script with Auto-Fix
==============================================================================
Working directory: /path/to/md_chapters_dvft
Max passes per file: 5
Error log: /path/to/md_chapters_dvft/compile_errors.log

Checking for required LaTeX packages...
Physics package is already installed.

Searching for chapter files...
Found 45 file(s) to compile

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Processing: kapitel_00.tex
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pass 1/5...
✓ Compilation successful!

...

==============================================================================
  COMPILATION SUMMARY
==============================================================================
Total files:      45
Successful:       43
Fixed and built:  5
Failed:           2

Error log: /path/to/md_chapters_dvft/compile_errors.log
==============================================================================
```

## Error Handling

### Common Errors and Fixes

| Error Type | Detection | Automatic Fix |
|------------|-----------|---------------|
| Missing Package | `File '*.sty' not found` | Install via tlmgr/apt-get, add \usepackage |
| Undefined Command | `Undefined control sequence` | Add required package (physics, amssymb, etc.) |
| Font Error | `Font ... not found` | Continue compilation |
| Missing Document | `Missing \begin{document}` | No automatic fix (requires manual intervention) |

### Exit Codes
- `0`: All files compiled successfully
- `1`: One or more files failed to compile

## Troubleshooting

### Script Won't Run
```bash
chmod +x compile_all_dvft.sh
```

### Permission Denied
Ensure you have sudo privileges or run:
```bash
sudo ./compile_all_dvft.sh
```

### Packages Won't Install
Manually install required packages:
```bash
sudo tlmgr install physics amsmath amssymb graphicx hyperref
```

### Files Not Found
Ensure `.tex` files exist in the same directory as the script, or check that files are named:
- `kapitel_00.tex` through `kapitel_43.tex`
- `main.tex`

## Advanced Usage

### Modify Maximum Passes
Edit the script and change:
```bash
MAX_PASSES=5  # Change to desired number
```

### Disable sudo
If you don't need sudo privileges, edit line 263 in the script:
```bash
# Change from:
sudo pdflatex -interaction=nonstopmode -file-line-error "$filename" > "$TEMP_LOG" 2>&1

# To:
pdflatex -interaction=nonstopmode -file-line-error "$filename" > "$TEMP_LOG" 2>&1
```

### Custom Error Log Location
Edit the script and change:
```bash
ERROR_LOG="/custom/path/compile_errors.log"
```

## Technical Details

### Script Architecture
1. **Configuration Section**: Sets up variables, paths, and colors
2. **Package Management Functions**: Check and install LaTeX packages
3. **Error Detection Functions**: Parse log files for specific error patterns
4. **Error Fixing Functions**: Automatically fix detected errors
5. **Compilation Function**: Main compilation loop with auto-fix
6. **Main Function**: Orchestrates the entire process

### Error Detection Patterns
- Missing packages: `! LaTeX Error: File.*\.sty' not found`
- Undefined commands: `! Undefined control sequence`
- Font errors: `Font.*not found`
- Missing document: `! LaTeX Error: Missing \\begin{document}`
- Runaway arguments: `Runaway argument`

## Version History

- **2025-12-28**: Initial version with auto-fix capabilities

## Author

Johann Pascher / GitHub Copilot

## License

Part of the T0-Time-Mass-Duality project.
