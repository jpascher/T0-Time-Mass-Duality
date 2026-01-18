#!/usr/bin/env python3
import os
import re
from pathlib import Path

def check_preamble(filepath):
    """Check what preamble a tex file uses"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(2000)  # First 2000 chars should contain preamble
            
        # Look for \input commands
        input_pattern = r'\\input\{([^}]+)\}'
        inputs = re.findall(input_pattern, content)
        
        # Look for \usepackage in document preamble (before \begin{document})
        doc_start = content.find(r'\begin{document}')
        if doc_start > 0:
            preamble = content[:doc_start]
        else:
            preamble = content
            
        has_usepackage = bool(re.search(r'\\usepackage', preamble))
        
        return {
            'inputs': inputs,
            'has_usepackage': has_usepackage,
            'has_inputenc': 'inputenc' in preamble,
            'has_fontenc': 'fontenc' in preamble,
        }
    except Exception as e:
        return {'error': str(e)}

# Check all standalone documents
de_dir = Path('2/tex-n/de_standalone')
en_dir = Path('2/tex-n/en_standalone')

results = {
    'correct_ebook': [],
    'correct_shared': [],
    'old_preambles': [],
    'inline_packages': [],
    'errors': []
}

for directory in [de_dir, en_dir]:
    if not directory.exists():
        continue
        
    for tex_file in sorted(directory.glob('*.tex')):
        info = check_preamble(tex_file)
        
        if 'error' in info:
            results['errors'].append((str(tex_file), info['error']))
            continue
            
        # Categorize based on preamble type
        inputs = info['inputs']
        
        if any('T0_preamble_shared-ebook' in inp for inp in inputs):
            results['correct_ebook'].append(str(tex_file))
        elif any('T0_preamble_shared_De' in inp or 'T0_preamble_shared_En' in inp for inp in inputs):
            if not any('ebook' in inp or 'a4' in inp for inp in inputs):
                results['correct_shared'].append(str(tex_file))
        elif info['has_usepackage'] or info['has_inputenc'] or info['has_fontenc']:
            results['inline_packages'].append((str(tex_file), inputs))
        elif inputs:
            results['old_preambles'].append((str(tex_file), inputs))

# Print summary
print("=" * 80)
print("PREAMBLE ANALYSIS RESULTS")
print("=" * 80)
print(f"\n✅ Already using ebook preamble: {len(results['correct_ebook'])}")
print(f"✓  Using shared preamble (non-ebook): {len(results['correct_shared'])}")
print(f"⚠  Using inline packages: {len(results['inline_packages'])}")
print(f"⚠  Using old/local preambles: {len(results['old_preambles'])}")
print(f"❌ Errors: {len(results['errors'])}")

if results['correct_shared']:
    print("\n" + "=" * 80)
    print("FILES USING SHARED PREAMBLE (should switch to ebook):")
    print("=" * 80)
    for f in results['correct_shared'][:20]:
        print(f"  {f}")
    if len(results['correct_shared']) > 20:
        print(f"  ... and {len(results['correct_shared']) - 20} more")

if results['inline_packages']:
    print("\n" + "=" * 80)
    print("FILES WITH INLINE PACKAGES (need preamble replacement):")
    print("=" * 80)
    for f, inputs in results['inline_packages'][:20]:
        print(f"  {f}")
        if inputs:
            print(f"    Current inputs: {inputs}")
    if len(results['inline_packages']) > 20:
        print(f"  ... and {len(results['inline_packages']) - 20} more")

if results['old_preambles']:
    print("\n" + "=" * 80)
    print("FILES WITH OLD/LOCAL PREAMBLES (need preamble replacement):")
    print("=" * 80)
    for f, inputs in results['old_preambles'][:20]:
        print(f"  {f}")
        print(f"    Current inputs: {inputs}")
    if len(results['old_preambles']) > 20:
        print(f"  ... and {len(results['old_preambles']) - 20} more")

if results['errors']:
    print("\n" + "=" * 80)
    print("FILES WITH ERRORS:")
    print("=" * 80)
    for f, err in results['errors']:
        print(f"  {f}: {err}")

print("\n" + "=" * 80)
print(f"TOTAL FILES TO FIX: {len(results['correct_shared']) + len(results['inline_packages']) + len(results['old_preambles'])}")
print("=" * 80)
