"""
Fix PDF references to use correct numbered prefixes for internal documents.
External URLs are left unchanged.
"""
import os
import re
from pathlib import Path
from collections import defaultdict
import shutil

def build_pdf_mapping(directory):
    """Build mapping from partial names to full numbered filenames."""
    tex_files = list(Path(directory).glob('*.tex'))
    mapping = {}
    
    for tex_file in tex_files:
        tex_name = tex_file.name
        pdf_name = tex_name.replace('.tex', '.pdf')
        
        # Extract components
        match = re.match(r'^(\d{3}[a-z]?)_(.*?)_De\.tex$', tex_name)
        if match:
            prefix = match.group(1)
            base_name = match.group(2)
            
            # Create various possible variations that might be referenced
            variations = [
                # Without prefix
                f"{base_name}_De.pdf",
                # Without underscores
                f"{base_name.replace('_', '')}De.pdf",
                # Capitalization variants
                f"{base_name}_de.pdf",
                # With version numbers
                f"{base_name}_v1_De.pdf",
            ]
            
            for var in variations:
                if var not in mapping:
                    mapping[var] = pdf_name
        
    # Add some specific known mappings
    specific_mappings = {
        'reise_De.pdf': '002_reise_De.pdf',
        'T0_Grundlagen_De.pdf': '003_T0_Grundlagen_v1_De.pdf',
        'HdokumentDe.pdf': '040_Hdokument_De.pdf',
        'Hdokument_De.pdf': '040_Hdokument_De.pdf',
        'T0-Energie_De.pdf': '010_T0_Energie_De.pdf',
        'systemDe.pdf': '059_system_De.pdf',
        'system_De.pdf': '059_system_De.pdf',
        'cosmic_De.pdf': '063_cosmic_De.pdf',
        'T0_Neutrinos_De.pdf': '007_T0_Neutrinos_De.pdf',
        'T0_Feinstruktur_De.pdf': '011_T0_Feinstruktur_De.pdf',
        'T0_Gravitationskonstante_De.pdf': '012_T0_Gravitationskonstante_De.pdf',
        'T0_Teilchenmassen_De.pdf': '006_T0_Teilchenmassen_De.pdf',
        'Teilchenmassen_De.pdf': '006_T0_Teilchenmassen_De.pdf',
        'gravitationskonstante_De.pdf': '045_gravitationskonstante_De.pdf',
        'NatEinheitenSystematik_De.pdf': '015_NatEinheitenSystematik_De.pdf',
        'Fraktale_Korrektur_Herleitung_De.pdf': '133_Fraktale_Korrektur_Herleitung_De.pdf',
        'T0_nat-si_De.pdf': '014_T0_nat-si_De.pdf',
        'T0_Energie_De.pdf': '010_T0_Energie_De.pdf',
        'parameterherleitung_De.pdf': '041_parameterherleitung_De.pdf',
        'Feinstrukturkonstante_De.pdf': '044_Feinstrukturkonstante_De.pdf',
        'Einheitenkonventionen_c_Geschwindigkeit_De.pdf': '134_Einheitenkonventionen_c_Geschwindigkeit_De.pdf',
        'zirkularitaet-Konstanten_De.pdf': '101_zirkularitaet-Konstanten_De.pdf',
        'TempEinheitenCMB_De.pdf': '061_TempEinheitenCMB_De.pdf',
        'Mathematische_struktur_De.pdf': '070_Mathematische_struktur_De.pdf',
        'ResolvingTheConstantsAlfa_De.pdf': '043_ResolvingTheConstantsAlfa_De.pdf',
        '137_De.pdf': '087_137_De.pdf',
        'T0_Anomalien_De.pdf': '018_T0_Anomale-g2-10_De.pdf',
        'Bell_De.pdf': '023_Bell_De.pdf',
        'QM_De.pdf': '035_QM_De.pdf',
        'T0_QM-QFT-RT_De.pdf': '020_T0_QM-QFT-RT_De.pdf',
        'redshift_deflection_De.pdf': '063_cosmic_De.pdf',  # Might need verification
        'QM-Detrmistic_p_De.pdf': '072_QM-Detrmistic_p_De.pdf',
        'scheinbar_instantan_De.pdf': '131_scheinbar_instantan_De.pdf',
        'QM-testen_De.pdf': '073_QM-testen_De.pdf',
        'Zusammenfassung_De.pdf': '081_Zusammenfassung_De.pdf',
        'T0_Kosmologie_De.pdf': '025_T0_Kosmologie_De.pdf',
        'Casimir_De.pdf': '091_Casimir_De.pdf',
        'T0_Book_Abstract_De.pdf': '001_T0_Book_Abstract_De.pdf',
        'T0_Modell_Uebersicht_De.pdf': '004_T0_Modell_Uebersicht_De.pdf',
        'T0_Bibliography_De.pdf': '082_T0_Bibliography_De.pdf',
        'CBM_De.pdf': '039_Zwei-Dipole-CMB_De.pdf',  # Might be typo for CMB
        'Charge_De.pdf': '124_Unit Charge_De.pdf',
        'dirac_De.pdf': '051_dirac_De.pdf',
        'g2_T0_Phenomenology.pdf': '018_T0_Anomale-g2-10_De.pdf',
        'FFGFT_Narrative_Master_De.pdf': '145_FFGFT_donat-teil1_De.pdf',  # Might need verification
        'T0_xi_ursprung.pdf': '009_T0_xi_ursprung_De.pdf',
    }
    
    mapping.update(specific_mappings)
    
    return mapping

