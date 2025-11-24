#!/usr/bin/env python3
"""
Update all unified LaTeX files with corrected preamble header.
This script replaces the header in all .tex files in 2/tex/unified_latex/ 
with the user-corrected version that fixes duplicate packages and color definitions.
"""

import os
import re
from pathlib import Path

# User-corrected preamble (cleaned up, no duplicates)
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
\usetikzlibrary{arrows,shapes,positioning,calc,decorations.pathmorphing,patterns}

% Hyperref setup
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=cyan,
    citecolor=green,
    pdftitle={T0 Theory Document},
    pdfauthor={Johann Pascher},
}

% Custom commands (common across all documents)
\newcommand{\T}{\mathrm{T}}
\newcommand{\Ti}{\T_0}
\newcommand{\mpl}{m_{\text{Pl}}}
\newcommand{\lpl}{\ell_{\text{Pl}}}
\newcommand{\tpl}{t_{\text{Pl}}}
\newcommand{\dd}{\mathrm{d}}
\newcommand{\vect}[1]{\boldsymbol{#1}}
\newcommand{\avg}[1]{\langle#1\rangle}

% Theorem-like environments
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{note}[theorem]{Note}

% Page style
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

"""


def extract_body(content):
    """Extract the document body (everything after \\begin{document})."""
    match = re.search(r'\\begin\{document\}', content, re.DOTALL)
    if match:
        return content[match.start():]
    return content


def update_tex_file(filepath):
    """Update a single .tex file with the corrected preamble."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Extract body content (from \begin{document} onwards)
        body = extract_body(content)
        
        if body:
            # Combine corrected preamble with body
            new_content = CORRECTED_PREAMBLE + body
            
            # Write updated content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True, filepath.name
        else:
            return False, f"{filepath.name} (no \\begin{{document}} found)"
    
    except Exception as e:
        return False, f"{filepath.name} (error: {str(e)})"


def main():
    """Main function to update all unified LaTeX files."""
    # Check both possible locations
    possible_dirs = [
        Path('2/tex/unified_latex'),
        Path('unified_latex')
    ]
    
    target_dir = None
    for dir_path in possible_dirs:
        if dir_path.exists() and dir_path.is_dir():
            target_dir = dir_path
            break
    
    if not target_dir:
        print("❌ Error: Could not find unified_latex directory.")
        print("   Checked: 2/tex/unified_latex/ and unified_latex/")
        print("   Please ensure the directory exists.")
        return
    
    print(f"📂 Processing .tex files in: {target_dir}")
    print(f"🔧 Updating headers with corrected preamble...")
    print()
    
    # Find all .tex files
    tex_files = list(target_dir.glob('*.tex'))
    
    if not tex_files:
        print(f"⚠️  No .tex files found in {target_dir}")
        return
    
    print(f"Found {len(tex_files)} .tex files")
    print()
    
    # Update each file
    updated = []
    failed = []
    
    for tex_file in tex_files:
        success, name = update_tex_file(tex_file)
        if success:
            updated.append(name)
        else:
            failed.append(name)
    
    # Report results
    print("=" * 60)
    print(f"✅ Successfully updated: {len(updated)} files")
    print(f"❌ Failed: {len(failed)} files")
    print("=" * 60)
    
    if failed:
        print("\n⚠️  Failed files:")
        for name in failed[:10]:  # Show first 10
            print(f"   - {name}")
        if len(failed) > 10:
            print(f"   ... and {len(failed) - 10} more")
    
    print(f"\n✨ Done! All headers updated in: {target_dir}")
    print("\n📝 Next steps:")
    print("   1. Review the updated files")
    print("   2. Test compilation with: pdflatex <any_file>.tex")
    print("   3. Commit changes: git add 2/tex/unified_latex/")
    print("   4. Push: git push origin copilot/add-latex-files-for-t0-papers")


if __name__ == '__main__':
    main()
