#!/usr/bin/env python3
"""
Fix duplicate number prefixes in PDF references.
Example: 040_040_040_Hdokument_De.pdf -> 040_Hdokument_De.pdf
"""

import os
import re
from pathlib import Path

def fix_duplicate_prefixes(file_path):
    """Remove duplicate prefixes from PDF references."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    modified = False
    new_content = []
    
    for line in content:
        original_line = line
        
        # Generic pattern to remove duplicate prefixes with various escape combinations
        # Match: 3 digits, optional backslashes+underscore, same 3 digits, underscore
        # Replace all variations
        
        # Try all common patterns iteratively until no more matches
        changed = True
        while changed:
            new_line = line
            
            # Pattern 1: 011\\\\_011\\_ -> 011\\_
            new_line = re.sub(r'(\d{3})\\\\_(\1)\\_', r'\1\\_', new_line)
            
            # Pattern 2: 011\\\\_011\\\\_  -> 011\\_
            new_line = re.sub(r'(\d{3})\\\\_(\1)\\\\_', r'\1\\_', new_line)
            
            # Pattern 3: 011_011_ -> 011_
            new_line = re.sub(r'(\d{3})_(\1)_', r'\1_', new_line)
            
            changed = (new_line != line)
            line = new_line
        
        if line != original_line:
            modified = True
            try:
                print(f"  Fixed: {original_line.strip()[:100]}")
                print(f"     -> {line.strip()[:100]}")
            except UnicodeEncodeError:
                print(f"  Fixed line {len(new_content)}")
        
        new_content.append(line)
    
    if modified:
        # Backup original
        backup_path = str(file_path) + '.bak8'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.writelines(content)
        
        # Write fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_content)
        
        return True
    
    return False

def main():
    # Process both German and English directories
    directories = [
        Path(r'C:\Users\johann\B18\2\tex-n\de_standalone'),
        Path(r'C:\Users\johann\B18\2\tex-n\en_standalone'),
    ]
    
    total_fixed = 0
    
    for base_dir in directories:
        if not base_dir.exists():
            print(f"ERROR: Directory not found: {base_dir}")
            continue
        
        print(f"\n{'='*80}")
        print(f"Processing: {base_dir}")
        print(f"{'='*80}\n")
        
        tex_files = sorted(base_dir.glob('*.tex'))
        print(f"Found {len(tex_files)} .tex files\n")
        
        fixed_count = 0
        
        for tex_file in tex_files:
            if fix_duplicate_prefixes(tex_file):
                fixed_count += 1
                print(f"Fixed: {tex_file.name}\n")
        
        print(f"Fixed {fixed_count} files in {base_dir.name}")
        total_fixed += fixed_count
    
    print(f"\n{'='*80}")
    print(f"TOTAL: Fixed {total_fixed} files")
    print(f"Backups saved as *.tex.bak8")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
