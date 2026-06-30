import re
import sys

# Mapping for LaTeX umlauts to Unicode
umlaut_map = {
    r'\\"a': 'ä',
    r'\\"o': 'ö',
    r'\\"u': 'ü',
    r'\\"A': 'Ä',
    r'\\"O': 'Ö',
    r'\\"U': 'Ü',
    r'\\ss': 'ß',
}

# Also replace common words like f\"ur, sch\"on, etc.
def replace_umlauts(text):
    for latex, uni in umlaut_map.items():
        text = re.sub(latex, uni, text)
    return text

if __name__ == "__main__":
    path = r"2/tex-n/de_standalone/116_T0_koide-formel-3_De.tex"
    with open(path, encoding='utf-8') as f:
        content = f.read()
    new_content = replace_umlauts(content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Umlaute ersetzt in: {path}")
    else:
        print("Keine Ersetzungen notwendig.")
