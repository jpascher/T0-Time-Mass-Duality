#!/usr/bin/env python3
"""
Convert Markdown files from markdown_content/ to unified LaTeX files in unified_latex/
Uses universal_preamble.tex as the common header for all documents
"""

import os
import re
import sys
from pathlib import Path

def markdown_to_latex_body(md_content):
    """Convert Markdown content back to LaTeX body content"""
    latex = md_content
    
    # Convert Markdown headings to LaTeX sections
    latex = re.sub(r'^# (.+)$', r'\\section{\1}', latex, flags=re.MULTILINE)
    latex = re.sub(r'^## (.+)$', r'\\subsection{\1}', latex, flags=re.MULTILINE)
    latex = re.sub(r'^### (.+)$', r'\\subsubsection{\1}', latex, flags=re.MULTILINE)
    latex = re.sub(r'^#### (.+)$', r'\\paragraph{\1}', latex, flags=re.MULTILINE)
    latex = re.sub(r'^##### (.+)$', r'\\subparagraph{\1}', latex, flags=re.MULTILINE)
    
    # Convert Markdown formatting to LaTeX
    # Bold: **text** -> \textbf{text}
    latex = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', latex)
    
    # Italic: *text* -> \textit{text} (but preserve existing \textit)
    # This is tricky because we don't want to convert * in math mode
    latex = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'\\textit{\1}', latex)
    
    # Code: `text` -> \texttt{text}
    latex = re.sub(r'`([^`]+)`', r'\\texttt{\1}', latex)
    
    # Convert Markdown horizontal rules to \newpage
    latex = re.sub(r'^---+$', r'\\newpage', latex, flags=re.MULTILINE)
    
    # Math mode is already in LaTeX format, no conversion needed
    
    return latex.strip()

def read_universal_preamble():
    """Read the universal preamble file"""
    preamble_path = Path(__file__).parent / 'universal_preamble.tex'
    
    if not preamble_path.exists():
        print(f"Error: {preamble_path} does not exist")
        return None
    
    try:
        with open(preamble_path, 'r', encoding='utf-8') as f:
            preamble = f.read()
        return preamble.strip()
    except Exception as e:
        print(f"Error reading universal preamble: {e}")
        return None

def convert_file(input_path, output_path, preamble):
    """Convert a single Markdown file to LaTeX with universal preamble"""
    try:
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
            md_content = f.read()
        
        # Convert markdown to latex body
        latex_body = markdown_to_latex_body(md_content)
        
        # Construct full LaTeX document
        latex_document = f"{preamble}\n\n\\begin{{document}}\n\n{latex_body}\n\n\\end{{document}}\n"
        
        # Write output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(latex_document)
        
        return True
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False

def main():
    # Get repository root
    repo_root = Path(__file__).parent
    markdown_dir = repo_root / 'markdown_content'
    latex_dir = repo_root / 'unified_latex'
    
    if not markdown_dir.exists():
        print(f"Error: {markdown_dir} does not exist")
        print("Run convert_to_markdown.py first")
        return 1
    
    # Read universal preamble
    preamble = read_universal_preamble()
    if preamble is None:
        return 1
    
    # Create output directory
    latex_dir.mkdir(exist_ok=True)
    
    # Find all .md files
    md_files = list(markdown_dir.glob('*.md'))
    print(f"Found {len(md_files)} .md files in {markdown_dir}")
    
    converted = 0
    failed = 0
    
    for md_file in md_files:
        # Create output path with .tex extension
        tex_file = latex_dir / md_file.name.replace('.md', '.tex')
        
        print(f"Converting: {md_file.name} -> {tex_file.name}")
        
        if convert_file(md_file, tex_file, preamble):
            converted += 1
        else:
            failed += 1
    
    print(f"\nConversion complete:")
    print(f"  Converted: {converted}")
    print(f"  Failed: {failed}")
    print(f"  Output directory: {latex_dir}")
    
    return 0 if failed == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
