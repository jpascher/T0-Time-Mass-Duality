<#
.SYNOPSIS
    Kompiliert LaTeX-Dateien im aktuellen Verzeichnis, verschiebt PDFs in Unterverzeichnisse (Deutsch/English)
    und löscht Nicht-.tex- und Nicht-.ps1-Dateien. Nur Dateien ohne existierendes PDF werden kompiliert.

.NOTES
    - Speichern: Speichere dieses Skript als 'compile_latex.ps1' im Verzeichnis mit den .tex-Dateien.
    - Starten: Führe das Skript in PowerShell mit '.\compile_latex.ps1' aus.
    - Voraussetzung: pdflatex muss im Systempfad verfügbar sein.
    - Falls Skriptausführung blockiert wird, setze die Ausführungsrichtlinie: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
#>

# Verzeichnisse erstellen, falls nicht vorhanden
$deutschDir = ".\Deutsch"
$englishDir = ".\English"
if (-not (Test-Path $deutschDir)) { New-Item -ItemType Directory -Path $deutschDir }
if (-not (Test-Path $englishDir)) { New-Item -ItemType Directory -Path $englishDir }

# Alle .tex Dateien im aktuellen Verzeichnis finden
$texFiles = Get-ChildItem -Path .\ -Filter *.tex

# Array für fehlerhafte Kompilierungen
$failedCompilations = @()

foreach ($file in $texFiles) {
    $pdfFile = $file.BaseName + ".pdf"
    $pdfInDeutsch = Join-Path $deutschDir $pdfFile
    $pdfInEnglish = Join-Path $englishDir $pdfFile
    
    # Prüfen, ob PDF bereits existiert
    if ((Test-Path $pdfFile) -or (Test-Path $pdfInDeutsch) -or (Test-Path $pdfInEnglish)) {
        Write-Host "$($file.Name): PDF existiert bereits, überspringe Kompilierung."
        continue
    }
    
    Write-Host "$($file.Name): Kompiliere..."
    
    # Zweimal kompilieren mit pdflatex
    $compileSuccess = $true
    for ($i = 1; $i -le 2; $i++) {
        $process = Start-Process -FilePath "pdflatex" -ArgumentList "-interaction=nonstopmode", $file.Name -NoNewWindow -Wait -PassThru -RedirectStandardOutput "latex_output.txt" -RedirectStandardError "latex_error.txt"
        if ($process.ExitCode -ne 0) {
            $compileSuccess = $false
            break
        }
    }
    
    if (-not $compileSuccess) {
        $failedCompilations += $file.Name
        Write-Host "$($file.Name): Kompilierung fehlgeschlagen."
        continue
    }
    
    # PDF-Datei verschieben
    if (Test-Path $pdfFile) {
        if ($file.Name -match "En\.tex$") {
            $destination = Join-Path $englishDir $pdfFile
            if (Test-Path $destination) { Remove-Item $destination -Force }
            Move-Item -Path $pdfFile -Destination $destination -Force
            Write-Host "$($file.Name): PDF nach English verschoben."
        } else {
            $destination = Join-Path $deutschDir $pdfFile
            if (Test-Path $destination) { Remove-Item $destination -Force }
            Move-Item -Path $pdfFile -Destination $destination -Force
            Write-Host "$($file.Name): PDF nach Deutsch verschoben."
        }
    } else {
        $failedCompilations += $file.Name
        Write-Host "$($file.Name): Kein PDF erzeugt."
    }
}

# Alle nicht-.tex und nicht-.ps1 Dateien löschen (Skript selbst und Verzeichnisse ausnehmen)
Get-ChildItem -Path .\ -Exclude *.tex,*.ps1,Deutsch,English | Remove-Item -Force

# Fehlerhafte Kompilierungen ausgeben
if ($failedCompilations.Count -gt 0) {
    Write-Host "`nFolgende Dokumente konnten nicht fehlerfrei kompiliert werden:"
    $failedCompilations | ForEach-Object { Write-Host $_ }
} else {
    Write-Host "`nAlle Dokumente wurden erfolgreich kompiliert oder übersprungen."
}