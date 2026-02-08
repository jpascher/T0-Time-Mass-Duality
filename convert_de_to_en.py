#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert all De.pdf references to En.pdf in English documents.
"""

import re
from pathlib import Path

def convert_de_to_en(file_path):
    """Convert _De.pdf to _En.pdf in English documents."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Skip URLs - don't change external links
    lines = content.split('\n')
    new_lines = []
    modified = False
    
    for line in lines:
        if '\\url{http' in line:
            # Don't modify URLs
            new_lines.append(line)
        else:
            # Replace _De.pdf with _En.pdf
            new_line = re.sub(r'_De\.pdf', r'_En.pdf', line)
            # Replace \_De.pdf with \_En.pdf (escaped version)
            new_line = re.sub(r'\\_De\\.pdf', r'\\_En.pdf', new_line)
            
            if new_line != line:
                modified = True
            new_lines.append(new_line)
    
    if modified:
        content = '\n'.join(new_lines)
        
        # Backup
        backup_path = str(file_path) + '.bak_de_to_en'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Write
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    return False

def main():
    base_dir = Path(r'C:\Users\johann\B18\2\tex-n\en_standalone')
    
    print(f"Converting De.pdf to En.pdf in English documents...\n")
    
    tex_files = sorted(base_dir.glob('*.tex'))
    fixed_count = 0
    changes_count = 0
    
    for tex_file in tex_files:
        # Count changes before
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
        before = content.count('_De.pdf') + content.count('\\_De.pdf')
        
        if convert_de_to_en(tex_file):
            with open(tex_file, 'r', encoding='utf-8') as f:
                new_content = f.read()
            after_de = new_content.count('_De.pdf') + new_content.count('\\_De.pdf')
            after_en = new_content.count('_En.pdf') + new_content.count('\\_En.pdf')
            
            changed = before - after_de
            changes_count += changed
            fixed_count += 1
            print(f"{tex_file.name}: {changed} references converted")
    
    print(f"\n{'='*80}")
    print(f"Fixed {fixed_count} files")
    print(f"Total {changes_count} references converted from _De.pdf to _En.pdf")
    print(f"Backups saved as *.tex.bak_de_to_en")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
