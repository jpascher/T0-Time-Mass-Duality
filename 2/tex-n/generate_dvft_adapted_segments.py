#!/usr/bin/env python3
"""
DVFT to T0-Adapted LaTeX Converter
Converts DVFT.txt chapters 1-15 into segmented LaTeX documents (4 chapters each)
with T0 Theory adaptations applied.
"""

import re
import os
from typing import List, Dict, Tuple

# T0 Theory adaptation guidelines
T0_ADAPTATIONS = {
    'vacuum_field_mapping': r'''
% T0 Theory Adaptation: Vacuum Field Mapping
% DVFT's complex scalar field $\Phi(x) = \rho(x) e^{i\theta(x)}$ is derived from T0's universal field $\Delta m(x,t)$:
% - Vacuum amplitude: $\rho(x) \propto 1/T(x,t) = m(x,t)$ (enforcing time-mass duality)
% - Vacuum phase: $\theta(x) = \phi_{\text{rotation}}(x,t)$ (node rotation dynamics)
''',
    'xi_parameter': r'''
% T0 Theory Adaptation: Fundamental Scale Parameter
% DVFT parameters are derived from T0's fundamental parameter $\xi = \frac{4}{3} \times 10^{-4}$:
% - Equilibrium amplitude: $\rho_0 = 1/\xi^2 \approx 5.625 \times 10^{7}$
% - Intrinsic frequency: $\mu = \xi m_0$ (where $m_0$ is reference mass from T0)
''',
    'time_mass_duality': r'''
% T0 Theory Adaptation: Time-Mass Duality
% The fundamental constraint $T(x,t) \cdot m(x,t) = 1$ governs all field dynamics.
% DVFT's vacuum pulsation emerges from: $\dot{\theta} = 1/T = m$
''',
    'lagrangian': r'''
% T0 Theory Adaptation: Lagrangian Foundation
% DVFT's action derives from T0's extended Lagrangian:
% $\mathcal{L}_0^{\text{ext}} = -\frac{1}{4} F_{\mu\nu}F^{\mu\nu} + \bar{\psi}(i\gamma^\mu D_\mu - m)\psi + \frac{1}{2}(\partial \Delta m)^2 - \frac{1}{2} m_T^2 (\Delta m)^2 + \xi m_\ell \bar{\psi}_\ell \psi_\ell \Delta m$
'''
}

