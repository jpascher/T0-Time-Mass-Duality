#!/bin/bash
# Test compilation of first 10 master documents
# To verify the compilation setup works

set -e

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

echo "=== TEST: LaTeX Compilation (First 10 Files) ==="
echo "Repository: $REPO_ROOT"
echo ""

# Create output directory
mkdir -p 2/pdf
OUTDIR="2/pdf"

# Clear test logs
> tex_compile_test_errors.txt
> tex_compile_test_success.txt

# Counter variables
total=0
success=0
failed=0

# Compile first 10 files
head -10 tex_master_files.txt | while IFS= read -r texfile; do
    total=$((total + 1))
    basename=$(basename "$texfile" .tex)
    
    echo "[$total/10] Compiling: $texfile"
    
    # Run latexmk with LuaLaTeX
    if latexmk -lualatex \
        -interaction=nonstopmode \
        -halt-on-error \
        -output-directory="$OUTDIR" \
        "$texfile" > "/tmp/${basename}_compile.log" 2>&1; then
        
        echo "  ✓ SUCCESS"
        echo "$texfile" >> tex_compile_test_success.txt
        success=$((success + 1))
    else
        echo "  ✗ FAILED (check /tmp/${basename}_compile.log)"
        echo "$texfile" >> tex_compile_test_errors.txt
        failed=$((failed + 1))
    fi
    
    echo ""
done

# Summary
echo "=== Test Compilation Summary ==="
echo "Total: 10 files"
echo "Success: $(wc -l < tex_compile_test_success.txt 2>/dev/null || echo 0)"
echo "Failed: $(wc -l < tex_compile_test_errors.txt 2>/dev/null || echo 0)"

if [ -s tex_compile_test_errors.txt ]; then
    echo ""
    echo "Failed files:"
    cat tex_compile_test_errors.txt
fi
