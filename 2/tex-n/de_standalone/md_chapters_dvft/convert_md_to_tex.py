#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DVFT Markdown to LaTeX Converter
Converts markdown files to LaTeX with proper Unicode handling
"""

import re
import sys
from pathlib import Path

# Unicode to LaTeX mappings
UNICODE_REPLACEMENTS = [
    # Mathematical italic letters (lowercase)
    ('𝑥', 'x'), ('𝑡', 't'), ('𝑚', 'm'), ('𝑛', 'n'), ('𝑖', 'i'),
    ('𝑒', 'e'), ('𝑘', 'k'), ('𝑟', 'r'), ('𝑐', 'c'), ('𝑔', 'g'),
    ('𝑎', 'a'), ('𝑏', 'b'), ('𝑑', 'd'), ('𝑓', 'f'), ('𝑝', 'p'),
    ('𝑠', 's'), ('𝑣', 'v'), ('𝑤', 'w'), ('𝑦', 'y'), ('𝑧', 'z'),
    
    # Mathematical italic letters (uppercase)
    ('𝐺', 'G'), ('𝐸', 'E'), ('𝐿', 'L'), ('𝑇', 'T'), ('𝑀', 'M'),
    ('𝐴', 'A'), ('𝐵', 'B'), ('𝐶', 'C'), ('𝐷', 'D'), ('𝐹', 'F'),
    ('𝐻', 'H'), ('𝐾', 'K'), ('𝑁', 'N'), ('𝑃', 'P'), ('𝑅', 'R'),
    ('𝑆', 'S'), ('𝑉', 'V'), ('𝑊', 'W'), ('𝑋', 'X'), ('𝑌', 'Y'),
    ('𝑍', 'Z'),
    
    # Greek letters (multiple Unicode variants - italic math)
    ('𝛼', r'\alpha'), ('𝛽', r'\beta'), ('𝛾', r'\gamma'), ('𝛿', r'\delta'),
    ('𝜀', r'\varepsilon'), ('𝜁', r'\zeta'), ('𝜂', r'\eta'), ('𝜃', r'\theta'),
    ('𝜄', r'\iota'), ('𝜅', r'\kappa'), ('𝜆', r'\lambda'), ('𝜇', r'\mu'),
    ('𝜈', r'\nu'), ('𝜉', r'\xi'), ('𝜋', r'\pi'), ('𝜌', r'\rho'),
    ('𝜎', r'\sigma'), ('𝜏', r'\tau'), ('𝜐', r'\upsilon'), ('𝜙', r'\varphi'),
    ('𝜒', r'\chi'), ('𝜓', r'\psi'), ('𝜔', r'\omega'),
    
    # Greek letters (normal Unicode)
    ('ϕ', r'\phi'), ('Φ', r'\Phi'),
    ('ρ', r'\rho'),
    ('θ', r'\theta'), ('Θ', r'\Theta'),
    ('μ', r'\mu'), ('λ', r'\lambda'), ('α', r'\alpha'),
    ('β', r'\beta'), ('γ', r'\gamma'), ('δ', r'\delta'),
    ('ε', r'\varepsilon'), ('η', r'\eta'), ('ξ', r'\xi'),
    ('π', r'\pi'), ('σ', r'\sigma'), ('τ', r'\tau'),
    ('ω', r'\omega'), ('Ω', r'\Omega'),
    
    # Superscripts
    ('²', r'\textsuperscript{2}'), ('³', r'\textsuperscript{3}'),
    ('⁰', r'\textsuperscript{0}'),
    
    # Subscripts
    ('₀', r'$_0$'), ('₁', r'$_1$'), ('₂', r'$_2$'),
    ('₃', r'$_3$'), ('₄', r'$_4$'),
    
    # Math operators and symbols
    ('−', '-'),  # Minus sign (U+2212) -> hyphen
    ('≈', r' $\approx$ '), ('≠', r' $\neq$ '),
    ('≤', r' $\leq$ '), ('≥', r' $\geq$ '),
    ('∂', r'$\partial$'), ('∇', r'$\nabla$'),
    ('√', r'$\sqrt$'), ('∞', r'$\infty$'),
    ('±', r' $\pm$ '), ('×', r' $\times$ '), ('÷', r' $\div$ '),
    ('∫', r'$\int$'), ('∑', r'$\sum$'), ('∏', r'$\prod$'),
    ('▫', r'$\Box$'),
    ('∗', '*'),  # Asterisk operator
    
    # Special symbols
    ('●', r'$\bullet$'), ('•', r'$\bullet$'),
    ('–', '--'), ('—', '---'), ('…', r'\ldots{}'),
]

def replace_unicode(text):
    """Replace Unicode characters with LaTeX equivalents"""
    for unicode_char, latex_cmd in UNICODE_REPLACEMENTS:
        text = text.replace(unicode_char, latex_cmd)
    return text

def convert_md_to_tex(md_file, tex_file):
    """Convert a single markdown file to LaTeX"""
    print(f"Converting: {md_file.name} -> {tex_file.name}")
    
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    output_lines = []
    skip_first_header = True
    
    for line in lines:
        # Remove Windows line endings
        line = line.rstrip('\r\n')
        
        # Skip the first markdown header (chapter title)
        if skip_first_header and re.match(r'^# (Kapitel \d+|00 Vorspann)$', line):
            skip_first_header = False
            continue
        
        # Convert other headers to sections
        if line.startswith('# '):
            section_title = line[2:].strip()
            line = f'\\section{{{section_title}}}'
        
        # Replace Unicode characters
        line = replace_unicode(line)
        
        output_lines.append(line)
    
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

def main():
    script_dir = Path(__file__).parent
    
    print("=== DVFT Markdown to LaTeX Converter (Python) ===")
    print(f"Working directory: {script_dir}")
    print()
    
    # Convert 00_Vorspann.md
    md_file = script_dir / "00_Vorspann.md"
    if md_file.exists():
        convert_md_to_tex(md_file, script_dir / "kapitel_00.tex")
    
    # Convert Kapitel_01.md to Kapitel_43.md
    for i in range(1, 44):
        md_file = script_dir / f"Kapitel_{i:02d}.md"
        if md_file.exists():
            convert_md_to_tex(md_file, script_dir / f"kapitel_{i:02d}.tex")
        else:
            print(f"Warning: {md_file.name} not found, skipping...")
    
    print()
    print("=== Conversion Complete ===")
    print(f"Generated {44} LaTeX files")

if __name__ == '__main__':
    main()
