import os
import re

# Dein fixes Arbeitsverzeichnis
BASE_DIR = r"C:\Users\johann\B15\2\fix_tabellen"
DE_DIR = os.path.join(BASE_DIR, "de_standalone")
EN_DIR = os.path.join(BASE_DIR, "en_standalone")
PROCESS_DIRS = [DE_DIR, EN_DIR]

# Zentraler Ordner für alle extrahierten Tabellen-Dateien
EXTRACTED_DIR = os.path.join(BASE_DIR, "extracted_tables")
os.makedirs(EXTRACTED_DIR, exist_ok=True)

def extract_tables_to_latex():
    """Extrahiert Tabellen aus allen .tex-Dateien und speichert pro Originaldatei eine kompilierbare _tables_only.tex im zentralen Ordner."""
    for directory in PROCESS_DIRS:
        if not os.path.exists(directory):
            print(f"Ordner nicht gefunden: {directory}")
            continue
        
        preamble = r"\input{../../../T0_preamble_shared_En.tex}" if "en_standalone" in directory else r"\input{../../../T0_preamble_shared_De.tex}"
        
        print(f"\nVerarbeite Ordner: {directory}")
        
        for root, _, files in os.walk(directory):
            for file in files:
                if not file.endswith('.tex'):
                    continue
                file_path = os.path.join(root, file)
                print(f"  Datei: {os.path.basename(file_path)}")

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Tabellen extrahieren
                tables = re.findall(r'(\\begin\{(tabular\*?|longtable)\}[^}]*\}[\s\S]*?\\end\{\2\})', content)
                tcolor_tables = re.findall(r'(\\begin\{tcolorbox\}[^}]*\}[\s\S]*?\\begin\{(tabular\*?|longtable)\}[^}]*\}[\s\S]*?\\end\{\2\}[\s\S]*?\\end\{tcolorbox\})', content)
                all_tables = [t[0] for t in tables] + [t[0] for t in tcolor_tables]

                if not all_tables:
                    print(f"    → Keine Tabellen gefunden.")
                    continue

                # Kompilierbares LaTeX erstellen
                output_file = os.path.join(EXTRACTED_DIR, f"{os.path.basename(file_path)}_tables_only.tex")
                latex_content = r"""\documentclass[12pt,a4paper]{book}
""" + preamble + r"""

\begin{document}

\title{Tabellen aus """ + os.path.basename(file_path) + r"""}
\maketitle

\tableofcontents
\newpage

"""

                for i, table in enumerate(all_tables, 1):
                    latex_content += f"\\section*{{Tabelle {i} aus {os.path.basename(file_path)}}}\n"
                    latex_content += f"\\begin{{adjustbox}}{{max width=\\textwidth}}\n{table.strip()}\n\\end{{adjustbox}}\n\n"
                    latex_content += "\\bigskip\n\\clearpage\n\n"

                latex_content += r"\end{document}"

                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(latex_content)

                print(f"    → {len(all_tables)} Tabellen extrahiert → {os.path.basename(output_file)}")

if __name__ == "__main__":
    print("=== Skript 1: Tabellen extrahieren ===")
    extract_tables_to_latex()
    print("\nFertig! Alle _tables_only.tex im Ordner 'extracted_tables' erstellt.")
    print("Kompiliere jede Datei, bearbeite und speichere als _tables_edited.tex für Skript 2.")