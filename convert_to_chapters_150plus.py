#!/usr/bin/env python3
"""
Convert standalone documents (150+) to chapter format.
- Removes preamble, \\begin{document}, \\title, \\maketitle
- Converts \\begin{abstract}...\\end{abstract} to \\section*{Abstract}
- Converts first \\section to \\chapter
- Removes \\tableofcontents and \\end{document}
- Output filename: same as input but with _ch.tex ending
"""

import os
import re
from pathlib import Path

def convert_standalone_to_chapter(source_file, target_file):
    """Convert a standalone LaTeX file to chapter format"""
    
    print(f"\n📖 Konvertiere: {source_file.name}")
    
    try:
        # Read source file
        # Skip if target file already exists and language matches
        if os.path.exists(target_file):
            # Check language marker in both source and target
            with open(source_file, 'r', encoding='utf-8') as f:
                src_content = f.read()
            with open(target_file, 'r', encoding='utf-8') as f:
                tgt_content = f.read()
            def detect_lang(text):
                if re.search(r'\\usepackage\[ngerman\]', text) or re.search(r'\\selectlanguage\{german\}', text) or re.search(r'\\begin\{document\}.*?german', text, re.DOTALL):
                    return 'de'
                if re.search(r'\\usepackage\[english\]', text) or re.search(r'\\selectlanguage\{english\}', text) or re.search(r'\\begin\{document\}.*?english', text, re.DOTALL):
                    return 'en'
                return None
            src_lang = detect_lang(src_content)
            tgt_lang = detect_lang(tgt_content)
            if src_lang == tgt_lang:
                print(f"   ⚠️  Zieldatei existiert bereits und Sprache stimmt überein: {target_file}, überspringe.")
                return True
            else:
                print(f"   ⚠️  Zieldatei existiert, aber Sprache stimmt nicht überein: {target_file}, wird überschrieben.")
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        
        # Find \begin{document}
        doc_start = -1
        for i, line in enumerate(lines):
            if re.match(r'^\s*\\begin\{document\}', line):
                doc_start = i
                print(f"   ✅ \\begin{{document}} bei Zeile {i+1}")
                break
        
        if doc_start == -1:
            print(f"   ❌ Keine \\begin{{document}} gefunden!")
            return False
        
        # First, find and extract \title
        title_content = None
        title_index = -1
        for idx, line in enumerate(lines):
            title_match = re.search(r'\\title\{(.+?)\}', line)
            if title_match:
                title_content = title_match.group(1)
                title_index = idx
                print(f"   ✅ Titel gefunden: {title_content[:50]}...")
                break
        # Remove everything before \title
        if title_index > 0:
            lines = lines[title_index:]
        
        # Process from \begin{document} onwards
        new_lines = []

        # Insert date for en_standalone files if missing
        if 'en_standalone' in str(source_file) and not any(re.match(r'^\\date\{', l) for l in lines):
            new_lines.append('\\date{January 2025}')
            print(f"   🗓️  Datum für englische Standalone-Datei ergänzt.")

        # Add chapter from title
        if title_content:
            new_lines.append(f'\\chapter{{{title_content}}}')
            new_lines.append('')
            print(f"   ✅ \\title → \\chapter umgewandelt")
        
        i = doc_start + 1
        in_abstract = False
        abstract_content = []
        
        while i < len(lines):
            line = lines[i]
            
            # Skip \title (already processed)
            if re.match(r'^\s*\\title\{', line):
                i += 1
                continue
            
            # Skip \maketitle (not needed in book)
            if re.match(r'^\s*\\maketitle', line):
                i += 1
                continue
            
            # Start of abstract
            if re.match(r'^\s*\\begin\{abstract\}', line):
                in_abstract = True
                i += 1
                continue
            
            # End of abstract
            if re.match(r'^\s*\\end\{abstract\}', line):
                in_abstract = False
                # Add abstract as section*
                new_lines.append('\\section*{Abstract}')
                new_lines.extend(abstract_content)
                new_lines.append('')  # Empty line after abstract
                abstract_content = []
                i += 1
                print(f"   ✅ Abstract umgewandelt zu \\section*{{Abstract}}")
                continue
            
            # Collect abstract content
            if in_abstract:
                abstract_content.append(line)
                i += 1
                continue
            
            # Skip \tableofcontents
            if re.match(r'^\s*\\tableofcontents', line):
                i += 1
                continue
            
            # Skip \end{document}
            if re.match(r'^\s*\\end\{document\}', line):
                i += 1
                continue
            
            # Keep \section as is (title already converted to chapter)
            new_lines.append(line)
            i += 1
        
        # Write target file
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        print(f"   ✅ Erstellt: {target_file.name}")
        print(f"      Original: {len(lines)} Zeilen")
        print(f"      Neu: {len(new_lines)} Zeilen")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    base_dir = Path(r"C:\Users\johann\B18\2\tex-n")
    
    # Define mappings: (source_dir, target_dir, pattern)
    mappings = [
        ("de_standalone", "de_chapters_new", "*_De.tex"),
        ("en_standalone", "en_chapters_new", "*_En.tex"),
    ]
    
    print("=" * 80)
    print("KONVERTIERE ALLE DOKUMENTE >= 150 ZU CHAPTER-FORMAT")
    print("=" * 80)
    
    total_converted = 0
    total_failed = 0
    
    for source_dir, target_dir, pattern in mappings:
        print(f"\n\n{'='*80}")
        print(f"📁 {source_dir} → {target_dir}")
        print("="*80)
        
        source_path = base_dir / source_dir
        target_path = base_dir / target_dir
        
        # Find all files >= 150
        files = sorted(source_path.glob(pattern))
        files_150plus = []
        
        for f in files:
            match = re.match(r'^(\d{3})_', f.name)
            if match and int(match.group(1)) >= 150:
                files_150plus.append(f)
        
        print(f"Gefunden: {len(files_150plus)} Dateien >= 150")
        
        for source_file in files_150plus:
            # Determine target filename - always add _ch before .tex
            target_name = source_file.name
            
            if target_name.endswith("_De.tex"):
                # Change to _De_ch.tex
                target_name = target_name.replace("_De.tex", "_De_ch.tex")
            elif target_name.endswith("_En.tex"):
                # Change to _En_ch.tex
                target_name = target_name.replace("_En.tex", "_En_ch.tex")
            
            target_file = target_path / target_name
            
            # Convert
            if convert_standalone_to_chapter(source_file, target_file):
                total_converted += 1
            else:
                total_failed += 1
    
    print("\n" + "="*80)
    print("ZUSAMMENFASSUNG")
    print("="*80)
    print(f"✅ Erfolgreich konvertiert: {total_converted}")
    print(f"❌ Fehler: {total_failed}")
    print("="*80)


if __name__ == "__main__":
    main()
