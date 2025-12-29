#!/usr/bin/env python3
"""
Script to prepare all 44 DVFT chapters as standalone files for comparison.

This script:
1. Processes chapters 1-11 from tex_DVFT_T0/ directory
2. Uses already combined chapters 12-44 from combined_chapters/
3. Creates a complete set of 44 standalone chapter files in all_chapters_standalone/

Usage:
    python3 prepare_all_chapters_for_comparison.py
"""

import os
import re
import shutil
from pathlib import Path

# Base paths
REPO_ROOT = Path("/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality")
DVFT_DIR = REPO_ROOT / "2/tex-n/de_DVFT"
INDIVIDUAL_DIR = DVFT_DIR / "tex_DVFT_T0"
COMBINED_DIR = DVFT_DIR / "combined_chapters"
OUTPUT_DIR = DVFT_DIR / "all_chapters_standalone"

# LaTeX preamble for standalone chapters 1-11
PREAMBLE = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[ngerman]{babel}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{geometry}
\geometry{a4paper,left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{float}

\begin{document}
"""

POSTAMBLE = r"""
\end{document}
"""

def extract_chapter_content(filepath):
    """Extract the main content from a LaTeX chapter file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove comment lines at the start (like % kapitel_XX.tex)
    lines = content.split('\n')
    content_lines = []
    started = False
    
    for line in lines:
        # Skip initial comment lines
        if line.strip().startswith('%') and not started:
            continue
        started = True
        content_lines.append(line)
    
    return '\n'.join(content_lines)

def create_standalone_chapter(chapter_num, source_file, output_file):
    """Create a standalone LaTeX file for a chapter."""
    print(f"  Processing chapter {chapter_num}...")
    
    # Read source content
    content = extract_chapter_content(source_file)
    
    # Extract title from content if possible
    title_match = re.search(r'\\section\{(.*?)\}', content)
    title = title_match.group(1) if title_match else f"Kapitel {chapter_num}"
    
    # Create standalone document
    standalone_content = PREAMBLE
    standalone_content += f"\n\\title{{Kapitel {chapter_num}: {title}}}\n"
    standalone_content += r"\author{}"
    standalone_content += "\n\\date{Dezember 2025}\n\n"
    standalone_content += r"\maketitle"
    standalone_content += "\n\n"
    standalone_content += content
    standalone_content += "\n\n"
    standalone_content += POSTAMBLE
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(standalone_content)
    
    print(f"    ✓ Created: {output_file.name}")

def copy_combined_chapter(chapter_num, source_file, output_file):
    """Copy a combined chapter to the output directory."""
    print(f"  Copying chapter {chapter_num}...")
    shutil.copy2(source_file, output_file)
    print(f"    ✓ Copied: {output_file.name}")

def main():
    print("=" * 70)
    print("DVFT Chapter Preparation for Comparison")
    print("=" * 70)
    print()
    
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    # Process chapters 1-11 from individual files
    print("Processing Chapters 1-11 (from individual files):")
    print("-" * 70)
    
    for i in range(1, 12):
        chapter_num = f"{i:02d}"
        source_file = INDIVIDUAL_DIR / f"kapitel_{chapter_num}.tex"
        output_file = OUTPUT_DIR / f"kapitel_{chapter_num}_standalone.tex"
        
        if source_file.exists():
            create_standalone_chapter(i, source_file, output_file)
        else:
            print(f"  ⚠ Warning: {source_file.name} not found")
    
    print()
    
    # Copy chapters 12-44 from combined directory (or fallback to individual)
    print("Processing Chapters 12-44 (from combined files):")
    print("-" * 70)
    
    copied_count = 0
    for i in range(12, 45):
        chapter_num = f"{i:02d}"
        source_file = COMBINED_DIR / f"kapitel_{chapter_num}_combined.tex"
        output_file = OUTPUT_DIR / f"kapitel_{chapter_num}_standalone.tex"
        
        if source_file.exists():
            copy_combined_chapter(i, source_file, output_file)
            copied_count += 1
        else:
            # Try without leading zero for chapters > 19
            if i >= 20:
                source_file = COMBINED_DIR / f"kapitel_{i}_combined.tex"
                if source_file.exists():
                    copy_combined_chapter(i, source_file, output_file)
                    copied_count += 1
                    continue
            
            # Fallback to individual file if combined doesn't exist
            individual_file = INDIVIDUAL_DIR / f"kapitel_{chapter_num}.tex"
            if individual_file.exists():
                print(f"  ⚠ Combined version not found, using individual file for chapter {i}")
                create_standalone_chapter(i, individual_file, output_file)
                copied_count += 1
            else:
                print(f"  ⚠ Warning: kapitel_{chapter_num} not found in combined or individual")
    
    print()
    print("=" * 70)
    print("Summary:")
    print("=" * 70)
    
    # Count files in output directory
    output_files = list(OUTPUT_DIR.glob("kapitel_*_standalone.tex"))
    print(f"Total standalone chapters created: {len(output_files)}")
    print(f"Expected: 44 chapters")
    
    if len(output_files) == 44:
        print("\n✅ SUCCESS: All 44 chapters prepared for comparison!")
    else:
        print(f"\n⚠ WARNING: Only {len(output_files)} chapters prepared (expected 44)")
    
    print(f"\nOutput location: {OUTPUT_DIR}")
    print()
    
    # Create README
    readme_content = """# All DVFT Chapters - Standalone Files

This directory contains all 44 DVFT chapters as standalone LaTeX files, prepared for comparison and analysis.

## Contents

### Chapters 1-11 (Foundational Theory)
- Extracted from individual files in `tex_DVFT_T0/`
- Wrapped with standalone document structure
- Files: `kapitel_01_standalone.tex` through `kapitel_11_standalone.tex`

### Chapters 12-44 (Applications)
- Copied from combined files in `combined_chapters/`
- Already in standalone format
- Files: `kapitel_12_standalone.tex` through `kapitel_44_standalone.tex`

## Usage

These files can be used for:
1. Side-by-side comparison of different chapter versions
2. Individual compilation of any chapter
3. Mathematical consistency validation
4. Content analysis and extraction

## Compilation

Each file can be compiled independently:
```bash
pdflatex kapitel_XX_standalone.tex
```

## Structure

All files follow a consistent structure:
- Document class: article (12pt, a4paper)
- Standard DVFT packages
- Title, author, date
- Chapter content
- Complete document (\\begin{document} ... \\end{document})
"""
    
    readme_file = OUTPUT_DIR / "README.md"
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ Created: {readme_file.name}")
    print()

if __name__ == "__main__":
    main()
