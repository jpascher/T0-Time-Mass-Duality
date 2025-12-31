#!/bin/bash

# Rekursive LaTeX-Kompilierung für alle narrativen Kapitel
# Autor: GitHub Copilot

cd /home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/narrative

SUCCESS_COUNT=0
FAIL_COUNT=0
FAILED_FILES=()

echo "========================================="
echo "Kompiliere alle narrativen Kapitel (De)"
echo "========================================="

# Kompiliere alle deutschen Kapitel
for i in $(seq -f "%02g" 1 44); do
    FILE="Kapitel_${i}_Narrative_De.tex"
    if [ -f "$FILE" ]; then
        echo "Kompiliere $FILE..."
        pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$FILE" > /dev/null 2>&1
        # Zweiter Durchlauf für TOC
        pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$FILE" > /dev/null 2>&1
        
        PDF_FILE="Kapitel_${i}_Narrative_De.pdf"
        if [ -f "$PDF_FILE" ]; then
            SIZE=$(stat -f%z "$PDF_FILE" 2>/dev/null || stat -c%s "$PDF_FILE" 2>/dev/null)
            echo "✅ $FILE erfolgreich kompiliert ($SIZE bytes)"
            SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        else
            echo "❌ $FILE fehlgeschlagen"
            FAIL_COUNT=$((FAIL_COUNT + 1))
            FAILED_FILES+=("$FILE")
        fi
    fi
done

echo ""
echo "========================================="
echo "Kompiliere alle narrativen Kapitel (En)"
echo "========================================="

# Kompiliere alle englischen Kapitel
for i in $(seq -f "%02g" 1 44); do
    FILE="Kapitel_${i}_Narrative_En.tex"
    if [ -f "$FILE" ]; then
        echo "Kompiliere $FILE..."
        pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$FILE" > /dev/null 2>&1
        # Zweiter Durchlauf für TOC
        pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$FILE" > /dev/null 2>&1
        
        PDF_FILE="Kapitel_${i}_Narrative_En.pdf"
        if [ -f "$PDF_FILE" ]; then
            SIZE=$(stat -f%z "$PDF_FILE" 2>/dev/null || stat -c%s "$PDF_FILE" 2>/dev/null)
            echo "✅ $FILE erfolgreich kompiliert ($SIZE bytes)"
            SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        else
            echo "❌ $FILE fehlgeschlagen"
            FAIL_COUNT=$((FAIL_COUNT + 1))
            FAILED_FILES+=("$FILE")
        fi
    fi
done

echo ""
echo "========================================="
echo "Kompiliere Master-Dateien"
echo "========================================="

# Deutsche Master-Datei
if [ -f "FFGFT_Narrative_Master_De.tex" ]; then
    echo "Kompiliere FFGFT_Narrative_Master_De.tex..."
    pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "FFGFT_Narrative_Master_De.tex" > /dev/null 2>&1
    pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "FFGFT_Narrative_Master_De.tex" > /dev/null 2>&1
    
    if [ -f "FFGFT_Narrative_Master_De.pdf" ]; then
        SIZE=$(stat -f%z "FFGFT_Narrative_Master_De.pdf" 2>/dev/null || stat -c%s "FFGFT_Narrative_Master_De.pdf" 2>/dev/null)
        echo "✅ FFGFT_Narrative_Master_De.tex erfolgreich kompiliert ($SIZE bytes)"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        echo "❌ FFGFT_Narrative_Master_De.tex fehlgeschlagen"
        FAIL_COUNT=$((FAIL_COUNT + 1))
        FAILED_FILES+=("FFGFT_Narrative_Master_De.tex")
    fi
fi

# Englische Master-Datei
if [ -f "FFGFT_Narrative_Master_En.tex" ]; then
    echo "Kompiliere FFGFT_Narrative_Master_En.tex..."
    pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "FFGFT_Narrative_Master_En.tex" > /dev/null 2>&1
    pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "FFGFT_Narrative_Master_En.tex" > /dev/null 2>&1
    
    if [ -f "FFGFT_Narrative_Master_En.pdf" ]; then
        SIZE=$(stat -f%z "FFGFT_Narrative_Master_En.pdf" 2>/dev/null || stat -c%s "FFGFT_Narrative_Master_En.pdf" 2>/dev/null)
        echo "✅ FFGFT_Narrative_Master_En.tex erfolgreich kompiliert ($SIZE bytes)"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        echo "❌ FFGFT_Narrative_Master_En.tex fehlgeschlagen"
        FAIL_COUNT=$((FAIL_COUNT + 1))
        FAILED_FILES+=("FFGFT_Narrative_Master_En.tex")
    fi
fi

echo ""
echo "========================================="
echo "ZUSAMMENFASSUNG"
echo "========================================="
echo "Erfolgreich kompiliert: $SUCCESS_COUNT"
echo "Fehlgeschlagen: $FAIL_COUNT"

if [ $FAIL_COUNT -gt 0 ]; then
    echo ""
    echo "Fehlgeschlagene Dateien:"
    for file in "${FAILED_FILES[@]}"; do
        echo "  - $file"
    done
    exit 1
else
    echo ""
    echo "✅ ALLE DATEIEN ERFOLGREICH KOMPILIERT!"
    exit 0
fi
