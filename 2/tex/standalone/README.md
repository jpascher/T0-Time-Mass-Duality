# T0 Standalone Documents - Compilation Guide

## Quick Start

### Linux/macOS
```bash
cd 2/tex/standalone
chmod +x compile_all.sh
./compile_all.sh          # Compile all languages
./compile_all.sh en       # Compile only English
```

### Windows
```cmd
cd 2\tex\standalone
compile_all.bat           # Compile all languages
compile_all.bat en        # Compile only English
```

## Manual Compilation

To compile a single document:
```bash
cd 2/tex/standalone/en
pdflatex T0_Introduction_En_ch.tex
pdflatex T0_Introduction_En_ch.tex   # Run twice for references
```

## Directory Structure

```
standalone/
├── compile_all.sh      # Linux/macOS build script
├── compile_all.bat     # Windows build script
├── README.md           # This file
├── en/                 # 81 English documents
│   ├── T0_Introduction_En_ch.tex
│   ├── T0_Grundlagen_En_ch.tex
│   └── ...
├── de/                 # 81 German documents (babel=german)
├── fr/                 # 81 French documents (babel=french)
└── es/                 # 81 Spanish documents (babel=spanish)
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

## Features

Each standalone document includes:
- **Minimal preamble**: Only packages used in that chapter
- **Relevant bibliography**: Only entries cited in that chapter
- **Language-specific settings**: Correct babel language configuration

## Cleaning Up

To remove generated PDFs and auxiliary files:
```bash
cd 2/tex/standalone
find . -name "*.pdf" -delete
find . -name "*.aux" -delete
find . -name "*.log" -delete
find . -name "*.out" -delete
```
