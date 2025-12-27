#!/usr/bin/env python3
import os
import re
import glob

# Extended Unicode character mapping
unicode_map = {
    # Additional Greek letters
    '𝑉': 'V', '𝑔': 'g', '𝑆': 'S', '𝑑': 'd', '𝑓': 'f', '𝑘': 'k',
    '𝑙': 'l', '𝑛': 'n', '𝑝': 'p', '𝑞': 'q', '𝑟': 'r', '𝑠': 's',
    '𝑢': 'u', '𝑣': 'v', '𝑤': 'w', '𝑎': 'a', '𝑏': 'b', '𝑜': 'o',
    '𝑗': 'j', '𝑈': 'U', '𝑅': 'R', '𝐻': 'H', '𝐿': 'L', '𝑊': 'W',
    '𝑁': 'N', '𝐾': 'K', '𝐵': 'B', '𝐷': 'D', '𝐴': 'A', '𝑀': 'M',
    '𝐶': 'C', '𝐽': 'J', '𝑄': 'Q', '𝐼': 'I', '𝑂': 'O',
    
    # Math symbols
    '−': '-',  # Minus sign
    '∗': '*',  # Asterisk operator
    '÷': '/',  # Division sign
    '×': r'\times',  # Multiplication
    '±': r'\pm',  # Plus-minus
    '∓': r'\mp',  # Minus-plus
    '∇': r'\nabla',  # Nabla
    '∂': r'\partial',  # Partial derivative
    '∆': r'\Delta',  # Delta (capital)
    '∑': r'\sum',  # Summation
    '∏': r'\prod',  # Product
    '∫': r'\int',  # Integral
    '√': r'\sqrt',  # Square root
    '∞': r'\infty',  # Infinity
    '≈': r'\approx',  # Approximately equal
    '≠': r'\neq',  # Not equal
    '≤': r'\leq',  # Less than or equal
    '≥': r'\geq',  # Greater than or equal
    '≡': r'\equiv',  # Identical to
    '∝': r'\propto',  # Proportional to
    '→': r'\rightarrow',  # Right arrow
    '←': r'\leftarrow',  # Left arrow
    '⇒': r'\Rightarrow',  # Double right arrow
    '⟹': r'\Longrightarrow',  # Long double right arrow
    '⇔': r'\Leftrightarrow',  # Double left-right arrow
    '∈': r'\in',  # Element of
    '∉': r'\notin',  # Not element of
    '⊂': r'\subset',  # Subset
    '⊃': r'\supset',  # Superset
    '∅': r'\emptyset',  # Empty set
    '∧': r'\wedge',  # Logical and
    '∨': r'\vee',  # Logical or
    '¬': r'\neg',  # Logical not
    '∀': r'\forall',  # For all
    '∃': r'\exists',  # There exists
    '⊗': r'\otimes',  # Tensor product
    '⊕': r'\oplus',  # Direct sum
    '⟨': r'\langle',  # Left angle bracket
    '⟩': r'\rangle',  # Right angle bracket
    '▫': r'\Box',  # Box operator (d'Alembertian)
    'ℒ': r'\mathcal{L}',  # Script L (Lagrangian)
    'ℋ': r'\mathcal{H}',  # Script H (Hamiltonian)
    
    # Superscripts
    '²': '^2', '³': '^3', '⁴': '^4', '⁵': '^5',
    '⁶': '^6', '⁷': '^7', '⁸': '^8', '⁹': '^9',
    '⁰': '^0', '¹': '^1',
}

def fix_unicode_in_file(filepath):
    """Fix Unicode characters in a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    replacements = 0
    
    for unicode_char, latex_replacement in unicode_map.items():
        count = content.count(unicode_char)
        if count > 0:
            content = content.replace(unicode_char, latex_replacement)
            replacements += count
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {replacements} Unicode characters in {os.path.basename(filepath)}")
        return replacements
    return 0

# Fix all content_only files
content_dir = 'content_only'
total_replacements = 0

if os.path.exists(content_dir):
    for tex_file in glob.glob(os.path.join(content_dir, '*.tex')):
        replacements = fix_unicode_in_file(tex_file)
        total_replacements += replacements

print(f"\nTotal: {total_replacements} Unicode characters replaced across all files")
