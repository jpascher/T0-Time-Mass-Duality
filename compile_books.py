#!/usr/bin/env python3
import subprocess
import os
import sys

os.chdir('/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality')

books = [
    '2/tex-n/completed/Teil1a_De.tex',
    '2/tex-n/completed/Teil1a_En.tex',
    '2/tex-n/completed/Teil1.ebook_De.tex',
    '2/tex-n/completed/Teil1.ebook_En.tex',
    '2/tex-n/completed/Teil2_De.tex',
    '2/tex-n/completed/Teil2_En.tex',
    '2/tex-n/completed/Teil2.ebook_De.tex',
    '2/tex-n/completed/Teil2.ebook_En.tex',
    '2/tex-n/completed/Teil3a_De.tex',
    '2/tex-n/completed/Teil3a_En.tex',
    '2/tex-n/completed/Teil3.ebook_De.tex',
    '2/tex-n/completed/Teil3.ebook_En.tex',
    '2/tex-n/completed/T0_Anwendungen_De.tex',
    '2/tex-n/completed/T0_Anwendungen_En.tex',
]

compiled = []
failed = []

for book in books:
    if not os.path.exists(book):
        print(f"SKIP: {book} (not found)")
        continue
    
    print(f"\n{'='*80}")
    print(f"Compiling: {book}")
    print('='*80)
    
    basename = os.path.basename(book).replace('.tex', '')
    working_dir = os.path.dirname(book)
    
    # Compile with lualatex
    cmd = ['lualatex', '-interaction=nonstopmode', '-halt-on-error', basename + '.tex']
    
    try:
        result = subprocess.run(cmd, cwd=working_dir, timeout=600, 
                              capture_output=True, text=True)
        
        # Check if PDF was created
        pdf_in_dir = os.path.join(working_dir, basename + '.pdf')
        pdf_target = os.path.join('2/pdf', basename + '.pdf')
        
        if os.path.exists(pdf_in_dir):
            # Move PDF to target directory
            import shutil
            shutil.copy2(pdf_in_dir, pdf_target)
            compiled.append(book)
            print(f"✓ SUCCESS: {basename}.pdf created")
        else:
            failed.append(book)
            print(f"✗ FAILED: {basename}.pdf not created")
            # Print last 30 lines of output for debugging
            print("\nLast lines of output:")
            print('\n'.join(result.stdout.split('\n')[-30:]))
            
    except subprocess.TimeoutExpired:
        failed.append(book)
        print(f"✗ TIMEOUT: {book}")
    except Exception as e:
        failed.append(book)
        print(f"✗ ERROR: {book} - {e}")

print(f"\n{'='*80}")
print(f"COMPILATION SUMMARY")
print('='*80)
print(f"Total books: {len(books)}")
print(f"Compiled successfully: {len(compiled)}")
print(f"Failed: {len(failed)}")

if compiled:
    print(f"\n✓ Successfully compiled:")
    for b in compiled:
        print(f"  - {os.path.basename(b)}")

if failed:
    print(f"\n✗ Failed to compile:")
    for b in failed:
        print(f"  - {os.path.basename(b)}")

sys.exit(0 if len(failed) == 0 else 1)
