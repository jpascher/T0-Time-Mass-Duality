#!/usr/bin/env python3
import os
import re
import shutil
from datetime import datetime

def rename_and_fix_urls():
    # Backup directory
    backup_dir = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(backup_dir, exist_ok=True)
    
    # Files that need "En" added before .pdf
    files_to_rename = {
        'Ho_Energie.tex': 'Ho_EnergieEn.tex',
        'Ho_Energie.pdf': 'Ho_EnergieEn.pdf',
        # Add more mappings if needed
    }
    
    # First, backup and rename files
    print("Step 1: Renaming files without 'En'...")
    for old_name, new_name in files_to_rename.items():
        if os.path.exists(old_name):
            shutil.copy2(old_name, os.path.join(backup_dir, old_name))
            os.rename(old_name, new_name)
            print(f"  ✓ Renamed {old_name} → {new_name}")
    
    # Get all .tex files
    tex_files = [f for f in os.listdir('.') if f.endswith('.tex')]
    
    print("\nStep 2: Fixing URLs in .tex files...")
    
    # URL patterns to fix
    url_fixes = [
        # Remove /English/ subdirectory
        (r'(https://github\.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf)/English/([^}]+)', r'\1/\2'),
        # Fix jpascher.github.io to github.com
        (r'https://jpascher\.github\.io/T0-Time-Mass-Duality/2/pdf/([^}]+)', 
         r'https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/\1'),
        # Fix specific filenames to include "En"
        (r'(https://[^}]+/)(Ho_Energie)(\.pdf)', r'\1\2En\3'),
        # Add more specific filename fixes as needed
    ]
    
    # Process each .tex file
    for tex_file in tex_files:
        print(f"  Processing: {tex_file}")
        
        # Backup
        shutil.copy2(tex_file, os.path.join(backup_dir, tex_file))
        
        # Read and fix
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for pattern, replacement in url_fixes:
            content = re.sub(pattern, replacement, content)
        
        # Write back if changed
        if content != original_content:
            with open(tex_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✓ Fixed URLs")
        else:
            print(f"    - No changes needed")
    
    print(f"\nBackup created in: {backup_dir}/")

if __name__ == "__main__":
    rename_and_fix_urls()