"""
Fix PDF references including LaTeX-escaped versions.
"""
import os
import re
from pathlib import Path
from collections import defaultdict
import shutil

def build_mapping_with_escapes():
    """Build mapping including LaTeX-escaped versions."""
    mapping = {
        # LaTeX-escaped versions (most common)
        'T0\\_Energie\\_De.pdf': '010_T0_Energie_De.pdf',
        'T0-Energie\\_De.pdf': '010_T0_Energie_De.pdf',
        'T0\\_Neutrinos\\_De.pdf': '007_T0_Neutrinos_De.pdf',
        'T0\\_Grundlagen\\_De.pdf': '003_T0_Grundlagen_v1_De.pdf',
        'T0\\_Feinstruktur\\_De.pdf': '011_T0_Feinstruktur_De.pdf',
        'T0\\_Gravitationskonstante\\_De.pdf': '012_T0_Gravitationskonstante_De.pdf',
        'T0\\_Teilchenmassen\\_De.pdf': '006_T0_Teilchenmassen_De.pdf',
        'Teilchenmassen\\_De.pdf': '006_T0_Teilchenmassen_De.pdf',
        '040\\_040\\_Hdokument\\_De.pdf': '040_Hdokument_De.pdf',
        '040\\_Hdokument\\_De.pdf': '040_Hdokument_De.pdf',
        'Hdokument\\_De.pdf': '040_Hdokument_De.pdf',
        'HdokumentDe.pdf': '040_Hdokument_De.pdf',
        '059\\_059\\_system\\_De.pdf': '059_system_De.pdf',
        '059\\_system\\_De.pdf': '059_system_De.pdf',
        'system\\_De.pdf': '059_system_De.pdf',
        'systemDe.pdf': '059_system_De.pdf',
        '039\\_039\\_Zwei-Dipole-CMB\\_De.pdf': '039_Zwei-Dipole-CMB_De.pdf',
        '039\\_Zwei-Dipole-CMB\\_De.pdf': '039_Zwei-Dipole-CMB_De.pdf',
        'Zwei-Dipole-CMB\\_De.pdf': '039_Zwei-Dipole-CMB_De.pdf',
        
        # More escaped versions
        'T0\\_Book\\_Abstract\\_De.pdf': '001_T0_Book_Abstract_De.pdf',
        'T0\\_Modell\\_Uebersicht\\_De.pdf': '004_T0_Modell_Uebersicht_De.pdf',
        'T0\\_tm-erweiterung-x6\\_De.pdf': '005_T0_tm-erweiterung-x6_De.pdf',
        'T0\\_xi-und-e\\_De.pdf': '008_T0_xi-und-e_De.pdf',
        'T0\\_SI\\_De.pdf': '013_T0_SI_De.pdf',
        'T0\\_nat-si\\_De.pdf': '014_T0_nat-si_De.pdf',
        'T0\\_QM-QFT-RT\\_De.pdf': '020_T0_QM-QFT-RT_De.pdf',
        'T0-QFT-ML\\_Addendum\\_De.pdf': '022_T0-QFT-ML_Addendum_De.pdf',
        'T0\\_7-fragen-3\\_De.pdf': '028_T0_7-fragen-3_De.pdf',
        'T0-Theory-vs-Synergetics\\_De.pdf': '033_T0-Theory-vs-Synergetics_De.pdf',
        'T0\\_QM-optimierung\\_De.pdf': '034_T0_QM-optimierung_De.pdf',
        'Bell\\_De.pdf': '023_Bell_De.pdf',
        'QM\\_De.pdf': '035_QM_De.pdf',
        'T0\\_Kosmologie\\_De.pdf': '025_T0_Kosmologie_De.pdf',
        'Casimir\\_De.pdf': '091_Casimir_De.pdf',
        'Zusammenfassung\\_De.pdf': '081_Zusammenfassung_De.pdf',
        
        # Non-escaped versions
        'T0_Energie_De.pdf': '010_T0_Energie_De.pdf',
        'T0-Energie_De.pdf': '010_T0_Energie_De.pdf',
        'T0_Neutrinos_De.pdf': '007_T0_Neutrinos_De.pdf',
        'T0_Grundlagen_De.pdf': '003_T0_Grundlagen_v1_De.pdf',
        'T0_Feinstruktur_De.pdf': '011_T0_Feinstruktur_De.pdf',
        'T0_Gravitationskonstante_De.pdf': '012_T0_Gravitationskonstante_De.pdf',
        'T0_Teilchenmassen_De.pdf': '006_T0_Teilchenmassen_De.pdf',
        'Hdokument_De.pdf': '040_Hdokument_De.pdf',
        'system_De.pdf': '059_system_De.pdf',
        'Zwei-Dipole-CMB_De.pdf': '039_Zwei-Dipole-CMB_De.pdf',
        'T0_Book_Abstract_De.pdf': '001_T0_Book_Abstract_De.pdf',
        'T0_Modell_Uebersicht_De.pdf': '004_T0_Modell_Uebersicht_De.pdf',
        'Bell_De.pdf': '023_Bell_De.pdf',
        'QM_De.pdf': '035_QM_De.pdf',
        'T0_Kosmologie_De.pdf': '025_T0_Kosmologie_De.pdf',
        'Casimir_De.pdf': '091_Casimir_De.pdf',
        'Zusammenfassung_De.pdf': '081_Zusammenfassung_De.pdf',
        
        # Additional mappings
        'cosmic_De.pdf': '063_cosmic_De.pdf',
        'cosmic\\_De.pdf': '063_cosmic_De.pdf',
        'gravitationskonstante_De.pdf': '045_gravitationskonstante_De.pdf',
        'gravitationskonstante\\_De.pdf': '045_gravitationskonstante_De.pdf',
        'NatEinheitenSystematik_De.pdf': '015_NatEinheitenSystematik_De.pdf',
        'NatEinheitenSystematik\\_De.pdf': '015_NatEinheitenSystematik_De.pdf',
        'parameterherleitung_De.pdf': '041_parameterherleitung_De.pdf',
        'parameterherleitung\\_De.pdf': '041_parameterherleitung_De.pdf',
        'Feinstrukturkonstante_De.pdf': '044_Feinstrukturkonstante_De.pdf',
        'Feinstrukturkonstante\\_De.pdf': '044_Feinstrukturkonstante_De.pdf',
        'TempEinheitenCMB_De.pdf': '061_TempEinheitenCMB_De.pdf',
        'TempEinheitenCMB\\_De.pdf': '061_TempEinheitenCMB_De.pdf',
        'Mathematische_struktur_De.pdf': '070_Mathematische_struktur_De.pdf',
        'Mathematische\\_struktur\\_De.pdf': '070_Mathematische_struktur_De.pdf',
        'ResolvingTheConstantsAlfa_De.pdf': '043_ResolvingTheConstantsAlfa_De.pdf',
        'ResolvingTheConstantsAlfa\\_De.pdf': '043_ResolvingTheConstantsAlfa_De.pdf',
        '137_De.pdf': '087_137_De.pdf',
        '137\\_De.pdf': '087_137_De.pdf',
        'T0_Anomalien_De.pdf': '018_T0_Anomale-g2-10_De.pdf',
        'T0\\_Anomalien\\_De.pdf': '018_T0_Anomale-g2-10_De.pdf',
        'QM-Detrmistic_p_De.pdf': '072_QM-Detrmistic_p_De.pdf',
        'QM-Detrmistic\\_p\\_De.pdf': '072_QM-Detrmistic_p_De.pdf',
        'scheinbar_instantan_De.pdf': '131_scheinbar_instantan_De.pdf',
        'scheinbar\\_instantan\\_De.pdf': '131_scheinbar_instantan_De.pdf',
        'QM-testen_De.pdf': '073_QM-testen_De.pdf',
        'QM-testen\\_De.pdf': '073_QM-testen_De.pdf',
        'T0_Bibliography_De.pdf': '082_T0_Bibliography_De.pdf',
        'T0\\_Bibliography\\_De.pdf': '082_T0_Bibliography_De.pdf',
    }
    
    return mapping

