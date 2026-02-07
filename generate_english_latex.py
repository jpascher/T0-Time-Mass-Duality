#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T0 Theory: English LaTeX Document Generator
============================================

This script recursively processes German LaTeX documents and creates
numbered English versions for the T0 Theory collection.

Usage:
  python3 generate_english_latex.py [--source-dir DIR] [--output-dir DIR] [--compile]

Author: Johann Pascher / Copilot
Date: 2025
"""

import os
import sys
import subprocess
import re
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse

# Source and output directories
DEFAULT_SOURCE_DIR = "2/tex/chapters"
DEFAULT_OUTPUT_DIR = "2/tex/chapters_en_numbered"

def get_document_title(tex_content):
  """Extract document title from LaTeX content."""
  # Try to find section/chapter title
  patterns = [
    r'\\chapter\{([^}]+)\}',
    r'\\section\{([^}]+)\}',
    r'\\subsection\*?\{([^}]+)\}',
    r'\\subsubsection\*?\{([^}]+)\}',
    r'\\title\{([^}]+)\}'
  ]
  for pattern in patterns:
    match = re.search(pattern, tex_content)
    if match:
      return match.group(1).strip()
  return None

def create_standalone_tex(chapter_file, output_dir, number, preamble_path):
  """Create a standalone compilable LaTeX document from a chapter file."""
  basename = os.path.basename(chapter_file)
  
  # Create output filename with number prefix
  name_without_ext = os.path.splitext(basename)[0]
  # Replace _De with _En if present
  if '_De' in name_without_ext:
    name_without_ext = name_without_ext.replace('_De', '_En')
  elif not '_En' in name_without_ext:
    name_without_ext = name_without_ext + '_En'
  
  # Add number prefix
  output_name = f"{number:03d}_{name_without_ext}.tex"
  output_path = os.path.join(output_dir, output_name)
  
  # Read chapter content
  try:
    with open(chapter_file, 'r', encoding='utf-8') as f:
      chapter_content = f.read()
  except Exception as e:
    print(f"Error reading {chapter_file}: {e}")
    return None
  
  # Get document title
  title = get_document_title(chapter_content) or name_without_ext
  
  # Convert \chapter to \section for article class
  chapter_content = re.sub(r'\\chapter\[([^\]]+)\]\{([^}]+)\}', r'\\section[\1]{\2}', chapter_content)
  chapter_content = re.sub(r'\\chapter\{([^}]+)\}', r'\\section{\1}', chapter_content)
  
  # Create standalone document
  standalone_doc = f'''\\documentclass[12pt,a4paper]{{article}}
\\input{{{preamble_path}}}

\\title{{{title}}}
\\author{{Johann Pascher}}
\\date{{2025}}

\\begin{{document}}
\\maketitle
\\tableofcontents
\\newpage

{chapter_content}

\\end{{document}}
'''
  
  # Write the standalone document
  try:
    with open(output_path, 'w', encoding='utf-8') as f:
      f.write(standalone_doc)
    print(f"Created: {output_name}")
    return output_path
  except Exception as e:
    print(f"Error writing {output_path}: {e}")
    return None

def compile_tex_to_pdf(tex_file, output_dir=None):
  """Compile a .tex file to PDF using pdflatex."""
  tex_dir = os.path.dirname(tex_file)
  tex_basename = os.path.basename(tex_file)
  
  try:
    # Run pdflatex twice for proper references
    for run in range(2):
      result = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', tex_basename],
        cwd=tex_dir,
        capture_output=True,
        timeout=120,
        encoding='latin-1',
        errors='replace'
      )
    
    pdf_name = os.path.splitext(tex_basename)[0] + '.pdf'
    pdf_path = os.path.join(tex_dir, pdf_name)
    
    if os.path.exists(pdf_path):
      # Move PDF to output directory if specified
      if output_dir and output_dir != tex_dir:
        target = os.path.join(output_dir, pdf_name)
        shutil.move(pdf_path, target)
        print(f" [OK] {pdf_name}")
        return target
      else:
        print(f" [OK] {pdf_name}")
        return pdf_path
    else:
      print(f" [FAIL] {tex_basename}")
      return None
      
  except subprocess.TimeoutExpired:
    print(f" [TIMEOUT] {tex_basename}")
    return None
  except Exception as e:
    print(f" [ERROR] {tex_basename}: {e}")
    return None

def clean_aux_files(directory):
  """Remove auxiliary LaTeX files."""
  patterns = ['*.aux', '*.log', '*.out', '*.toc', '*.lof', '*.lot', 
        '*.fls', '*.fdb_latexmk', '*.synctex.gz', '*.bbl', '*.blg']
  for pattern in patterns:
    for f in Path(directory).glob(pattern):
      try:
        f.unlink()
      except:
        pass

def main():
  parser = argparse.ArgumentParser(description='Generate English LaTeX documents from T0 sources')
  parser.add_argument('--source-dir', type=str, default=DEFAULT_SOURCE_DIR,
            help=f'Source directory with German chapters (default: {DEFAULT_SOURCE_DIR})')
  parser.add_argument('--output-dir', type=str, default=DEFAULT_OUTPUT_DIR,
            help=f'Output directory for English documents (default: {DEFAULT_OUTPUT_DIR})')
  parser.add_argument('--compile', action='store_true',
            help='Compile generated .tex files to PDF')
  parser.add_argument('--pdf-dir', type=str, default='2/pdf/en',
            help='Output directory for PDFs (default: 2/pdf/en)')
  parser.add_argument('--preamble', type=str, default='../T0_preamble_En',
            help='Path to preamble file (relative to output dir)')
  parser.add_argument('--clean', action='store_true',
            help='Clean auxiliary files after compilation')
  
  args = parser.parse_args()
  
  # Get absolute paths
  script_dir = Path(__file__).parent.resolve()
  source_dir = script_dir / args.source_dir
  output_dir = script_dir / args.output_dir
  pdf_dir = script_dir / args.pdf_dir
  
  print("=" * 60)
  print("T0 Theory: English LaTeX Document Generator")
  print("=" * 60)
  print(f"Source directory: {source_dir}")
  print(f"Output directory: {output_dir}")
  print(f"PDF directory:  {pdf_dir}")
  print("=" * 60)
  print()
  
  # Create output directories
  output_dir.mkdir(parents=True, exist_ok=True)
  if args.compile:
    pdf_dir.mkdir(parents=True, exist_ok=True)
  
  # Find all German chapter files
  if not source_dir.exists():
    print(f"Error: Source directory not found: {source_dir}")
    # Try to find chapters in chapters_en directory
    source_dir = script_dir / "2/tex/chapters_en"
    if source_dir.exists():
      print(f"Using existing English chapters from: {source_dir}")
    else:
      return 1
  
  tex_files = sorted([f for f in source_dir.glob("*.tex") if f.is_file()])
  print(f"Found {len(tex_files)} source files")
  print()
  
  # Process each file
  created_files = []
  for i, tex_file in enumerate(tex_files, start=1):
    result = create_standalone_tex(str(tex_file), str(output_dir), i, args.preamble)
    if result:
      created_files.append(result)
  
  print()
  print(f"Created {len(created_files)} standalone documents")
  
  # Compile to PDF if requested
  if args.compile and created_files:
    print()
    print("Compiling to PDF...")
    print("-" * 40)
    
    successful = 0
    for tex_file in created_files:
      pdf = compile_tex_to_pdf(tex_file, str(pdf_dir))
      if pdf:
        successful += 1
    
    print()
    print(f"Successfully compiled: {successful}/{len(created_files)}")
  
  # Clean auxiliary files if requested
  if args.clean:
    print()
    print("Cleaning auxiliary files...")
    clean_aux_files(str(output_dir))
  
  print()
  print("Done!")
  return 0

if __name__ == '__main__':
  sys.exit(main())

