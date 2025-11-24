#!/usr/bin/env python3
"""
Convert LaTeX documents to Markdown and then back to unified LaTeX files.
This script performs a three-stage conversion:
1. Extract document body from original .tex files in 2/tex/
2. Convert to Markdown format in markdown_content/
3. Convert back to LaTeX with universal preamble in unified_latex/
"""

import os
import re
import shutil
from pathlib import Path

# Define directories
SOURCE_DIR = Path("2/tex")
MARKDOWN_DIR = Path("markdown_content")
UNIFIED_LATEX_DIR = Path("unified_latex")
PREAMBLE_FILE = Path("universal_preamble.tex")

def extract_document_body(tex_content):
    """Extract content between \\begin{document} and \\end{document}"""
    # Find the document environment
    begin_match = re.search(r'\\begin\{document\}', tex_content)
    end_match = re.search(r'\\end\{document\}', tex_content)
    
    if begin_match and end_match:
        start = begin_match.end()
        end = end_match.start()
        body = tex_content[start:end].strip()
        return body
    
    # If no document environment found, return the whole content (after stripping preamble)
    # Try to find where content starts (after the preamble)
    lines = tex_content.split('\n')
    content_started = False
    body_lines = []
    
    for line in lines:
        # Skip preamble commands
        if line.strip().startswith('\\documentclass') or \
           line.strip().startswith('\\usepackage') or \
           line.strip().startswith('\\newcommand') or \
           line.strip().startswith('\\def') or \
           line.strip().startswith('\\title') or \
           line.strip().startswith('\\author') or \
           line.strip().startswith('\\date'):
            continue
        if line.strip().startswith('\\begin{document}'):
            content_started = True
            continue
        if line.strip().startswith('\\end{document}'):
            break
        if content_started or (line.strip() and not line.strip().startswith('\\')):
            body_lines.append(line)
    
    return '\n'.join(body_lines).strip()

def tex_to_markdown(tex_content):
    """Convert LaTeX body content to Markdown format"""
    md_content = tex_content
    
    # Remove \\maketitle
    md_content = re.sub(r'\\maketitle\s*', '', md_content)
    
    # Convert sections
    md_content = re.sub(r'\\chapter\{([^}]+)\}', r'# \1', md_content)
    md_content = re.sub(r'\\section\{([^}]+)\}', r'## \1', md_content)
    md_content = re.sub(r'\\subsection\{([^}]+)\}', r'### \1', md_content)
    md_content = re.sub(r'\\subsubsection\{([^}]+)\}', r'#### \1', md_content)
    
    # Convert text formatting
    md_content = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', md_content)
    md_content = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', md_content)
    md_content = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', md_content)
    
    # Convert itemize and enumerate to lists
    md_content = re.sub(r'\\begin\{itemize\}', '', md_content)
    md_content = re.sub(r'\\end\{itemize\}', '', md_content)
    md_content = re.sub(r'\\begin\{enumerate\}', '', md_content)
    md_content = re.sub(r'\\end\{enumerate\}', '', md_content)
    md_content = re.sub(r'\\item\s+', r'- ', md_content)
    
    # Keep math environments as LaTeX (markdown supports inline LaTeX)
    # Just make sure equations are properly formatted
    
    # Remove excessive blank lines
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)
    
    return md_content.strip()

def markdown_to_tex(md_content, original_filename):
    """Convert Markdown content back to LaTeX format (body only)"""
    tex_content = md_content
    
    # Convert headings back
    tex_content = re.sub(r'^# (.+)$', r'\\chapter{\1}', tex_content, flags=re.MULTILINE)
    tex_content = re.sub(r'^## (.+)$', r'\\section{\1}', tex_content, flags=re.MULTILINE)
    tex_content = re.sub(r'^### (.+)$', r'\\subsection{\1}', tex_content, flags=re.MULTILINE)
    tex_content = re.sub(r'^#### (.+)$', r'\\subsubsection{\1}', tex_content, flags=re.MULTILINE)
    
    # Convert text formatting back (be careful with nested formatting)
    # First handle **text** that's not inside math
    def replace_bold(match):
        text = match.group(1)
        if '$' in text:  # Don't convert if inside math
            return match.group(0)
        return f'\\textbf{{{text}}}'
    
    def replace_italic(match):
        text = match.group(1)
        if '$' in text:  # Don't convert if inside math
            return match.group(0)
        return f'\\textit{{{text}}}'
    
    tex_content = re.sub(r'\*\*([^*]+)\*\*', replace_bold, tex_content)
    tex_content = re.sub(r'\*([^*\n]+)\*', replace_italic, tex_content)
    
    # Convert lists back
    tex_content = re.sub(r'^- (.+)$', r'\\item \1', tex_content, flags=re.MULTILINE)
    
    # Wrap consecutive \item commands in itemize environment
    lines = tex_content.split('\n')
    result_lines = []
    in_list = False
    
    for line in lines:
        if line.strip().startswith('\\item'):
            if not in_list:
                result_lines.append('\\begin{itemize}')
                in_list = True
            result_lines.append(line)
        else:
            if in_list:
                result_lines.append('\\end{itemize}')
                in_list = False
            result_lines.append(line)
    
    if in_list:
        result_lines.append('\\end{itemize}')
    
    tex_content = '\n'.join(result_lines)
    
    return tex_content.strip()