def fix_escaped_references(tex_file, pdf_mapping, dry_run=True):
    """Fix PDF references including LaTeX-escaped versions."""
    with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content
    fixes = []
    
    lines = content.split('\n')
    new_lines = []
    
    for line_num, line in enumerate(lines, 1):
        new_line = line
        
        # Skip external URLs
        if re.search(r'\\url\{https?://', line):
            new_lines.append(line)
            continue
        
        # Skip preamble comments
        if re.match(r'^\s*%\s*(Standardized preamble|Filename):', line):
            new_lines.append(line)
            continue
        
        # Fix references - sort by length to avoid partial replacements
        for old_ref, new_ref in sorted(pdf_mapping.items(), key=lambda x: len(x[0]), reverse=True):
            if old_ref in line:
                old_line = new_line
                new_line = new_line.replace(old_ref, new_ref)
                if new_line != old_line:
                    fixes.append({
                        'line': line_num,
                        'old': old_ref,
                        'new': new_ref
                    })
        
        new_lines.append(new_line)
    
    new_content = '\n'.join(new_lines)
    
    if new_content != original_content and not dry_run:
        # Create backup
        backup_file = tex_file.with_suffix('.tex.bak4')
        shutil.copy2(tex_file, backup_file)
        
        # Write fixed content
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return fixes, new_content != original_content

