#!/usr/bin/env python3
"""
Normalize German quotation marks in DE narrative files.
Converts Unicode and ASCII quotes to LaTeX format ``Text''.
"""

import os
import re
import sys

def is_in_math_environment(text, pos):
    """Check if position is inside a math environment."""
    # Simple heuristic: count $ and \( before position
    before = text[:pos]
    
    # Count inline math delimiters
    dollar_count = before.count('$') - before.count(r'\$')
    if dollar_count % 2 == 1:
        return True
    
    # Count \(...\) pairs
    inline_open = len(re.findall(r'\\\(', before))
    inline_close = len(re.findall(r'\\\)', before))
    if inline_open > inline_close:
        return True
    
    # Check for display math environments
    display_envs = ['equation', 'align', 'gather', 'multline', 'flalign', 'alignat']
    for env in display_envs:
        begin_count = len(re.findall(rf'\\begin\{{{env}\*?\}}', before))
        end_count = len(re.findall(rf'\\end\{{{env}\*?\}}', before))
        if begin_count > end_count:
            return True
    
    # Check \[...\]
    display_open = len(re.findall(r'\\\[', before))
    display_close = len(re.findall(r'\\\]', before))
    if display_open > display_close:
        return True
    
    return False

def is_in_url_or_command(text, pos):
    """Check if position is inside URL or special commands."""
    # Look back for \url{, \href{
    before = text[:pos]
    
    # Simple check: find last \url{ or \href{ before position
    url_match = re.search(r'\\(url|href)\{[^}]*$', before)
    if url_match:
        # Check if there's a closing brace after position
        after = text[pos:]
        if '}' in after:
            return True
    
    return False

def normalize_quotes_in_file(filepath):
    """Normalize quotes in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
        return False
    
    original_content = content
    changes_made = False
    
    # Step 1: Replace Unicode quotes
    # „ → `` (opening quote)
    if '„' in content:
        content = content.replace('„', '``')
        changes_made = True
    
    # " → '' (closing quote)
    if '"' in content:
        content = content.replace('"', "''")
        changes_made = True
    
    # " → '' (alternative closing quote)
    if '"' in content:
        content = content.replace('"', "''")
        changes_made = True
    
    # Step 2: Replace ASCII quotes "..." → ``...''
    # More careful approach: only replace pairs on the same line in text
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        # Skip lines that are likely in math or special commands
        if '\\[' in line or '\\]' in line or '\\begin{' in line or '\\end{' in line:
            new_lines.append(line)
            continue
        
        # Count quotes on this line
        quote_count = line.count('"')
        
        if quote_count >= 2 and quote_count % 2 == 0:
            # Try to replace pairs carefully
            new_line = line
            quote_positions = [m.start() for m in re.finditer('"', line)]
            
            # Process pairs from right to left to preserve positions
            for i in range(len(quote_positions) - 1, 0, -2):
                close_pos = quote_positions[i]
                open_pos = quote_positions[i-1]
                
                # Check if this looks like a quote pair (reasonable distance)
                if close_pos - open_pos < 200:  # Max quote length
                    # Replace closing quote
                    new_line = new_line[:close_pos] + "''" + new_line[close_pos+1:]
                    # Replace opening quote
                    new_line = new_line[:open_pos] + '``' + new_line[open_pos+1:]
                    changes_made = True
            
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # Write back if changes were made
    if changes_made and content != original_content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Normalized: {os.path.basename(filepath)}")
            return True
        except Exception as e:
            print(f"Error writing {filepath}: {e}", file=sys.stderr)
            return False
    else:
        print(f"  No changes: {os.path.basename(filepath)}")
        return False

def main():
    """Main function to process all German narrative files."""
    base_dir = '/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/narrative'
    
    # Directories to process
    directories = [
        os.path.join(base_dir, 'de_chapters'),
        os.path.join(base_dir, 'de_standalone')
    ]
    
    total_files = 0
    changed_files = 0
    
    for directory in directories:
        print(f"\nProcessing directory: {directory}")
        print("=" * 60)
        
        if not os.path.exists(directory):
            print(f"Warning: Directory does not exist: {directory}")
            continue
        
        # Find all German narrative files
        for filename in sorted(os.listdir(directory)):
            if filename.startswith('Kapitel_') and filename.endswith('_Narrative_De.tex'):
                filepath = os.path.join(directory, filename)
                total_files += 1
                
                if normalize_quotes_in_file(filepath):
                    changed_files += 1
    
    print("\n" + "=" * 60)
    print(f"Summary: {changed_files}/{total_files} files modified")
    print("=" * 60)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
