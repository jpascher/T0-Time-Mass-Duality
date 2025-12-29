#!/bin/bash
#
# Script to compile DVFT master document using pdflatex
# Usage: ./compile_dvft_master.sh
#

set -e  # Exit on error

echo "======================================================================"
echo "DVFT Master Document Compilation Script"
echo "======================================================================"
echo ""

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo "Error: pdflatex not found. Please install TeXLive or MiKTeX."
    echo "On Ubuntu/Debian: sudo apt-get install texlive-latex-extra texlive-lang-german"
    exit 1
fi

echo "Step 1: Preparing chapter content files..."
python3 prepare_chapters_for_master.py
if [ $? -ne 0 ]; then
    echo "Error: Failed to prepare chapter content files."
    exit 1
fi

echo ""
echo "Step 2: Running pdflatex (first pass)..."
pdflatex -interaction=nonstopmode DVFT_Complete_Combined.tex

echo ""
echo "Step 3: Running pdflatex (second pass for cross-references)..."
pdflatex -interaction=nonstopmode DVFT_Complete_Combined.tex

echo ""
echo "Step 4: Running pdflatex (third pass for table of contents)..."
pdflatex -interaction=nonstopmode DVFT_Complete_Combined.tex

echo ""
echo "======================================================================"
echo "Compilation complete!"
echo ""
echo "Output file: DVFT_Complete_Combined.pdf"
echo ""

# Display file info
if [ -f "DVFT_Complete_Combined.pdf" ]; then
    pdf_size=$(du -h DVFT_Complete_Combined.pdf | cut -f1)
    pdf_pages=$(pdfinfo DVFT_Complete_Combined.pdf 2>/dev/null | grep "Pages:" | awk '{print $2}' || echo "unknown")
    echo "PDF Size: $pdf_size"
    echo "Pages: $pdf_pages"
    echo ""
fi

echo "======================================================================"
echo ""
echo "To view the PDF:"
echo "  - Linux: xdg-open DVFT_Complete_Combined.pdf"
echo "  - macOS: open DVFT_Complete_Combined.pdf"
echo "  - Windows: start DVFT_Complete_Combined.pdf"
echo ""
echo "Auxiliary files (.aux, .log, .toc, etc.) can be cleaned with:"
echo "  rm -f DVFT_Complete_Combined.{aux,log,toc,out,pdf}"
echo ""
