#!/bin/bash
# ==============================================================================
# T0 Theory: DVFT LaTeX Compilation Script with Auto-Fixing
# ==============================================================================
# This script recursively compiles all LaTeX chapter files (kapitel_00.tex to
# kapitel_43.tex) and main.tex using pdflatex with physics package support.
# It attempts to automatically fix common LaTeX errors until all files compile
# successfully.
#
# Usage:
#   sudo ./compile_all_dvft.sh [OPTIONS]
#
# Options:
#   -p, --passes NUM      Number of compilation passes per file (default: 3)
#   -l, --log FILE        Error log file (default: dvft_compilation_errors.log)
#   -v, --verbose         Verbose output
#   -h, --help            Show this help message
#   --no-fix              Disable automatic error fixing
#   --dry-run             Show what would be done without making changes
#
# Author: Johann Pascher
# Date: 2025-12-28
# ==============================================================================

set -o pipefail

# Default values
MAX_PASSES=3
LOG_FILE="dvft_compilation_errors.log"
VERBOSE=false
AUTO_FIX=true
DRY_RUN=false
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Counters
SUCCESS=0
FAILED=0
FIXED=0
TOTAL=0

# Usage function
usage() {
    echo "T0 Theory DVFT LaTeX Compilation Script"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -p, --passes NUM      Number of compilation passes per file (default: 3)"
    echo "  -l, --log FILE        Error log file (default: dvft_compilation_errors.log)"
    echo "  -v, --verbose         Verbose output"
    echo "  -h, --help            Show this help message"
    echo "  --no-fix              Disable automatic error fixing"
    echo "  --dry-run             Show what would be done without making changes"
    echo ""
    echo "Examples:"
    echo "  sudo $0                      # Compile all files with default settings"
    echo "  sudo $0 -v -p 4              # Verbose mode with 4 passes per file"
    echo "  sudo $0 --no-fix             # Compile without automatic error fixing"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -p|--passes)
            MAX_PASSES="$2"
            shift 2
            ;;
        -l|--log)
            LOG_FILE="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        --no-fix)
            AUTO_FIX=false
            shift
            ;;
        --dry-run)
            DRY_RUN=true
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

# Check if running as root (required for sudo pdflatex)
if [ "$EUID" -ne 0 ] && [ "$DRY_RUN" = false ]; then
    echo -e "${RED}Error: This script requires root privileges (sudo)${NC}"
    echo "Please run with: sudo $0"
    exit 1
fi

# Check if pdflatex is available (skip for dry-run)
if [ "$DRY_RUN" = false ] && ! command -v pdflatex &> /dev/null; then
    echo -e "${RED}Error: pdflatex is not installed or not in PATH${NC}"
    echo "Please install TeX Live or another LaTeX distribution."
    exit 1
fi

# Initialize log file
LOG_PATH="$SCRIPT_DIR/$LOG_FILE"
# Try to create log file, warn if it fails but continue
if ! touch "$LOG_PATH" 2>/dev/null; then
    echo -e "${YELLOW}Warning: Cannot write to log file: $LOG_PATH${NC}"
    LOG_PATH="/tmp/dvft_compilation_errors.log"
    echo -e "Using temporary log file: ${CYAN}$LOG_PATH${NC}"
    touch "$LOG_PATH" 2>/dev/null || {
        echo -e "${RED}Error: Cannot create log file. Check permissions.${NC}"
        exit 1
    }
fi

echo "============================================================" > "$LOG_PATH"
echo "DVFT LaTeX Compilation Log" >> "$LOG_PATH"
echo "Date: $(date)" >> "$LOG_PATH"
echo "============================================================" >> "$LOG_PATH"
echo "" >> "$LOG_PATH"

echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}T0 Theory DVFT LaTeX Compilation Script${NC}"
echo -e "${BLUE}============================================================${NC}"
echo -e "Working directory: ${CYAN}$SCRIPT_DIR${NC}"
echo -e "Error log file: ${CYAN}$LOG_PATH${NC}"
echo -e "Compilation passes: ${CYAN}$MAX_PASSES${NC}"
echo -e "Auto-fix errors: ${CYAN}$AUTO_FIX${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""

# Function to check if a LaTeX package is installed
is_package_installed() {
    local package="$1"
    kpsewhich "$package.sty" &> /dev/null
    return $?
}

# Function to install missing LaTeX packages
install_package() {
    local package="$1"
    
    echo -e "${YELLOW}Installing LaTeX package: $package${NC}" | tee -a "$LOG_PATH"
    
    if [ "$DRY_RUN" = true ]; then
        echo "[DRY-RUN] Would install package: $package"
        return 0
    fi
    
    # Try to install via tlmgr if available
    if command -v tlmgr &> /dev/null; then
        tlmgr install "$package" >> "$LOG_PATH" 2>&1
        return $?
    fi
    
    # Try apt-get for Debian/Ubuntu systems
    # Map common package names to apt package names
    if command -v apt-get &> /dev/null; then
        case "$package" in
            physics|siunitx|geometry|hyperref|amsmath|graphicx)
                apt-get install -y "texlive-latex-extra" >> "$LOG_PATH" 2>&1
                ;;
            *)
                apt-get install -y "texlive-full" >> "$LOG_PATH" 2>&1
                ;;
        esac
        return $?
    fi
    
    return 1
}

# Function to extract and fix common LaTeX errors
analyze_and_fix_errors() {
    local tex_file="$1"
    local log_file="$2"
    local fixed=false
    
    if [ ! -f "$log_file" ]; then
        return 1
    fi
    
    # Extract errors from log file
    local errors=$(grep "^!" "$log_file" | head -5)
    
    if [ -z "$errors" ]; then
        return 1
    fi
    
    echo "" >> "$LOG_PATH"
    echo "Analyzing errors in: $(basename "$tex_file")" >> "$LOG_PATH"
    echo "$errors" >> "$LOG_PATH"
    echo "" >> "$LOG_PATH"
    
    if [ "$AUTO_FIX" = false ]; then
        return 1
    fi
    
    # Fix 1: Missing physics package
    if echo "$errors" | grep -q "physics.sty"; then
        echo -e "${YELLOW}Fixing: Missing physics package${NC}"
        if ! is_package_installed "physics"; then
            install_package "physics"
            fixed=true
        fi
    fi
    
    # Fix 2: Undefined control sequence
    if echo "$errors" | grep -q "Undefined control sequence"; then
        # Check for common missing commands
        if grep -q "\\bra\|\\ket\|\\braket" "$tex_file" && ! grep -q "\\usepackage{physics}" "$tex_file"; then
            echo -e "${YELLOW}Fixing: Adding physics package for quantum notation${NC}"
            if [ "$DRY_RUN" = false ]; then
                # Add physics package after documentclass
                sed -i '/\\documentclass/a \\usepackage{physics}' "$tex_file"
                fixed=true
            fi
        fi
        
        if grep -q "\\qty\|\\SI" "$tex_file" && ! grep -q "\\usepackage{siunitx}" "$tex_file"; then
            echo -e "${YELLOW}Fixing: Adding siunitx package for units${NC}"
            if [ "$DRY_RUN" = false ]; then
                sed -i '/\\documentclass/a \\usepackage{siunitx}' "$tex_file"
                install_package "siunitx"
                fixed=true
            fi
        fi
    fi
    
    # Fix 3: Missing font
    if echo "$errors" | grep -q "Font.*not found"; then
        echo -e "${YELLOW}Fixing: Installing missing fonts${NC}"
        if command -v apt-get &> /dev/null && [ "$DRY_RUN" = false ]; then
            apt-get install -y texlive-fonts-recommended texlive-fonts-extra >> "$LOG_PATH" 2>&1
            fixed=true
        fi
    fi
    
    # Fix 4: Missing amsmath commands
    if echo "$errors" | grep -q "Undefined control sequence.*\\\\align\|Undefined control sequence.*\\\\equation" && ! grep -q "\\usepackage{amsmath}" "$tex_file"; then
        echo -e "${YELLOW}Fixing: Adding amsmath package${NC}"
        if [ "$DRY_RUN" = false ]; then
            sed -i '/\\documentclass/a \\usepackage{amsmath}' "$tex_file"
            fixed=true
        fi
    fi
    
    # Fix 5: Missing graphicx
    if echo "$errors" | grep -q "Undefined control sequence.*\\\\includegraphics" && ! grep -q "\\usepackage{graphicx}" "$tex_file"; then
        echo -e "${YELLOW}Fixing: Adding graphicx package${NC}"
        if [ "$DRY_RUN" = false ]; then
            sed -i '/\\documentclass/a \\usepackage{graphicx}' "$tex_file"
            fixed=true
        fi
    fi
    
    # Fix 6: UTF-8 input encoding issues
    if echo "$errors" | grep -q "inputenc\|Unicode"; then
        echo -e "${YELLOW}Fixing: Adding UTF-8 input encoding${NC}"
        if [ "$DRY_RUN" = false ]; then
            if ! grep -q "\\usepackage\[utf8\]{inputenc}" "$tex_file"; then
                sed -i '/\\documentclass/a \\usepackage[utf8]{inputenc}' "$tex_file"
                fixed=true
            fi
        fi
    fi
    
    # Fix 7: Missing hyperref
    if echo "$errors" | grep -q "href\|hyperref" && ! grep -q "\\usepackage{hyperref}" "$tex_file"; then
        echo -e "${YELLOW}Fixing: Adding hyperref package${NC}"
        if [ "$DRY_RUN" = false ]; then
            sed -i '/\\documentclass/a \\usepackage{hyperref}' "$tex_file"
            fixed=true
        fi
    fi
    
    # Fix 8: Missing geometry package for margins
    if echo "$errors" | grep -q "geometry"; then
        if ! is_package_installed "geometry"; then
            install_package "geometry"
            fixed=true
        fi
    fi
    
    if [ "$fixed" = true ]; then
        echo -e "${GREEN}Applied automatic fixes to: $(basename "$tex_file")${NC}"
        return 0
    fi
    
    return 1
}

