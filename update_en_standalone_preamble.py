import os
import re

def update_preamble_in_en_standalone():
    root = os.path.join('.', '2', 'tex-n', 'en_standalone')
    pattern = re.compile(r'\\input\{\.\./\.\./\.\./T0_preamble_shared-ebook_En\}')
    replacement = r'\\input{T0_preamble_standalone_En}'
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith('.tex'):
                fpath = os.path.join(dirpath, fname)
                with open(fpath, encoding='utf-8') as f:
                    content = f.read()
                new_content = pattern.sub(replacement, content)
                if new_content != content:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {fpath}")

if __name__ == "__main__":
    update_preamble_in_en_standalone()
