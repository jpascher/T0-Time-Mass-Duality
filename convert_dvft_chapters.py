#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T0 Theory: DVFT Chapter Converter with T0 Integration
======================================================

This script converts DVFT chapters to LaTeX format with T0 theory integration,
cross-references to T0 documents, and alignment with the DVFT_alles_De.tex framework.

Usage:
    python3 convert_dvft_chapters.py [--source DVFT.txt] [--output-dir DIR]

Author: Johann Pascher / Copilot
Date: 2025
"""

import os
import re
import argparse
from pathlib import Path
from datetime import datetime


# Mapping of T0-related topics to PDF documents for cross-referencing
T0_REFERENCE_MAP = {
    'xi': '009_T0_xi_ursprung_De.pdf',
    'ξ': '009_T0_xi_ursprung_De.pdf',
    'Zeit-Masse-Dualität': '002_T0_Grundlagen_De.pdf',
    'Time-Mass Duality': '002_T0_Grundlagen_De.pdf',
    'T(x,t) · m(x,t) = 1': '002_T0_Grundlagen_De.pdf',
    'Teilchenmassen': '006_T0_Teilchenmassen_De.pdf',
    'Feinstrukturkonstante': '011_T0_Feinstruktur_De.pdf',
    'Energiefeld': '004_T0_Energie_De.pdf',
    'E = mc²': '077_E-mc2_De.pdf',
    'Gravitationskonstante': '015_T0_Gravitationskonstante_De.pdf',
    'Kosmologie': '016_T0_Kosmologie_De.pdf',
    'CMB': '030_T0_CMB-Anomalie_De.pdf',
    'Quantenmechanik': '020_T0_QM-QFT-RT_De.pdf',
    'Lagrangian': '027_T0_lagrndian_De.pdf',
    'anomale magnetische Moment': '103_T0_Anomale-g2-6_De.pdf',
    'Neutrinos': '014_T0_Neutrinos_De.pdf',
    'QFT': '097_QFT_De.pdf',
    'Casimir': '091_Casimir_De.pdf',
}


class DVFTChapterConverter:
    """Converts DVFT text chapters to LaTeX with T0 integration."""
    
    def __init__(self, preamble_path="../T0_preamble_shared_De.tex"):
        self.preamble_path = preamble_path
        self.chapter_number = 0
    
    def extract_chapters(self, dvft_text):
        """Extract individual chapters from the full DVFT text."""
        chapters = []
        
        # Split by CHAPTER markers
        chapter_pattern = r'CHAPTER\s+(\d+):\s*([^\n]+)'
        parts = re.split(chapter_pattern, dvft_text)
        
        # First part is introduction/abstract
        if parts[0].strip():
            chapters.append({
                'number': 0,
                'title': 'Einführung und Abstract',
                'content': parts[0].strip()
            })
        
        # Process remaining chapters
        for i in range(1, len(parts), 3):
            if i + 2 <= len(parts):
                chapter_num = parts[i]
                chapter_title = parts[i + 1].strip()
                chapter_content = parts[i + 2].strip() if i + 2 < len(parts) else ''
                
                chapters.append({
                    'number': int(chapter_num),
                    'title': chapter_title,
                    'content': chapter_content
                })
        
        return chapters
    
    def add_t0_cross_references(self, content):
        """Add cross-references to relevant T0 documents."""
        references_added = set()
        modified_content = content
        
        for topic, pdf_file in T0_REFERENCE_MAP.items():
            # Find occurrences of the topic
            pattern = re.escape(topic)
            matches = list(re.finditer(pattern, modified_content, re.IGNORECASE))
            
            if matches and pdf_file not in references_added:
                # Add footnote reference at first occurrence
                first_match = matches[0]
                # Add reference marker
                ref_text = f"\\footnote{{Siehe auch T0-Dokument: \\texttt{{{pdf_file}}}}}"
                insert_pos = first_match.end()
                modified_content = (
                    modified_content[:insert_pos] + 
                    ref_text + 
                    modified_content[insert_pos:]
                )
                references_added.add(pdf_file)
        
        return modified_content
    
    def adapt_to_t0_terminology(self, content):
        """Adapt DVFT terminology to T0 theory framework."""
        adaptations = {
            r'vacuum field\s+𝜙\(𝑥\)': r'T0-Vakuumfeld $\\Phi(x)$ (abgeleitet aus $\\Delta m(x,t)$)',
            r'vacuum amplitude\s+𝜌\(𝑥\)': r'Vakuumamplitude $\\rho(x)$ ($\\propto m(x,t) = 1/T(x,t)$)',
            r'vacuum phase\s+θ\(𝑥\)': r'Vakuumphase $\\theta(x)$ (aus T0-Knoten-Rotation)',
            r'𝜙\(𝑥\)\s*=\s*𝜌\(𝑥\)𝑒\s*𝑖𝜃\(𝑥\)': r'$\\Phi(x) = \\rho(x)e^{i\\theta(x)}$ (T0-abgeleitet)',
            r'DVFT postulates': r'DVFT (als effektive phänomenologische Schicht von T0) postuliert',
            r'(?<!T0-)vacuum': r'T0-Vakuum',
        }
        
        result = content
        for pattern, replacement in adaptations.items():
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        return result
    
    def convert_math_notation(self, content):
        """Convert Unicode math symbols to LaTeX."""
        replacements = {
            '𝜙': r'$\Phi$',
            '𝜌': r'$\rho$',
            'θ': r'$\theta$',
            '∇': r'$\nabla$',
            '∂': r'$\partial$',
            '≈': r'$\approx$',
            '≠': r'$\neq$',
            '≤': r'$\leq$',
            '≥': r'$\geq$',
            '∞': r'$\infty$',
            '±': r'$\pm$',
            '×': r'$\times$',
            '÷': r'$\div$',
            '√': r'$\sqrt$',
            '∫': r'$\int$',
            '∑': r'$\sum$',
            '∏': r'$\prod$',
            '∆': r'$\Delta$',
            'μ': r'$\mu$',
        }
        
        result = content
        for unicode_char, latex_code in replacements.items():
            result = result.replace(unicode_char, latex_code)
        
        return result
    
    def format_content_to_latex(self, content):
        """Format content as LaTeX with proper structure."""
        lines = content.split('\n')
        latex_lines = []
        in_list = False
        list_type = None
        
        for line in lines:
            line_stripped = line.strip()
            
            if not line_stripped:
                if in_list:
                    latex_lines.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                latex_lines.append('')
                continue
            
            # Detect numbered lists
            if re.match(r'^\d+\.\s+', line_stripped):
                if not in_list or list_type != 'enumerate':
                    if in_list:
                        latex_lines.append(f'\\end{{{list_type}}}')
                    latex_lines.append('\\begin{enumerate}')
                    in_list = True
                    list_type = 'enumerate'
                item_text = re.sub(r'^\d+\.\s*', '', line_stripped)
                latex_lines.append(f'  \\item {item_text}')
            # Detect bullet lists
            elif line_stripped.startswith('•') or line_stripped.startswith('-'):
                if not in_list or list_type != 'itemize':
                    if in_list:
                        latex_lines.append(f'\\end{{{list_type}}}')
                    latex_lines.append('\\begin{itemize}')
                    in_list = True
                    list_type = 'itemize'
                item_text = line_stripped[1:].strip()
                latex_lines.append(f'  \\item {item_text}')
            # Section headers
            elif line_stripped.isupper() and len(line_stripped) < 100:
                if in_list:
                    latex_lines.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                latex_lines.append(f'\\subsection{{{line_stripped.title()}}}')
            else:
                if in_list and not line_stripped.startswith(' '):
                    latex_lines.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                latex_lines.append(line_stripped)
        
        if in_list:
            latex_lines.append(f'\\end{{{list_type}}}')
        
        return '\n'.join(latex_lines)
    
    def create_chapter_latex(self, chapter, output_dir):
        """Create a standalone LaTeX document for a chapter."""
        chapter_num = chapter['number']
        chapter_title = chapter['title']
        chapter_content = chapter['content']
        
        # Convert content
        content = self.convert_math_notation(chapter_content)
        content = self.adapt_to_t0_terminology(content)
        content = self.format_content_to_latex(content)
        content = self.add_t0_cross_references(content)
        
        # Generate filename
        chapter_id = f"{chapter_num:02d}"
        safe_title = re.sub(r'[^\w\s-]', '', chapter_title)
        safe_title = re.sub(r'[-\s]+', '_', safe_title)
        filename = f"201_{chapter_id}_DVFT_{safe_title}_De.tex"
        output_path = os.path.join(output_dir, filename)
        
        # Create t0box summary if this is introduction
        t0_note = ''
        if chapter_num == 0:
            t0_note = '''
\\begin{t0box}[T0-Anpassung]
Dieses Dokument präsentiert die Dynamische Vakuum-Feldtheorie (DVFT), vollständig angepasst und integriert in die T0 Zeit-Masse-Dualitätstheorie. Alle DVFT-Konzepte werden aus T0-Prinzipien abgeleitet:
\\begin{itemize}
\\item Vakuumfeld $\\Phi(x)$ $\\rightarrow$ abgeleitet aus T0-Massenschwankungsfeld $\\Delta m(x,t)$
\\item Vakuumamplitude $\\rho(x)$ $\\rightarrow$ entspricht $m(x,t) = 1/T(x,t)$ (T0-Dualität)
\\item Vakuumphase $\\theta(x)$ $\\rightarrow$ aus T0-Knoten-Rotationsdynamik
\\item Fundamentaler Parameter $\\xi = \\frac{4}{3} \\times 10^{-4}$ durchgehend angewendet
\\end{itemize}
Querverweise zu relevanten T0-Dokumenten sind als Fußnoten enthalten.
\\end{t0box}
'''
        
        # Create full document
        latex_doc = f'''\\documentclass[12pt,a4paper]{{article}}

\\input{{{self.preamble_path}}}

\\title{{DVFT Kapitel {chapter_num}: {chapter_title}\\\\
\\large Angepasst an T0 Zeit-Masse-Dualitätstheorie}}

\\author{{Originalkonzept: Satish B. Thorwe\\\\
Angepasst an T0-Theorie: Johann Pascher}}

\\date{{{datetime.now().strftime('%d. %B %Y')}}}

\\begin{{document}}

\\maketitle

\\tableofcontents

\\newpage
{t0_note}

{content}

\\section{{Referenzen zu T0-Dokumenten}}

Dieses Kapitel steht in Zusammenhang mit folgenden T0-Dokumenten im Repository \\texttt{{2/pdf/}}:

\\begin{{itemize}}
  \\item \\texttt{{002\\_T0\\_Grundlagen\\_De.pdf}} -- T0 Zeit-Masse-Dualität Grundlagen
  \\item \\texttt{{004\\_T0\\_Energie\\_De.pdf}} -- T0 Energiefeld-Theorie
  \\item \\texttt{{009\\_T0\\_xi\\_ursprung\\_De.pdf}} -- Ursprung des geometrischen Parameters $\\xi$
  \\item \\texttt{{201\\_DVFT-alles\\_De.pdf}} -- Vollständiges DVFT-Dokument (Rahmenwerk)
\\end{{itemize}}

\\end{{document}}
'''
        
        # Write file
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(latex_doc)
        
        print(f"  Created: {filename}")
        return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Convert DVFT chapters to LaTeX with T0 integration'
    )
    parser.add_argument(
        '--source',
        default='2/tex-n/DVFT.txt',
        help='Source DVFT text file (default: 2/tex-n/DVFT.txt)'
    )
    parser.add_argument(
        '--output-dir',
        default='2/tex-n/de_standalone',
        help='Output directory for LaTeX files (default: 2/tex-n/de_standalone)'
    )
    
    args = parser.parse_args()
    
    # Read source file
    print(f"Reading source file: {args.source}")
    try:
        with open(args.source, 'r', encoding='utf-8') as f:
            dvft_text = f.read()
    except FileNotFoundError:
        print(f"Error: Source file not found: {args.source}")
        return 1
    except Exception as e:
        print(f"Error reading source file: {e}")
        return 1
    
    # Initialize converter
    converter = DVFTChapterConverter()
    
    # Extract chapters
    print("Extracting chapters...")
    chapters = converter.extract_chapters(dvft_text)
    print(f"Found {len(chapters)} chapters")
    
    # Convert each chapter
    print(f"\nConverting chapters to LaTeX...")
    print(f"Output directory: {args.output_dir}\n")
    
    converted_files = []
    for chapter in chapters:
        output_path = converter.create_chapter_latex(chapter, args.output_dir)
        converted_files.append(output_path)
    
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Converted {len(converted_files)} chapter(s) successfully.")
    print(f"\nGenerated files:")
    for filepath in converted_files:
        print(f"  - {os.path.basename(filepath)}")
    
    return 0


if __name__ == '__main__':
    exit(main())
