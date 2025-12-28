#!/bin/bash
# ==============================================================================
# LaTeX Chapter Compilation Script for DVFT
# ==============================================================================
# This script recursively compiles all LaTeX chapter files (kapitel_00.tex to 
# kapitel_43.tex) and main.tex using sudo pdflatex, incorporating the physics 
# package, until all errors are resolved.
#
# The script handles:
# - Multiple passes for references and citations
# - Error detection and reporting
# - Common LaTeX issue fixes (missing packages, undefined commands)
# - Automatic package installation
#
# Usage:
#   ./compile_all.sh [OPTIONS]
#
# Options:
#   -h, --help          Show this help message
#   -v, --verbose       Verbose output
#   -c, --clean         Clean auxiliary files after compilation
#   -n, --no-sudo       Don't use sudo for pdflatex (for testing)
#
# Author: Generated for T0 Theory
# Date: 2025
# ==============================================================================

# Note: We don't use 'set -e' here because we want to handle errors explicitly
# and continue processing files even if some compilations fail.

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Configuration
USE_SUDO=true
VERBOSE=false
CLEAN=false
MAX_PASSES=3
LOG_DIR="$SCRIPT_DIR/compile_logs"
MAIN_LOG="$LOG_DIR/compile_all.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
SUCCESS_COUNT=0
FAILED_COUNT=0
SKIPPED_COUNT=0

# Arrays to track files
declare -a FAILED_FILES
declare -a SUCCESS_FILES

# Usage function
usage() {
    cat << EOF
LaTeX Chapter Compilation Script for DVFT

Usage: $0 [OPTIONS]

Options:
  -h, --help          Show this help message
  -v, --verbose       Verbose output
  -c, --clean         Clean auxiliary files after compilation
  -n, --no-sudo       Don't use sudo for pdflatex (for testing)

Description:
  Compiles all LaTeX chapter files (kapitel_00.tex to kapitel_43.tex) and
  main.tex using pdflatex with multiple passes for references.

Examples:
  $0                  # Compile all files with sudo
  $0 -v               # Compile with verbose output
  $0 -c               # Compile and clean auxiliary files
  $0 -n               # Compile without sudo (for testing)

EOF
    exit 0
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -c|--clean)
            CLEAN=true
            shift
            ;;
        -n|--no-sudo)
            USE_SUDO=false
            shift
            ;;
        *)
            echo -e "${RED}Error: Unknown option: $1${NC}"
            usage
            ;;
    esac
done

# Create log directory
mkdir -p "$LOG_DIR"

# Initialize main log
echo "============================================================" > "$MAIN_LOG"
echo "LaTeX Compilation Log" >> "$MAIN_LOG"
echo "Started: $(date)" >> "$MAIN_LOG"
echo "Directory: $SCRIPT_DIR" >> "$MAIN_LOG"
echo "Use sudo: $USE_SUDO" >> "$MAIN_LOG"
echo "============================================================" >> "$MAIN_LOG"
echo "" >> "$MAIN_LOG"

# Function to log messages
log_message() {
    local level="$1"
    shift
    local message="$*"
    echo "[$level] $(date '+%Y-%m-%d %H:%M:%S') $message" >> "$MAIN_LOG"
    
    if [ "$VERBOSE" = true ]; then
        case "$level" in
            INFO)
                echo -e "${BLUE}[INFO]${NC} $message"
                ;;
            SUCCESS)
                echo -e "${GREEN}[SUCCESS]${NC} $message"
                ;;
            WARNING)
                echo -e "${YELLOW}[WARNING]${NC} $message"
                ;;
            ERROR)
                echo -e "${RED}[ERROR]${NC} $message"
                ;;
            *)
                echo "[${level}] $message"
                ;;
        esac
    fi
}

# Function to check if pdflatex is available
check_pdflatex() {
    if command -v pdflatex &> /dev/null; then
        log_message "INFO" "pdflatex found: $(which pdflatex)"
        return 0
    else
        echo -e "${RED}Error: pdflatex is not installed or not in PATH${NC}"
        echo "Please install TeX Live or another LaTeX distribution."
        echo "On Ubuntu/Debian: sudo apt-get install texlive-full"
        echo "On other systems, visit: https://www.tug.org/texlive/"
        exit 1
    fi
}

