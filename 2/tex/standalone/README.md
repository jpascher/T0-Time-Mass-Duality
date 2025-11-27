# T0 Standalone Documents - Compilation Guide

## Quick Start

### Linux/macOS
```bash
cd 2/tex/standalone
chmod +x compile_all.sh
./compile_all.sh          # Compile all languages (en, de, fr, es, it)
./compile_all.sh en       # Compile only English
./compile_all.sh it       # Compile only Italian
```

### Windows
```cmd
cd 2\tex\standalone
compile_all.bat           # Compile all languages (en, de, fr, es, it)
compile_all.bat en        # Compile only English
compile_all.bat it        # Compile only Italian
```

## Manual Compilation

To compile a single document:
```bash
# English
cd 2/tex/standalone/en
pdflatex 137_En.tex
pdflatex 137_En.tex   # Run twice for references

# Italian
cd 2/tex/standalone/it
pdflatex 137_It.tex
pdflatex 137_It.tex   # Run twice for references
```

## Directory Structure

```
standalone/
├── compile_all.sh      # Linux/macOS build script
├── compile_all.bat     # Windows build script
├── README.md           # This file
├── en/                 # 95 English documents
│   ├── 137_En.tex
│   ├── T0_Introduction_En.tex
│   └── ...
├── de/                 # German documents (babel=german)
├── fr/                 # French documents (babel=french)
├── es/                 # Spanish documents (babel=spanish)
└── it/                 # 95 Italian documents (babel=italian)
    ├── 137_It.tex
    ├── T0_Introduction_It.tex
    └── ...
```

## Requirements

- **pdflatex** (TeX Live, MiKTeX, or MacTeX)
- Required packages: `amsmath`, `amssymb`, `hyperref`, `babel`, `geometry`, etc.

Install on Ubuntu/Debian:
```bash
sudo apt-get install texlive-full
```

Install on macOS:
```bash
brew install --cask mactex
```

Install on Windows:
- Download and install MiKTeX from https://miktex.org/download

## Features

Each standalone document includes:
- **Minimal preamble**: Only packages used in that chapter
- **Relevant bibliography**: Only entries cited in that chapter
- **Language-specific settings**: Correct babel language configuration
- **Blue hyperlinks**: All internal links are colored blue for easy navigation

## Supported Languages

| Language | Directory | Babel Setting |
|----------|-----------|---------------|
| English  | `en/`     | `english`     |
| German   | `de/`     | `german`      |
| French   | `fr/`     | `french`      |
| Spanish  | `es/`     | `spanish`     |
| Italian  | `it/`     | `italian`     |

## Cleaning Up

To remove generated PDFs and auxiliary files:
```bash
cd 2/tex/standalone
find . -name "*.pdf" -delete
find . -name "*.aux" -delete
find . -name "*.log" -delete
find . -name "*.out" -delete
```
