#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final comprehensive fix for all remaining PDF reference issues.
Handles both German (De) and English (En) documents.
"""

import os
import re
from pathlib import Path

# Comprehensive mapping of partial names to full numbered names
FILENAME_MAPPINGS = {
    # Common mappings (works for both De and En)
    'T0_FineStructure': '011_T0_Feinstruktur',
    'T0_GravitationalConstant': '012_T0_Gravitationskonstante',
    'T0_ParticleMasses': '006_T0_Teilchenmassen',
    'T0_Teilchenmassen': '006_T0_Teilchenmassen',
    'T0_Neutrinos': '007_T0_Neutrinos',
    'T0_Cosmology': '025_T0_Kosmologie',
    'T0_Kosmologie': '025_T0_Kosmologie',
    'T0_QM-QFT-RT': '020_T0_QM-QFT-RT',
    'T0_Foundations': '003_T0_Grundlagen_v1',
    'T0_Fundamentals': '003_T0_Grundlagen_v1',
    'T0_Grundlagen': '003_T0_Grundlagen_v1',
    'T0_Basics': '003_T0_Grundlagen_v1',
    'T0_Anomalies': '018_T0_Anomale-g2-10',
    'T0_Anomale-g2-10': '018_T0_Anomale-g2-10',
    'HdokumentDe': '040_Hdokument',
    'Hdokument': '040_Hdokument',
    'Zusammenfassung': '081_Zusammenfassung',
    'T0-Energie': '010_T0_Energie',
    'T0_Energie': '010_T0_Energie',
    'cosmic': '063_cosmic',
    'DerivationVonBeta': '093_DerivationVonBeta',
    'xi_parameter_partikel': '008_T0_xi-und-e',
    'systemDe': '059_system',
    'system': '059_system',
    'T0vsESM_ConceptualAnalysis': '095_T0vsESM_ConceptualAnalysis',
    'QM-Detrmistic_p': '072_QM-Detrmistic_p',
    'scheinbar_instantan': '073_scheinbar_instantan',
    'QM-testen': '035_QM',
    'T0_xi_origin': '009_T0_xi_ursprung',
    'T0_gravitational_constant': '012_T0_Gravitationskonstante',
    'gravitational_constant': '045_gravitationskonstante',
    'T0_particle_masses': '006_T0_Teilchenmassen',
    'natural_units_systematics': '015_NatEinheitenSystematik',
    'fractal_correction_derivation': '133_fractal_correction_derivation',
    'T0_natural_SI': '014_T0_nat-si',
    'T0_energy': '010_T0_Energie',
    'T0_fine_structure': '011_T0_Feinstruktur',
    'parameter_derivation': '041_parameterherleitung',
    'fine_structure_constant': '044_feinstrukturkonstante',
    'unit_conventions_c_speed': '134_unit_conventions_c_speed',
    'circularity_constants': '101_circularity_constants',
    'FFGFT-torsion': '149_FFGFT-torsion',
    'FFGFT_donat-teil1': '145_FFGFT_donat-teil1',
}

def fix_pdf_references(file_path, lang_suffix):
    """Fix all PDF reference issues in a file."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    modified = False
    new_content = []
    
    for line_num, line in enumerate(content, 1):
        original_line = line
        
        # Skip URLs
        if re.search(r'\\url\{https?://', line):
            new_content.append(line)
            continue
        
        # Skip input lines
        if re.search(r'\\input\{', line):
            new_content.append(line)
            continue
        
        # Step 1: Add missing prefixes using mappings
        for partial, full in FILENAME_MAPPINGS.items():
            # Match pattern: word boundary, partial name, underscore or dash, language, .pdf
            pattern = rf'\b{re.escape(partial)}([_\-]?{lang_suffix}\.pdf)'
            if re.search(pattern, line):
                replacement = f'{full}\\1'
                line = re.sub(pattern, replacement, line)
        
        # Step 2: Escape all underscores in PDF names (but not in URLs)
        # Match: number_text_lang.pdf where underscores need escaping
        def escape_underscores(match):
            pdf_ref = match.group(0)
            # Escape underscores that aren't already escaped
            escaped = re.sub(r'(?<!\\)_', r'\\_', pdf_ref)
            return escaped
        
        # Find PDF references with language suffix
        line = re.sub(
            rf'\b[\w\-]+(?<!\\)_(?:[\w\-]+(?<!\\)_)*{lang_suffix}\.pdf\b',
            escape_underscores,
            line
        )
        
        if line != original_line:
            modified = True
        
        new_content.append(line)
    
    if modified:
        # Backup
        backup_path = str(file_path) + '.bak_final'
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
        (Path(r'C:\Users\johann\B18\2\tex-n\de_standalone'), 'De'),
        (Path(r'C:\Users\johann\B18\2\tex-n\en_standalone'), 'En'),
    ]
    
    total_fixed = 0
    
    for base_dir, lang in directories:
        if not base_dir.exists():
            print(f"ERROR: Directory not found: {base_dir}")
            continue
        
        print(f"\n{'='*80}")
        print(f"Processing {lang} documents: {base_dir}")
        print(f"{'='*80}\n")
        
        tex_files = sorted(base_dir.glob('*.tex'))
        fixed_count = 0
        
        for tex_file in tex_files:
            if fix_pdf_references(tex_file, lang):
                fixed_count += 1
                print(f"Fixed: {tex_file.name}")
        
        print(f"\nFixed {fixed_count} {lang} files")
        total_fixed += fixed_count
    
    print(f"\n{'='*80}")
    print(f"TOTAL: Fixed {total_fixed} files across all languages")
    print(f"Backups saved as *.tex.bak_final")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
