#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
DVFT Markdown to LaTeX Converter
=================================

Converts DVFT chapter markdown files to LaTeX format with:
- Markdown headers to \section{}
- Unicode math symbols to LaTeX commands
- Physics package integration
- T0_preamble_shared_De.tex header

Author: Generated for T0 Theory Project
Date: 2025-12-28
"""

import os
import re
from pathlib import Path


# Mapping of Unicode symbols to LaTeX commands
UNICODE_TO_LATEX = {
    '𝜙': r'\varphi',
    'Φ': r'\Phi',
    '𝜌': r'\rho',
    'ρ': r'\rho',
    'θ': r'\theta',
    'Θ': r'\Theta',
    '𝜃': r'\theta',
    'μ': r'\mu',
    '𝜇': r'\mu',
    'ξ': r'\xi',
    'α': r'\alpha',
    '𝛼': r'\alpha',  # Mathematical italic alpha
    'β': r'\beta',
    '𝛽': r'\beta',  # Mathematical italic beta
    'γ': r'\gamma',
    '𝛾': r'\gamma',  # Mathematical italic gamma
    'δ': r'\delta',
    '𝛿': r'\delta',  # Mathematical italic delta
    'ε': r'\varepsilon',
    '𝜀': r'\varepsilon',  # Mathematical italic epsilon
    'ζ': r'\zeta',
    '𝜁': r'\zeta',  # Mathematical italic zeta
    'η': r'\eta',
    '𝜂': r'\eta',  # Mathematical italic eta
    'λ': r'\lambda',
    '𝜆': r'\lambda',  # Mathematical italic lambda
    'ν': r'\nu',
    '𝜈': r'\nu',  # Mathematical italic nu
    'π': r'\pi',
    '𝜋': r'\pi',  # Mathematical italic pi
    'σ': r'\sigma',
    '𝜎': r'\sigma',  # Mathematical italic sigma
    'τ': r'\tau',
    '𝜏': r'\tau',  # Mathematical italic tau
    'ω': r'\omega',
    '𝜔': r'\omega',  # Mathematical italic omega
    'Ω': r'\Omega',
    '∇': r'\nabla',
    '∂': r'\partial',
    '∫': r'\int',
    '≈': r'\approx',
    '≠': r'\neq',
    '≤': r'\leq',
    '≥': r'\geq',
    '×': r'\times',
    '÷': r'\div',
    '±': r'\pm',
    '∓': r'\mp',
    '∞': r'\infty',
    '√': r'\sqrt',
    '∑': r'\sum',
    '∏': r'\prod',
    '⊕': r'\oplus',
    '⊗': r'\otimes',
    '∈': r'\in',
    '∉': r'\notin',
    '⊂': r'\subset',
    '⊃': r'\supset',
    '∪': r'\cup',
    '∩': r'\cap',
    '→': r'\to',
    '←': r'\leftarrow',
    '↔': r'\leftrightarrow',
    '⇒': r'\Rightarrow',
    '⇐': r'\Leftarrow',
    '⇔': r'\Leftrightarrow',
    '∀': r'\forall',
    '∃': r'\exists',
    '¬': r'\neg',
    '∧': r'\land',
    '∨': r'\lor',
    'ħ': r'\hbar',
    '℘': r'\wp',
    'ℏ': r'\hbar',
    '°': r'^\circ',
    '·': r'\cdot',
    '▫': r'\Box',
    # Mathematical italic characters (Unicode Mathematical Alphanumeric Symbols)
    '𝐴': r'A',
    '𝐵': r'B',
    '𝐶': r'C',
    '𝐷': r'D',
    '𝐸': r'E',
    '𝐹': r'F',
    '𝐺': r'G',
    '𝐻': r'H',
    '𝐼': r'I',
    '𝐽': r'J',
    '𝐾': r'K',
    '𝐿': r'L',
    '𝑀': r'M',
    '𝑁': r'N',
    '𝑂': r'O',
    '𝑃': r'P',
    '𝑄': r'Q',
    '𝑅': r'R',
    '𝑆': r'S',
    '𝑇': r'T',
    '𝑈': r'U',
    '𝑉': r'V',
    '𝑊': r'W',
    '𝑋': r'X',
    '𝑌': r'Y',
    '𝑍': r'Z',
    '𝑎': r'a',
    '𝑏': r'b',
    '𝑐': r'c',
    '𝑑': r'd',
    '𝑒': r'e',
    '𝑓': r'f',
    '𝑔': r'g',
    '𝘩': r'h',
    '𝑖': r'i',
    '𝑗': r'j',
    '𝑘': r'k',
    '𝑙': r'l',
    '𝑚': r'm',
    '𝑛': r'n',
    '𝑜': r'o',
    '𝑝': r'p',
    '𝑞': r'q',
    '𝑟': r'r',
    '𝑠': r's',
    '𝑡': r't',
    '𝑢': r'u',
    '𝑣': r'v',
    '𝑤': r'w',
    '𝑥': r'x',
    '𝑦': r'y',
    '𝑧': r'z',
    # Subscripts
    '₀': r'_0',
    '₁': r'_1',
    '₂': r'_2',
    '₃': r'_3',
    '₄': r'_4',
    '₅': r'_5',
    '₆': r'_6',
    '₇': r'_7',
    '₈': r'_8',
    '₉': r'_9',
    # Superscripts
    '⁰': r'^0',
    '¹': r'^1',
    '²': r'^2',
    '³': r'^3',
    '⁴': r'^4',
    '⁵': r'^5',
    '⁶': r'^6',
    '⁷': r'^7',
    '⁸': r'^8',
    '⁹': r'^9',
}


def replace_unicode_symbols(text):
    """Replace Unicode mathematical symbols with LaTeX commands."""
    for unicode_char, latex_cmd in UNICODE_TO_LATEX.items():
        # Simple string replacement - escape the replacement string
        text = text.replace(unicode_char, latex_cmd)
    return text


def convert_headers_to_sections(text):
    """Convert Markdown headers to LaTeX sections."""
    lines = text.split('\n')
    result = []
    
    for line in lines:
        # Skip the first header (chapter title) as it will be used as document title
        if line.startswith('# '):
            # This is the main chapter title - skip it as we handle it separately
            continue
        elif line.startswith('## '):
            # Convert ## to \section{}
            title = line[3:].strip()
            result.append(f'\\section{{{title}}}')
        elif line.startswith('### '):
            # Convert ### to \subsection{}
            title = line[4:].strip()
            result.append(f'\\subsection{{{title}}}')
        elif line.startswith('#### '):
            # Convert #### to \subsubsection{}
            title = line[5:].strip()
            result.append(f'\\subsubsection{{{title}}}')
        else:
            result.append(line)
    
    return '\n'.join(result)


def escape_latex_special_chars(text):
    """Escape special LaTeX characters, but preserve math mode and commands."""
    # Don't escape characters that are already part of LaTeX commands
    # This is a simplified approach - we preserve backslashes
    
    # Protect existing LaTeX commands temporarily
    latex_commands = re.findall(r'\\[a-zA-Z]+(?:\{[^}]*\})?', text)
    placeholders = []
    for i, cmd in enumerate(latex_commands):
        placeholder = f'<<<LATEXCMD{i}>>>'
        placeholders.append((placeholder, cmd))
        text = text.replace(cmd, placeholder, 1)
    
    # Now escape special characters (but not backslash)
    # We'll be conservative and only escape the most common problematic ones
    replacements = {
        '%': r'\%',
        '&': r'\&',
        '#': r'\#',
        '$': r'\$',
        '_': r'\_',
    }
    
    for char, escaped in replacements.items():
        text = text.replace(char, escaped)
    
    # Restore LaTeX commands
    for placeholder, cmd in placeholders:
        text = text.replace(placeholder, cmd)
    
    return text


def process_math_expressions(text):
    """Process mathematical expressions and ensure they're properly formatted."""
    # Handle inline equations (text with = signs that look like equations)
    # This is a heuristic approach - we'll be more conservative now
    
    # Handle superscripts (but only the standalone ones that weren't already converted)
    # The subscripts and superscripts in UNICODE_TO_LATEX will already be handled
    
    return text