def read_dvft_source(filename: str) -> List[str]:
    """Read the DVFT.txt source file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()

def extract_chapter_ranges(lines: List[str]) -> List[Tuple[int, str, int, int]]:
    """Extract chapter positions and ranges from the document"""
    chapters = []
    
    for i, line in enumerate(lines):
        if line.strip().startswith('CHAPTER '):
            # Extract chapter number
            match = re.match(r'CHAPTER (\d+):', line.strip())
            if match:
                chapter_num = int(match.group(1))
                chapters.append((i, line.strip(), chapter_num))
    
    # Add ranges
    chapter_ranges = []
    for i in range(len(chapters)):
        start_line = chapters[i][0]
        end_line = chapters[i+1][0] if i < len(chapters) - 1 else len(lines)
        chapter_ranges.append((
            chapters[i][2],  # chapter number
            chapters[i][1],  # chapter title
            start_line,
            end_line
        ))
    
    return chapter_ranges

def convert_math_to_latex(text: str) -> str:
    """Convert mathematical notation to LaTeX format"""
    # Handle special Unicode equation characters first
    text = text.replace('𝜙', '\\phi')
    text = text.replace('𝑥', 'x')
    text = text.replace('𝜌', '\\rho')
    text = text.replace('𝜃', '\\theta')
    text = text.replace('𝑖', 'i')
    text = text.replace('𝑒', 'e')
    text = text.replace('𝑡', 't')
    
    # Greek letters (standard Unicode)
    replacements = {
        'Φ': r'\Phi',
        'φ': r'\phi',
        'ρ': r'\rho',
        'θ': r'\theta',
        'μ': r'\mu',
        '∇': r'\nabla',
        '∂': r'\partial',
        '≈': r'\approx',
        '≥': r'\geq',
        '≤': r'\leq',
        '→': r'\rightarrow',
        '×': r'\times',
        '±': r'\pm',
        '∓': r'\mp',
        '∞': r'\infty',
        'α': r'\alpha',
        'β': r'\beta',
        'γ': r'\gamma',
        'δ': r'\delta',
        'ε': r'\epsilon',
        'λ': r'\lambda',
        'π': r'\pi',
        'σ': r'\sigma',
        'τ': r'\tau',
        'ω': r'\omega',
        'Ω': r'\Omega',
        'Δ': r'\Delta',
        'Λ': r'\Lambda',
        'Σ': r'\Sigma',
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    # Handle subscripts
    text = re.sub(r'(\w)₀', r'\1_0', text)
    text = re.sub(r'(\w)₁', r'\1_1', text)
    text = re.sub(r'(\w)₂', r'\1_2', text)
    text = re.sub(r'(\w)₃', r'\1_3', text)
    
    # Handle superscripts
    text = text.replace('²', '^2')
    text = text.replace('³', '^3')
    
    # Fix exponential notation: e followed by superscript or i*something
    # Pattern: e^{...} or e^i*theta
    text = re.sub(r'e\s*\^?\s*\{?\s*i\s*\\theta\s*\}?', r'e^{i\\theta}', text)
    text = re.sub(r'e\s*-?\s*i\s*\\mu\s*t', r'e^{-i\\mu t}', text)
    
    # Detect and wrap standalone equations
    stripped = text.strip()
    # Check if line contains equation-like content
    if ('=' in stripped) and len(stripped) < 150:
        # Check if it contains math symbols
        has_math = any(s in stripped for s in ['\\', '_', '^', '\\rho', '\\theta', '\\phi', '\\mu', '\\Phi'])
        # Check if it's not already in display math mode
        not_in_math = not (stripped.startswith('\\[') or stripped.startswith('$$') or 
                          stripped.startswith('\\begin{equation'))
        # Check if it's not a paragraph of text
        word_count = len(stripped.split())
        is_short = word_count < 15
        
        if has_math and not_in_math and is_short:
            return '\\[' + stripped + '\\]\n'
    
    return text

def wrap_inline_math(text: str) -> str:
    """Wrap inline math expressions in $ delimiters"""
    # Wrap Greek letters and math symbols that aren't already in math mode
    # Pattern: backslash command not already in $ or \[ \]
    
    # Split by existing math delimiters to avoid double-wrapping
    parts = re.split(r'(\$[^$]+\$|\\\[[^\]]+\\\])', text)
    
    result = []
    for i, part in enumerate(parts):
        # Skip parts that are already math
        if part.startswith('$') or part.startswith('\\['):
            result.append(part)
        else:
            # Wrap individual LaTeX commands with $
            part = re.sub(r'(\\(?:phi|rho|theta|mu|Phi|nabla|partial|alpha|beta|gamma|delta|epsilon|lambda|pi|sigma|tau|omega|Omega|Delta|Lambda|Sigma|times|approx|geq|leq|rightarrow|infty)(?:_\{?\w+\}?)?)', r'$\1$', part)
            # Clean up double dollars
            part = re.sub(r'\$\$+', r'$', part)
            # Remove empty math
            part = re.sub(r'\$\s*\$', r'', part)
            result.append(part)
    
    return ''.join(result)

def convert_text_formatting(text: str) -> str:
    """Convert text formatting to LaTeX"""
    # Apply inline math wrapping
    text = wrap_inline_math(text)
    return text

def parse_chapter_content(lines: List[str], start: int, end: int) -> str:
    """Parse and convert chapter content to LaTeX"""
    content = []
    in_itemize = False
    in_enumerate = False
    i = start + 1  # Skip chapter title line
    
    while i < end:
        line = lines[i]
        
        # Skip empty lines at the start
        if not content and not line.strip():
            i += 1
            continue
        
        # Handle numbered lists (subsections)
        if re.match(r'^(\d+)\.\s+(.+)$', line.strip()):
            # Close any open lists
            if in_itemize:
                content.append('\\end{itemize}\n')
                in_itemize = False
            if in_enumerate:
                content.append('\\end{enumerate}\n')
                in_enumerate = False
            
            match = re.match(r'^(\d+)\.\s+(.+)$', line.strip())
            title = match.group(2)
            content.append(f'\\subsection{{{title}}}\n')
            i += 1
            continue
        
        # Handle bullet points
        if line.strip().startswith('•'):
            if not in_itemize:
                content.append('\\begin{itemize}\n')
                in_itemize = True
            item_text = line.strip()[1:].strip()
            item_text = convert_math_to_latex(item_text)
            item_text = convert_text_formatting(item_text)
            content.append(f'  \\item {item_text}\n')
            i += 1
            continue
        
        # Close itemize if we're no longer in bullet points
        if in_itemize and line.strip() and not line.strip().startswith('•'):
            content.append('\\end{itemize}\n')
            in_itemize = False
        
        # Handle multi-line equations (e.g., phi(x) = rho(x)e^{i*theta(x)})
        # Check if this looks like the start of an equation
        stripped = line.strip()
        if any(char in stripped for char in ['𝜙', '𝜌', '𝜃', 'φ', 'ρ', 'θ', 'Φ']) and '=' in stripped:
            # Collect the full equation across multiple lines
            equation_lines = [line]
            j = i + 1
            # Look ahead for continuation (usually mathematical symbols on next lines)
            while j < end and j < i + 5:  # Limit lookahead
                next_line = lines[j].strip()
                # Check if it looks like a continuation
                if next_line and not next_line.startswith('Where') and \
                   any(char in next_line for char in ['𝑖', '𝜃', '𝜌', '𝜙', 'i', 'θ', 'ρ', 'φ', '^', '_']) and \
                   len(next_line) < 30:
                    equation_lines.append(lines[j])
                    j += 1
                else:
                    break
            
            # Combine and format the equation
            full_equation = ''.join(line.strip() for line in equation_lines)
            full_equation = convert_math_to_latex(full_equation)
            # If not already wrapped, wrap it
            if not full_equation.startswith('\\['):
                content.append(f'\\[{full_equation}\\]\n')
            else:
                content.append(full_equation + '\n')
            
            i = j
            continue
        
        # Convert math and add line
        line = convert_math_to_latex(line)
        line = convert_text_formatting(line)
        content.append(line)
        i += 1
    
    # Close any open environments
    if in_itemize:
        content.append('\\end{itemize}\n')
    if in_enumerate:
        content.append('\\end{enumerate}\n')
    
    return ''.join(content)

def generate_segment_preamble(segment_num: int, chapter_start: int, chapter_end: int) -> str:
    """Generate LaTeX preamble for a segment document"""
    return f'''\\documentclass[12pt,a4paper]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage[english]{{babel}}
\\usepackage{{amsmath,amsfonts,amssymb}}
\\usepackage{{physics}}
\\usepackage{{geometry}}
\\usepackage{{hyperref}}
\\usepackage{{fancyhdr}}
\\usepackage{{graphicx}}
\\usepackage{{cite}}
\\usepackage{{tcolorbox}}
\\usepackage{{enumitem}}

\\geometry{{margin=1in}}
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[L]{{Dynamic Vacuum Field Theory}}
\\fancyhead[R]{{Adapted to T0 Theory}}
\\fancyfoot[C]{{\\thepage}}

\\title{{Dynamic Vacuum Field Theory Adapted to T0 Theory\\\\
\\large Chapters {chapter_start}--{chapter_end}}}
\\author{{Based on work by Satish B. Thorwe\\\\
Adapted to T0 Theory Framework}}
\\date{{December 25, 2025}}

\\begin{{document}}

\\maketitle

\\begin{{tcolorbox}}[colback=blue!5!white,colframe=blue!75!black,title=T0 Theory Framework]
This document presents Dynamic Vacuum Field Theory (DVFT) adapted to align with T0 Theory as its fundamental basis. T0 Theory provides the conclusive core framework with:
\\begin{{itemize}}
\\item Time-mass duality: $T(x,t) \\cdot m(x,t) = 1$
\\item Fundamental parameter: $\\xi = \\frac{{4}}{{3}} \\times 10^{{-4}}$
\\item Simplified Lagrangian: $\\mathcal{{L}} = \\varepsilon (\\partial \\Delta m)^2$
\\item Extended Lagrangian including time-field interactions
\\item Node dynamics for particles and spin
\\end{{itemize}}

DVFT is reformulated as a phenomenological layer on T0, deriving its vacuum field $\\Phi = \\rho e^{{i\\theta}}$ directly from T0 principles.
\\end{{tcolorbox}}

\\tableofcontents
\\newpage

'''

def generate_segment_footer() -> str:
    """Generate LaTeX footer for a segment document"""
    return '''
\\section*{References and Notes}

This document is part of the DVFT-T0 integration project. For complete details on T0 Theory, refer to the main T0 documentation. DVFT content is based on the work by Satish B. Thorwe, adapted to align with T0 Theory framework.

\\subsection*{Key Adaptations}
\\begin{enumerate}
\\item DVFT's vacuum field $\\Phi(x) = \\rho(x) e^{i\\theta(x)}$ is derived from T0's $\\Delta m(x,t)$
\\item All DVFT parameters are expressed in terms of T0's $\\xi$
\\item Vacuum dynamics emerge from T0's time-mass duality
\\item Field equations are grounded in T0's extended Lagrangian
\\end{enumerate}

\\end{document}
'''

def insert_t0_adaptation_note(chapter_num: int) -> str:
    """Insert T0 adaptation note at the beginning of specific chapters"""
    notes = {
        1: T0_ADAPTATIONS['vacuum_field_mapping'],
        2: T0_ADAPTATIONS['xi_parameter'],
        3: T0_ADAPTATIONS['lagrangian'],
        4: T0_ADAPTATIONS['time_mass_duality'],
    }
    
    if chapter_num in notes:
        return f'''
\\begin{{tcolorbox}}[colback=green!5!white,colframe=green!50!black,title=T0 Adaptation Note]
{notes[chapter_num]}
\\end{{tcolorbox}}

'''
    return ''

def generate_segment(lines: List[str], chapters: List[Tuple[int, str, int, int]], 
                    segment_start: int, segment_end: int, output_file: str):
    """Generate a segment document containing 4 chapters"""
    
    segment_chapters = [ch for ch in chapters if segment_start <= ch[0] <= segment_end]
    
    if not segment_chapters:
        print(f"No chapters found for segment {segment_start}-{segment_end}")
        return
    
    # Generate document
    latex_content = generate_segment_preamble(
        (segment_start - 1) // 4 + 1,
        segment_start,
        segment_end
    )
    
    for chapter_num, chapter_title, start_line, end_line in segment_chapters:
        # Extract chapter title
        title = chapter_title.replace(f'CHAPTER {chapter_num}:', '').strip()
        
        # Add chapter section
        latex_content += f'\\section{{{title}}}\n'
        latex_content += f'\\label{{sec:ch{chapter_num:02d}}}\n\n'
        
        # Add T0 adaptation note for key chapters
        latex_content += insert_t0_adaptation_note(chapter_num)
        
        # Parse and add chapter content
        chapter_content = parse_chapter_content(lines, start_line, end_line)
        latex_content += chapter_content
        latex_content += '\n\\newpage\n\n'
    
    # Add footer
    latex_content += generate_segment_footer()
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print(f"✓ Generated {output_file}")
    print(f"  Chapters: {[ch[0] for ch in segment_chapters]}")

def main():
    """Main conversion function"""
    print("=" * 70)
    print("DVFT to T0-Adapted LaTeX Converter")
    print("=" * 70)
    print()
    
    # File paths
    base_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n'
    source_file = os.path.join(base_dir, 'DVFT.txt')
    
    # Read source
    print("Reading DVFT.txt...")
    lines = read_dvft_source(source_file)
    print(f"✓ Read {len(lines)} lines")
    
    # Extract chapters
    print("\nExtracting chapter information...")
    chapters = extract_chapter_ranges(lines)
    print(f"✓ Found {len(chapters)} chapters")
    
    # Filter to chapters 1-15
    chapters_1_15 = [ch for ch in chapters if 1 <= ch[0] <= 15]
    print(f"✓ Focusing on chapters 1-15 ({len(chapters_1_15)} chapters)")
    
    print("\nChapters to convert:")
    for ch_num, ch_title, _, _ in chapters_1_15:
        print(f"  {ch_num:2d}. {ch_title}")
    
    # Generate segments
    print("\n" + "=" * 70)
    print("Generating segmented LaTeX documents")
    print("=" * 70)
    
    segments = [
        (1, 4, 'DVFT_Chapters_01-04_En.tex'),
        (5, 8, 'DVFT_Chapters_05-08_En.tex'),
        (9, 12, 'DVFT_Chapters_09-12_En.tex'),
        (13, 15, 'DVFT_Chapters_13-15_En.tex'),
    ]
    
    for start, end, filename in segments:
        print(f"\nGenerating segment: Chapters {start}-{end}")
        output_path = os.path.join(base_dir, filename)
        generate_segment(lines, chapters_1_15, start, end, output_path)
    
    print("\n" + "=" * 70)
    print("✓ Conversion complete!")
    print("=" * 70)
    print("\nGenerated files:")
    for _, _, filename in segments:
        print(f"  - {filename}")
    
    print("\nNext steps:")
    print("  1. Review generated LaTeX files")
    print("  2. Test compilation with: pdflatex <filename>")
    print("  3. Commit each file separately")

if __name__ == '__main__':
    main()
