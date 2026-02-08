"""Remove 'Fazit: Die T0-Revolution' sections from all documents"""
import re
from pathlib import Path

def remove_fazit_revolution(file_path):
    """Remove sections titled 'Fazit: Die T0-Revolution' or similar"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Patterns to match section titles
    patterns = [
        r'\\section\{Fazit:?\s+Die\s+T0-Revolution\}.*?(?=\\section|\\chapter|\\end\{document\}|$)',
        r'\\subsection\{Fazit:?\s+Die\s+T0-Revolution\}.*?(?=\\subsection|\\section|\\chapter|\\end\{document\}|$)',
        r'\\section\*\{Fazit:?\s+Die\s+T0-Revolution\}.*?(?=\\section|\\chapter|\\end\{document\}|$)',
        # English variants
        r'\\section\{Conclusion:?\s+The\s+T0\s+Revolution\}.*?(?=\\section|\\chapter|\\end\{document\}|$)',
        r'\\subsection\{Conclusion:?\s+The\s+T0\s+Revolution\}.*?(?=\\subsection|\\section|\\chapter|\\end\{document\}|$)',
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Clean up multiple blank lines
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    if content != original:
        # Backup
        backup_path = str(file_path) + '.bak_fazit_removal'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original)
        
        # Write fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    return False

# Process main directories
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
        
        if remove_fazit_revolution(tex_file):
            print(f"  Removed Fazit: {tex_file.name}")
            modified_count += 1
            dir_count += 1
    
    if dir_count == 0:
        print("  (keine Änderungen)")

print(f"\n{'='*60}")
print(f"GESAMT: {modified_count} Dateien geändert")
print(f"{'='*60}")
