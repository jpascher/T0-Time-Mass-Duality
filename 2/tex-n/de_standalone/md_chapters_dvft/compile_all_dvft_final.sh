#!/bin/bash
# ==============================================================================
# DVFT Chapter Compilation Script
# ==============================================================================
# This script converts DVFT Markdown chapters to LaTeX and compiles them to PDF.
# 
# Features:
#   - Converts Markdown files (00_Vorspann.md to Kapitel_43.md) to LaTeX
#   - Generates LaTeX files (kapitel_00.tex to kapitel_43.tex)
#   - Converts physical notation (φ→\varphi, ρ→\rho, θ→\theta)
#   - Includes physics package and proper LaTeX structure
#   - Creates main.tex that includes all chapters
#   - Compiles with pdflatex (up to 3 passes per file)
#   - Fixes common LaTeX errors automatically
#   - Logs all output and errors
#
# Usage:
#   ./compile_all_dvft_final.sh
#   sudo ./compile_all_dvft_final.sh  (if sudo required for pdflatex)
#
# Author: Generated for T0 Theory Repository
# Date: 2025
# ==============================================================================

set -u  # Exit on undefined variables, but not on errors (we handle them)

# ==============================================================================
# Configuration
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/compilation.log"
ERROR_LOG="$SCRIPT_DIR/compilation_errors.log"
MAX_PASSES=3
MAIN_TEX="main.tex"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
TOTAL_FILES=0
CONVERTED_FILES=0
COMPILED_FILES=0
FAILED_FILES=0

# ==============================================================================
# Logging Functions
# ==============================================================================

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

log_error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $*" | tee -a "$LOG_FILE" >> "$ERROR_LOG"
}

log_info() {
    echo -e "${BLUE}[INFO]${NC} $*" | tee -a "$LOG_FILE"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $*" | tee -a "$LOG_FILE"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $*" | tee -a "$LOG_FILE"
}

log_fail() {
    echo -e "${RED}[FAIL]${NC} $*" | tee -a "$LOG_FILE"
}

# ==============================================================================
# Initialization
# ==============================================================================

init() {
    log "============================================================"
    log "DVFT Chapter Compilation Script"
    log "============================================================"
    log "Script directory: $SCRIPT_DIR"
    log "Log file: $LOG_FILE"
    log "Error log: $ERROR_LOG"
    log "============================================================"
    
    # Clear previous logs
    > "$LOG_FILE"
    > "$ERROR_LOG"
    
    # Check for pdflatex
    if ! command -v pdflatex &> /dev/null; then
        log_warning "pdflatex not found in PATH. Will proceed with conversion only."
        log_warning "To compile PDFs, install texlive or run with sudo if needed."
    fi
    
    cd "$SCRIPT_DIR" || exit 1
}

# ==============================================================================
# Markdown to LaTeX Conversion Functions
# ==============================================================================

convert_math_symbols() {
    local content="$1"
    
    # Convert Unicode math symbols to LaTeX
    content="${content//φ/\\varphi}"
    content="${content//𝜙/\\Phi}"
    content="${content//ρ/\\rho}"
    content="${content//𝜌/\\rho}"
    content="${content//θ/\\theta}"
    content="${content//∇/\\nabla}"
    content="${content//∂/\\partial}"
    content="${content//≈/\\approx}"
    content="${content//≠/\\neq}"
    content="${content//≤/\\leq}"
    content="${content//≥/\\geq}"
    content="${content//∞/\\infty}"
    content="${content//±/\\pm}"
    content="${content//×/\\times}"
    content="${content//÷/\\div}"
    content="${content//√/\\sqrt}"
    content="${content//∫/\\int}"
    content="${content//∑/\\sum}"
    content="${content//∏/\\prod}"
    content="${content//∆/\\Delta}"
    content="${content//Δ/\\Delta}"
    content="${content//μ/\\mu}"
    content="${content//λ/\\lambda}"
    content="${content//κ/\\kappa}"
    content="${content//Λ/\\Lambda}"
    content="${content//α/\\alpha}"
    content="${content//β/\\beta}"
    content="${content//γ/\\gamma}"
    content="${content//Γ/\\Gamma}"
    content="${content//ω/\\omega}"
    content="${content//Ω/\\Omega}"
    content="${content//π/\\pi}"
    content="${content//σ/\\sigma}"
    content="${content//τ/\\tau}"
    content="${content//ψ/\\psi}"
    content="${content//Ψ/\\Psi}"
    content="${content//χ/\\chi}"
    content="${content//ξ/\\xi}"
    content="${content//η/\\eta}"
    content="${content//ν/\\nu}"
    content="${content//ε/\\epsilon}"
    content="${content//ζ/\\zeta}"
    content="${content//℘/\\wp}"
    
    echo "$content"
}

