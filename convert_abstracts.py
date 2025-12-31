#!/usr/bin/env python3
"""
Convert abstract environment to section in section files
"""
import os
import re

def convert_abstract_to_section(content):
    """Convert \\begin{abstract}...\\end{abstract} to \\section{Zusammenfassung}"""
    # Replace abstract with section for German
    content = re.sub(
        r'\\begin\{abstract\}(.*?)\\end\{abstract\}',
        r'\\section*{Zusammenfassung}\n\1',
        content,
        flags=re.DOTALL
    )
    return content

def convert_abstract_to_section_en(content):
    """Convert \\begin{abstract}...\\end{abstract} to \\section{Abstract}"""
    # Replace abstract with section for English
    content = re.sub(
        r'\\begin\{abstract\}(.*?)\\end\{abstract\}',
        r'\\section*{Abstract}\n\1',
        content,
        flags=re.DOTALL
    )
    return content

# Process German chapter files (original files, not section files)
de_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_FFGFT/tex_kapitel'

print("Converting abstract to section in German chapter files...")
for filename in os.listdir(de_dir):
    if filename.endswith('.tex') and not filename.endswith('_section.tex'):
        filepath = os.path.join(de_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = convert_abstract_to_section(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Converted: {filename}")

# Process English chapter files
en_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/en_FFGFT/tex_kapitel'

print("\nConverting abstract to section in English chapter files...")
for filename in os.listdir(en_dir):
    if filename.endswith('.tex') and not filename.endswith('_section.tex'):
        filepath = os.path.join(en_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = convert_abstract_to_section_en(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Converted: {filename}")

print("\nRegenerate section files...")
import subprocess
subprocess.run([
    'python3',
    '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/create_sections.py'
], check=True)

print("\nAbstract to section conversion complete!")
