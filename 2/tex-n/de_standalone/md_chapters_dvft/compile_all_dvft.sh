#!/bin/bash
# ==============================================================================
# T0 Theory: DVFT LaTeX Compilation Script with Auto-Fix
# ==============================================================================
# This script recursively compiles all LaTeX chapter files (kapitel_00.tex to 
# kapitel_43.tex) and main.tex using sudo pdflatex, incorporating the physics 
# package, and fixes common LaTeX errors like missing packages, undefined 
# commands, or font issues until all errors are resolved.
#
# Features:
#   - Uses sudo pdflatex for compilation
#   - Handles up to 5 compilation passes per file
#   - Automatically fixes common LaTeX errors
#   - Installs missing packages (including physics package)
#   - Logs errors to compile_errors.log
#
# Usage:
#   ./compile_all_dvft.sh
#
# Author: Johann Pascher
# Date: 2025
# ==============================================================================

set -u  # Exit on undefined variables

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAX_PASSES=5
ERROR_LOG="$SCRIPT_DIR/compile_errors.log"
TEMP_LOG="/tmp/dvft_compile_$$.log"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Counters
SUCCESS=0
FAILED=0
FIXED=0
TOTAL=0

# Initialize error log
echo "==============================================================================" > "$ERROR_LOG"
echo "DVFT LaTeX Compilation Error Log" >> "$ERROR_LOG"
echo "Started: $(date)" >> "$ERROR_LOG"
echo "==============================================================================" >> "$ERROR_LOG"
echo "" >> "$ERROR_LOG"

# Function to check and install LaTeX packages
check_and_install_packages() {
    echo -e "${CYAN}Checking for required LaTeX packages...${NC}"
    
    # Check if physics package is installed
    if ! kpsewhich physics.sty &> /dev/null; then
        echo -e "${YELLOW}Physics package not found. Installing...${NC}"
        if sudo tlmgr install physics &> /dev/null; then
            echo -e "${GREEN}Physics package installed successfully.${NC}"
        else
            echo -e "${YELLOW}Attempting alternative installation method...${NC}"
            if sudo apt-get update &> /dev/null && sudo apt-get install -y texlive-latex-extra &> /dev/null; then
                echo -e "${GREEN}LaTeX packages installed via apt-get.${NC}"
            else
                echo -e "${RED}Warning: Could not install physics package automatically.${NC}"
                echo "Please install it manually: sudo tlmgr install physics"
            fi
        fi
    else
        echo -e "${GREEN}Physics package is already installed.${NC}"
    fi
    
    # Check for other common packages
    local packages=("amsmath" "amssymb" "graphicx" "hyperref" "geometry" "xcolor")
    for pkg in "${packages[@]}"; do
        if ! kpsewhich "${pkg}.sty" &> /dev/null; then
            echo -e "${YELLOW}Installing ${pkg}...${NC}"
            sudo tlmgr install "$pkg" &> /dev/null || true
        fi
    done
}

# Function to detect error type from log
detect_error_type() {
    local log_file="$1"
    
    # Missing package
    if grep -q "! LaTeX Error: File.*\.sty' not found" "$log_file"; then
        echo "missing_package"
        return
    fi
    
    # Undefined control sequence
    if grep -q "! Undefined control sequence" "$log_file"; then
        echo "undefined_command"
        return
    fi
    
    # Font not found
    if grep -q "Font.*not found" "$log_file"; then
        echo "font_error"
        return
    fi
    
    # Missing \begin{document}
    if grep -q "! LaTeX Error: Missing \\\\begin{document}" "$log_file"; then
        echo "missing_document"
        return
    fi
    
    # Runaway argument
    if grep -q "Runaway argument" "$log_file"; then
        echo "runaway_argument"
        return
    fi
    
    echo "unknown"
}

# Function to extract missing package name
extract_package_name() {
    local log_file="$1"
    grep "! LaTeX Error: File.*\.sty' not found" "$log_file" | \
        sed "s/.*File \`\(.*\)\.sty' not found.*/\1/" | head -1
}

# Function to extract undefined command
extract_undefined_command() {
    local log_file="$1"
    grep -A1 "! Undefined control sequence" "$log_file" | \
        grep -v "^--$" | tail -1 | \
        sed 's/.*\(\\\[a-zA-Z]*\).*/\1/' | head -1
}

