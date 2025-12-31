#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to create narrative versions of FFGFT chapters 14-44
with expanded content using the brain metaphor
"""

import os
import sys

def create_narrative_intro_de(chapter_num, chapter_title):
    """Create a German narrative introduction with brain metaphor"""
    intros = {
        14: """
    \\subsection*{Narrative Einführung: Das erwachende kosmische Gehirn}
    
    Stellen Sie sich vor, Sie beobachten die Entwicklung eines Gehirns im Zeitraffer – nicht das Wachstum eines biologischen Organs, sondern die Entstehung des Universums selbst. Was wir gemeinhin als „Urknall" und „Expansion des Raums" bezeichnen, ist in Wahrheit ein viel subtilerer und faszinierender Prozess: das Erwachen eines kosmischen Bewusstseins aus einem Zustand reiner Potenzialität.
    
    In diesem Kapitel erforschen wir, wie physikalischer Raum nicht als vorgegebene Bühne existiert, sondern durch eine fraktale Amplitude-Front erschaffen wird – vergleichbar mit der neuronalen Aktivierung, die sich wellenförmig durch Gehirnregionen ausbreitet und dabei erst die Voraussetzung für Bewusstsein schafft. Die „Expansion" des Universums ist tatsächlich diese Aktivierungsfront, die mit einer Geschwindigkeit knapp über der Lichtgeschwindigkeit durch das fraktale Vakuum läuft.
    
    Genau wie ein sich entwickelndes Gehirn nicht einfach größer wird, sondern komplexere Windungen und Verbindungen ausbildet, schafft diese Front nicht einfach „mehr Raum", sondern strukturiert das Vakuum auf eine Weise, die zunehmend komplexe physikalische Phänomene ermöglicht. Der gesamte Prozess wird durch einen einzigen geometrischen Parameter bestimmt: $\\xi = \\frac{4}{3} \\times 10^{-4}$ – die fraktale Packungsdichte des kosmischen Gehirns.
    
    \\subsection*{Die mathematische Grundlage}
    """
    }
    
    # Default intro for other chapters
    default_intro = f"""
    \\subsection*{{Narrative Einführung: Das kosmische Gehirn im Detail}}
    
    Wir setzen unsere Reise durch das kosmische Gehirn fort. In diesem Kapitel betrachten wir weitere Aspekte der fraktalen Struktur des Universums, die – wie die komplexen Windungen eines Gehirns – auf allen Skalen selbstähnliche Muster aufweisen. Was auf den ersten Blick wie isolierte physikalische Phänomene erscheint, erweist sich bei genauerer Betrachtung als Ausdruck eines einheitlichen geometrischen Prinzips: der fraktalen Packung mit Parameter $\\xi = \\frac{{4}}{{3}} \\times 10^{{-4}}$.
    
    Genau wie verschiedene Hirnregionen spezialisierte Funktionen erfüllen und dennoch durch ein gemeinsames neuronales Netzwerk verbunden sind, zeigen die hier diskutierten Phänomene, wie lokale Strukturen und globale Eigenschaften des Universums durch die Time-Mass-Dualität miteinander verwoben sind.
    
    \\subsection*{{Die mathematische Grundlage}}
    """
    
    return intros.get(chapter_num, default_intro)

def create_narrative_conclusion_de(chapter_num):
    """Create a German narrative conclusion connecting to brain metaphor"""
    return """
    
    \\subsection*{Narrative Zusammenfassung: Das Gehirn verstehen}
    
    Was wir in diesem Kapitel gesehen haben, ist mehr als eine Sammlung mathematischer Formeln – es ist ein Fenster in die Funktionsweise des kosmischen Gehirns. Jede Gleichung, jede Herleitung offenbart einen Aspekt der zugrundeliegenden fraktalen Geometrie, die das Universum strukturiert.
    
    Denken Sie an die zentrale Metapher: Das Universum als sich entwickelndes Gehirn, dessen Komplexität nicht durch Größenwachstum, sondern durch zunehmende Faltung bei konstantem Volumen entsteht. Die fraktale Dimension $D_f = 3 - \\xi$ beschreibt genau diese Faltungstiefe – ein Maß dafür, wie stark das kosmische Gewebe in sich selbst zurückgefaltet ist.
    
    Die hier präsentierten Ergebnisse sind keine isolierten Fakten, sondern Puzzleteile eines größeren Bildes: einer Realität, in der Zeit und Masse dual zueinander sind, in der Raum nicht fundamental ist, sondern aus der Aktivität eines fraktalen Vakuums emergiert, und in der alle beobachtbaren Phänomene aus einem einzigen geometrischen Parameter $\\xi$ folgen.
    
    Dieses Verständnis transformiert unsere Sicht auf das Universum von einem mechanischen Uhrwerk zu einem lebendigen, sich selbst organisierenden System – einem kosmischen Gehirn, das in jedem Moment seine eigene Struktur durch die Time-Mass-Dualität erschafft und erhält.
    """

def process_chapter_de(chapter_num, source_dir, target_dir):
    """Process a single German chapter"""
    source_file = os.path.join(source_dir, f"kapitel_{chapter_num}a_De.tex")
    target_file = os.path.join(target_dir, f"Kapitel_{chapter_num:02d}_Narrative_De.tex")
    
    if not os.path.exists(source_file):
        print(f"Warning: Source file {source_file} not found")
        return False
    
    try:
        # Read source file
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the section title
        import re
        section_match = re.search(r'\\section\{([^}]+)\}', content)
        if section_match:
            chapter_title = section_match.group(1)
        else:
            chapter_title = f"Kapitel {chapter_num}"
        
        # Insert narrative intro after the section header
        section_pattern = r'(\\section\{[^}]+\}[\s\n]*)'
        narrative_intro = create_narrative_intro_de(chapter_num, chapter_title)
        content = re.sub(section_pattern, lambda m: m.group(1) + narrative_intro + '\n\t', content, count=1)
        
        # Add narrative conclusion before \end{document}
        narrative_conclusion = create_narrative_conclusion_de(chapter_num)
        content = content.replace('\\end{document}', narrative_conclusion + '\n\t\n\\end{document}')
        
        # Update headheight in preamble if present
        content = re.sub(r'\\setlength\{\\headheight\}\{[^}]+\}', 
                        r'\\setlength{\\headheight}{30pt}', content)
        
        # If geometry doesn't set headheight, add it
        if 'headheight' not in content and '\\usepackage{geometry}' in content:
            content = re.sub(r'(\\usepackage\{geometry\})',
                           r'\1\n\\setlength{\\headheight}{30pt}', content)
        
        # Write target file
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created: {target_file}")
        return True
        
    except Exception as e:
        print(f"Error processing chapter {chapter_num}: {e}")
        return False

def main():
    """Main function to create all narrative chapters"""
    repo_root = "/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality"
    source_dir = os.path.join(repo_root, "2/tex-n/de_FFGFT/tex_kapitel")
    target_dir = os.path.join(repo_root, "2/narrative")
    
    # Ensure target directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    # Process chapters 14-44
    success_count = 0
    for chapter_num in range(14, 45):
        if process_chapter_de(chapter_num, source_dir, target_dir):
            success_count += 1
    
    print(f"\nCompleted: {success_count}/31 chapters created successfully")
    
    return 0 if success_count == 31 else 1

if __name__ == "__main__":
    sys.exit(main())
