#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T0 LaTeX Content Preservation Converter
========================================

This script converts LaTeX documents while preserving content:
1. Extracts content (body) from original document
2. Applies standardized preamble
3. Preserves all text, formulas, and structure
4. Only changes formatting and header

Usage:
    python convert_preserve_content.py --file Document.tex
    python convert_preserve_content.py --all --dry-run

Author: Johann Pascher
Date: 2025
"""

import os
import re
import sys
import argparse
import shutil
from pathlib import Path
from typing import Optional, Tuple
import hashlib


def detect_language(content: str, filename: str) -> str:
    """Detect document language from filename or babel package."""
    if filename.endswith('_De.tex') or 'De.tex' in filename:
        return 'De'
    elif filename.endswith('_En.tex') or 'En.tex' in filename:
        return 'En'
    
    # Check babel package
    if re.search(r'\\usepackage\[.*ngerman.*\]\{babel\}', content):
        return 'De'
    elif re.search(r'\\usepackage\[.*german.*\]\{babel\}', content):
        return 'De'
    
    return 'En'  # Default to English


def extract_document_parts(content: str) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str], str]:
    """
    Extract documentclass, title, author, date, and body from LaTeX content.
    
    Returns:
        Tuple of (documentclass, title, author, date, body)
    """
    # Extract documentclass
    docclass_match = re.search(r'\\documentclass(\[.*?\])?\{(\w+)\}', content)
    if docclass_match:
        options = docclass_match.group(1) or ''
        doctype = docclass_match.group(2)
        documentclass = f"\\documentclass{options}{{{doctype}}}"
    else:
        documentclass = "\\documentclass[12pt,a4paper]{article}"
    
    # Extract title (preserve full content including line breaks)
    title = None
    title_match = re.search(r'\\title\{(.*?)\}(?=\s*(?:\\author|\\date|\\begin|\\maketitle|$))', content, re.DOTALL)
    if title_match:
        title = f"\\title{{{title_match.group(1)}}}"
    
    # Extract author
    author = None
    author_match = re.search(r'\\author\{(.*?)\}(?=\s*(?:\\date|\\title|\\begin|\\maketitle|$))', content, re.DOTALL)
    if author_match:
        author = f"\\author{{{author_match.group(1)}}}"
    
    # Extract date
    date = None
    date_match = re.search(r'\\date\{(.*?)\}', content, re.DOTALL)
    if date_match:
        date = f"\\date{{{date_match.group(1)}}}"
    
    # Extract body (everything between \begin{document} and \end{document})
    body_match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if body_match:
        body = body_match.group(1).strip()
    else:
        body = ""
    
    return documentclass, title, author, date, body


def get_content_hash(body: str) -> str:
    """Generate a hash of the content for verification."""
    # Normalize whitespace for comparison
    normalized = re.sub(r'\s+', ' ', body.strip())
    return hashlib.md5(normalized.encode('utf-8', errors='replace')).hexdigest()


def create_standardized_document(documentclass: str, title: Optional[str], author: Optional[str], 
                                  date: Optional[str], body: str, language: str, filename: str) -> str:
    """Create a new document with standardized preamble but preserved content."""
    
    preamble_file = f"T0_preamble_{language}"
    
    lines = [
        documentclass,
        "",
        f"% Standardized preamble - {filename}",
        f"\\input{{{preamble_file}}}",
        ""
    ]
    
    if title:
        lines.append(title)
    if author:
        lines.append(author)
    if date:
        lines.append(date)
    
    lines.append("")
    lines.append("\\begin{document}")
    lines.append(body)
    lines.append("\\end{document}")
    
    return '\n'.join(lines)


def convert_file(filepath: Path, dry_run: bool = False, backup: bool = True) -> Tuple[bool, str]:
    """
    Convert a single LaTeX file to use standardized preamble while preserving content.
    
    Returns:
        Tuple of (success, message)
    """
    filename = filepath.name
    
    # Skip preamble files and chapter files
    if filename.startswith('T0_preamble_') or filename.endswith('_ch.tex'):
        return True, "Skipped (preamble/chapter file)"
    
    if filename.startswith('pri'):
        return True, "Skipped (preamble file)"
    
    try:
        # Read with multiple encodings
        content = None
        for encoding in ['utf-8', 'latin-1', 'cp1252']:
            try:
                with open(filepath, 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
        
        if content is None:
            return False, "Could not read file with any encoding"
        
        # Check if already standardized
        if '\\input{T0_preamble_' in content:
            return True, "Already standardized"
        
        # Check if it has \begin{document}
        if '\\begin{document}' not in content:
            return True, "Not a standalone document"
        
        # Extract parts
        documentclass, title, author, date, body = extract_document_parts(content)
        
        if not body:
            return False, "Could not extract document body"
        
        # Get content hash before
        hash_before = get_content_hash(body)
        
        # Detect language
        language = detect_language(content, filename)
        
        # Create new document
        new_content = create_standardized_document(
            documentclass, title, author, date, body, language, filename
        )
        
        # Verify content is preserved by extracting and comparing
        _, _, _, _, new_body = extract_document_parts(new_content)
        hash_after = get_content_hash(new_body)
        
        if hash_before != hash_after:
            return False, f"Content verification failed (hash mismatch)"
        
        if dry_run:
            return True, f"Would convert (content hash: {hash_before[:8]})"
        
        # Backup original
        if backup:
            backup_path = filepath.with_suffix('.tex.bak')
            shutil.copy2(filepath, backup_path)
        
        # Write new content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, f"Converted successfully (content hash: {hash_before[:8]})"
        
    except Exception as e:
        return False, f"Error: {str(e)[:100]}"


def main():
    parser = argparse.ArgumentParser(description='Convert LaTeX documents with content preservation')
    parser.add_argument('--file', type=str, help='Convert a single file')
    parser.add_argument('--all', action='store_true', help='Convert all .tex files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    parser.add_argument('--no-backup', action='store_true', help='Do not create backup files')
    
    args = parser.parse_args()
    
    tex_dir = Path(__file__).parent
    
    if args.file:
        files = [tex_dir / args.file]
    elif args.all:
        files = sorted(tex_dir.glob('*.tex'))
    else:
        parser.print_help()
        return 1
    
    print("=" * 60)
    print("T0 LaTeX Content Preservation Converter")
    print("=" * 60)
    print(f"Mode: {'Dry run' if args.dry_run else 'Convert'}")
    print(f"Backup: {'No' if args.no_backup else 'Yes'}")
    print(f"Files: {len(files)}")
    print("=" * 60)
    
    results = {'success': 0, 'skipped': 0, 'failed': 0}
    
    for filepath in files:
        success, message = convert_file(filepath, args.dry_run, not args.no_backup)
        
        if 'Skipped' in message or 'Already' in message or 'Not a standalone' in message:
            results['skipped'] += 1
            print(f"  [SKIP] {filepath.name}: {message}")
        elif success:
            results['success'] += 1
            print(f"  [OK]   {filepath.name}: {message}")
        else:
            results['failed'] += 1
            print(f"  [FAIL] {filepath.name}: {message}")
    
    print("=" * 60)
    print(f"Results: {results['success']} converted, {results['skipped']} skipped, {results['failed']} failed")
    print("=" * 60)
    
    return 0 if results['failed'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
