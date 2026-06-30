"""Fix PDF filename comments in preamble - remove incorrect escaping"""
import os
import re
from pathlib import Path

def fix_preamble_comment(file_path):
    """Fix preamble comment with PDF filename"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Find lines like: % Standardized preamble - 003\_T0\_Grundlagen\_v1\_De.pdf
    # The problem is the backslashes before underscores are already escaped in the file
    # This causes LaTeX to see \\ (escaped backslash) followed by _ (which is an error)
    
    # Pattern: Match comment lines with escaped underscores in PDF filenames
    # Replace: \_ with just _  in comment lines
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Only fix in comment lines
        if line.strip().startswith('%') and '.pdf' in line:
            # Remove backslash before underscores in PDF filenames
            line = line.replace('\\_', '_')
        fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    if content != original:
        # Backup
        backup_path = str(file_path) + '.bak_preamble_fix'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original)
        
        # Write fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    return False

# Process all directories
directories = [
    r'C:\Users\johann\B18\2\tex-n\de_standalone',
    r'C:\Users\johann\B18\2\tex-n\en_standalone',
    r'C:\Users\johann\B18\2\tex-n\de_chapters_new',
    r'C:\Users\johann\B18\2\tex-n\en_chapters_new'
]

modified_count = 0
for directory in directories:
    if not os.path.exists(directory):
        continue
    
    for tex_file in Path(directory).glob('*.tex'):
        if tex_file.name.startswith('T0_preamble'):
            continue
            
        if fix_preamble_comment(tex_file):
            print(f"Fixed: {tex_file.name}")
            modified_count += 1

print(f"\n{modified_count} files modified")
