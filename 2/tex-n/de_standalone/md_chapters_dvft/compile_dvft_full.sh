#!/bin/bash
# ==============================================================================
# DVFT Full Compilation Script
# ==============================================================================
# This script:
# 1. Converts Markdown files (00_Vorspann.md to Kapitel_43.md) to LaTeX
# 2. Creates a main.tex file that includes all chapters
# 3. Compiles each chapter and main.tex with pdflatex
# 4. Fixes common errors iteratively until successful
# 5. Logs all output and errors
#
# Author: Johann Pascher / GitHub Copilot
# Date: 2025-12-28
# ==============================================================================

set -o pipefail

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/compilation.log"
ERROR_LOG="$SCRIPT_DIR/errors.log"
MAX_RETRIES=5
PREAMBLE_PATH="../../../T0_preamble_shared_De.tex"

# Counters
TOTAL_FILES=0
SUCCESS_COUNT=0
FAILED_COUNT=0

# Initialize log files
echo "=== DVFT Full Compilation ===" > "$LOG_FILE"
echo "Started: $(date)" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "=== DVFT Compilation Errors ===" > "$ERROR_LOG"
echo "Started: $(date)" >> "$ERROR_LOG"
echo "" >> "$ERROR_LOG"

# Function to print colored messages
print_msg() {
    local color=$1
    shift
    echo -e "${color}$@${NC}"
}

print_status() {
    print_msg "$BLUE" "[INFO] $@"
}

print_success() {
    print_msg "$GREEN" "[SUCCESS] $@"
}

print_warning() {
    print_msg "$YELLOW" "[WARNING] $@"
}

print_error() {
    print_msg "$RED" "[ERROR] $@"
}

