#!/usr/bin/env python3
"""
Fix German quotes in LaTeX files - convert `` '' to proper German quotes
"""
import os
import re

def fix_german_quotes(content):
    """Replace LaTeX-style quotes with proper German quotes"""
    # Replace ``...'' with German UTF-8 quotes
    # Using chr() to avoid quote syntax issues
    opening_quote = chr(8222)  # „
    closing_quote = chr(8220)  # "
    
    # Replace paired quotes
    content = re.sub(r"``(.*?)''", opening_quote + r'\1' + closing_quote, content)
    
    # Handle standalone quotes
    content = content.replace("``", opening_quote)
    content = content.replace("''", closing_quote)
    
    return content

# Process all German tex files
de_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_FFGFT/tex_kapitel'

files_to_fix = []
for filename in os.listdir(de_dir):
    if filename.endswith('.tex') and not filename.endswith('_section.tex'):
        files_to_fix.append(filename)

print(f"Fixing quotes in {len(files_to_fix)} German chapter files...")

for filename in sorted(files_to_fix):
    filepath = os.path.join(de_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = fix_german_quotes(content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed: {filename}")
        else:
            print(f"  - No changes: {filename}")
    except Exception as e:
        print(f"  ✗ Error fixing {filename}: {e}")

print("\nNow regenerating section files...")

# Regenerate section files after fixing quotes
import subprocess
subprocess.run([
    'python3',
    '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/create_sections.py'
], check=True)

print("\nQuote fixing complete!")
