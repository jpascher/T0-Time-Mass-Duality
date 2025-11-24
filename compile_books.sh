#!/bin/bash
# Compile T0 Books - English and German versions
# This script compiles both T0_Book_En.tex and T0_Book_De.tex

echo "========================================"
echo "Kompilierung der T0 Bücher"
echo "Compiling T0 Books"
echo "========================================"
echo ""

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo "FEHLER: pdflatex wurde nicht gefunden!"
    echo "ERROR: pdflatex not found!"
    echo ""
    echo "Bitte installieren Sie eine LaTeX-Distribution:"
    echo "Please install a LaTeX distribution:"
    echo "  - Linux: sudo apt-get install texlive-full"
    echo "  - macOS: https://www.tug.org/mactex/"
    exit 1
fi

echo "Gefunden: pdflatex"
echo "Found: pdflatex"
echo ""

# Compile English book
echo "----------------------------------------"
echo "Kompiliere englisches Buch..."
echo "Compiling English book..."
echo "----------------------------------------"
pdflatex -interaction=nonstopmode T0_Book_En.tex
if [ $? -ne 0 ]; then
    echo "WARNUNG: Erster Durchlauf mit Fehlern"
    echo "WARNING: First pass had errors"
fi
echo "Zweiter Durchlauf für Referenzen..."
echo "Second pass for references..."
pdflatex -interaction=nonstopmode T0_Book_En.tex

if [ -f T0_Book_En.pdf ]; then
    echo ""
    echo "ERFOLG: T0_Book_En.pdf wurde erstellt!"
    echo "SUCCESS: T0_Book_En.pdf created!"
else
    echo ""
    echo "FEHLER: T0_Book_En.pdf konnte nicht erstellt werden!"
    echo "ERROR: T0_Book_En.pdf could not be created!"
fi
echo ""

# Compile German book
echo "----------------------------------------"
echo "Kompiliere deutsches Buch..."
echo "Compiling German book..."
echo "----------------------------------------"
pdflatex -interaction=nonstopmode T0_Book_De.tex
if [ $? -ne 0 ]; then
    echo "WARNUNG: Erster Durchlauf mit Fehlern"
    echo "WARNING: First pass had errors"
fi
echo "Zweiter Durchlauf für Referenzen..."
echo "Second pass for references..."
pdflatex -interaction=nonstopmode T0_Book_De.tex

if [ -f T0_Book_De.pdf ]; then
    echo ""
    echo "ERFOLG: T0_Book_De.pdf wurde erstellt!"
    echo "SUCCESS: T0_Book_De.pdf created!"
else
    echo ""
    echo "FEHLER: T0_Book_De.pdf konnte nicht erstellt werden!"
    echo "ERROR: T0_Book_De.pdf could not be created!"
fi
echo ""

# Clean up auxiliary files
echo "----------------------------------------"
echo "Bereinige Hilfsdateien..."
echo "Cleaning up auxiliary files..."
echo "----------------------------------------"
rm -f T0_Book_*.aux T0_Book_*.log T0_Book_*.out T0_Book_*.toc 2>/dev/null

echo ""
echo "========================================"
echo "Kompilierung abgeschlossen!"
echo "Compilation completed!"
echo "========================================"
echo ""
echo "Erstellte PDFs:"
echo "Created PDFs:"
[ -f T0_Book_En.pdf ] && echo "  - T0_Book_En.pdf"
[ -f T0_Book_De.pdf ] && echo "  - T0_Book_De.pdf"
echo ""
