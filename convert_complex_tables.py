#!/usr/bin/env python3
"""
Convert complex tables to list format for KDP compliance.
Focus on tables with:
- More than 5 columns
- More than 30 lines
- Combination of many columns AND narrow widths
"""

import re
import os
from pathlib import Path

def extract_table_structure(tabular_content):
    """Extract column definition from tabular content."""
    # Find {columns} definition
    match = re.search(r'\{([^}]+)\}', tabular_content[:200])
    if match:
        col_def = match.group(1)
        # Count columns
        cols = col_def.count('l') + col_def.count('c') + col_def.count('r')
        cols += len(re.findall(r'p\{[^}]+\}', col_def))
        return cols, col_def
    return 0, ""

def is_table_complex(content, tabular_start):
    """Determine if a table is complex enough to need conversion."""
    # Find end of tabular
    brace_count = 1
    idx = tabular_start
    
    while idx < len(content) and brace_count > 0:
        if content[idx] == '{' and (idx == 0 or content[idx-1] != '\\'):
            brace_count += 1
        elif content[idx] == '}' and (idx == 0 or content[idx-1] != '\\'):
            brace_count -= 1
        idx += 1
    
    table_content = content[tabular_start:idx]
    
    # Get column count
    cols, col_def = extract_table_structure(table_content)
    
    # Count data lines (lines with & or \\)
    data_lines = sum(1 for line in table_content.split('\n') 
                     if ('&' in line or '\\\\' in line) and not line.strip().startswith('%'))
    
    # Check for narrow columns
    narrow_cols = re.findall(r'p\{([0-9.]+)cm\}', col_def)
    has_narrow = any(float(w) < 3.5 for w in narrow_cols) if narrow_cols else False
    
    # Criteria for "very complex" - needs conversion
    is_very_complex = (
        cols > 6 or  # More than 6 columns
        data_lines > 50 or  # More than 50 lines
        (cols > 5 and data_lines > 30) or  # More than 5 cols AND 30 lines
        (cols > 4 and has_narrow)  # More than 4 cols with narrow widths
    )
    
    return is_very_complex, cols, data_lines

def convert_table_to_list(table_content):
    """
    Convert a complex table to list format.
    This is a simplified conversion - manual review may be needed.
    """
    lines = table_content.split('\n')
    
    # Try to extract headers
    headers = []
    data_rows = []
    
    for line in lines:
        if '&' in line and not line.strip().startswith('%'):
            cells = [c.strip() for c in re.split(r'(?<!\\)&', line)]
            cells = [c.replace('\\\\', '').strip() for c in cells]
            
            if not headers and any('textbf' in c or 'hline' in line for c in cells):
                headers = cells
            elif cells and any(c for c in cells):
                data_rows.append(cells)
    
    # Build list format
    result = []
    result.append("\n% TABLE CONVERTED TO LIST FORMAT FOR KDP COMPLIANCE")
    result.append("% Original table was too complex (many columns/rows)")
    result.append("\n\\begin{itemize}")
    
    for i, row in enumerate(data_rows, 1):
        if not any(row):  # Skip empty rows
            continue
            
        # Create item for each row
        item_text = " -- ".join([c for c in row if c])
        result.append(f"    \\item {item_text}")
    
    result.append("\\end{itemize}\n")
    
    return '\n'.join(result)

def process_file(filepath):
    """Process a single file to convert complex tables."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        conversion_count = 0
        
        # Find all \begin{tabular} that are complex
        offset = 0
        new_content = content
        
        for match in re.finditer(r'\\begin\{tabular\}', content):
            tabular_start = match.end()
            is_complex, cols, lines = is_table_complex(content, tabular_start)
            
            if is_complex:
                # Find the complete table environment including \begin{table}...\end{table}
                # Look backwards for \begin{table} or start of tabular
                table_env_start = content.rfind('\\begin{table}', max(0, match.start() - 500), match.start())
                if table_env_start == -1:
                    table_env_start = match.start()
                
                # Find forward to \end{tabular}
                brace_count = 1
                idx = tabular_start
                while idx < len(content) and brace_count > 0:
                    if content[idx] == '{' and (idx == 0 or content[idx-1] != '\\'):
                        brace_count += 1
                    elif content[idx] == '}' and (idx == 0 or content[idx-1] != '\\'):
                        brace_count -= 1
                    idx += 1
                
                # Find \end{table} if it exists
                table_env_end = content.find('\\end{table}', idx, idx + 100)
                if table_env_end != -1:
                    table_env_end += len('\\end{table}')
                else:
                    table_env_end = idx
                
                # Extract the full table
                full_table = content[table_env_start:table_env_end]
                tabular_content = content[match.start():idx]
                
                # Convert to list format
                list_format = convert_table_to_list(tabular_content)
                
                # Replace in new_content with offset adjustment
                actual_start = table_env_start + offset
                actual_end = table_env_end + offset
                
                new_content = new_content[:actual_start] + list_format + new_content[actual_end:]
                offset += len(list_format) - (table_env_end - table_env_start)
                
                conversion_count += 1
                modified = True
                
                print(f"      Converted table: {cols} cols, {lines} lines")
        
        if modified:
            # Create backup
            backup_path = str(filepath) + '.BACKUP_TABLE_CONVERSION'
            if not os.path.exists(backup_path):
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            # Write modified content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True, conversion_count
        
        return False, 0
        
    except Exception as e:
        print(f"    ✗ ERROR: {e}")
        return False, 0

def main():
    repo_root = Path('/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality')
    
    directories = [
        (repo_root / '2/tex-n/de_chapters_new', 'German'),
        (repo_root / '2/tex-n/en_chapters_new', 'English')
    ]
    
    print("=" * 100)
    print("CONVERTING COMPLEX TABLES TO LIST FORMAT FOR KDP COMPLIANCE")
    print("=" * 100)
    print("\nConverting tables with:")
    print("  - More than 6 columns, OR")
    print("  - More than 50 lines, OR")
    print("  - More than 5 columns AND 30+ lines, OR")
    print("  - More than 4 columns with narrow widths (<3.5cm)")
    print("\n" + "=" * 100)
    
    total_files = 0
    total_modified = 0
    total_conversions = 0
    
    for directory, lang in directories:
        print(f"\n{lang} Chapters:")
        print("-" * 100)
        
        for tex_file in sorted(directory.glob('*_ch.tex')):
            if '.BACKUP' in str(tex_file):
                continue
                
            modified, conv_count = process_file(tex_file)
            total_files += 1
            
            if modified:
                total_modified += 1
                total_conversions += conv_count
                print(f"  ✓ {tex_file.name}: Converted {conv_count} table(s)")
    
    print("\n" + "=" * 100)
    print(f"SUMMARY:")
    print(f"  Processed: {total_files} files")
    print(f"  Modified: {total_modified} files")
    print(f"  Converted: {total_conversions} tables")
    print("=" * 100)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
