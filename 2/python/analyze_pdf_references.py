"""
Analyze PDF references in LaTeX files and identify issues.
"""
import os
import re
from pathlib import Path
from collections import defaultdict

def extract_pdf_references(tex_file):
    """Extract all PDF references from a LaTeX file."""
    references = {
        'preamble_comments': [],  # % Standardized preamble - XXX.pdf
        'filename_comments': [],  # % Filename: XXX.pdf
        'document_refs': [],      # References in document body
        'urls': [],               # External URLs with .pdf
    }
    
    with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            # Preamble comments
            if re.search(r'%\s*Standardized preamble\s*-\s*(.+\.pdf)', line, re.IGNORECASE):
                match = re.search(r'%\s*Standardized preamble\s*-\s*(.+\.pdf)', line, re.IGNORECASE)
                pdf_name = match.group(1).strip()
                references['preamble_comments'].append((line_num, pdf_name))
            
            # Filename comments
            if re.search(r'%\s*Filename:\s*(.+\.pdf)', line, re.IGNORECASE):
                match = re.search(r'%\s*Filename:\s*(.+\.pdf)', line, re.IGNORECASE)
                pdf_name = match.group(1).strip()
                references['filename_comments'].append((line_num, pdf_name))
            
            # Document references (not URLs)
            # Look for patterns like: \textbf{XXX_De.pdf}, \textit{XXX_De.pdf}, XXX_De.pdf in text
            local_refs = re.findall(r'(?:textbf|textit|texttt)?{?([0-9]{3}[_a-zA-Z0-9\-]+_(?:De|En)\.pdf)}?', line)
            for ref in local_refs:
                if 'url{' not in line.lower():  # Skip if part of URL
                    references['document_refs'].append((line_num, ref))
            
            # Also catch simpler patterns
            simple_refs = re.findall(r'([A-Z][a-zA-Z0-9_\-]+_(?:De|En)\.pdf)', line)
            for ref in simple_refs:
                if 'url{' not in line.lower() and ref not in [r[1] for r in references['document_refs']]:
                    references['document_refs'].append((line_num, ref))
            
            # External URLs
            url_refs = re.findall(r'\\url{([^}]+\.pdf[^}]*)}', line)
            for url in url_refs:
                references['urls'].append((line_num, url))
    
    return references

def normalize_filename(filename):
    """Normalize filename for comparison."""
    # Remove LaTeX escapes
    normalized = filename.replace('\\_', '_')
    normalized = normalized.replace('\\\\', '\\')
    return normalized

def get_expected_pdf_name(tex_filename):
    """Get expected PDF name from TEX filename."""
    # For 001_T0_Book_Abstract_De.tex -> 001_T0_Book_Abstract_De.pdf
    return tex_filename.replace('.tex', '.pdf')

def analyze_directory(directory):
    """Analyze all TEX files in directory for PDF reference issues."""
    tex_dir = Path(directory)
    issues = defaultdict(list)
    
    # Get list of TEX files
    tex_files = sorted(tex_dir.glob('*.tex'))
    
    # Build list of expected PDF names
    expected_pdfs = {get_expected_pdf_name(f.name) for f in tex_files}
    
    print(f"Analyzing {len(tex_files)} TEX files...")
    print(f"Expected {len(expected_pdfs)} corresponding PDF files")
    print()
    
    for tex_file in tex_files:
        tex_name = tex_file.name
        expected_pdf = get_expected_pdf_name(tex_name)
        
        refs = extract_pdf_references(tex_file)
        
        # Check preamble comments
        for line_num, pdf_ref in refs['preamble_comments']:
            normalized = normalize_filename(pdf_ref)
            if normalized != expected_pdf:
                issues[tex_name].append({
                    'type': 'preamble_mismatch',
                    'line': line_num,
                    'found': pdf_ref,
                    'expected': expected_pdf,
                    'severity': 'high'
                })
        
        # Check filename comments
        for line_num, pdf_ref in refs['filename_comments']:
            normalized = normalize_filename(pdf_ref)
            if normalized != expected_pdf:
                issues[tex_name].append({
                    'type': 'filename_comment_mismatch',
                    'line': line_num,
                    'found': pdf_ref,
                    'expected': expected_pdf,
                    'severity': 'high'
                })
        
        # Check document references
        for line_num, pdf_ref in refs['document_refs']:
            normalized = normalize_filename(pdf_ref)
            if normalized not in expected_pdfs:
                # Check for common patterns of broken references
                issues[tex_name].append({
                    'type': 'broken_reference',
                    'line': line_num,
                    'found': pdf_ref,
                    'severity': 'medium'
                })
    
    return issues, expected_pdfs

