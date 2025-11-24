#!/usr/bin/env python3
"""
Complete conversion pipeline: LaTeX → Markdown → Unified LaTeX
Converts all documents from 2/tex/ through markdown to unified LaTeX with consistent header.
"""

import os
import re
import sys
from pathlib import Path

# Repository root
REPO_ROOT = Path(__file__).parent

# Directories
TEX_SOURCE_DIR = REPO_ROOT / "2" / "tex"
MARKDOWN_DIR = REPO_ROOT / "markdown_content"
UNIFIED_LATEX_DIR = REPO_ROOT / "unified_latex"
UNIVERSAL_PREAMBLE_FILE = REPO_ROOT / "universal_preamble.tex"

def extract_document_body(tex_content):
    """Extract content between \\begin{document} and \\end{document}."""
    # Find \begin{document}
    begin_match = re.search(r'\\begin\{document\}', tex_content)
    if not begin_match:
        return None
    
    # Find \end{document}
    end_match = re.search(r'\\end\{document\}', tex_content)
    if not end_match:
        return None
    
    # Extract content between begin and end
    start_pos = begin_match.end()
    end_pos = end_match.start()
    body = tex_content[start_pos:end_pos].strip()
    
    # Remove \maketitle, \tableofcontents, etc. that appear right after \begin{document}
    body = re.sub(r'^\\maketitle\s*', '', body)
    body = re.sub(r'^\\tableofcontents\s*', '', body)
    
    return body

def latex_to_markdown(latex_content):
    """Convert LaTeX document body to Markdown."""
    md = latex_content
    
    # Convert sections
    md = re.sub(r'\\section\*?\{([^}]+)\}', r'# \1', md)
    md = re.sub(r'\\subsection\*?\{([^}]+)\}', r'## \1', md)
    md = re.sub(r'\\subsubsection\*?\{([^}]+)\}', r'### \1', md)
    
    # Convert text formatting
    md = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', md)
    md = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', md)
    md = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', md)
    
    # Keep math environments as-is (will be converted back to LaTeX)
    # Just mark them so we can identify them
    md = re.sub(r'\\begin\{equation\}', r'\n```math-equation\n', md)
    md = re.sub(r'\\end\{equation\}', r'\n```\n', md)
    md = re.sub(r'\\begin\{align\}', r'\n```math-align\n', md)
    md = re.sub(r'\\end\{align\}', r'\n```\n', md)
    md = re.sub(r'\\begin\{eqnarray\}', r'\n```math-eqnarray\n', md)
    md = re.sub(r'\\end\{eqnarray\}', r'\n```\n', md)
    
    # Keep inline math with $...$
    # (no changes needed, will work in both)
    
    # Convert itemize/enumerate
    md = re.sub(r'\\begin\{itemize\}', r'', md)
    md = re.sub(r'\\end\{itemize\}', r'', md)
    md = re.sub(r'\\begin\{enumerate\}', r'', md)
    md = re.sub(r'\\end\{enumerate\}', r'', md)
    md = re.sub(r'\\item\s+', r'- ', md)
    
    # Remove bibliography if present
    md = re.sub(r'\\begin\{thebibliography\}.*?\\end\{thebibliography\}', '', md, flags=re.DOTALL)
    md = re.sub(r'\\bibliography\{[^}]+\}', '', md)
    md = re.sub(r'\\bibliographystyle\{[^}]+\}', '', md)
    
    # Clean up excessive whitespace
    md = re.sub(r'\n{3,}', r'\n\n', md)
    
    return md.strip()

def markdown_to_unified_latex(md_content, filename_base):
    """Convert Markdown back to LaTeX with proper environments."""
    tex = md_content
    
    # Convert headers back to sections
    tex = re.sub(r'^# (.+)$', r'\\section{\1}', tex, flags=re.MULTILINE)
    tex = re.sub(r'^## (.+)$', r'\\subsection{\1}', tex, flags=re.MULTILINE)
    tex = re.sub(r'^### (.+)$', r'\\subsubsection{\1}', tex, flags=re.MULTILINE)
    
    # Convert text formatting back
    tex = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', tex)
    tex = re.sub(r'\*([^*]+)\*', r'\\emph{\1}', tex)
    
    # Convert math environments back
    tex = re.sub(r'```math-equation\n', r'\\begin{equation}\n', tex)
    tex = re.sub(r'```math-align\n', r'\\begin{align}\n', tex)
    tex = re.sub(r'```math-eqnarray\n', r'\\begin{eqnarray}\n', tex)
    tex = re.sub(r'```\n', r'\\end{equation}\n', tex)  # Simplified - assumes equation
    
    # Convert lists back
    lines = tex.split('\n')
    in_itemize = False
    result_lines = []
    for line in lines:
        if line.strip().startswith('- '):
            if not in_itemize:
                result_lines.append('\\begin{itemize}')
                in_itemize = True
            result_lines.append('\\item ' + line.strip()[2:])
        else:
            if in_itemize and line.strip() == '':
                result_lines.append('\\end{itemize}')
                in_itemize = False
            result_lines.append(line)
    
    if in_itemize:
        result_lines.append('\\end{itemize}')
    
    tex = '\n'.join(result_lines)
    
    return tex

