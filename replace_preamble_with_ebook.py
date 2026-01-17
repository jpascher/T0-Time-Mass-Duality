#!/usr/bin/env python3
import os
import re
import sys

def replace_preamble_in_file(filepath):
    """Replace T0_preamble_shared with T0_preamble_shared-ebook in a LaTeX file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace German preamble
        content = re.sub(
            r'\\input\{([^}]*/)T0_preamble_shared_De\}',
            r'\\input{\1T0_preamble_shared-ebook_De}',
            content
        )
        
        # Replace English preamble
        content = re.sub(
            r'\\input\{([^}]*/)T0_preamble_shared_En\}',
            r'\\input{\1T0_preamble_shared-ebook_En}',
            content
        )
        
        # Check if any changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    base_dirs = ['2/tex-n/de_standalone', '2/tex-n/en_standalone']
    total_changed = 0
    
    for base_dir in base_dirs:
        if not os.path.exists(base_dir):
            continue
            
        for filename in os.listdir(base_dir):
            if filename.endswith('.tex'):
                filepath = os.path.join(base_dir, filename)
                if replace_preamble_in_file(filepath):
                    total_changed += 1
                    print(f"✓ Updated: {filepath}")
    
    print(f"\n✅ Total files updated: {total_changed}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