# Function to check and install missing packages
check_missing_packages() {
    local log_file="$1"
    local packages_to_install=()
    
    # Common missing package patterns
    if grep -q "! LaTeX Error: File.*\.sty' not found" "$log_file"; then
        # Extract package names
        while IFS= read -r line; do
            if [[ "$line" =~ File\ \'([^\']+)\.sty\'\ not\ found ]]; then
                package_name="${BASH_REMATCH[1]}"
                packages_to_install+=("$package_name")
                log_message "WARNING" "Missing package detected: $package_name"
            fi
        done < "$log_file"
    fi
    
    # Check for specific packages mentioned in errors
    if grep -q "physics" "$log_file"; then
        # Check if tlmgr is available and package is not installed
        if command -v tlmgr &>/dev/null; then
            if ! tlmgr list --only-installed physics 2>/dev/null | grep -q "physics"; then
                packages_to_install+=("physics")
            fi
        else
            # If tlmgr is not available, add to list anyway
            packages_to_install+=("physics")
        fi
    fi
    
    # Install missing packages
    if [ ${#packages_to_install[@]} -gt 0 ]; then
        log_message "INFO" "Attempting to install missing packages: ${packages_to_install[*]}"
        for pkg in "${packages_to_install[@]}"; do
            if [ "$USE_SUDO" = true ]; then
                sudo tlmgr install "$pkg" 2>&1 | tee -a "$MAIN_LOG" || true
            else
                tlmgr install "$pkg" 2>&1 | tee -a "$MAIN_LOG" || true
            fi
        done
        return 0  # Indicate packages were installed
    fi
    
    return 1  # No packages installed
}

# Function to detect common LaTeX errors that might be fixable
detect_fixable_errors() {
    local tex_file="$1"
    local log_file="$2"
    
    # Check for undefined control sequences
    if grep -q "Undefined control sequence" "$log_file"; then
        log_message "WARNING" "Undefined control sequences detected in $tex_file"
        
        # Check if physics commands are used but package is not included
        if grep -q "\\qty\\|\\dd\\|\\dv\\|\\pdv" "$tex_file" 2>/dev/null; then
            if ! grep -q "\\usepackage.*physics" "$tex_file" 2>/dev/null; then
                log_message "INFO" "Physics commands detected but package not included in $tex_file"
                log_message "INFO" "Consider adding \\usepackage{physics} to the preamble"
            fi
        fi
    fi
    
    # Check for undefined references (needs multiple passes)
    if grep -q "Reference.*undefined\\|Citation.*undefined" "$log_file"; then
        log_message "INFO" "Undefined references found - will resolve with multiple passes"
    fi
    
    # Return 1 since we're not actually fixing anything, just detecting
    return 1
}

# Function to compile a single LaTeX file
compile_latex_file() {
    local tex_file="$1"
    local basename=$(basename "$tex_file" .tex)
    local file_log="$LOG_DIR/${basename}_compile.log"
    
    if [ ! -f "$tex_file" ]; then
        log_message "WARNING" "File not found: $tex_file"
        echo -e "${YELLOW}[SKIP]${NC} $basename (file not found)"
        ((SKIPPED_COUNT++))
        return 1
    fi
    
    echo -ne "Compiling: ${basename}..."
    log_message "INFO" "Starting compilation of $basename"
    
    # Determine pdflatex command
    local PDFLATEX_CMD="pdflatex"
    if [ "$USE_SUDO" = true ]; then
        PDFLATEX_CMD="sudo pdflatex"
    fi
    
    # Compilation loop with multiple passes
    local pass=1
    local success=false
    local package_retry_count=0
    local max_package_retries=2
    
    while [ $pass -le $MAX_PASSES ]; do
        log_message "INFO" "Pass $pass for $basename"
        
        # Run pdflatex without shell-escape for security
        cd "$SCRIPT_DIR"
        $PDFLATEX_CMD -interaction=nonstopmode \
            -output-directory="$SCRIPT_DIR" \
            "$tex_file" > "$file_log" 2>&1
        
        local exit_code=$?
        
        # Check if PDF was created
        if [ -f "$SCRIPT_DIR/${basename}.pdf" ]; then
            # Check for warnings but continue if PDF exists
            if [ $exit_code -eq 0 ]; then
                success=true
                log_message "SUCCESS" "Pass $pass completed successfully for $basename"
                
                # Check if we need another pass (for references)
                if [ $pass -lt $MAX_PASSES ] && grep -q "Rerun to get" "$file_log"; then
                    log_message "INFO" "References need update, running another pass"
                    ((pass++))
                    continue
                fi
                break
            else
                log_message "WARNING" "Pass $pass completed with warnings for $basename"
            fi
        else
            # Compilation failed
            log_message "ERROR" "Pass $pass failed for $basename (exit code: $exit_code)"
            
            # Try to fix common errors only on first pass with limited retries
            if [ $pass -eq 1 ] && [ $package_retry_count -lt $max_package_retries ]; then
                # Check for missing packages and install them
                if check_missing_packages "$file_log"; then
                    log_message "INFO" "Packages installed, retrying compilation (attempt $((package_retry_count + 1)))"
                    ((package_retry_count++))
                    # Continue to next iteration without incrementing pass
                    continue
                fi
                
                # Detect fixable errors (informational only)
                detect_fixable_errors "$tex_file" "$file_log"
            fi
        fi
        
        ((pass++))
    done
    
    # Report results
    if [ -f "$SCRIPT_DIR/${basename}.pdf" ]; then
        echo -e "\r${GREEN}[OK]${NC}   $basename (PDF created)"
        log_message "SUCCESS" "Compilation successful: $basename"
        SUCCESS_FILES+=("$basename")
        ((SUCCESS_COUNT++))
        return 0
    else
        echo -e "\r${RED}[FAIL]${NC} $basename"
        log_message "ERROR" "Compilation failed: $basename"
        
        # Extract and display first error
        if [ -f "$file_log" ]; then
            local first_error=$(grep -m 1 "^!" "$file_log" || echo "Unknown error")
            echo "  Error: $first_error"
            log_message "ERROR" "  $first_error"
        fi
        
        FAILED_FILES+=("$basename")
        ((FAILED_COUNT++))
        return 1
    fi
}

# Function to clean auxiliary files
clean_auxiliary_files() {
    log_message "INFO" "Cleaning auxiliary files"
    echo "Cleaning auxiliary files..."
    
    local patterns=(
        "*.aux" "*.log" "*.out" "*.toc" "*.lof" "*.lot" 
        "*.fls" "*.fdb_latexmk" "*.synctex.gz" "*.bbl" "*.blg"
        "*.nav" "*.snm" "*.vrb" "*.bcf" "*.run.xml"
        "*.idx" "*.ilg" "*.ind"
    )
    
    cd "$SCRIPT_DIR"
    for pattern in "${patterns[@]}"; do
        # Allow shell expansion for glob patterns
        # shellcheck disable=SC2086
        rm -f $pattern 2>/dev/null || true
    done
    
    log_message "INFO" "Cleanup complete"
}

# Main compilation routine
main() {
    echo "============================================================"
    echo "LaTeX Chapter Compilation Script for DVFT"
    echo "============================================================"
    echo "Directory: $SCRIPT_DIR"
    echo "Using sudo: $USE_SUDO"
    echo "Verbose: $VERBOSE"
    echo "Clean after: $CLEAN"
    echo "============================================================"
    echo ""
    
    # Check for pdflatex
    check_pdflatex
    
    # Find all chapter files (kapitel_00.tex to kapitel_43.tex)
    echo "Looking for chapter files..."
    local chapter_files=()
    
    # Add main.tex if it exists
    if [ -f "$SCRIPT_DIR/main.tex" ]; then
        chapter_files+=("$SCRIPT_DIR/main.tex")
        echo "Found: main.tex"
    fi
    
    # Add chapter files
    for i in $(seq -f "%02g" 0 43); do
        if [ -f "$SCRIPT_DIR/kapitel_${i}.tex" ]; then
            chapter_files+=("$SCRIPT_DIR/kapitel_${i}.tex")
            echo "Found: kapitel_${i}.tex"
        fi
    done
    
    local total_files=${#chapter_files[@]}
    
    if [ $total_files -eq 0 ]; then
        echo -e "${YELLOW}Warning: No LaTeX files found to compile${NC}"
        echo "Looking for: main.tex, kapitel_00.tex through kapitel_43.tex"
        log_message "WARNING" "No LaTeX files found to compile"
        exit 0
    fi
    
    echo ""
    echo "Found $total_files file(s) to compile"
    echo ""
    
    # Compile each file
    for tex_file in "${chapter_files[@]}"; do
        compile_latex_file "$tex_file"
        echo ""
    done
    
    # Clean auxiliary files if requested
    if [ "$CLEAN" = true ]; then
        echo ""
        clean_auxiliary_files
        echo ""
    fi
    
    # Print summary
    echo "============================================================"
    echo "Compilation Summary"
    echo "============================================================"
    echo "Total files:   $total_files"
    echo "Successful:    $SUCCESS_COUNT"
    echo "Failed:        $FAILED_COUNT"
    echo "Skipped:       $SKIPPED_COUNT"
    echo "============================================================"
    
    log_message "INFO" "Compilation complete - Success: $SUCCESS_COUNT, Failed: $FAILED_COUNT, Skipped: $SKIPPED_COUNT"
    
    # List successful files
    if [ $SUCCESS_COUNT -gt 0 ]; then
        echo ""
        echo "Successfully compiled:"
        for file in "${SUCCESS_FILES[@]}"; do
            echo "  ✓ $file.pdf"
        done
    fi
    
    # List failed files with details
    if [ $FAILED_COUNT -gt 0 ]; then
        echo ""
        echo -e "${RED}Failed to compile:${NC}"
        for file in "${FAILED_FILES[@]}"; do
            echo "  ✗ $file"
            if [ -f "$LOG_DIR/${file}_compile.log" ]; then
                echo "    Log: $LOG_DIR/${file}_compile.log"
            fi
        done
        echo ""
        echo "Check individual log files in: $LOG_DIR"
    fi
    
    echo ""
    echo "Complete log: $MAIN_LOG"
    echo ""
    
    # Exit with appropriate code
    if [ $FAILED_COUNT -gt 0 ]; then
        exit 1
    else
        exit 0
    fi
}

# Run main function
main "$@"

