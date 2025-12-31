#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create master FFGFT document that includes all chapters
"""

import os
import re
import subprocess
from pathlib import Path

def fix_unicode_chars(text):
    """Comprehensive Unicode character fixing for LaTeX"""
    # Fix Unicode bullets and symbols
    text = text.replace('●', r'$\bullet$')
    text = text.replace('•', r'$\bullet$')
    text = text.replace('◦', r'$\circ$')
    text = text.replace('–', '--')
    text = text.replace('—', '---')
    text = text.replace('"', '``')
    text = text.replace('"', "''")
    text = text.replace(''', "`")
    text = text.replace(''', "'")
    text = text.replace('…', r'\ldots')
    text = text.replace('×', r'$\times$')
    text = text.replace('÷', r'$\div$')
    text = text.replace('≈', r'$\approx$')
    text = text.replace('≠', r'$\neq$')
    text = text.replace('≤', r'$\leq$')
    text = text.replace('≥', r'$\geq$')
    text = text.replace('∞', r'$\infty$')
    text = text.replace('±', r'$\pm$')
    text = text.replace('∓', r'$\mp$')
    text = text.replace('√', r'$\sqrt{}$')
    text = text.replace('∫', r'$\int$')
    text = text.replace('∑', r'$\sum$')
    text = text.replace('∏', r'$\prod$')
    text = text.replace('∂', r'$\partial$')
    text = text.replace('∇', r'$\nabla$')
    text = text.replace('⊗', r'$\otimes$')
    text = text.replace('⊕', r'$\oplus$')
    text = text.replace('∈', r'$\in$')
    text = text.replace('∉', r'$\notin$')
    text = text.replace('⊂', r'$\subset$')
    text = text.replace('⊃', r'$\supset$')
    text = text.replace('∪', r'$\cup$')
    text = text.replace('∩', r'$\cap$')
    text = text.replace('∀', r'$\forall$')
    text = text.replace('∃', r'$\exists$')
    text = text.replace('→', r'$\rightarrow$')
    text = text.replace('←', r'$\leftarrow$')
    text = text.replace('↔', r'$\leftrightarrow$')
    text = text.replace('⇒', r'$\Rightarrow$')
    text = text.replace('⇐', r'$\Leftarrow$')
    text = text.replace('⇔', r'$\Leftrightarrow$')
    
    # Fix mathematical Unicode characters (italic/bold variants)
    math_unicode_map = {
        '𝑎': 'a', '𝑏': 'b', '𝑐': 'c', '𝑑': 'd', '𝑒': 'e', '𝑓': 'f', '𝑔': 'g', '𝑕': 'h',
        '𝑥': 'x', '𝑦': 'y', '𝑧': 'z', '𝑡': 't', '𝑟': 'r', '𝑖': 'i', '𝑗': 'j', '𝑘': 'k',
        '𝑙': 'l', '𝑚': 'm', '𝑛': 'n', '𝑜': 'o', '𝑝': 'p', '𝑞': 'q', '𝑠': 's', '𝑢': 'u',
        '𝑣': 'v', '𝑤': 'w',
        '𝐴': 'A', '𝐵': 'B', '𝐶': 'C', '𝐷': 'D', '𝐸': 'E', '𝐹': 'F', '𝐺': 'G', '𝐻': 'H',
        '𝑋': 'X', '𝑌': 'Y', '𝑍': 'Z', '𝑇': 'T', '𝑅': 'R', '𝐼': 'I', '𝐽': 'J', '𝐾': 'K',
        '𝐿': 'L', '𝑀': 'M', '𝑁': 'N', '𝑂': 'O', '𝑃': 'P', '𝑄': 'Q', '𝑆': 'S', '𝑈': 'U',
        '𝑉': 'V', '𝑊': 'W',
        '𝜙': r'\phi', '𝜌': r'\rho', '𝜃': r'\theta', '𝜇': r'\mu',
        '𝛼': r'\alpha', '𝛽': r'\beta', '𝛾': r'\gamma', '𝛿': r'\delta',
        '𝜆': r'\lambda', '𝜋': r'\pi', '𝜎': r'\sigma', '𝜏': r'\tau',
        '𝜔': r'\omega', '𝜈': r'\nu', '𝜀': r'\epsilon', '𝜅': r'\kappa',
        '𝜉': r'\xi', '𝜂': r'\eta', '𝜁': r'\zeta', '𝜒': r'\chi', '𝜓': r'\psi',
        'Φ': r'\Phi', 'Ψ': r'\Psi', 'Ω': r'\Omega', 'Δ': r'\Delta',
        'Γ': r'\Gamma', 'Λ': r'\Lambda', 'Σ': r'\Sigma', 'Θ': r'\Theta',
        'Ξ': r'\Xi', 'Π': r'\Pi',
    }
    for unicode_char, latex_char in math_unicode_map.items():
        text = text.replace(unicode_char, latex_char)
    
    # Remove any remaining problematic Unicode characters by replacing with ?
    # This is a fallback for anything we missed
    text = text.encode('ascii', 'replace').decode('ascii')
    
    return text

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
        
        # Fix all Unicode characters
        body = fix_unicode_chars(body)
        
        return body.strip()
    return ""

def create_content_files(chapters_dir, output_dir):
    """Create content-only versions of all chapters"""
    os.makedirs(output_dir, exist_ok=True)
    
    chapter_files = sorted([f for f in os.listdir(chapters_dir) if f.startswith('201_') and '_FFGFT_' in f and f.endswith('.tex')])
    
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
    
    chapter_files = sorted([f for f in os.listdir(chapters_dir) if f.startswith('201_') and 'FFGFT_' in f and f.endswith('.tex')])
    
    # Create master document
    master_content = r'''\documentclass[12pt,a4paper]{book}

\input{../T0_preamble_shared_De.tex}

\title{Angepasste Fundamentale Fraktalgeometrische Feldtheorie (FFGFT)\\
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
Dieses Dokument vereint alle 44 Kapitel der angepassten Fundamentalen Fraktalgeometrischen Feldtheorie (FFGFT), vollständig integriert in die T0 Zeit-Masse-Dualitätstheorie. 

Alle FFGFT-Konzepte werden aus T0-Prinzipien abgeleitet:
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

def compile_latex(tex_file, max_runs=4):
    """Compile LaTeX document with pdflatex, iterating until successful"""
    tex_dir = os.path.dirname(tex_file)
    tex_basename = os.path.basename(tex_file)
    
    print(f"\nCompiling {tex_basename}...")
    print("=" * 60)
    
    for run in range(1, max_runs + 1):
        print(f"\nCompilation run {run}/{max_runs}...")
        try:
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', tex_basename],
                cwd=tex_dir,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            # Check if PDF was created
            pdf_file = tex_file.replace('.tex', '.pdf')
            
            if result.returncode != 0:
                print(f"  ⚠ Warning: pdflatex returned error code {result.returncode}")
                # Check log for actual errors
                log_file = tex_file.replace('.tex', '.log')
                if os.path.exists(log_file):
                    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                        log_content = f.read()
                    
                    # Look for fatal errors
                    if '! Emergency stop' in log_content or '! ==> Fatal error' in log_content:
                        print(f"  ✗ Fatal error in run {run}")
                        errors = re.findall(r'! .*', log_content)
                        if errors:
                            print("  First errors found:")
                            for error in errors[:10]:  # Show first 10 errors
                                print(f"    {error}")
                        return False
                    else:
                        print(f"  ℹ Non-fatal warnings, continuing...")
            
            if os.path.exists(pdf_file):
                file_size = os.path.getsize(pdf_file)
                if file_size > 1000:  # PDF should be at least 1KB
                    print(f"  ✓ Run {run} completed - PDF size: {file_size/1024:.1f} KB")
                else:
                    print(f"  ⚠ PDF created but suspiciously small: {file_size} bytes")
            else:
                print(f"  ⚠ No PDF generated yet in run {run}")
                
        except subprocess.TimeoutExpired:
            print(f"  ✗ Timeout in run {run}")
            return False
        except Exception as e:
            print(f"  ✗ Exception in run {run}: {e}")
            return False
    
    # Final check
    pdf_file = tex_file.replace('.tex', '.pdf')
    if os.path.exists(pdf_file):
        file_size = os.path.getsize(pdf_file)
        print("\n" + "=" * 60)
        print(f"✓ SUCCESS: PDF created successfully!")
        print(f"  File: {os.path.basename(pdf_file)}")
        print(f"  Size: {file_size/1024:.1f} KB")
        print("=" * 60)
        return True
    else:
        print("\n" + "=" * 60)
        print(f"✗ FAILED: PDF not created after {max_runs} runs")
        print("=" * 60)
        return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chapters_dir = os.path.join(base_dir, '2/tex-n/de_standalone')
    content_dir = os.path.join(chapters_dir, 'content_only')
    master_file = os.path.join(chapters_dir, 'FFGFT_Complete_Master_De.tex')
    
    print("="*70)
    print(" " * 15 + "FFGFT Master Document Creation & Compilation")
    print("="*70)
    
    # Step 1: Create content-only files
    print("\n[STEP 1/3] Extracting content-only versions of chapters...")
    print("-" * 70)
    chapter_files = create_content_files(chapters_dir, content_dir)
    print(f"✓ Extracted {len(chapter_files)} chapters successfully")
    
    # Step 2: Create master document
    print("\n[STEP 2/3] Creating master document...")
    print("-" * 70)
    num_chapters = create_master_document(chapters_dir, content_dir, master_file)
    print(f"✓ Master document created with {num_chapters} chapters")
    print(f"  Location: {os.path.relpath(master_file, base_dir)}")
    
    # Step 3: Compile
    print("\n[STEP 3/3] Compiling master document to PDF...")
    print("-" * 70)
    success = compile_latex(master_file, max_runs=4)
    
    print("\n" + "="*70)
    if success:
        pdf_file = master_file.replace('.tex', '.pdf')
        print("✓✓✓ SUCCESS ✓✓✓")
        print(f"\nMaster PDF created: {os.path.relpath(pdf_file, base_dir)}")
        print("\nAll 44 FFGFT chapters have been compiled into a single document!")
    else:
        print("✗✗✗ COMPILATION FAILED ✗✗✗")
        print("\nThe master document was created but PDF compilation had errors.")
        print("Check the .log file for details:")
        log_file = master_file.replace('.tex', '.log')
        print(f"  {os.path.relpath(log_file, base_dir)}")
    print("="*70)
    
    return 0 if success else 1

if __name__ == '__main__':
    exit(main())
