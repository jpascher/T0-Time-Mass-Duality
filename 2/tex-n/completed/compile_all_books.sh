#!/bin/bash

echo "=== Recursive Compilation of All Books ==="
echo "Starting 3-pass compilation for all 6 books..."
echo ""

BOOKS=("Teil1_De.tex" "Teil1_En.tex" "Teil2_De.tex" "Teil2_En.tex" "Teil3_De.tex" "Teil3_En.tex")
SUCCESS_COUNT=0
FAIL_COUNT=0
FAILED_BOOKS=()

for book in "${BOOKS[@]}"; do
    echo "----------------------------------------"
    echo "Compiling: $book"
    echo "----------------------------------------"
    
    # Run pdflatex 3 times
    for pass in 1 2 3; do
        echo "Pass $pass/3..."
        pdflatex -interaction=nonstopmode -halt-on-error "$book" > /dev/null 2>&1
        if [ $? -ne 0 ]; then
            echo "❌ Compilation FAILED on pass $pass"
            FAIL_COUNT=$((FAIL_COUNT + 1))
            FAILED_BOOKS+=("$book")
            break
        fi
    done
    
    if [ $? -eq 0 ]; then
        echo "✅ $book compiled successfully"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        
        # Get PDF size
        if [ -f "${book%.tex}.pdf" ]; then
            SIZE=$(ls -lh "${book%.tex}.pdf" | awk '{print $5}')
            echo "   PDF size: $SIZE"
        fi
    fi
    echo ""
done

echo "========================================"
echo "COMPILATION SUMMARY"
echo "========================================"
echo "✅ Successful: $SUCCESS_COUNT/6 books"
echo "❌ Failed: $FAIL_COUNT/6 books"

if [ $FAIL_COUNT -gt 0 ]; then
    echo ""
    echo "Failed books:"
    for failed in "${FAILED_BOOKS[@]}"; do
        echo "  - $failed"
    done
    exit 1
else
    echo ""
    echo "🎉 ALL BOOKS COMPILED SUCCESSFULLY!"
    exit 0
fi
