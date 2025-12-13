#!/usr/bin/env python3
"""
Continuous table conversion script - processes all 62 remaining files
"""
import os
import re
import subprocess
import sys

# Files that need conversion (62 remaining)
FILES_TO_CONVERT = {
    'de': [
        '006_T0_Teilchenmassen_De.tex', '009_T0_xi_ursprung_De.tex', '010_T0_Energie_De.tex',
        '014_T0_nat-si_De.tex', '015_NatEinheitenSystematik_De.tex', '016_T0_Vollstaendige_Berchnungen_De.tex',
        '023_Bell_De.tex', '024_T0_netze_De.tex', '025_T0_Kosmologie_De.tex',
        '028_T0_7-fragen-3_De.tex', '032_T0_umkehrung_De.tex', '033_T0-Theory-vs-Synergetics_De.tex',
        '035_QM_De.tex', '039_Zwei-Dipole-CMB_De.tex', '041_parameterherleitung_De.tex',
        '042_xi_parmater_partikel_De.tex', '046_Teilchenmassen_De.tex', '054_Elimination_Of_Mass_Dirac_Tabelle_De.tex',
        '059_system_De.tex', '062_Moll_Candela_De.tex', '066_ParameterSystemdipendent_De.tex',
        '071_QM-Detrmistic_De.tex', '072_QM-Detrmistic_p_De.tex', '075_RSA_De.tex',
        '077_E-mc2_De.tex', '081_Zusammenfassung_De.tex', '084_T0_photonenchip-umsetzung_De.tex',
        '085_T0_photonenchip-einführung_De.tex', '087_137_De.tex', '091_Casimir_De.tex',
        '103_T0_Anomale-g2-6_De.tex'
    ],
    'en': [
        '005_T0_tm-erweiterung-x6_En.tex', '006_T0_Teilchenmassen_En.tex', '007_T0_Neutrinos_En.tex',
        '009_T0_xi_ursprung_En.tex', '010_T0_Energie_En.tex', '014_T0_nat-si_En.tex',
        '015_NatEinheitenSystematik_En.tex', '016_T0_Vollstaendige_Berchnungen_En.tex', '018_T0_Anomale-g2-9_En.tex',
        '022_T0-QFT-ML_Addendum_En.tex', '023_Bell_En.tex', '024_T0_netze_En.tex',
        '025_T0_Kosmologie_En.tex', '028_T0_7-fragen-3_En.tex', '032_T0_umkehrung_En.tex',
        '033_T0-Theory-vs-Synergetics_En.tex', '035_QM_En.tex', '039_Zwei-Dipole-CMB_En.tex',
        '041_parameterherleitung_En.tex', '042_xi_parmater_partikel_En.tex', '046_Teilchenmassen_En.tex',
        '054_Elimination_Of_Mass_Dirac_Tabelle_En.tex', '059_system_En.tex', '062_Moll_Candela_En.tex',
        '066_ParameterSystemdipendent_En.tex', '071_QM-Detrmistic_En.tex', '072_QM-Detrmistic_p_En.tex',
        '075_RSA_En.tex', '084_T0_photonenchip-umsetzung_En.tex', '085_T0_photonenchip-einführung_En.tex',
        '087_137_En.tex', '091_Casimir_En.tex', '103_T0_Anomale-g2-6_En.tex'
    ]
}

def convert_table_to_adjustbox(content):
    """Convert wide tables to adjustbox format"""
    lines = content.split('\n')
    result = []
    in_table = False
    table_start = -1
    
    for i, line in enumerate(lines):
        # Detect table start
        if r'\begin{table}' in line and not in_table:
            in_table = True
            table_start = i
            result.append(line)
            continue
        
        # Detect tabular that needs adjustbox
        if in_table and r'\begin{tabular}' in line:
            # Check if adjustbox is already there
            if i > 0 and 'adjustbox' in lines[i-1]:
                result.append(line)
                continue
            
            # Add adjustbox wrapper
            result.append(r'\begin{adjustbox}{max width=\textwidth}')
            
            # Convert column spec to percentage-based
            match = re.search(r'\\begin\{tabular\}\{([^}]+)\}', line)
            if match:
                colspec = match.group(1)
                # Convert to percentage-based with spacing
                new_colspec = convert_colspec(colspec)
                new_line = line.replace(colspec, new_colspec)
                result.append(new_line)
            else:
                result.append(line)
            continue
        
        # Close adjustbox before end tabular
        if in_table and r'\end{tabular}' in line:
            result.append(line)
            result.append(r'\end{adjustbox}')
            continue
        
        # End table
        if r'\end{table}' in line:
            in_table = False
            result.append(line)
            continue
        
        result.append(line)
    
    return '\n'.join(result)

