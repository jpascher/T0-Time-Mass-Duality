#!/bin/bash

# Automatische Verarbeitung ALLER DE standalone Dokumente
# Läuft kontinuierlich bis alle fertig sind

SOURCE_DIR="2/tex-n/de_standalone"
PROCESSED_DIR="2/tex-n/de_standalone_processed"
PDF_DIR="2/pdf"
PREAMBLE="T0_preamble_standalone_De.tex"

mkdir -p "$PROCESSED_DIR"
mkdir -p "$PDF_DIR"

# Zähler
TOTAL=0
SUCCESS=0
FAILED=0

echo "=== AUTOMATISCHE BATCH-VERARBEITUNG GESTARTET ==="
echo "Quelle: $SOURCE_DIR"
echo "Ziel: $PROCESSED_DIR"
echo "PDFs: $PDF_DIR"
echo ""

# Finde alle .tex Dateien (außer Preamble)
find "$SOURCE_DIR" -maxdepth 1 -name "*.tex" -type f ! -name "T0_preamble*.tex" | sort | while read ORIG_FILE; do
    BASENAME=$(basename "$ORIG_FILE")
    TOTAL=$((TOTAL + 1))
    
    echo "[$TOTAL] Verarbeite: $BASENAME"
    
    # Kopiere zu processed
    PROCESSED_FILE="$PROCESSED_DIR/$BASENAME"
    cp "$ORIG_FILE" "$PROCESSED_FILE"
    
    # Kompiliere (3 Durchläufe)
    cd "$PROCESSED_DIR"
    COMPILE_SUCCESS=true
    
    for i in 1 2 3; do
        if lualatex -interaction=nonstopmode -halt-on-error "$BASENAME" > /dev/null 2>&1; then
            echo "  ✓ Durchlauf $i erfolgreich"
        else
            echo "  ✗ Durchlauf $i fehlgeschlagen"
            COMPILE_SUCCESS=false
            break
        fi
    done
    
    cd - > /dev/null
    
    # Wenn erfolgreich, verschiebe PDF
    if [ "$COMPILE_SUCCESS" = true ]; then
        PDF_NAME="${BASENAME%.tex}.pdf"
        if [ -f "$PROCESSED_DIR/$PDF_NAME" ]; then
            mv "$PROCESSED_DIR/$PDF_NAME" "$PDF_DIR/$PDF_NAME"
            SUCCESS=$((SUCCESS + 1))
            echo "  ✓ PDF erstellt: $PDF_NAME"
            
            # Füge zu Links hinzu
            echo "$SUCCESS. 2/pdf/$PDF_NAME" >> pdf_links_with_numbers.txt
        fi
    else
        FAILED=$((FAILED + 1))
        echo "  ✗ Kompilierung fehlgeschlagen"
    fi
    
    # Aufräumen
    rm -f "$PROCESSED_DIR"/*.aux "$PROCESSED_DIR"/*.log "$PROCESSED_DIR"/*.out "$PROCESSED_DIR"/*.toc "$PROCESSED_DIR"/*.synctex.gz
    
    echo ""
done

echo "=== BATCH-VERARBEITUNG ABGESCHLOSSEN ==="
echo "Verarbeitet: $TOTAL"
echo "Erfolgreich: $SUCCESS"
echo "Fehlgeschlagen: $FAILED"
