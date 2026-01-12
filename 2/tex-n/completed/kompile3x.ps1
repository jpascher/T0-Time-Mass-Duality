<#
.SYNOPSIS
    Kompiliert NUR die .tex-Dateien DIREKT im aktuellen Verzeichnis (keine Unterordner!)
    3× pdflatex, PDF bleibt im aktuellen Ordner, löscht temporäre Dateien

.NOTES
    - Speichern als z. B. kompile3x.ps1
    - pdflatex muss im PATH sein
#>

# Wichtig: Nur Dateien im aktuellen Verzeichnis (Tiefe 0)
$texFiles = Get-ChildItem -Path . -Filter *.tex -File -Depth 0

if ($texFiles.Count -eq 0) {
    Write-Host "Keine .tex-Dateien direkt im aktuellen Verzeichnis gefunden." -ForegroundColor Yellow
    exit
}

$failedCompilations = @()

foreach ($file in $texFiles) {
    $pdfFile = $file.BaseName + ".pdf"
    
    if (Test-Path $pdfFile) {
        Write-Host "$($file.Name): PDF existiert bereits → überspringe" -ForegroundColor Cyan
        continue
    }
    
    Write-Host "`n$($file.Name): Kompiliere (3× pdflatex)..." -ForegroundColor White
    
    $compileSuccess = $true
    
    for ($i = 1; $i -le 3; $i++) {
        Write-Host "  Lauf $i/3 ..." -NoNewline
        
        $process = Start-Process -FilePath "pdflatex" `
            -ArgumentList "-interaction=nonstopmode", "`"$($file.FullName)`"" `
            -NoNewWindow -Wait -PassThru `
            -RedirectStandardOutput "latex_output_$($file.BaseName)_$i.txt" `
            -RedirectStandardError "latex_error_$($file.BaseName)_$i.txt"
        
        if ($process.ExitCode -ne 0) {
            $compileSuccess = $false
            Write-Host " FEHLER!" -ForegroundColor Red
            break
        }
        Write-Host " OK" -ForegroundColor Green
    }
    
    if (-not $compileSuccess) {
        $failedCompilations += $file.Name
        Write-Host "→ Kompilierung fehlgeschlagen" -ForegroundColor Red
        continue
    }
    
    if (Test-Path $pdfFile) {
        Write-Host "→ PDF erfolgreich erstellt" -ForegroundColor Green
    } else {
        $failedCompilations += $file.Name
        Write-Host "→ Kein PDF erzeugt!" -ForegroundColor Red
    }
}

# Aufräumen
Write-Host "`nRäume temporäre Dateien auf..." -ForegroundColor DarkGray
Get-ChildItem -Path . `
    -Exclude *.tex, *.ps1 `
    -File `
    | Remove-Item -Force -ErrorAction SilentlyContinue

# Zusammenfassung
Write-Host "`n──────────────────────────────" -ForegroundColor DarkGray
if ($failedCompilations.Count -gt 0) {
    Write-Host "Folgende Dateien hatten Probleme:" -ForegroundColor Yellow
    $failedCompilations | ForEach-Object { Write-Host "  $_" }
} else {
    Write-Host "Alles erfolgreich durchgelaufen (oder bereits vorhanden)" -ForegroundColor Green
}