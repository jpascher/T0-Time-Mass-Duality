# PowerShell-Skript: fix_consistency.ps1

# Fehlerbehandlung aktivieren
$ErrorActionPreference = "Stop"

# Repository-Wurzel ermitteln
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path  # C:\Users\johann\1

# Überprüfen, ob TeX-Dateien im Unterverzeichnis 2/arb/English existieren
$texFiles = Get-ChildItem -Path (Join-Path $repoRoot "2\arb\English\*.tex") -ErrorAction SilentlyContinue
if (-not $texFiles) {
    Write-Output "Keine .tex-Dateien in 2\arb\English gefunden!"
    exit 1
}

# Überprüfen, ob Git-Repository vorhanden ist
if (-not (Test-Path (Join-Path $repoRoot ".git"))) {
    Write-Output "Dieses Verzeichnis ist kein Git-Repository!"
    exit 1
}

# Erstellen eines Backup-Verzeichnisses mit Zeitstempel
$backupDir = "backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path (Join-Path $repoRoot "2\$backupDir") | Out-Null

# Git-Branch für Änderungen erstellen
$branchExists = git branch --list consistency-fixes
if ($branchExists) {
    git checkout consistency-fixes
} else {
    git checkout -b consistency-fixes
}

# Log-Datei für Änderungen
$logFile = "changes_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"
"Aenderungsprotokoll" | Out-File -FilePath (Join-Path $repoRoot "2\$logFile") -Encoding utf8

# Für jede TeX-Datei
foreach ($file in $texFiles) {
    # Backup erstellen
    Copy-Item -Path $file.FullName -Destination (Join-Path $repoRoot "2\$backupDir")
    Write-Output "Bearbeite $($file.Name)..." | Tee-Object -FilePath (Join-Path $repoRoot "2\$logFile") -Append

    # Inhalt der Datei lesen
    $content = Get-Content -Path $file.FullName -Raw

    # 1. Korrektur der β_T-Formel und Dimension
    $newContent = $content -replace '\\beta_T\^{\\text{nat}} = [^=]*=', '\beta_T^{\text{nat}} = \frac{\lambda_h^2 v^2}{16\pi^3 m_h^2 \xi} ='

    # 2. Korrekte Dimension für κ
    $newContent = $newContent -replace '\[\\kappa\^{\\text{nat}}\] = \[E\^0\]', '[\kappa^{\text{nat}}] = [E]'
    $newContent = $newContent -replace '\\kappa ist dimensionslos', '\kappa hat die Dimension [E]'

    # 3. Korrektur der κ-Berechnung
    $newContent = $newContent -replace '\\kappa\^{\\text{nat}} = \\beta_T\^{\\text{nat}} \\cdot y v', '\kappa^{\text{nat}} = \beta_T^{\text{nat}} \cdot \frac{y v}{r_g^2}'

    # 4. Konsistente Feldgleichung
    $newContent = $newContent -replace '\\nabla\^2 \\Tfield = -\\kappa \\rho\(x\) \\Tfield', '\nabla^2 \Tfield = -\kappa \rho(x) \Tfield^2'

    # 5. Korrektes Gravitationspotential
    $newContent = $newContent -replace '\\Phi\(r\) = -\\frac{r_g}{r}', '\Phi(r) = -\frac{r_g}{r} + \kappa r'

    # Änderungen speichern, falls der Inhalt geändert wurde
    if ($newContent -ne $content) {
        $newContent | Set-Content -Path $file.FullName -Encoding utf8
        try {
            # Git-Pfad relativ zum Repository-Wurzelverzeichnis
            $relativePath = $file.FullName.Substring($repoRoot.Length + 1)
            git add $relativePath
            git commit -m "Konsistenzkorrektur fuer $($file.Name)"
            Write-Output "Aenderungen an $($file.Name) committed." | Tee-Object -FilePath (Join-Path $repoRoot "2\$logFile") -Append
        } catch {
            Write-Output "Fehler beim Commit fuer $($file.Name): $_" | Tee-Object -FilePath (Join-Path $repoRoot "2\$logFile") -Append
            exit 1
        }
    } else {
        Write-Output "Keine Aenderungen an $($file.Name) vorgenommen." | Tee-Object -FilePath (Join-Path $repoRoot "2\$logFile") -Append
    }
}

Write-Output "Alle Aenderungen abgeschlossen. Die Originaldateien wurden in $backupDir gesichert." | Tee-Object -FilePath (Join-Path $repoRoot "2\$logFile") -Append
Write-Output "Ueberpruefen Sie die Aenderungen mit 'git diff master' und fuehren Sie 'git push' aus, um sie auf GitHub hochzuladen." | Tee-Object -FilePath (Join-Path $repoRoot "2\$logFile") -Append