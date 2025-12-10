#!/usr/bin/env python3
import re
import sys

def generate_chapter_file(standalone_path, chapter_path):
    """Generate chapter file with EXACT content preservation, removing maketitle and tableofcontents"""
    with open(standalone_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'\\title\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', content)
    if not title_match:
        print(f"Warning: No title found in {standalone_path}")
        return False
    
    title = title_match.group(1)
    
    # Extract content between \begin{document} and \end{document}
    doc_match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if not doc_match:
        print(f"Error: No document environment found in {standalone_path}")
        return False
    
    doc_content = doc_match.group(1)
    
    # Remove \maketitle and \tableofcontents (with optional whitespace)
    doc_content = re.sub(r'\s*\\maketitle\s*', '\n', doc_content)
    doc_content = re.sub(r'\s*\\tableofcontents\s*', '\n', doc_content)
    
    # Write chapter file with EXACT content
    with open(chapter_path, 'w', encoding='utf-8') as f:
        f.write(f"% Chapter file: {chapter_path.split('/')[-1]}\n")
        f.write(f"% Source: {standalone_path.split('/')[-1]}\n\n")
        f.write(f"\\chapter{{{title}}}\n")
        f.write(doc_content)
    
    return True

if __name__ == '__main__':
    # Generate chapter files for the 8 landscape-fixed documents
    docs = [
        ('de_standalone/018_T0_Anomale-g2-9_De.tex', 'de_chapters_new/018_T0_Anomale-g2-9_De_ch.tex'),
        ('de_standalone/041_parameterherleitung_De.tex', 'de_chapters_new/041_parameterherleitung_De_ch.tex'),
        ('de_standalone/054_Elimination_Of_Mass_Dirac_Tabelle_De.tex', 'de_chapters_new/054_Elimination_Of_Mass_Dirac_Tabelle_De_ch.tex'),
        ('de_standalone/103_T0_Anomale-g2-6_De.tex', 'de_chapters_new/103_T0_Anomale-g2-6_De_ch.tex'),
        ('en_standalone/018_T0_Anomale-g2-9_En.tex', 'en_chapters_new/018_T0_Anomale-g2-9_En_ch.tex'),
        ('en_standalone/041_parameterherleitung_En.tex', 'en_chapters_new/041_parameterherleitung_En_ch.tex'),
        ('en_standalone/054_Elimination_Of_Mass_Dirac_Tabelle_En.tex', 'en_chapters_new/054_Elimination_Of_Mass_Dirac_Tabelle_En_ch.tex'),
        ('en_standalone/103_T0_Anomale-g2-6_En.tex', 'en_chapters_new/103_T0_Anomale-g2-6_En_ch.tex'),
    ]
    
    for standalone, chapter in docs:
        print(f"Generating {chapter}...")
        if generate_chapter_file(standalone, chapter):
            print(f"  ✓ Success")
        else:
            print(f"  ✗ Failed")
            sys.exit(1)
    
    print("\nAll chapter files generated successfully!")
