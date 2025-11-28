#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T0 LaTeX PDF Generator
======================

This script compiles all T0 LaTeX documents to PDF format using pdflatex.
It processes files in parallel and generates a report of successful and failed compilations.

Usage:
    python compile_all_pdfs.py [--output-dir OUTDIR] [--jobs N]

Author: Johann Pascher
Date: 2025
"""

import os
import subprocess
import sys
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import shutil


def compile_latex(tex_file: Path, output_dir: Path, max_runs: int = 2) -> tuple:
    """
    Compile a LaTeX file to PDF.
    
    Args:
        tex_file: Path to the .tex file
        output_dir: Directory to store the PDF
        max_runs: Maximum number of pdflatex runs (for references)
        
    Returns:
        Tuple of (filename, success, message)
    """
    filename = tex_file.name
    
    # Skip preamble files and chapter files
    if filename.startswith('T0_preamble_') or filename.endswith('_ch.tex'):
        return (filename, None, "Skipped (preamble/chapter file)")
    
    if filename.startswith('pri') and not filename.startswith('principle'):
        return (filename, None, "Skipped (preamble file)")
    
    try:
        # Create temp directory for compilation
        work_dir = tex_file.parent
        
        for run in range(max_runs):
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 
                 f'-output-directory={work_dir}', str(tex_file)],
                capture_output=True,
                timeout=120,
                cwd=work_dir,
                encoding='latin-1',
                errors='replace'
            )
        
        # Check if PDF was created
        pdf_name = tex_file.stem + '.pdf'
        pdf_path = work_dir / pdf_name
        
        if pdf_path.exists():
            # Move PDF to output directory if different
            if output_dir != work_dir:
                target_path = output_dir / pdf_name
                shutil.copy2(pdf_path, target_path)
            return (filename, True, f"Success: {pdf_name}")
        else:
            # Extract error from log
            log_path = work_dir / (tex_file.stem + '.log')
            error_msg = "PDF not created"
            if log_path.exists():
                with open(log_path, 'r', errors='ignore') as f:
                    log_content = f.read()
                    # Find first error
                    for line in log_content.split('\n'):
                        if line.startswith('!'):
                            error_msg = line[:100]
                            break
            return (filename, False, error_msg)
            
    except subprocess.TimeoutExpired:
        return (filename, False, "Timeout (>120s)")
    except Exception as e:
        return (filename, False, str(e)[:100])


def clean_aux_files(tex_dir: Path):
    """Remove auxiliary LaTeX files."""
    patterns = ['*.aux', '*.log', '*.out', '*.toc', '*.lof', '*.lot', 
                '*.fls', '*.fdb_latexmk', '*.synctex.gz', '*.bbl', '*.blg']
    for pattern in patterns:
        for f in tex_dir.glob(pattern):
            try:
                f.unlink()
            except:
                pass


def main():
    parser = argparse.ArgumentParser(description='Compile all T0 LaTeX documents to PDF')
    parser.add_argument('--output-dir', type=str, default='../pdf',
                        help='Output directory for PDFs (default: ../pdf)')
    parser.add_argument('--jobs', '-j', type=int, default=4,
                        help='Number of parallel jobs (default: 4)')
    parser.add_argument('--clean', action='store_true',
                        help='Clean auxiliary files after compilation')
    parser.add_argument('--file', type=str,
                        help='Compile only the specified file')
    
    args = parser.parse_args()
    
    tex_dir = Path(__file__).parent
    output_dir = (tex_dir / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if args.file:
        tex_files = [tex_dir / args.file]
    else:
        tex_files = sorted(tex_dir.glob('*.tex'))
    
    print(f"{'='*60}")
    print("T0 LaTeX PDF Generator")
    print(f"{'='*60}")
    print(f"Source directory: {tex_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Files to process: {len(tex_files)}")
    print(f"Parallel jobs: {args.jobs}")
    print(f"{'='*60}\n")
    
    results = {'success': [], 'failed': [], 'skipped': []}
    
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {executor.submit(compile_latex, f, output_dir): f for f in tex_files}
        
        for future in as_completed(futures):
            filename, success, message = future.result()
            
            if success is None:
                results['skipped'].append((filename, message))
                print(f"  [SKIP] {filename}")
            elif success:
                results['success'].append((filename, message))
                print(f"  [OK]   {filename}")
            else:
                results['failed'].append((filename, message))
                print(f"  [FAIL] {filename}: {message}")
    
    if args.clean:
        print("\nCleaning auxiliary files...")
        clean_aux_files(tex_dir)
    
    print(f"\n{'='*60}")
    print("Summary:")
    print(f"  Successful: {len(results['success'])}")
    print(f"  Failed:     {len(results['failed'])}")
    print(f"  Skipped:    {len(results['skipped'])}")
    print(f"{'='*60}")
    
    if results['failed']:
        print("\nFailed files:")
        for filename, message in results['failed']:
            print(f"  - {filename}: {message}")
    
    return 0 if not results['failed'] else 1


if __name__ == '__main__':
    sys.exit(main())
