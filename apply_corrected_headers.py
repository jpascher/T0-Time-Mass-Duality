#!/usr/bin/env python3
"""
Apply corrected universal preamble to all unified LaTeX files.
This script updates all .tex files in unified_latex/ directory with the corrected header.
"""

import os
import re
from pathlib import Path

# Corrected universal preamble
CORRECTED_PREAMBLE = r"""\documentclass[11pt,a4paper,openany]{book}

% Essential packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage[a4paper,margin=2.5cm]{geometry}
\usepackage{lmodern}

% Math and physics packages
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{mathtools}
\usepackage{physics}
\usepackage{siunitx}

% Graphics and tables
\usepackage{graphicx}
\usepackage[table,xcdraw]{xcolor}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{tcolorbox}
\usepackage{booktabs}
\usepackage{array}
\usepackage{longtable}
\usepackage{float}

% Document formatting
\usepackage{fancyhdr}
\usepackage{tocloft}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{microtype}
\usepackage{enumitem}
\usepackage{newunicodechar}

% Additional packages (cleaned up - removed duplicates)
\usepackage{adjustbox}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{amsfonts}
\usepackage{bm}
\usepackage{braket}
\usepackage{breakurl}
\usepackage{cancel}
\usepackage{caption}
\usepackage{cite}
\usepackage{csquotes}
\usepackage{doi}
\usepackage{forest}
\usepackage{gensymb}
\usepackage{hyphenat}
\usepackage{listings}
\usepackage{mdframed}
\usepackage{multicol}
\usepackage{multirow}
\usepackage{natbib}
\usepackage{pdflscape}
\usepackage{ragged2e}
\usepackage{setspace}
\usepackage{slashed}
\usepackage{tabularx}
\usepackage{textcomp}
\usepackage{textgreek}
\usepackage{upgreek}
\usepackage{url}

% Color definitions (FIXED: removed extra \definecolor commands)
\definecolor{blue}{rgb}{0,0,1}
\definecolor{boxgray}{RGB}{240,240,240}
\definecolor{deepblue}{RGB}{0,0,127}
\definecolor{deepgreen}{RGB}{0,127,0}
\definecolor{deepred}{RGB}{191,0,0}
\definecolor{t0blue}{RGB}{0,102,204}
\definecolor{t0green}{RGB}{0,153,0}
\definecolor{t0orange}{RGB}{255,152,0}
\definecolor{t0purple}{RGB}{102,0,204}
\definecolor{t0red}{RGB}{204,0,0}
\definecolor{t0yellow}{RGB}{255,204,0}

% TikZ libraries
\usetikzlibrary{arrows,shapes,positioning,calc,patterns,decorations.pathmorphing,decorations.markings}

% PGFPlots setup
\pgfplotsset{compat=1.18}

% Hyperref setup
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=cyan,
    citecolor=green,
    pdftitle={T0 Theory Document},
    pdfauthor={Johann Pascher},
    pdfsubject={T0 Theory},
    pdfkeywords={T0, physics, theory}
}

% Header and footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
\fancyfoot[C]{T0 Theory - Johann Pascher}

% Theorem environments
\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}
\newtheorem{remark}{Remark}[section]
\newtheorem{example}{Example}[section]

% Custom commands (common across T0 documents)
\newcommand{\T}[1]{\text{#1}}
\newcommand{\mat}[1]{\mathbf{#1}}
\newcommand{\E}{\mathrm{e}}
\newcommand{\I}{\mathrm{i}}
\newcommand{\diff}{\mathrm{d}}
\newcommand{\Real}{\mathrm{Re}}
\newcommand{\Imag}{\mathrm{Im}}

"""

def extract_document_body(content):
    """Extract content between \begin{document} and \end{document}."""
    begin_match = re.search(r'\\begin\{document\}', content)
    end_match = re.search(r'\\end\{document\}', content)
    
    if begin_match and end_match:
        start = begin_match.end()
        end = end_match.start()
        return content[start:end].strip()
    
    # If no document environment found, return content after preamble
    # Try to find where the preamble ends
    lines = content.split('\n')
    content_start = 0
    in_preamble = True
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Skip empty lines and comments
        if not stripped or stripped.startswith('%'):
            continue
        # Check if line is a preamble command
        if stripped.startswith('\\documentclass') or stripped.startswith('\\usepackage') or \
           stripped.startswith('\\definecolor') or stripped.startswith('\\newcommand') or \
           stripped.startswith('\\renewcommand') or stripped.startswith('\\geometry') or \
           stripped.startswith('\\pagestyle') or stripped.startswith('\\theoremstyle') or \
           stripped.startswith('\\newtheorem') or stripped.startswith('\\hypersetup') or \
           stripped.startswith('\\usetikzlibrary') or stripped.startswith('\\pgfplotsset') or \
           stripped.startswith('\\fancyhead') or stripped.startswith('\\fancyfoot') or \
           stripped.startswith('\\fancyhf') or stripped.startswith('\\setlength') or \
           stripped.startswith('\\newunicodechar'):
            continue
        # Found content
        content_start = i
        break
    
    return '\n'.join(lines[content_start:]).strip()

def update_file(filepath):
    """Update a single .tex file with corrected preamble."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract document body
        body = extract_document_body(content)
        
        # Create new content with corrected preamble
        new_content = CORRECTED_PREAMBLE + '\n\\begin{document}\n\n' + body + '\n\n\\end{document}\n'
        
        # Write updated content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, None
    except Exception as e:
        return False, str(e)

def main():
    """Main function to update all files."""
    script_dir = Path(__file__).parent
    unified_latex_dir = script_dir / 'unified_latex'
    
    if not unified_latex_dir.exists():
        print(f"Error: Directory '{unified_latex_dir}' not found!")
        return 1
    
    # Get all .tex files
    tex_files = list(unified_latex_dir.glob('*.tex'))
    
    if not tex_files:
        print(f"No .tex files found in '{unified_latex_dir}'")
        return 1
    
    print(f"Found {len(tex_files)} .tex files to update...")
    print(f"Applying corrected universal preamble to all files...\n")
    
    success_count = 0
    fail_count = 0
    errors = []
    
    for tex_file in sorted(tex_files):
        success, error = update_file(tex_file)
        if success:
            success_count += 1
            print(f"✓ {tex_file.name}")
        else:
            fail_count += 1
            errors.append((tex_file.name, error))
            print(f"✗ {tex_file.name}: {error}")
    
    print(f"\n{'='*60}")
    print(f"Update complete!")
    print(f"  Success: {success_count} files")
    print(f"  Failed:  {fail_count} files")
    print(f"{'='*60}")
    
    if errors:
        print("\nErrors:")
        for filename, error in errors:
            print(f"  - {filename}: {error}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
