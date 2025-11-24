#!/usr/bin/env python3
"""
Convert LaTeX documents to Markdown
Extracts content between \begin{document} and \end{document}
Preserves mathematical notation and structure
"""

import os
import re
from pathlib import Path

def extract_latex_content(tex_content):
    """Extract content between \begin{document} and \end{document}"""
    # Find \begin{document}
    begin_match = re.search(r'\\begin\{document\}', tex_content)
    if not begin_match:
        return tex_content  # No \begin{document}, return as-is
    
    # Find \end{document}
    end_match = re.search(r'\\end\{document\}', tex_content)
    if not end_match:
        # Take everything after \begin{document}
        content = tex_content[begin_match.end():]
    else:
        # Extract content between
        content = tex_content[begin_match.end():end_match.start()]
    
    return content.strip()

def latex_to_markdown(tex_content):
    """Convert LaTeX content to Markdown"""
    # Extract document body
    content = extract_latex_content(tex_content)
    
    # Skip preamble commands if they appear after \begin{document}
    lines = content.split('\n')
    filtered_lines = []
    
    skip_patterns = [
        r'^\s*\\documentclass',
        r'^\s*\\usepackage',
        r'^\s*\\newcommand',
        r'^\s*\\renewcommand',
        r'^\s*\\definecolor',
        r'^\s*\\def\\',
        r'^\s*\\DeclareMathOperator',
        r'^\s*\\theoremstyle',
        r'^\s*\\newtheorem',
        r'^\s*\\pagestyle',
        r'^\s*\\fancyhead',
        r'^\s*\\fancyfoot',
    ]
    
    for line in lines:
        # Skip preamble commands
        if any(re.match(pattern, line) for pattern in skip_patterns):
            continue
        filtered_lines.append(line)
    
    content = '\n'.join(filtered_lines)
    
    # Convert LaTeX sectioning to Markdown
    content = re.sub(r'\\section\*?\{([^}]+)\}', r'# \1', content)
    content = re.sub(r'\\subsection\*?\{([^}]+)\}', r'## \1', content)
    content = re.sub(r'\\subsubsection\*?\{([^}]+)\}', r'### \1', content)
    content = re.sub(r'\\paragraph\{([^}]+)\}', r'#### \1', content)
    
    # Convert \maketitle (keep as comment for reference)
    content = re.sub(r'\\maketitle', '<!-- \\maketitle -->', content)
    
    # Convert \textbf and \textit
    content = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', content)
    content = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', content)
    
    # Keep LaTeX math as-is (markdown supports it)
    # Keep \begin{equation}, \begin{align}, etc.
    
    # Add LaTeX fence markers for better readability
    # But keep math environments as LaTeX
    
    return content.strip()

def convert_file(input_path, output_path):
    """Convert single .tex file to .md"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            tex_content = f.read()
        
        md_content = latex_to_markdown(tex_content)
        
        # Add header comment
        header = f"<!-- Converted from {input_path.name} -->\n\n"
        md_content = header + md_content
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return True
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False

def main():
    """Convert all .tex files in 2/tex/ to markdown_content/"""
    repo_root = Path(__file__).parent
    tex_dir = repo_root / '2' / 'tex'
    output_dir = repo_root / 'markdown_content'
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Find all .tex files
    tex_files = list(tex_dir.glob('*.tex'))
    print(f"Found {len(tex_files)} .tex files in {tex_dir}")
    
    success_count = 0
    for tex_file in sorted(tex_files):
        # Skip non-document files
        if tex_file.name in ['1.bat', '1.py', '1_sceleton.py']:
            continue
        
        # Create output filename
        md_file = output_dir / tex_file.name.replace('.tex', '.md')
        
        if convert_file(tex_file, md_file):
            success_count += 1
            if success_count % 20 == 0:
                print(f"Converted {success_count}/{len(tex_files)} files...")
    
    print(f"\nConversion complete!")
    print(f"Successfully converted {success_count} files to {output_dir}")
    print(f"Failed: {len(tex_files) - success_count}")

if __name__ == '__main__':
    main()
