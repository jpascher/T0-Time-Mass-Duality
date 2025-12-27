#!/usr/bin/env python3
"""
Extract content from standalone LaTeX chapter files for inclusion in master document.
Removes \documentclass, preamble, \begin{document}, \maketitle, and \end{document}.
"""

import os
import re

def extract_content(input_file, output_file):
    """Extract only the content between \begin{document} and \end{document}."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find content between \begin{document} and \end{document}
    match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if not match:
        print(f"Warning: Could not find document environment in {input_file}")
        return False
    
    extracted = match.group(1).strip()
    
    # Remove \maketitle if present
    extracted = re.sub(r'\\maketitle\s*', '', extracted)
    
    # Write extracted content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(extracted + '\n')
    
    return True

# Process all Kapitel_*_De.tex files
source_dir = '.'
output_dir = 'content_only'
os.makedirs(output_dir, exist_ok=True)

files_processed = 0
for filename in sorted(os.listdir(source_dir)):
    if filename.startswith('Kapitel_') and filename.endswith('_De.tex'):
        input_path = os.path.join(source_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        if extract_content(input_path, output_path):
            files_processed += 1
            print(f"Processed: {filename}")

print(f"\nTotal files processed: {files_processed}")
print(f"Content-only files saved to: {output_dir}/")