# Function to convert markdown to LaTeX
convert_md_to_tex() {
    local md_file=$1
    local tex_file=$2
    
    print_status "Converting $md_file to $tex_file..."
    
    # Extract chapter title from markdown
    local chapter_title=$(head -1 "$md_file" | sed 's/^# //')
    local chapter_num=$(echo "$chapter_title" | grep -o '[0-9]\+' | head -1)
    
    # Start creating LaTeX file
    cat > "$tex_file" <<'EOF'
\documentclass[12pt,a4paper]{article}

% Use shared T0 preamble
EOF
    echo "\\input{$PREAMBLE_PATH}" >> "$tex_file"
    cat >> "$tex_file" <<EOF

\\title{$chapter_title}
\\author{}
\\date{}

\\begin{document}
\\maketitle

EOF
    
    # Process markdown content
    # Skip the first line (title) and convert the rest
    tail -n +2 "$md_file" | while IFS= read -r line; do
        # Skip empty lines at the start
        if [[ -z "$line" && ! -s "${tex_file}.tmp" ]]; then
            continue
        fi
        
        # Convert headers
        if [[ "$line" =~ ^###[[:space:]](.+)$ ]]; then
            echo "\\subsubsection{${BASH_REMATCH[1]}}" >> "${tex_file}.tmp"
        elif [[ "$line" =~ ^##[[:space:]](.+)$ ]]; then
            echo "\\subsection{${BASH_REMATCH[1]}}" >> "${tex_file}.tmp"
        elif [[ "$line" =~ ^#[[:space:]](.+)$ ]]; then
            echo "\\section{${BASH_REMATCH[1]}}" >> "${tex_file}.tmp"
        else
            # Convert special characters and math notation
            local converted_line="$line"
            
            # Convert Greek letters and symbols
            converted_line=$(echo "$converted_line" | sed \
                -e 's/φ/\\varphi/g' \
                -e 's/Φ/\\Phi/g' \
                -e 's/ρ/\\rho/g' \
                -e 's/θ/\\theta/g' \
                -e 's/μ/\\mu/g' \
                -e 's/λ/\\lambda/g' \
                -e 's/α/\\alpha/g' \
                -e 's/β/\\beta/g' \
                -e 's/γ/\\gamma/g' \
                -e 's/δ/\\delta/g' \
                -e 's/ε/\\varepsilon/g' \
                -e 's/π/\\pi/g' \
                -e 's/σ/\\sigma/g' \
                -e 's/τ/\\tau/g' \
                -e 's/ω/\\omega/g' \
                -e 's/Ω/\\Omega/g' \
                -e 's/ξ/\\xi/g' \
                -e 's/ℏ/\\hbar/g' \
                -e 's/∇/\\nabla/g' \
                -e 's/∂/\\partial/g' \
                -e 's/∫/\\int/g' \
                -e 's/∑/\\sum/g' \
                -e 's/√/\\sqrt/g' \
                -e 's/≈/\\approx/g' \
                -e 's/≠/\\neq/g' \
                -e 's/≤/\\leq/g' \
                -e 's/≥/\\geq/g' \
                -e 's/→/\\rightarrow/g' \
                -e 's/←/\\leftarrow/g' \
                -e 's/↔/\\leftrightarrow/g' \
                -e 's/⟨/\\langle/g' \
                -e 's/⟩/\\rangle/g' \
                -e 's/×/\\times/g' \
                -e 's/÷/\\div/g' \
                -e 's/±/\\pm/g' \
                -e 's/∞/\\infty/g' \
                -e 's/▫/\\Box/g' \
                -e 's/²/\^2/g' \
                -e 's/³/\^3/g' \
                -e 's/₀/_0/g' \
                -e 's/₁/_1/g' \
                -e 's/₂/_2/g' \
                -e 's/₃/_3/g' \
            )
            
            # Escape special LaTeX characters (but not if already escaped)
            converted_line=$(echo "$converted_line" | sed \
                -e 's/\([^\\]\)%/\1\\%/g' \
                -e 's/\([^\\]\)&/\1\\&/g' \
                -e 's/\([^\\]\)\$/\1\\\$/g' \
            )
            
            # Handle inline math (text between $ symbols)
            # This is basic - more complex math may need manual adjustment
            
            echo "$converted_line" >> "${tex_file}.tmp"
        fi
    done
    
    # Append end of document
    cat >> "${tex_file}.tmp" <<'EOF'

\end{document}
EOF
    
    # Move temp file to final location
    if [[ -f "${tex_file}.tmp" ]]; then
        cat "${tex_file}.tmp" >> "$tex_file"
        rm -f "${tex_file}.tmp"
    fi
    
    print_success "Converted $md_file to $tex_file"
    echo "$(date): Converted $md_file to $tex_file" >> "$LOG_FILE"
}

# Function to create main.tex
create_main_tex() {
    local main_file="$SCRIPT_DIR/main.tex"
    
    print_status "Creating main.tex..."
    
    cat > "$main_file" <<EOF
\\documentclass[12pt,a4paper]{book}

% Use shared T0 preamble
\\input{$PREAMBLE_PATH}

\\title{Dynamic Vacuum Field Theory\\\\Complete Collection}
\\author{Satish B. Thorwe}
\\date{\\today}

\\begin{document}

\\maketitle
\\tableofcontents
\\newpage

EOF
    
    # Add all chapter files as inputs
    echo "% Include all chapters" >> "$main_file"
    
    # Include vorspann (chapter 00)
    echo "\\chapter{Vorspann}" >> "$main_file"
    echo "\\input{kapitel_00_content}" >> "$main_file"
    echo "" >> "$main_file"
    
    # Include chapters 01-43
    for i in $(seq -f "%02g" 1 43); do
        echo "\\chapter{Kapitel $i}" >> "$main_file"
        echo "\\input{kapitel_${i}_content}" >> "$main_file"
        echo "" >> "$main_file"
    done
    
    cat >> "$main_file" <<'EOF'

\end{document}
EOF
    
    print_success "Created main.tex"
    echo "$(date): Created main.tex" >> "$LOG_FILE"
}

# Function to extract content from chapter for inclusion
extract_chapter_content() {
    local tex_file=$1
    local content_file=$2
    
    # Extract content between \begin{document} and \end{document}
    # Skip \maketitle and title-related commands
    sed -n '/\\begin{document}/,/\\end{document}/p' "$tex_file" | \
        sed '1d;$d' | \
        grep -v '\\maketitle' | \
        grep -v '\\title{' | \
        grep -v '\\author{' | \
        grep -v '\\date{' > "$content_file"
    
    echo "$(date): Extracted content from $tex_file to $content_file" >> "$LOG_FILE"
}

# Function to fix common LaTeX errors
fix_latex_errors() {
    local tex_file=$1
    local log_file="${tex_file%.tex}.log"
    
    if [[ ! -f "$log_file" ]]; then
        return 0
    fi
    
    local fixed=0
    
    # Check for undefined control sequence
    if grep -q "Undefined control sequence" "$log_file"; then
        print_warning "Fixing undefined control sequences in $tex_file..."
        
        # Add common packages if missing
        if ! grep -q "\\usepackage{amsmath}" "$tex_file"; then
            sed -i '/\\documentclass/a \\usepackage{amsmath}' "$tex_file"
            fixed=1
        fi
        
        if ! grep -q "\\usepackage{amssymb}" "$tex_file"; then
            sed -i '/\\documentclass/a \\usepackage{amssymb}' "$tex_file"
            fixed=1
        fi
        
        if ! grep -q "\\usepackage{physics}" "$tex_file"; then
            sed -i '/\\documentclass/a \\usepackage{physics}' "$tex_file"
            fixed=1
        fi
    fi
    
    # Check for missing $ inserted
    if grep -q "Missing \\$ inserted" "$log_file"; then
        print_warning "Math mode errors detected in $tex_file"
        # This is harder to fix automatically - log it
        echo "$(date): Math mode errors in $tex_file - manual fix may be needed" >> "$ERROR_LOG"
    fi
    
    # Check for missing packages
    if grep -q "LaTeX Error: File.*not found" "$log_file"; then
        print_warning "Missing package detected in $tex_file"
        local missing_pkg=$(grep "LaTeX Error: File.*not found" "$log_file" | head -1 | sed "s/.*File \`\([^']*\).*/\1/")
        echo "$(date): Missing package: $missing_pkg in $tex_file" >> "$ERROR_LOG"
    fi
    
    return $fixed
}

# Function to compile a LaTeX file with retries
compile_tex() {
    local tex_file=$1
    local basename=$(basename "$tex_file" .tex)
    local dirname=$(dirname "$tex_file")
    
    print_status "Compiling $basename.tex..."
    
    cd "$dirname" || return 1
    
    local retry_count=0
    local success=0
    
    while [[ $retry_count -lt $MAX_RETRIES ]]; do
        # Run pdflatex
        if command -v sudo >/dev/null 2>&1 && [[ $EUID -ne 0 ]]; then
            sudo pdflatex -interaction=nonstopmode -halt-on-error "$basename.tex" >> "$LOG_FILE" 2>&1
            local exit_code=$?
        else
            pdflatex -interaction=nonstopmode -halt-on-error "$basename.tex" >> "$LOG_FILE" 2>&1
            local exit_code=$?
        fi
        
        if [[ $exit_code -eq 0 ]]; then
            success=1
            break
        else
            print_warning "Compilation failed (attempt $((retry_count + 1))/$MAX_RETRIES)"
            
            # Try to fix errors
            fix_latex_errors "$basename.tex"
            local fix_result=$?
            
            if [[ $fix_result -eq 0 ]]; then
                # No fixes applied, log the error
                echo "$(date): Compilation failed for $basename.tex" >> "$ERROR_LOG"
                if [[ -f "$basename.log" ]]; then
                    echo "Error details:" >> "$ERROR_LOG"
                    grep -A 5 "^!" "$basename.log" >> "$ERROR_LOG" 2>/dev/null || true
                    echo "" >> "$ERROR_LOG"
                fi
                break
            fi
        fi
        
        retry_count=$((retry_count + 1))
    done
    
    cd "$SCRIPT_DIR" || return 1
    
    if [[ $success -eq 1 ]]; then
        print_success "Successfully compiled $basename.tex"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        return 0
    else
        print_error "Failed to compile $basename.tex after $MAX_RETRIES attempts"
        FAILED_COUNT=$((FAILED_COUNT + 1))
        return 1
    fi
}

# Function to check if required tools are installed
check_requirements() {
    print_status "Checking requirements..."
    
    local missing_tools=()
    
    if ! command -v pdflatex >/dev/null 2>&1; then
        missing_tools+=("pdflatex (texlive)")
    fi
    
    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        print_error "Missing required tools: ${missing_tools[*]}"
        print_error "Please install them first."
        print_status "On Ubuntu/Debian: sudo apt-get install texlive-latex-extra texlive-fonts-recommended"
        return 1
    fi
    
    print_success "All required tools are installed"
    return 0
}

# Main execution
main() {
    print_msg "$CYAN" "=========================================="
    print_msg "$CYAN" "  DVFT Full Compilation Script"
    print_msg "$CYAN" "=========================================="
    echo ""
    
    # Check requirements
    if ! check_requirements; then
        exit 1
    fi
    
    # Step 1: Convert all markdown files to LaTeX
    print_msg "$CYAN" "\n=== Step 1: Converting Markdown to LaTeX ==="
    
    # Convert vorspann
    if [[ -f "$SCRIPT_DIR/00_Vorspann.md" ]]; then
        convert_md_to_tex "$SCRIPT_DIR/00_Vorspann.md" "$SCRIPT_DIR/kapitel_00.tex"
        TOTAL_FILES=$((TOTAL_FILES + 1))
    fi
    
    # Convert chapters 01-43
    for i in $(seq -f "%02g" 1 43); do
        local md_file="$SCRIPT_DIR/Kapitel_${i}.md"
        local tex_file="$SCRIPT_DIR/kapitel_${i}.tex"
        
        if [[ -f "$md_file" ]]; then
            convert_md_to_tex "$md_file" "$tex_file"
            TOTAL_FILES=$((TOTAL_FILES + 1))
        else
            print_warning "Markdown file not found: $md_file"
        fi
    done
    
    # Step 2: Extract content for inclusion in main.tex
    print_msg "$CYAN" "\n=== Step 2: Extracting Chapter Contents ==="
    
    for i in $(seq -f "%02g" 0 43); do
        local tex_file="$SCRIPT_DIR/kapitel_${i}.tex"
        local content_file="$SCRIPT_DIR/kapitel_${i}_content.tex"
        
        if [[ -f "$tex_file" ]]; then
            extract_chapter_content "$tex_file" "$content_file"
        fi
    done
    
    # Step 3: Create main.tex
    print_msg "$CYAN" "\n=== Step 3: Creating main.tex ==="
    create_main_tex
    
    # Step 4: Compile individual chapters
    print_msg "$CYAN" "\n=== Step 4: Compiling Individual Chapters ==="
    
    for i in $(seq -f "%02g" 0 43); do
        local tex_file="$SCRIPT_DIR/kapitel_${i}.tex"
        
        if [[ -f "$tex_file" ]]; then
            compile_tex "$tex_file"
        fi
    done
    
    # Step 5: Compile main.tex (run multiple times for references)
    print_msg "$CYAN" "\n=== Step 5: Compiling main.tex ==="
    
    for run in 1 2 3; do
        print_status "Main compilation run $run/3..."
        compile_tex "$SCRIPT_DIR/main.tex"
    done
    
    # Summary
    print_msg "$CYAN" "\n=========================================="
    print_msg "$CYAN" "  Compilation Summary"
    print_msg "$CYAN" "=========================================="
    echo ""
    print_status "Total files processed: $TOTAL_FILES"
    print_success "Successfully compiled: $SUCCESS_COUNT"
    print_error "Failed to compile: $FAILED_COUNT"
    echo ""
    print_status "Log file: $LOG_FILE"
    print_status "Error log: $ERROR_LOG"
    echo ""
    
    if [[ $FAILED_COUNT -eq 0 ]]; then
        print_success "All compilations completed successfully!"
        return 0
    else
        print_warning "Some compilations failed. Check the error log for details."
        return 1
    fi
}

# Run main function
main "$@"
