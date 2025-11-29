#!/usr/bin/env python3
"""
Build complete book - minimal changes: remove documentclass, begin/end document.
Uses T0_preamble for all definitions.
"""
import os
import re
import sys

# Kapitel für Kurzbuch (50 Kapitel)
SHORT_CHAPTERS = [
    "T0_Book_Abstract",
    "T0_Introduction",
    "reise",
    "T0_Grundlagen",
    "T0_Modell_Uebersicht",
    "T0_7-fragen-3",
    "Hannah",
    "Markov",
    "T0-Theory-vs-Synergetics",
    "T0_threeclock",
    "T0_penrose",
    "T0_peratt",
    "T0_Analyse_MNRAS_Widerlegung",
    "T0vsESM_ConceptualAnalysis",
    "T0_Teilchenmassen",
    "Teilchenmassen",
    "T0_tm-erweiterung-x6",
    "T0_Neutrinos",
    "T0_koide-formel-3",
    "T0_xi-und-e",
    "T0_xi_ursprung",
    "T0_SI",
    "T0_nat-si",
    "T0_Vollstaendige_Berchnungen",
    "T0_verhaeltnis-absolut",
    "T0_Energie",
    "T0_Feinstruktur",
    "T0_Gravitationskonstante",
    "T0_Kosmologie",
    "T0_Geometrische_Kosmologie",
    "Zwei-Dipole-CMB",
    "T0_Anomale_Magnetische_Momente",
    "T0_Anomale-g2-6",
    "T0_Anomale-g2-9",
    "T0_lagrndian",
    "dirac",
    "T0_QM-QFT-RT",
    "T0-QFT-ML_Addendum",
    "T0_QAT",
    "T0_QM-optimierung",
    "T0_g2-erweiterung-4",
    "T0_freqeunz",
    "universale-ableitung",
    "T0_umkehrung",
    "T0_netze",
    "RSA",
    "T0_photonenchip-einführung",
    "T0_photonenchip-umsetzung",
    "T0_photonenchip-china",
    "Zusammenfassung",
]

def extract_body_content(filepath):
    """Extract content between begin{document} and end{document}."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
        if match:
            body = match.group(1).strip()
            body = re.sub(r'\\maketitle\s*', '', body)
            body = re.sub(r'\\tableofcontents\s*', '', body)
            return body
        return None
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def get_chapter_title(filepath):
    """Extract title from document."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        match = re.search(r'\\title\{([^}]+)\}', content)
        if match:
            title = match.group(1)
            title = re.sub(r'\\\\\[[^\]]*\]', ' ', title)
            title = re.sub(r'\\\\', ' ', title)
            title = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', title)
            title = re.sub(r'\\[a-zA-Z]+', '', title)
            title = re.sub(r'\[[^\]]*\]', '', title)
            title = re.sub(r'[{}]', '', title)
            title = re.sub(r'\s+', ' ', title).strip()
            if len(title) > 70:
                title = title[:67] + "..."
            return title
        
        basename = os.path.basename(filepath)
        return basename.replace('.tex', '').replace('_', ' ')
    except:
        return os.path.basename(filepath).replace('.tex', '')

def build_book(lang, short=False):
    """Build book for given language."""
    completed_dir = "completed"
    suffix = f"_{lang}" if lang in ["De", "En"] else lang
    
    if lang == "De":
        preamble_file = "T0_preamble_De"
        cover_file = "T0_deckblatt_De.png"
        toc_title = "Inhaltsverzeichnis"
        footer = "T0-Theorie -- Johann Pascher"
        book_subtitle = "Kurzfassung (50 Kapitel)" if short else "Vollständige Sammlung"
    else:
        preamble_file = "T0_preamble_En"
        cover_file = "T0_deckblatt_En.png"
        toc_title = "Contents"
        footer = "T0-Theory -- Johann Pascher"
        book_subtitle = "Short Version (50 Chapters)" if short else "Complete Collection"
    
    # Get list of tex files
    if short:
        tex_files = []
        for base in SHORT_CHAPTERS:
            fname = f"{base}{suffix}.tex"
            fpath = os.path.join(completed_dir, fname)
            if os.path.exists(fpath):
                tex_files.append(fname)
            else:
                # Try alternate naming
                fname2 = f"{base}De.tex" if lang == "De" else f"{base}En.tex"
                fpath2 = os.path.join(completed_dir, fname2)
                if os.path.exists(fpath2):
                    tex_files.append(fname2)
    else:
        tex_files = sorted([f for f in os.listdir(completed_dir) 
                           if f.endswith('.tex') and suffix in f])
    
    output_file = f"T0_Book_Short_{lang}.tex" if short else f"T0_Complete_Book_Full_{lang}.tex"
    
    # Build preamble
    preamble = f"""\\documentclass[a4paper,11pt]{{book}}
\\input{{completed/{preamble_file}}}

\\usepackage{{fancyhdr}}
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[LE,RO]{{\\scriptsize\\thepage}}
\\fancyhead[LO]{{\\scriptsize T0}}
\\fancyhead[RE]{{\\scriptsize Pascher}}
\\fancyfoot[C]{{\\scriptsize {footer}}}

\\fancypagestyle{{plain}}{{
  \\fancyhf{{}}
  \\fancyfoot[C]{{\\scriptsize\\thepage}}
  \\renewcommand{{\\headrulewidth}}{{0pt}}
}}

\\begin{{document}}

% Cover
\\begin{{titlepage}}
\\centering
\\includegraphics[width=\\textwidth]{{{cover_file}}}
\\end{{titlepage}}

\\frontmatter
\\tableofcontents

\\mainmatter
"""
    
    chapters = []
    chapter_num = 0
    
    for tex_file in tex_files:
        filepath = os.path.join(completed_dir, tex_file)
        
        body = extract_body_content(filepath)
        if not body:
            continue
        
        title = get_chapter_title(filepath)
        chapter_num += 1
        
        chapters.append(f"\n\\chapter{{{title}}}\n{body}\n")
        print(f"  Added chapter {chapter_num}: {title[:60]}...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(preamble)
        for ch in chapters:
            f.write(ch)
        f.write("\n\\end{document}\n")
    
    print(f"\nBook written to: {output_file}")
    print(f"Total chapters: {chapter_num}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 build_complete_book.py <De|En> [short]")
        sys.exit(1)
    
    lang = sys.argv[1]
    short = len(sys.argv) > 2 and sys.argv[2] == "short"
    build_book(lang, short)
