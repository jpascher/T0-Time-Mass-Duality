"""
Comprehensive fix for ALL PDF references - standardize to numbered prefixes.
"""
import os
import re
from pathlib import Path
from collections import defaultdict
import shutil

def build_comprehensive_mapping(directory):
    """Build comprehensive mapping including all variations."""
    tex_files = list(Path(directory).glob('*.tex'))
    mapping = {}
    
    # Build mapping from actual files
    for tex_file in tex_files:
        tex_name = tex_file.name
        pdf_name = tex_name.replace('.tex', '.pdf')
        
        # Extract base name without prefix
        match = re.match(r'^(\d{3}[a-z]?)_(.*?)_De\.tex$', tex_name)
        if match:
            prefix = match.group(1)
            base_name = match.group(2)
            
            # Map variations without prefix
            mapping[f"{base_name}_De.pdf"] = pdf_name
            
            # Map with underscores removed
            mapping[f"{base_name.replace('_', '')}De.pdf"] = pdf_name
            
            # Map common typos and variations
            if base_name == "T0_Book_Abstract":
                mapping["T0_Book_Abstract_De.pdf"] = pdf_name
                mapping["Book_Abstract_De.pdf"] = pdf_name
            
            if base_name == "T0_Modell_Uebersicht":
                mapping["T0_Modell_Uebersicht_De.pdf"] = pdf_name
                mapping["Modell_Uebersicht_De.pdf"] = pdf_name
            
    # Add comprehensive manual mappings for all variations
    specific_mappings = {
        # Already have prefix but incomplete
        "T0_Book_Abstract_De.pdf": "001_T0_Book_Abstract_De.pdf",
        "T0_Modell_Uebersicht_De.pdf": "004_T0_Modell_Uebersicht_De.pdf",
        "T0_tm-erweiterung-x6_De.pdf": "005_T0_tm-erweiterung-x6_De.pdf",
        "T0_xi-und-e_De.pdf": "008_T0_xi-und-e_De.pdf",
        "T0_SI_De.pdf": "013_T0_SI_De.pdf",
        "T0_nat-si_De.pdf": "014_T0_nat-si_De.pdf",
        "T0_QM-QFT-RT_De.pdf": "020_T0_QM-QFT-RT_De.pdf",
        "T0-QFT-ML_Addendum_De.pdf": "022_T0-QFT-ML_Addendum_De.pdf",
        "T0_7-fragen-3_De.pdf": "028_T0_7-fragen-3_De.pdf",
        "T0-Theory-vs-Synergetics_De.pdf": "033_T0-Theory-vs-Synergetics_De.pdf",
        "T0_QM-optimierung_De.pdf": "034_T0_QM-optimierung_De.pdf",
        "Zwei-Dipole-CMB_De.pdf": "039_Zwei-Dipole-CMB_De.pdf",
        
        # Variations and typos
        "Hdokument_De.pdf": "040_Hdokument_De.pdf",
        "Bell-Teil2_De.pdf": "023a_Bell-Teil2_De.pdf",
        "Formel_De.pdf": "047_neutrino-Formel_De.pdf",
        "neutrino-Formel_De.pdf": "047_neutrino-Formel_De.pdf",
        "universale-ableitung_De.pdf": "056_universale-ableitung_De.pdf",
        "musical-spiral-137-_De.pdf": "060_musical-spiral-137-_De.pdf",
        "Zeit-konstant_De.pdf": "069_Zeit-konstant_De.pdf",
        "QM-testen_De.pdf": "073_QM-testen_De.pdf",
        "photonenchip-china_De.pdf": "083_T0_photonenchip-china_De.pdf",
        "T0_photonenchip-china_De.pdf": "083_T0_photonenchip-china_De.pdf",
        "photonenchip-umsetzung_De.pdf": "084_T0_photonenchip-umsetzung_De.pdf",
        "T0_photonenchip-umsetzung_De.pdf": "084_T0_photonenchip-umsetzung_De.pdf",
        "photonenchip-einführung_De.pdf": "085_T0_photonenchip-einführung_De.pdf",
        "T0_photonenchip-einführung_De.pdf": "085_T0_photonenchip-einführung_De.pdf",
        "Dokumentenübersicht_De.pdf": "086_T0_Dokumentenübersicht_De.pdf",
        "T0_Dokumentenübersicht_De.pdf": "086_T0_Dokumentenübersicht_De.pdf",
        "koide-formel-3_De.pdf": "116_T0_koide-formel-3_De.pdf",
        "T0_koide-formel-3_De.pdf": "116_T0_koide-formel-3_De.pdf",
        "verhaeltnis-absolut_De.pdf": "122_T0_verhaeltnis-absolut_De.pdf",
        "T0_verhaeltnis-absolut_De.pdf": "122_T0_verhaeltnis-absolut_De.pdf",
        "lagrandian-einfach_De.pdf": "129_lagrandian-einfach_De.pdf",
        
        # Filename with typo in original
        "016_T0_Vollstaendige_Berechnungen_De.pdf": "016_T0_Vollstaendige_Berchnungen_De.pdf",
        "T0_Vollstaendige_Berechnungen_De.pdf": "016_T0_Vollstaendige_Berchnungen_De.pdf",
        
        # Previously fixed ones to ensure consistency
        "reise_De.pdf": "002_reise_De.pdf",
        "T0_Grundlagen_De.pdf": "003_T0_Grundlagen_v1_De.pdf",
        "HdokumentDe.pdf": "040_Hdokument_De.pdf",
        "T0-Energie_De.pdf": "010_T0_Energie_De.pdf",
        "systemDe.pdf": "059_system_De.pdf",
        "system_De.pdf": "059_system_De.pdf",
        "cosmic_De.pdf": "063_cosmic_De.pdf",
        "T0_Neutrinos_De.pdf": "007_T0_Neutrinos_De.pdf",
        "T0_Feinstruktur_De.pdf": "011_T0_Feinstruktur_De.pdf",
        "T0_Gravitationskonstante_De.pdf": "012_T0_Gravitationskonstante_De.pdf",
        "T0_Teilchenmassen_De.pdf": "006_T0_Teilchenmassen_De.pdf",
        "Teilchenmassen_De.pdf": "006_T0_Teilchenmassen_De.pdf",
        "gravitationskonstante_De.pdf": "045_gravitationskonstante_De.pdf",
        "NatEinheitenSystematik_De.pdf": "015_NatEinheitenSystematik_De.pdf",
        "Fraktale_Korrektur_Herleitung_De.pdf": "133_Fraktale_Korrektur_Herleitung_De.pdf",
        "T0_Energie_De.pdf": "010_T0_Energie_De.pdf",
        "parameterherleitung_De.pdf": "041_parameterherleitung_De.pdf",
        "Feinstrukturkonstante_De.pdf": "044_Feinstrukturkonstante_De.pdf",
        "Einheitenkonventionen_c_Geschwindigkeit_De.pdf": "134_Einheitenkonventionen_c_Geschwindigkeit_De.pdf",
        "zirkularitaet-Konstanten_De.pdf": "101_zirkularitaet-Konstanten_De.pdf",
        "TempEinheitenCMB_De.pdf": "061_TempEinheitenCMB_De.pdf",
        "Mathematische_struktur_De.pdf": "070_Mathematische_struktur_De.pdf",
        "ResolvingTheConstantsAlfa_De.pdf": "043_ResolvingTheConstantsAlfa_De.pdf",
        "137_De.pdf": "087_137_De.pdf",
        "T0_Anomalien_De.pdf": "018_T0_Anomale-g2-10_De.pdf",
        "Bell_De.pdf": "023_Bell_De.pdf",
        "QM_De.pdf": "035_QM_De.pdf",
        "redshift_deflection_De.pdf": "063_cosmic_De.pdf",
        "QM-Detrmistic_p_De.pdf": "072_QM-Detrmistic_p_De.pdf",
        "scheinbar_instantan_De.pdf": "131_scheinbar_instantan_De.pdf",
        "Zusammenfassung_De.pdf": "081_Zusammenfassung_De.pdf",
        "T0_Kosmologie_De.pdf": "025_T0_Kosmologie_De.pdf",
        "Casimir_De.pdf": "091_Casimir_De.pdf",
        "T0_Bibliography_De.pdf": "082_T0_Bibliography_De.pdf",
        "CBM_De.pdf": "039_Zwei-Dipole-CMB_De.pdf",
        "Charge_De.pdf": "124_Unit Charge_De.pdf",
        "Unit Charge_De.pdf": "124_Unit Charge_De.pdf",
        "dirac_De.pdf": "051_dirac_De.pdf",
        "g2_T0_Phenomenology.pdf": "018_T0_Anomale-g2-10_De.pdf",
        "FFGFT_Narrative_Master_De.pdf": "145_FFGFT_donat-teil1_De.pdf",
        "T0_xi_ursprung.pdf": "009_T0_xi_ursprung_De.pdf",
    }
    
    mapping.update(specific_mappings)
    
    return mapping

