#!/usr/bin/env python3
"""
Remove HTL Leonding references from all LaTeX documents.
Removes the following patterns:
- "Unveröffentlichtes Manuskript, HTL Leonding."
- ", HTL Leonding, Österreich"
- ", HTL Leonding, Austria"
- ", HTL Leonding"
"""

import os
import glob
from pathlib import Path

# Patterns to remove (in order - most specific first)
PATTERNS_TO_REMOVE = [
    "Unveröffentlichtes Manuskript, HTL Leonding.",
    ", HTL Leonding, Österreich",
    ", HTL Leonding, Austria",
    ", HTL Leonding.",  # With period at end
    ", HTL Leonding (",  # In bibliography entries
    ", HTL Leonding",  # General case - do this last
]

def clean_htl_references(file_path):
    """Remove HTL Leonding references from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        removed_patterns = []
        
        # Apply each pattern removal
        for pattern in PATTERNS_TO_REMOVE:
            if pattern in content:
                content = content.replace(pattern, '')
                removed_patterns.append(pattern)
        
        if content != original_content:
            # Create backup
            backup_path = file_path + '.bak_htl'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Write cleaned content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return removed_patterns
        
        return None
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def main():
    base_dir = r'C:\Users\johann\B18\2\tex-n'
    
    if not os.path.exists(base_dir):
        print(f"Directory not found: {base_dir}")
        return
    
    print("=" * 80)
    print("Removing HTL Leonding references from all LaTeX documents")
    print("=" * 80)
    
    # Find all .tex files recursively
    tex_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip backup directories
        if any(skip in root for skip in ['.bak', 'backup', '_orig']):
            continue
        for file in files:
            if file.endswith('.tex') and not file.endswith('.bak_htl'):
                tex_files.append(os.path.join(root, file))
    
    print(f"\nGefundene .tex Dateien: {len(tex_files)}")
    print("\nVerarbeite Dateien...\n")
    
    total_cleaned = 0
    total_patterns = 0
    
    for file_path in sorted(tex_files):
        removed = clean_htl_references(file_path)
        
        if removed:
            total_cleaned += 1
            total_patterns += len(removed)
            rel_path = os.path.relpath(file_path, base_dir)
            try:
                print(f"OK {rel_path}")
            except UnicodeEncodeError:
                print(f"OK {rel_path.encode('ascii', 'ignore').decode()}")
            for pattern in removed:
                try:
                    print(f"    - Entfernt: '{pattern[:50]}...'")
                except UnicodeEncodeError:
                    print(f"    - Entfernt: [pattern]")
    
    print("\n" + "=" * 80)
    print(f"Dateien bereinigt: {total_cleaned}")
    print(f"Gesamt entfernte Muster: {total_patterns}")
    print("=" * 80)

if __name__ == '__main__':
    main()
