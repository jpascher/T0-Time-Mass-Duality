<#
.SYNOPSIS
    Kompiliert LaTeX-Dateien im aktuellen Verzeichnis mit LuaLaTeX (für moderne Schriften),
    verschiebt PDFs in Unterverzeichnisse (Deutsch/English) und löscht unnötige Dateien.
    Nur Dateien ohne existierendes PDF werden kompiliert.

.NOTES
    - Speichern: Als 'compile_latex.ps1' im Verzeichnis mit den .tex-Dateien speichern.
    - Starten: In PowerShell mit '.\compile_latex.ps1' ausführen.
    - Voraussetzung: LuaLaTeX muss im Systempfad verfügbar sein (TeX Live / MiKTeX).
      Für moderne Schriften (Inter, JetBrains Mono usw.) muss das Dokument mit LuaLaTeX kompiliert werden.
    - Falls Skript blockiert wird: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
#>

# Verzeichnisse erstellen, falls nicht vorhanden
$deutschDir = ".\Deutsch"
$englishDir = ".\English"
if (-not (Test-Path $deutschDir)) { New-Item -ItemType Directory -Path $deutschDir }
if (-not (Test-Path $englishDir)) { New-Item -ItemType Directory -Path $englishDir }

# Prüfen, ob LuaLaTeX verfügbar ist
if (-not (Get-Command lualatex -ErrorAction SilentlyContinue)) {
    Write-Host "FEHLER: LuaLaTeX nicht gefunden! Bitte stelle sicher, dass LuaLaTeX im Systempfad ist." -ForegroundColor Red
    Write-Host "Beispielpfade: C:\texlive\2025\bin\win32\lualatex.exe oder MiKTeX-Installation."
    exit 1
}

# Alle .tex-Dateien im aktuellen Verzeichnis finden
$texFiles = Get-ChildItem -Path .\ -Filter *.tex

# Array für fehlerhafte Kompilierungen
$failedCompilations = @()

foreach ($file in $texFiles) {
    $pdfFile = $file.BaseName + ".pdf"
    $pdfInDeutsch = Join-Path $deutschDir $pdfFile
    $pdfInEnglish = Join-Path $englishDir $pdfFile
    
    # Prüfen, ob PDF bereits existiert
    if ((Test-Path $pdfFile) -or (Test-Path $pdfInDeutsch) -or (Test-Path $pdfInEnglish)) {
        Write-Host "$($file.Name): PDF existiert bereits, überspringe Kompilierung." -ForegroundColor Gray
        continue
    }
    
    Write-Host "$($file.Name): Kompiliere mit LuaLaTeX..." -ForegroundColor Cyan
    
    # Zweimal kompilieren mit lualatex (für korrekte Referenzen, Inhaltsverzeichnis etc.)
    $compileSuccess = $true
    for ($i = 1; $i -le 2; $i++) {
        $process = Start-Process -FilePath "lualatex" `
            -ArgumentList "-interaction=nonstopmode", "-synctex=1", $file.Name `
            -NoNewWindow -Wait -PassThru -RedirectStandardOutput "latex_output.txt" -RedirectStandardError "latex_error.txt"
        
        if ($process.ExitCode -ne 0) {
            $compileSuccess = $false
            Write-Host "$($file.Name): Kompilierung fehlgeschlagen (Durchlauf $i)." -ForegroundColor Red
            break
        }
    }
    
    if (-not $compileSuccess) {
        $failedCompilations += $file.Name
        continue
    }
    
    # PDF-Datei verschieben
    if (Test-Path $pdfFile) {
        if ($file.Name -match "En\.tex$") {
            $destination = Join-Path $englishDir $pdfFile
            if (Test-Path $destination) { Remove-Item $destination -Force }
            Move-Item -Path $pdfFile -Destination $destination -Force
            Write-Host "$($file.Name): PDF nach English verschoben." -ForegroundColor Green
        } else {
            $destination = Join-Path $deutschDir $pdfFile
            if (Test-Path $destination) { Remove-Item $destination -Force }
            Move-Item -Path $pdfFile -Destination $destination -Force
            Write-Host "$($file.Name): PDF nach Deutsch verschoben." -ForegroundColor Green
        }
    } else {
        $failedCompilations += $file.Name
        Write-Host "$($file.Name): Kein PDF erzeugt." -ForegroundColor Red
    }
}

# Alle nicht-.tex und nicht-.ps1 Dateien löschen (Skript selbst und Verzeichnisse ausnehmen)
Get-ChildItem -Path .\ -Exclude *.tex, *.ps1, Deutsch, English | Remove-Item -Force -ErrorAction SilentlyContinue

# Fehlerhafte Kompilierungen ausgeben
if ($failedCompilations.Count -gt 0) {
    Write-Host "`nFolgende Dokumente konnten nicht fehlerfrei kompiliert werden:" -ForegroundColor Yellow
    $failedCompilations | ForEach-Object { Write-Host "  - $_" }
} else {
    Write-Host "`nAlle Dokumente wurden erfolgreich kompiliert oder übersprungen." -ForegroundColor Green
}