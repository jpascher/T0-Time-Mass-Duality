"""Fix double backslashes before LaTeX commands"""
import re
from pathlib import Path

def fix_double_backslashes(file_path):
    """Fix double backslashes before LaTeX commands"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Skip comment lines
        if line.strip().startswith('%'):
            fixed_lines.append(line)
            continue
        
        # Replace \\command with \command (but not \\ at end of line)
        # Match: \\ followed by letter (start of command)
        fixed_line = re.sub(r'\\\\([a-zA-Z])', r'\\\1', line)
        fixed_lines.append(fixed_line)
    
    content = '\n'.join(fixed_lines)
    
    if content != original:
        # Backup
        backup_path = str(file_path) + '.bak_dbl_cmd'
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
    r'C:\Users\johann\B18\2\tex-n\en_standalone'
]

modified_count = 0
for directory in directories:
    directory = Path(directory)
    if not directory.exists():
        continue
    
    for tex_file in directory.glob('*.tex'):
        if tex_file.name.startswith('T0_preamble'):
            continue
            
        if fix_double_backslashes(tex_file):
            print(f"Fixed: {tex_file.name}")
            modified_count += 1

print(f"\n{modified_count} files modified")
