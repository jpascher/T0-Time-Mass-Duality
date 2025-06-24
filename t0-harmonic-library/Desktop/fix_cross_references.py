#!/usr/bin/env python3
"""
Script to fix cross-references in HTML files generated from LaTeX.
This script:
1. Parses LaTeX files to identify labels and their corresponding numbers/text
2. Parses HTML files to find broken references (???)
3. Replaces broken references with the correct text from the LaTeX files
4. Creates backups of all files before modification

Usage:
    python fix_cross_references.py [directory]

If directory is not specified, it will use the current directory.
"""

import os
import sys
import re
import shutil
from pathlib import Path
from collections import defaultdict

def extract_labels_from_latex(tex_file):
    """
    Extract all labels and their corresponding numbers/text from a LaTeX file.
    Returns a dictionary mapping label names to their values.
    """
    try:
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Dictionary to store labels
        labels = {}
        
        # Extract section numbers and their labels
        section_pattern = r'\\(section|subsection|subsubsection|chapter|part){([^}]*)}\s*\\label{([^}]*)}'
        for match in re.finditer(section_pattern, content):
            section_type, section_text, label = match.groups()
            # For now we'll store the section text - in a more complex version we'd compute the number
            labels[label] = section_text
        
        # Extract equation labels
        equation_pattern = r'\\begin{equation}\\label{([^}]*)}(.*?)\\end{equation}'
        for match in re.finditer(equation_pattern, content, re.DOTALL):
            label, equation = match.groups()
            # Store the equation number (we'd need to compute this based on LaTeX rules)
            # For now just store a placeholder
            labels[label] = f"Equation ({label})"
        
        # Extract figure labels
        figure_pattern = r'\\begin{figure}.*?\\caption{(.*?)}\\label{([^}]*)}.*?\\end{figure}'
        for match in re.finditer(figure_pattern, content, re.DOTALL):
            caption, label = match.groups()
            labels[label] = f"Figure: {caption}"
        
        # Extract table labels
        table_pattern = r'\\begin{table}.*?\\caption{(.*?)}\\label{([^}]*)}.*?\\end{table}'
        for match in re.finditer(table_pattern, content, re.DOTALL):
            caption, label = match.groups()
            labels[label] = f"Table: {caption}"
        
        # Add patterns for other types of references as needed
        
        return labels
    
    except Exception as e:
        print(f"Error processing LaTeX file {tex_file}: {e}")
        return {}

def fix_references_in_html(html_file, label_map):
    """
    Fix broken references in an HTML file using the label map.
    """
    try:
        # Read the original content
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create a backup of the original file
        backup_path = f"{html_file}.bak"
        shutil.copy2(html_file, backup_path)
        
        # Find broken references
        ref_pattern = r'\\ref{([^}]*)}'
        
        def replace_ref(match):
            label = match.group(1)
            if label in label_map:
                return label_map[label]
            else:
                return f"???({label})"
        
        # Replace broken references
        modified_content = re.sub(ref_pattern, replace_ref, content)
        
        # Handle \eqref specially (for equation references)
        eqref_pattern = r'\\eqref{([^}]*)}'
        def replace_eqref(match):
            label = match.group(1)
            if label in label_map:
                return f"({label_map[label]})"
            else:
                return f"???({label})"
        
        modified_content = re.sub(eqref_pattern, replace_eqref, modified_content)
        
        # Also look for ??? in the text which might be failed references
        question_pattern = r'\?\?\?'
        modified_content = re.sub(question_pattern, "[Reference]", modified_content)
        
        # Write the modified content back to the file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        print(f"✅ Fixed references in {html_file}")
        return True
    
    except Exception as e:
        print(f"❌ Error processing HTML file {html_file}: {e}")
        return False

def build_label_map(directory):
    """
    Build a map of all labels in all LaTeX files in the directory.
    """
    directory_path = Path(directory)
    
    # Global label map
    label_map = {}
    
    # First pass: collect all labels from all LaTeX files
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.tex'):
                tex_file = os.path.join(root, file)
                file_labels = extract_labels_from_latex(tex_file)
                # Add to global map, possibly overwriting earlier definitions
                label_map.update(file_labels)
    
    return label_map

def process_html_files(directory, label_map):
    """
    Process all HTML files in the directory and its subdirectories.
    """
    directory_path = Path(directory)
    
    # Counters for statistics
    total_files = 0
    modified_files = 0
    
    # Process all HTML files
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.html'):
                html_file = os.path.join(root, file)
                total_files += 1
                if fix_references_in_html(html_file, label_map):
                    modified_files += 1
    
    # Print final statistics
    print(f"\nProcessed {total_files} HTML files")
    print(f"Fixed references in {modified_files} files")

def find_tex_html_pairs(directory):
    """
    Find pairs of .tex and .html files that might correspond to each other.
    This can be used for more sophisticated matching.
    """
    directory_path = Path(directory)
    
    tex_files = []
    html_files = []
    
    # Find all .tex and .html files
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.tex'):
                tex_files.append(os.path.join(root, file))
            elif file.lower().endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    # Try to match them based on name similarity
    pairs = []
    for tex_file in tex_files:
        tex_name = os.path.splitext(os.path.basename(tex_file))[0]
        
        # Try various possible matching patterns
        possible_html_names = [
            f"{tex_name}.html",
            f"{tex_name}En.html",
            f"{tex_name}_En.html"
        ]
        
        for html_file in html_files:
            html_basename = os.path.basename(html_file)
            if html_basename in possible_html_names:
                pairs.append((tex_file, html_file))
                break
    
    return pairs

def main():
    """Main function that processes command line arguments and runs the script."""
    # Use the first command line argument as the directory, or current directory if not specified
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)
    
    print(f"Processing LaTeX and HTML files in {os.path.abspath(directory)}")
    
    # Find matching .tex and .html pairs for more sophisticated processing
    pairs = find_tex_html_pairs(directory)
    print(f"Found {len(pairs)} matching .tex and .html file pairs")
    
    # Build a global label map from all LaTeX files
    print("Building label map from LaTeX files...")
    label_map = build_label_map(directory)
    print(f"Found {len(label_map)} unique labels")
    
    # Process all HTML files
    print("Fixing references in HTML files...")
    process_html_files(directory, label_map)

if __name__ == "__main__":
    main()