def convert_markdown_to_latex(md_content, chapter_number, chapter_title):
    """Convert a markdown chapter to LaTeX format."""
    
    # Extract the title from the first line if it's a header
    lines = md_content.strip().split('\n')
    if lines[0].startswith('# '):
        # Remove the title line
        md_content = '\n'.join(lines[1:])
    
    # Convert headers to sections
    content = convert_headers_to_sections(md_content)
    
    # Replace Unicode symbols
    content = replace_unicode_symbols(content)
    
    # Process math expressions
    content = process_math_expressions(content)
    
    # Escape special characters (done last to not interfere with our replacements)
    # Actually, we'll skip this for now as it might break the Unicode replacements
    # content = escape_latex_special_chars(content)
    
    # Create the LaTeX document
    latex_doc = f"""% DVFT Chapter {chapter_number}: {chapter_title}
% Generated from Markdown
% Date: 2025-12-28

\\documentclass[12pt,a4paper]{{article}}

% Include the shared T0 preamble
\\input{{../../../T0_preamble_shared_De.tex}}

\\begin{{document}}

\\title{{{chapter_title}}}
\\author{{Dynamic Vacuum Field Theory}}
\\date{{2025}}
\\maketitle

{content}

\\end{{document}}
"""
    
    return latex_doc


def process_all_chapters(input_dir, output_dir):
    """Process all markdown chapters and convert them to LaTeX."""
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get all markdown files
    md_files = sorted(input_path.glob('*.md'))
    
    chapter_files = []
    
    for md_file in md_files:
        # Read the markdown content
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Extract chapter number from filename
        filename = md_file.stem
        if filename.startswith('00_'):
            chapter_num = '00'
            chapter_name = 'Vorspann'
        else:
            # Extract number from "Kapitel_XX"
            match = re.match(r'Kapitel_(\d+)', filename)
            if match:
                chapter_num = match.group(1)
                chapter_name = f'Kapitel {int(chapter_num)}'
            else:
                continue
        
        # Extract title from first line
        lines = md_content.split('\n')
        title = chapter_name
        if lines[0].startswith('# '):
            title = lines[0][2:].strip()
        
        # Convert to LaTeX
        latex_content = convert_markdown_to_latex(md_content, chapter_num, title)
        
        # Write to output file
        output_file = output_path / f'kapitel_{chapter_num}.tex'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        chapter_files.append((chapter_num, output_file.name, title))
        print(f"✓ Converted {md_file.name} → {output_file.name}")
    
    return chapter_files


