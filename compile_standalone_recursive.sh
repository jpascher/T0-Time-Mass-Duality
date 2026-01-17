#!/bin/bash

# Recursive compilation of standalone documents
# Learn from each compilation and fix issues

REPO_ROOT="/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality"
DE_DIR="$REPO_ROOT/2/tex-n/de_standalone"
EN_DIR="$REPO_ROOT/2/tex-n/en_standalone"
LOG_FILE="/tmp/recursive_compilation.log"

echo "=== RECURSIVE STANDALONE COMPILATION ===" > $LOG_FILE
echo "Started: $(date)" >> $LOG_FILE
echo "" >> $LOG_FILE

SUCCESS=0
FAILED=0
TOTAL=0

# Function to compile a single file
compile_file() {
    local file=$1
    local basename=$(basename "$file" .tex)
    
    TOTAL=$((TOTAL + 1))
    
    echo -ne "\r[$TOTAL] Compiling: $basename..."
    
    cd "$(dirname "$file")"
    local log_file="/tmp/${basename}_compile.log"
    lualatex -interaction=nonstopmode -halt-on-error "$basename.tex" > "$log_file" 2>&1
    
    if [ $? -eq 0 ]; then
        SUCCESS=$((SUCCESS + 1))
        echo -ne "\r[$TOTAL] ✓ $basename"
        echo "✓ SUCCESS: $basename" >> $LOG_FILE
        # Copy fresh PDF into central 2/pdf directory (overwrites older versions)
        if [ -f "${basename}.pdf" ]; then
            cp "${basename}.pdf" "$REPO_ROOT/2/pdf/${basename}.pdf"
        fi
        return 0
    else
        FAILED=$((FAILED + 1))
        echo -ne "\r[$TOTAL] ✗ $basename"
        echo "✗ FAILED: $basename" >> $LOG_FILE
        
        # Extract error
        error=$(grep -A3 "^!" "$log_file" | head -5)
        echo "$error" >> $LOG_FILE
        echo "" >> $LOG_FILE
        
        return 1
    fi
}

# Compile German standalone files
echo ""
echo "=== German Standalone Files ==="
echo ""

for file in "$DE_DIR"/*.tex; do
    if [ -f "$file" ]; then
        compile_file "$file"
        echo ""
    fi
done

# Compile English standalone files  
echo ""
echo "=== English Standalone Files ==="
echo ""

for file in "$EN_DIR"/*.tex; do
    if [ -f "$file" ]; then
        compile_file "$file"
        echo ""
    fi
done

# Summary
echo ""
echo "==================================="
echo "SUMMARY:"
echo "  Total:   $TOTAL"
echo "  Success: $SUCCESS"
echo "  Failed:  $FAILED"
echo "==================================="
echo ""
echo "Detailed log: $LOG_FILE"

# Show first few failures
if [ $FAILED -gt 0 ]; then
    echo ""
    echo "First failures:"
    grep "^✗" $LOG_FILE | head -10
fi

