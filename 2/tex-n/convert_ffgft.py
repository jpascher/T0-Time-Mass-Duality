#!/usr/bin/env python3
"""
FFGFT Document Converter
Converts FFGFT.txt to LaTeX format (English) and generates German translation
"""

import re
import sys
import os

def read_ffgft_source(filename):
    """Read the FFGFT.txt source file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()

def parse_chapters(lines):
    """Parse the document into chapters"""
    chapters = []
    current_chapter = None
    current_content = []
    
    for line in lines:
        # Check for chapter headers
        if line.strip().startswith('CHAPTER '):
            if current_chapter:
                chapters.append({
                    'title': current_chapter,
                    'content': current_content
                })
            current_chapter = line.strip()
            current_content = []
        elif current_chapter:
            current_content.append(line)
    
    # Add last chapter
    if current_chapter:
        chapters.append({
            'title': current_chapter,
            'content': current_content
        })
    
    return chapters

def convert_math_expressions(text):
    """Convert mathematical expressions to LaTeX"""
    # Convert superscripts like e^{iθ}
    text = re.sub(r'e\^{([^}]+)}', r'e^{\1}', text)
    text = re.sub(r'e\^\(([^\)]+)\)', r'e^{\1}', text)
    
    # Convert subscripts
    text = re.sub(r'ρ₀', r'\\rho_0', text)
    text = re.sub(r'Φ', r'\\Phi', text)
    text = re.sub(r'φ', r'\\phi', text)
    text = re.sub(r'θ', r'\\theta', text)
    text = re.sub(r'ρ', r'\\rho', text)
    text = re.sub(r'μ', r'\\mu', text)
    
    # Wrap standalone equations
    if '=' in text and len(text.strip()) < 80 and not text.strip().startswith('•'):
        text = f'\\[{text.strip()}\\]\n'
    
    return text

def generate_latex_preamble():
    """Generate LaTeX document preamble"""
    return r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amsfonts,amssymb}
\usepackage{physics}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{cite}

\geometry{margin=1in}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{Fundamental Fractal-Geometric Field Theory}
\fancyfoot[C]{\thepage}

\title{Fundamental Fractal-Geometric Field Theory}
\author{Satish B. Thorwe, MSc\\Robert Gordon University, Aberdeen UK}
\date{}

\begin{document}

\maketitle

\begin{abstract}
This paper presents a unified theoretical model in which spacetime curvature arises from distortions in a dynamic vacuum field described by a complex scalar $\phi(x)=\rho(x)e^{i\theta(x)}$ where $\phi(x)$ is dynamic vacuum field, $\rho(x)$ is vacuum amplitude and $\theta(x)$ is vacuum phase. The vacuum possesses an intrinsic field with its phase evolves linearly with time and matter locally perturbs it. These perturbations propagate outward at speed of light, producing stress-energy that curves spacetime through Einstein's field equations. The model provides a physical and causal explanation for curvature at a distance and serves as a bridge between Quantum Mechanics and classical General Relativity. Complete mathematical framework for Fundamental Fractal-Geometric Field Theory (FFGFT) is presented with its applications in cosmology and quantum mechanics.
\end{abstract}

\tableofcontents
\newpage

'''

def convert_chapter_to_latex(chapter):
    """Convert a single chapter to LaTeX format"""
    title = chapter['title'].replace('CHAPTER ', '')
    parts = title.split(':', 1)
    if len(parts) == 2:
        number = parts[0].strip()
        name = parts[1].strip()
        latex = f'\\section{{{name}}}\n\\label{{sec:ch{number}}}\n\n'
    else:
        latex = f'\\section{{{title}}}\n\n'
    
    content = ''.join(chapter['content'])
    
    # Convert numbered sections
    content = re.sub(r'^(\d+)\.\s+(.+)$', r'\\subsection{\2}', content, flags=re.MULTILINE)
    
    # Convert bullet points
    content = re.sub(r'^•\s+(.+)$', r'\\item \1', content, flags=re.MULTILINE)
    
    # Wrap itemize blocks
    lines = content.split('\n')
    in_itemize = False
    result_lines = []
    
    for line in lines:
        if '\\item' in line and not in_itemize:
            result_lines.append('\\begin{itemize}')
            in_itemize = True
        elif '\\item' not in line and in_itemize and line.strip():
            result_lines.append('\\end{itemize}')
            in_itemize = False
        result_lines.append(line)
    
    if in_itemize:
        result_lines.append('\\end{itemize}')
    
    content = '\n'.join(result_lines)
    
    # Convert math
    content = convert_math_expressions(content)
    
    return latex + content + '\n\n'

def generate_latex_footer():
    """Generate LaTeX document footer"""
    return r'''
\section{References}
\label{sec:references}

References will be added based on citations in the full document.

\end{document}
'''

def generate_german_translation_header():
    """Generate header for German translation"""
    return r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[ngerman]{babel}
\usepackage{amsmath,amsfonts,amssymb}
\usepackage{physics}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{cite}

\geometry{margin=1in}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{Dynamische Vakuumfeldtheorie}
\fancyfoot[C]{\thepage}

\title{Dynamische Vakuumfeldtheorie}
\author{Satish B. Thorwe, MSc\\Robert Gordon University, Aberdeen UK}
\date{}

\begin{document}

\maketitle

\begin{abstract}
Diese Arbeit präsentiert ein einheitliches theoretisches Modell, in dem die Raumzeit-Krümmung aus Verzerrungen in einem dynamischen Vakuumfeld entsteht, das durch ein komplexes Skalarfeld $\phi(x)=\rho(x)e^{i\theta(x)}$ beschrieben wird, wobei $\phi(x)$ das dynamische Vakuumfeld, $\rho(x)$ die Vakuumamplitude und $\theta(x)$ die Vakuumphase ist. Das Vakuum besitzt ein intrinsisches Feld, dessen Phase sich linear mit der Zeit entwickelt, und Materie stört es lokal. Diese Störungen breiten sich mit Lichtgeschwindigkeit aus und erzeugen Stress-Energie, die die Raumzeit durch Einsteins Feldgleichungen krümmt. Das Modell liefert eine physikalische und kausale Erklärung für Krümmung über Distanz und dient als Brücke zwischen Quantenmechanik und klassischer Allgemeiner Relativitätstheorie. Ein vollständiges mathematisches Rahmenwerk für die Dynamische Vakuumfeldtheorie (FFGFT) wird mit ihren Anwendungen in Kosmologie und Quantenmechanik präsentiert.
\end{abstract}

\tableofcontents
\newpage

'''

def main():
    """Main conversion function"""
    print("Starting FFGFT conversion...")
    
    # Read source
    source_file = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/FFGFT.txt'
    lines = read_ffgft_source(source_file)
    print(f"Read {len(lines)} lines from source")
    
    # Parse chapters
    chapters = parse_chapters(lines)
    print(f"Found {len(chapters)} chapters")
    
    # Generate English LaTeX
    latex_en = generate_latex_preamble()
    
    for i, chapter in enumerate(chapters, 1):
        print(f"Converting chapter {i}/{len(chapters)}: {chapter['title'][:50]}...")
        latex_en += convert_chapter_to_latex(chapter)
    
    latex_en += generate_latex_footer()
    
    # Write English version
    output_en = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/FFGFT_En.tex'
    with open(output_en, 'w', encoding='utf-8') as f:
        f.write(latex_en)
    print(f"✓ English LaTeX written to {output_en} ({len(latex_en)} bytes)")
    
    # Generate German version (simplified translation of structure)
    print("Generating German version structure...")
    latex_de = generate_german_translation_header()
    latex_de += "\\section{Hinweis}\nDie vollständige deutsche Übersetzung wird maschinell erstellt und muss manuell überprüft werden.\n\n"
    latex_de += "\\section{Einleitung}\nFFGFT-Dokument - Automatische Konvertierung in Arbeit.\n\n"
    latex_de += generate_latex_footer()
    
    output_de = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/FFGFT_De.tex'
    with open(output_de, 'w', encoding='utf-8') as f:
        f.write(latex_de)
    print(f"✓ German LaTeX template written to {output_de}")
    
    print("\n✓ Conversion complete!")
    print(f"  - English: {len(chapters)} chapters converted")
    print(f"  - German: Template created (requires translation)")
    print(f"\nNext steps:")
    print(f"  1. Review {output_en}")
    print(f"  2. Compile with: pdflatex {output_en}")
    print(f"  3. Use translation service for German version")

if __name__ == '__main__':
    main()
