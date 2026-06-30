#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive fix: Add ALL missing prefixes to PDF references.
Processes both German and English documents.
"""

import re
from pathlib import Path

# Comprehensive mapping - all known PDF files with their correct prefixes
COMPREHENSIVE_MAPPINGS = {
    # Common files (works for both De and En)
    'T0\\_Casimir\\_Effekt': '091\\_Casimir',
    'T0_Casimir_Effekt': '091_Casimir',
    'T0\\_Alpha\\_Xi': '087\\_137',
    'T0_Alpha_Xi': '087_137',
    'T0\\_G\\_from\\_Xi': '045\\_gravitationskonstante',
    'T0_G_from_Xi': '045_gravitationskonstante',
    'FFGFT\\_Narrative\\_Master': '145\\_FFGFT\\_donat-teil1',
    'FFGFT_Narrative_Master': '145_FFGFT_donat-teil1',
    'T0\\_FieldEquation': '019\\_T0\\_lagrndian',
    'T0_FieldEquation': '019_T0_lagrndian',
    'T0\\_QM-QFT-GR': '020\\_T0\\_QM-QFT-RT',
    'T0_QM-QFT-GR': '020_T0_QM-QFT-RT',
    'T0\\_Redshift\\_Analysis': '061\\_TempEinheitenCMB',
    'T0_Redshift_Analysis': '061_TempEinheitenCMB',
    'T0\\_Framework': '040\\_Hdokument',
    'T0_Framework': '040_Hdokument',
    'T0\\_Numerics\\_Implementation': '114\\_T0\\_freqeunz',
    'T0_Numerics_Implementation': '114_T0_freqeunz',
    'T0\\_Kosmologie': '025\\_T0\\_Kosmologie',
    'T0_Kosmologie': '025_T0_Kosmologie',
    'Bell-Teil2': '023a\\_Bell-Teil2',
    'T0\\_Anomale-g2-10': '018\\_T0\\_Anomale-g2-10',
    'T0_Anomale-g2-10': '018_T0_Anomale-g2-10',
    'FFGFT\\_donat-teil1': '145\\_FFGFT\\_donat-teil1',
    'FFGFT_donat-teil1': '145_FFGFT_donat-teil1',
}

def fix_file(file_path, lang_suffix):
    """Add missing prefixes to PDF references."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False
    changes = []
    
    # Process line by line to skip URLs
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        # Skip URLs
        if '\\url{http' in line or '% Filename:' in line or '\\input{' in line:
            new_lines.append(line)
            continue
        
        original_line = line
        
        # Apply all mappings
        for partial, full in COMPREHENSIVE_MAPPINGS.items():
            # Create patterns for this language
            # Pattern 1: partial_Lang.pdf -> full_Lang.pdf
            pattern = f'{partial}_{lang_suffix}\\.pdf'
            replacement = f'{full}_{lang_suffix}.pdf'
            if re.search(pattern, line):
                line = re.sub(pattern, replacement, line)
                if line != original_line:
                    changes.append(f"{partial}_{lang_suffix}.pdf -> {full}_{lang_suffix}.pdf")
                    modified = True
                    original_line = line
        
        new_lines.append(line)
    
    if modified:
        content = '\n'.join(new_lines)
        
        # Backup
        backup_path = str(file_path) + '.bak_comprehensive'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Write
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, changes
    
    return False, []

def main():
    directories = [
        (Path(r'C:\Users\johann\B18\2\tex-n\de_standalone'), 'De'),
        (Path(r'C:\Users\johann\B18\2\tex-n\en_standalone'), 'En'),
    ]
    
    total_fixed = 0
    total_changes = 0
    
    for base_dir, lang in directories:
        if not base_dir.exists():
            print(f"ERROR: Directory not found: {base_dir}")
            continue
        
        print(f"\n{'='*80}")
        print(f"Processing {lang} documents: {base_dir.name}")
        print(f"{'='*80}\n")
        
        tex_files = sorted(base_dir.glob('*.tex'))
        fixed_count = 0
        
        for tex_file in tex_files:
            was_fixed, changes = fix_file(tex_file, lang)
            if was_fixed:
                fixed_count += 1
                total_changes += len(changes)
                print(f"{tex_file.name}: {len(changes)} changes")
        
        print(f"\nFixed {fixed_count} {lang} files")
        total_fixed += fixed_count
    
    print(f"\n{'='*80}")
    print(f"TOTAL: Fixed {total_fixed} files with {total_changes} changes")
    print(f"Backups saved as *.tex.bak_comprehensive")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
