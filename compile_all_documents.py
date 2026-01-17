#!/usr/bin/env python3
"""
Compile all German and English LaTeX documents with ebook preamble.
Fix errors iteratively and track progress.
"""
import subprocess
import os
import re
from pathlib import Path

def compile_document(tex_file, output_dir):
    """Compile a single LaTeX document with lualatex."""
    try:
        result = subprocess.run(
            ['lualatex', '-interaction=nonstopmode', '-output-directory', output_dir, tex_file],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=output_dir
        )
        return result.returncode == 0, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"
    except Exception as e:
        return False, str(e)

def main():
    base_dir = Path('/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality')
    
    de_dir = base_dir / '2/tex-n/de_standalone'
    en_dir = base_dir / '2/tex-n/en_standalone'
    
    # Get all .tex files with number prefixes
    de_files = sorted([f for f in os.listdir(de_dir) if f.endswith('.tex') and re.match(r'^\d', f)])
    en_files = sorted([f for f in os.listdir(en_dir) if f.endswith('.tex') and re.match(r'^\d', f)])
    
    print(f"Found {len(de_files)} German files and {len(en_files)} English files")
    print(f"Total: {len(de_files) + len(en_files)} documents to compile\n")
    
    success_count = 0
    fail_count = 0
    failed_docs = []
    
    # Compile German documents
    print("=" * 60)
    print("COMPILING GERMAN DOCUMENTS")
    print("=" * 60)
    for i, filename in enumerate(de_files[:50], 1):  # First 50 for this batch
        tex_path = de_dir / filename
        print(f"[{i}/{len(de_files[:50])}] Compiling {filename}...", end=" ")
        success, log = compile_document(filename, str(de_dir))
        if success:
            print("✓")
            success_count += 1
        else:
            print("✗")
            fail_count += 1
            failed_docs.append((filename, "DE"))
    
    # Compile English documents
    print("\n" + "=" * 60)
    print("COMPILING ENGLISH DOCUMENTS")
    print("=" * 60)
    for i, filename in enumerate(en_files[:50], 1):  # First 50 for this batch
        tex_path = en_dir / filename
        print(f"[{i}/{len(en_files[:50])}] Compiling {filename}...", end=" ")
        success, log = compile_document(filename, str(en_dir))
        if success:
            print("✓")
            success_count += 1
        else:
            print("✗")
            fail_count += 1
            failed_docs.append((filename, "EN"))
    
    print("\n" + "=" * 60)
    print("COMPILATION SUMMARY")
    print("=" * 60)
    print(f"Successful: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Success rate: {100*success_count/(success_count+fail_count):.1f}%")
    
    if failed_docs:
        print(f"\nFailed documents ({len(failed_docs)}):")
        for doc, lang in failed_docs[:10]:  # Show first 10
            print(f"  - {doc} ({lang})")
        if len(failed_docs) > 10:
            print(f"  ... and {len(failed_docs) - 10} more")

if __name__ == '__main__':
    main()