def print_report(issues, expected_pdfs):
    """Print a detailed report of issues."""
    print("=" * 80)
    print("PDF REFERENCE ANALYSIS REPORT")
    print("=" * 80)
    print()
    
    # High severity issues
    high_issues = {k: [i for i in v if i['severity'] == 'high'] 
                   for k, v in issues.items() if any(i['severity'] == 'high' for i in v)}
    
    if high_issues:
        print("HIGH SEVERITY: Preamble/Filename Mismatches")
        print("-" * 80)
        for tex_file, file_issues in sorted(high_issues.items()):
            print(f"\n{tex_file}:")
            for issue in file_issues:
                print(f"  Line {issue['line']}: {issue['type']}")
                print(f"    Found:    {issue['found']}")
                print(f"    Expected: {issue['expected']}")
        print()
    
    # Medium severity issues
    medium_issues = {k: [i for i in v if i['severity'] == 'medium'] 
                     for k, v in issues.items() if any(i['severity'] == 'medium' for i in v)}
    
    if medium_issues:
        print("MEDIUM SEVERITY: Potentially Broken Document References")
        print("-" * 80)
        for tex_file, file_issues in sorted(medium_issues.items()):
            print(f"\n{tex_file}:")
            refs = defaultdict(list)
            for issue in file_issues:
                refs[issue['found']].append(issue['line'])
            for ref, lines in sorted(refs.items()):
                print(f"  {ref} (lines: {', '.join(map(str, lines))})")
        print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    total_high = sum(len([i for i in v if i['severity'] == 'high']) for v in issues.values())
    total_medium = sum(len([i for i in v if i['severity'] == 'medium']) for v in issues.values())
    
    print(f"Files with issues: {len(issues)}")
    print(f"High severity issues: {total_high}")
    print(f"Medium severity issues: {total_medium}")
    print()
    
    # Common problematic references
    all_broken_refs = defaultdict(int)
    for file_issues in issues.values():
        for issue in file_issues:
            if issue['type'] == 'broken_reference':
                all_broken_refs[issue['found']] += 1
    
    if all_broken_refs:
        print("Most Common Potentially Broken References:")
        print("-" * 80)
        for ref, count in sorted(all_broken_refs.items(), key=lambda x: x[1], reverse=True)[:20]:
            print(f"  {ref}: {count} occurrences")

def main():
    directory = r'C:\Users\johann\B18\2\tex-n\de_standalone'
    
    if not os.path.exists(directory):
        print(f"Error: Directory not found: {directory}")
        return
    
    issues, expected_pdfs = analyze_directory(directory)
    print_report(issues, expected_pdfs)
    
    # Generate fix suggestions
    print()
    print("=" * 80)
    print("FIX SUGGESTIONS")
    print("=" * 80)
    print()
    print("1. For preamble mismatches: Update the comment to match the TEX filename")
    print("2. For broken references: Verify the referenced document exists or update")
    print("3. Common patterns to check:")
    print("   - Missing number prefixes (e.g., T0_Grundlagen_De.pdf vs 003_T0_Grundlagen_v1_De.pdf)")
    print("   - Version suffixes (e.g., _v1)")
    print("   - Naming inconsistencies (e.g., HdokumentDe.pdf vs 040_Hdokument_De.pdf)")

if __name__ == '__main__':
    main()