def main():
    directory = Path(r'C:\Users\johann\B18\2\tex-n\de_standalone')
    
    if not directory.exists():
        print(f"Error: Directory not found: {directory}")
        return
    
    # Build mapping with escapes
    print("Building mapping with LaTeX-escaped versions...")
    pdf_mapping = build_mapping_with_escapes()
    print(f"Created {len(pdf_mapping)} mappings\n")
    
    # Show sample mappings
    print("Sample escaped mappings:")
    print("-" * 80)
    for i, (old, new) in enumerate(sorted(pdf_mapping.items())[:15]):
        if '\\' in old:
            print(f"  {old} → {new}")
    print()
    
    # First pass: dry run
    print("=" * 80)
    print("DRY RUN - Fixing LaTeX-escaped references")
    print("=" * 80)
    print()
    
    all_fixes = {}
    tex_files = sorted(directory.glob('*.tex'))
    
    for tex_file in tex_files:
        fixes, needs_fix = fix_escaped_references(tex_file, pdf_mapping, dry_run=True)
        if fixes:
            all_fixes[tex_file.name] = fixes
    
    if not all_fixes:
        print("✓ All escaped references are already fixed!")
        return
    
    # Show what will be fixed
    print(f"Files needing fixes: {len(all_fixes)}\n")
    
    total_fixes = 0
    for tex_name, fixes in sorted(all_fixes.items()):
        print(f"\n{tex_name}:")
        
        # Group by old->new
        fix_map = defaultdict(list)
        for fix in fixes:
            key = (fix['old'], fix['new'])
            fix_map[key].append(fix['line'])
        
        for (old, new), lines in sorted(fix_map.items())[:10]:
            print(f"  {old}")
            print(f"    → {new}")
            print(f"    Lines: {', '.join(map(str, sorted(set(lines))[:10]))}")
        
        if len(fix_map) > 10:
            print(f"  ... and {len(fix_map) - 10} more")
        
        total_fixes += len(fixes)
    
    print()
    print("=" * 80)
    print(f"TOTAL: {total_fixes} fixes in {len(all_fixes)} files")
    print("=" * 80)
    
    # Ask for confirmation
    response = input("\nApply all these fixes? (yes/no): ").strip().lower()
    
    if response == 'yes':
        print("\nApplying fixes...")
        fixed_count = 0
        for tex_file in tex_files:
            fixes, needs_fix = fix_escaped_references(tex_file, pdf_mapping, dry_run=False)
            if needs_fix:
                print(f"✓ Fixed: {tex_file.name} ({len(fixes)} changes)")
                fixed_count += 1
        
        print()
        print("=" * 80)
        print(f"DONE: Fixed {fixed_count} files")
        print("=" * 80)
        print("\nBackup files created with .tex.bak4 extension")
        print("Run analyze_pdf_references.py again to verify")
    else:
        print("\nFixes cancelled.")

if __name__ == '__main__':
    main()
