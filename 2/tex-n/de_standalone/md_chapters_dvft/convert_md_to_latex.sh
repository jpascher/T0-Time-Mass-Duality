#!/bin/bash

# ==============================================================================
# DVFT Markdown to LaTeX Conversion Script
# ==============================================================================
# This script converts all Markdown files (00_Vorspann.md to Kapitel_43.md)
# to LaTeX files (kapitel_00.tex to kapitel_43.tex) with proper formatting
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== DVFT Markdown to LaTeX Converter ==="
echo "Working directory: $SCRIPT_DIR"
echo ""

# Run Python conversion script
python3 convert_md_to_tex.py

echo ""
echo "=== Creating main.tex ==="

# Create main.tex file
cat > main.tex << 'EOF'
\documentclass[12pt,a4paper]{article}

% Include the shared T0 preamble
\input{../../../../T0_preamble_shared_De.tex}

% Additional packages for this document
\usepackage{physics}

\begin{document}

% Title page
\title{Dynamic Vacuum Field Theory\\Complete Chapters}
\author{Satish B. Thorwe}
\date{\today}
\maketitle

\tableofcontents
\newpage

% Include all chapters
\input{kapitel_00.tex}
\newpage

\input{kapitel_01.tex}
\newpage

\input{kapitel_02.tex}
\newpage

\input{kapitel_03.tex}
\newpage

\input{kapitel_04.tex}
\newpage

\input{kapitel_05.tex}
\newpage

\input{kapitel_06.tex}
\newpage

\input{kapitel_07.tex}
\newpage

\input{kapitel_08.tex}
\newpage

\input{kapitel_09.tex}
\newpage

\input{kapitel_10.tex}
\newpage

\input{kapitel_11.tex}
\newpage

\input{kapitel_12.tex}
\newpage

\input{kapitel_13.tex}
\newpage

\input{kapitel_14.tex}
\newpage

\input{kapitel_15.tex}
\newpage

\input{kapitel_16.tex}
\newpage

\input{kapitel_17.tex}
\newpage

\input{kapitel_18.tex}
\newpage

\input{kapitel_19.tex}
\newpage

\input{kapitel_20.tex}
\newpage

\input{kapitel_21.tex}
\newpage

\input{kapitel_22.tex}
\newpage

\input{kapitel_23.tex}
\newpage

\input{kapitel_24.tex}
\newpage

\input{kapitel_25.tex}
\newpage

\input{kapitel_26.tex}
\newpage

\input{kapitel_27.tex}
\newpage

\input{kapitel_28.tex}
\newpage

\input{kapitel_29.tex}
\newpage

\input{kapitel_30.tex}
\newpage

\input{kapitel_31.tex}
\newpage

\input{kapitel_32.tex}
\newpage

\input{kapitel_33.tex}
\newpage

\input{kapitel_34.tex}
\newpage

\input{kapitel_35.tex}
\newpage

\input{kapitel_36.tex}
\newpage

\input{kapitel_37.tex}
\newpage

\input{kapitel_38.tex}
\newpage

\input{kapitel_39.tex}
\newpage

\input{kapitel_40.tex}
\newpage

\input{kapitel_41.tex}
\newpage

\input{kapitel_42.tex}
\newpage

\input{kapitel_43.tex}

\end{document}
EOF

echo "main.tex created successfully"
echo ""

echo "=== Compiling LaTeX files recursively ==="
echo ""

# Function to compile with error handling
compile_latex() {
    local max_attempts=3
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        echo "Compilation attempt $attempt of $max_attempts..."
        
        # Run pdflatex
        sudo pdflatex -interaction=nonstopmode -halt-on-error main.tex > compile.log 2>&1
        
        if [ $? -eq 0 ]; then
            echo "✓ Compilation successful!"
            
            # Run again for references and TOC
            echo "Running second pass for references..."
            sudo pdflatex -interaction=nonstopmode -halt-on-error main.tex > compile2.log 2>&1
            
            if [ -f "main.pdf" ]; then
                echo "✓ PDF generated successfully: main.pdf"
                return 0
            fi
        else
            echo "✗ Compilation failed on attempt $attempt"
            
            # Check for missing packages
            if grep -q "! LaTeX Error: File.*not found" compile.log; then
                echo "Checking for missing packages..."
                
                # Extract package names and try to install
                missing_packages=$(grep "! LaTeX Error: File.*sty" compile.log | sed -n "s/.*File \`\(.*\)\.sty' not found.*/\1/p" | sort -u)
                
                if [ -n "$missing_packages" ]; then
                    echo "Found missing packages: $missing_packages"
                    echo "Attempting to install missing packages..."
                    
                    # Try to install common LaTeX packages
                    sudo apt-get install -y texlive-latex-extra texlive-science texlive-fonts-extra > /dev/null 2>&1 || true
                fi
            fi
            
            # Show error details
            echo ""
            echo "Error details from compile.log:"
            grep -A 5 "^!" compile.log | head -20 || echo "No specific errors found in log"
        fi
        
        attempt=$((attempt + 1))
    done
    
    echo "✗ Compilation failed after $max_attempts attempts"
    echo "Please check compile.log for details"
    return 1
}

# Compile the main document
compile_latex

echo ""
echo "=== Conversion Complete ==="
echo "Generated files:"
echo "  - kapitel_00.tex to kapitel_43.tex"
echo "  - main.tex"
if [ -f "main.pdf" ]; then
    echo "  - main.pdf"
fi
echo ""
echo "To recompile manually, run:"
echo "  pdflatex main.tex"
echo ""
