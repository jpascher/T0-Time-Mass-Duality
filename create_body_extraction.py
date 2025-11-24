#!/usr/bin/env python3
"""
Extract document bodies from LaTeX files without modifying originals.
Creates wrapper files that use docmute package to include only document content.
"""

import os
import re
from pathlib import Path

def create_body_wrapper_file(source_file, output_file):
    """Create a wrapper file that includes only the document body."""
    with open(output_file, 'w', encoding='utf-8') as f:
        # The wrapper uses a simple approach: include the source file
        # The main document will handle the preamble
        f.write(f"% Auto-generated wrapper for {os.path.basename(source_file)}\n")
        f.write(f"% Includes only document body content\n\n")
        # We'll use a custom approach: read the file and extract body
        with open(source_file, 'r', encoding='utf-8', errors='ignore') as src:
            content = src.read()
            
        # Find content between \begin{document} and \end{document}
        begin_match = re.search(r'\\begin\{document\}', content)
        end_match = re.search(r'\\end\{document\}', content)
        
        if begin_match and end_match:
            body = content[begin_match.end():end_match.start()]
            f.write(body)
        else:
            f.write(f"% Warning: Could not extract body from {source_file}\n")
            f.write("\\section{Document Content Unavailable}\n")
            f.write(f"The document {os.path.basename(source_file)} could not be processed.\\par\n")

# Create output directory
output_dir = Path("2/tex_bodies")
output_dir.mkdir(exist_ok=True)

# List of all tex files to process
tex_files = [
    "T0_Grundlagen_en.tex",
    "T0_Modell_Uebersicht_En.tex",
    # Add more files as needed
]

# Process files in 2/tex directory
tex_dir = Path("2/tex")
if tex_dir.exists():
    tex_files = list(tex_dir.glob("*.tex"))
    print(f"Found {len(tex_files)} .tex files in 2/tex/")
    
    for tex_file in tex_files:
        output_file = output_dir / tex_file.name
        try:
            create_body_wrapper_file(tex_file, output_file)
            print(f"Created: {output_file}")
        except Exception as e:
            print(f"Error processing {tex_file}: {e}")

print(f"\nBody extraction complete. Files saved to {output_dir}/")