def fix_all_references(tex_file, pdf_mapping, dry_run=True):
    """Fix ALL PDF references in file."""
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
        
        # Fix preamble/filename comments
        if re.match(r'^\s*%\s*(Standardized preamble|Filename):', line):
            # Get expected PDF name from file
            expected_pdf = tex_file.name.replace('.tex', '.pdf')
            
            if 'Standardized preamble' in line:
                new_line = f'% Standardized preamble - {expected_pdf}'
            elif 'Filename:' in line:
                new_line = f'% Filename: {expected_pdf}'
            
            if new_line != line:
                fixes.append({
                    'line': line_num,
                    'type': 'preamble',
                    'old': line.strip(),
                    'new': new_line.strip()
                })
        else:
            # Fix document references
            for old_ref, new_ref in sorted(pdf_mapping.items(), key=lambda x: len(x[0]), reverse=True):
                if old_ref in line and new_ref != old_ref:
                    # Check if reference doesn't already have correct prefix
                    if not re.match(r'^\d{3}', old_ref):
                        old_line = new_line
                        new_line = new_line.replace(old_ref, new_ref)
                        if new_line != old_line:
                            fixes.append({
                                'line': line_num,
                                'type': 'reference',
                                'old': old_ref,
                                'new': new_ref
                            })
        
        new_lines.append(new_line)
    
    new_content = '\n'.join(new_lines)
    
    if new_content != original_content and not dry_run:
        # Create backup
        backup_file = tex_file.with_suffix('.tex.bak3')
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
    
    # Build comprehensive mapping
    print("Building comprehensive PDF mapping...")
    pdf_mapping = build_comprehensive_mapping(directory)
    print(f"Created {len(pdf_mapping)} mappings\n")
    
    # Show sample mappings
    print("Sample mappings (first 20):")
    print("-" * 80)
    for i, (old, new) in enumerate(sorted(pdf_mapping.items())[:20]):
        print(f"  {old} → {new}")
    print("  ...\n")
    
    # First pass: dry run
    print("=" * 80)
    print("COMPREHENSIVE DRY RUN - Standardizing ALL references")
    print("=" * 80)
    print()
    
    all_fixes = {}
    tex_files = sorted(directory.glob('*.tex'))
    
    for tex_file in tex_files:
        fixes, needs_fix = fix_all_references(tex_file, pdf_mapping, dry_run=True)
        if fixes:
            all_fixes[tex_file.name] = fixes
    
    if not all_fixes:
        print("✓ All references are already standardized!")
        return
    
    # Show what will be fixed
    print(f"Files needing fixes: {len(all_fixes)}\n")
    
    total_fixes = 0
    for tex_name, fixes in sorted(all_fixes.items()):
        print(f"\n{tex_name}:")
        
        # Group by type
        preamble_fixes = [f for f in fixes if f['type'] == 'preamble']
        ref_fixes = [f for f in fixes if f['type'] == 'reference']
        
        if preamble_fixes:
            print("  Preamble:")
            for fix in preamble_fixes[:3]:
                print(f"    Line {fix['line']}: {fix['new']}")
        
        if ref_fixes:
            print("  References:")
            # Group by old->new
            fix_map = defaultdict(list)
            for fix in ref_fixes:
                key = (fix['old'], fix['new'])
                fix_map[key].append(fix['line'])
            
            for (old, new), lines in sorted(fix_map.items())[:10]:
                print(f"    {old} → {new}")
                print(f"      Lines: {', '.join(map(str, sorted(set(lines))[:5]))}")
            
            if len(fix_map) > 10:
                print(f"    ... and {len(fix_map) - 10} more")
        
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
            fixes, needs_fix = fix_all_references(tex_file, pdf_mapping, dry_run=False)
            if needs_fix:
                print(f"✓ Fixed: {tex_file.name} ({len(fixes)} changes)")
                fixed_count += 1
        
        print()
        print("=" * 80)
        print(f"DONE: Fixed {fixed_count} files")
        print("=" * 80)
        print("\nBackup files created with .tex.bak3 extension")
        print("Run analyze_pdf_references.py again to verify")
    else:
        print("\nFixes cancelled.")

if __name__ == '__main__':
    main()