# Function to fix missing package
fix_missing_package() {
    local tex_file="$1"
    local package="$2"
    
    echo -e "${YELLOW}  → Attempting to install package: $package${NC}"
    
    # Try to install the package
    if sudo tlmgr install "$package" &> /dev/null; then
        echo -e "${GREEN}  ✓ Package $package installed${NC}"
        return 0
    else
        # Try adding \usepackage to the file if not already present
        if ! grep -q "\\usepackage.*{$package}" "$tex_file"; then
            echo -e "${YELLOW}  → Adding \\usepackage{$package} to file${NC}"
            # Find the line with \documentclass or first \usepackage
            local insert_line=$(grep -n "\\\\documentclass\|\\\\usepackage" "$tex_file" | tail -1 | cut -d: -f1)
            if [ -n "$insert_line" ]; then
                insert_line=$((insert_line + 1))
                sed -i "${insert_line}i\\\\usepackage{$package}" "$tex_file"
                echo -e "${GREEN}  ✓ Added \\usepackage{$package}${NC}"
                return 0
            fi
        fi
    fi
    
    return 1
}

# Function to fix undefined command
fix_undefined_command() {
    local tex_file="$1"
    local command="$2"
    
    echo -e "${YELLOW}  → Attempting to fix undefined command: $command${NC}"
    
    # Common command fixes
    case "$command" in
        "\\bra"|"\\ket"|"\\braket")
            if ! grep -q "\\usepackage.*{physics}" "$tex_file"; then
                echo -e "${YELLOW}  → Adding physics package for $command${NC}"
                local insert_line=$(grep -n "\\\\documentclass\|\\\\usepackage" "$tex_file" | tail -1 | cut -d: -f1)
                if [ -n "$insert_line" ]; then
                    insert_line=$((insert_line + 1))
                    sed -i "${insert_line}i\\\\usepackage{physics}" "$tex_file"
                    echo -e "${GREEN}  ✓ Added physics package${NC}"
                    return 0
                fi
            fi
            ;;
        "\\mathbb"|"\\mathcal"|"\\mathfrak")
            if ! grep -q "\\usepackage.*{amssymb}" "$tex_file"; then
                echo -e "${YELLOW}  → Adding amssymb package${NC}"
                fix_missing_package "$tex_file" "amssymb"
                return 0
            fi
            ;;
        "\\includegraphics")
            if ! grep -q "\\usepackage.*{graphicx}" "$tex_file"; then
                echo -e "${YELLOW}  → Adding graphicx package${NC}"
                fix_missing_package "$tex_file" "graphicx"
                return 0
            fi
            ;;
    esac
    
    return 1
}

# Function to ensure physics package is in preamble
ensure_physics_package() {
    local tex_file="$1"
    
    # Check if file has \documentclass
    if ! grep -q "\\documentclass" "$tex_file"; then
        return 1
    fi
    
    # Check if physics package is already included
    if grep -q "\\usepackage.*{physics}" "$tex_file"; then
        return 0
    fi
    
    # Add physics package after documentclass or last usepackage
    local insert_line=$(grep -n "\\\\documentclass\|\\\\usepackage" "$tex_file" | tail -1 | cut -d: -f1)
    if [ -n "$insert_line" ]; then
        insert_line=$((insert_line + 1))
        sed -i "${insert_line}i\\\\usepackage{physics}" "$tex_file"
        echo -e "${GREEN}  ✓ Added physics package to preamble${NC}"
        return 0
    fi
    
    return 1
}

