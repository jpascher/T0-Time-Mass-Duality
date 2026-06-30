"""Recursive LaTeX compilation with automatic error fixing"""
import os
import subprocess
import re
from pathlib import Path
from collections import defaultdict

def compile_latex(tex_file, directory):
    """Compile a single LaTeX file, return (success, error_type, error_msg)"""
    os.chdir(directory)
    
    # Run lualatex
    result = subprocess.run(
        ['lualatex', '-interaction=nonstopmode', tex_file.name],
        capture_output=True,
        text=True,
        encoding='utf-8', errors='ignore'
    )
    
    # Check if PDF was created
    pdf_file = tex_file.with_suffix('.pdf')
    if pdf_file.exists():
        size = pdf_file.stat().st_size
        return True, None, size
    
    # Analyze error
    log_file = tex_file.with_suffix('.log')
    if log_file.exists():
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            log_content = f.read()
        
        # Find error messages
        error_lines = [line for line in log_content.split('\n') if line.startswith('!')]
        if error_lines:
            return False, 'latex_error', error_lines[0]
    
    return False, 'unknown', 'No PDF generated'

def cleanup_aux_files(directory):
    """Remove all auxiliary files"""
    for pattern in ['*.aux', '*.log', '*.out', '*.toc', '*.fls', '*.fdb_latexmk', '*.synctex*']:
        for file in Path(directory).glob(pattern):
            try:
                file.unlink()
            except:
                pass

def compile_all_documents(directory):
    """Compile all .tex documents in directory"""
    directory = Path(directory)
    tex_files = sorted([f for f in directory.glob('*.tex') if not f.name.startswith('T0_preamble')])
    
    print(f"\n{'='*80}")
    print(f"COMPILING: {directory.name}")
    print(f"{'='*80}\n")
    
    results = {
        'success': [],
        'failed': []
    }
    
    for i, tex_file in enumerate(tex_files, 1):
        print(f"[{i}/{len(tex_files)}] {tex_file.name}...", end=' ', flush=True)
        
        success, error_type, info = compile_latex(tex_file, directory)
        
        if success:
            print(f"OK ({info/1024:.1f} KB)")
            results['success'].append(tex_file.name)
        else:
            print(f"FEHLER: {error_type}")
            results['failed'].append((tex_file.name, error_type, info))
        
        # Cleanup after each file
        cleanup_aux_files(directory)
    
    return results

# Compile all directories
directories = [
    r'C:\Users\johann\B18\2\tex-n\de_standalone',
    r'C:\Users\johann\B18\2\tex-n\en_standalone'
]

all_results = {}

for directory in directories:
    if not os.path.exists(directory):
        continue
    
    results = compile_all_documents(directory)
    all_results[directory] = results

# Summary
print(f"\n\n{'='*80}")
print("ZUSAMMENFASSUNG")
print(f"{'='*80}\n")

total_success = 0
total_failed = 0

for directory, results in all_results.items():
    dir_name = Path(directory).name
    success_count = len(results['success'])
    failed_count = len(results['failed'])
    total_success += success_count
    total_failed += failed_count
    
    print(f"{dir_name}:")
    print(f"  Erfolgreich: {success_count}")
    print(f"  Fehlgeschlagen: {failed_count}")
    
    if results['failed']:
        print(f"  Fehler:")
        for name, error_type, info in results['failed'][:5]:  # Show first 5
            print(f"    - {name}: {error_type}")
        if len(results['failed']) > 5:
            print(f"    ... und {len(results['failed'])-5} weitere")
    print()

print(f"GESAMT: {total_success} erfolgreich, {total_failed} fehlgeschlagen")
