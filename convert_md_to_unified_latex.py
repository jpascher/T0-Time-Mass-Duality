#!/usr/bin/env python3
"""
Convert Markdown files from markdown_content/ to unified LaTeX format in unified_latex/
Uses the universal_preamble.tex as the consistent header for all documents
"""

import os
import re
from pathlib import Path

def read_universal_preamble():
    """Read the universal preamble template"""
    repo_root = Path(__file__).parent
    preamble_path = repo_root / 'universal_preamble.tex'
    
    if not preamble_path.exists():
        raise FileNotFoundError("universal_preamble.tex not found")
    
    with open(preamble_path, 'r', encoding='utf-8') as f:
        preamble = f.read()
    
    # Find where the preamble ends (before \begin{document})
    match = re.search(r'\\begin\{document\}', preamble)
    if match:
        return preamble[:match.start()].strip()
    return preamble.strip()

def convert_markdown_to_latex(md_content):
    """Convert Markdown content back to LaTeX format"""
    latex_content = md_content
    
    # Convert headers back to LaTeX
    latex_content = re.sub(r'^# (.+)$', r'\\chapter{\1}', latex_content, flags=re.MULTILINE)
    latex_content = re.sub(r'^## (.+)$', r'\\section{\1}', latex_content, flags=re.MULTILINE)
    latex_content = re.sub(r'^### (.+)$', r'\\subsection{\1}', latex_content, flags=re.MULTILINE)
    latex_content = re.sub(r'^#### (.+)$', r'\\subsubsection{\1}', latex_content, flags=re.MULTILINE)
    
    # Convert markdown bold/italic back to LaTeX
    latex_content = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', latex_content)
    latex_content = re.sub(r'\*([^*]+)\*', r'\\textit{\1}', latex_content)
    
    # Convert markdown lists back to LaTeX
    # This is a simplified conversion - complex nested lists may need refinement
    in_list = False
    lines = latex_content.split('\n')
    new_lines = []
    
    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                new_lines.append('\\begin{itemize}')
                in_list = True
            new_lines.append('\\item ' + line.strip()[2:])
        else:
            if in_list and line.strip():
                new_lines.append('\\end{itemize}')
                in_list = False
            new_lines.append(line)
    
    if in_list:
        new_lines.append('\\end{itemize}')
    
    latex_content = '\n'.join(new_lines)
    
    # Convert horizontal rules to \newpage
    latex_content = re.sub(r'\n---\n', r'\n\\newpage\n', latex_content)
    
    return latex_content

def create_unified_latex_document(title, md_content, preamble):
    """Create a complete LaTeX document with unified preamble"""
    # Convert markdown to LaTeX
    latex_body = convert_markdown_to_latex(md_content)
    
    # Build complete document
    document = f"{preamble}\n\n"
    document += "\\begin{document}\n\n"
    document += f"\\title{{{title}}}\n"
    document += "\\author{Johann Pascher}\n"
    document += "\\date{\\today}\n"
    document += "\\maketitle\n"
    document += "\\tableofcontents\n"
    document += "\\newpage\n\n"
    document += latex_body
    document += "\n\n\\end{document}\n"
    
    return document

def process_md_file(md_path, latex_output_dir, preamble):
    """Process a single .md file and convert to unified LaTeX"""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Extract title from filename (remove _De/_En suffix if present)
        title = md_path.stem
        title = re.sub(r'_(De|En)$', '', title)
        title = title.replace('_', ' ')
        
        # Create unified LaTeX document
        latex_content = create_unified_latex_document(title, md_content, preamble)
        
        # Create output filename
        latex_filename = md_path.stem + '.tex'
        latex_path = latex_output_dir / latex_filename
        
        # Write LaTeX file
        with open(latex_path, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"Converted: {md_path.name} → {latex_filename}")
        return True
        
    except Exception as e:
        print(f"Error processing {md_path.name}: {e}")
        return False

def main():
    # Setup directories
    repo_root = Path(__file__).parent
    md_dir = repo_root / 'markdown_content'
    latex_dir = repo_root / 'unified_latex'
    
    # Create unified LaTeX output directory
    latex_dir.mkdir(exist_ok=True)
    
    # Read universal preamble
    try:
        preamble = read_universal_preamble()
        print(f"Loaded universal preamble ({len(preamble)} characters)")
    except Exception as e:
        print(f"Error loading preamble: {e}")
        return
    
    # Find all .md files
    md_files = list(md_dir.glob('*.md'))
    print(f"Found {len(md_files)} .md files in {md_dir}")
    
    # Process each file
    success_count = 0
    for md_file in sorted(md_files):
        if process_md_file(md_file, latex_dir, preamble):
            success_count += 1
    
    print(f"\nConversion complete: {success_count}/{len(md_files)} files converted successfully")
    print(f"Unified LaTeX files saved to: {latex_dir}")

if __name__ == '__main__':
    main()
