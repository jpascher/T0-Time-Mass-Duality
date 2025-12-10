#!/bin/bash

echo "=== Recursive Compilation of All Books (3 passes each) ==="
echo ""

BOOKS=("Teil1_De" "Teil1_En" "Teil2_De" "Teil2_En" "Teil3_De" "Teil3_En")
SUCCESS_COUNT=0
FAIL_COUNT=0
declare -a FAILED_BOOKS

for book in "${BOOKS[@]}"; do
    echo "========================================"
    echo "📚 Compiling: ${book}.tex"
    echo "========================================"
    
    FAILED=0
    
    for pass in 1 2 3; do
        echo -n "Pass $pass/3... "
        pdflatex -interaction=nonstopmode "${book}.tex" > "${book}_pass${pass}.log" 2>&1
        
        if [ $? -ne 0 ]; then
            echo "❌ FAILED"
            echo ""
            echo "Last 30 lines of error log:"
            tail -30 "${book}_pass${pass}.log"
            FAILED=1
            break
        else
            echo "✅ OK"
        fi
    done
    
    if [ $FAILED -eq 0 ] && [ -f "${book}.pdf" ]; then
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        SIZE=$(ls -lh "${book}.pdf" | awk '{print $5}')
        PAGES=$(pdfinfo "${book}.pdf" 2>/dev/null | grep "Pages:" | awk '{print $2}')
        echo ""
        echo "✅ ${book}.pdf created successfully"
        echo "   Size: $SIZE"
        if [ ! -z "$PAGES" ]; then
            echo "   Pages: $PAGES"
        fi
    else
        FAIL_COUNT=$((FAIL_COUNT + 1))
        FAILED_BOOKS+=("$book")
        echo ""
        echo "❌ ${book}.pdf compilation FAILED"
    fi
    echo ""
done

echo "========================================"
echo "📊 COMPILATION SUMMARY"
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
