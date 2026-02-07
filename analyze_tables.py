#!/usr/bin/env python3
"""
Analyze LaTeX files to find tables that might need conversion to list format.
Focus on:
1. Tables with many columns (>4 columns)
2. Tables with long content (>30 lines)
3. Tables with narrow column definitions (p{2cm}, p{3cm}, etc.)
"""

import re
from pathlib import Path

def analyze_table(content, start_pos):
  """Analyze a single table and return metrics."""
  # Find the end of the table
  brace_count = 1
  idx = start_pos
  
  while idx < len(content) and brace_count > 0:
    if content[idx] == '{' and (idx == 0 or content[idx-1] != '\\'):
      brace_count += 1
    elif content[idx] == '}' and (idx == 0 or content[idx-1] != '\\'):
      brace_count -= 1
    idx += 1
  
  table_content = content[start_pos:idx]
  
  # Count columns (look for & separators in first data row)
  lines = table_content.split('\n')
  max_cols = 0
  for line in lines:
    if '&' in line and not line.strip().startswith('%'):
      cols = line.count('&') + 1
      max_cols = max(max_cols, cols)
  
  # Count lines
  data_lines = len([l for l in lines if '&' in l or '\\\\' in l])
  
  # Check for narrow columns
  narrow_cols = re.findall(r'p\{([0-9.]+)cm\}', table_content[:200])
  has_narrow = any(float(w) < 4 for w in narrow_cols)
  
  return {
    'columns': max_cols,
    'lines': data_lines,
    'length': len(table_content),
    'narrow_columns': has_narrow,
    'narrow_widths': narrow_cols
  }

def analyze_file(filepath):
  """Analyze a file for problematic tables."""
  try:
    with open(filepath, 'r', encoding='utf-8') as f:
      content = f.read()
    
    problems = []
    
    # Find all \begin{tabular} instances
    for match in re.finditer(r'\\begin\{tabular\}', content):
      start_pos = match.end()
      metrics = analyze_table(content, start_pos)
      
      # Flag as problematic if:
      # - More than 4 columns
      # - More than 20 data lines
      # - Has narrow columns (< 4cm)
      is_problematic = (
        metrics['columns'] > 4 or
        metrics['lines'] > 20 or
        metrics['narrow_columns']
      )
      
      if is_problematic:
        # Get surrounding context for identification
        line_num = content[:match.start()].count('\n') + 1
        context_start = max(0, match.start() - 200)
        context = content[context_start:match.start()]
        
        # Try to find section/subsection
        section_match = re.search(r'\\(?:sub)?section\{([^}]+)\}', context)
        section = section_match.group(1) if section_match else "Unknown"
        
        problems.append({
          'line': line_num,
          'section': section,
          'metrics': metrics
        })
    
    return problems
    
  except Exception as e:
    return []

def main():
  repo_root = Path('/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality')
  
  # Focus on the books that were rejected by KDP
  # Teil1_De: Pages 2-10
  # Teil2_De: Pages 8, 11-12, 179, 183, 185, 366-370
  # Teil3_De: Pages affected
  # Teil2_En: Pages 3-8, 13-14, 197
  
  print("=" * 100)
  print("ANALYZING TABLES FOR KDP COMPLIANCE")
  print("=" * 100)
  print("\nCriteria for problematic tables:")
  print(" - More than 4 columns")
  print(" - More than 20 data lines")
  print(" - Narrow columns (< 4cm width)")
  print("\n" + "=" * 100)
  
  directories = [
    (repo_root / '2/tex-n/de_chapters_new', 'German'),
    (repo_root / '2/tex-n/en_chapters_new', 'English')
  ]
  
  total_files = 0
  total_problems = 0
  
  for directory, lang in directories:
    print(f"\n{lang} Chapters:")
    print("-" * 100)
    
    for tex_file in sorted(directory.glob('*_ch.tex')):
      problems = analyze_file(tex_file)
      if problems:
        total_files += 1
        total_problems += len(problems)
        print(f"\n📄 {tex_file.name} - {len(problems)} problematic table(s)")
        for i, prob in enumerate(problems, 1):
          print(f"  [{i}] Line {prob['line']}, Section: {prob['section'][:60]}")
          print(f"    Columns: {prob['metrics']['columns']}, Lines: {prob['metrics']['lines']}")
          if prob['metrics']['narrow_columns']:
            print(f"    Narrow cols: {', '.join(prob['metrics']['narrow_widths'])}cm")
  
  print("\n" + "=" * 100)
  print(f"SUMMARY: Found {total_problems} problematic tables in {total_files} files")
  print("=" * 100)

if __name__ == '__main__':
  main()

