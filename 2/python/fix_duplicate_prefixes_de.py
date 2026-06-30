#!/usr/bin/env python3
"""
Remove duplicate prefix numbers in German standalone documents.
Converts patterns like 018\_018\_ to 018\_
"""

import os
import re

def fix_duplicate_prefixes(file_path):
    """Remove duplicate prefix numbers."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Find and replace patterns like 018\_018\_ with 018\_
        # Use a loop to handle potential triple/quadruple duplicates
        changed = True
        iterations = 0
        max_iterations = 10
        
        while changed and iterations < max_iterations:
            new_content = content
            
            # Pattern: 123\_123\_ -> 123\_
            # Look for three digits followed by \_ followed by the same three digits and \_
            pattern = r'(\d{3})\\_\1\\_'
            new_content = re.sub(pattern, r'\1\\_', new_content)
            
            if new_content == content:
                changed = False
            else:
                content = new_content
                iterations += 1
        
        if content != original_content:
            # Create backup
            backup_path = file_path + '.bak_dedup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Write fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Count how many fixes were made
            original_matches = len(re.findall(r'(\d{3})\\_\1\\_', original_content))
            remaining_matches = len(re.findall(r'(\d{3})\\_\1\\_', content))
            
            return original_matches - remaining_matches
        
        return 0
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def main():
    de_dir = r'C:\Users\johann\B18\2\tex-n\de_standalone'
    
    if not os.path.exists(de_dir):
        print(f"Directory not found: {de_dir}")
        return
    
    print("=" * 80)
    print("Removing duplicate prefix numbers (DE)")
    print("=" * 80)
    
    total_fixed = 0
    files_fixed = 0
    
    for filename in sorted(os.listdir(de_dir)):
        if not filename.endswith('.tex'):
            continue
        
        file_path = os.path.join(de_dir, filename)
        fixes = fix_duplicate_prefixes(file_path)
        
        if fixes > 0:
            files_fixed += 1
            total_fixed += fixes
            print(f"✓ {filename}: {fixes} doppelte Präfixe entfernt")
    
    print("\n" + "=" * 80)
    print(f"Dateien korrigiert: {files_fixed}")
    print(f"Gesamt entfernte Duplikate: {total_fixed}")
    print("=" * 80)

if __name__ == '__main__':
    main()