def create_main_tex(output_dir, chapter_files):
    """Create a main.tex file that includes all chapters."""
    
    output_path = Path(output_dir)
    
    # Sort chapter files by number
    chapter_files.sort(key=lambda x: int(x[0]))
    
    # Create the main.tex content
    main_content = """% DVFT Complete Document - Main File
% Generated automatically
% Date: 2025-12-28

\\documentclass[12pt,a4paper]{book}

% Include the shared T0 preamble
\\input{../../../T0_preamble_shared_De.tex}

\\begin{document}

% Title page
\\title{Dynamic Vacuum Field Theory\\\\Complete Documentation}
\\author{Satish B. Thorwe}
\\date{2025}
\\maketitle

% Table of contents
\\tableofcontents
\\newpage

"""
    
    # Add input statements for each chapter
    for chapter_num, filename, title in chapter_files:
        # For the book class, we use \chapter instead of including full documents
        # We'll need to extract just the content part from each file
        # For now, let's just comment them as standalone files
        main_content += f"% Chapter {chapter_num}: {title}\n"
        main_content += f"% Standalone file: {filename}\n\n"
    
    main_content += """
% Note: This main.tex is a placeholder.
% Each chapter is designed as a standalone document.
% To create a combined document, the chapter files would need to be
% modified to remove \\documentclass, \\begin{document}, etc.
% and use only the content section.

\\end{document}
"""
    
    # Write main.tex
    main_file = output_path / 'main.tex'
    with open(main_file, 'w', encoding='utf-8') as f:
        f.write(main_content)
    
    print(f"\n✓ Created main.tex")
    
    # Also create a content-only version of each chapter for inclusion
    print("\nCreating content-only versions for inclusion...")
    
    content_dir = output_path / 'content_only'
    content_dir.mkdir(exist_ok=True)
    
    for chapter_num, filename, title in chapter_files:
        source_file = output_path / filename
        content_file = content_dir / filename
        
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract only the content between \begin{document} and \end{document}
        match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
        if match:
            body_content = match.group(1).strip()
            
            # Remove \maketitle and similar commands
            body_content = re.sub(r'\\title\{.*?\}', '', body_content)
            body_content = re.sub(r'\\author\{.*?\}', '', body_content)
            body_content = re.sub(r'\\date\{.*?\}', '', body_content)
            body_content = re.sub(r'\\maketitle', '', body_content)
            
            # Add chapter heading
            chapter_content = f"\\chapter{{{title}}}\n\\label{{chap:{chapter_num}}}\n\n{body_content}"
            
            with open(content_file, 'w', encoding='utf-8') as f:
                f.write(chapter_content)
    
    # Create an updated main.tex that includes the content-only versions
    main_content_complete = """% DVFT Complete Document - Main File with All Chapters
% Generated automatically
% Date: 2025-12-28

\\documentclass[12pt,a4paper]{book}

% Include the shared T0 preamble
\\input{../../../T0_preamble_shared_De.tex}

\\begin{document}

% Title page
\\title{Dynamic Vacuum Field Theory\\\\Complete Documentation}
\\author{Satish B. Thorwe}
\\date{2025}
\\maketitle

% Table of contents
\\tableofcontents
\\cleardoublepage

"""
    
    # Add input statements for each chapter
    for chapter_num, filename, title in chapter_files:
        main_content_complete += f"\\input{{content_only/{filename}}}\n"
        main_content_complete += f"\\cleardoublepage\n\n"
    
    main_content_complete += """
\\end{document}
"""
    
    # Write main_complete.tex
    main_complete_file = output_path / 'main_complete.tex'
    with open(main_complete_file, 'w', encoding='utf-8') as f:
        f.write(main_content_complete)
    
    print(f"✓ Created main_complete.tex with all chapters included")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Convert DVFT Markdown chapters to LaTeX'
    )
    parser.add_argument(
        '--input-dir',
        default='/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_standalone/md_chapters_dvft',
        help='Input directory containing markdown files'
    )
    parser.add_argument(
        '--output-dir',
        default='/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_standalone/dvft_latex_chapters',
        help='Output directory for LaTeX files'
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("DVFT Markdown to LaTeX Converter")
    print("=" * 60)
    print(f"\nInput directory:  {args.input_dir}")
    print(f"Output directory: {args.output_dir}")
    print()
    
    # Process all chapters
    chapter_files = process_all_chapters(args.input_dir, args.output_dir)
    
    # Create main.tex
    create_main_tex(args.output_dir, chapter_files)
    
    print("\n" + "=" * 60)
    print(f"✓ Conversion complete! {len(chapter_files)} chapters processed.")
    print("=" * 60)


if __name__ == '__main__':
    main()