# Function to compile a single LaTeX file
compile_tex_file() {
    local tex_file="$1"
    local filename=$(basename "$tex_file")
    local basename="${filename%.tex}"
    local dir=$(dirname "$tex_file")
    
    echo -e "${CYAN}[$(($TOTAL + 1))] Compiling: $filename${NC}"
    
    if [ ! -f "$tex_file" ]; then
        echo -e "${YELLOW}[SKIP] $filename (file not found)${NC}"
        echo "SKIPPED: $filename (file not found)" >> "$LOG_PATH"
        return 2
    fi
    
    # Check if file contains \begin{document}
    if ! grep -q '\\begin{document}' "$tex_file" 2>/dev/null; then
        echo -e "${YELLOW}[SKIP] $filename (no \\begin{document})${NC}"
        echo "SKIPPED: $filename (no \\begin{document})" >> "$LOG_PATH"
        return 2
    fi
    
    local pass=1
    local success=false
    local attempts=0
    local max_fix_attempts=3
    
    # Try compilation with automatic fixing
    while [ $pass -le $MAX_PASSES ] && [ "$success" = false ]; do
        if [ "$VERBOSE" = true ]; then
            echo "  Pass $pass/$MAX_PASSES..."
        fi
        
        if [ "$DRY_RUN" = true ]; then
            echo "[DRY-RUN] Would run: pdflatex -interaction=nonstopmode -output-directory=$dir $tex_file"
            success=true
            break
        fi
        
        # Run pdflatex
        pdflatex -interaction=nonstopmode \
            -output-directory="$dir" \
            "$tex_file" > /dev/null 2>&1
        
        local exit_code=$?
        local log_file="$dir/$basename.log"
        local pdf_file="$dir/$basename.pdf"
        
        # Check if compilation succeeded
        if [ -f "$pdf_file" ] && [ $exit_code -eq 0 ]; then
            success=true
            break
        fi
        
        # Try to fix errors if on first pass and haven't exceeded fix attempts
        if [ $pass -eq 1 ] && [ $attempts -lt $max_fix_attempts ]; then
            if analyze_and_fix_errors "$tex_file" "$log_file"; then
                ((attempts++))
                ((FIXED++))
                # Retry compilation after fixing, but don't increment pass yet
                continue
            fi
        fi
        
        # Increment pass counter if we didn't fix anything or exhausted fix attempts
        ((pass++))
    done
    
    # Check final result
    local pdf_file="$dir/$basename.pdf"
    if [ "$success" = true ] || [ -f "$pdf_file" ]; then
        echo -e "${GREEN}[SUCCESS] $filename${NC}"
        echo "SUCCESS: $filename" >> "$LOG_PATH"
        return 0
    else
        # Extract and log error
        local log_file="$dir/$basename.log"
        echo -e "${RED}[FAILED] $filename${NC}"
        echo "FAILED: $filename" >> "$LOG_PATH"
        
        if [ -f "$log_file" ]; then
            echo "Error details:" >> "$LOG_PATH"
            grep -A5 "^!" "$log_file" | head -20 >> "$LOG_PATH"
            echo "" >> "$LOG_PATH"
        fi
        
        return 1
    fi
}

