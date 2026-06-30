import os
import re

# Mapping for double apostrophe and double backtick to umlaut
umlaut_map = {
    "''a": "ä",
    "''o": "ö",
    "''u": "ü",
    "''A": "Ä",
    "''O": "Ö",
    "''U": "Ü",
    "``a": "ä",
    "``o": "ö",
    "``u": "ü",
    "``A": "Ä",
    "``O": "Ö",
    "``U": "Ü"
}

# Additional common replacements
word_map = {
    "f''ur": "für",
    "N''ahe": "Nähe",
    "Verh''altnis": "Verhältnis",
    "f''unf": "fünf",
    "r''aum": "räum",
    "T''one": "Töne",
    "Komplexit''at": "Komplexität",
    "w''ahlt": "wählt",
    "Realit''at": "Realität",
    "H''aufig": "Häufig",
    "zuf''allig": "zufällig",
    "repr''asent": "repräsent",
    "Universalit''at": "Universalität",
    "Lufts''aule": "Luftsäule",
    "Verh''altnisse": "Verhältnisse",
    "materialabh''angig": "materialabhängig",
    "Sph''are": "Sphäre",
    "harmonischen Verh''altnisse": "harmonischen Verhältnisse",
    "enth''alt": "enthält",
    "Br''ucke": "Brücke",
    "Br''ucken": "Brücken",
    "vollst''andig": "vollständig",
    "m''oglich": "möglich",
    "k''onnen": "können",
    "sch""on": "schön"
}

def replace_umlauts(text):
    # Replace all ''a, ''o, ...
    for k, v in umlaut_map.items():
        text = text.replace(k, v)
    # Replace common words
    for k, v in word_map.items():
        text = re.sub(rf"{re.escape(k)}", v, text)
    return text

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = replace_umlauts(content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")

def process_dir(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.tex'):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    process_dir(r"2\tex-n\de_standalone")
    process_dir(r"2\tex-n\de_chapters_new")
