#!/usr/bin/env python3
"""
Script to translate German LaTeX FFGFT chapters to English.
This script processes chapters systematically, replacing German text with English
while preserving all LaTeX structures, equations, and formatting.
"""

import os
import re
from pathlib import Path

# Translation dictionaries for common terms
translations = {
    # Document setup
    r'\\usepackage\[ngerman\]\{babel\}': r'\\usepackage[english]{babel}',
    'Hyperref als eines der letzten Pakete laden': 'Load hyperref as one of the last packages',
    'Saubere PDF-Lesezeichen': 'Clean PDF bookmarks',
    r'\\def\\approx\{etwa\}': r'\\def\\approx{approx}',
    
    # Common LaTeX terms
    'Wichtige Symbole und ihre Einheiten': 'Important Symbols and their Units',
    'Symbol': 'Symbol',
    'Bedeutung': 'Meaning',
    'Einheit \\(SI\\)': 'Unit (SI)',
    'Einheitenprüfung': 'Unit Check',
    'Erkl\\\\"arung': 'Explanation',
    
    # Chapter titles
    'Kapitel': 'Chapter',
    
    # Common physics terms
    'Fraktale Dimension': 'Fractal dimension',
    'dimensionslos': 'dimensionless',
    'Lichtgeschwindigkeit': 'Speed of light',
    'Gravitationskonstante': 'Gravitational constant',
    'Testmasse': 'Test mass',
    'Planck-Länge': 'Planck length',
    'Zentralmasse': 'Central mass',
    'Bahndrehimpuls': 'Orbital angular momentum',
    
    # Subsection common terms
    'Schlussfolgerung': 'Conclusion',
    'Vergleich mit': 'Comparison with',
    'Testbare Vorhersagen': 'Testable Predictions',
    
    # Month/Time
    'Jahr': 'year',
    'Jahrhundert': 'century',
}

def translate_file(input_path, output_path):
    """Translate a single German LaTeX file to English."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply translations
    for german, english in translations.items():
        content = re.sub(german, english, content)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Translated: {input_path.name} -> {output_path.name}")

def main():
    """Main translation function."""
    base_dir = Path(__file__).parent
    de_dir = base_dir / '2/tex-n/de_FFGFT/tex_kapitel'
    en_dir = base_dir / '2/tex-n/en_FFGFT/tex_kapitel'
    
    # Ensure output directory exists
    en_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all German chapter files
    de_files = sorted(de_dir.glob('*.tex'))
    
    print(f"Found {len(de_files)} German chapter files to translate")
    
    for de_file in de_files:
        # Create output filename
        en_filename = de_file.name.replace('_De.tex', '_En.tex')
        en_file = en_dir / en_filename
        
        # Skip if already exists
        if en_file.exists():
            print(f"Skipping {de_file.name} (already translated)")
            continue
        
        # Translate
        translate_file(de_file, en_file)
    
    print(f"\nTranslation complete! All chapters processed.")

if __name__ == '__main__':
    main()
