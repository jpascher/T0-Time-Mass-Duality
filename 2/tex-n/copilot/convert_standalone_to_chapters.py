#!/usr/bin/env python3
"""
Convert standalone LaTeX files to chapter files for inclusion in master documents.
Based on CHAPTER_FORMAT_INSTRUCTIONS.md
"""

import re
import os
from pathlib import Path

def extract_title_from_standalone(content):
  """Extract title text from \title{...} command with proper brace matching"""
  # Find the start of \title{
  match = re.search(r'\\title\{', content)
  if not match:
    return None
  
  start = match.end()
  brace_count = 1
  i = start
  
  # Match braces to find the end
  while i < len(content) and brace_count > 0:
    if content[i] == '{' and (i == 0 or content[i-1] != '\\'):
      brace_count += 1
    elif content[i] == '}' and (i == 0 or content[i-1] != '\\'):
      brace_count -= 1
    i += 1
  
  if brace_count == 0:
    title = content[start:i-1]
    
    # Clean up the title - remove \textbf, \large, \normalsize, etc.
    title = re.sub(r'\\textbf\{([^}]+)\}', r'\1', title)
    title = re.sub(r'\\large\s*', '', title)
    title = re.sub(r'\\normalsize\s*', '', title)
    title = re.sub(r'\\\\\s*', ' ', title) # Replace \\ with space
    title = title.strip()
    
    # Remove "Kapitel X:" or "Chapter X:" from beginning if present
    title = re.sub(r'^(Kapitel|Chapter)\s+\d+:\s*', '', title, flags=re.IGNORECASE)
    
    return title
  return None

def extract_content_from_standalone(content):
  """Extract content between \begin{document} and \end{document}"""
  # Find content between \begin{document} and \end{document}
  match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
  if match:
    doc_content = match.group(1).strip()
    
    # Remove \title, \author, \date, \maketitle more carefully
    # Remove \title{...} with proper brace matching
    doc_content = re.sub(r'\\title\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', '', doc_content, flags=re.DOTALL)
    doc_content = re.sub(r'\\author\{[^}]*\}', '', doc_content)
    doc_content = re.sub(r'\\date\{[^}]*\}', '', doc_content)
    doc_content = re.sub(r'\\maketitle', '', doc_content)
    
    # Convert \section*{Abstract} to \section{Abstract}
    doc_content = re.sub(r'\\section\*\{Abstract\}', r'\\section{Abstract}', doc_content)
    # Convert \section*{Zusammenfassung} to \section{Zusammenfassung}
    doc_content = re.sub(r'\\section\*\{Zusammenfassung\}', r'\\section{Zusammenfassung}', doc_content)
    
    # Clean up extra whitespace at the beginning
    doc_content = doc_content.lstrip()
    
    return doc_content
  return None

def convert_standalone_to_chapter(standalone_path, chapter_path, chapter_num, lang='de'):
  """Convert a standalone file to a chapter file"""
  if not os.path.exists(standalone_path):
    print(f"Warning: {standalone_path} does not exist, skipping")
    return False
  
  with open(standalone_path, 'r', encoding='utf-8') as f:
    content = f.read()
  
  # Extract title
  title = extract_title_from_standalone(content)
  if not title:
    print(f"Warning: Could not extract title from {standalone_path}")
    title = "Untitled"
  
  # Extract content
  doc_content = extract_content_from_standalone(content)
  if not doc_content:
    print(f"Warning: Could not extract content from {standalone_path}")
    return False
  
  # Build chapter file
  chapter_content = []
  
  # Add chapter heading
  if lang == 'de':
    chapter_content.append(f"\\chapter{{Kapitel {chapter_num}: {title}}}")
    chapter_content.append(f"\\label{{chap:{chapter_num}}}")
  else: # en
    chapter_content.append(f"\\chapter{{Chapter {chapter_num}: {title}}}")
    chapter_content.append(f"\\label{{chap:{chapter_num}-en}}")
  
  chapter_content.append("")
  chapter_content.append(doc_content)
  
  # Write chapter file
  with open(chapter_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(chapter_content))
  
  print(f"Created: {chapter_path}")
  return True

def main():
  """Main conversion process"""
  base_dir = Path(__file__).parent
  
  # Convert all 44 chapters
  success_count = {'de': 0, 'en': 0}
  
  for i in range(1, 45):
    chapter_num = f"{i:02d}"
    
    # German
    de_standalone = base_dir / f"de_standalone/Kapitel_{chapter_num}a_Narrative_De.tex"
    de_chapter = base_dir / f"de_chapters/Kapitel_{chapter_num}_Narrative_De.tex"
    if convert_standalone_to_chapter(de_standalone, de_chapter, chapter_num, 'de'):
      success_count['de'] += 1
    
    # English
    en_standalone = base_dir / f"en_standalone/Kapitel_{chapter_num}a_Narrative_En.tex"
    en_chapter = base_dir / f"en_chapters/Kapitel_{chapter_num}_Narrative_En.tex"
    if convert_standalone_to_chapter(en_standalone, en_chapter, chapter_num, 'en'):
      success_count['en'] += 1
  
  print(f"\nConversion complete:")
  print(f" German chapters: {success_count['de']}/44")
  print(f" English chapters: {success_count['en']}/44")

if __name__ == '__main__':
  main()