convert_markdown_to_latex() {
    local md_file="$1"
    local tex_file="$2"
    local standalone="$3"  # "yes" for standalone, "no" for \input
    
    log_info "Converting $md_file to $tex_file"
    
    if [ ! -f "$md_file" ]; then
        log_error "Markdown file not found: $md_file"
        return 1
    fi
    
    local content=$(cat "$md_file")
    
    # Extract title from first line
    local title=$(echo "$content" | grep -m1 "^# " | sed 's/^# //')
    if [ -z "$title" ]; then
        title="Untitled Chapter"
    fi
    
    # Remove the title line from content
    content=$(echo "$content" | tail -n +2)
    
    # Convert math symbols
    content=$(convert_math_symbols "$content")
    
    # Escape special LaTeX characters more carefully
    # First protect existing LaTeX commands
    content=$(echo "$content" | sed 's/\\/BACKSLASHTEMP/g')
    content=$(echo "$content" | sed 's/&/\\&/g')
    content=$(echo "$content" | sed 's/%/\\%/g')
    content=$(echo "$content" | sed 's/#/\\#/g')
    content=$(echo "$content" | sed 's/\$/\\$/g')
    # Restore backslashes
    content=$(echo "$content" | sed 's/BACKSLASHTEMP/\\/g')
    
    # Convert bold text **text** to \textbf{text}
    content=$(echo "$content" | sed 's/\*\*\([^*]*\)\*\*/\\textbf{\1}/g')
    
    # Convert italic text *text* to \textit{text} (but not in URLs)
    content=$(echo "$content" | sed 's/\*\([^*]*\)\*/\\textit{\1}/g')
    
    # Convert inline code `text` to \texttt{text}
    content=$(echo "$content" | sed 's/`\([^`]*\)`/\\texttt{\1}/g')
    
    # Convert section headers
    # ## Header -> \subsection{Header}
    content=$(echo "$content" | sed 's/^## \(.*\)$/\\subsection{\1}/')
    
    # ### Header -> \subsubsection{Header}
    content=$(echo "$content" | sed 's/^### \(.*\)$/\\subsubsection{\1}/')
    
    # Create LaTeX document
    if [ "$standalone" = "yes" ]; then
        # Standalone document with full preamble
        cat > "$tex_file" << EOF
\\documentclass[12pt,a4paper]{article}

% Packages
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{physics}
\\usepackage{graphicx}
\\usepackage{hyperref}
\\usepackage[margin=2.5cm]{geometry}

% Physics notation
\\renewcommand{\\varphi}{\\phi}

\\title{$title}
\\author{DVFT - Dynamic Vacuum Field Theory}
\\date{\\today}

\\begin{document}

\\section{$title}

$content

\\end{document}
EOF
    else
        # Chapter file for \input (no preamble, no document environment)
        cat > "$tex_file" << EOF
% Chapter: $title
\\section{$title}

$content
EOF
    fi
    
    if [ $? -eq 0 ]; then
        log_success "Converted: $md_file → $tex_file"
        return 0
    else
        log_fail "Failed to convert: $md_file"
        return 1
    fi
}

# ==============================================================================
# LaTeX Compilation Functions
# ==============================================================================

