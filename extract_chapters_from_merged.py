#!/usr/bin/env python3
"""
Script to extract individual chapters from merged DVFT files.
Creates separate LaTeX files for each chapter in a new directory.

Usage:
    python3 extract_chapters_from_merged.py
"""

import os
import re
from pathlib import Path

def read_file(filepath):
    """Read a file and return its content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def write_file(filepath, content):
    """Write content to a file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        return False

def extract_preamble(content):
    """Extract the preamble and document setup from merged file."""
    # Find everything up to (but not including) the first \section
    match = re.search(r'(.*?)\\section\{', content, re.DOTALL)
    if match:
        preamble = match.group(1)
        # Remove \maketitle and intro text from preamble, keep only up to \begin{document}
        # We'll include \begin{document} but nothing after it
        doc_match = re.search(r'(.*?\\begin\{document\})', preamble, re.DOTALL)
        if doc_match:
            return doc_match.group(1)
    return None

def extract_chapters(content):
    """Extract individual chapters from merged content."""
    chapters = []
    
    # Find all sections starting with "Kapitel XX:"
    pattern = r'\\section\{Kapitel\s+(\d+):\s*([^}]+)\}'
    
    # Find all chapter positions
    chapter_positions = []
    for match in re.finditer(pattern, content):
        chapter_num = int(match.group(1))
        chapter_title = match.group(2).strip()
        start_pos = match.start()
        chapter_positions.append({
            'num': chapter_num,
            'title': chapter_title,
            'start': start_pos,
            'match': match
        })
    
    # Extract content for each chapter
    for i, chapter in enumerate(chapter_positions):
        # Determine end position (start of next chapter or end of document)
        if i < len(chapter_positions) - 1:
            end_pos = chapter_positions[i + 1]['start']
        else:
            # Find \end{document} or end of file
            end_match = re.search(r'\\end\{document\}', content[chapter['start']:])
            if end_match:
                end_pos = chapter['start'] + end_match.start()
            else:
                end_pos = len(content)
        
        # Extract chapter content
        chapter_content = content[chapter['start']:end_pos].strip()
        
        chapters.append({
            'num': chapter['num'],
            'title': chapter['title'],
            'content': chapter_content
        })
    
    return chapters

def create_standalone_chapter(chapter, preamble_template):
    """Create a standalone LaTeX file for a chapter."""
    # Remove any existing \title commands from preamble
    preamble_clean = re.sub(r'\\title\{[^}]*\}', '', preamble_template)
    preamble_clean = re.sub(r'\\author\{[^}]*\}', '', preamble_clean)
    preamble_clean = re.sub(r'\\date\{[^}]*\}', '', preamble_clean)
    
    # Modify the preamble to include a title for this specific chapter
    chapter_preamble = preamble_clean.replace(
        '\\begin{document}',
        f'\\title{{Kapitel {chapter["num"]}: {chapter["title"]}}}\n\\author{{}}\n\\date{{}}\n\n\\begin{{document}}\n\n\\maketitle\n'
    )
    
    # Combine preamble, chapter content, and closing
    full_content = chapter_preamble + '\n' + chapter['content'] + '\n\n\\end{document}\n'
    
    return full_content

def main():
    base_dir = Path("/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_DVFT")
    
    # Merged files to process
    merged_files = [
        "202_12-15_De.tex",
        "202_16-19_De.tex",
        "202_20-32_De.tex",
        "202_33-43_De.tex",
    ]
    
    # Create output directory
    output_dir = base_dir / "extracted_chapters_from_merged"
    output_dir.mkdir(exist_ok=True)
    
    print("=" * 80)
    print("EXTRACTING CHAPTERS FROM MERGED FILES")
    print("=" * 80)
    print()
    print(f"Output directory: {output_dir}")
    print()
    
    all_chapters_extracted = []
    
    # Process each merged file
    for merged_file in merged_files:
        filepath = base_dir / merged_file
        
        if not filepath.exists():
            print(f"⚠️  File not found: {merged_file}")
            continue
        
        print(f"Processing: {merged_file}")
        
        # Read merged file
        content = read_file(filepath)
        if not content:
            continue
        
        # Extract preamble
        preamble = extract_preamble(content)
        if not preamble:
            print(f"  ⚠️  Could not extract preamble from {merged_file}")
            continue
        
        # Extract chapters
        chapters = extract_chapters(content)
        
        if not chapters:
            print(f"  ⚠️  No chapters found in {merged_file}")
            continue
        
        print(f"  Found {len(chapters)} chapters")
        
        # Create individual files for each chapter
        for chapter in chapters:
            chapter_num = chapter['num']
            
            # Create standalone chapter file
            standalone_content = create_standalone_chapter(chapter, preamble)
            
            # Write to file
            output_file = output_dir / f"kapitel_{chapter_num:02d}_merged.tex"
            
            if write_file(output_file, standalone_content):
                print(f"    ✓ Extracted Kapitel {chapter_num}: {chapter['title'][:50]}...")
                all_chapters_extracted.append(chapter_num)
            else:
                print(f"    ✗ Failed to write Kapitel {chapter_num}")
    
    # Summary
    print()
    print("=" * 80)
    print("EXTRACTION SUMMARY")
    print("=" * 80)
    print(f"Total chapters extracted: {len(all_chapters_extracted)}")
    print(f"Output directory: {output_dir}")
    print()
    
    if all_chapters_extracted:
        all_chapters_extracted.sort()
        print(f"Chapters extracted: {', '.join(map(str, all_chapters_extracted))}")
        print()
        print("Files created:")
        for chapter_num in all_chapters_extracted:
            print(f"  - kapitel_{chapter_num:02d}_merged.tex")
    else:
        print("⚠️  No chapters were extracted.")
    
    print()
    print("=" * 80)
    print("✓ Extraction complete!")
    print("=" * 80)

if __name__ == "__main__":
    main()
