"""Remove HTL Leonding references and email address from all documents"""
import re
from pathlib import Path

def remove_htl_references(file_path):
    """Remove HTL references and email from document"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Patterns to remove (case-insensitive)
    patterns_to_remove = [
        r'Höhere Technische Lehranstalt Leonding[,\s]*Österreich',
        r'HTL Leonding[,\s]*Österreich',
        r'HTL Leonding',
        r'Kontakt:\s*johann\.pascher@gmail\.com',
        r'johann\.pascher@gmail\.com',
        r'Leonding[,\s]*Österreich',
    ]
    
    for pattern in patterns_to_remove:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)
    
    # Clean up multiple blank lines
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    if content != original:
        # Backup
        backup_path = str(file_path) + '.bak_htl_removal'
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
    directory = Path(directory)
    if not directory.exists():
        continue
    
    print(f"\n{directory.name}:")
    dir_count = 0
    
    for tex_file in sorted(directory.glob('*.tex')):
        if remove_htl_references(tex_file):
            print(f"  Removed HTL: {tex_file.name}")
            modified_count += 1
            dir_count += 1
    
    if dir_count == 0:
        print("  (keine Änderungen)")

print(f"\n{'='*60}")
print(f"GESAMT: {modified_count} Dateien geändert")
print(f"{'='*60}")