compile_latex() {
    local tex_file="$1"
    local basename=$(basename "$tex_file" .tex)
    local max_attempts="$MAX_PASSES"
    
    log_info "Compiling $tex_file (up to $max_attempts passes)"
    
    if [ ! -f "$tex_file" ]; then
        log_error "LaTeX file not found: $tex_file"
        return 1
    fi
    
    if ! command -v pdflatex &> /dev/null; then
        log_warning "pdflatex not available, skipping compilation"
        return 2
    fi
    
    # Try compilation with multiple passes
    local pass=1
    local success=false
    
    while [ $pass -le $max_attempts ]; do
        log_info "  Pass $pass/$max_attempts for $basename"
        
        # Run pdflatex
        if pdflatex -interaction=nonstopmode -halt-on-error "$tex_file" >> "$LOG_FILE" 2>&1; then
            success=true
            # Check if we need another pass (for references, etc.)
            if [ $pass -lt $max_attempts ] && grep -q "Rerun" "${basename}.log" 2>/dev/null; then
                log_info "  Rerun required, continuing..."
                ((pass++))
                continue
            else
                break
            fi
        else
            log_warning "  Pass $pass failed, attempting fixes..."
            
            # Try to fix common errors
            if fix_latex_errors "$tex_file" "${basename}.log"; then
                log_info "  Applied fixes, retrying..."
                ((pass++))
                continue
            else
                log_error "  Could not fix errors"
                break
            fi
        fi
        
        ((pass++))
    done
    
    # Check if PDF was created
    if [ -f "${basename}.pdf" ]; then
        log_success "Compiled: $tex_file → ${basename}.pdf"
        return 0
    else
        log_fail "Failed to compile: $tex_file"
        # Extract and log error
        if [ -f "${basename}.log" ]; then
            log_error "Last error in ${basename}.log:"
            grep -A 3 "^!" "${basename}.log" | tail -5 >> "$ERROR_LOG"
        fi
        return 1
    fi
}

fix_latex_errors() {
    local tex_file="$1"
    local log_file="$2"
    
    if [ ! -f "$log_file" ]; then
        return 1
    fi
    
    local fixed=false
    
    # Check for undefined control sequence
    if grep -q "Undefined control sequence" "$log_file"; then
        log_info "    Fixing undefined control sequences..."
        
        # Add missing packages
        if ! grep -q "\\usepackage{physics}" "$tex_file"; then
            sed -i '/\\usepackage{hyperref}/a \\usepackage{physics}' "$tex_file"
            fixed=true
        fi
        
        if ! grep -q "\\usepackage{amssymb}" "$tex_file"; then
            sed -i '/\\usepackage{amsmath}/a \\usepackage{amssymb}' "$tex_file"
            fixed=true
        fi
    fi
    
    # Check for missing font shape
    if grep -q "Font shape" "$log_file"; then
        log_info "    Fixing font shape issues..."
        if ! grep -q "\\usepackage[T1]{fontenc}" "$tex_file"; then
            sed -i '/\\usepackage\[utf8\]{inputenc}/a \\usepackage[T1]{fontenc}' "$tex_file"
            fixed=true
        fi
    fi
    
    # Check for overfull/underfull boxes (warning, not error - ignore)
    # These are just warnings, not errors
    
    if [ "$fixed" = true ]; then
        log_success "    Applied fixes to $tex_file"
        return 0
    else
        return 1
    fi
}

# ==============================================================================
# Main Compilation Workflow
# ==============================================================================

create_main_tex() {
    log_info "Creating main.tex file"
    
    cat > "$MAIN_TEX" << 'EOF'
\documentclass[12pt,a4paper]{book}

% Packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{physics}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage[margin=2.5cm]{geometry}

% Physics notation
\renewcommand{\varphi}{\phi}

\title{Dynamic Vacuum Field Theory\\Complete Collection}
\author{DVFT Research}
\date{\today}

\begin{document}

\maketitle
\tableofcontents
\newpage

% Include all chapters
EOF
    
    # Add input statements for chapters that exist
    local chapters_added=0
    
    # Check for chapter 00
    if [ -f "kapitel_00.tex" ]; then
        echo "\\input{kapitel_00}" >> "$MAIN_TEX"
        ((chapters_added++))
    fi
    
    # Add chapters 01-43
    for i in $(seq 1 43); do
        local chapter_num=$(printf "%02d" $i)
        local tex_file="kapitel_${chapter_num}.tex"
        
        if [ -f "$tex_file" ]; then
            echo "\\input{kapitel_${chapter_num}}" >> "$MAIN_TEX"
            ((chapters_added++))
        fi
    done
    
    cat >> "$MAIN_TEX" << 'EOF'

\end{document}
EOF
    
    log_success "Created $MAIN_TEX with $chapters_added chapters"
}

