import re
import os

# Pfad zur Eingabedatei
input_file = 'DVFT.txt'

# Ausgabeverzeichnis
output_dir = 'DVFT_Kapitel'
os.makedirs(output_dir, exist_ok=True)

# Gesamten Text einlesen
with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Alles vor dem ersten CHAPTER als Intro speichern
first_chapter_pos = text.find('CHAPTER 1:')
if first_chapter_pos != -1:
    intro_text = text[:first_chapter_pos].strip()
    intro_path = os.path.join(output_dir, '00_intro.txt')
    with open(intro_path, 'w', encoding='utf-8') as f:
        f.write(intro_text)
    print(f"Gespeichert: {intro_path}")

# Schlüsselwörter pro Kapitel (kurz, nur ein Wort)
key_words = [
    "vacuum", "dynamic", "equations", "curvature", "problems", "emc2",
    "relativity", "chapter8", "chapter9", "chapter10", "chapter11", "chapter12",
    "chapter13", "chapter14", "chapter15", "chapter16", "chapter17", "chapter18",
    "chapter19", "chapter20", "chapter21", "chapter22", "chapter23", "chapter24",
    "chapter25", "chapter26", "chapter27", "chapter28", "chapter29", "chapter30",
    "chapter31", "chapter32", "chapter33", "chapter34", "chapter35", "chapter36",
    "chapter37", "chapter38", "singularity", "entropy", "alternative",
    "properties", "planck", "axioms"
]

# Regex für Kapitel erfassen
pattern = r'(CHAPTER\s+(\d+):[^\n]*\n(?:.|[\n\r])*?)(?=CHAPTER\s+\d+:|REFERENCES|$)'
matches = re.finditer(pattern, text, re.MULTILINE | re.DOTALL)

chapter_count = 0
for match in matches:
    chapter_count += 1
    chapter_text = match.group(1).strip()
    
    # Schlüsselwort wählen
    idx = chapter_count - 1
    if idx < len(key_words):
        keyword = key_words[idx]
    else:
        keyword = f"chapter{chapter_count}"
    
    # Dateiname: nur nummer_wort.txt (klein, keine Sonderzeichen)
    filename = f"{chapter_count:02d}_{keyword.lower()}.txt"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(chapter_text)
    
    print(f"Gespeichert: {filepath}")

# References separat speichern
ref_pos = text.find('REFERENCES')
if ref_pos != -1:
    references_text = text[ref_pos:].strip()
    ref_path = os.path.join(output_dir, 'references.txt')
    with open(ref_path, 'w', encoding='utf-8') as f:
        f.write(references_text)
    print(f"Gespeichert: {ref_path}")

print(f"\nFertig! Intro + {chapter_count} Kapitel + References in '{output_dir}' gespeichert.")