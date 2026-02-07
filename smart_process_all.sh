#!/bin/bash

SOURCE_DIR="2/tex-n/de_standalone"
PROCESSED_DIR="2/tex-n/de_standalone_processed"
PDF_DIR="2/pdf"

mkdir -p "$PROCESSED_DIR"
mkdir -p "$PDF_DIR"

# Kopiere Preamble-Datei
echo "Kopiere Preamble..."
cp "$SOURCE_DIR/T0_preamble_standalone_De.tex" "$PROCESSED_DIR/"

# Zähler
SUCCESS=0
FAILED=0
TOTAL=0

> pdf_links_with_numbers.txt

echo "=== INTELLIGENTE BATCH-VERARBEITUNG ==="
echo ""

# Verarbeite alle Dokumente
find "$SOURCE_DIR" -maxdepth 1 -name "[0-9]*.tex" -type f | sort | while read ORIG_FILE; do
    BASENAME=$(basename "$ORIG_FILE")
    TOTAL=$((TOTAL + 1))
    
    echo "[$TOTAL] $BASENAME"
    
    # Kopiere Datei
    cp "$ORIG_FILE" "$PROCESSED_DIR/"
    
    # Kompiliere in processed-Verzeichnis
    cd "$PROCESSED_DIR"
    
    # 3 Durchläufe
    SUCCESS_FLAG=true
    for i in 1 2 3; do
        if ! lualatex -interaction=nonstopmode -halt-on-error "$BASENAME" >/dev/null 2>&1; then
            SUCCESS_FLAG=false
            break
        fi
    done
    
    cd - >/dev/null
    
    # Ergebnis
    PDF_NAME="${BASENAME%.tex}.pdf"
    if [ "$SUCCESS_FLAG" = true ] && [ -f "$PROCESSED_DIR/$PDF_NAME" ]; then
        mv "$PROCESSED_DIR/$PDF_NAME" "$PDF_DIR/"
        SUCCESS=$((SUCCESS + 1))
        echo "  ✓ Erfolgreich"
        echo "$SUCCESS. 2/pdf/$PDF_NAME" >> pdf_links_with_numbers.txt
    else
        FAILED=$((FAILED + 1))
        echo "  ✗ Fehlgeschlagen"
    fi
    
    # Cleanup
    rm -f "$PROCESSED_DIR"/*.aux "$PROCESSED_DIR"/*.log "$PROCESSED_DIR"/*.out \
          "$PROCESSED_DIR"/*.toc "$PROCESSED_DIR"/*.synctex.gz
    
done

echo ""
echo "=== ABGESCHLOSSEN ==="
echo "Erfolgreich: $SUCCESS"
echo "Fehlgeschlagen: $FAILED"
