import os
import re

BASE_DIR = r"C:\Users\johann\B15\2\fix_tabellen"
DE_DIR = os.path.join(BASE_DIR, "de_standalone")
EN_DIR = os.path.join(BASE_DIR, "en_standalone")
PROCESS_DIRS = [DE_DIR, EN_DIR]

EXTRACTED_DIR = os.path.join(BASE_DIR, "extracted_tables")
FINAL_CORRECTED_DIR = os.path.join(BASE_DIR, "final_corrected")
os.makedirs(FINAL_CORRECTED_DIR, exist_ok=True)

def replace_edited_tables():
    print("=== Skript 2: Bearbeitete Tabellen aus _tables.tex einsetzen ===\n")

    for directory in PROCESS_DIRS:
        if not os.path.exists(directory):
            continue

        for root, _, files in os.walk(directory):
            for file in files:
                if not file.endswith('.tex'):
                    continue
                original_path = os.path.join(root, file)
                original_name = os.path.basename(file)

                # Bearbeitete Datei: Originalname + _tables.tex
                edited_file_name = original_name.replace('.tex', '_tables.tex')
                edited_path = os.path.join(EXTRACTED_DIR, edited_file_name)

                if not os.path.exists(edited_path):
                    print(f"  Bearbeitete Datei fehlt: {edited_file_name} → überspringe {original_name}")
                    continue

                print(f"  Einsetzen in: {original_name}")

                with open(original_path, 'r', encoding='utf-8') as f:
                    original_content = f.read()

                with open(edited_path, 'r', encoding='utf-8') as f:
                    edited_content = f.read()

                # Extrahiere korrigierte Tabellen aus der bearbeiteten Datei
                pattern = r'\\section\*\{Tabelle \d+ aus [^}]*\}\s*([\s\S]*?)(?=\\section\*\{Tabelle |\Z)'
                edited_tables = re.findall(pattern, edited_content)

                # Original-Tabellen finden
                original_tables_raw = re.findall(r'(\\begin\{(tabular\*?|longtable|tcolorbox)\}[^}]*\}[\s\S]*?\\end\{\2\})', original_content)
                original_tables = [t[0] for t in original_tables_raw]

                updated_content = original_content
                replaced_count = 0
                for old_table, new_table in zip(original_tables, edited_tables):
                    if old_table.strip() in updated_content:
                        updated_content = updated_content.replace(old_table.strip(), new_table.strip(), 1)
                        replaced_count += 1

                if replaced_count < len(edited_tables):
                    print(f"    Fallback aktiv – positionsbasiertes Ersetzen")
                    parts = re.split(r'(\\begin\{(tabular\*?|longtable|tcolorbox)\}[^}]*\}[\s\S]*?\\end\{\2\})', original_content)
                    new_parts = parts[:1]
                    idx = 0
                    for i in range(1, len(parts), 2):
                        if idx < len(edited_tables):
                            new_parts.append(edited_tables[idx].strip())
                            if i + 1 < len(parts):
                                new_parts.append(parts[i + 1])
                            idx += 1
                        else:
                            new_parts.append(parts[i])
                            if i + 1 < len(parts):
                                new_parts.append(parts[i + 1])
                    updated_content = ''.join(new_parts)

                # Speichern mit Originalnamen
                final_path = os.path.join(FINAL_CORRECTED_DIR, original_name)
                with open(final_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                print(f"    → {len(edited_tables)} Tabellen eingesetzt → {original_name}")

    print(f"\nFertig! Alle korrigierten Dateien liegen in:\n{FINAL_CORRECTED_DIR}")

if __name__ == "__main__":
    replace_edited_tables()