#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Progressive Narrative Chapter Generator for FFGFT
Creates chapters 14-44 with progressive narrative style
"""

import os
import re

def get_progressive_intro(chapter_num):
  """Generate progressive introductions that build on previous chapters"""
  
  intros = {
    15: """\\subsection*{Progressive Narrative Einführung}
    
Nachdem wir in Kapitel 14 gesehen haben, wie Raum aus der fraktalen Amplitude-Front emergiert, wenden wir uns nun einem noch fundamentaleren Aspekt zu: der geometrischen Struktur dieser Emergenz. Die Time-Mass-Dualität, die wir aus den ersten Kapiteln kennen, manifestiert sich hier in einer spezifischen mathematischen Form, die wir jetzt detailliert untersuchen werden.

Erinnern wir uns: Im kosmischen Gehirn entspricht die Raum-Schöpfung der Ausbreitung neuronaler Aktivität. In diesem Kapitel erforschen wir die präzise geometrische Sprache, in der dieser Prozess beschrieben wird – eine Sprache, die auf dem fraktalen Parameter $\\xi$ und der bereits etablierten Dualitätsbeziehung aufbaut.
""",
    16: """\\subsection*{Progressive Narrative Einführung}

Die vorangegangenen Kapitel haben uns gezeigt, wie Raum emergiert (Kapitel 14) und welche geometrische Struktur diesem Prozess zugrunde liegt (Kapitel 15). Nun untersuchen wir die dynamischen Konsequenzen dieser Geometrie: Wie verhält sich Materie in einem Raum, der selbst ein emergentes Phänomen ist?

Diese Frage führt uns zu einer der elegantesten Vorhersagen der FFGFT. In einem Universum, das sich wie ein reifendes Gehirn entwickelt, erwarten wir spezifische Signaturen in der Bewegung von Galaxien und der Verteilung von Materie. Diese Kapitel baut auf unseren Erkenntnissen über die fraktale Dimension $D_f = 3 - \\xi$ auf und zeigt, wie sie sich in beobachtbaren Phänomenen manifestiert.
""",
    17: """\\subsection*{Progressive Narrative Einführung}

Wir haben nun die Grundlagen der Raum-Emergenz (Kapitel 14), ihre geometrische Beschreibung (Kapitel 15) und die dynamischen Konsequenzen für Materie (Kapitel 16) verstanden. Dieses Kapitel führt diese Erkenntnisse zusammen und untersucht, wie sie sich auf kosmologischen Skalen auswirken.

Die Time-Mass-Dualität, die wir seit den ersten Kapiteln kennen, zeigt hier ihre volle Kraft: Sie verbindet lokale Phänomene (wie die Bewegung einzelner Galaxien) mit globalen kosmischen Strukturen. Im Bild des kosmischen Gehirns entspricht dies der Verbindung zwischen einzelnen neuronalen Feuerereignissen und emergenten Bewusstseinsphänomenen.
""",
  }
  
  # Default progressive intro for chapters not specifically defined
  default = f"""\\subsection*{{Progressive Narrative Einführung}}

Dieses Kapitel baut auf den vorangegangenen Erkenntnissen auf. Wir haben in den ersten {chapter_num-1} Kapiteln die fundamentalen Prinzipien der FFGFT kennengelernt: die Time-Mass-Dualität, die fraktale Geometrie mit Parameter $\\xi = \\frac{{4}}{{3}} \\times 10^{{-4}}$, die Emergenz des Raums, und zahlreiche Anwendungen dieser Prinzipien.

In diesem Kapitel erweitern wir unser Verständnis um weitere Aspekte, die aus den etablierten Prinzipien folgen. Wir werden sehen, wie die bereits bekannten Konzepte neue Einsichten ermöglichen und wie sich das Bild des kosmischen Gehirns weiter verfeinert.

