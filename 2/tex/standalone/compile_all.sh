#!/bin/bash
# Compile all standalone LaTeX documents to PDF
# Usage: ./compile_all.sh [language]
# Examples:
#   ./compile_all.sh        # Compile all languages
#   ./compile_all.sh en     # Compile only English
#   ./compile_all.sh de     # Compile only German

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LANGUAGES="${1:-en de fr es}"

compile_language() {
    local lang=$1
    local lang_dir="$SCRIPT_DIR/$lang"
    
    if [ ! -d "$lang_dir" ]; then
        echo "Directory $lang_dir not found, skipping..."
        return
    fi
    
    echo "=========================================="
    echo "Compiling $lang documents..."
    echo "=========================================="
    
    cd "$lang_dir"
    
    # Count files
    local total=$(ls -1 *.tex 2>/dev/null | wc -l)
    local count=0
    local success=0
    local failed=0
    
    for texfile in *.tex; do
        if [ -f "$texfile" ]; then
            count=$((count + 1))
            echo "[$count/$total] Compiling $texfile..."
            
            # Run pdflatex twice for references
            if pdflatex -interaction=nonstopmode "$texfile" > /dev/null 2>&1; then
                pdflatex -interaction=nonstopmode "$texfile" > /dev/null 2>&1
                success=$((success + 1))
                echo "  ✓ Success: ${texfile%.tex}.pdf"
            else
                failed=$((failed + 1))
                echo "  ✗ Failed: $texfile"
            fi
            
            # Clean up auxiliary files
            rm -f "${texfile%.tex}.aux" "${texfile%.tex}.log" "${texfile%.tex}.out" \
                  "${texfile%.tex}.toc" "${texfile%.tex}.lof" "${texfile%.tex}.lot" \
                  "${texfile%.tex}.bbl" "${texfile%.tex}.blg" 2>/dev/null
        fi
    done
    
    echo ""
    echo "Results for $lang: $success success, $failed failed out of $total files"
    echo ""
}

echo "T0 Standalone Document Compiler"
echo "================================"
echo ""

for lang in $LANGUAGES; do
    compile_language "$lang"
done

echo "=========================================="
echo "Compilation complete!"
echo "=========================================="
