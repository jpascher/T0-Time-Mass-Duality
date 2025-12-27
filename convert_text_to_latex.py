#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T0 Theory: Text to LaTeX Document Converter
============================================

This script converts text files to LaTeX documents following the T0 document style.
It handles dialog-based content, technical descriptions, and code blocks.

Usage:
    python3 convert_text_to_latex.py [--input-dir DIR] [--output-dir DIR]

Author: Johann Pascher / Copilot
Date: 2025
"""

import os
import re
import argparse
from pathlib import Path
from datetime import datetime


class TextToLatexConverter:
    """Converts text files to LaTeX documents with T0 styling."""
    
    def __init__(self, preamble_path="T0_preamble_shared_De.tex"):
        self.preamble_path = preamble_path
        self.next_number = self.get_next_document_number()
    
    def get_next_document_number(self, tex_dir="2/tex-n/de_standalone"):
        """Find the next available document number in the tex directory."""
        if not os.path.exists(tex_dir):
            return 200  # Start at 200 for converted text files
        
        max_num = 199  # Start searching from 200
        for filename in os.listdir(tex_dir):
            if filename.endswith('.tex'):
                match = re.match(r'^(\d+)_', filename)
                if match:
                    num = int(match.group(1))
                    max_num = max(max_num, num)
        
        return max_num + 1
    
    def escape_latex(self, text):
        """Escape special LaTeX characters."""
        # Dictionary of LaTeX special characters and their escapes
        replacements = {
            '\\': r'\textbackslash{}',
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}',
        }
        
        # Don't escape if it's already in a LaTeX command
        if text.strip().startswith('\\'):
            return text
        
        result = text
        for char, escape in replacements.items():
            if char != '\\':  # Handle backslash separately
                result = result.replace(char, escape)
        
        return result
    
    def detect_structure(self, content):
        """Detect the structure of the content (dialog, technical, code, etc.)."""
        # Check for dialog patterns
        dialog_patterns = [
            r'^[A-ZÄÖÜ][a-zäöüß]+:',  # Name: at start of line
            r'^\*\*[^*]+\*\*:',  # **Name**: markdown bold
        ]
        
        for pattern in dialog_patterns:
            if re.search(pattern, content, re.MULTILINE):
                return 'dialog'
        
        # Check for code blocks
        if '```' in content:
            return 'code'
        
        # Check for mathematical content
        if re.search(r'\\\[|\\\(|\\begin\{equation\}', content):
            return 'mathematical'
        
        return 'technical'
    
    def convert_dialog_to_latex(self, content):
        """Convert dialog-based content to LaTeX format."""
        lines = content.split('\n')
        latex_content = []
        in_paragraph = False
        
        for line in lines:
            line = line.strip()
            
            if not line:
                if in_paragraph:
                    latex_content.append('')
                in_paragraph = False
                continue
            
            # Match dialog patterns
            # Pattern 1: Name: text
            match1 = re.match(r'^([A-ZÄÖÜ][a-zäöüß]+):\s*(.+)$', line)
            # Pattern 2: **Name**: text
            match2 = re.match(r'^\*\*([^*]+)\*\*:\s*(.+)$', line)
            
            if match1:
                speaker = match1.group(1)
                text = match1.group(2)
                latex_content.append(f'\\textbf{{{speaker}:}} {text}')
                latex_content.append('')
                in_paragraph = False
            elif match2:
                speaker = match2.group(1)
                text = match2.group(2)
                latex_content.append(f'\\textbf{{{speaker}:}} {text}')
                latex_content.append('')
                in_paragraph = False
            elif line.startswith('#'):
                # Markdown headers
                level = len(re.match(r'^#+', line).group(0))
                title = line.lstrip('#').strip()
                if level == 1:
                    latex_content.append(f'\\section{{{title}}}')
                elif level == 2:
                    latex_content.append(f'\\subsection{{{title}}}')
                elif level == 3:
                    latex_content.append(f'\\subsubsection{{{title}}}')
                else:
                    latex_content.append(f'\\paragraph{{{title}}}')
                latex_content.append('')
                in_paragraph = False
            else:
                # Regular text
                latex_content.append(line)
                in_paragraph = True
        
        return '\n'.join(latex_content)
    
    def convert_code_to_latex(self, content):
        """Convert content with code blocks to LaTeX format."""
        # Split by code blocks
        parts = re.split(r'```(\w*)\n(.*?)```', content, flags=re.DOTALL)
        latex_content = []
        
        for i, part in enumerate(parts):
            if i % 3 == 0:
                # Regular text
                if part.strip():
                    latex_content.append(self.convert_technical_to_latex(part))
            elif i % 3 == 1:
                # Language identifier (skip)
                pass
            else:
                # Code content
                language = parts[i-1] if parts[i-1] else 'text'
                latex_content.append(f'\\begin{{lstlisting}}[language={language}]')
                latex_content.append(part)
                latex_content.append('\\end{lstlisting}')
        
        return '\n'.join(latex_content)
    
    def convert_technical_to_latex(self, content):
        """Convert technical content to LaTeX format."""
        lines = content.split('\n')
        latex_content = []
        in_list = False
        list_type = None
        in_equation = False
        in_math_block = False
        
        for line in lines:
            original_line = line
            line_stripped = line.strip()
            
            # Check if we're in a math block
            if line_stripped.startswith('\\['):
                in_math_block = True
                if in_list:
                    latex_content.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                latex_content.append(line_stripped)
                continue
            
            if in_math_block:
                latex_content.append(line_stripped)
                if line_stripped.endswith('\\]'):
                    in_math_block = False
                continue
            
            if not line_stripped:
                if in_list:
                    latex_content.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                latex_content.append('')
                continue
            
            # Headers
            if line_stripped.startswith('###'):
                if in_list:
                    latex_content.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                title = line_stripped.lstrip('#').strip()
                latex_content.append(f'\\subsubsection{{{title}}}')
            elif line_stripped.startswith('##'):
                if in_list:
                    latex_content.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                title = line_stripped.lstrip('#').strip()
                latex_content.append(f'\\subsection{{{title}}}')
            elif line_stripped.startswith('#'):
                if in_list:
                    latex_content.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                title = line_stripped.lstrip('#').strip()
                latex_content.append(f'\\section{{{title}}}')
            # Lists
            elif line_stripped.startswith('- ') or line_stripped.startswith('* '):
                if not in_list or list_type != 'itemize':
                    if in_list:
                        latex_content.append(f'\\end{{{list_type}}}')
                    latex_content.append('\\begin{itemize}')
                    in_list = True
                    list_type = 'itemize'
                item_text = line_stripped[2:].strip()
                # Convert bold text in item
                item_text = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', item_text)
                latex_content.append(f'  \\item {item_text}')
            elif re.match(r'^\d+\.', line_stripped):
                if not in_list or list_type != 'enumerate':
                    if in_list:
                        latex_content.append(f'\\end{{{list_type}}}')
                    latex_content.append('\\begin{enumerate}')
                    in_list = True
                    list_type = 'enumerate'
                item_text = re.sub(r'^\d+\.\s*', '', line_stripped)
                # Convert bold text in item
                item_text = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', item_text)
                latex_content.append(f'  \\item {item_text}')
            # Math blocks
            elif line_stripped.startswith('\\begin{equation'):
                if in_list:
                    latex_content.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                in_equation = True
                latex_content.append(line_stripped)
            elif '\\end{equation' in line_stripped:
                latex_content.append(line_stripped)
                in_equation = False
            # Bold text **text**
            elif '**' in line_stripped and not in_equation:
                if in_list and not line_stripped.startswith(' ') and not line_stripped.startswith('\t'):
                    latex_content.append(f'\\end{{{list_type}}}')
                    in_list = False
                    list_type = None
                line_converted = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', line_stripped)
                latex_content.append(line_converted)
            else:
                # Regular line
                if in_list and not line_stripped.startswith(' ') and not line_stripped.startswith('\t'):
                    # Check if it's a continuation or new paragraph
                    if line_stripped and not line_stripped[0].isupper() or len(line_stripped) < 20:
                        # Likely continuation
                        latex_content.append(line_stripped)
                    else:
                        latex_content.append(f'\\end{{{list_type}}}')
                        in_list = False
                        list_type = None
                        latex_content.append(line_stripped)
                else:
                    latex_content.append(line_stripped)
        
        if in_list:
            latex_content.append(f'\\end{{{list_type}}}')
        
        return '\n'.join(latex_content)
    
    def extract_title_from_content(self, content):
        """Extract a title from the content."""
        lines = content.split('\n')
        
        for line in lines[:10]:  # Check first 10 lines
            line = line.strip()
            # Check for markdown headers
            if line.startswith('#'):
                return line.lstrip('#').strip()
            # Check for dialog start
            match = re.match(r'^([A-ZÄÖÜ][a-zäöüß\s]+):', line)
            if match:
                return f"Dialog: {match.group(1)}"
        
        # Use first non-empty line
        for line in lines[:5]:
            line = line.strip()
            if line and len(line) > 10:
                # Take first 60 characters
                title = line[:60]
                if len(line) > 60:
                    title += "..."
                return title
        
        return "Untitled Document"
    
    def convert_file(self, input_path, output_dir):
        """Convert a single text file to LaTeX."""
        print(f"Converting: {input_path}")
        
        # Read input file
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"  Error reading file: {e}")
            return None
        
        # Extract title
        title = self.extract_title_from_content(content)
        
        # Generate filename
        basename = os.path.splitext(os.path.basename(input_path))[0]
        # Clean filename
        basename = re.sub(r'[^\w\-äöüÄÖÜß]', '_', basename)
        output_filename = f"{self.next_number:03d}_{basename}_De.tex"
        output_path = os.path.join(output_dir, output_filename)
        
        # Detect content structure
        structure_type = self.detect_structure(content)
        print(f"  Detected structure: {structure_type}")
        
        # Convert content
        if structure_type == 'dialog':
            latex_body = self.convert_dialog_to_latex(content)
        elif structure_type == 'code':
            latex_body = self.convert_code_to_latex(content)
        else:
            latex_body = self.convert_technical_to_latex(content)
        
        # Create standalone LaTeX document
        latex_doc = f'''\\documentclass[12pt,a4paper]{{article}}
\\input{{{self.preamble_path}}}

\\title{{{title}}}
\\author{{Johann Pascher}}
\\date{{{datetime.now().year}}}

\\begin{{document}}
\\maketitle
\\tableofcontents
\\newpage

{latex_body}

\\end{{document}}
'''
        
        # Write output file
        try:
            os.makedirs(output_dir, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(latex_doc)
            print(f"  Created: {output_filename}")
            self.next_number += 1
            return output_path
        except Exception as e:
            print(f"  Error writing file: {e}")
            return None


def main():
    parser = argparse.ArgumentParser(
        description='Convert text files to LaTeX documents with T0 styling'
    )
    parser.add_argument(
        '--input-dir',
        default='.',
        help='Directory containing text files to convert (default: current directory)'
    )
    parser.add_argument(
        '--output-dir',
        default='2/tex-n/de_standalone',
        help='Output directory for LaTeX files (default: 2/tex-n/de_standalone)'
    )
    parser.add_argument(
        '--preamble',
        default='T0_preamble_shared_De.tex',
        help='Path to preamble file (default: T0_preamble_shared_De.tex)'
    )
    parser.add_argument(
        '--files',
        nargs='+',
        help='Specific files to convert (default: all .txt files)'
    )
    
    args = parser.parse_args()
    
    # Initialize converter
    converter = TextToLatexConverter(preamble_path=args.preamble)
    
    # Find text files to convert
    if args.files:
        text_files = args.files
    else:
        text_files = []
        for filename in os.listdir(args.input_dir):
            if filename.endswith('.txt') and not filename.startswith('.'):
                # Skip log files
                if 'output' in filename.lower() or 'error' in filename.lower():
                    continue
                text_files.append(os.path.join(args.input_dir, filename))
    
    if not text_files:
        print("No text files found to convert.")
        return
    
    print(f"Found {len(text_files)} text file(s) to convert.")
    print(f"Output directory: {args.output_dir}")
    print(f"Starting conversion...\n")
    
    # Convert each file
    converted = []
    for text_file in text_files:
        result = converter.convert_file(text_file, args.output_dir)
        if result:
            converted.append(result)
    
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Converted {len(converted)} file(s) successfully.")
    if converted:
        print(f"\nGenerated files:")
        for filepath in converted:
            print(f"  - {os.path.basename(filepath)}")


if __name__ == '__main__':
    main()
