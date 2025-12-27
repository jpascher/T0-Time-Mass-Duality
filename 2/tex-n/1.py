import os
import re

INPUT_FILE = 'DVFT.txt'
OUTPUT_DIR = '2/md_chapters_dvft'
os.makedirs(OUTPUT_DIR, exist_ok=True)

if not os.path.exists(INPUT_FILE):
    print(f"Fehler: {INPUT_FILE} nicht gefunden!")
    exit()

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    full_text = f.read()

# Robuster Regex: "CHAPTER" (groß/klein), Leerzeichen, Zahl, optional Leerzeichen, Doppelpunkt, optional Leerzeichen
# Splittet und behält den Marker
parts = re.split(r'(CHAPTER\s*\d+\s*:)', full_text, flags=re.IGNORECASE)

chapters = []
current_content = parts[0].strip()  # Vorspann/Einleitung

if current_content:
    chapters.append(("00_Vorspann", current_content))

for i in range(1, len(parts), 2):
    if i + 1 < len(parts):
        title_line = parts[i].strip()  # z. B. "CHAPTER 1:" oder "Chapter 5 :"
        content = parts[i + 1]  # Inhalt bis zum nächsten Marker (nicht strip, um Zeilen zu erhalten)
        
        # Kapitel-Nummer extrahieren
        match = re.search(r'\d+', title_line)
        if match:
            num = match.group(0).zfill(2)
        else:
            num = f"{len(chapters):02d}"
        
        title = f"Kapitel_{num}"
        
        # Inhalt bereinigen (leading/trailing Whitespace entfernen, aber innere Zeilen behalten)
        content_clean = content.strip()
        
        chapters.append((title, content_clean))

# Separate .md-Dateien erstellen
for idx, (title, content) in enumerate(chapters):
    filename = f"{title}.md"
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title.replace('_', ' ')}\n\n")
        f.write(content + "\n")
    
    lines = len(content.splitlines())
    print(f"Erstellt: {output_path} ({lines} Zeilen, vollständiger Inhalt)")

print(f"\nFertig! {len(chapters)} Kapitel als separate .md-Dateien in {OUTPUT_DIR}/ (aus deinen Dokumenten in DVFT.txt unter 2/-Struktur).")
print("Beispiel-Dateien: Kapitel_01.md bis Kapitel_43.md")