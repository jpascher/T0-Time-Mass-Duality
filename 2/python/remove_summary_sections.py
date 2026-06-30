#!/usr/bin/env python3
"""
Remove summary, future, and conclusion sections from LaTeX files.
Preserves content and calculations - only removes specific sections.
"""

import os
import re
from pathlib import Path
import shutil

def find_section_end(lines, start_index, section_level):
    """
    Find the end of a section by looking for the next section of same or higher level.
    Returns the index of the line before the next section.
    """
    # Map section commands to hierarchy levels
    level_map = {
        'chapter': 1,
        'section': 2,
        'subsection': 3,
        'subsubsection': 4
    }
    
    current_level = level_map.get(section_level, 2)
    
    # Start searching from the line after the section command
    for i in range(start_index + 1, len(lines)):
        line = lines[i]
        
        # Check for section commands at same or higher level
        for cmd in ['chapter', 'section', 'subsection', 'subsubsection']:
            if level_map[cmd] <= current_level:
                pattern = rf'^\s*\\{cmd}\*?\{{'
                if re.match(pattern, line):
                    return i - 1  # Return index before the new section
    
    # If no next section found, return end of document (before \end{document} if present)
    for i in range(len(lines) - 1, start_index, -1):
        if re.match(r'^\s*\\end\{document\}', lines[i]):
            return i - 1
    
    return len(lines) - 1

def should_remove_section(title):
    """Check if section should be removed based on title"""
    title_lower = title.lower()
    
    # Keywords that indicate sections to remove
    remove_keywords = [
        'zusammenfassung',
        'zukunft',
        'ausblick',
        'zukünftig',
        'summary',
        'conclusion',
        'future',
        'outlook',
        'perspectives'
    ]
    
    # Check if any keyword is in the title
    for keyword in remove_keywords:
        if keyword in title_lower:
            return True
    
    return False

def remove_sections(file_path):
    """Remove summary/future sections from a LaTeX file"""
    
    print(f"\nFile: {file_path.name}")
    
    # Create backup
    backup_path = file_path.with_suffix('.tex.bak_summary_removal')
    shutil.copy2(file_path, backup_path)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        original_line_count = len(lines)
        
        # Find all sections to remove
        sections_to_remove = []
        
        pattern = r'^(\s*)\\(chapter|section|subsection|subsubsection)(\*?)\{([^}]+)\}'
        
        for i, line in enumerate(lines):
            match = re.match(pattern, line)
            if match:
                indent = match.group(1)
                section_type = match.group(2)
                starred = match.group(3)
                title = match.group(4)
                
                if should_remove_section(title):
                    # Find where this section ends
                    end_index = find_section_end(lines, i, section_type)
                    sections_to_remove.append((i, end_index, title))
                    print(f"  Marked for removal: \\{section_type}{starred}{{{title}}} (Lines {i+1}-{end_index+1})")
        
        if not sections_to_remove:
            print(f"  OK: No sections to remove")
            backup_path.unlink()  # Remove unnecessary backup
            return False
        
        # Remove sections in reverse order to maintain indices
        sections_to_remove.sort(reverse=True)
        
        removed_lines = 0
        for start, end, title in sections_to_remove:
            # Remove lines from start to end (inclusive)
            del lines[start:end+1]
            removed_lines += (end - start + 1)
        
        # Check if file still has substantial content
        new_content = '\n'.join(lines)
        
        # Verify file still has content (at least some equations or text)
        has_content = bool(re.search(r'\\begin\{(equation|align|enumerate|itemize|description)', new_content))
        has_text = len(new_content.strip()) > 500  # At least 500 characters
        
        if not has_content and not has_text:
            print(f"  WARNING: File would become too empty! Changes NOT saved.")
            backup_path.unlink()
            return False
        
        # Write modified file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  DONE: Deleted {removed_lines} lines")
        print(f"  Stats: {original_line_count} -> {len(lines)} lines")
        
        return True
        
    except Exception as e:
        print(f"  ERROR: {e}")
        # Restore backup on error
        if backup_path.exists():
            shutil.copy2(backup_path, file_path)
            backup_path.unlink()
        return False

def main():
    base_dir = Path(r"C:\Users\johann\B18\2\tex-n")
    
    directories = [
        base_dir / "de_standalone",
        base_dir / "en_standalone",
        base_dir / "de_chapters_new",
        base_dir / "en_chapters_new"
    ]
    
    print("=" * 80)
    print("ENTFERNE ZUSAMMENFASSUNGS- UND ZUKUNFTS-ABSCHNITTE")
    print("=" * 80)
    
    total_files = 0
    modified_files = 0
    
    for directory in directories:
        print(f"\n\n{'='*80}")
        print(f"Directory: {directory.name}")
        print("="*80)
        
        tex_files = sorted(directory.glob("*.tex"))
        print(f"Gefunden: {len(tex_files)} .tex Dateien")
        
        for tex_file in tex_files:
            total_files += 1
            if remove_sections(tex_file):
                modified_files += 1
    
    print("\n" + "="*80)
    print("ZUSAMMENFASSUNG")
    print("="*80)
    print(f"Geprüft: {total_files} Dateien")
    print(f"Modifiziert: {modified_files} Dateien")
    print(f"Backups erstellt: {modified_files} (.bak_summary_removal)")
    print("="*80)

if __name__ == "__main__":
    main()
