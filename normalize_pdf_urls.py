#!/usr/bin/env python3
"""
Normalize PDF URLs to use prefixed filenames.
Updates URLs in en_standalone files.
"""

import os
import re

# Mapping from old unprefixed names to correct prefixed names
URL_MAPPINGS = {
    # Main documents
    'HdokumentEn.pdf': '040_Hdokument_En.pdf',
    'HdokumentDe.pdf': '040_Hdokument_De.pdf',
    
    # Cosmic/Cosmology
    'cosmicEn.pdf': '063_cosmic_En.pdf',
    'cosmicDe.pdf': '063_cosmic_De.pdf',
    
    # Particle masses
    'TeilchenmassenEn.pdf': '006_T0_Teilchenmassen_En.pdf',
    'TeilchenmassenDe.pdf': '006_T0_Teilchenmassen_De.pdf',
    
    # Energy formulation
    'T0-EnergieEn.pdf': '010_T0_Energie_En.pdf',
    'T0-EnergieDe.pdf': '010_T0_Energie_De.pdf',
    
    # Temperature/CMB
    'TempEinheitenCMBEn.pdf': '061_TempEinheitenCMB_En.pdf',
    'TempEinheitenCMBDe.pdf': '061_TempEinheitenCMB_De.pdf',
    
    # Lagrangian
    'lagrandian-einfachEn.pdf': '129_lagrandian-einfach_En.pdf',
    'lagrandian-einfachDe.pdf': '129_lagrandian-einfach_De.pdf',
    
    # Redshift - these don't exist, remove them
    'redshift_deflectionEn.pdf': None,  # Remove
    'redshift_deflectionDe.pdf': None,  # Remove
    'redshift_deflection_En.pdf': None,  # Remove
    'redshift_deflection_De.pdf': None,  # Remove
    
    # Gravitational constant
    'gravitationskonstnte_En.pdf': '127_gravitationskonstnte_En.pdf',
}

def normalize_urls(file_path):
    """Normalize PDF URLs in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # Process each mapping
        for old_name, new_name in URL_MAPPINGS.items():
            url_pattern = f'https://jpascher.github.io/T0-Time-Mass-Duality/2/pdf/{old_name}'
            
            if url_pattern in content:
                if new_name is None:
                    # Don't replace, just note it (manual removal needed)
                    changes.append(f"  FOUND (needs manual removal): {old_name}")
                else:
                    new_url = f'https://jpascher.github.io/T0-Time-Mass-Duality/2/pdf/{new_name}'
                    content = content.replace(url_pattern, new_url)
                    changes.append(f"  {old_name} → {new_name}")
        
        if content != original_content:
            # Create backup
            backup_path = file_path + '.bak_url'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Write normalized content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return changes
        return None
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def main():
    en_dir = r'C:\Users\johann\B18\2\tex-n\en_standalone'
    
    if not os.path.exists(en_dir):
        print(f"Directory not found: {en_dir}")
        return
    
    print("=" * 80)
    print("Normalizing PDF URLs in English standalone documents")
    print("=" * 80)
    
    total_fixed = 0
    
    for filename in sorted(os.listdir(en_dir)):
        if not filename.endswith('.tex'):
            continue
        
        file_path = os.path.join(en_dir, filename)
        changes = normalize_urls(file_path)
        
        if changes:
            total_fixed += 1
            print(f"\n✓ {filename}")
            for change in changes:
                print(change)
    
    print("\n" + "=" * 80)
    print(f"Total files updated: {total_fixed}")
    print("=" * 80)
    print("\nNOTE: redshift_deflection URLs found but NOT removed automatically.")
    print("These need manual review as the documents don't exist.")

if __name__ == '__main__':
    main()
