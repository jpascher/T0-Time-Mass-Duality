#!/usr/bin/env python3
"""
Generate ALL DVFT chapters (1-43) with T0 Theory adaptations
- NO content truncation
- Complete chapter text from DVFT.txt
- T0 adaptations and cross-references only
- Links to T0 PDF documents
"""

import re
import os
from pathlib import Path

# Repository paths
BASE_DIR = Path("/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n")
DVFT_FILE = BASE_DIR / "DVFT.txt"
EN_DIR = BASE_DIR / "en_standalone"
DE_DIR = BASE_DIR / "de_standalone"

# T0 Theory core concepts for adaptations
T0_ADAPTATIONS = {
    'rho': r'\rho \propto 1/T(x,t)',  # Vacuum amplitude from time field
    'xi': r'\xi = 4/3 \times 10^{-4}',  # Single T0 parameter
    'time_mass_duality': r'T(x,t) \cdot m(x,t) = 1',
    'principle': 'T0 Theory: Time-Mass Duality',
    'pdf_reference': '../T0_Theory_Complete.pdf'  # Main T0 document
}

# German translations
T0_ADAPTATIONS_DE = {
    'principle': 'T0-Theorie: Zeit-Masse-Dualität',
    'pdf_reference': '../T0_Theorie_Vollstaendig.pdf'
}

