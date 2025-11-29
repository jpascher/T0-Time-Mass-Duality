#!/usr/bin/env python3
"""
Script to prepare chapter files for book integration.
Extracts content between \begin{document} and \end{document},
removes \maketitle, \tableofcontents, and adjusts chapter levels.
"""

import os
import re
import sys

def extract_chapter_content(tex_file):
    """Extract content from a standalone LaTeX document for book integration."""
    with open(tex_file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Find content between \begin{document} and \end{document}
    match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if not match:
        return None
    
    body = match.group(1)
    
    # Remove \maketitle
    body = re.sub(r'\\maketitle\s*', '', body)
    
    # Remove \tableofcontents
    body = re.sub(r'\\tableofcontents\s*', '', body)
    
    # Remove \frontmatter, \mainmatter, \backmatter
    body = re.sub(r'\\(front|main|back)matter\s*', '', body)
    
    # Convert \chapter* to \section* (since book will have its own chapters)
    body = re.sub(r'\\chapter\*', r'\\section*', body)
    body = re.sub(r'\\chapter\{', r'\\section{', body)
    
    # Convert \section to \subsection
    body = re.sub(r'\\section\*', r'\\subsection*', body)
    body = re.sub(r'\\section\{', r'\\subsection{', body)
    
    # Convert \subsection to \subsubsection
    body = re.sub(r'\\subsection\*', r'\\subsubsection*', body)
    body = re.sub(r'\\subsection\{', r'\\subsubsection{', body)
    
    # Remove addcontentsline for chapters (will be added by book)
    body = re.sub(r'\\addcontentsline\{toc\}\{chapter\}\{[^}]*\}\s*', '', body)
    
    return body.strip()

def process_chapters(chapter_list, output_dir):
    """Process a list of chapter files and create chapter content files."""
    os.makedirs(output_dir, exist_ok=True)
    
    for chapter_file in chapter_list:
        base_name = os.path.basename(chapter_file)
        output_file = os.path.join(output_dir, f"ch_{base_name}")
        
        content = extract_chapter_content(chapter_file)
        if content:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"% Chapter content extracted from {base_name}\n")
                f.write(f"% For book integration\n\n")
                f.write(content)
            print(f"Created: {output_file}")
        else:
            print(f"Warning: Could not extract content from {chapter_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python prepare_chapters.py <chapter1.tex> [chapter2.tex] ...")
        print("       python prepare_chapters.py --all")
        sys.exit(1)
    
    if sys.argv[1] == "--all":
        # Process all _De.tex files in completed/
        completed_dir = "completed"
        chapters = [os.path.join(completed_dir, f) for f in os.listdir(completed_dir) 
                   if f.endswith('_De.tex')]
        chapters.sort()
        process_chapters(chapters, "chapters")
    else:
        process_chapters(sys.argv[1:], "chapters")