def is_external_url(line):
    """Check if the PDF reference is part of an external URL."""
    return bool(re.search(r'\\url\{https?://', line))

def fix_pdf_references_in_file(tex_file, pdf_mapping, dry_run=True):
    """Fix PDF references in a single file."""
    with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content
    fixes = []
    
    # Find all non-external PDF references
    lines = content.split('\n')
    new_lines = []
    
    for line_num, line in enumerate(lines, 1):
        new_line = line
        
        # Skip if it's an external URL
        if is_external_url(line):
            new_lines.append(line)
            continue
        
        # Skip preamble comments (already handled)
        if re.match(r'^\s*%\s*(Standardized preamble|Filename):', line):
            new_lines.append(line)
            continue
        
        # Find internal PDF references that need fixing
        for old_ref, new_ref in pdf_mapping.items():
            if old_ref in line and new_ref != old_ref:
                # Check if this reference doesn't already have a number prefix
                if not re.match(r'^\d{3}', old_ref):
                    # Make sure we're not in a URL context
                    pattern = re.escape(old_ref)
                    if re.search(pattern, line):
                        new_line = new_line.replace(old_ref, new_ref)
                        if new_line != line:
                            fixes.append({
                                'line': line_num,
                                'old': old_ref,
                                'new': new_ref,
                                'context': line.strip()[:80]
                            })
        
        new_lines.append(new_line)
    
    new_content = '\n'.join(new_lines)
    
    if new_content != original_content and not dry_run:
        # Create backup
        backup_file = tex_file.with_suffix('.tex.bak2')
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
    
    # Build mapping
    print("Building PDF filename mapping...")
    pdf_mapping = build_pdf_mapping(directory)
    print(f"Found {len(pdf_mapping)} mappings\n")
    
    # First pass: dry run
    print("=" * 80)
    print("DRY RUN - Analyzing fixes needed")
    print("=" * 80)
    print()
    
    all_fixes = {}
    tex_files = sorted(directory.glob('*.tex'))
    
    for tex_file in tex_files:
        fixes, needs_fix = fix_pdf_references_in_file(tex_file, pdf_mapping, dry_run=True)
        if fixes:
            all_fixes[tex_file.name] = fixes
    
    if not all_fixes:
        print("No fixes needed!")
        return
    
    # Show what will be fixed
    print(f"Files needing fixes: {len(all_fixes)}\n")
    
    total_fixes = 0
    for tex_name, fixes in sorted(all_fixes.items()):
        print(f"\n{tex_name}:")
        # Group by old->new to avoid repetition
        fix_map = defaultdict(list)
        for fix in fixes:
            key = (fix['old'], fix['new'])
            fix_map[key].append(fix['line'])
        
        for (old, new), lines in sorted(fix_map.items()):
            print(f"  {old} → {new}")
            print(f"    Lines: {', '.join(map(str, sorted(set(lines))))}")
            total_fixes += len(lines)
    
    print()
    print("=" * 80)
    print(f"TOTAL FIXES: {total_fixes} references in {len(all_fixes)} files")
    print("=" * 80)
    
    # Ask for confirmation
    response = input("\nApply these fixes? (yes/no): ").strip().lower()
    
    if response == 'yes':
        print("\nApplying fixes...")
        fixed_count = 0
        for tex_file in tex_files:
            fixes, needs_fix = fix_pdf_references_in_file(tex_file, pdf_mapping, dry_run=False)
            if needs_fix:
                print(f"✓ Fixed: {tex_file.name}")
                fixed_count += 1
        
        print()
        print("=" * 80)
        print(f"DONE: Fixed {fixed_count} files")
        print("=" * 80)
        print("\nBackup files created with .tex.bak2 extension")
        print("Run analyze_pdf_references.py again to verify fixes")
    else:
        print("\nFixes cancelled.")

if __name__ == '__main__':
    main()
