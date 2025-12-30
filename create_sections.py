#!/usr/bin/env python3
"""
Extract content from LaTeX chapter files to create section files
that can be included in main documents via \\input{}
"""
import os
import re

def extract_document_content(tex_file_path):
    """Extract content between \\begin{document} and \\end{document}"""
    with open(tex_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find content between \begin{document} and \end{document}
    match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if match:
        doc_content = match.group(1).strip()
        # Remove \maketitle if present at the start
        doc_content = re.sub(r'^\s*\\maketitle\s*', '', doc_content, flags=re.MULTILINE)
        return doc_content
    return None

def create_section_file(source_file, output_file):
    """Create a section file from a chapter file"""
    content = extract_document_content(source_file)
    if content:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content + '\n')
        return True
    return False

# Process German files
de_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_DVFT/tex_kapitel'
de_files = [
    '202a_1-11_De.tex',
] + [f'kapitel_{i}a_De.tex' for i in range(12, 45)]

print("Creating German section files...")
for filename in de_files:
    source = os.path.join(de_dir, filename)
    if os.path.exists(source):
        output = source.replace('.tex', '_section.tex')
        if create_section_file(source, output):
            print(f"  ✓ {filename} -> {os.path.basename(output)}")
        else:
            print(f"  ✗ Failed: {filename}")
    else:
        print(f"  ⚠ Not found: {filename}")

# Process English files
en_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/en_DVFT/tex_kapitel'
en_files = [
    '202a_1-11_En.tex',
] + [f'kapitel_{i}a_En.tex' for i in range(12, 45)]

print("\nCreating English section files...")
for filename in en_files:
    source = os.path.join(en_dir, filename)
    if os.path.exists(source):
        output = source.replace('.tex', '_section.tex')
        if create_section_file(source, output):
            print(f"  ✓ {filename} -> {os.path.basename(output)}")
        else:
            print(f"  ✗ Failed: {filename}")
    else:
        print(f"  ⚠ Not found: {filename}")

print("\nSection files created successfully!")
