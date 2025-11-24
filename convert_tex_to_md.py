#!/usr/bin/env python3
"""
Convert all LaTeX documents from 2/tex/ to Markdown format in markdown_content/
Extracts content between \begin{document} and \end{document}, preserving structure
"""

import os
import re
from pathlib import Path

def extract_document_body(tex_content):
    """Extract content between \begin{document} and \end{document}"""
    # Find the document body
    begin_match = re.search(r'\\begin\{document\}', tex_content)
    end_match = re.search(r'\\end\{document\}', tex_content)
    
    if not begin_match or not end_match:
        return None
    
    body = tex_content[begin_match.end():end_match.start()].strip()
    return body

def convert_latex_to_markdown(latex_body):
    """Convert LaTeX content to Markdown format"""
    md_content = latex_body
    
    # Convert section commands
    md_content = re.sub(r'\\chapter\{([^}]+)\}', r'# \1', md_content)
    md_content = re.sub(r'\\section\{([^}]+)\}', r'## \1', md_content)
    md_content = re.sub(r'\\subsection\{([^}]+)\}', r'### \1', md_content)
    md_content = re.sub(r'\\subsubsection\{([^}]+)\}', r'#### \1', md_content)
    
    # Convert \maketitle, \tableofcontents
    md_content = re.sub(r'\\maketitle', '', md_content)
    md_content = re.sub(r'\\tableofcontents', '', md_content)
    
    # Convert basic formatting
    md_content = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', md_content)
    md_content = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', md_content)
    md_content = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', md_content)
    
    # Keep math expressions as-is (they're compatible with many MD renderers)
    # $...$ and $$...$$ are kept
    
    # Convert itemize/enumerate to markdown lists
    md_content = re.sub(r'\\begin\{itemize\}', '', md_content)
    md_content = re.sub(r'\\end\{itemize\}', '', md_content)
    md_content = re.sub(r'\\begin\{enumerate\}', '', md_content)
    md_content = re.sub(r'\\end\{enumerate\}', '', md_content)
    md_content = re.sub(r'\\item\s+', '- ', md_content)
    
    # Remove common LaTeX commands that don't translate well
    md_content = re.sub(r'\\newpage', '\n\n---\n\n', md_content)
    md_content = re.sub(r'\\clearpage', '\n\n---\n\n', md_content)
    
    # Clean up excessive whitespace
    md_content = re.sub(r'\n\n\n+', '\n\n', md_content)
    
    return md_content.strip()

def process_tex_file(tex_path, md_output_dir):
    """Process a single .tex file and convert to markdown"""
    try:
        with open(tex_path, 'r', encoding='utf-8') as f:
            tex_content = f.read()
        
        # Extract document body
        body = extract_document_body(tex_content)
        if body is None:
            print(f"Warning: Could not find document body in {tex_path.name}")
            return False
        
        # Convert to markdown
        md_content = convert_latex_to_markdown(body)
        
        # Create output filename
        md_filename = tex_path.stem + '.md'
        md_path = md_output_dir / md_filename
        
        # Write markdown file
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Converted: {tex_path.name} → {md_filename}")
        return True
        
    except Exception as e:
        print(f"Error processing {tex_path.name}: {e}")
        return False

def main():
    # Setup directories
    repo_root = Path(__file__).parent
    tex_dir = repo_root / '2' / 'tex'
    md_dir = repo_root / 'markdown_content'
    
    # Create markdown output directory
    md_dir.mkdir(exist_ok=True)
    
    # Find all .tex files
    tex_files = list(tex_dir.glob('*.tex'))
    print(f"Found {len(tex_files)} .tex files in {tex_dir}")
    
    # Process each file
    success_count = 0
    for tex_file in sorted(tex_files):
        if process_tex_file(tex_file, md_dir):
            success_count += 1
    
    print(f"\nConversion complete: {success_count}/{len(tex_files)} files converted successfully")
    print(f"Markdown files saved to: {md_dir}")

if __name__ == '__main__':
    main()