convert_all_chapters() {
    log_info "Converting all Markdown chapters to LaTeX..."
    
    # Convert 00_Vorspann.md to kapitel_00.tex
    if [ -f "00_Vorspann.md" ]; then
        ((TOTAL_FILES++))
        if convert_markdown_to_latex "00_Vorspann.md" "kapitel_00.tex" "no"; then
            ((CONVERTED_FILES++))
        fi
    fi
    
    # Convert Kapitel_01.md to Kapitel_43.md
    for i in $(seq 1 43); do
        local chapter_num=$(printf "%02d" $i)
        local md_file="Kapitel_${chapter_num}.md"
        local tex_file="kapitel_${chapter_num}.tex"
        
        if [ -f "$md_file" ]; then
            ((TOTAL_FILES++))
            if convert_markdown_to_latex "$md_file" "$tex_file" "no"; then
                ((CONVERTED_FILES++))
            fi
        fi
    done
    
    log_info "Conversion complete: $CONVERTED_FILES/$TOTAL_FILES files converted"
}

convert_all_chapters_standalone() {
    log_info "Converting all Markdown chapters to standalone LaTeX..."
    
    # Convert 00_Vorspann.md to kapitel_00_standalone.tex
    if [ -f "00_Vorspann.md" ]; then
        if convert_markdown_to_latex "00_Vorspann.md" "kapitel_00_standalone.tex" "yes"; then
            log_success "Created standalone: kapitel_00_standalone.tex"
        fi
    fi
    
    # Convert Kapitel_01.md to Kapitel_43.md
    for i in $(seq 1 43); do
        local chapter_num=$(printf "%02d" $i)
        local md_file="Kapitel_${chapter_num}.md"
        local tex_file="kapitel_${chapter_num}_standalone.tex"
        
        if [ -f "$md_file" ]; then
            if convert_markdown_to_latex "$md_file" "$tex_file" "yes"; then
                log_success "Created standalone: $tex_file"
            fi
        fi
    done
    
    log_info "Standalone conversion complete"
}

compile_all_chapters() {
    log_info "Compiling all LaTeX chapters..."
    
    if ! command -v pdflatex &> /dev/null; then
        log_warning "Skipping compilation - pdflatex not available"
        return
    fi
    
    # Compile individual standalone chapters
    log_info "Compiling standalone chapters..."
    for i in $(seq 0 43); do
        local chapter_num=$(printf "%02d" $i)
        local tex_file="kapitel_${chapter_num}_standalone.tex"
        
        if [ -f "$tex_file" ]; then
            if compile_latex "$tex_file"; then
                ((COMPILED_FILES++))
            else
                ((FAILED_FILES++))
            fi
        fi
    done
    
    # Compile main.tex
    if [ -f "$MAIN_TEX" ]; then
        log_info "Compiling main document: $MAIN_TEX"
        if compile_latex "$MAIN_TEX"; then
            ((COMPILED_FILES++))
        else
            ((FAILED_FILES++))
        fi
    fi
    
    log_info "Compilation complete: $COMPILED_FILES compiled, $FAILED_FILES failed"
}

cleanup_aux_files() {
    log_info "Cleaning up auxiliary files..."
    
    # Remove auxiliary files but keep PDFs and logs
    rm -f *.aux *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz *.nav *.snm *.vrb
    
    log_success "Cleanup complete"
}

# ==============================================================================
# Main Script
# ==============================================================================

main() {
    init
    
    # Step 1: Convert all Markdown files to LaTeX (for \input in main.tex)
    convert_all_chapters
    
    # Step 2: Create main.tex
    create_main_tex
    
    # Step 3: Convert all Markdown files to standalone LaTeX (for individual compilation)
    convert_all_chapters_standalone
    
    # Step 4: Compile all LaTeX files
    compile_all_chapters
    
    # Step 5: Cleanup
    cleanup_aux_files
    
    # Summary
    log "============================================================"
    log "SUMMARY"
    log "============================================================"
    log "Total Markdown files: $TOTAL_FILES"
    log "Successfully converted: $CONVERTED_FILES"
    log "Successfully compiled: $COMPILED_FILES"
    log "Failed compilations: $FAILED_FILES"
    log "============================================================"
    log "Log file: $LOG_FILE"
    log "Error log: $ERROR_LOG"
    log "============================================================"
    
    if [ $FAILED_FILES -gt 0 ]; then
        log_warning "Some compilations failed. Check $ERROR_LOG for details."
        return 1
    else
        log_success "All operations completed successfully!"
        return 0
    fi
}

# Run main function
main
exit $?
