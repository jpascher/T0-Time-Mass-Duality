#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T0 LaTeX Document Standardization Script
=========================================

This script standardizes LaTeX documents in the T0-Time-Mass-Duality repository
by replacing individual preambles with references to shared preamble files.

Usage:
    python standardize_latex.py [--dry-run] [--backup]

Options:
    --dry-run   Show what would be changed without modifying files
    --backup    Create .bak backup files before modifying

Author: Johann Pascher
Date: 2025
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import Tuple, Optional, List


def detect_language(content: str, filename: str) -> str:
    """
    Detect the document language based on babel package or filename.
    
    Detection order:
    1. Filename patterns: '_De.tex', 'De.tex', '_En.tex', 'En.tex'
    2. Babel package: \\usepackage[ngerman]{babel}, \\usepackage[german]{babel},
       \\usepackage[english]{babel}
    3. Fallback: 'En' for English
    
    Examples:
        'Zeit_De.tex' -> 'De' (German, by filename)
        'Bell_En.tex' -> 'En' (English, by filename)
        'document.tex' with \\usepackage[ngerman]{babel} -> 'De' (German, by babel)
    
    Args:
        content: The LaTeX file content
        filename: The filename
        
    Returns:
        'De' for German, 'En' for English
    """
    # Check filename first
    if filename.endswith('_De.tex') or filename.endswith('De.tex'):
        return 'De'
    elif filename.endswith('_En.tex') or filename.endswith('En.tex'):
        return 'En'
    
    # Check babel package
    if re.search(r'\\usepackage\[.*?ngerman.*?\]\{babel\}', content):
        return 'De'
    elif re.search(r'\\usepackage\[.*?german.*?\]\{babel\}', content):
        return 'De'
    elif re.search(r'\\usepackage\[.*?english.*?\]\{babel\}', content):
        return 'En'
    
    # Default to German if using ngerman anywhere
    if 'ngerman' in content or 'german' in content.lower():
        return 'De'
    
    return 'En'


def extract_document_class(content: str) -> Optional[str]:
    """
    Extract the documentclass line from the content.
    
    Args:
        content: The LaTeX file content
        
    Returns:
        The documentclass line or None if not found
    """
    match = re.search(r'(\\documentclass\[.*?\]\{.*?\}|\\documentclass\{.*?\})', content, re.DOTALL)
    if match:
        return match.group(1)
    return None


