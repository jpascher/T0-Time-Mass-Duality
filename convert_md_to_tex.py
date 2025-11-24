#!/usr/bin/env python3
"""
Convert Markdown documents back to LaTeX format with unified preamble.
Uses the universal_preamble.tex as the header for all documents.
"""

import os
import re
import sys
from pathlib import Path

def read_universal_preamble():
    """Read the universal preamble template"""
    preamble_path = Path(__file__).parent / 'universal_preamble.tex'
    if not preamble_path.exists():
        print(f"Error: universal_preamble.tex not found at {preamble_path}")
        return None
    
    with open(preamble_path, 'r', encoding='utf-8') as f:
        return f.read()

def markdown_to_latex(md_content, title):
    """Convert Markdown content back to LaTeX"""
    content = md_content
    
    # Skip metadata header (lines starting with # and containing "Converted from")
    lines = content.split('\n')
    start_idx = 0
    for i, line in enumerate(lines):
        if line.strip() == '---' and i < 10:
            start_idx = i + 1
            break
    
    content = '\n'.join(lines[start_idx:]).strip()
    
    # Convert Markdown headings to LaTeX sections
    content = re.sub(r'^# (.+)$', r'\\chapter{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'\\section{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.+)$', r'\\subsection{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^#### (.+)$', r'\\subsubsection{\1}', content, flags=re.MULTILINE)
    
    # Convert Markdown formatting to LaTeX
    content = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', content)
    content = re.sub(r'\*(.+?)\*', r'\\textit{\1}', content)
    
    # Convert lists (simple conversion)
    content = re.sub(r'^- (.+)$', r'\\item \1', content, flags=re.MULTILINE)
    
    # Wrap consecutive \item commands in itemize environment
    lines = content.split('\n')
    in_list = False
    result = []
    for line in lines:
        if line.strip().startswith('\\item'):
            if not in_list:
                result.append('\\begin{itemize}')
                in_list = True
            result.append(line)
        else:
            if in_list:
                result.append('\\end{itemize}')
                in_list = False
            result.append(line)
    
    if in_list:
        result.append('\\end{itemize}')
    
    content = '\n'.join(result)
    
    # Add title and maketitle
    doc_title = title.replace('_', ' ')
    title_section = f"\\title{{{doc_title}}}\n"
    title_section += "\\author{Johann Pascher}\n"
    title_section += "\\date{\\today}\n\n"
    
    return title_section, content

def create_unified_latex(md_path, output_path, preamble):
    """Create a unified LaTeX document from Markdown"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        title = md_path.stem
        title_section, body_content = markdown_to_latex(md_content, title)
        
        # Build complete LaTeX document
        latex_doc = preamble + '\n\n'
        latex_doc += title_section
        latex_doc += '\\begin{document}\n\n'
        latex_doc += '\\maketitle\n'
        latex_doc += '\\tableofcontents\n\n'
        latex_doc += body_content
        latex_doc += '\n\n\\end{document}\n'
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(latex_doc)
        
        return True
    except Exception as e:
        print(f"Error converting {md_path}: {e}")
        return False

def main():
    repo_root = Path(__file__).parent
    source_dir = repo_root / 'markdown_content'
    output_dir = repo_root / 'unified_latex'
    
    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        print("Please run convert_tex_to_md.py first")
        return 1
    
    preamble = read_universal_preamble()
    if preamble is None:
        return 1
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    md_files = list(source_dir.glob('*.md'))
    print(f"Found {md_files} .md files to convert")
    
    success_count = 0
    for md_file in md_files:
        tex_file = output_dir / f"{md_file.stem}.tex"
        if create_unified_latex(md_file, tex_file, preamble):
            success_count += 1
            print(f"✓ {md_file.name} → {tex_file.name}")
        else:
            print(f"✗ {md_file.name}")
    
    print(f"\nConverted {success_count}/{len(md_files)} files successfully")
    
    # Create a master book file
    create_master_book(output_dir, md_files, preamble)
    
    return 0

def create_master_book(output_dir, md_files, preamble):
    """Create a master book that includes all documents"""
    master_file = output_dir / 'T0_Complete_Book.tex'
    
    book_content = preamble + '\n\n'
    book_content += '\\title{T0 Theory - Complete Collection}\n'
    book_content += '\\author{Johann Pascher}\n'
    book_content += '\\date{\\today}\n\n'
    book_content += '\\begin{document}\n\n'
    book_content += '\\maketitle\n'
    book_content += '\\tableofcontents\n\n'
    
    for md_file in sorted(md_files):
        tex_name = f"{md_file.stem}.tex"
        book_content += f'\\input{{{tex_name}}}\n'
        book_content += '\\clearpage\n\n'
    
    book_content += '\\end{document}\n'
    
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write(book_content)
    
    print(f"\n✓ Created master book: {master_file.name}")

if __name__ == '__main__':
    sys.exit(main())
