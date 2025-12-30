#!/usr/bin/env python3
"""
Remove abstract environments from section files as book class doesn't support them
"""
import os
import re

def remove_abstract(content):
    """Remove \\begin{abstract}...\\end{abstract} blocks"""
    # Remove abstract environment entirely
    content = re.sub(r'\\begin\{abstract\}.*?\\end\{abstract\}', '', content, flags=re.DOTALL)
    return content

# Process German section files
de_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_DVFT/tex_kapitel'

print("Removing abstract environments from German section files...")
for filename in os.listdir(de_dir):
    if filename.endswith('_section.tex'):
        filepath = os.path.join(de_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = remove_abstract(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed: {filename}")

# Process English section files
en_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/en_DVFT/tex_kapitel'

print("\nRemoving abstract environments from English section files...")
for filename in os.listdir(en_dir):
    if filename.endswith('_section.tex'):
        filepath = os.path.join(en_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = remove_abstract(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed: {filename}")

print("\nAbstract environments removed!")
