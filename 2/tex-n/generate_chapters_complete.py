#!/usr/bin/env python3
"""
Complete Chapter Generation Script with Post-Processing

This script combines all chapter generation steps:
1. Extract content from standalone documents
2. Remove \maketitle and \tableofcontents
3. Convert abstract environments to sections
4. Remove \appendix commands (prevents counter overflow in books)
5. Fix unclosed chapter commands
6. Preserve ALL content exactly (especially resizebox and tables)

Usage:
    python generate_chapters_complete.py De 018 041 054 103
    python generate_chapters_complete.py En 018 041 054 103
    python generate_chapters_complete.py De --all  # Process all German documents
    
Author: GitHub Copilot
Created: 2024-12-09
Version: 1.1 - Added \appendix command removal
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional


def extract_title(content: str) -> str:
    """
    Extract title from standalone document and clean it for chapter use.
    
    Args:
        content: Full standalone document content
        
    Returns:
        Cleaned title text suitable for \chapter{} command
    """
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


def fix_abstract_environment(content: str, language: str) -> str:
    """
    Convert \begin{abstract}...\end{abstract} to section.
    
    The abstract environment doesn't work in book class, so we convert it
    to a section for compatibility.
    
    Args:
        content: Chapter file content
        language: 'De' for German or 'En' for English
        
    Returns:
        Content with abstract converted to section
    """
    if language == 'De':
        section_name = 'Zusammenfassung'
    else:  # En
        section_name = 'Abstract'
    
    # Replace \begin{abstract} with section
    content = re.sub(
        r'\\begin\{abstract\}',
        f'\\section*{{{section_name}}}',
        content
    )
    
    # Remove \end{abstract}
    content = re.sub(r'\\end\{abstract\}', '', content)
    
    return content


def fix_chapter_command(content: str) -> str:
    """
    Ensure \chapter{} command has proper closing brace.
    
    Some complex titles may have unclosed braces which cause LaTeX errors.
    This function attempts to fix common issues.
    
    Args:
        content: Chapter file content
        
    Returns:
        Content with fixed chapter command
    """
    # Find \chapter{ command
    chapter_match = re.search(r'(\\chapter\{[^}]*?)(\n|$)', content)
    if chapter_match:
        chapter_text = chapter_match.group(1)
        # Count braces
        open_count = chapter_text.count('{')
        close_count = chapter_text.count('}')
        
        # If unbalanced, add closing brace before newline
        if open_count > close_count:
            missing = open_count - close_count
            content = content.replace(
                chapter_match.group(0),
                chapter_text + ('}' * missing) + '\n'
            )
    
    return content


def remove_appendix_commands(content: str) -> str:
    """
    Remove appendix commands from chapter files.
    
    The appendix command is used in standalone documents to switch to appendix
    mode, but it causes counter overflow errors when multiple chapters in a book
    each try to start their own appendix. In chapter files, we simply remove the
    appendix command and keep the sections as regular sections within the chapter.
    
    Args:
        content: Chapter file content
        
    Returns:
        Content with appendix commands removed
    """
    # Remove appendix command (with optional surrounding whitespace and tabs)
    content = re.sub(r'^[ \t]*\\appendix[ \t]*$', '', content, flags=re.MULTILINE)
    
    return content


def generate_chapter_file(
    standalone_file: Path,
    output_dir: Path,
    language: str
) -> Tuple[bool, str]:
    """
    Generate chapter file with complete post-processing.
    
    This function performs all necessary transformations:
    1. Extracts content between \begin{document} and \end{document}
    2. Removes \maketitle and \tableofcontents
    3. Converts abstract environment to section
    4. Removes \appendix commands (prevents counter overflow)
    5. Fixes unclosed chapter commands
    6. Preserves ALL other content exactly
    
    Args:
        standalone_file: Path to standalone .tex file
        output_dir: Directory for chapter files
        language: 'De' or 'En'
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        # Read standalone file
        with open(standalone_file, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # Extract title for chapter command
        title = extract_title(content)
        
        # Find content between \begin{document} and \end{document}
        match = re.search(
            r'\\begin\{document\}(.*?)\\end\{document\}',
            content,
            re.DOTALL
        )
        if not match:
            return False, f"No document environment found in {standalone_file.name}"
        
        # Extract body - EXACT content
        body = match.group(1)
        
        # Post-processing steps
        # 1. Remove \maketitle (not needed in books)
        body = re.sub(r'\s*\\maketitle\s*', r'\n', body)
        
        # 2. Remove \tableofcontents (book has its own TOC)
        body = re.sub(r'\s*\\tableofcontents\s*', r'\n', body)
        
        # 3. Convert abstract environment to section
        body = fix_abstract_environment(body, language)
        
        # 4. Remove \appendix commands (causes counter overflow in books)
        body = remove_appendix_commands(body)
        
        # Create chapter file name
        base_name = standalone_file.stem  # e.g., 018_T0_Anomale-g2-9_De
        chapter_file = output_dir / f"{base_name}_ch.tex"
        
        # Build chapter content
        chapter_content = (
            f"% Chapter file: {base_name}_ch.tex\n"
            f"% Source: {standalone_file.name}\n"
            f"% Generated by: generate_chapters_complete.py\n"
            f"\n"
            f"\\chapter{{{title}}}\n"
            f"{body}"
        )
        
        # 4. Fix unclosed chapter commands
        chapter_content = fix_chapter_command(chapter_content)
        
        # Write chapter file
        with open(chapter_file, 'w', encoding='utf-8') as f:
            f.write(chapter_content)
        
        return True, f"Created {chapter_file.name}"
        
    except Exception as e:
        return False, f"Failed to process {standalone_file.name}: {e}"


def verify_chapter_file(
    standalone_file: Path,
    chapter_file: Path
) -> Tuple[bool, List[str]]:
    """
    Verify that chapter file was generated correctly.
    
    Checks:
    - Chapter file exists
    - Contains \chapter{} command
    - Content is preserved (no missing resizebox or tables)
    
    Args:
        standalone_file: Original standalone file
        chapter_file: Generated chapter file
        
    Returns:
        Tuple of (success: bool, issues: List[str])
    """
    issues = []
    
    if not chapter_file.exists():
        issues.append(f"Chapter file not found: {chapter_file}")
        return False, issues
    
    try:
        # Read files
        with open(standalone_file, 'r', encoding='utf-8') as f:
            standalone_content = f.read()
        with open(chapter_file, 'r', encoding='utf-8') as f:
            chapter_content = f.read()
        
        # Check for \chapter{} command
        if not re.search(r'\\chapter\{', chapter_content):
            issues.append("Missing \\chapter{} command")
        
        # Check that resizebox is preserved
        standalone_resizebox_count = standalone_content.count('\\resizebox')
        chapter_resizebox_count = chapter_content.count('\\resizebox')
        if standalone_resizebox_count != chapter_resizebox_count:
            issues.append(
                f"Resizebox count mismatch: "
                f"standalone={standalone_resizebox_count}, "
                f"chapter={chapter_resizebox_count}"
            )
        
        # Check for unclosed braces
        chapter_line = re.search(r'\\chapter\{[^\n]*', chapter_content)
        if chapter_line:
            line_text = chapter_line.group(0)
            if line_text.count('{') != line_text.count('}'):
                issues.append("Unclosed braces in \\chapter{} command")
        
        # Check that abstract is converted
        if re.search(r'\\begin\{abstract\}', chapter_content):
            issues.append("Abstract environment not converted to section")
        
        # Check that maketitle is removed
        if re.search(r'\\maketitle', chapter_content):
            issues.append("\\maketitle not removed")
        
        # Check that tableofcontents is removed
        if re.search(r'\\tableofcontents', chapter_content):
            issues.append("\\tableofcontents not removed")
        
    except Exception as e:
        issues.append(f"Verification failed: {e}")
    
    return len(issues) == 0, issues


def main():
    """Main function - generate chapter files with post-processing."""
    script_dir = Path(__file__).parent
    
    # Get language from command line
    if len(sys.argv) < 2:
        print("Usage: python generate_chapters_complete.py <language> [file1] [file2] ...")
        print("       language: De or En")
        print("       files: specific file numbers (e.g., 018 041 103)")
        print("       or --all to process all files")
        print()
        print("Example:")
        print("  python generate_chapters_complete.py De 018 041 054 103")
        print("  python generate_chapters_complete.py En --all")
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
            if not matching:
                print(f"Warning: No file found matching '{num}_*_{language}.tex'")
            standalone_files.extend(matching)
    else:
        print("Error: No files specified. Use file numbers or --all")
        sys.exit(1)
    
    if not standalone_files:
        print(f"No standalone files found for language '{language}'")
        sys.exit(1)
    
    # Print header
    print("=" * 70)
    print("Complete Chapter Generation with Post-Processing")
    print("=" * 70)
    print(f"Language: {language}")
    print(f"Standalone dir: {standalone_dir}")
    print(f"Chapter dir: {chapter_dir}")
    print(f"Files to process: {len(standalone_files)}")
    print("=" * 70)
    print()
    print("Processing steps:")
    print("  1. Extract content from standalone")
    print("  2. Remove \\maketitle and \\tableofcontents")
    print("  3. Convert abstract environment to section")
    print("  4. Remove \\appendix commands")
    print("  5. Fix unclosed chapter commands")
    print("  6. Verify generated file")
    print("=" * 70)
    print()
    
    # Process files
    success_count = 0
    verification_issues = []
    
    for standalone_file in standalone_files:
        print(f"Processing: {standalone_file.name}")
        
        # Generate chapter file
        success, message = generate_chapter_file(
            standalone_file,
            chapter_dir,
            language
        )
        
        if success:
            print(f"  ✓ {message}")
            
            # Verify generated file
            chapter_file = chapter_dir / f"{standalone_file.stem}_ch.tex"
            verify_success, issues = verify_chapter_file(
                standalone_file,
                chapter_file
            )
            
            if verify_success:
                print(f"  ✓ Verification passed")
                success_count += 1
            else:
                print(f"  ⚠ Verification issues:")
                for issue in issues:
                    print(f"    - {issue}")
                verification_issues.append((standalone_file.name, issues))
        else:
            print(f"  ✗ {message}")
    
    # Print summary
    print()
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Successfully processed: {success_count}/{len(standalone_files)} files")
    
    if verification_issues:
        print(f"\nVerification issues found in {len(verification_issues)} files:")
        for filename, issues in verification_issues:
            print(f"  {filename}:")
            for issue in issues:
                print(f"    - {issue}")
        print("\n⚠ Please review and fix verification issues before compiling books")
        return 1
    else:
        print("\n✓ All files generated and verified successfully!")
        print("\nNext steps:")
        print("  1. Commit generated chapter files")
        print("  2. Compile books to verify: pdflatex Teil1_De.tex")
        print("  3. Run 3 passes for proper cross-references")
        return 0


if __name__ == '__main__':
    sys.exit(main())
