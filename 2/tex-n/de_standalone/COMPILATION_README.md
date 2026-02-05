# LaTeX Compilation System for DE Standalone Documents

## Overview
This directory contains 118 German standalone LaTeX documents that are compiled individually using a shared preamble.

## Key Files
- `T0_preamble_standalone_De.tex` - Shared preamble (96 lines, A4 single-sided)
- `iterative_compiler.sh` - Automated compilation and preamble extension script
- `compilation_log.txt` - Detailed compilation log
- `successful_compilations.txt` - List of successfully compiled files
- `failed_compilations.txt` - List of files that failed compilation
- `preamble_additions.txt` - Log of additions made to preamble

## Usage

### Run Full Compilation
```bash
cd /home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_standalone
./iterative_compiler.sh
```

### Compile Single File
```bash
lualatex -interaction=nonstopmode <filename>.tex
```

## Preamble Features
- **Page Format**: A4 single-sided (`twoside=false`)
- **Fonts**: Inter (main), JetBrains Mono (mono), Libertinus Math (math)
- **Custom Environments**: 31 tcolorbox environments for content structuring
- **Packages**: longtable, tabularx, booktabs, adjustbox, lscape, pdflscape

## Compilation Statistics
- Total Documents: 118
- Current Success Rate: Check `compilation_log.txt` for latest stats
- Preamble Lines: 96 (optimized and modular)

## Troubleshooting
1. If fonts are missing, fallback to Latin Modern fonts
2. Check `.log` files for specific errors
3. Missing packages are automatically added by iterative_compiler.sh
4. For unicode-math issues, ensure LuaLaTeX is used (not pdflatex)

## Maintenance
- The preamble is iteratively extended based on compilation errors
- Each addition is logged in `preamble_additions.txt`
- Remove duplicate or conflicting definitions manually if needed
