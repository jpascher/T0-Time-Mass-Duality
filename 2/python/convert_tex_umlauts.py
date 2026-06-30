#!/usr/bin/env python3
"""
Convert TeX umlauts to UTF-8 in all LaTeX files
Converts: \"a → ä, \"o → ö, \"u → ü, \"A → Ä, \"O → Ö, \"U → Ü, \ss → ß
"""

import os
import re
from pathlib import Path
import shutil

def convert_tex_umlauts(content):
    """Convert TeX umlauts to UTF-8"""
    
    # Define replacements (order matters!)
    # Format: (find_string, replace_string)
    replacements = [
        ('{\\"a}', 'ä'),
        ('{\\"o}', 'ö'),
        ('{\\"u}', 'ü'),
        ('{\\"A}', 'Ä'),
        ('{\\"O}', 'Ö'),
        ('{\\"U}', 'Ü'),
        ('\\"a', 'ä'),
        ('\\"o', 'ö'),
        ('\\"u', 'ü'),
        ('\\"A', 'Ä'),
        ('\\"O', 'Ö'),
        ('\\"U', 'Ü'),
        ('{\\"a}', 'ä'),
        ('{\\ss}', 'ß'),
        ('\\ss', 'ß'),
        ('f\\"u', 'für'),
        ('f\\"a', 'fär'),  # falls es vorkommt
        ('f\\"o', 'för'),  # falls es vorkommt
    ]
    
    modified = False
    for find_str, replace_str in replacements:
        if find_str in content:
            content = content.replace(find_str, replace_str)
            modified = True
    
    return content, modified

def process_file(file_path):
    """Process a single LaTeX file"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, modified = convert_tex_umlauts(content)
        
        if modified:
            # Create backup
            backup_path = file_path.with_suffix('.tex.bak_umlaut_conversion')
            shutil.copy2(file_path, backup_path)
            
            # Write modified file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        
        return False
        
    except Exception as e:
        print(f"ERROR processing {file_path.name}: {e}")
        return False

def main():
    base_dir = Path(r"C:\Users\johann\B18\2\tex-n")
    
    directories = [
        base_dir / "de_standalone",
        base_dir / "en_standalone",
        base_dir / "de_chapters_new",
        base_dir / "en_chapters_new"
    ]
    
    print("=" * 80)
    print("KONVERTIERE TEX-UMLAUTE ZU UTF-8")
    print("=" * 80)
    
    total_files = 0
    modified_files = 0
    
    for directory in directories:
        print(f"\nDirectory: {directory.name}")
        
        tex_files = sorted(directory.glob("*.tex"))
        dir_modified = 0
        
        for tex_file in tex_files:
            total_files += 1
            if process_file(tex_file):
                dir_modified += 1
                modified_files += 1
                print(f"  Fixed: {tex_file.name}")
        
        if dir_modified == 0:
            print(f"  OK: No TeX umlauts found")
        else:
            print(f"  Modified: {dir_modified} files")
    
    print("\n" + "="*80)
    print("ZUSAMMENFASSUNG")
    print("="*80)
    print(f"Geprüft: {total_files} Dateien")
    print(f"Modifiziert: {modified_files} Dateien")
    print(f"Backups: {modified_files} (.bak_umlaut_conversion)")
    print("="*80)

if __name__ == "__main__":
    main()
