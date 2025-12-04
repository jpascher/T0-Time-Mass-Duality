#!/bin/bash
# ==============================================================================
# T0 Theory: LaTeX Compilation Script
# ==============================================================================
# This script recursively compiles all .tex files in the repository to PDF.
# 
# Usage:
#   ./compile_all_tex.sh [OPTIONS]
#
# Options:
#   -d, --dir DIR       Starting directory (default: current directory)
#   -o, --output DIR    Output directory for PDFs (default: same as source)
#   -j, --jobs N        Number of parallel jobs (default: 4)
#   -c, --clean         Clean auxiliary files after compilation
#   -v, --verbose       Verbose output
#   -h, --help          Show this help message
#
# Author: Johann Pascher
# Date: 2025
# ==============================================================================

set -e

# Default values
START_DIR="."
OUTPUT_DIR=""
JOBS=4
CLEAN=false
VERBOSE=false
MAX_RUNS=2

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
SUCCESS=0
FAILED=0
SKIPPED=0

# Usage function
usage() {
    echo "T0 Theory LaTeX Compilation Script"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -d, --dir DIR       Starting directory (default: current directory)"
    echo "  -o, --output DIR    Output directory for PDFs (default: same as source)"
    echo "  -j, --jobs N        Number of parallel jobs (default: 4)"
    echo "  -c, --clean         Clean auxiliary files after compilation"
    echo "  -v, --verbose       Verbose output"
    echo "  -h, --help          Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                          # Compile all .tex files in current directory"
    echo "  $0 -d 2/tex                 # Compile all .tex files in 2/tex directory"
    echo "  $0 -d 2/tex -o 2/pdf        # Compile and output PDFs to 2/pdf"
    echo "  $0 -c                       # Compile and clean auxiliary files"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -d|--dir)
            START_DIR="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -j|--jobs)
            JOBS="$2"
            shift 2
            ;;
        -c|--clean)
            CLEAN=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo -e "${RED}Error: pdflatex is not installed or not in PATH${NC}"
    echo "Please install TeX Live or another LaTeX distribution."
    exit 1
fi

# Resolve directories
START_DIR=$(realpath "$START_DIR")
if [[ -n "$OUTPUT_DIR" ]]; then
    OUTPUT_DIR=$(realpath -m "$OUTPUT_DIR")
    mkdir -p "$OUTPUT_DIR"
fi

echo "============================================================"
echo "T0 Theory LaTeX Compilation Script"
echo "============================================================"
echo "Source directory: $START_DIR"
if [[ -n "$OUTPUT_DIR" ]]; then
    echo "Output directory: $OUTPUT_DIR"
else
    echo "Output directory: Same as source"
fi
echo "Parallel jobs: $JOBS"
echo "Clean auxiliary: $CLEAN"
echo "============================================================"
echo ""

# Function to check if a file should be skipped
should_skip() {
    local filename=$(basename "$1")
    
    # Skip preamble files
    if [[ "$filename" == *"preamble"* ]]; then
        return 0
    fi
    
    # Skip chapter files (ending in _ch.tex)
    if [[ "$filename" == *"_ch.tex" ]]; then
        return 0
    fi
    
    # Skip pri*.tex files (unless it starts with principle)
    if [[ "$filename" == pri*.tex ]] && [[ "$filename" != principle*.tex ]]; then
        return 0
    fi
    
    # Skip t0_macros.tex and similar
    if [[ "$filename" == "t0_macros.tex" ]] || [[ "$filename" == "t0_pandoc_macros.tex" ]]; then
        return 0
    fi
    
    return 1
}

# Function to compile a single LaTeX file
compile_tex() {
    local tex_file="$1"
    local filename=$(basename "$tex_file")
    local dir=$(dirname "$tex_file")
    local basename="${filename%.tex}"
    
    # Skip certain files
    if should_skip "$tex_file"; then
        echo -e "${YELLOW}[SKIP]${NC} $filename (preamble/chapter/macro file)"
        return 2  # Skipped
    fi
    
    # Check if file contains \begin{document}
    if ! grep -q '\\begin{document}' "$tex_file" 2>/dev/null; then
        echo -e "${YELLOW}[SKIP]${NC} $filename (no \\begin{document})"
        return 2  # Skipped
    fi
    
    # Determine output directory
    local out_dir="$dir"
    if [[ -n "$OUTPUT_DIR" ]]; then
        out_dir="$OUTPUT_DIR"
    fi
    
    # Run pdflatex
    local success=true
    for run in $(seq 1 $MAX_RUNS); do
        if $VERBOSE; then
            echo "  Running pdflatex (pass $run) on $filename..."
        fi
        
        if ! pdflatex -interaction=nonstopmode -halt-on-error \
            -output-directory="$dir" "$tex_file" > /dev/null 2>&1; then
            success=false
            break
        fi
    done
    
    # Check if PDF was created
    local pdf_file="$dir/$basename.pdf"
    if [[ -f "$pdf_file" ]]; then
        # Move to output directory if different
        if [[ -n "$OUTPUT_DIR" ]] && [[ "$dir" != "$OUTPUT_DIR" ]]; then
            mv "$pdf_file" "$OUTPUT_DIR/"
        fi
        echo -e "${GREEN}[OK]${NC}   $filename"
        return 0
    else
        # Try to extract error from log
        local log_file="$dir/$basename.log"
        local error_msg=""
        if [[ -f "$log_file" ]]; then
            error_msg=$(grep -m1 "^!" "$log_file" 2>/dev/null | head -c 80 || echo "Unknown error")
        fi
        echo -e "${RED}[FAIL]${NC} $filename: $error_msg"
        return 1
    fi
}

# Function to clean auxiliary files
clean_aux() {
    local dir="$1"
    local patterns="*.aux *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz *.bbl *.blg *.nav *.snm *.vrb"
    
    for pattern in $patterns; do
        find "$dir" -name "$pattern" -type f -delete 2>/dev/null || true
    done
}

# Export functions for parallel execution
export -f compile_tex should_skip
export VERBOSE MAX_RUNS OUTPUT_DIR
export RED GREEN YELLOW BLUE NC

# Find all .tex files and compile them
echo "Finding .tex files..."
TEX_FILES=$(find "$START_DIR" -name "*.tex" -type f | sort)
TOTAL=$(echo "$TEX_FILES" | wc -l)
echo "Found $TOTAL .tex files"
echo ""

# Process files
if command -v parallel &> /dev/null && [[ $JOBS -gt 1 ]]; then
    # Use GNU parallel if available
    echo "Using GNU parallel with $JOBS jobs..."
    echo "$TEX_FILES" | parallel -j "$JOBS" compile_tex {}
else
    # Sequential processing
    echo "Processing files sequentially..."
    while IFS= read -r tex_file; do
        if [[ -n "$tex_file" ]]; then
            compile_tex "$tex_file"
            result=$?
            case $result in
                0) ((SUCCESS++)) ;;
                1) ((FAILED++)) ;;
                2) ((SKIPPED++)) ;;
            esac
        fi
    done <<< "$TEX_FILES"
fi

# Clean auxiliary files if requested
if $CLEAN; then
    echo ""
    echo "Cleaning auxiliary files..."
    clean_aux "$START_DIR"
fi

echo ""
echo "============================================================"
echo "Summary:"
echo "  Successful: $SUCCESS"
echo "  Failed:     $FAILED"
echo "  Skipped:    $SKIPPED"
echo "============================================================"

# Return exit code based on failures
if [[ $FAILED -gt 0 ]]; then
    exit 1
fi
exit 0
