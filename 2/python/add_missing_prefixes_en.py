#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add missing number prefixes to PDF references in English files.
"""

import re
from pathlib import Path

# Mapping of names without prefix to correct prefixed names
REPLACEMENTS = {
    'T0\\_FineStructure\\_En.pdf': '011\\_T0\\_Feinstruktur\\_En.pdf',
    'T0\\_GravitationalConstant\\_En.pdf': '012\\_T0\\_Gravitationskonstante\\_En.pdf',
    'T0\\_ParticleMasses\\_En.pdf': '006\\_T0\\_Teilchenmassen\\_En.pdf',
    'T0\\_Neutrinos\\_En.pdf': '007\\_T0\\_Neutrinos\\_En.pdf',
    'T0\\_Cosmology\\_En.pdf': '025\\_T0\\_Kosmologie\\_En.pdf',
    'T0\\_Foundations\\_En.pdf': '003\\_T0\\_Grundlagen\\_v1\\_En.pdf',
    'T0\\_Fundamentals\\_En.pdf': '003\\_T0\\_Grundlagen\\_v1\\_En.pdf',
    'T0\\_Anomalies\\_En.pdf': '018\\_T0\\_Anomale-g2-10\\_En.pdf',
    
    # Without escapes (for initial pass)
    'T0_FineStructure_En.pdf': '011_T0_Feinstruktur_En.pdf',
    'T0_GravitationalConstant_En.pdf': '012_T0_Gravitationskonstante_En.pdf',
    'T0_ParticleMasses_En.pdf': '006_T0_Teilchenmassen_En.pdf',
    'T0_Neutrinos_En.pdf': '007_T0_Neutrinos_En.pdf',
    'T0_Cosmology_En.pdf': '025_T0_Kosmologie_En.pdf',
    'T0_Foundations_En.pdf': '003_T0_Grundlagen_v1_En.pdf',
    'T0_Fundamentals_En.pdf': '003_T0_Grundlagen_v1_En.pdf',
    'T0_Anomalies_En.pdf': '018_T0_Anomale-g2-10_En.pdf',
    
    # German files
    'HdokumentDe.pdf': '040_Hdokument_De.pdf',
    'Zusammenfassung\\_De.pdf': '081\\_Zusammenfassung\\_De.pdf',
    'T0-Energie\\_De.pdf': '010\\_T0\\_Energie\\_De.pdf',
    'cosmic\\_De.pdf': '063\\_cosmic\\_De.pdf',
    'DerivationVonBetaDe.pdf': '093_DerivationVonBeta_De.pdf',
    'xi\\_parameter\\_partikel\\_De.pdf': '008\\_T0\\_xi-und-e\\_De.pdf',
    'systemDe.pdf': '059_system_De.pdf',
    'T0vsESM\\_ConceptualAnalysis\\_De.pdf': '095\\_T0vsESM\\_ConceptualAnalysis\\_De.pdf',
    'QM-Detrmistic\\_p\\_De.pdf': '072\\_QM-Detrmistic\\_p\\_De.pdf',
    'scheinbar\\_instantan\\_De.pdf': '073\\_scheinbar\\_instantan\\_De.pdf',
    'QM-testenDe.pdf': '035_QM_De.pdf',
}

def fix_file(file_path):
    """Replace PDF names without prefixes."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False
    
    # Skip URLs
    if '\\url{https' in content:
        # Don't process URLs
        pass
    
    for old_name, new_name in REPLACEMENTS.items():
        if old_name in content:
            content = content.replace(old_name, new_name)
            modified = True
            print(f"  {file_path.name}: {old_name} -> {new_name}")
    
    if modified:
        # Backup
        backup_path = str(file_path) + '.bak_prefix'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Write
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    return False

def main():
    base_dir = Path(r'C:\Users\johann\B18\2\tex-n\en_standalone')
    
    print(f"Processing English standalone documents...\n")
    
    tex_files = sorted(base_dir.glob('*.tex'))
    fixed_count = 0
    
    for tex_file in tex_files:
        if fix_file(tex_file):
            fixed_count += 1
    
    print(f"\n{'='*80}")
    print(f"Fixed {fixed_count} files")
    print(f"Backups saved as *.tex.bak_prefix")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