def load_universal_preamble():
    """Load the universal preamble template."""
    if not UNIVERSAL_PREAMBLE_FILE.exists():
        print(f"ERROR: Universal preamble not found at {UNIVERSAL_PREAMBLE_FILE}")
        return None
    
    with open(UNIVERSAL_PREAMBLE_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def create_unified_latex_document(content, title, universal_preamble_content):
    """Create a complete unified LaTeX document with universal preamble."""
    # Start with document class
    doc = "\\documentclass[11pt,a4paper]{article}\n\n"
    
    # Add the universal preamble content (packages, commands, etc.)
    doc += universal_preamble_content + "\n\n"
    
    # Begin document
    doc += "\\begin{document}\n\n"
    
    # Add title if we have one
    if title:
        doc += f"\\title{{{title}}}\n"
        doc += "\\maketitle\n\n"
    
    # Add the main content
    doc += content + "\n\n"
    
    # End document
    doc += "\\end{document}\n"
    
    return doc

def process_file(tex_file, universal_preamble):
    """Process a single .tex file through the full pipeline."""
    filename = tex_file.name
    filename_base = tex_file.stem
    
    print(f"Processing: {filename}")
    
    # Step 1: Read LaTeX source
    try:
        with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
            tex_content = f.read()
    except Exception as e:
        print(f"  ERROR reading {filename}: {e}")
        return False
    
    # Step 2: Extract document body
    body = extract_document_body(tex_content)
    if body is None:
        print(f"  WARNING: Could not extract document body from {filename}")
        return False
    
    # Step 3: Convert to Markdown
    md_content = latex_to_markdown(body)
    
    # Step 4: Save Markdown
    md_file = MARKDOWN_DIR / f"{filename_base}.md"
    try:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"  → Saved Markdown: {md_file.name}")
    except Exception as e:
        print(f"  ERROR writing Markdown {md_file.name}: {e}")
        return False
    
    # Step 5: Convert Markdown back to LaTeX
    unified_tex_content = markdown_to_unified_latex(md_content, filename_base)
    
    # Step 6: Extract title from original if possible
    title_match = re.search(r'\\title\{([^}]+)\}', tex_content)
    title = title_match.group(1) if title_match else filename_base.replace('_', ' ')
    
    # Step 7: Create complete unified LaTeX document
    complete_doc = create_unified_latex_document(
        unified_tex_content,
        title,
        universal_preamble
    )
    
    # Step 8: Save unified LaTeX
    unified_tex_file = UNIFIED_LATEX_DIR / filename
    try:
        with open(unified_tex_file, 'w', encoding='utf-8') as f:
            f.write(complete_doc)
        print(f"  → Saved Unified LaTeX: {unified_tex_file.name}")
    except Exception as e:
        print(f"  ERROR writing unified LaTeX {unified_tex_file.name}: {e}")
        return False
    
    return True

def main():
    """Main conversion pipeline."""
    print("=" * 80)
    print("LaTeX → Markdown → Unified LaTeX Conversion Pipeline")
    print("=" * 80)
    
    # Create output directories
    MARKDOWN_DIR.mkdir(exist_ok=True)
    UNIFIED_LATEX_DIR.mkdir(exist_ok=True)
    print(f"Created directories:")
    print(f"  - {MARKDOWN_DIR}")
    print(f"  - {UNIFIED_LATEX_DIR}")
    
    # Load universal preamble
    print("\nLoading universal preamble...")
    universal_preamble = load_universal_preamble()
    if universal_preamble is None:
        return 1
    print(f"✓ Loaded universal preamble ({len(universal_preamble)} characters)")
    
    # Find all .tex files in source directory
    if not TEX_SOURCE_DIR.exists():
        print(f"ERROR: Source directory not found: {TEX_SOURCE_DIR}")
        return 1
    
    tex_files = sorted(TEX_SOURCE_DIR.glob("*.tex"))
    print(f"\nFound {len(tex_files)} LaTeX files in {TEX_SOURCE_DIR}")
    
    # Process each file
    print("\n" + "=" * 80)
    print("Processing files...")
    print("=" * 80 + "\n")
    
    success_count = 0
    fail_count = 0
    
    for tex_file in tex_files:
        if process_file(tex_file, universal_preamble):
            success_count += 1
        else:
            fail_count += 1
        print()
    
    # Summary
    print("=" * 80)
    print("Conversion Summary")
    print("=" * 80)
    print(f"Total files processed: {len(tex_files)}")
    print(f"  ✓ Successful: {success_count}")
    print(f"  ✗ Failed: {fail_count}")
    print(f"\nOutput directories:")
    print(f"  - Markdown: {MARKDOWN_DIR} ({len(list(MARKDOWN_DIR.glob('*.md')))} files)")
    print(f"  - Unified LaTeX: {UNIFIED_LATEX_DIR} ({len(list(UNIFIED_LATEX_DIR.glob('*.tex')))} files)")
    print("=" * 80)
    
    return 0 if fail_count == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