def load_universal_preamble():
    """Load the universal preamble content"""
    if not PREAMBLE_FILE.exists():
        raise FileNotFoundError(f"Universal preamble file not found: {PREAMBLE_FILE}")
    
    with open(PREAMBLE_FILE, 'r', encoding='utf-8') as f:
        preamble = f.read()
    
    # Remove \begin{document} if it exists in the preamble file
    preamble = re.sub(r'\\begin\{document\}.*', '', preamble, flags=re.DOTALL)
    
    return preamble.strip()

def process_tex_file(tex_file_path):
    """Process a single .tex file through the conversion pipeline"""
    print(f"Processing: {tex_file_path.name}")
    
    # Read original .tex file
    try:
        with open(tex_file_path, 'r', encoding='utf-8') as f:
            tex_content = f.read()
    except Exception as e:
        print(f"  Error reading {tex_file_path}: {e}")
        return False
    
    # Step 1: Extract document body
    body_content = extract_document_body(tex_content)
    if not body_content:
        print(f"  Warning: No content extracted from {tex_file_path.name}")
        body_content = tex_content  # Use full content as fallback
    
    # Step 2: Convert to Markdown
    md_content = tex_to_markdown(body_content)
    
    # Save Markdown file
    md_file = MARKDOWN_DIR / tex_file_path.name.replace('.tex', '.md')
    try:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f"<!-- Converted from {tex_file_path.name} -->\n\n")
            f.write(md_content)
        print(f"  → Created: {md_file.name}")
    except Exception as e:
        print(f"  Error writing Markdown {md_file}: {e}")
        return False
    
    # Step 3: Convert Markdown back to LaTeX body
    tex_body = markdown_to_tex(md_content, tex_file_path.name)
    
    # Step 4: Create unified LaTeX file with universal preamble
    try:
        preamble = load_universal_preamble()
        
        # Adjust babel language based on filename
        if '_De' in tex_file_path.name:
            preamble = preamble.replace('[english]', '[ngerman]')
        
        unified_content = f"{preamble}\n\n\\begin{{document}}\n\n{tex_body}\n\n\\end{{document}}\n"
        
        unified_file = UNIFIED_LATEX_DIR / tex_file_path.name
        with open(unified_file, 'w', encoding='utf-8') as f:
            f.write(unified_content)
        print(f"  → Created: {unified_file.name}")
    except Exception as e:
        print(f"  Error creating unified LaTeX {unified_file}: {e}")
        return False
    
    return True

def main():
    """Main conversion pipeline"""
    print("="*70)
    print("LaTeX to Markdown to Unified LaTeX Conversion Pipeline")
    print("="*70)
    print()
    
    # Create output directories
    MARKDOWN_DIR.mkdir(exist_ok=True)
    UNIFIED_LATEX_DIR.mkdir(exist_ok=True)
    print(f"Created directories:")
    print(f"  - {MARKDOWN_DIR}/")
    print(f"  - {UNIFIED_LATEX_DIR}/")
    print()
    
    # Check if source directory exists
    if not SOURCE_DIR.exists():
        print(f"Error: Source directory not found: {SOURCE_DIR}")
        return
    
    # Check if preamble file exists
    if not PREAMBLE_FILE.exists():
        print(f"Error: Universal preamble file not found: {PREAMBLE_FILE}")
        return
    
    # Get all .tex files
    tex_files = sorted(SOURCE_DIR.glob("*.tex"))
    print(f"Found {len(tex_files)} .tex files in {SOURCE_DIR}/")
    print()
    
    # Process each file
    success_count = 0
    failed_count = 0
    
    for tex_file in tex_files:
        if process_tex_file(tex_file):
            success_count += 1
        else:
            failed_count += 1
        print()
    
    # Summary
    print("="*70)
    print("Conversion Complete!")
    print("="*70)
    print(f"Successfully processed: {success_count} files")
    print(f"Failed: {failed_count} files")
    print()
    print(f"Output directories:")
    print(f"  - Markdown files: {MARKDOWN_DIR}/")
    print(f"  - Unified LaTeX files: {UNIFIED_LATEX_DIR}/")
    print()

if __name__ == "__main__":
    main()
