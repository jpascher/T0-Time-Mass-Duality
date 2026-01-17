#!/usr/bin/env python3
import subprocess, os, re
from pathlib import Path

def compile_doc(tex_file, output_dir):
    try:
        result = subprocess.run(['lualatex', '-interaction=nonstopmode', '-output-directory', output_dir, tex_file],
                              capture_output=True, text=True, timeout=120, cwd=output_dir)
        return result.returncode == 0
    except: return False

base = Path('/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality')
de_dir, en_dir = base / '2/tex-n/de_standalone', base / '2/tex-n/en_standalone'
de_files = sorted([f for f in os.listdir(de_dir) if f.endswith('.tex') and re.match(r'^\d', f)])
en_files = sorted([f for f in os.listdir(en_dir) if f.endswith('.tex') and re.match(r'^\d', f)])

success, fail = 0, 0
print(f"Compiling remaining {len(de_files[50:])} German + {len(en_files[50:])} English = {len(de_files[50:]) + len(en_files[50:])} docs\n")

print("GERMAN DOCUMENTS (51-115)")
for i, f in enumerate(de_files[50:], 51):
    print(f"[{i}/{len(de_files)}] {f}...", end=" ")
    if compile_doc(f, str(de_dir)): print("✓"); success += 1
    else: print("✗"); fail += 1

print("\nENGLISH DOCUMENTS (51-114)")
for i, f in enumerate(en_files[50:], 51):
    print(f"[{i}/{len(en_files)}] {f}...", end=" ")
    if compile_doc(f, str(en_dir)): print("✓"); success += 1
    else: print("✗"); fail += 1

print(f"\n{'='*60}\nSUMMARY: {success} success, {fail} failed ({100*success/(success+fail):.1f}%)")