# Main compilation logic
echo "Starting compilation..."
echo ""

# Find all chapter files (kapitel_00.tex to kapitel_43.tex)
for i in $(seq -w 0 43); do
    tex_file="$SCRIPT_DIR/kapitel_$i.tex"
    
    if [ -f "$tex_file" ]; then
        ((TOTAL++))
        compile_tex_file "$tex_file"
        result=$?
        
        case $result in
            0) ((SUCCESS++)) ;;
            1) ((FAILED++)) ;;
            2) ;; # Skipped, don't count
        esac
    fi
done

# Compile main.tex if it exists
if [ -f "$SCRIPT_DIR/main.tex" ]; then
    ((TOTAL++))
    compile_tex_file "$SCRIPT_DIR/main.tex"
    result=$?
    
    case $result in
        0) ((SUCCESS++)) ;;
        1) ((FAILED++)) ;;
        2) ;; # Skipped
    esac
fi

# Check if no files were found
if [ $TOTAL -eq 0 ]; then
    echo -e "${YELLOW}No LaTeX files found to compile.${NC}"
    echo -e "${YELLOW}Expected files: kapitel_00.tex to kapitel_43.tex and/or main.tex${NC}"
    echo -e "${YELLOW}Location: $SCRIPT_DIR${NC}"
    echo ""
    echo "NOTE: This directory currently contains Markdown files (.md)."
    echo "You may need to convert them to LaTeX format first."
fi

# Summary
echo ""
echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}Compilation Summary:${NC}"
echo -e "  Total files processed: ${CYAN}$TOTAL${NC}"
echo -e "  Successful: ${GREEN}$SUCCESS${NC}"
echo -e "  Failed: ${RED}$FAILED${NC}"
echo -e "  Auto-fixed: ${MAGENTA}$FIXED${NC}"
echo -e "${BLUE}============================================================${NC}"
echo -e "Detailed log: ${CYAN}$LOG_PATH${NC}"
echo ""

# Exit with appropriate code
if [ $FAILED -gt 0 ]; then
    echo -e "${RED}Some compilations failed. Check the log file for details.${NC}"
    exit 1
elif [ $TOTAL -eq 0 ]; then
    echo -e "${YELLOW}No files were compiled.${NC}"
    exit 2
else
    echo -e "${GREEN}All compilations completed successfully!${NC}"
    exit 0
fi
