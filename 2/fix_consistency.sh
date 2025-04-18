#!/bin/bash

# Fehlerbehandlung aktivieren
set -e

# Überprüfen, ob TeX-Dateien existieren
if ! ls *.tex &> /dev/null; then
    echo "Keine .tex-Dateien im aktuellen Verzeichnis gefunden!"
    exit 1
fi

# Überprüfen, ob Git-Repository vorhanden ist
if ! git rev-parse --is-inside-work-tree &> /dev/null; then
    echo "Dieses Verzeichnis ist kein Git-Repository!"
    exit 1
fi

# Erstellen eines Backup-Verzeichnisses mit Zeitstempel
BACKUP_DIR="backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Git-Branch für Änderungen erstellen
git checkout -b consistency-fixes

# Log für Änderungen
LOG_FILE="changes_$(date +%Y%m%d_%H%M%S).log"
touch "$LOG_FILE"

# Für jede TeX-Datei im Unterverzeichnis arb/English
for file in arb/English/*.tex; do
    # Backup erstellen
    cp "$file" "$BACKUP_DIR/"
    
    
    echo "Bearbeite $file..." | tee -a "$LOG_FILE"
    
    # 1. Korrektur der β_T-Formel und Dimension
    sed -i.bak -E 's/\\beta_T\^{\\text{nat\}\} = [^=]*=/\\beta_T\^{\\text{nat\}} = \\frac{\\lambda_h^2 v^2}{16\\pi^3 m_h^2 \\xi} =/g' "$file"
    
    # 2. Korrekte Dimension für κ
    sed -i.bak 's/\[\\kappa\^{\\text{nat}}\] = \[E\^0\]/\[\\kappa\^{\\text{nat}}\] = \[E\]/g' "$file"
    sed -i.bak 's/\\kappa ist dimensionslos/\\kappa hat die Dimension \[E\]/g' "$file"
    
    # 3. Korrektur der κ-Berechnung
    sed -i.bak 's/\\kappa\^{\\text{nat}} = \\beta_T\^{\\text{nat}} \\cdot y v/\\kappa\^{\\text{nat}} = \\beta_T\^{\\text{nat}} \\cdot \\frac{y v}{r_g^2}/g' "$file"
    
    # 4. Konsistente Feldgleichung
    sed -i.bak 's/\\nabla\^2 \\Tfield = -\\kappa \\rho(x) \\Tfield/\\nabla\^2 \\Tfield = -\\kappa \\rho(x) \\Tfield\^2/g' "$file"
    
    # 5. Korrektes Gravitationspotential
    sed -i.bak 's/\\Phi(r) = -\\frac{r_g}{r}/\\Phi(r) = -\\frac{r_g}{r} + \\kappa r/g' "$file"
    
    # Überprüfen, ob Änderungen vorgenommen wurden
    if git diff --quiet "$file"; then
        echo "Keine Änderungen an $file vorgenommen." | tee -a "$LOG_FILE"
    else
        git add "$file"
        git commit -m "Konsistenzkorrektur für $file"
        echo "Änderungen an $file committed." | tee -a "$LOG_FILE"
    fi
done

echo "Alle Änderungen abgeschlossen. Die Originaldateien wurden in $BACKUP_DIR gesichert." | tee -a "$LOG_FILE"
echo "Überprüfen Sie die Änderungen mit 'git diff master' und führen Sie 'git push' aus, um sie auf GitHub hochzuladen." | tee -a "$LOG_FILE"