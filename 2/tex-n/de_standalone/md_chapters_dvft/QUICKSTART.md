# Quick Start Guide - DVFT Compilation

## Run the Script

```bash
./compile_all_dvft_final.sh
```

## What It Does

1. **Converts** 44 Markdown files to LaTeX
2. **Creates** main.tex with all chapters
3. **Compiles** to PDF (if pdflatex available)
4. **Logs** all output to compilation.log

## Output Files

- `kapitel_XX.tex` - For inclusion in main.tex
- `kapitel_XX_standalone.tex` - Standalone chapters
- `main.tex` - Complete book
- `*.pdf` - Compiled PDFs (if pdflatex installed)

## Requirements

- Bash shell (standard on Linux/Mac)
- pdflatex (optional, for PDF generation)

## Install LaTeX (Optional)

### Ubuntu/Debian
```bash
sudo apt-get install texlive-full
```

### macOS
```bash
brew install --cask mactex
```

## Troubleshooting

- **No pdflatex?** Script still converts to LaTeX
- **Permission denied?** Run `chmod +x compile_all_dvft_final.sh`
- **Need sudo?** Run `sudo ./compile_all_dvft_final.sh`

## Check Logs

```bash
cat compilation.log         # Full log
cat compilation_errors.log  # Errors only
```

## More Info

See [README.md](README.md) for complete documentation.
