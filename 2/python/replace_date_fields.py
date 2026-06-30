import os
import re

import os
import re

# Replacement patterns for English and German
REPLACEMENTS_EN = [
    (re.compile(r'\\date\{[^}]*\}'), r'\\date{January 2025}'),
    (re.compile(r'\\datum\{[^}]*\}'), r'\\datum{January 2025}')
]
REPLACEMENTS_DE = [
    (re.compile(r'\\date\{[^}]*\}'), r'\\date{Januar 2025}'),
    (re.compile(r'\\datum\{[^}]*\}'), r'\\datum{Januar 2025}')
]

# Search all .tex files recursively from current directory
ROOTS = [os.getcwd()]

def is_german_file(path):
    # Heuristic: 'de_' or '_De' or '_de' in path or filename
    lowered = path.lower()
    return ("de_" in lowered or lowered.endswith('_de.tex') or lowered.endswith('_de_ch.tex'))

for root in ROOTS:
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith('.tex'):
                fpath = os.path.join(dirpath, fname)
                replacements = REPLACEMENTS_DE if is_german_file(fpath) else REPLACEMENTS_EN
                with open(fpath, encoding='utf-8') as f:
                    content = f.read()
                # Insert date if missing
                if not re.search(r'\\date\{[^}]*\}', content):
                    if is_german_file(fpath):
                        content = '\\date{Januar 2025}\n' + content
                    else:
                        content = '\\date{January 2025}\n' + content
                new_content = content
                for pattern, repl in replacements:
                    new_content = pattern.sub(repl, new_content)
                if new_content != content:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {fpath}")
