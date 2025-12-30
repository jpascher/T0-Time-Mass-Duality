#!/usr/bin/env python3
"""
Remove chapter number prefix from section titles in section files
Convert \section{Kapitel 12: Title} to just content without the section command
since the main document already provides \chapter{Title}
"""
import os
import re

def clean_section_title(content):
    """Remove \section{Kapitel X: ...} from beginning as main doc has \chapter"""
    # Remove the first \section command that has "Kapitel" in it
    content = re.sub(r'\\section\{Kapitel \d+[a-z]?: [^}]+\}\s*', '', content, count=1)
    return content

# Process German section files
de_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_DVFT/tex_kapitel'

print("Removing chapter titles from German section files...")
count = 0
for filename in os.listdir(de_dir):
    if filename.endswith('_section.tex'):
        filepath = os.path.join(de_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = clean_section_title(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"  ✓ Cleaned: {filename}")

print(f"\nCleaned {count} German section files")

# Process English section files
en_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/en_DVFT/tex_kapitel'

print("\nRemoving chapter titles from English section files...")
count = 0
for filename in os.listdir(en_dir):
    if filename.endswith('_section.tex'):
        filepath = os.path.join(en_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        # For English, also remove "Chapter X:" patterns
        content = re.sub(r'\\section\{Chapter \d+[a-z]?: [^}]+\}\s*', '', content, count=1)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"  ✓ Cleaned: {filename}")

print(f"\nCleaned {count} English section files")
print("\nChapter title removal complete!")