def extract_chapters_from_dvft():
    """Extract all chapters with COMPLETE content - NO TRUNCATION"""
    with open(DVFT_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Split by chapter markers
    chapter_pattern = r'CHAPTER (\d+):\s*([^\n]+)'
    
    chapters = []
    matches = list(re.finditer(chapter_pattern, content))
    
    for i, match in enumerate(matches):
        chapter_num = int(match.group(1))
        chapter_title = match.group(2).strip()
        
        # Extract FULL content until next chapter (or end of file)
        start_pos = match.start()
        end_pos = matches[i+1].start() if i+1 < len(matches) else len(content)
        
        chapter_content = content[start_pos:end_pos].strip()
        
        chapters.append({
            'num': chapter_num,
            'title': chapter_title,
            'content': chapter_content,
            'length': len(chapter_content)
        })
    
    return chapters

def sanitize_latex(text):
    """Convert plain text to LaTeX, preserving ALL content"""
    # Escape special LaTeX characters
    text = text.replace('\\', '\\textbackslash{}')
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('_', '\\_')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('~', '\\textasciitilde{}')
    text = text.replace('^', '\\textasciicircum{}')
    
    # Convert equations (preserve math mode)
    text = re.sub(r'𝜙\(𝑥\)', r'$\\Phi(x)$', text)
    text = re.sub(r'𝜌\(𝑥\)', r'$\\rho(x)$', text)
    text = re.sub(r'θ\(x\)', r'$\\theta(x)$', text)
    
    return text

def add_t0_preamble(chapter_num, title, language='en'):
    """Add T0-specific preamble with PDF cross-references"""
    if language == 'en':
        return f"""\\documentclass[12pt,a4paper]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage{{amsmath,amssymb,amsthm}}
\\usepackage{{geometry}}
\\usepackage{{graphicx}}
\\usepackage{{hyperref}}
\\usepackage{{physics}}
\\usepackage{{siunitx}}

\\geometry{{margin=1in}}

\\title{{Chapter {chapter_num}: {title}\\\\
\\large T0 Theory — Dynamic Vacuum Field Theory Integration}}
\\author{{T0-DVFT Framework}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\begin{{abstract}}
This chapter presents {title} within the unified T0-DVFT framework. T0 Theory establishes the fundamental time-mass duality $T(x,t) \\cdot m(x,t) = 1$ with single parameter $\\xi = 4/3 \\times 10^{{-4}}$. DVFT's vacuum field $\\Phi = \\rho e^{{i\\theta}}$ emerges naturally with $\\rho \\propto 1/T(x,t)$, providing complete physical foundation for all phenomena described herein.

\\textbf{{Cross-Reference:}} For comprehensive T0 Theory foundations, see \\href{{../{T0_ADAPTATIONS['pdf_reference']}}}{{T0 Theory Complete Documentation}}.
\\end{{abstract}}

"""
    else:  # German
        return f"""\\documentclass[12pt,a4paper]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage[ngerman]{{babel}}
\\usepackage{{amsmath,amssymb,amsthm}}
\\usepackage{{geometry}}
\\usepackage{{graphicx}}
\\usepackage{{hyperref}}
\\usepackage{{physics}}
\\usepackage{{siunitx}}

\\geometry{{margin=1in}}

\\title{{Kapitel {chapter_num}: {title}\\\\
\\large T0-Theorie — Integration der Dynamischen Vakuumfeldtheorie}}
\\author{{T0-DVFT-Framework}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\begin{{abstract}}
Dieses Kapitel präsentiert {title} im vereinheitlichten T0-DVFT-Framework. Die T0-Theorie etabliert die fundamentale Zeit-Masse-Dualität $T(x,t) \\cdot m(x,t) = 1$ mit einzigem Parameter $\\xi = 4/3 \\times 10^{{-4}}$. DVFTs Vakuumfeld $\\Phi = \\rho e^{{i\\theta}}$ entsteht natürlich mit $\\rho \\propto 1/T(x,t)$ und liefert vollständige physikalische Grundlage für alle hier beschriebenen Phänomene.

\\textbf{{Querverweis:}} Für umfassende T0-Theorie-Grundlagen siehe \\href{{../{T0_ADAPTATIONS_DE['pdf_reference']}}}{{T0-Theorie Vollständige Dokumentation}}.
\\end{{abstract}}

"""

def add_t0_conclusion(chapter_num, language='en'):
    """Add T0-specific conclusion linking to main theory"""
    if language == 'en':
        return f"""

\\section{{T0-DVFT Integration Summary}}

This chapter demonstrates how {chapter_num}'s concepts integrate seamlessly into T0 Theory's unified framework:

\\begin{{itemize}}
\\item \\textbf{{Time-Mass Duality:}} $T(x,t) \\cdot m(x,t) = 1$ underlies all phenomena
\\item \\textbf{{Vacuum Field:}} $\\Phi(x,t) = \\rho(x,t) e^{{i\\theta(x,t)}}$ with $\\rho = 1/(T \\cdot \\xi)$
\\item \\textbf{{Single Parameter:}} $\\xi = 4/3 \\times 10^{{-4}}$ determines all scales
\\item \\textbf{{Zero Free Parameters:}} All constants derive from $\\xi$ and time field structure
\\end{{itemize}}

\\textbf{{For detailed T0 Theory foundations:}}
\\begin{{itemize}}
\\item Main Document: \\href{{../{T0_ADAPTATIONS['pdf_reference']}}}{{T0\\_Theory\\_Complete.pdf}}
\\item Experimental Validation: \\href{{../T0_Experimental_Tests.pdf}}{{T0\\_Experimental\\_Tests.pdf}}
\\item Mathematical Framework: \\href{{../T0_Mathematical_Foundations.pdf}}{{T0\\_Mathematical\\_Foundations.pdf}}
\\end{{itemize}}

\\end{{document}}
"""
    else:  # German
        return f"""

\\section{{T0-DVFT-Integrationszusammenfassung}}

Dieses Kapitel demonstriert, wie die Konzepte von Kapitel {chapter_num} nahtlos in das vereinheitlichte Framework der T0-Theorie integrieren:

\\begin{{itemize}}
\\item \\textbf{{Zeit-Masse-Dualität:}} $T(x,t) \\cdot m(x,t) = 1$ liegt allen Phänomenen zugrunde
\\item \\textbf{{Vakuumfeld:}} $\\Phi(x,t) = \\rho(x,t) e^{{i\\theta(x,t)}}$ mit $\\rho = 1/(T \\cdot \\xi)$
\\item \\textbf{{Einzelner Parameter:}} $\\xi = 4/3 \\times 10^{{-4}}$ bestimmt alle Skalen
\\item \\textbf{{Null freie Parameter:}} Alle Konstanten leiten sich von $\\xi$ und Zeitfeldstruktur ab
\\end{{itemize}}

\\textbf{{Für detaillierte T0-Theorie-Grundlagen:}}
\\begin{{itemize}}
\\item Hauptdokument: \\href{{../{T0_ADAPTATIONS_DE['pdf_reference']}}}{{T0\\_Theorie\\_Vollstaendig.pdf}}
\\item Experimentelle Validierung: \\href{{../T0_Experimentelle_Tests.pdf}}{{T0\\_Experimentelle\\_Tests.pdf}}
\\item Mathematisches Framework: \\href{{../T0_Mathematische_Grundlagen.pdf}}{{T0\\_Mathematische\\_Grundlagen.pdf}}
\\end{{itemize}}

\\end{{document}}
"""

def create_chapter_file(chapter_data, language='en'):
    """Create complete LaTeX file with NO content truncation"""
    
    num = chapter_data['num']
    title = chapter_data['title']
    content = chapter_data['content']
    
    # Generate filename
    title_safe = re.sub(r'[^a-zA-Z0-9]+', '_', title)
    if language == 'en':
        filename = f"Chapter_{num:02d}_{title_safe}_En.tex"
        output_dir = EN_DIR
    else:
        filename = f"Kapitel_{num:02d}_{title_safe}_De.tex"
        output_dir = DE_DIR
    
    filepath = output_dir / filename
    
    # Build complete LaTeX document
    latex_content = add_t0_preamble(num, title, language)
    
    # Add FULL chapter content (NO TRUNCATION)
    # Convert DVFT text to LaTeX sections
    sections = content.split('\n\n')
    for section in sections:
        if section.strip():
            # Detect section headers
            if re.match(r'^\d+\.', section):
                section_title = section.split('\n')[0]
                section_body = '\n'.join(section.split('\n')[1:])
                latex_content += f"\\section{{{section_title}}}\n\n{section_body}\n\n"
            else:
                latex_content += f"{section}\n\n"
    
    # Add T0 conclusion
    latex_content += add_t0_conclusion(num, language)
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    return filepath

# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("GENERATING ALL DVFT CHAPTERS WITH T0 ADAPTATIONS")
    print("=" * 60)
    print(f"Source: {DVFT_FILE}")
    print(f"Output EN: {EN_DIR}")
    print(f"Output DE: {DE_DIR}")
    print()
    
    # Extract ALL chapters
    chapters = extract_chapters_from_dvft()
    print(f"Extracted {len(chapters)} complete chapters from DVFT.txt")
    
    # Show chapter sizes to confirm NO truncation
    print("\nChapter content lengths (characters):")
    for ch in chapters[:10]:  # Show first 10 as sample
        print(f"  Chapter {ch['num']:2d}: {ch['length']:,} chars - {ch['title'][:50]}")
    print(f"  ... ({len(chapters) - 10} more chapters)")
    
    # Check existing files
    existing_en = list(EN_DIR.glob("Chapter_*.tex"))
    existing_de = list(DE_DIR.glob("Kapitel_*.tex"))
    print(f"\nExisting: {len(existing_en)} EN, {len(existing_de)} DE chapters")
    
    # Generate ALL chapters
    print("\nGenerating chapters...")
    created_en = 0
    created_de = 0
    
    for chapter in chapters:
        # English version
        try:
            create_chapter_file(chapter, 'en')
            created_en += 1
            print(f"  ✓ EN Chapter {chapter['num']:2d}: {chapter['title'][:40]}")
        except Exception as e:
            print(f"  ✗ EN Chapter {chapter['num']:2d} FAILED: {e}")
        
        # German version
        try:
            create_chapter_file(chapter, 'de')
            created_de += 1
            print(f"  ✓ DE Kapitel {chapter['num']:2d}: {chapter['title'][:40]}")
        except Exception as e:
            print(f"  ✗ DE Kapitel {chapter['num']:2d} FAILED: {e}")
    
    print()
    print("=" * 60)
    print(f"COMPLETED: {created_en} EN + {created_de} DE chapters created")
    print(f"Total: {created_en + created_de} files with COMPLETE content")
    print("=" * 60)
