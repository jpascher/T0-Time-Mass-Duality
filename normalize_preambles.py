#!/usr/bin/env python3
"""
Normalize all standalone documents to use shared LuaLaTeX preambles
according to Section 8 of copilot-lualatex-server.md
"""
import os
import re
from pathlib import Path

def normalize_preamble(filepath):
    """Replace inline packages with shared ebook preamble"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Determine language from filename
        is_german = '_De.tex' in str(filepath)
        lang = 'De' if is_german else 'En'
        
        # Target preamble
        preamble_line = f'\\input{{../../../T0_preamble_shared-ebook_{lang}}}'
        
        # Check if already using ebook preamble
        if 'T0_preamble_shared-ebook' in content:
            return False, "Already using ebook preamble"
            
        # Find documentclass line
        doc_class_match = re.search(r'(\\documentclass\[?[^\]]*\]?\{[^}]+\})', content)
        if not doc_class_match:
            return False, "No documentclass found"
            
        doc_class = doc_class_match.group(1)
        doc_class_end = doc_class_match.end()
        
        # Find \begin{document}
        begin_doc_match = re.search(r'\\begin\{document\}', content)
        if not begin_doc_match:
            return False, "No \\begin{document} found"
            
        begin_doc_pos = begin_doc_match.start()
        
        # Extract preamble section
        old_preamble = content[doc_class_end:begin_doc_pos]
        
        # Check if has existing shared preamble input (non-ebook)
        has_shared = bool(re.search(r'\\input\{[^}]*T0_preamble_shared_(?:De|En)\}', old_preamble))
        
        # Remove problematic packages for LuaLaTeX
        # Keep only document-specific custom commands/environments
        lines_to_keep = []
        for line in old_preamble.split('\n'):
            stripped = line.strip()
            # Skip these common pdflatex-specific packages
            if any(pkg in stripped for pkg in [
                '\\usepackage[utf8]{inputenc}',
                '\\usepackage[T1]{fontenc}',
                '\\usepackage{lmodern}',
                '\\usepackage[ngerman]{babel}',
                '\\usepackage[english]{babel}',
                '\\usepackage{fontspec}',
                '\\usepackage{polyglossia}',
                '\\usepackage{geometry}',
                '\\usepackage{hyperref}',
                '\\usepackage{amsmath}',
                '\\usepackage{amssymb}',
                '\\usepackage{graphicx}',
            ]):
                continue
            # Skip shared preamble inputs (will be replaced)
            if '\\input' in stripped and 'T0_preamble' in stripped:
                continue
            # Keep comments and custom commands
            if stripped.startswith('%') or '\\newcommand' in stripped or '\\newtheorem' in stripped:
                lines_to_keep.append(line)
            elif stripped and not stripped.startswith('\\usepackage'):
                lines_to_keep.append(line)
                
        # Build new preamble
        new_preamble = f"\n{preamble_line}\n"
        if lines_to_keep:
            # Add a comment separator
            new_preamble += "% Document-specific commands:\n"
            new_preamble += '\n'.join(lines_to_keep)
            
        # Reconstruct document
        new_content = content[:doc_class_end] + new_preamble + '\n' + content[begin_doc_pos:]
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        return True, "Normalized"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

# Process all standalone documents
de_dir = Path('2/tex-n/de_standalone')
en_dir = Path('2/tex-n/en_standalone')

# Excluded files (known problematic per section 8.4)
excluded = {
    '201_FFGFT-alles_De.tex',
    '201a_FFGFT-alles_De.tex',
    '201_FFGFT-alles_En.tex',
    '201a_FFGFT-alles_En.tex'
}

stats = {'normalized': 0, 'skipped': 0, 'errors': 0}
errors = []

for directory in [de_dir, en_dir]:
    if not directory.exists():
        continue
        
    for tex_file in sorted(directory.glob('*.tex')):
        # Skip excluded files
        if tex_file.name in excluded:
            stats['skipped'] += 1
            print(f"SKIP (excluded): {tex_file.name}")
            continue
            
        success, msg = normalize_preamble(tex_file)
        if success:
            stats['normalized'] += 1
            print(f"✓ {tex_file.name}")
        else:
            if "Already using" in msg:
                stats['skipped'] += 1
            else:
                stats['errors'] += 1
                errors.append((tex_file.name, msg))
                print(f"✗ {tex_file.name}: {msg}")

print("\n" + "=" * 80)
print(f"NORMALIZATION COMPLETE")
print("=" * 80)
print(f"Normalized: {stats['normalized']}")
print(f"Skipped: {stats['skipped']}")
print(f"Errors: {stats['errors']}")

if errors:
    print("\nErrors:")
    for name, msg in errors:
        print(f"  {name}: {msg}")
