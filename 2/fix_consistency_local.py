import os
import shutil
from datetime import datetime
import logging

# Konfiguration
TEX_DIR = r"C:\Users\johann\1\2\arb\English"
BACKUP_DIR = os.path.join(TEX_DIR, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
LOG_FILE = os.path.join(TEX_DIR, f"changes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Logging einrichten
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, encoding='utf-8',
                    format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# Überprüfen, ob TeX-Dateien existieren
tex_files = [f for f in os.listdir(TEX_DIR) if f.endswith('.tex')]
if not tex_files:
    logger.error("Keine .tex-Dateien in %s gefunden!", TEX_DIR)
    print(f"Keine .tex-Dateien in {TEX_DIR} gefunden!")
    exit(1)

# Backup-Verzeichnis erstellen
os.makedirs(BACKUP_DIR, exist_ok=True)
logger.info("Backup-Verzeichnis erstellt: %s", BACKUP_DIR)
print(f"Backup-Verzeichnis erstellt: {BACKUP_DIR}")

# Ersetzungspaare (exakte Strings statt Regex)
replacements = [
    # 1. β_T-Formel (Standard)
    {
        'search': r'\beta_T^{\text{nat}} = \frac{\lambda_h^2 v^2}{16 \pi^3 m_h^2 \xi} =',
        'replace': r'\beta_T^{\text{nat}} = \frac{\lambda_h^2 v^2}{16\pi^3 m_h^2 \xi} =',
        'validate': lambda s: r'\beta_T^{\text{nat}} = ' in s and '=' in s
    },
    # 2. β_T-Formel (ZeitMasseT0ParamsEn.tex)
    {
        'search': r'\beta_T^{\text{nat}} = \frac{\lambda_h^2 v^2}{4\pi^2 \lambda_0^2 \alpha_0}',
        'replace': r'\beta_T^{\text{nat}} = \frac{\lambda_h^2 v^2}{16\pi^3 m_h^2 \xi} =',
        'validate': lambda s: r'\beta_T^{\text{nat}} = \frac{\lambda_h^2 v^2}{4\pi^2 \lambda_0^2 \alpha_0}' in s
    },
    # 3. Dimension von κ
    {
        'search': r'[\kappa^{\text{nat}}] = [E^0]',
        'replace': r'[\kappa^{\text{nat}}] = [E]',
        'validate': lambda s: r'[\kappa^{\text{nat}}] = ' in s
    },
    # 4. κ Dimensionstext
    {
        'search': r'\kappa ist dimensionslos',
        'replace': r'\kappa hat die Dimension [E]',
        'validate': lambda s: r'\kappa ist dimensionslos' in s
    },
    # 5. κ-Berechnung
    {
        'search': r'\kappa^{\text{nat}} = \beta_T^{\text{nat}} \cdot y v',
        'replace': r'\kappa^{\text{nat}} = \beta_T^{\text{nat}} \cdot \frac{y v}{r_g^2}',
        'validate': lambda s: r'\kappa^{\text{nat}} = \beta_T^{\text{nat}} \cdot y v' in s
    },
    # 6. Feldgleichung
    {
        'search': r'\nabla^2 \Tfield = -\kappa \rho(x) \Tfield',
        'replace': r'\nabla^2 \Tfield = -\kappa \rho(x) \Tfield^2',
        'validate': lambda s: r'\nabla^2 \Tfield = -\kappa \rho(x) \Tfield' in s
    },
    # 7. Gravitationspotential
    {
        'search': r'\Phi(r) = -\frac{r_g}{r}',
        'replace': r'\Phi(r) = -\frac{r_g}{r} + \kappa r',
        'validate': lambda s: r'\Phi(r) = -\frac{r_g}{r}' in s
    }
]

# Verarbeitung der Dateien
for tex_file in tex_files:
    file_path = os.path.join(TEX_DIR, tex_file)
    logger.info("Bearbeite %s...", tex_file)
    print(f"Bearbeite {tex_file}...")

    # Backup erstellen
    shutil.copy2(file_path, BACKUP_DIR)

    # Datei lesen
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        logger.error("Kodierungsfehler bei %s. Versuche alternative Kodierung.", tex_file)
        print(f"Kodierungsfehler bei {tex_file}. Versuche alternative Kodierung.")
        with open(file_path, 'r', encoding='latin1') as f:
            content = f.read()

    # Ersetzungen durchführen
    new_content = content
    changes_made = False
    for replacement in replacements:
        search_str = replacement['search']
        replace_str = replacement['replace']
        validate = replacement['validate']
        
        # Prüfen, ob der Suchstring vorhanden ist und validiert wird
        if search_str in new_content and validate(new_content):
            logger.info("Treffer für '%s' in %s gefunden.", search_str, tex_file)
            print(f"Treffer für '{search_str}' in {tex_file} gefunden.")
            new_content = new_content.replace(search_str, replace_str)
            changes_made = True
        else:
            logger.info("Kein Treffer für '%s' in %s.", search_str, tex_file)

    # Änderungen speichern
    if changes_made:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            logger.info("Änderungen an %s gespeichert.", tex_file)
            print(f"Änderungen an {tex_file} gespeichert.")
        except Exception as e:
            logger.error("Fehler beim Speichern von %s: %s", tex_file, e)
            print(f"Fehler beim Speichern von {tex_file}: {e}")
            exit(1)
    else:
        logger.info("Keine Änderungen an %s vorgenommen.", tex_file)
        print(f"Keine Änderungen an {tex_file} vorgenommen.")

# Abschluss
logger.info("Alle Änderungen abgeschlossen. Originaldateien in %s gesichert.", BACKUP_DIR)
print(f"Alle Änderungen abgeschlossen. Originaldateien in {BACKUP_DIR} gesichert.")