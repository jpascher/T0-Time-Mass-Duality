#!/usr/bin/env python3
"""
Script to remove ALL \resizebox commands from LaTeX chapter files.
This addresses the systematic KDP rejection issue where table structures
trigger automated readability flags.

Strategy:
- Find all \resizebox{\textwidth}{!}{ ... } commands
- Extract the table content inside
- Replace with the table content directly (no resizebox wrapper)
- Preserve all other formatting
"""

import re
import os
import sys
from pathlib import Path

def remove_resizebox_from_content(content):
    """
    Remove \resizebox commands while preserving inner content.
    Handles nested braces correctly.
    """
    
    modified = content
    changes_made = 0
    
    # Pattern to match \resizebox{\textwidth}{!}{...} with optional % and whitespace
    while '\\resizebox{\\textwidth}{!}{' in modified or '\\resizebox{\\textwidth}{!}' in modified:
        # Find the start of \resizebox
        start_idx = modified.find('\\resizebox{\\textwidth}{!}')
        if start_idx == -1:
            break
        
        # Skip past \resizebox{\textwidth}{!}
        idx = start_idx + len('\\resizebox{\\textwidth}{!}')
        
        # Skip optional % and whitespace
        while idx < len(modified) and modified[idx] in '%\n\r\t ':
            idx += 1
        
        # Now we should be at the opening brace
        if idx >= len(modified) or modified[idx] != '{':
            print(f"WARNING: Expected opening brace at position {idx}")
            break
        
        # Find the matching closing brace
        brace_count = 0
        content_start = idx + 1
        idx = content_start
        
        while idx < len(modified):
            if modified[idx] == '{' and (idx == 0 or modified[idx-1] != '\\'):
                brace_count += 1
            elif modified[idx] == '}' and (idx == 0 or modified[idx-1] != '\\'):
                if brace_count == 0:
                    # This is the matching closing brace
                    inner_content = modified[content_start:idx]
                    # Replace the entire \resizebox{...}{...}{...} with just the inner content
                    modified = modified[:start_idx] + inner_content + modified[idx+1:]
                    changes_made += 1
                    break
                else:
                    brace_count -= 1
            idx += 1
        else:
            # Couldn't find matching brace, skip this one
            print(f"WARNING: Could not find matching brace for resizebox at position {start_idx}")
            break
    
    return modified, changes_made

def process_file(filepath):
    """Process a single LaTeX file to remove resizebox commands."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified_content, changes = remove_resizebox_from_content(content)
        
        if changes > 0:
            # Create backup
            backup_path = str(filepath) + '.BACKUP_RESIZEBOX'
            if not os.path.exists(backup_path):
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            # Write modified content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            print(f"✓ {filepath.name}: Removed {changes} resizebox command(s)")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"✗ ERROR processing {filepath}: {e}")
        return False

def main():
    repo_root = Path('/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality')
    
    # Process both German and English chapter directories
    directories = [
        repo_root / '2/tex-n/de_chapters_new',
        repo_root / '2/tex-n/en_chapters_new'
    ]
    
    total_processed = 0
    total_modified = 0
    
    for directory in directories:
        print(f"\nProcessing directory: {directory}")
        print("=" * 80)
        
        for tex_file in sorted(directory.glob('*_ch.tex')):
            if process_file(tex_file):
                total_modified += 1
            total_processed += 1
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: Processed {total_processed} files, modified {total_modified} files")
    print("=" * 80)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
