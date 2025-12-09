#!/usr/bin/env python3
"""
Generate chapter files with EXACT content preservation.
Extracts content between \begin{document} and \end{document} without ANY modifications.
"""

import os
import re
import sys
from pathlib import Path

def extract_title(content: str) -> str:
    """Extract title from standalone document."""
    title_match = re.search(r'\\title\{(.*?)\}', content, re.DOTALL)
    if title_match:
        title_text = title_match.group(1)
        # Clean up title - remove LaTeX formatting for chapter name
        title_text = re.sub(r'\\textbf\{(.*?)\}', r'\1', title_text)
        title_text = re.sub(r'\\large.*?(?=\\\\|\}|$)', '', title_text)
        title_text = re.sub(r'\\normalsize.*?(?=\\\\|\}|$)', '', title_text)
        title_text = re.sub(r'\\\\.*$', '', title_text, flags=re.MULTILINE)
        title_text = title_text.strip()
        # Take first line only
        first_line = title_text.split('\n')[0].strip()
        return first_line
    return "Unknown Title"

def generate_chapter_file(standalone_file: Path, output_dir: Path) -> bool:
    """
    Generate chapter file with EXACT content from standalone file.
    
    Args:
        standalone_file: Path to standalone .tex file
        output_dir: Directory for chapter files
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Read standalone file
        with open(standalone_file, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # Extract title for chapter command
        title = extract_title(content)
        
        # Find content between \begin{document} and \end{document}
        match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
        if not match:
            print(f"  [ERROR] No document environment found in {standalone_file.name}")
            return False
        
        # Extract body - EXACT content, no modifications
        body = match.group(1)
        
        # Create chapter file name
        base_name = standalone_file.stem  # e.g., 018_T0_Anomale-g2-9_De
        chapter_file = output_dir / f"{base_name}_ch.tex"
        
        # Build chapter content
        chapter_lines = [
            f"% Chapter file: {base_name}_ch.tex",
            f"% Source: {standalone_file.name}",
            "",
            f"\\chapter{{{title}}}",
            body,  # EXACT content from standalone
        ]
        
        # Write chapter file
        with open(chapter_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(chapter_lines))
        
        print(f"  [OK] Created {chapter_file.name}")
        return True
        
    except Exception as e:
        print(f"  [ERROR] Failed to process {standalone_file.name}: {e}")
        return False


def main():
    """Generate chapter files for specified standalone documents."""
    script_dir = Path(__file__).parent
    
    # Get language from command line (De or En)
    if len(sys.argv) < 2:
        print("Usage: python generate_chapter_exact.py <language> [file1] [file2] ...")
        print("       language: De or En")
        print("       files: specific file numbers (e.g., 018 041 103)")
        print("       or --all to process all files")
        sys.exit(1)
    
    language = sys.argv[1]
    if language not in ['De', 'En']:
        print(f"Error: Language must be 'De' or 'En', got '{language}'")
        sys.exit(1)
    
    # Determine standalone and chapter directories
    standalone_dir = script_dir / f"{language.lower()}_standalone"
    chapter_dir = script_dir / f"{language.lower()}_chapters_new"
    
    if not standalone_dir.exists():
        print(f"Error: Standalone directory not found: {standalone_dir}")
        sys.exit(1)
    
    chapter_dir.mkdir(exist_ok=True)
    
    # Get list of files to process
    if len(sys.argv) > 2 and sys.argv[2] == '--all':
        # Process all standalone files
        standalone_files = sorted(standalone_dir.glob(f"*_{language}.tex"))
    elif len(sys.argv) > 2:
        # Process specific files
        file_numbers = sys.argv[2:]
        standalone_files = []
        for num in file_numbers:
            # Find files starting with this number
            matching = list(standalone_dir.glob(f"{num}_*_{language}.tex"))
            standalone_files.extend(matching)
    else:
        print("Error: No files specified. Use file numbers or --all")
        sys.exit(1)
    
    if not standalone_files:
        print(f"No standalone files found for language '{language}'")
        sys.exit(1)
    
    print(f"=" * 60)
    print(f"Generating Chapter Files - EXACT Content Preservation")
    print(f"=" * 60)
    print(f"Language: {language}")
    print(f"Standalone dir: {standalone_dir}")
    print(f"Chapter dir: {chapter_dir}")
    print(f"Files to process: {len(standalone_files)}")
    print(f"=" * 60)
    
    success_count = 0
    for standalone_file in standalone_files:
        if generate_chapter_file(standalone_file, chapter_dir):
            success_count += 1
    
    print(f"=" * 60)
    print(f"Results: {success_count}/{len(standalone_files)} files processed successfully")
    print(f"=" * 60)
    
    return 0 if success_count == len(standalone_files) else 1


if __name__ == '__main__':
    sys.exit(main())
