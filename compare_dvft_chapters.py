#!/usr/bin/env python3
"""
Compare DVFT chapters to identify theoretical deviations.
This creates a detailed report showing differences between versions.
"""

import os
import re
from pathlib import Path
from difflib import SequenceMatcher, unified_diff

def read_file(filepath):
    """Read a file and return its content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return None

def extract_section_range(text, section_pattern):
    """Extract a section from text based on pattern."""
    # Find section start
    match = re.search(section_pattern, text, re.IGNORECASE)
    if not match:
        return None
    
    start = match.start()
    # Find next section
    next_section = re.search(r'\\section\{', text[start + 10:])
    if next_section:
        end = start + 10 + next_section.start()
    else:
        end = len(text)
    
    return text[start:end]

def extract_equations_from_text(text):
    """Extract equations with their context."""
    equations = []
    
    # Find equation environments
    patterns = [
        r'\\begin\{equation\}(.*?)\\end\{equation\}',
        r'\\\[(.*?)\\\]',
    ]
    
    for pattern in patterns:
        for match in re.finditer(pattern, text, re.DOTALL):
            # Get some context before and after
            context_start = max(0, match.start() - 100)
            context_end = min(len(text), match.end() + 100)
            context = text[context_start:context_end]
            
            equations.append({
                'content': match.group(1).strip(),
                'context': context
            })
    
    return equations

def compare_texts(text1, text2, label1, label2):
    """Compare two texts and return difference metrics."""
    # Normalize whitespace
    text1_norm = re.sub(r'\s+', ' ', text1)
    text2_norm = re.sub(r'\s+', ' ', text2)
    
    # Calculate similarity
    similarity = SequenceMatcher(None, text1_norm, text2_norm).ratio()
    
    # Extract equations
    eqs1 = extract_equations_from_text(text1)
    eqs2 = extract_equations_from_text(text2)
    
    # Find missing equations
    missing_in_2 = []
    for eq in eqs1:
        eq_norm = re.sub(r'\s+', '', eq['content'])
        text2_compact = re.sub(r'\s+', '', text2)
        if eq_norm not in text2_compact:
            missing_in_2.append(eq)
    
    missing_in_1 = []
    for eq in eqs2:
        eq_norm = re.sub(r'\s+', '', eq['content'])
        text1_compact = re.sub(r'\s+', '', text1)
        if eq_norm not in text1_compact:
            missing_in_1.append(eq)
    
    return {
        'similarity': similarity,
        'eq_count_1': len(eqs1),
        'eq_count_2': len(eqs2),
        'missing_in_2': missing_in_2,
        'missing_in_1': missing_in_1,
        'length_1': len(text1),
        'length_2': len(text2),
    }

def main():
    base_dir = Path("/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_DVFT")
    individual_dir = base_dir / "tex_DVFT_T0"
    
    # Mapping of chapters to merged files based on filenames
    chapter_to_merged = {}
    for i in range(12, 16):
        chapter_to_merged[i] = "202_12-15_De.tex"
    for i in range(16, 20):
        chapter_to_merged[i] = "202_16-19_De.tex"
    for i in range(20, 33):
        chapter_to_merged[i] = "202_20-32_De.tex"
    for i in range(33, 44):
        chapter_to_merged[i] = "202_33-43_De.tex"
    for i in range(43, 45):
        chapter_to_merged[i] = "202_43-44_De.tex"
    
    print("=" * 100)
    print(" " * 20 + "DVFT CHAPTER COMPARISON REPORT")
    print("=" * 100)
    print()
    print("Comparing individual chapters (tex_DVFT_T0/kapitel_XX.tex)")
    print("with merged versions (202_XX-YY_De.tex)")
    print()
    
    critical_differences = []
    moderate_differences = []
    minor_differences = []
    
    for chapter_num in range(12, 45):
        individual_file = individual_dir / f"kapitel_{chapter_num:02d}.tex"
        
        if not individual_file.exists():
            continue
        
        if chapter_num not in chapter_to_merged:
            continue
        
        merged_filename = chapter_to_merged[chapter_num]
        merged_file = base_dir / merged_filename
        
        # Read files
        ind_content = read_file(individual_file)
        merged_content = read_file(merged_file)
        
        if not ind_content or not merged_content:
            continue
        
        # Extract the chapter section from merged file
        # The merged files have sections like "\section{Kapitel 12: ...}"
        chapter_section = extract_section_range(
            merged_content,
            rf'\\section\{{.*?Kapitel\s+{chapter_num}[:\s]'
        )
        
        if not chapter_section:
            print(f"⚠️  Chapter {chapter_num}: Not found in {merged_filename}")
            continue
        
        # Compare
        comparison = compare_texts(ind_content, chapter_section, 
                                  f"Individual", f"Merged")
        
        # Categorize differences
        issue = {
            'chapter': chapter_num,
            'merged_file': merged_filename,
            'comparison': comparison
        }
        
        if comparison['similarity'] < 0.5:
            critical_differences.append(issue)
        elif comparison['similarity'] < 0.8:
            moderate_differences.append(issue)
        elif comparison['similarity'] < 0.95 or comparison['missing_in_2'] or comparison['missing_in_1']:
            minor_differences.append(issue)
    
    # Print detailed report
    print("=" * 100)
    print("ANALYSIS RESULTS")
    print("=" * 100)
    print()
    
    if critical_differences:
        print("🔴 CRITICAL DIFFERENCES (Similarity < 50%):")
        print("    These chapters have substantial differences that affect the theory:")
        print()
        for issue in critical_differences:
            comp = issue['comparison']
            print(f"  Chapter {issue['chapter']} (in {issue['merged_file']}):")
            print(f"    - Similarity: {comp['similarity']*100:.1f}%")
            print(f"    - Individual version: {comp['eq_count_1']} equations, {comp['length_1']} chars")
            print(f"    - Merged version: {comp['eq_count_2']} equations, {comp['length_2']} chars")
            print(f"    - Equations in individual but not merged: {len(comp['missing_in_2'])}")
            print(f"    - Equations in merged but not individual: {len(comp['missing_in_1'])}")
            
            if comp['missing_in_2']:
                print(f"    - Examples of equations missing from merged version:")
                for i, eq in enumerate(comp['missing_in_2'][:2], 1):
                    preview = eq['content'][:80].replace('\n', ' ')
                    print(f"      {i}. {preview}...")
            print()
    
    if moderate_differences:
        print("🟡 MODERATE DIFFERENCES (Similarity 50-80%):")
        print("    These chapters have noticeable differences:")
        print()
        for issue in moderate_differences:
            comp = issue['comparison']
            print(f"  Chapter {issue['chapter']} (in {issue['merged_file']}):")
            print(f"    - Similarity: {comp['similarity']*100:.1f}%")
            print(f"    - Equations: {comp['eq_count_1']} (individual) vs {comp['eq_count_2']} (merged)")
            print(f"    - Missing from merged: {len(comp['missing_in_2'])}")
            print(f"    - Missing from individual: {len(comp['missing_in_1'])}")
            print()
    
    if minor_differences:
        print("🟢 MINOR DIFFERENCES (Similarity 80-95% or equation differences):")
        print("    These chapters have small differences:")
        print()
        for issue in minor_differences:
            comp = issue['comparison']
            print(f"  Chapter {issue['chapter']}: {comp['similarity']*100:.1f}% similar", end='')
            if comp['missing_in_2'] or comp['missing_in_1']:
                print(f" ({len(comp['missing_in_2'])} missing from merged, {len(comp['missing_in_1'])} extra in merged)", end='')
            print()
    
    # Summary
    print()
    print("=" * 100)
    print("SUMMARY")
    print("=" * 100)
    total = len(critical_differences) + len(moderate_differences) + len(minor_differences)
    analyzed = len([c for c in range(12, 45) if (individual_dir / f"kapitel_{c:02d}.tex").exists()])
    
    print(f"Chapters analyzed: {analyzed}")
    print(f"Chapters with differences: {total}")
    print(f"  - Critical (< 50% similar): {len(critical_differences)}")
    print(f"  - Moderate (50-80% similar): {len(moderate_differences)}")
    print(f"  - Minor (80-95% similar or equation diffs): {len(minor_differences)}")
    print()
    
    if critical_differences or moderate_differences:
        print("⚠️  ACTION REQUIRED:")
        print("    Review the differences above to determine if they affect the theory.")
        print("    The versions have different content that should be reconciled.")
    else:
        print("✓ No significant theoretical deviations detected.")
    
    print("=" * 100)

if __name__ == "__main__":
    main()
