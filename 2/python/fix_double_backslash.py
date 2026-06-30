#!/usr/bin/env python3
"""
Remove double backslashes before underscores in PDF references.
Converts \\_ to \_ in all .tex files.
"""

import os
import sys

def fix_double_backslash(file_path):
    """Remove double backslashes before underscores."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace \\_ with \_ (double backslash underscore to single)
        # In the file, \\_ is stored as two backslashes + underscore
        content = content.replace('\\\\_', '\\_')
        
        if content != original_content:
            # Create backup
            backup_path = file_path + '.bak_dbl'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Write fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    en_dir = r'C:\Users\johann\B18\2\tex-n\en_standalone'
    
    if not os.path.exists(en_dir):
        print(f"Directory not found: {en_dir}")
        sys.exit(1)
    
    print("=" * 80)
    print("Fixing double backslashes in PDF references (EN)")
    print("=" * 80)
    
    fixed_count = 0
    
    for filename in sorted(os.listdir(en_dir)):
        if not filename.endswith('.tex'):
            continue
        
        file_path = os.path.join(en_dir, filename)
        
        if fix_double_backslash(file_path):
            fixed_count += 1
            print(f"✓ Fixed: {filename}")
    
    print("\n" + "=" * 80)
    print(f"Total files fixed: {fixed_count}")
    print("=" * 80)

if __name__ == '__main__':
    main()
