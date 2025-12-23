#!/bin/bash
# build_print.sh — Build print-ready PDF for T0 erklärt Band 1 (populärwissenschaftliche Ausgabe)
# Copyright © 2025 J. Pascher. Licensed under CC BY 4.0.
#
# Output: print_output/T0_erklaert_Band1_de.pdf (A5 format, suitable for book printing)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Building T0 erklärt Band 1 Print PDF ==="

# Input file
INPUT_MD="book1_popularwissenschaft_de.md"
OUTPUT_DIR="print_output"
OUTPUT_PDF="${OUTPUT_DIR}/T0_erklaert_Band1_de.pdf"
COVER_PNG="cover.png"

# Check if input exists
if [ ! -f "$INPUT_MD" ]; then
    echo "ERROR: Input file $INPUT_MD not found!"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Generate cover if needed (reuse from EPUB build)
if [ ! -f "$COVER_PNG" ]; then
    echo "Generating cover image..."
    FONT="DejaVu-Sans"
    FONT_BOLD="DejaVu-Sans-Bold"
    if ! convert -list font 2>/dev/null | grep -q "DejaVu-Sans"; then
        echo "Warning: DejaVu fonts not found, using system defaults"
        FONT=""
        FONT_BOLD=""
    fi
    
    if [ -n "$FONT" ]; then
        convert -size 600x800 xc:'#1a1a2e' \
            -font "$FONT_BOLD" -pointsize 36 -fill '#eaeaea' \
            -gravity North -annotate +0+120 'T0 erklärt' \
            -font "$FONT" -pointsize 24 -fill '#cccccc' \
            -gravity North -annotate +0+180 'Band 1' \
            -font "$FONT" -pointsize 18 -fill '#888888' \
            -gravity North -annotate +0+230 'Zeit, Masse und die Geometrie der Natur' \
            -font "$FONT" -pointsize 14 -fill '#666666' \
            -gravity South -annotate +0+60 'J. Pascher' \
            -font "$FONT" -pointsize 12 -fill '#555555' \
            -gravity South -annotate +0+30 'Populärwissenschaftliche Reihe' \
            "$COVER_PNG"
    else
        convert -size 600x800 xc:'#1a1a2e' \
            -pointsize 36 -fill '#eaeaea' \
            -gravity North -annotate +0+120 'T0 erklärt' \
            -pointsize 24 -fill '#cccccc' \
            -gravity North -annotate +0+180 'Band 1' \
            -pointsize 18 -fill '#888888' \
            -gravity North -annotate +0+230 'Zeit, Masse und die Geometrie der Natur' \
            -pointsize 14 -fill '#666666' \
            -gravity South -annotate +0+60 'J. Pascher' \
            -pointsize 12 -fill '#555555' \
            -gravity South -annotate +0+30 'Populärwissenschaftliche Reihe' \
            "$COVER_PNG"
    fi
    echo "Cover image generated: $COVER_PNG"
fi

# Copy cover to output directory
cp "$COVER_PNG" "${OUTPUT_DIR}/cover.png"

# Check for LaTeX engine
PDF_ENGINE=""
for engine in xelatex lualatex pdflatex; do
    if command -v "$engine" &>/dev/null; then
        PDF_ENGINE="$engine"
        echo "Using PDF engine: $PDF_ENGINE"
        break
    fi
done

if [ -z "$PDF_ENGINE" ]; then
    echo "WARNING: No LaTeX engine found (xelatex, lualatex, pdflatex)."
    echo "Falling back to wkhtmltopdf or simple pandoc PDF..."
    
    if command -v wkhtmltopdf &>/dev/null; then
        echo "Using wkhtmltopdf..."
        # First convert to HTML, then to PDF
        pandoc "$INPUT_MD" \
            --from markdown \
            --to html5 \
            --standalone \
            --metadata title="T0 erklärt: Zeit, Masse und die Geometrie der Natur" \
            --metadata author="J. Pascher" \
            --metadata lang="de" \
            --toc \
            --toc-depth=2 \
            -o "${OUTPUT_DIR}/temp.html"
        
        wkhtmltopdf --page-size A5 --margin-top 20mm --margin-bottom 20mm \
            --margin-left 15mm --margin-right 15mm \
            "${OUTPUT_DIR}/temp.html" "$OUTPUT_PDF"
        rm -f "${OUTPUT_DIR}/temp.html"
    else
        echo "ERROR: No PDF generation tool available. Please install texlive or wkhtmltopdf."
        exit 1
    fi
else
    # Build PDF using pandoc with LaTeX
    echo "Building print PDF with pandoc + $PDF_ENGINE..."
    pandoc "$INPUT_MD" \
        --from markdown \
        --to pdf \
        --pdf-engine="$PDF_ENGINE" \
        --output "$OUTPUT_PDF" \
        --metadata title="T0 erklärt: Zeit, Masse und die Geometrie der Natur" \
        --metadata author="J. Pascher" \
        --metadata lang="de" \
        --metadata date="2025" \
        --toc \
        --toc-depth=2 \
        -V geometry:a5paper \
        -V geometry:margin=2cm \
        -V fontsize=11pt \
        -V documentclass=book \
        -V mainfont="DejaVu Serif" \
        -V sansfont="DejaVu Sans" \
        -V monofont="DejaVu Sans Mono" \
        -V linkcolor=blue \
        -V urlcolor=blue \
        -V toccolor=black
fi

echo "=== Print build complete ==="
echo "Output directory: $OUTPUT_DIR"
ls -la "$OUTPUT_DIR"