Die hier präsentierten Ergebnisse setzen das Verständnis der vorherigen Kapitel voraus und führen die Argumentation systematisch fort.
"""
  
  return intros.get(chapter_num, default)

def get_progressive_conclusion(chapter_num):
  """Generate progressive conclusions that link to future chapters"""
  
  return f"""
\\subsection*{{Progressive Narrative Zusammenfassung}}

Dieses Kapitel hat unsere Reise durch die FFGFT um wichtige Aspekte erweitert. Die hier entwickelten Konzepte bauen direkt auf den Erkenntnissen der Kapitel 1-{chapter_num-1} auf und bereiten den Boden für die folgenden Untersuchungen.

Im kosmischen Gehirn entspricht jedes neue Kapitel einer tieferen Schicht des Verständnisses – ähnlich wie in einem neuronalen Netzwerk höhere Verarbeitungsebenen auf den Aktivierungen niedrigerer Ebenen aufbauen. Die hier präsentierten mathematischen Strukturen sind nicht isoliert, sondern integraler Bestandteil des Gesamtbildes, das sich durch alle 44 Kapitel hindurch entfaltet.

In den kommenden Kapiteln werden wir sehen, wie diese Erkenntnisse weitere Anwendungen finden und wie sich das einheitliche Bild der FFGFT weiter vervollständigt. Jeder Schritt bringt uns näher an ein umfassendes Verständnis des Universums als sich selbst organisierendes, fraktal strukturiertes System – ein kosmisches Gehirn, das in jedem Moment seine eigene Struktur durch die Time-Mass-Dualität erschafft und erhält.
"""

def create_narrative_chapter_de(chapter_num, source_dir, target_dir):
  """Create a single German narrative chapter with progressive style"""
  
  source_file = os.path.join(source_dir, f"kapitel_{chapter_num}a_De.tex")
  target_file = os.path.join(target_dir, f"Kapitel_{chapter_num:02d}_Narrative_De.tex")
  
  if not os.path.exists(source_file):
    print(f"Warning: Source file {source_file} not found")
    return False
  
  try:
    # Read source file
    with open(source_file, 'r', encoding='utf-8') as f:
      content = f.read()
    
    # Update headheight in geometry
    if 'headheight' not in content and 'geometry' in content:
      content = re.sub(r'(\\geometry\{[^}]+)\}', 
              r'\1}\n\\setlength{\\headheight}{30pt}', content)
    
    # Find the main section and insert progressive intro after it
    section_pattern = r'(\\section\{[^}]+\}\s*)'
    progressive_intro = get_progressive_intro(chapter_num)
    
    # Insert progressive intro after section title
    content = re.sub(section_pattern, 
            lambda m: m.group(1) + '\n' + progressive_intro + '\n\\subsection*{Der mathematische Rahmen}\n\n',
            content, count=1)
    
    # Add progressive conclusion before \end{document}
    progressive_conclusion = get_progressive_conclusion(chapter_num)
    content = content.replace('\\end{document}', 
                progressive_conclusion + '\n\\end{document}')
    
    # Write target file
    with open(target_file, 'w', encoding='utf-8') as f:
      f.write(content)
    
    print(f"Created: {target_file}")
    return True
    
  except Exception as e:
    print(f"Error processing chapter {chapter_num}: {e}")
    return False

def main():
  """Generate all narrative chapters 15-44"""
  
  repo_root = "/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality"
  source_dir = os.path.join(repo_root, "2/tex-n/de_FFGFT/tex_kapitel")
  target_dir = os.path.join(repo_root, "2/narrative")
  
  # Process chapters 15-44 (chapter 14 already done manually)
  success_count = 0
  for chapter_num in range(15, 45):
    if create_narrative_chapter_de(chapter_num, source_dir, target_dir):
      success_count += 1
  
  print(f"\nCompleted: {success_count}/30 German chapters created")
  
  return 0 if success_count == 30 else 1

if __name__ == "__main__":
  import sys
  sys.exit(main())

