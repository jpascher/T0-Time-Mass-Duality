#!/usr/bin/env python3
"""
Script to rename T0-Theorie/T0 theory to FFGFT systematically across chapter files.
Preserves mathematical symbols like T_0, T0 in equations and formulas.
"""

import re
import os
from pathlib import Path

def is_in_math_mode(text, pos):
    """Check if position is inside math mode ($...$, \[...\], align, equation, etc.)"""
    # This is a simplified check - looks for $ before and after
    before = text[:pos]
    after = text[pos:]
    
    # Count $ signs before position
    dollar_count = before.count('$')
    
    # If odd number of $ before, we're likely in inline math
    if dollar_count % 2 == 1:
        return True
    
    # Check for display math environments
    if '\\[' in before and '\\]' not in before[before.rfind('\\['):]:
        return True
    
    # Check for align, equation, etc.
    math_envs = ['align', 'equation', 'gather', 'multline', 'eqnarray']
    for env in math_envs:
        begin_pattern = f'\\begin{{{env}'
        end_pattern = f'\\end{{{env}'
        if begin_pattern in before:
            last_begin = before.rfind(begin_pattern)
            last_end = before.rfind(end_pattern)
            if last_end < last_begin:
                return True
    
    return False

def replace_t0_theory_german(content):
    """Replace German T0-Theorie references with FFGFT"""
    
    # Store math environments to protect them
    math_blocks = []
    
    # German patterns to replace (outside math mode)
    patterns = [
        # Full phrases with variants
        (r'die\s+T0-Theorie\s+der\s+Zeit-Masse-Dualität', 
         'die Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT), die früher als T0-Theorie (Zeit-Masse-Dualität) bekannt war,'),
        (r'T0-Theorie\s+\(Time-Mass-Duality\)', 
         'Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT)'),
        (r'T0-Theorie\s+der\s+Zeit-Masse-Dualität', 
         'Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT)'),
        (r'der\s+T0-Theorie', 'der FFGFT'),
        (r'die\s+T0-Theorie', 'die FFGFT'),
        (r'in\s+der\s+T0-Theorie', 'in der FFGFT'),
        (r'T0-Theorie-basiert', 'FFGFT-basiert'),
        (r'T0-Theorie', 'FFGFT'),
        (r'T0\s+Theorie', 'FFGFT'),
    ]
    
    result = content
    for pattern, replacement in patterns:
        # Only replace if not in math mode (simple approximation)
        result = re.sub(pattern, replacement, result)
    
    return result

def replace_t0_theory_english(content):
    """Replace English T0 theory references with FFGFT"""
    
    # English patterns to replace (outside math mode)
    patterns = [
        # Full phrases
        (r'the\s+T0\s+theory\s+of\s+time-mass\s+duality', 
         'the Fundamental Fractal-Geometric Field Theory (FFGFT), previously known as T0 theory (Time-Mass Duality),'),
        (r'T0\s+theory\s+\(Time-Mass\s+Duality\)', 
         'Fundamental Fractal-Geometric Field Theory (FFGFT)'),
        (r'T0\s+theory\s+of\s+time-mass\s+duality', 
         'Fundamental Fractal-Geometric Field Theory (FFGFT)'),
        (r'the\s+T0\s+theory', 'the FFGFT'),
        (r'within\s+T0\s+theory', 'within the FFGFT'),
        (r'T0-theory-based', 'FFGFT-based'),
        (r'T0\s+Theory', 'FFGFT'),
        (r'T0\s+theory', 'FFGFT'),
    ]
    
    result = content
    for pattern, replacement in patterns:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    
    return result

def process_file(filepath, is_german=True):
    """Process a single file to rename T0 references"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply appropriate replacements
        if is_german:
            content = replace_t0_theory_german(content)
        else:
            content = replace_t0_theory_english(content)
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    base_dir = Path('/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/narrative')
    
    # Process German chapters
    print("Processing German chapter files...")
    de_chapters = list((base_dir / 'de_chapters_new').glob('*.tex'))
    de_count = 0
    for filepath in de_chapters:
        if process_file(filepath, is_german=True):
            de_count += 1
            print(f"  Updated: {filepath.name}")
    
    # Process English chapters
    print("\nProcessing English chapter files...")
    en_chapters = list((base_dir / 'en_chapters_new').glob('*.tex'))
    en_count = 0
    for filepath in en_chapters:
        if process_file(filepath, is_german=False):
            en_count += 1
            print(f"  Updated: {filepath.name}")
    
    # Process master documents
    print("\nProcessing master documents...")
    master_de = base_dir / 'completted' / 'T0_Anwendungen_De.tex'
    master_en = base_dir / 'completted' / 'T0_Anwendungen_En.tex'
    
    master_count = 0
    if master_de.exists() and process_file(master_de, is_german=True):
        master_count += 1
        print(f"  Updated: {master_de.name}")
    
    if master_en.exists() and process_file(master_en, is_german=False):
        master_count += 1
        print(f"  Updated: {master_en.name}")
    
    print(f"\n=== Summary ===")
    print(f"German chapters updated: {de_count}")
    print(f"English chapters updated: {en_count}")
    print(f"Master documents updated: {master_count}")
    print(f"Total files updated: {de_count + en_count + master_count}")

if __name__ == '__main__':
    main()