# Function to compile a single file with auto-fix
compile_with_autofix() {
    local tex_file="$1"
    local filename=$(basename "$tex_file")
    local dir=$(dirname "$tex_file")
    local basename="${filename%.tex}"
    
    echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Processing: ${filename}${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    # Log to error file
    echo "==============================================================================" >> "$ERROR_LOG"
    echo "File: $filename" >> "$ERROR_LOG"
    echo "Started: $(date)" >> "$ERROR_LOG"
    echo "------------------------------------------------------------------------------" >> "$ERROR_LOG"
    
    # Ensure physics package is in preamble
    ensure_physics_package "$tex_file"
    
    local pass=1
    local success=false
    local fixed_this_file=false
    
    while [ $pass -le $MAX_PASSES ]; do
        echo -e "${CYAN}Pass $pass/$MAX_PASSES...${NC}"
        
        # Change to directory and compile
        cd "$dir" || return 1
        
        # Run pdflatex with sudo
        if sudo pdflatex -interaction=nonstopmode -file-line-error \
            "$filename" > "$TEMP_LOG" 2>&1; then
            echo -e "${GREEN}✓ Compilation successful!${NC}"
            success=true
            break
        else
            echo -e "${YELLOW}⚠ Compilation failed${NC}"
            
            # Copy log file
            local log_file="$dir/$basename.log"
            if [ -f "$log_file" ]; then
                cat "$log_file" >> "$ERROR_LOG"
                
                # Detect error type
                local error_type=$(detect_error_type "$log_file")
                echo -e "${YELLOW}  Error type: $error_type${NC}"
                
                # Attempt to fix based on error type
                case "$error_type" in
                    missing_package)
                        local pkg=$(extract_package_name "$log_file")
                        if [ -n "$pkg" ]; then
                            if fix_missing_package "$tex_file" "$pkg"; then
                                fixed_this_file=true
                                echo "  FIXED: Installed/added package $pkg" >> "$ERROR_LOG"
                            fi
                        fi
                        ;;
                    undefined_command)
                        local cmd=$(extract_undefined_command "$log_file")
                        if [ -n "$cmd" ]; then
                            if fix_undefined_command "$tex_file" "$cmd"; then
                                fixed_this_file=true
                                echo "  FIXED: Added package for command $cmd" >> "$ERROR_LOG"
                            fi
                        fi
                        ;;
                    font_error)
                        echo -e "${YELLOW}  → Font error detected, trying to continue...${NC}"
                        echo "  Font error - attempting to continue" >> "$ERROR_LOG"
                        ;;
                    *)
                        echo -e "${YELLOW}  → Unknown error type${NC}"
                        echo "  Unknown error" >> "$ERROR_LOG"
                        ;;
                esac
            fi
        fi
        
        pass=$((pass + 1))
    done
    
    echo "" >> "$ERROR_LOG"
    
    # Update counters
    TOTAL=$((TOTAL + 1))
    if [ "$success" = true ]; then
        SUCCESS=$((SUCCESS + 1))
        if [ "$fixed_this_file" = true ]; then
            FIXED=$((FIXED + 1))
        fi
        return 0
    else
        FAILED=$((FAILED + 1))
        echo -e "${RED}✗ Failed after $MAX_PASSES passes${NC}"
        return 1
    fi
}

# Main script
main() {
    echo -e "${BLUE}"
    echo "=============================================================================="
    echo "  DVFT LaTeX Compilation Script with Auto-Fix"
    echo "=============================================================================="
    echo -e "${NC}"
    echo "Working directory: $SCRIPT_DIR"
    echo "Max passes per file: $MAX_PASSES"
    echo "Error log: $ERROR_LOG"
    echo ""
    
    # Check and install packages
    check_and_install_packages
    echo ""
    
    # Find all chapter files (kapitel_00.tex to kapitel_43.tex)
    echo -e "${CYAN}Searching for chapter files...${NC}"
    local files=()
    
    # Add kapitel files (00 to 43)
    for i in $(seq -w 0 43); do
        local kapitel_file="$SCRIPT_DIR/kapitel_$i.tex"
        if [ -f "$kapitel_file" ]; then
            files+=("$kapitel_file")
        fi
    done
    
    # Add main.tex if it exists
    if [ -f "$SCRIPT_DIR/main.tex" ]; then
        files+=("$SCRIPT_DIR/main.tex")
    fi
    
    if [ ${#files[@]} -eq 0 ]; then
        echo -e "${YELLOW}No .tex files found matching kapitel_*.tex or main.tex${NC}"
        echo -e "${YELLOW}Looking for any .tex files in the directory...${NC}"
        # Fallback: find any .tex files
        while IFS= read -r -d '' file; do
            files+=("$file")
        done < <(find "$SCRIPT_DIR" -maxdepth 1 -name "*.tex" -type f -print0)
    fi
    
    echo -e "${GREEN}Found ${#files[@]} file(s) to compile${NC}"
    echo ""
    
    # Compile each file
    for tex_file in "${files[@]}"; do
        compile_with_autofix "$tex_file"
    done
    
    # Print summary
    echo ""
    echo -e "${BLUE}"
    echo "=============================================================================="
    echo "  COMPILATION SUMMARY"
    echo "=============================================================================="
    echo -e "${NC}"
    echo -e "Total files:      ${TOTAL}"
    echo -e "${GREEN}Successful:       ${SUCCESS}${NC}"
    echo -e "${YELLOW}Fixed and built:  ${FIXED}${NC}"
    echo -e "${RED}Failed:           ${FAILED}${NC}"
    echo ""
    echo "Error log: $ERROR_LOG"
    echo -e "${BLUE}==============================================================================${NC}"
    echo ""
    
    # Clean up temp log
    rm -f "$TEMP_LOG"
    
    # Exit with appropriate code
    if [ $FAILED -gt 0 ]; then
        exit 1
    fi
    exit 0
}

# Run main function
main "$@"
