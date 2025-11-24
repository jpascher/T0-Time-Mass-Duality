#!/usr/bin/env python3
"""
Convert Markdown files back to LaTeX with unified preamble
Creates new .tex files with consistent header from universal_preamble.tex
"""

import os
import re
from pathlib import Path

def markdown_to_latex_content(md_content):
    """Convert Markdown content back to LaTeX document body"""
    content = md_content
    
    # Remove conversion header comment
    content = re.sub(r'<!-- Converted from .* -->\s*', '', content)
    
    # Convert Markdown headings to LaTeX sectioning
    content = re.sub(r'^# (.+)$', r'\\section{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'\\subsection{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.+)$', r'\\subsubsection{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^#### (.+)$', r'\\paragraph{\1}', content, flags=re.MULTILINE)
    
    # Convert back maketitle comments
    content = re.sub(r'<!-- \\maketitle -->', r'\\maketitle', content)
    
    # Convert **bold** and *italic* back (but be careful with math)
    # Only convert if not inside $ or $$ or \begin{...}
    # Simple approach: convert in text paragraphs
    lines = content.split('\n')
    converted_lines = []
    in_math_env = False
    
    for line in lines:
        # Check if we're in a math environment
        if re.match(r'\\begin\{(equation|align|gather|multline|split)', line):
            in_math_env = True
        elif re.match(r'\\end\{(equation|align|gather|multline|split)', line):
            in_math_env = False
        
        # Only convert markdown formatting outside math environments
        if not in_math_env and not re.search(r'\$.*\$', line):
            line = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', line)
            line = re.sub(r'\*([^*]+)\*', r'\\textit{\1}', line)
        
        converted_lines.append(line)
    
    content = '\n'.join(converted_lines)
    
    return content.strip()

def create_unified_latex(md_path, output_path, preamble):
    """Create unified LaTeX file with common preamble"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        latex_body = markdown_to_latex_content(md_content)
        
        # Create full LaTeX document
        full_doc = f"{preamble}\n\n\\begin{{document}}\n\n{latex_body}\n\n\\end{{document}}\n"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_doc)
        
        return True
    except Exception as e:
        print(f"Error converting {md_path}: {e}")
        return False

def load_preamble(preamble_file):
    """Load universal preamble from file"""
    try:
        with open(preamble_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract everything before \begin{document}
        match = re.search(r'\\begin\{document\}', content)
        if match:
            return content[:match.start()].strip()
        else:
            # No \begin{document}, assume entire file is preamble
            return content.strip()
    except Exception as e:
        print(f"Error loading preamble: {e}")
        return None

def main():
    """Convert all .md files in markdown_content/ to unified_latex/"""
    repo_root = Path(__file__).parent
    md_dir = repo_root / 'markdown_content'
    output_dir = repo_root / 'unified_latex'
    preamble_file = repo_root / 'universal_preamble.tex'
    
    # Load universal preamble
    print(f"Loading universal preamble from {preamble_file}")
    preamble = load_preamble(preamble_file)
    if not preamble:
        print("ERROR: Failed to load preamble!")
        return
    
    print(f"Loaded preamble ({len(preamble)} characters)")
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Find all .md files
    md_files = list(md_dir.glob('*.md'))
    print(f"Found {len(md_files)} .md files in {md_dir}")
    
    success_count = 0
    for md_file in sorted(md_files):
        # Create output filename
        tex_file = output_dir / md_file.name.replace('.md', '.tex')
        
        if create_unified_latex(md_file, tex_file, preamble):
            success_count += 1
            if success_count % 20 == 0:
                print(f"Converted {success_count}/{len(md_files)} files...")
    
    print(f"\nConversion complete!")
    print(f"Successfully converted {success_count} files to {output_dir}")
    print(f"Failed: {len(md_files) - success_count}")

if __name__ == '__main__':
    main()
