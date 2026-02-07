#!/bin/bash
# Compile all LaTeX master documents with LuaLaTeX
# Following instructions from copilot-lualatex-all-tex.md

set -e

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

echo "=== LaTeX Master Document Compilation ==="
echo "Repository: $REPO_ROOT"
echo "Date: $(date)"
echo ""

# Create output directory
mkdir -p 2/pdf
OUTDIR="2/pdf"

# Clear previous error log
> tex_compile_errors.txt
> tex_compile_success.txt

echo "Output directory: $OUTDIR"
echo "Total master files to compile: $(wc -l < tex_master_files.txt)"
echo ""

# Counter variables
total=0
success=0
failed=0

# Compile each file
while IFS= read -r texfile; do
    total=$((total + 1))
    basename=$(basename "$texfile" .tex)
    
    echo "[$total] Compiling: $texfile"
    
    # Run latexmk with LuaLaTeX
    if latexmk -lualatex \
        -interaction=nonstopmode \
        -halt-on-error \
        -output-directory="$OUTDIR" \
        "$texfile" 2>&1 | tee "/tmp/${basename}_compile.log"; then
        
        echo "  ✓ SUCCESS: $texfile" | tee -a tex_compile_success.txt
        success=$((success + 1))
    else
        echo "  ✗ FAILED: $texfile" | tee -a tex_compile_errors.txt
        failed=$((failed + 1))
    fi
    
    echo ""
done < tex_master_files.txt

# Summary
echo "=== Compilation Summary ==="
echo "Total files: $total"
echo "Successful:  $success"
echo "Failed:      $failed"
echo ""
echo "Success rate: $(awk "BEGIN {printf \"%.1f\", ($success/$total)*100}")%"
echo ""

if [ $failed -gt 0 ]; then
    echo "Failed files logged in: tex_compile_errors.txt"
    echo "Check log files in: /tmp/*_compile.log"
    exit 1
else
    echo "All files compiled successfully!"
    exit 0
fi
