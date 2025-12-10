import os

# Directory containing the LaTeX files
tex_dir = r'C:\Users\johann\1\2\tex'

# New subdirectory for preambles
preamble_dir = os.path.join(tex_dir, 'preambles')
os.makedirs(preamble_dir, exist_ok=True)

print("Schritt 1: Extrahiere und sammle Preambles...")

# Dictionary to hold preambles: filename -> preamble content
preambles = {}

# Process each .tex file to extract preambles
for file in os.listdir(tex_dir):
    if file.endswith('.tex'):
        file_path = os.path.join(tex_dir, file)
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find the position of \begin{document}
            begin_doc = content.find(r'\begin{document}')
            if begin_doc != -1:
                preamble = content[:begin_doc]
                preambles[file] = preamble
            else:
                print(f"Keine \\begin{{document}} in {file} gefunden")
        except Exception as e:
            print(f"Fehler bei {file}: {e}")

print(f"{len(preambles)} Preambles extrahiert.")

print("Schritt 2: Teile in zwei Teile: teil1.tex und teil2.tex im Unterverzeichnis preambles...")

# Sort the filenames alphabetically
sorted_files = sorted(preambles.keys())
num_files = len(sorted_files)
half = num_files // 2

# First half
content1 = ""
for filename in sorted_files[:half]:
    content1 += f'=== {filename}.preamble ===\n\n'
    content1 += preambles[filename]
    content1 += '\n\n' + '=' * 50 + '\n\n'

# Second half
content2 = ""
for filename in sorted_files[half:]:
    content2 += f'=== {filename}.preamble ===\n\n'
    content2 += preambles[filename]
    content2 += '\n\n' + '=' * 50 + '\n\n'

# Output files im Unterverzeichnis
output_file1 = os.path.join(preamble_dir, 'teil1.tex')
output_file2 = os.path.join(preamble_dir, 'teil2.tex')

# Write to files
with open(output_file1, 'w', encoding='utf-8') as f1:
    f1.write(content1)

with open(output_file2, 'w', encoding='utf-8') as f2:
    f2.write(content2)

print(f"Preambles in zwei Teile geteilt: {output_file1} und {output_file2}")
print("Alle Schritte abgeschlossen!")