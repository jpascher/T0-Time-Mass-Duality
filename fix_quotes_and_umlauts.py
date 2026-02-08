"""Fix remaining TeX umlauts and replace double quotes with LaTeX quotes"""
import re
from pathlib import Path

def fix_document(file_path):
    """Fix TeX umlauts and double quotes"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # 1. Fix TeX umlauts
    umlaut_replacements = {
        '\\"a': 'ä', '\\"o': 'ö', '\\"u': 'ü',
        '\\"A': 'Ä', '\\"O': 'Ö', '\\"U': 'Ü',
        '\\ss': 'ß', 'f\\"u': 'für'
    }
    
    for old, new in umlaut_replacements.items():
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changes.append(f"  {old} -> {new} ({count}x)")
    
    # 2. Replace double quotes with LaTeX quotes
    # Pattern: Find "text" and replace with ``text''
    # But skip lines that start with % (comments)
    # And skip things like url{...} and href{...}
    
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Skip comment lines
        if line.strip().startswith('%'):
            fixed_lines.append(line)
            continue
        
        # Skip lines with URLs/hrefs
        if 'url{' in line or 'href{' in line or 'cite{' in line or 'ref{' in line:
            fixed_lines.append(line)
            continue
        
        # Replace " with '' (close quote) or `` (open quote)
        # Simple heuristic: after space/start = open, before space/punctuation = close
        fixed_line = line
        
        # Replace closing quotes (before space, comma, period, etc.)
        fixed_line = re.sub(r'"(\s|,|\.|\)|\]|:|;|$)', r"''\1", fixed_line)
        
        # Replace opening quotes (after space, start, parenthesis, etc.)
        fixed_line = re.sub(r'(\s|\(|\[|^)"', r'\1``', fixed_line)
        
        # Remaining quotes (between words) - default to close
        fixed_line = fixed_line.replace('"', "''")
        
        if fixed_line != line:
            changes.append(f"  Quote change in line")
        
        fixed_lines.append(fixed_line)
    
    content = '\n'.join(fixed_lines)
    
    if content != original:
        # Backup
        backup_path = str(file_path) + '.bak_quotes_umlauts'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original)
        
        # Write fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, changes
    return False, []

# Process all directories
directories = [
    r'C:\Users\johann\B18\2\tex-n\de_standalone',
    r'C:\Users\johann\B18\2\tex-n\en_standalone',
    r'C:\Users\johann\B18\2\tex-n\de_chapters_new',
    r'C:\Users\johann\B18\2\tex-n\en_chapters_new'
]

modified_count = 0
for directory in directories:
    directory = Path(directory)
    if not directory.exists():
        continue
    
    print(f"\n{directory.name}:")
    dir_count = 0
    
    for tex_file in sorted(directory.glob('*.tex')):
        if tex_file.name.startswith('T0_preamble'):
            continue
        
        modified, changes = fix_document(tex_file)
        if modified:
            print(f"  Fixed: {tex_file.name}")
            if changes and len(changes) <= 5:
                for change in changes[:3]:
                    print(change)
            modified_count += 1
            dir_count += 1
    
    if dir_count == 0:
        print("  (keine Änderungen)")

print(f"\n{'='*60}")
print(f"GESAMT: {modified_count} Dateien geändert")
print(f"{'='*60}")
