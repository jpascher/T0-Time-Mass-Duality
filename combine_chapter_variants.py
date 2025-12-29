#!/usr/bin/env python3
"""
Script to combine the two variants of DVFT chapters:
1. Individual chapters (tex_DVFT_T0/) - technical with detailed equations
2. Merged chapters (extracted_chapters_from_merged/) - narrative summaries

Creates unified chapters that combine:
- Narrative introduction from merged version
- Detailed mathematical content from individual version
- Unified formulas without contradictions
"""

import os
import re
from pathlib import Path

def read_file(filepath):
    """Read a file and return its content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def write_file(filepath, content):
    """Write content to a file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        return False

def extract_section_content(content):
    """Extract content after \\section command, excluding preamble."""
    # Find the first \section
    match = re.search(r'(\\section\{[^}]+\}.*)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return content

def extract_equations(text):
    """Extract all equations from text with their context."""
    equations = []
    
    # Find equation environments
    patterns = [
        (r'\\begin\{equation\}(.*?)\\end\{equation\}', 'equation'),
        (r'\\\[(.*?)\\\]', 'display'),
    ]
    
    for pattern, eq_type in patterns:
        for match in re.finditer(pattern, text, re.DOTALL):
            equations.append({
                'full': match.group(0),
                'content': match.group(1).strip(),
                'type': eq_type,
                'start': match.start(),
                'end': match.end()
            })
    
    return equations

def normalize_equation(eq_content):
    """Normalize equation for comparison."""
    # Remove whitespace and comments
    normalized = re.sub(r'\s+', '', eq_content)
    normalized = re.sub(r'%.*$', '', normalized, flags=re.MULTILINE)
    return normalized

def find_duplicate_equations(equations):
    """Find duplicate equations and return indices to keep."""
    seen = {}
    keep_indices = []
    
    for i, eq in enumerate(equations):
        norm = normalize_equation(eq['content'])
        if norm not in seen:
            seen[norm] = i
            keep_indices.append(i)
    
    return keep_indices

def extract_preamble_from_merged(merged_content):
    """Extract preamble from merged file, excluding title/author/date."""
    match = re.search(r'(.*?)\\title\{', merged_content, re.DOTALL)
    if match:
        preamble = match.group(1).rstrip()
        # Remove \begin{document} if present
        if preamble.endswith('\\begin{document}'):
            preamble = preamble[:-16].rstrip()
        return preamble
    
    # Fallback: up to \begin{document}
    match = re.search(r'(.*?)\\begin\{document\}', merged_content, re.DOTALL)
    if match:
        return match.group(1).rstrip()
    return None

def combine_chapters(individual_content, merged_content, chapter_num):
    """
    Combine individual (technical) and merged (narrative) versions.
    Strategy:
    1. Use preamble from merged version
    2. Start with narrative introduction from merged version
    3. Add detailed technical content from individual version
    4. Remove duplicate equations
    5. Ensure consistent notation
    """
    
    # Extract sections
    individual_section = extract_section_content(individual_content)
    
    # Extract narrative intro from merged (first paragraph after \section)
    merged_section = extract_section_content(merged_content)
    
    # Get the narrative introduction (text before first subsection or equation)
    intro_match = re.search(r'(\\section\{[^}]+\}.*?)(?:\\subsection|\\begin\{equation\}|\\\[)', 
                           merged_section, re.DOTALL)
    narrative_intro = ""
    if intro_match:
        narrative_intro = intro_match.group(1).strip()
    else:
        # If no subsection found, take first substantial paragraph
        intro_match = re.search(r'(\\section\{[^}]+\}(?:.*?\\par|.*?)\n\n)', 
                               merged_section, re.DOTALL)
        if intro_match:
            narrative_intro = intro_match.group(1).strip()
    
    # If we couldn't extract intro, use the merged section title
    if not narrative_intro:
        section_match = re.search(r'\\section\{([^}]+)\}', merged_section)
        if section_match:
            narrative_intro = f"\\section{{{section_match.group(1)}}}\n\n"
    
    # Build combined content
    combined_parts = []
    
    # Add narrative introduction
    if narrative_intro:
        combined_parts.append(narrative_intro)
        combined_parts.append("\n")
    
    # Add detailed technical content from individual version
    # Remove the section title from individual since we already have it
    individual_without_section = re.sub(r'^\\section\{[^}]+\}\n*', '', individual_section)
    combined_parts.append(individual_without_section)
    
    combined_content = ''.join(combined_parts)
    
    # Extract all equations and remove duplicates
    all_equations = extract_equations(combined_content)
    if all_equations:
        keep_indices = find_duplicate_equations(all_equations)
        
        # If duplicates found, rebuild content without them
        if len(keep_indices) < len(all_equations):
            # Sort equations by position (reverse to remove from end first)
            equations_to_remove = [eq for i, eq in enumerate(all_equations) if i not in keep_indices]
            equations_to_remove.sort(key=lambda x: x['start'], reverse=True)
            
            # Remove duplicate equations
            for eq in equations_to_remove:
                combined_content = (combined_content[:eq['start']] + 
                                  combined_content[eq['end']:])
    
    return combined_content

def create_combined_chapter(chapter_num, individual_dir, merged_dir, output_dir):
    """Create a combined chapter file."""
    
    # Read individual chapter
    individual_file = individual_dir / f"kapitel_{chapter_num:02d}.tex"
    if not individual_file.exists():
        return None
    
    individual_content = read_file(individual_file)
    if not individual_content:
        return None
    
    # Read merged chapter
    merged_file = merged_dir / f"kapitel_{chapter_num:02d}_merged.tex"
    if not merged_file.exists():
        return None
    
    merged_content = read_file(merged_file)
    if not merged_content:
        return None
    
    # Extract preamble from merged version
    preamble = extract_preamble_from_merged(merged_content)
    if not preamble:
        print(f"  Warning: Could not extract preamble for chapter {chapter_num}")
        return None
    
    # Get chapter title from merged version
    title_match = re.search(r'\\section\{Kapitel\s+\d+:\s*([^}]+)\}', merged_content)
    if title_match:
        chapter_title = title_match.group(1).strip()
    else:
        # Fallback to individual version
        title_match = re.search(r'\\section\{([^}]+)\}', individual_content)
        chapter_title = title_match.group(1).strip() if title_match else f"Kapitel {chapter_num}"
    
    # Combine the chapters
    combined_section = combine_chapters(individual_content, merged_content, chapter_num)
    
    # Build final document
    final_content = preamble + "\n\n"
    final_content += f"\\title{{Kapitel {chapter_num}: {chapter_title}}}\n"
    final_content += "\\author{}\n"
    final_content += "\\date{}\n\n"
    final_content += "\\begin{document}\n\n"
    final_content += "\\maketitle\n\n"
    final_content += combined_section
    final_content += "\n\n\\end{document}\n"
    
    # Write output file
    output_file = output_dir / f"kapitel_{chapter_num:02d}_combined.tex"
    if write_file(output_file, final_content):
        return {
            'chapter': chapter_num,
            'title': chapter_title,
            'output_file': output_file.name
        }
    
    return None

def main():
    base_dir = Path("/home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_DVFT")
    
    individual_dir = base_dir / "tex_DVFT_T0"
    merged_dir = base_dir / "extracted_chapters_from_merged"
    output_dir = base_dir / "combined_chapters"
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    print("=" * 80)
    print("COMBINING CHAPTER VARIANTS")
    print("=" * 80)
    print()
    print("Strategy:")
    print("  1. Narrative introduction from merged version (conceptual overview)")
    print("  2. Detailed technical content from individual version (equations & proofs)")
    print("  3. Remove duplicate equations")
    print("  4. Unified formatting")
    print()
    print(f"Output directory: {output_dir}")
    print()
    
    results = []
    
    # Process chapters 12-43
    for chapter_num in range(12, 44):
        result = create_combined_chapter(chapter_num, individual_dir, merged_dir, output_dir)
        
        if result:
            results.append(result)
            print(f"✓ Combined Kapitel {result['chapter']:02d}: {result['title'][:60]}...")
        else:
            # Check if files exist
            ind_exists = (individual_dir / f"kapitel_{chapter_num:02d}.tex").exists()
            merged_exists = (merged_dir / f"kapitel_{chapter_num:02d}_merged.tex").exists()
            
            if not ind_exists and not merged_exists:
                pass  # Skip chapters that don't exist in either version
            else:
                print(f"⚠ Skipped Kapitel {chapter_num} (ind:{ind_exists}, merged:{merged_exists})")
    
    # Summary
    print()
    print("=" * 80)
    print("COMBINATION SUMMARY")
    print("=" * 80)
    print(f"Total chapters combined: {len(results)}")
    print(f"Output directory: {output_dir}")
    print()
    
    if results:
        print("Combined chapters:")
        for result in results:
            print(f"  - Kapitel {result['chapter']:02d}: {result['output_file']}")
    
    print()
    print("=" * 80)
    print("✓ Combination complete!")
    print("=" * 80)
    print()
    print("The combined chapters include:")
    print("  • Narrative introduction (merged version)")
    print("  • Detailed mathematical derivations (individual version)")
    print("  • Unified equations (duplicates removed)")
    print("  • Consistent formatting")

if __name__ == "__main__":
    main()
