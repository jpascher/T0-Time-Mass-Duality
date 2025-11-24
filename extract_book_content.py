#!/usr/bin/env python3
"""
Extract content from LaTeX files and create a universal preamble for book compilation.
This script:
1. Analyzes all .tex files in 2/tex/ to collect packages and custom commands
2. Creates a universal preamble with all necessary packages
3. Generates wrapper files that extract only document body content
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_preamble_and_body(tex_file):
    """Extract preamble and document body from a LaTeX file."""
    try:
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Try with latin-1 encoding if utf-8 fails
        try:
            with open(tex_file, 'r', encoding='latin-1') as f:
                content = f.read()
        except:
            print(f"Warning: Could not read {tex_file}, skipping")
            return "", "", ""
    
    # Find \begin{document} and \end{document}
    begin_match = re.search(r'\\begin\{document\}', content)
    end_match = re.search(r'\\end\{document\}', content)
    
    if not begin_match or not end_match:
        return None, None, None
    
    preamble = content[:begin_match.start()]
    body = content[begin_match.end():end_match.start()]
    
    # Clean body from any remaining preamble-like commands
    body = clean_body_content(body)
    
    return preamble, body, content

def clean_body_content(body):
    """Remove any preamble commands that might remain in body."""
    # Remove \documentclass
    body = re.sub(r'\\documentclass(\[[^\]]*\])?\{[^}]+\}', '', body)
    
    # Remove \usepackage
    body = re.sub(r'\\usepackage(\[[^\]]*\])?\{[^}]+\}', '', body)
    
    # Remove \newcommand, \renewcommand, \def
    body = re.sub(r'\\newcommand\{[^}]+\}(\[[^\]]*\])?\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\renewcommand\{[^}]+\}(\[[^\]]*\])?\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\def\\[^{]+\{[^}]*\}', '', body, flags=re.DOTALL)
    
    # Remove \definecolor
    body = re.sub(r'\\definecolor\{[^}]+\}\{[^}]+\}\{[^}]+\}', '', body)
    
    # Remove \newtheorem
    body = re.sub(r'\\newtheorem(\*)?(\[[^\]]*\])?\{[^}]+\}(\[[^\]]*\])?\{[^}]+\}', '', body)
    
    # Remove \DeclareMathOperator
    body = re.sub(r'\\DeclareMathOperator(\*)?(\[[^\]]*\])?\{[^}]+\}\{[^}]+\}', '', body)
    
    # Remove various setup commands
    body = re.sub(r'\\sisetup\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\pgfplotsset\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\hypersetup\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\geometry\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\usetikzlibrary\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\newunicodechar\{[^}]+\}\{[^}]+\}', '', body)
    
    # Remove \pagestyle and \fancyhf
    body = re.sub(r'\\pagestyle\{[^}]+\}', '', body)
    body = re.sub(r'\\fancyhf\[[^\]]*\]\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\fancyhead\[[^\]]*\]\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\fancyfoot\[[^\]]*\]\{[^}]*\}', '', body, flags=re.DOTALL)
    
    # Remove \author, \title, \date (but keep \maketitle)
    body = re.sub(r'\\author\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\title\{[^}]*\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\date\{[^}]*\}', '', body, flags=re.DOTALL)
    
    # Clean up excessive whitespace
    body = re.sub(r'\n\n\n+', '\n\n', body)
    body = body.strip()
    
    return body

def extract_packages(preamble):
    r"""Extract all \usepackage commands from preamble."""
    packages = []
    # Match \usepackage[options]{package} or \usepackage{package}
    pattern = r'\\usepackage(\[[^\]]*\])?\{([^}]+)\}'
    for match in re.finditer(pattern, preamble):
        options = match.group(1) if match.group(1) else ''
        package = match.group(2)
        packages.append((package, options))
    return packages

def extract_custom_commands(preamble):
    r"""Extract custom command definitions from preamble."""
    commands = []
    
    # Match various command definition patterns
    patterns = [
        r'\\newcommand\{[^}]+\}(\[[^\]]*\])?\{[^}]+\}',
        r'\\renewcommand\{[^}]+\}(\[[^\]]*\])?\{[^}]+\}',
        r'\\def[^{]+\{[^}]+\}',
        r'\\newunicodechar\{[^}]+\}\{[^}]+\}',
        r'\\definecolor\{[^}]+\}\{[^}]+\}\{[^}]+\}',
        r'\\newtheorem(\*)?(\[[^\]]*\])?\{[^}]+\}(\[[^\]]*\])?\{[^}]+\}',
        r'\\DeclareMathOperator(\*)?(\[[^\]]*\])?\{[^}]+\}\{[^}]+\}',
        r'\\sisetup\{[^}]+\}',
        r'\\pgfplotsset\{[^}]+\}',
        r'\\usetikzlibrary\{[^}]+\}',
        r'\\hypersetup\{[^}]+\}',
        r'\\geometry\{[^}]+\}',
    ]
    
    for pattern in patterns:
        for match in re.finditer(pattern, preamble, re.MULTILINE | re.DOTALL):
            commands.append(match.group(0))
    
    return commands

def analyze_all_tex_files(tex_dir):
    """Analyze all .tex files and collect packages and commands."""
    all_packages = defaultdict(set)
    all_commands = set()
    file_info = {}
    
    tex_files = list(Path(tex_dir).glob('*.tex'))
    print(f"Found {len(tex_files)} .tex files to analyze...")
    
    for tex_file in tex_files:
        print(f"Analyzing: {tex_file.name}")
        preamble, body, full_content = extract_preamble_and_body(tex_file)
        
        if preamble is None:
            print(f"  Warning: Could not find document structure in {tex_file.name}")
            continue
        
        # Extract packages
        packages = extract_packages(preamble)
        for pkg, opts in packages:
            all_packages[pkg].add(opts)
        
        # Extract custom commands
        commands = extract_custom_commands(preamble)
        all_commands.update(commands)
        
        file_info[tex_file.name] = {
            'preamble': preamble,
            'body': body,
            'full_content': full_content
        }
    
    return all_packages, all_commands, file_info

def create_universal_preamble(all_packages, all_commands):
    """Create a universal preamble with all necessary packages and commands."""
    preamble_lines = []
    
    # Document class
    preamble_lines.append(r"\documentclass[11pt,a4paper,openany]{book}")
    preamble_lines.append("")
    
    # Essential packages first
    essential_order = ['inputenc', 'fontenc', 'babel', 'geometry', 'lmodern']
    
    preamble_lines.append("% Essential packages")
    for pkg in essential_order:
        if pkg in all_packages:
            opts_set = all_packages[pkg]
            # Use the most comprehensive options
            if pkg == 'inputenc':
                preamble_lines.append(r"\usepackage[utf8]{inputenc}")
            elif pkg == 'fontenc':
                preamble_lines.append(r"\usepackage[T1]{fontenc}")
            elif pkg == 'babel':
                preamble_lines.append(r"\usepackage[english]{babel}")
            elif pkg == 'geometry':
                preamble_lines.append(r"\usepackage[a4paper,margin=2.5cm]{geometry}")
            elif pkg == 'lmodern':
                preamble_lines.append(r"\usepackage{lmodern}")
            del all_packages[pkg]
    
    preamble_lines.append("")
    preamble_lines.append("% Math and physics packages")
    math_packages = ['amsmath', 'amssymb', 'amsthm', 'mathtools', 'physics', 'siunitx']
    for pkg in math_packages:
        if pkg in all_packages:
            opts_set = all_packages[pkg]
            if opts_set and any(opts_set):
                opt = list(opts_set)[0]
                preamble_lines.append(f"\\usepackage{opt}{{{pkg}}}")
            else:
                preamble_lines.append(f"\\usepackage{{{pkg}}}")
            del all_packages[pkg]
    
    preamble_lines.append("")
    preamble_lines.append("% Graphics and tables")
    graphics_packages = ['graphicx', 'xcolor', 'tikz', 'pgfplots', 'tcolorbox', 'booktabs', 'array', 'longtable', 'float']
    for pkg in graphics_packages:
        if pkg in all_packages:
            opts_set = all_packages[pkg]
            if pkg == 'xcolor' and '[table' in str(opts_set):
                preamble_lines.append(r"\usepackage[table,xcdraw]{xcolor}")
            elif opts_set and any(opts_set):
                opt = list(opts_set)[0]
                preamble_lines.append(f"\\usepackage{opt}{{{pkg}}}")
            else:
                preamble_lines.append(f"\\usepackage{{{pkg}}}")
            del all_packages[pkg]
    
    preamble_lines.append("")
    preamble_lines.append("% Document formatting")
    format_packages = ['fancyhdr', 'tocloft', 'hyperref', 'cleveref', 'microtype', 'enumitem', 'newunicodechar']
    for pkg in format_packages:
        if pkg in all_packages:
            opts_set = all_packages[pkg]
            if opts_set and any(opts_set):
                opt = list(opts_set)[0]
                preamble_lines.append(f"\\usepackage{opt}{{{pkg}}}")
            else:
                preamble_lines.append(f"\\usepackage{{{pkg}}}")
            del all_packages[pkg]
    
    # Remaining packages
    if all_packages:
        preamble_lines.append("")
        preamble_lines.append("% Additional packages")
        for pkg in sorted(all_packages.keys()):
            opts_set = all_packages[pkg]
            if opts_set and any(opts_set):
                opt = list(opts_set)[0]
                preamble_lines.append(f"\\usepackage{opt}{{{pkg}}}")
            else:
                preamble_lines.append(f"\\usepackage{{{pkg}}}")
    
    # Add custom commands
    if all_commands:
        preamble_lines.append("")
        preamble_lines.append("% Custom commands and definitions")
        # Sort and deduplicate
        unique_commands = sorted(set(all_commands))
        for cmd in unique_commands:
            preamble_lines.append(cmd)
    
    # Add common settings
    preamble_lines.append("")
    preamble_lines.append("% Common settings")
    preamble_lines.append(r"\setlength{\headheight}{15pt}")
    preamble_lines.append(r"\pgfplotsset{compat=1.18}")
    preamble_lines.append(r"\usetikzlibrary{positioning,shapes,arrows,arrows.meta}")
    preamble_lines.append("")
    preamble_lines.append(r"% Hyperref setup")
    preamble_lines.append(r"\hypersetup{")
    preamble_lines.append(r"    colorlinks=true,")
    preamble_lines.append(r"    linkcolor=blue,")
    preamble_lines.append(r"    citecolor=blue,")
    preamble_lines.append(r"    urlcolor=blue")
    preamble_lines.append(r"}")
    preamble_lines.append("")
    
    return '\n'.join(preamble_lines)

def create_content_only_files(file_info, output_dir):
    """Create content-only files that only contain document bodies."""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    for filename, info in file_info.items():
        output_file = output_path / filename
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(info['body'])
        print(f"Created content-only file: {output_file.name}")

def main():
    # Directories
    tex_dir = Path('2/tex')
    output_dir = Path('book_content')
    
    print("="*70)
    print("T0 Theory Book Content Extractor")
    print("="*70)
    print()
    
    # Analyze all files
    all_packages, all_commands, file_info = analyze_all_tex_files(tex_dir)
    
    print()
    print(f"Total unique packages found: {len(all_packages)}")
    print(f"Total custom commands found: {len(all_commands)}")
    print(f"Total files processed: {len(file_info)}")
    print()
    
    # Create universal preamble
    print("Creating universal preamble...")
    universal_preamble = create_universal_preamble(all_packages, all_commands)
    
    # Save universal preamble
    with open('universal_preamble.tex', 'w', encoding='utf-8') as f:
        f.write(universal_preamble)
    print("Universal preamble saved to: universal_preamble.tex")
    print()
    
    # Create content-only files
    print("Creating content-only files...")
    create_content_only_files(file_info, output_dir)
    print()
    
    print("="*70)
    print("Processing complete!")
    print("="*70)
    print()
    print("Next steps:")
    print("1. Review universal_preamble.tex")
    print("2. Check content files in book_content/")
    print("3. Update T0_Book_En.tex to use universal preamble and content-only files")

if __name__ == '__main__':
    main()
