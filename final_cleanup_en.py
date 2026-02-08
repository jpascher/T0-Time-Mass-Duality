#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final cleanup - add ALL missing prefixes to English documents.
"""

import re
from pathlib import Path

# Extended mapping for all remaining cases
REPLACEMENTS = {
    # QM/QFT documents
    'T0\\_QM-QFT-RT\\_En.pdf': '020\\_T0\\_QM-QFT-RT\\_En.pdf',
    'T0_QM-QFT-RT_En.pdf': '020_T0_QM-QFT-RT_En.pdf',
    
    # Basics/Fundamentals
    'T0\\_Basics\\_En.pdf': '003\\_T0\\_Grundlagen\\_v1\\_En.pdf',
    'T0_Basics_En.pdf': '003_T0_Grundlagen_v1_En.pdf',
    'T0\\_Grundlagen\\_En.pdf': '003\\_T0\\_Grundlagen\\_v1\\_En.pdf',
    'T0_Grundlagen_En.pdf': '003_T0_Grundlagen_v1_En.pdf',
    
    # Kosmologie
    'T0\\_Kosmologie\\_En.pdf': '025\\_T0\\_Kosmologie\\_En.pdf',
    'T0_Kosmologie_En.pdf': '025_T0_Kosmologie_En.pdf',
    
    # Anomalies/g-2
    'T0\\_Anomale-g2-9\\_En.pdf': '018\\_T0\\_Anomale-g2-10\\_En.pdf',
    'T0_Anomale-g2-9_En.pdf': '018_T0_Anomale-g2-10_En.pdf',
    'T0\\_g2-extension-4\\_En.pdf': '018\\_T0\\_Anomale-g2-10\\_En.pdf',
    'T0_g2-extension-4_En.pdf': '018_T0_Anomale-g2-10_En.pdf',
    
    # Extensions
    'T0\\_tm-extension-x6\\_En.pdf': '005\\_T0\\_tm-erweiterung-x6\\_En.pdf',
    'T0_tm-extension-x6_En.pdf': '005_T0_tm-erweiterung-x6_En.pdf',
    
    # Addendum
    'T0-QFT-ML\\_Addendum\\_En.pdf': '022\\_T0-QFT-ML\\_Addendum\\_En.pdf',
    'T0-QFT-ML_Addendum_En.pdf': '022_T0-QFT-ML_Addendum_En.pdf',
    
    # Cosmic/Redshift
    'redshift\\_deflection\\_En.pdf': '061\\_TempEinheitenCMB\\_En.pdf',
    'redshift_deflection_En.pdf': '061_TempEinheitenCMB_En.pdf',
    'cosmic\\_En.pdf': '063\\_cosmic\\_En.pdf',
    'cosmic_En.pdf': '063_cosmic_En.pdf',
}

def fix_file(file_path):
    """Replace PDF names without prefixes."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False
    changes = []
    
    for old_name, new_name in REPLACEMENTS.items():
        count = content.count(old_name)
        if count > 0:
            content = content.replace(old_name, new_name)
            modified = True
            changes.append(f"{old_name} -> {new_name} ({count}x)")
    
    if modified:
        # Backup
        backup_path = str(file_path) + '.bak_final_cleanup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Write
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n{file_path.name}:")
        for change in changes:
            print(f"  {change}")
        
        return True
    
    return False

def main():
    base_dir = Path(r'C:\Users\johann\B18\2\tex-n\en_standalone')
    
    print(f"Final cleanup - adding remaining prefixes...\n")
    print(f"{'='*80}\n")
    
    tex_files = sorted(base_dir.glob('*.tex'))
    fixed_count = 0
    total_changes = 0
    
    for tex_file in tex_files:
        if fix_file(tex_file):
            fixed_count += 1
    
    print(f"\n{'='*80}")
    print(f"Fixed {fixed_count} files")
    print(f"Backups saved as *.tex.bak_final_cleanup")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
