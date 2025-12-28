#!/bin/bash

################################################################################
# DVFT Chapter Compilation Script
# 
# This script recursively compiles all DVFT LaTeX chapter files with:
# - Multiple passes for cross-references and table of contents
# - Error handling and detailed logging
# - Support for both individual chapters and main document
# 
# Usage:
#   ./compile_dvft_chapters.sh [--all|--main|--chapter NUMBER]
#
# Author: Generated for T0 Theory Project
# Date: 2025-12-28
################################################################################

set -e  # Exit on error

# Configuration
REPO_ROOT="/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality"
DVFT_DIR="$REPO_ROOT/2/tex-n/de_standalone/dvft_latex_chapters"
LOG_DIR="/tmp/dvft_compilation_logs"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
MAIN_LOG="$LOG_DIR/compilation_${TIMESTAMP}.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Statistics
TOTAL=0
SUCCESS=0
FAILED=0
WARNINGS=0

################################################################################
# Functions
################################################################################

# Initialize logging
init_logging() {
    mkdir -p "$LOG_DIR"
    echo "================================================================================================" > "$MAIN_LOG"
    echo "DVFT LaTeX Compilation Log" >> "$MAIN_LOG"
    echo "Started: $(date)" >> "$MAIN_LOG"
    echo "Directory: $DVFT_DIR" >> "$MAIN_LOG"
    echo "================================================================================================" >> "$MAIN_LOG"
    echo "" >> "$MAIN_LOG"
}

# Print colored message
print_msg() {
    local color=$1
    shift
    echo -e "${color}$@${NC}"
}

# Print to both console and log
log_msg() {
    echo "$@" | tee -a "$MAIN_LOG"
}

# Compile a single LaTeX file with multiple passes
compile_latex_file() {
    local file=$1
    local basename=$(basename "$file" .tex)
    local dir=$(dirname "$file")
    local logfile="$LOG_DIR/${basename}_${TIMESTAMP}.log"
    
    TOTAL=$((TOTAL + 1))
    
    print_msg "$BLUE" "[$TOTAL] Compiling: $basename..."
    log_msg "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log_msg "Compiling: $basename.tex"
    log_msg "Directory: $dir"
    log_msg "Time: $(date)"
    log_msg ""
    
    cd "$dir"
    
    # First pass
    print_msg "$YELLOW" "  → Pass 1/3..."
    if sudo pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "$basename.tex" > "$logfile" 2>&1; then
        # Second pass (for cross-references)
        print_msg "$YELLOW" "  → Pass 2/3..."
        if sudo pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "$basename.tex" >> "$logfile" 2>&1; then
            # Third pass (to resolve all references)
            print_msg "$YELLOW" "  → Pass 3/3..."
            if sudo pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "$basename.tex" >> "$logfile" 2>&1; then
                # Check for warnings
                if grep -q "Warning" "$logfile"; then
                    WARNINGS=$((WARNINGS + 1))
                    print_msg "$YELLOW" "  ✓ $basename (with warnings)"
                    log_msg "STATUS: SUCCESS (with warnings)"
                else
                    print_msg "$GREEN" "  ✓ $basename"
                    log_msg "STATUS: SUCCESS"
                fi
                SUCCESS=$((SUCCESS + 1))
                log_msg "PDF created: ${basename}.pdf"
                
                # Clean up auxiliary files
                rm -f "${basename}.aux" "${basename}.log" "${basename}.out" "${basename}.toc" 2>/dev/null || true
                
                return 0
            fi
        fi
    fi
    
    # If we get here, compilation failed
    FAILED=$((FAILED + 1))
    print_msg "$RED" "  ✗ $basename FAILED"
    log_msg "STATUS: FAILED"
    log_msg ""
    log_msg "Error details:"
    
    # Extract and display errors
    if [ -f "$logfile" ]; then
        # Get the last error from the log
        grep -A5 "^!" "$logfile" | head -20 | tee -a "$MAIN_LOG"
        
        # Also look for specific error patterns
        if grep -q "File.*not found" "$logfile"; then
            log_msg ""
            log_msg "Missing files:"
            grep "File.*not found" "$logfile" | tee -a "$MAIN_LOG"
        fi
    fi
    
    log_msg ""
    log_msg "Full log saved to: $logfile"
    
    return 1
}

