#!/usr/bin/env python3
"""
Convert LaTeX files from 2/tex/ to Markdown files in markdown_content/
Extracts only the document body (content between \begin{document} and \end{document})
and converts LaTeX commands to Markdown where possible
"""

import os
import re
import sys
from pathlib import Path

def extract_document_body(tex_content):
    """Extract content between \begin{document} and \end{document}"""
    # Find \begin{document}
    begin_match = re.search(r'\\begin\{document\}', tex_content, re.DOTALL)
    if not begin_match:
        return tex_content  # No \begin{document}, return as is
    
    start = begin_match.end()
    
    # Find \end{document}
    end_match = re.search(r'\\end\{document\}', tex_content[start:], re.DOTALL)
    if not end_match:
        return tex_content[start:]  # No \end{document}, return from \begin{document} onwards
    
    end = start + end_match.start()
    return tex_content[start:end].strip()

def latex_to_markdown(latex_content):
    """Convert LaTeX content to Markdown"""
    md = latex_content
    
    # Remove \maketitle, \tableofcontents
    md = re.sub(r'\\maketitle\s*', '', md)
    md = re.sub(r'\\tableofcontents\s*', '', md)
    
    # Convert sections
    md = re.sub(r'\\section\*?\{([^}]+)\}', r'# \1', md)
    md = re.sub(r'\\subsection\*?\{([^}]+)\}', r'## \1', md)
    md = re.sub(r'\\subsubsection\*?\{([^}]+)\}', r'### \1', md)
    md = re.sub(r'\\paragraph\{([^}]+)\}', r'#### \1', md)
    md = re.sub(r'\\subparagraph\{([^}]+)\}', r'##### \1', md)
    
    # Convert text formatting
    md = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', md)
    md = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', md)
    md = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', md)
    md = re.sub(r'\\texttt\{([^}]+)\}', r'`\1`', md)
    
    # Keep math environments as LaTeX (Markdown supports it)
    # No conversion needed for $...$ and $$...$$
    
    # Convert itemize/enumerate to Markdown lists
    # This is complex, so we'll keep the LaTeX for now
    
    # Remove simple LaTeX commands that don't need conversion
    md = re.sub(r'\\noindent\s*', '', md)
    md = re.sub(r'\\newpage\s*', '\n\n---\n\n', md)
    md = re.sub(r'\\clearpage\s*', '\n\n---\n\n', md)
    
    # Clean up multiple blank lines
    md = re.sub(r'\n{3,}', '\n\n', md)
    
    return md.strip()

def convert_file(input_path, output_path):
    """Convert a single LaTeX file to Markdown"""
    try:
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
            tex_content = f.read()
        
        # Extract body
        body = extract_document_body(tex_content)
        
        # Convert to markdown
        md_content = latex_to_markdown(body)
        
        # Write output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return True
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False

def main():
    # Get repository root
    repo_root = Path(__file__).parent
    tex_dir = repo_root / '2' / 'tex'
    markdown_dir = repo_root / 'markdown_content'
    
    if not tex_dir.exists():
        print(f"Error: {tex_dir} does not exist")
        return 1
    
    # Create output directory
    markdown_dir.mkdir(exist_ok=True)
    
    # Find all .tex files
    tex_files = list(tex_dir.glob('*.tex'))
    print(f"Found {len(tex_files)} .tex files in {tex_dir}")
    
    converted = 0
    failed = 0
    
    for tex_file in tex_files:
        # Create output path with .md extension
        md_file = markdown_dir / tex_file.name.replace('.tex', '.md')
        
        print(f"Converting: {tex_file.name} -> {md_file.name}")
        
        if convert_file(tex_file, md_file):
            converted += 1
        else:
            failed += 1
    
    print(f"\nConversion complete:")
    print(f"  Converted: {converted}")
    print(f"  Failed: {failed}")
    print(f"  Output directory: {markdown_dir}")
    
    return 0 if failed == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
