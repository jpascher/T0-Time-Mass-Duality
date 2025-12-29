#!/usr/bin/env python3
"""
Script to prepare combined chapters for inclusion in master document.
Extracts content (without preamble and document environment) from combined chapters.
"""

import os
import re

def extract_content_from_chapter(chapter_file):
    """Extract content between \\begin{document} and \\end{document}"""
    with open(chapter_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find content between \begin{document} and \end{document}
    match = re.search(r'\\begin\{document\}(.*)\\end\{document\}', content, re.DOTALL)
    if match:
        chapter_content = match.group(1).strip()
        
        # Remove \maketitle if present
        chapter_content = re.sub(r'\\maketitle\s*', '', chapter_content)
        
        # Remove standalone title definitions
        chapter_content = re.sub(r'\\title\{[^}]*\}\s*', '', chapter_content)
        chapter_content = re.sub(r'\\author\{[^}]*\}\s*', '', chapter_content)
        chapter_content = re.sub(r'\\date\{[^}]*\}\s*', '', chapter_content)
        
        return chapter_content.strip()
    return ""

def process_all_chapters():
    """Process all 42 combined chapters"""
    base_dir = "2/tex-n/de_DVFT/combined_chapters"
    
    # Chapters to process (1-16, 18-43, excluding 17 and 44)
    chapters = list(range(1, 17)) + list(range(18, 44))
    
    processed_count = 0
    
    for chapter_num in chapters:
        input_file = os.path.join(base_dir, f"kapitel_{chapter_num:02d}_combined.tex")
        output_file = os.path.join(base_dir, f"kapitel_{chapter_num:02d}_combined_content.tex")
        
        if os.path.exists(input_file):
            print(f"Processing Kapitel {chapter_num:02d}...")
            content = extract_content_from_chapter(input_file)
            
            if content:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                processed_count += 1
                print(f"  ✓ Created {output_file}")
            else:
                print(f"  ✗ No content found in {input_file}")
        else:
            print(f"  ⚠ File not found: {input_file}")
    
    print(f"\nProcessed {processed_count} chapters successfully.")
    return processed_count

if __name__ == "__main__":
    print("="*70)
    print("DVFT Combined Chapters - Content Extraction")
    print("="*70)
    print()
    
    count = process_all_chapters()
    
    print()
    print("="*70)
    print(f"Extraction complete! {count} content files created.")
    print("Ready to compile master document.")
    print("="*70)