# Compile all chapter files
compile_all_chapters() {
    print_msg "$BLUE" "\n================================================================================================"
    print_msg "$BLUE" "Compiling All DVFT Chapters"
    print_msg "$BLUE" "================================================================================================\n"
    
    local chapter_count=0
    
    # Compile chapters in order
    for i in $(seq -f "%02g" 0 43); do
        local chapter_file="$DVFT_DIR/kapitel_${i}.tex"
        if [ -f "$chapter_file" ]; then
            compile_latex_file "$chapter_file"
            chapter_count=$((chapter_count + 1))
            echo ""
        fi
    done
    
    log_msg "Compiled $chapter_count chapter files"
}

# Compile the main document
compile_main_document() {
    print_msg "$BLUE" "\n================================================================================================"
    print_msg "$BLUE" "Compiling Main Document"
    print_msg "$BLUE" "================================================================================================\n"
    
    local main_file="$DVFT_DIR/main_complete.tex"
    
    if [ -f "$main_file" ]; then
        compile_latex_file "$main_file"
    else
        print_msg "$RED" "Error: Main file not found: $main_file"
        log_msg "ERROR: Main file not found"
        return 1
    fi
}

# Compile a specific chapter
compile_specific_chapter() {
    local chapter_num=$1
    local chapter_file="$DVFT_DIR/kapitel_${chapter_num}.tex"
    
    print_msg "$BLUE" "\n================================================================================================"
    print_msg "$BLUE" "Compiling Chapter $chapter_num"
    print_msg "$BLUE" "================================================================================================\n"
    
    if [ -f "$chapter_file" ]; then
        compile_latex_file "$chapter_file"
    else
        print_msg "$RED" "Error: Chapter file not found: $chapter_file"
        log_msg "ERROR: Chapter file not found"
        return 1
    fi
}

# Print summary
print_summary() {
    local end_time=$(date)
    
    print_msg "$BLUE" "\n================================================================================================"
    print_msg "$BLUE" "COMPILATION SUMMARY"
    print_msg "$BLUE" "================================================================================================\n"
    
    log_msg "Finished: $end_time"
    log_msg ""
    log_msg "Statistics:"
    log_msg "  Total files:    $TOTAL"
    log_msg "  Successful:     $SUCCESS"
    log_msg "  Failed:         $FAILED"
    log_msg "  With warnings:  $WARNINGS"
    log_msg ""
    
    if [ $SUCCESS -gt 0 ]; then
        print_msg "$GREEN" "✓ Successfully compiled: $SUCCESS files"
    fi
    
    if [ $WARNINGS -gt 0 ]; then
        print_msg "$YELLOW" "⚠ Warnings in: $WARNINGS files"
    fi
    
    if [ $FAILED -gt 0 ]; then
        print_msg "$RED" "✗ Failed: $FAILED files"
        log_msg ""
        log_msg "Failed files:"
        grep "FAILED" "$MAIN_LOG" | tee -a /dev/stderr
    fi
    
    log_msg ""
    log_msg "Full log: $MAIN_LOG"
    log_msg "Individual logs: $LOG_DIR/*_${TIMESTAMP}.log"
    
    print_msg "$BLUE" "\nDetailed log saved to: $MAIN_LOG"
}

################################################################################
# Main Script
################################################################################

main() {
    local mode="${1:-all}"
    
    # Print header
    print_msg "$BLUE" "\n================================================================================================"
    print_msg "$BLUE" "DVFT LaTeX Compilation Script"
    print_msg "$BLUE" "================================================================================================\n"
    
    # Check if directory exists
    if [ ! -d "$DVFT_DIR" ]; then
        print_msg "$RED" "Error: DVFT directory not found: $DVFT_DIR"
        exit 1
    fi
    
    # Initialize logging
    init_logging
    
    # Parse command line arguments
    case "$mode" in
        --all)
            compile_all_chapters
            ;;
        --main)
            compile_main_document
            ;;
        --chapter)
            if [ -z "$2" ]; then
                print_msg "$RED" "Error: Chapter number required"
                echo "Usage: $0 --chapter NUMBER"
                exit 1
            fi
            compile_specific_chapter "$2"
            ;;
        *)
            # Default: compile all
            compile_all_chapters
            ;;
    esac
    
    # Print summary
    print_summary
    
    # Exit with appropriate code
    if [ $FAILED -gt 0 ]; then
        exit 1
    else
        exit 0
    fi
}

# Run main function with all arguments
main "$@"
