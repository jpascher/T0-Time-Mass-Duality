#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple string replacement for all missing prefixes.
"""

from pathlib import Path

# Simple string mappings
REPLACEMENTS_EN = {
    'T0_Casimir_Effekt_En.pdf': '091_Casimir_En.pdf',
    'T0\\_Casimir\\_Effekt\\_En.pdf': '091\\_Casimir\\_En.pdf',
    'T0_Alpha_Xi_En.pdf': '087_137_En.pdf',
    'T0\\_Alpha\\_Xi\\_En.pdf': '087\\_137\\_En.pdf',
    'T0_G_from_Xi_En.pdf': '045_gravitationskonstante_En.pdf',
    'T0\\_G\\_from\\_Xi\\_En.pdf': '045\\_gravitationskonstante\\_En.pdf',
    'FFGFT_Narrative_Master_En.pdf': '145_FFGFT_donat-teil1_En.pdf',
    'FFGFT\\_Narrative\\_Master\\_En.pdf': '145\\_FFGFT\\_donat-teil1\\_En.pdf',
    'T0_FieldEquation_En.pdf': '019_T0_lagrndian_En.pdf',
    'T0\\_FieldEquation\\_En.pdf': '019\\_T0\\_lagrndian\\_En.pdf',
    'T0_QM-QFT-GR_En.pdf': '020_T0_QM-QFT-RT_En.pdf',
    'T0\\_QM-QFT-GR\\_En.pdf': '020\\_T0\\_QM-QFT-RT\\_En.pdf',
    'T0_Redshift_Analysis_En.pdf': '061_TempEinheitenCMB_En.pdf',
    'T0\\_Redshift\\_Analysis\\_En.pdf': '061\\_TempEinheitenCMB\\_En.pdf',
    'T0_Framework_En.pdf': '040_Hdokument_En.pdf',
    'T0\\_Framework\\_En.pdf': '040\\_Hdokument\\_En.pdf',
    'T0_Numerics_Implementation_En.pdf': '114_T0_freqeunz_En.pdf',
    'T0\\_Numerics\\_Implementation\\_En.pdf': '114\\_T0\\_freqeunz\\_En.pdf',
    'T0_Cosmology_En.pdf': '025_T0_Kosmologie_En.pdf',
    'T0\\_Cosmology\\_En.pdf': '025\\_T0\\_Kosmologie\\_En.pdf',
    'Bell-Teil2_En.pdf': '023a_Bell-Teil2_En.pdf',
    'Bell-Teil2\\_En.pdf': '023a\\_Bell-Teil2\\_En.pdf',
    'T0_Anomale-g2-10_En.pdf': '018_T0_Anomale-g2-10_En.pdf',
    'T0\\_Anomale-g2-10\\_En.pdf': '018\\_T0\\_Anomale-g2-10\\_En.pdf',
}

REPLACEMENTS_DE = {
    'T0_Kosmologie.pdf': '025_T0_Kosmologie_De.pdf',
    'T0\\_Kosmologie.pdf': '025\\_T0\\_Kosmologie_De.pdf',
}

def fix_file(file_path, replacements):
    """Apply string replacements."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False
    changes = []
    
    for old, new in replacements.items():
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            modified = True
            changes.append(f"{old} -> {new} ({count}x)")
    
    if modified:
        # Backup
        backup_path = str(file_path) + '.bak_simple'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Write
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if changes:
            print(f"\n{file_path.name}:")
            for change in changes:
                print(f"  {change}")
        
        return True
    
    return False

def main():
    base_en = Path(r'C:\Users\johann\B18\2\tex-n\en_standalone')
    base_de = Path(r'C:\Users\johann\B18\2\tex-n\de_standalone')
    
    print("Processing English documents...")
    print("="*80)
    
    en_fixed = 0
    for tex_file in sorted(base_en.glob('*.tex')):
        if fix_file(tex_file, REPLACEMENTS_EN):
            en_fixed += 1
    
    print(f"\nFixed {en_fixed} English files\n")
    
    print("Processing German documents...")
    print("="*80)
    
    de_fixed = 0
    for tex_file in sorted(base_de.glob('*.tex')):
        if fix_file(tex_file, REPLACEMENTS_DE):
            de_fixed += 1
    
    print(f"\nFixed {de_fixed} German files\n")
    
    print("="*80)
    print(f"TOTAL: {en_fixed + de_fixed} files fixed")
    print("="*80)

if __name__ == '__main__':
    main()
