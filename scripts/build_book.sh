#!/bin/bash
# Build script for T0 Book 1
# This script compiles the markdown chapters into a PDF

set -e

BOOK_DIR="book1/Book1_T0_erklaert_de"
OUTPUT_DIR="$BOOK_DIR/output"

echo "=== T0 Book 1 Build Script ==="
echo "Building from: $BOOK_DIR"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Check for pandoc
if ! command -v pandoc &> /dev/null; then
    echo "Error: pandoc is not installed"
    exit 1
fi

# Combine all chapters
echo "Combining chapters..."
cat "$BOOK_DIR/chapters/"*.md > "$OUTPUT_DIR/combined_book.md"

# Convert to PDF if LaTeX is available
if command -v pdflatex &> /dev/null; then
    echo "Converting to PDF..."
    pandoc "$OUTPUT_DIR/combined_book.md" \
        -o "$OUTPUT_DIR/T0_Book1_erklaert.pdf" \
        --pdf-engine=pdflatex \
        -V geometry:margin=2.5cm \
        -V fontsize=11pt \
        --toc \
        --toc-depth=2 \
        -V title="T0 Theory Explained" \
        -V author="Johann Pascher" \
        -V date="$(date +%Y-%m-%d)"
    echo "PDF created: $OUTPUT_DIR/T0_Book1_erklaert.pdf"
else
    echo "Note: pdflatex not available, skipping PDF generation"
    echo "Markdown combined at: $OUTPUT_DIR/combined_book.md"
fi

echo "=== Build complete ==="