def convert_colspec(colspec):
    """Convert column specification to percentage-based with spacing"""
    # Parse columns more carefully
    original = colspec
    
    # Count actual columns (not @ markers)
    cols = 0
    i = 0
    while i < len(colspec):
        if colspec[i] in 'lcr':
            cols += 1
            i += 1
        elif colspec[i] == 'p' and i+1 < len(colspec) and colspec[i+1] == '{':
            # Find matching }
            depth = 0
            j = i + 1
            while j < len(colspec):
                if colspec[j] == '{':
                    depth += 1
                elif colspec[j] == '}':
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            cols += 1
            i = j + 1
        else:
            i += 1
    
    if cols == 0 or cols == 1:
        return original  # Don't modify single-column or zero-column specs
    
    # Calculate percentages  
    if cols == 2:
        width_per_col = 0.45
    elif cols == 3:
        width_per_col = 0.30
    elif cols == 4:
        width_per_col = 0.23
    elif cols == 5:
        width_per_col = 0.18
    elif cols == 6:
        width_per_col = 0.15
    else:
        width_per_col = 0.13
    
    # Build new colspec
    col_parts = []
    for i in range(cols):
        col_parts.append(f'p{{{width_per_col:.2f}\\textwidth}}')
    
    return '@{}' + '@{\\hspace{2mm}}'.join(col_parts) + '@{}'

def process_file(filepath):
    """Process a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Only process if file has tables
        if r'\begin{table}' not in content:
            return True, "No tables found"
        
        # Convert tables
        new_content = convert_table_to_adjustbox(content)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # Compile to test
        base = os.path.basename(filepath).replace('.tex', '')
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', filepath],
            cwd=os.path.dirname(filepath),
            capture_output=True,
            timeout=60
        )
        
        if result.returncode == 0:
            return True, "Success"
        else:
            return False, "Compilation failed"
    
    except Exception as e:
        return False, str(e)

def main():
    base_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n'
    
    total = len(FILES_TO_CONVERT['de']) + len(FILES_TO_CONVERT['en'])
    processed = 0
    success = 0
    
    print(f"Starting conversion of {total} files...")
    print("=" * 60)
    
    # Process German files
    for filename in FILES_TO_CONVERT['de']:
        filepath = os.path.join(base_dir, 'de_standalone', filename)
        if not os.path.exists(filepath):
            print(f"SKIP: {filename} (not found)")
            continue
        
        print(f"Processing {processed+1}/{total}: {filename}...", end=' ')
        ok, msg = process_file(filepath)
        processed += 1
        if ok:
            success += 1
            print("✓")
        else:
            print(f"✗ ({msg})")
        
        if processed % 10 == 0:
            print(f"\n--- Progress: {processed}/{total} ({success} successful) ---\n")
    
    # Process English files
    for filename in FILES_TO_CONVERT['en']:
        filepath = os.path.join(base_dir, 'en_standalone', filename)
        if not os.path.exists(filepath):
            print(f"SKIP: {filename} (not found)")
            continue
        
        print(f"Processing {processed+1}/{total}: {filename}...", end=' ')
        ok, msg = process_file(filepath)
        processed += 1
        if ok:
            success += 1
            print("✓")
        else:
            print(f"✗ ({msg})")
        
        if processed % 10 == 0:
            print(f"\n--- Progress: {processed}/{total} ({success} successful) ---\n")
    
    print("=" * 60)
    print(f"COMPLETE: {success}/{processed} files converted successfully")
    return 0 if success == processed else 1

if __name__ == '__main__':
    sys.exit(main())
