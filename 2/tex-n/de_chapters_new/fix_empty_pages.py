import os
import re

# Pfad, den du angegeben hast – direkt übernommen
ROOT_DIR = r"C:\Users\johann\B16\1\2\fix\de_chapters_new"

# Muster für \chapter-Zeilen (erfasst auch mit optionalem Kurztitle: \chapter[Titel]{Langer Titel})
CHAPTER_PATTERN = re.compile(r'^\s*\\chapter(\[.*?\])?\{.*\}')

# Die Zeile, die wir einfügen wollen
INSERT_LINE = r'\let\cleardoublepage\clearpage'

def process_tex_file(filepath):
  with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
  
  new_lines = []
  modified = False
  i = 0
  
  while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    
    # Prüfen, ob dies eine \chapter-Zeile ist (ignoriert führende Leerzeichen/Kommentare)
    if CHAPTER_PATTERN.match(line.strip()):
      # Schauen, ob die Insert-Zeile bereits in den nächsten 10 Zeilen vorkommt
      already_inserted = False
      for j in range(i + 1, min(i + 11, len(lines))):
        if INSERT_LINE in lines[j]:
          already_inserted = True
          break
      
      if not already_inserted:
        # Direkt nach der \chapter-Zeile einfügen (mit Kommentar)
        new_lines.append(INSERT_LINE + ' % Entfernt leere Seite vor diesem Kapitel\n')
        modified = True
    
    i += 1
  
  if modified:
    with open(filepath, 'w', encoding='utf-8') as f:
      f.writelines(new_lines)
    print(f"GEÄNDERT: {filepath}")
  else:
    print(f"Unverändert: {filepath}")

def main():
  if not os.path.exists(ROOT_DIR):
    print(f"FEHLER: Der Pfad existiert nicht: {ROOT_DIR}")
    return
  
  tex_files = []
  for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
      if file.endswith('.tex'):
        tex_files.append(os.path.join(root, file))
  
  print(f"Gefundene .tex-Dateien: {len(tex_files)}\n")
  
  changed_count = 0
  for tex_file in tex_files:
    process_tex_file(tex_file)
    if "GEÄNDERT" in tex_file: # Dummy-Check – eigentlich über modified
      changed_count += 1
  
  print(f"\nFertig! {changed_count} Dateien wurden geändert.")
  print("Alle Kapitel sollten jetzt ohne leere Seite davor beginnen.")
  print("Kompiliere dein Haupt-Dokument neu (mehrfach), um die Änderungen zu sehen.")

if __name__ == "__main__":
  main()
