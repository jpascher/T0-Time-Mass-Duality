#!/bin/bash
# Iterative document-by-document compilation and fixing
# Process each LaTeX document individually, analyze errors, and fix them minimally

set -e

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

echo "=== Iterative LaTeX Document Processing ==="
echo "Repository: $REPO_ROOT"
echo "Date: $(date)"
echo ""

# Create output directory
mkdir -p 2/pdf
OUTDIR="2/pdf"

# Create work files
> document_processing_log.txt
> documents_to_fix.txt
> documents_completed.txt

# Function to analyze log file for errors
analyze_errors() {
    local logfile="$1"
    local texfile="$2"
    
    echo "Analyzing errors in: $logfile" >> document_processing_log.txt
    
    # Check for common LaTeX errors
    if grep -q "Undefined control sequence" "$logfile"; then
        echo "  ERROR: Undefined control sequence" | tee -a document_processing_log.txt
        grep -A 3 "Undefined control sequence" "$logfile" | head -10 | tee -a document_processing_log.txt
    fi
    
    if grep -q "Environment .* undefined" "$logfile"; then
        echo "  ERROR: Undefined environment" | tee -a document_processing_log.txt
        grep -A 2 "Environment .* undefined" "$logfile" | head -10 | tee -a document_processing_log.txt
    fi
    
    if grep -q "Missing \\\\begin{document}" "$logfile"; then
        echo "  ERROR: Missing begin document" | tee -a document_processing_log.txt
    fi
    
    if grep -q "File .* not found" "$logfile"; then
        echo "  ERROR: File not found" | tee -a document_processing_log.txt
        grep "File .* not found" "$logfile" | head -5 | tee -a document_processing_log.txt
    fi
    
    if grep -q "Package .* Error" "$logfile"; then
        echo "  ERROR: Package error" | tee -a document_processing_log.txt
        grep -A 2 "Package .* Error" "$logfile" | head -10 | tee -a document_processing_log.txt
    fi
    
    # Extract first real error line number
    grep -n "^!" "$logfile" | head -1 | tee -a document_processing_log.txt
}

# Process documents one by one
doc_count=0
max_docs=${1:-10}  # Default to first 10 documents, or use argument

echo "Processing first $max_docs documents..."
echo ""

while IFS= read -r texfile && [ $doc_count -lt $max_docs ]; do
    doc_count=$((doc_count + 1))
    basename=$(basename "$texfile" .tex)
    logfile="/tmp/${basename}_compile.log"
    
    echo "=== [$doc_count/$max_docs] Processing: $texfile ==="
    echo ""
    
    # Try to compile
    echo "Compiling with LuaLaTeX..."
    
    # Get the directory of the tex file for proper path resolution
    texdir=$(dirname "$texfile")
    texbase=$(basename "$texfile")
    
    # Change to the tex file's directory before compiling
    (cd "$texdir" && latexmk -lualatex \
        -interaction=nonstopmode \
        -halt-on-error \
        "$texbase") > "$logfile" 2>&1
    
    if [ $? -eq 0 ]; then
        
        echo "✓ SUCCESS: $texfile"
        echo "$texfile" >> documents_completed.txt
        
        # Move PDF to output directory
        pdffile="$texdir/${basename}.pdf"
        if [ -f "$pdffile" ]; then
            mv "$pdffile" "$OUTDIR/"
            echo "  PDF moved to: $OUTDIR/${basename}.pdf ($(du -h "$OUTDIR/${basename}.pdf" | cut -f1))"
        fi
    else
        echo "✗ FAILED: $texfile"
        echo "$texfile" >> documents_to_fix.txt
        
        # Analyze the error
        echo ""
        echo "Error Analysis:"
        if [ -f "$logfile" ]; then
            analyze_errors "$logfile" "$texfile"
        fi
        
        echo ""
        echo "To fix this document:"
        echo "  1. Check log: $logfile"
        echo "  2. Edit: $texfile"
        echo "  3. Re-run this script"
    fi
    
    echo ""
    echo "---"
    echo ""
    
done < tex_master_files.txt

# Summary
echo ""
echo "=== Processing Summary ==="
echo "Documents processed: $doc_count"
echo "Completed successfully: $(wc -l < documents_completed.txt 2>/dev/null || echo 0)"
echo "Need fixing: $(wc -l < documents_to_fix.txt 2>/dev/null || echo 0)"
echo ""
echo "Detailed log: document_processing_log.txt"

if [ -s documents_to_fix.txt ]; then
    echo ""
    echo "Documents that need fixing:"
    cat documents_to_fix.txt
    echo ""
    echo "Next steps:"
    echo "1. Review errors in document_processing_log.txt"
    echo "2. Fix the identified LaTeX errors minimally"
    echo "3. Re-run this script to continue"
fi
