#!/usr/bin/env python3
import os
import re
from pathlib import Path

def convert_standalone_to_chapter(source_file, target_file):
    print(f"\n📖 Konvertiere: {source_file.name}")
    try:
        if os.path.exists(target_file):
            with open(source_file, 'r', encoding='utf-8') as f:
                src_content = f.read()
            with open(target_file, 'r', encoding='utf-8') as f:
                tgt_content = f.read()
            def detect_lang(text):
                if re.search(r'\\usepackage\[ngerman\]', text) or re.search(r'\\selectlanguage\{german\}', text):
                    return 'de'
                if re.search(r'\\usepackage\[english\]', text) or re.search(r'\\selectlanguage\{english\}', text):
                    return 'en'
                return None
            src_lang = detect_lang(src_content)
            tgt_lang = detect_lang(tgt_content)
            if src_lang == tgt_lang:
                print(f"   ⚠️  Zieldatei existiert bereits, überspringe.")
                return True
            else:
                print(f"   ⚠️  Zieldatei existiert, wird überschrieben.")
        
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        
        # Extrahiere Titel ZUERST (vor \begin{document})
        title_text = None
        title_start = -1
        for i, line in enumerate(lines):
            if '\\title{' in line:
                title_start = i
                break
        
        if title_start >= 0:
            # Sammle mehrzeiligen Titel
            title_lines = []
            brace_count = 0
            for i in range(title_start, len(lines)):
                line = lines[i]
                title_lines.append(line)
                brace_count += line.count('{') - line.count('}')
                if brace_count == 0 and '\\title{' in ''.join(title_lines):
                    break
            
            # Entferne \title{ und }
            title_full = '\n'.join(title_lines)
            title_full = re.sub(r'\\title\{', '', title_full, 1)
            title_full = title_full.rstrip()
            if title_full.endswith('}'):
                title_full = title_full[:-1]
            title_text = title_full
        
        # Finde \begin{document}
        doc_start = -1
        for i, line in enumerate(lines):
            if '\\begin{document}' in line:
                doc_start = i
                break
        
        if doc_start < 0:
            print(f"   ❌ Kein \\begin{{document}} gefunden")
            return False
        
        # Starte Ausgabe
        output_lines = []
        
        # Füge Chapter hinzu (aus Titel)
        if title_text:
            output_lines.append(f'\\chapter{{{title_text}}}')
            output_lines.append('')
        
        # Verarbeite ab \begin{document}
        i = doc_start + 1
        in_abstract = False
        abstract_lines = []
        
        while i < len(lines):
            line = lines[i]
            
            # \end{document} - Ende
            if '\\end{document}' in line:
                break
            
            # \maketitle entfernen
            if '\\maketitle' in line:
                i += 1
                continue
            
            # \tableofcontents entfernen
            if '\\tableofcontents' in line:
                i += 1
                continue
            
            # Abstract Start
            if '\\begin{abstract}' in line:
                in_abstract = True
                abstract_lines = []
                i += 1
                continue
            
            # Abstract Ende
            if '\\end{abstract}' in line:
                in_abstract = False
                output_lines.append('\\section*{Abstract}')
                output_lines.extend(abstract_lines)
                output_lines.append('')
                i += 1
                continue
            
            # Sammle Abstract-Inhalt
            if in_abstract:
                abstract_lines.append(line)
                i += 1
                continue
            
            # Normale Zeile
            output_lines.append(line)
            i += 1
        
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))
        
        print(f"   ✅ Erstellt: {target_file.name}")
        return True
        
    except Exception as e:
        print(f"   ❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    base_dir = Path(r"C:\Users\johann\B18\2\tex-n")
    mappings = [
        ("de_standalone", "de_chapters_new", "*_De.tex"),
        ("en_standalone", "en_chapters_new", "*_En.tex"),
    ]
    total_converted = 0
    total_failed = 0
    
    for source_dir, target_dir, pattern in mappings:
        print(f"\n{'='*80}")
        print(f"📁 {source_dir} → {target_dir}")
        source_path = base_dir / source_dir
        target_path = base_dir / target_dir
        
        if not source_path.exists():
            print(f"⚠️  Quellverzeichnis nicht gefunden: {source_path}")
            continue
        
        files = sorted(source_path.glob(pattern))
        print(f"Gefunden: {len(files)} Dateien")
        
        for source_file in files:
            target_name = source_file.name
            if target_name.endswith("_De.tex"):
                target_name = target_name.replace("_De.tex", "_De_ch.tex")
            elif target_name.endswith("_En.tex"):
                target_name = target_name.replace("_En.tex", "_En_ch.tex")
            
            target_file = target_path / target_name
            
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