def extract_title_author_date(content: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Extract title, author, and date from the preamble.
    
    Args:
        content: The LaTeX file content
        
    Returns:
        Tuple of (title, author, date) - each may be None
    """
    title = None
    author = None
    date = None
    
    # Find \begin{document} position
    begin_doc = content.find(r'\begin{document}')
    if begin_doc == -1:
        preamble = content
    else:
        preamble = content[:begin_doc]
    
    # Extract title (may span multiple lines)
    # Note: Using group(0) intentionally to get the full \title{...} command
    title_match = re.search(r'\\title\{(.*?)\}(?=\s*(?:\\author|\\date|\\begin|$))', preamble, re.DOTALL)
    if title_match:
        title = title_match.group(0)  # Full command including \title{...}
    
    # Extract author
    # Note: Using group(0) intentionally to get the full \author{...} command
    author_match = re.search(r'\\author\{(.*?)\}(?=\s*(?:\\date|\\title|\\begin|$))', preamble, re.DOTALL)
    if author_match:
        author = author_match.group(0)  # Full command including \author{...}
    
    # Extract date
    # Note: Using group(0) intentionally to get the full \date{...} command
    date_match = re.search(r'\\date\{(.*?)\}', preamble, re.DOTALL)
    if date_match:
        date = date_match.group(0)  # Full command including \date{...}
    
    return title, author, date


def extract_custom_header_config(content: str) -> Optional[str]:
    """
    Extract custom fancyhdr configuration if present.
    
    Args:
        content: The LaTeX file content
        
    Returns:
        Custom header configuration or None
    """
    # Find \begin{document} position
    begin_doc = content.find(r'\begin{document}')
    if begin_doc == -1:
        return None
    
    preamble = content[:begin_doc]
    
    # Look for custom fancyhead/fancyfoot configurations
    header_lines = []
    for line in preamble.split('\n'):
        stripped = line.strip()
        if stripped.startswith(r'\fancyhead[') or stripped.startswith(r'\fancyfoot['):
            # Skip default header/footer that's in preamble
            if 'T0-Theorie' not in stripped and 'T0 Theory' not in stripped:
                header_lines.append(line)
        elif stripped.startswith(r'\fancyhf{}'):
            header_lines.append(line)
    
    if header_lines:
        return '\n'.join(header_lines)
    return None


def find_begin_document(content: str) -> int:
    """Find the position of \\begin{document} in the content."""
    match = re.search(r'\\begin\{document\}', content)
    if match:
        return match.start()
    return -1


def standardize_document(content: str, filename: str, preamble_path: str) -> Tuple[str, bool, List[str]]:
    """
    Standardize a LaTeX document by replacing its preamble with a reference
    to the shared preamble file.
    
    Args:
        content: The original file content
        filename: The filename (for language detection)
        preamble_path: Relative path to the preamble file
        
    Returns:
        Tuple of (new_content, was_modified, list of notes/warnings)
    """
    notes = []
    
    # Check if this is a chapter file (no documentclass)
    if r'\documentclass' not in content:
        notes.append(f"Skipping: No \\documentclass found (likely a chapter file)")
        return content, False, notes
    
    # Check if already standardized
    if r'\input{T0_preamble_' in content:
        notes.append("Already standardized")
        return content, False, notes
    
    # Find \begin{document}
    begin_doc_pos = find_begin_document(content)
    if begin_doc_pos == -1:
        notes.append("Skipping: No \\begin{document} found")
        return content, False, notes
    
    # Detect language
    lang = detect_language(content, filename)
    notes.append(f"Detected language: {lang}")
    
    # Extract documentclass
    doc_class = extract_document_class(content)
    if not doc_class:
        notes.append("Warning: Could not extract documentclass")
        return content, False, notes
    
    # Extract title, author, date
    title, author, date = extract_title_author_date(content)
    
    # Build new preamble
    new_preamble_parts = [doc_class, '']
    new_preamble_parts.append(f'% Standardized preamble - {filename}')
    new_preamble_parts.append(f'\\input{{{preamble_path}T0_preamble_{lang}}}')
    new_preamble_parts.append('')
    
    # Add title, author, date if they exist
    if title:
        new_preamble_parts.append(title)
    if author:
        new_preamble_parts.append(author)
    if date:
        new_preamble_parts.append(date)
    
    new_preamble_parts.append('')
    
    # Get document body (from \begin{document} onward)
    document_body = content[begin_doc_pos:]
    
    # Combine new preamble with document body
    new_content = '\n'.join(new_preamble_parts) + document_body
    
    notes.append("Successfully standardized")
    return new_content, True, notes


def process_file(filepath: Path, preamble_path: str, dry_run: bool = False, backup: bool = False) -> Tuple[bool, List[str]]:
    """
    Process a single LaTeX file.
    
    Args:
        filepath: Path to the LaTeX file
        preamble_path: Relative path to preamble directory
        dry_run: If True, don't actually modify the file
        backup: If True, create a backup before modifying
        
    Returns:
        Tuple of (was_modified, list of notes)
    """
    notes = []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    except Exception as e:
        notes.append(f"Error reading file: {e}")
        return False, notes
    
    new_content, modified, std_notes = standardize_document(content, filepath.name, preamble_path)
    notes.extend(std_notes)
    
    if modified and not dry_run:
        if backup:
            backup_path = filepath.with_suffix('.tex.bak')
            try:
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                notes.append(f"Backup created: {backup_path.name}")
            except Exception as e:
                notes.append(f"Warning: Could not create backup: {e}")
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            notes.append("File updated successfully")
        except Exception as e:
            notes.append(f"Error writing file: {e}")
            return False, notes
    elif modified and dry_run:
        notes.append("Would be modified (dry-run)")
    
    return modified, notes


def main():
    parser = argparse.ArgumentParser(
        description='Standardize T0 LaTeX documents by using shared preambles'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--backup',
        action='store_true',
        help='Create .bak backup files before modifying'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Process only the specified file'
    )
    parser.add_argument(
        '--tex-dir',
        type=str,
        default='.',
        help='Directory containing LaTeX files (default: current directory)'
    )
    
    args = parser.parse_args()
    
    tex_dir = Path(args.tex_dir)
    if not tex_dir.exists():
        print(f"Error: Directory '{tex_dir}' does not exist")
        sys.exit(1)
    
    # Determine preamble path based on location
    preamble_path = ''  # Will be relative path to preamble
    
    if args.file:
        files = [Path(args.file)]
    else:
        files = list(tex_dir.glob('*.tex'))
    
    print(f"{'='*60}")
    print("T0 LaTeX Document Standardization")
    print(f"{'='*60}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print(f"Backup: {'Yes' if args.backup else 'No'}")
    print(f"Directory: {tex_dir.absolute()}")
    print(f"Files found: {len(files)}")
    print(f"{'='*60}")
    print()
    
    modified_count = 0
    skipped_count = 0
    error_count = 0
    
    for filepath in sorted(files):
        if filepath.name.startswith('T0_preamble_'):
            continue  # Skip preamble files themselves
        
        print(f"Processing: {filepath.name}")
        
        modified, notes = process_file(filepath, preamble_path, args.dry_run, args.backup)
        
        for note in notes:
            print(f"  - {note}")
        
        if modified:
            modified_count += 1
        elif 'Error' in ' '.join(notes):
            error_count += 1
        else:
            skipped_count += 1
        
        print()
    
    print(f"{'='*60}")
    print("Summary:")
    print(f"  Modified: {modified_count}")
    print(f"  Skipped:  {skipped_count}")
    print(f"  Errors:   {error_count}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
