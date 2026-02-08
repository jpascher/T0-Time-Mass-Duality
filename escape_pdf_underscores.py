#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Escape all underscores in PDF filenames with backslash.
Example: 040_Hdokument_De.pdf -> 040\\_Hdokument\\_De.pdf
BUT: Skip URLs and lines already properly escaped
"""

import os
import re
from pathlib import Path

def escape_pdf_underscores(file_path):
    """Escape underscores in PDF references."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    modified = False
    new_content = []
    
    for line_num, line in enumerate(content, 1):
        original_line = line
        
        # Skip URLs - don't modify external links
        if re.search(r'\\url\{https?://', line):
            new_content.append(line)
            continue
        
        # Pattern: Find PDF filenames with unescaped underscores
        # Match: word_characters.pdf but NOT word\_characters.pdf
        # Look for underscores NOT preceded by backslash
        def replace_underscores(match):
            pdf_name = match.group(0)
            # Replace all underscores that are NOT already escaped
            escaped = re.sub(r'(?<!\\)_', r'\\_', pdf_name)
            return escaped
        
        # Match PDF filenames: digits/letters/hyphens followed by _De.pdf or _En.pdf
        # But only replace if underscores are not already escaped
        line = re.sub(r'\b[\w\-]+(?<!\\)_(?:[\w\-]+(?<!\\)_)*(?:De|En)\.pdf\b', 
                      replace_underscores, line)
        
        if line != original_line:
            modified = True
            try:
                print(f"  Line {line_num}: {original_line.strip()[:80]}")
                print(f"        -> {line.strip()[:80]}")
            except UnicodeEncodeError:
                print(f"  Line {line_num}: <contains special characters>")
        
        new_content.append(line)
    
    if modified:
        # Backup original
        backup_path = str(file_path) + '.bak6'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.writelines(content)
        
        # Write fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_content)
        
        return True
    
    return False

def main():
    base_dir = Path(r'C:\Users\johann\B18\2\tex-n\de_standalone')
    
    if not base_dir.exists():
        print(f"ERROR: Directory not found: {base_dir}")
        return
    
    tex_files = sorted(base_dir.glob('*.tex'))
    print(f"Found {len(tex_files)} .tex files\n")
    
    fixed_count = 0
    
    for tex_file in tex_files:
        if escape_pdf_underscores(tex_file):
            fixed_count += 1
            print(f"Fixed: {tex_file.name}\n")
    
    print(f"\n{'='*80}")
    print(f"SUMMARY: Escaped underscores in {fixed_count} files")
    print(f"Backups saved as *.tex.bak6")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
