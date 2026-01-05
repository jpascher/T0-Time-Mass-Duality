#!/usr/bin/env python3
"""
Update master documents to use chapter files instead of content files.
Based on CHAPTER_FORMAT_INSTRUCTIONS.md
"""

import re
from pathlib import Path

def update_master_document(master_path, lang='de'):
    """Update a master document to use chapter files"""
    with open(master_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove merge conflict markers and old content file includes
    content = re.sub(r'<<<<<<< HEAD\n', '', content)
    content = re.sub(r'=======\n', '', content)
    content = re.sub(r'>>>>>>> copilot/narrative-reset\n', '', content)
    content = re.sub(r'% Kapitel 05 fehlt\n?', '', content)
    
    # Find where the chapter inputs start (after the Vorwort/Preface section)
    if lang == 'de':
        # Find the section after "Vorwort zur narrativen Fassung" and before "Nachwort"
        pattern = r'(\\textit\{Johann Pascher, Dezember 2025\}\s*\n\s*\\newpage\s*\n\s*)(% Kapitel 1-44.*?\n)(\\input\{Kapitel_\d+_Narrative_De_content\}.*?)(\\chapter\*\{Nachwort)'
        
        # Build the new chapter inputs
        chapter_inputs = ['% Kapitel 1-44: Using chapter files from de_chapters/\n']
        for i in range(1, 45):
            chapter_inputs.append(f'\\input{{de_chapters/Kapitel_{i:02d}_Narrative_De}}\n')
        chapter_inputs.append('\n')
        
        replacement = r'\1' + ''.join(chapter_inputs) + r'\4'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
    else:  # en
        # Similar for English
        pattern = r'(\\textit\{Johann Pascher, December 2025\}\s*\n\s*\\newpage\s*\n\s*)(% Chapters 1-44.*?\n)(\\input\{Kapitel_\d+_Narrative_En_content\}.*?)(\\chapter\*\{Afterword)'
        
        chapter_inputs = ['% Chapters 1-44: Using chapter files from en_chapters/\n']
        for i in range(1, 45):
            chapter_inputs.append(f'\\input{{en_chapters/Kapitel_{i:02d}_Narrative_En}}\n')
        chapter_inputs.append('\n')
        
        replacement = r'\1' + ''.join(chapter_inputs) + r'\4'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write back
    with open(master_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {master_path}")

def main():
    """Main update process"""
    base_dir = Path(__file__).parent
    
    # Update German master
    de_master = base_dir / "FFGFT_Narrative_Master_De.tex"
    update_master_document(de_master, 'de')
    
    # Update English master  
    en_master = base_dir / "FFGFT_Narrative_Master_En.tex"
    update_master_document(en_master, 'en')
    
    print("\nMaster documents updated successfully!")

if __name__ == '__main__':
    main()
