#!/bin/bash
# build_epub.sh — Build EPUB for T0 erklärt Band 1 (populärwissenschaftliche Ausgabe)
# Copyright © 2025 J. Pascher. Licensed under CC BY 4.0.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Building T0 erklärt Band 1 EPUB ==="

# Input file
INPUT_MD="book1_popularwissenschaft_de.md"
OUTPUT_EPUB="T0_erklaert_Band1_de.epub"
COVER_PNG="cover.png"

# Check if input exists
if [ ! -f "$INPUT_MD" ]; then
    echo "ERROR: Input file $INPUT_MD not found!"
    exit 1
fi

# Generate a simple cover image using ImageMagick (if not exists)
if [ ! -f "$COVER_PNG" ]; then
    echo "Generating cover image..."
    # Use system default font with fallback (Ubuntu has DejaVu fonts installed)
    FONT="DejaVu-Sans"
    FONT_BOLD="DejaVu-Sans-Bold"
    # Check if fonts are available, otherwise use default
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
        # Fallback: simple cover without specific fonts
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
else
    echo "Cover image already exists: $COVER_PNG"
fi

# Build EPUB using pandoc
echo "Building EPUB with pandoc..."
pandoc "$INPUT_MD" \
    --from markdown \
    --to epub3 \
    --output "$OUTPUT_EPUB" \
    --epub-cover-image="$COVER_PNG" \
    --metadata title="T0 erklärt: Zeit, Masse und die Geometrie der Natur" \
    --metadata author="J. Pascher" \
    --metadata lang="de" \
    --metadata date="2025" \
    --toc \
    --toc-depth=2

echo "=== Build complete ==="
echo "Output: $OUTPUT_EPUB"
ls -la "$OUTPUT_EPUB" "$COVER_PNG"
