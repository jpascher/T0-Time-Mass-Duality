import os
import re

BASE_DIR = r"C:\Users\johann\B15\2\fix_tabellen"
DE_DIR = os.path.join(BASE_DIR, "de_standalone")
EN_DIR = os.path.join(BASE_DIR, "en_standalone")
PROCESS_DIRS = [DE_DIR, EN_DIR]

EXTRACTED_DIR = os.path.join(BASE_DIR, "extracted_tables")

def replace_edited_tables():
    """Setzt korrigierte Tabellen aus _tables_edited.tex in die Originaldateien ein."""
    for directory in PROCESS_DIRS:
        if not os.path.exists(directory):
            continue
        
        print(f"\nVerarbeite Ordner: {directory}")
        
        for root, _, files in os.walk(directory):
            for file in files:
                if not file.endswith('.tex'):
                    continue
                file_path = os.path.join(root, file)
                rel_file = os.path.basename(file_path)
                
                edited_file = os.path.join(EXTRACTED_DIR, f"{rel_file}_tables_edited.tex")
                if not os.path.exists(edited_file):
                    print(f"  Bearbeitete Datei fehlt: {os.path.basename(edited_file)}")
                    continue
                
                with open(edited_file, 'r', encoding='utf-8') as f:
                    edited_content = f.read()

                with open(file_path, 'r', encoding='utf-8') as f:
                    original_content = f.read()

                # Extrahiere korrigierte Tabellen aus edited .tex
                edited_tables = re.findall(r'\\section*\{Tabelle \d+ aus .*?\}\s*(\\begin\{adjustbox\}.*?\\end\{adjustbox\})', edited_content, re.DOTALL)
                original_tables = re.findall(r'(\\begin\{adjustbox\}.*?\\end\{adjustbox\})', original_content, re.DOTALL)

                if len(edited_tables) != len(original_tables):
                    print(f"  Anzahl Tabellen stimmt nicht überein in {rel_file}: Original {len(original_tables)}, Edited {len(edited_tables)}")
                    continue

                updated_content = original_content
                for old, new in zip(original_tables, edited_tables):
                    updated_content = updated_content.replace(old, new.strip())

                final_path = file_path.replace('.tex', '_kdp_final.tex')
                with open(final_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                print(f"  Tabellen eingesetzt → {os.path.basename(final_path)}")

if __name__ == "__main__":
    print("=== Skript 2: Bearbeitete Tabellen einsetzen ===")
    replace_edited_tables()
    print("\nFertig! Alle _kdp_final.tex erstellt.")