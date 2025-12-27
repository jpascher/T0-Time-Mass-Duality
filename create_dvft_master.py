#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create master DVFT document that includes all chapters
"""

import os
import re
import subprocess
from pathlib import Path

def extract_content_only(tex_file):
    """Extract only the content between \\begin{document} and \\end{document}"""
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find content between \begin{document} and \end{document}
    match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if match:
        body = match.group(1)
        # Remove \maketitle, \tableofcontents, \newpage at the beginning
        body = re.sub(r'^\s*\\maketitle\s*', '', body)
        body = re.sub(r'^\s*\\tableofcontents\s*', '', body)
        body = re.sub(r'^\s*\\newpage\s*', '', body, count=1)
        
        # Fix Unicode characters that cause issues
        body = body.replace('●', r'$\bullet$')
        body = body.replace('•', r'$\bullet$')
        body = body.replace('–', '--')
        body = body.replace('—', '---')
        body = body.replace('"', '``')
        body = body.replace('"', "''")
        body = body.replace(''', "`")
        body = body.replace(''', "'")
        
        # Fix mathematical Unicode characters (𝑥, 𝑦, etc.)
        # These are mathematical alphanumeric symbols that should be regular letters in math mode
        math_unicode_map = {
            '𝑥': 'x', '𝑦': 'y', '𝑧': 'z', '𝑡': 't', '𝑟': 'r', '𝑖': 'i',
            '𝜙': r'\phi', '𝜌': r'\rho', '𝜃': r'\theta', '𝜇': r'\mu',
            '𝛼': r'\alpha', '𝛽': r'\beta', '𝛾': r'\gamma', '𝛿': r'\delta',
            '𝜆': r'\lambda', '𝜋': r'\pi', '𝜎': r'\sigma', '𝜏': r'\tau',
            '𝜔': r'\omega', '𝜈': r'\nu', '𝜀': r'\epsilon', '𝜅': r'\kappa',
            'Φ': r'\Phi', 'Ψ': r'\Psi', 'Ω': r'\Omega', 'Δ': r'\Delta',
            'Γ': r'\Gamma', 'Λ': r'\Lambda', 'Σ': r'\Sigma', 'Θ': r'\Theta',
        }
        for unicode_char, latex_char in math_unicode_map.items():
            body = body.replace(unicode_char, latex_char)
        
        return body.strip()
    return ""

def create_content_files(chapters_dir, output_dir):
    """Create content-only versions of all chapters"""
    os.makedirs(output_dir, exist_ok=True)
    
    chapter_files = sorted([f for f in os.listdir(chapters_dir) if f.startswith('201_') and '_DVFT_' in f and f.endswith('.tex')])
    
    for chapter_file in chapter_files:
        input_path = os.path.join(chapters_dir, chapter_file)
        # Create content-only filename
        content_filename = chapter_file.replace('.tex', '_content.tex')
        output_path = os.path.join(output_dir, content_filename)
        
        content = extract_content_only(input_path)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created: {content_filename}")
    
    return chapter_files

def create_master_document(chapters_dir, content_dir, output_file):
    """Create master document that includes all chapters"""
    
    chapter_files = sorted([f for f in os.listdir(chapters_dir) if f.startswith('201_') and 'DVFT_' in f and f.endswith('.tex')])
    
    # Create master document
    master_content = r'''\documentclass[12pt,a4paper]{book}

\input{../T0_preamble_shared_De.tex}

\title{Angepasste Dynamische Vakuum-Feldtheorie (DVFT)\\
\large Vollständige Kapitelsammlung\\
Integriert in die T0 Zeit-Masse-Dualitätstheorie}

\author{Originalkonzept: Satish B. Thorwe\\
Vollständig Angepasst und Integriert: Johann Pascher}

\date{27. Dezember 2025}

\begin{document}

\maketitle

\tableofcontents

\newpage

\begin{t0box}[Über dieses Dokument]
Dieses Dokument vereint alle 44 Kapitel der angepassten Dynamischen Vakuum-Feldtheorie (DVFT), vollständig integriert in die T0 Zeit-Masse-Dualitätstheorie. 

Alle DVFT-Konzepte werden aus T0-Prinzipien abgeleitet:
\begin{itemize}
\item Vakuumfeld $\Phi(x)$ aus T0-Massenschwankungsfeld $\Delta m(x,t)$
\item Vakuumamplitude $\rho(x)$ entspricht $m(x,t) = 1/T(x,t)$
\item Vakuumphase $\theta(x)$ aus T0-Knoten-Rotationsdynamik  
\item Fundamentaler Parameter $\xi = \frac{4}{3} \times 10^{-4}$ durchgehend angewendet
\item Zeit-Masse-Dualität $T(x,t) \cdot m(x,t) = 1$ als Grundlage
\end{itemize}
\end{t0box}

\newpage

'''
    
    # Add includes for all chapters
    for chapter_file in chapter_files:
        content_filename = chapter_file.replace('.tex', '_content.tex')
        # Use relative path from content directory
        include_path = os.path.join('content_only', content_filename.replace('.tex', ''))
        master_content += f'\\include{{{include_path}}}\n'
        master_content += '\\newpage\n\n'
    
    master_content += r'''
\end{document}
'''
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(master_content)
    
    print(f"\nCreated master document: {output_file}")
    return len(chapter_files)

def compile_latex(tex_file, max_runs=3):
    """Compile LaTeX document with pdflatex"""
    tex_dir = os.path.dirname(tex_file)
    tex_basename = os.path.basename(tex_file)
    
    print(f"\nCompiling {tex_basename}...")
    
    for run in range(1, max_runs + 1):
        print(f"  Run {run}/{max_runs}...")
        try:
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', tex_basename],
                cwd=tex_dir,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode != 0:
                print(f"  Error in run {run}")
                # Save error log
                log_file = tex_file.replace('.tex', '.log')
                if os.path.exists(log_file):
                    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                        log_content = f.read()
                    # Extract error messages
                    errors = re.findall(r'! .*', log_content)
                    if errors:
                        print("  Errors found:")
                        for error in errors[:5]:  # Show first 5 errors
                            print(f"    {error}")
                return False
            else:
                print(f"  Run {run} completed successfully")
        except subprocess.TimeoutExpired:
            print(f"  Timeout in run {run}")
            return False
        except Exception as e:
            print(f"  Exception in run {run}: {e}")
            return False
    
    pdf_file = tex_file.replace('.tex', '.pdf')
    if os.path.exists(pdf_file):
        print(f"\n✓ PDF created successfully: {os.path.basename(pdf_file)}")
        return True
    else:
        print(f"\n✗ PDF not found: {os.path.basename(pdf_file)}")
        return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chapters_dir = os.path.join(base_dir, '2/tex-n/de_standalone')
    content_dir = os.path.join(chapters_dir, 'content_only')
    master_file = os.path.join(chapters_dir, 'DVFT_Complete_Master_De.tex')
    
    print("="*60)
    print("Creating DVFT Master Document")
    print("="*60)
    
    # Step 1: Create content-only files
    print("\nStep 1: Extracting content-only versions of chapters...")
    chapter_files = create_content_files(chapters_dir, content_dir)
    print(f"Extracted {len(chapter_files)} chapters")
    
    # Step 2: Create master document
    print("\nStep 2: Creating master document...")
    num_chapters = create_master_document(chapters_dir, content_dir, master_file)
    print(f"Master document includes {num_chapters} chapters")
    
    # Step 3: Compile
    print("\nStep 3: Compiling master document...")
    success = compile_latex(master_file, max_runs=3)
    
    if success:
        print("\n" + "="*60)
        print("SUCCESS: Master document compiled successfully!")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("FAILED: Compilation errors occurred")
        print("Check the .log file for details")
        print("="*60)
    
    return 0 if success else 1

if __name__ == '__main__':
    exit(main())
