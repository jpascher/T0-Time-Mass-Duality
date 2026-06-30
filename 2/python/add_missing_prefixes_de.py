#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add missing number prefixes to PDF references in German files.
"""

import re
from pathlib import Path

# Mapping of names without prefix to correct prefixed names  
REPLACEMENTS = {
    # German files - escaped versions
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
    'QM-testen\\_De.pdf': '035\\_QM\\_De.pdf',
    'FFGFT-torsion\\_De.pdf': '149\\_FFGFT-torsion\\_De.pdf',
    'T0\\_Anomale-g2-10\\_De.pdf': '018\\_T0\\_Anomale-g2-10\\_De.pdf',
    'FFGFT\\_donat-teil1\\_De.pdf': '145\\_FFGFT\\_donat-teil1\\_De.pdf',
}

def fix_file(file_path):
    """Replace PDF names without prefixes."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False
    
    for old_name, new_name in REPLACEMENTS.items():
        if old_name in content:
            content = content.replace(old_name, new_name)
            modified = True
            print(f"  {file_path.name}: {old_name} -> {new_name}")
    
    if modified:
        # Backup
        backup_path = str(file_path) + '.bak_prefix_de'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Write
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    return False

def main():
    base_dir = Path(r'C:\Users\johann\B18\2\tex-n\de_standalone')
    
    print(f"Processing German standalone documents...\n")
    
    tex_files = sorted(base_dir.glob('*.tex'))
    fixed_count = 0
    
    for tex_file in tex_files:
        if fix_file(tex_file):
            fixed_count += 1
    
    print(f"\n{'='*80}")
    print(f"Fixed {fixed_count} files")
    print(f"Backups saved as *.tex.bak_prefix_de")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
