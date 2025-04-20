import os
import re

# Konfiguration
TEX_DIR = r"C:\Users\johann\1\2\arb\English"

# Ersetzungsmuster
replacements = [
    (r'\\beta_T\^{\\text{nat}}\s*=\s*[^=]*=', r'\beta_T^{\text{nat}} = \frac{\\lambda_h^2 v^2}{16\\pi^3 m_h^2 \\xi} ='),
    (r'\[\\kappa\^{\\text{nat}}\]\s*=\s*\[E\^0\]', r'[\kappa^{\text{nat}}] = [E]'),
    (r'\\kappa\s+ist\s+dimensionslos\b', r'\kappa hat die Dimension [E]'),
    (r'\\kappa\^{\\text{nat}}\s*=\s*\\beta_T\^{\\text{nat}}\s*\\cdot\s*y\s*v\b', r'\kappa^{\text{nat}} = \beta_T^{\text{nat}} \cdot \frac{y v}{r_g^2}'),
    (r'\\nabla\^2\s*\\Tfield\s*=\s*-\\kappa\s*\\rho\(x\)\s*\\Tfield\b', r'\nabla^2 \\Tfield = -\kappa \rho(x) \\Tfield^2'),
    (r'\\Phi\(r\)\s*=\s*-\\frac{r_g}{r}\b', r'\Phi(r) = -\frac{r_g}{r} + \\kappa r')
]

# Überprüfen, ob TeX-Dateien existieren
tex_files = [f for f in os.listdir(TEX_DIR) if f.endswith('.tex')]
if not tex_files:
    print(f"Keine .tex-Dateien in {TEX_DIR} gefunden!")
    exit(1)

# Treffer anzeigen
for tex_file in tex_files:
    file_path = os.path.join(TEX_DIR, tex_file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin1') as f:
            content = f.read()
    
    print(f"\nTreffer in {tex_file}:")
    for pattern, _ in replacements:
        matches = re.findall(pattern, content)
        if matches:
            print(f"  Muster '{pattern}': {matches}")