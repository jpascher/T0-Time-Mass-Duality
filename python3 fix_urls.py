#!/usr/bin/env python3
import os
import re
import shutil
from datetime import datetime

def fix_urls_in_tex_files():
    # Backup directory
    backup_dir = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Create backup directory
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Get all .tex files in current directory
    tex_files = [f for f in os.listdir('.') if f.endswith('.tex')]
    
    if not tex_files:
        print("No .tex files found in current directory!")
        return
    
    # URL patterns to fix
    patterns = [
        # Remove /English/ subdirectory
        (r'(https://github\.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf)/English/([^}]+)', r'\1/\2'),
        # Remove /pdf/English/ if it appears
        (r'(https://github\.com/jpascher/T0-Time-Mass-Duality/blob/main/2)/pdf/English/([^}]+)', r'\1/pdf/\2'),
        # Fix jpascher.github.io URLs to github.com
        (r'https://jpascher\.github\.io/T0-Time-Mass-Duality/2/pdf/([^}]+)', 
         r'https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/\1'),
    ]
    
    # Process each file
    for tex_file in tex_files:
        print(f"Processing: {tex_file}")
        
        # Create backup
        shutil.copy2(tex_file, os.path.join(backup_dir, tex_file))
        
        # Read file
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply fixes
        original_content = content
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)
        
        # Write back if changed
        if content != original_content:
            with open(tex_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed URLs in {tex_file}")
        else:
            print(f"  - No changes needed in {tex_file}")
    
    print(f"\nBackup created in: {backup_dir}/")
    print("Done!")

if __name__ == "__main__":
    fix_urls_in_tex_files()