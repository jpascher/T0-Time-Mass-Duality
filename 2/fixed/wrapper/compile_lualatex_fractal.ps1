<#
.SYNOPSIS
    Kompiliert NUR die 30 geänderten fraktalen Korrekturdateien mit LuaLaTeX,
    verschiebt PDFs in Unterverzeichnisse (Deutsch/English) und löscht unnötige Dateien.

.NOTES
    - Starten: In PowerShell mit '.\compile_lualatex_fractal.ps1' ausführen.
    - Muss im Verzeichnis mit den Standalone-Wrappern (.tex) ausgeführt werden.
    - Die zugehörigen _ch.tex Dateien müssen im selben Verzeichnis liegen.
#>

# Liste der 30 geänderten Chapter-Dateien (ohne _ch.tex Suffix)
$changedFiles = @(
    "003_T0_Grundlagen_v1_En",
    "008_T0_xi-und-e_De",
    "008_T0_xi-und-e_En",
    "011_T0_Feinstruktur_En",
    "012_T0_Gravitationskonstante_De",
    "012_T0_Gravitationskonstante_En",
    "030_T0_penrose_De",
    "030_T0_penrose_En",
    "033_T0-Theory-vs-Synergetics_De",
    "033_T0-Theory-vs-Synergetics_En",
    "038_Markov_De",
    "038_Markov_En",
    "041_parameterherleitung_De",
    "041_parameterherleitung_En",
    "060_musical-spiral-137-_En",
    "070_Mathematische_struktur_De",
    "070_Mathematische_struktur_En",
    "086_T0_Dokumentenuebersicht_De",
    "086_T0_Dokumentenuebersicht_En",
    "089_Amper_Low_De",
    "089_Amper_Low_En",
    "124_Unit_Charge_En",
    "131_scheinbar_instantan_De",
    "131_scheinbar_instantan_En",
    "133_Fraktale_Korrektur_Herleitung_De",
    "133_Fraktale_Korrektur_Herleitung_En",
    "137_De",
    "137_En",
    "141_Renormierung_De",
    "141_Renormierung_En"
)

# Verzeichnisse erstellen, falls nicht vorhanden
$deutschDir = ".\Deutsch"
$englishDir = ".\English"
if (-not (Test-Path $deutschDir)) { New-Item -ItemType Directory -Path $deutschDir }
if (-not (Test-Path $englishDir)) { New-Item -ItemType Directory -Path $englishDir }

# Prüfen, ob LuaLaTeX verfügbar ist
if (-not (Get-Command lualatex -ErrorAction SilentlyContinue)) {
    Write-Host "FEHLER: LuaLaTeX nicht gefunden!" -ForegroundColor Red
    exit 1
}

# Array für fehlerhafte Kompilierungen
$failedCompilations = @()
$successCount = 0

Write-Host "`n=== Kompiliere $($changedFiles.Count) geaenderte Fraktal-Korrekturdateien ===" -ForegroundColor Yellow
Write-Host ""

foreach ($baseName in $changedFiles) {
    $texFile = "$baseName.tex"
    $pdfFile = "$baseName.pdf"
    
    # Prüfen ob Wrapper-Datei existiert
    if (-not (Test-Path $texFile)) {
        Write-Host "$texFile : Wrapper nicht gefunden, ueberspringe." -ForegroundColor DarkYellow
        $failedCompilations += "$texFile (Wrapper fehlt)"
        continue
    }
    
    # Prüfen ob Chapter-Datei existiert (im ch-Verzeichnis)
    $chFile = "..\ch\${baseName}_ch.tex"
    if (-not (Test-Path $chFile)) {
        Write-Host "$texFile : Chapter-Datei ${chFile} fehlt, ueberspringe." -ForegroundColor DarkYellow
        $failedCompilations += "$texFile (_ch.tex fehlt)"
        continue
    }
    
    # Vorhandenes PDF löschen (erzwingt Neukompilierung)
    $pdfInDeutsch = Join-Path $deutschDir $pdfFile
    $pdfInEnglish = Join-Path $englishDir $pdfFile
    if (Test-Path $pdfFile) { Remove-Item $pdfFile -Force }
    if (Test-Path $pdfInDeutsch) { Remove-Item $pdfInDeutsch -Force }
    if (Test-Path $pdfInEnglish) { Remove-Item $pdfInEnglish -Force }
    
    Write-Host "$texFile : Kompiliere mit LuaLaTeX..." -ForegroundColor Cyan
    
    # Zweimal kompilieren
    $compileSuccess = $true
    for ($i = 1; $i -le 2; $i++) {
        $process = Start-Process -FilePath "lualatex" `
            -ArgumentList "-interaction=nonstopmode", "-synctex=1", $texFile `
            -NoNewWindow -Wait -PassThru -RedirectStandardOutput "latex_output.txt" -RedirectStandardError "latex_error.txt"
        
        if ($process.ExitCode -ne 0) {
            $compileSuccess = $false
            Write-Host "$texFile : Kompilierung fehlgeschlagen (Durchlauf $i)." -ForegroundColor Red
            break
        }
    }
    
    if (-not $compileSuccess) {
        $failedCompilations += $texFile
        continue
    }
    
    # PDF-Datei verschieben
    if (Test-Path $pdfFile) {
        if ($texFile -match "En\.tex$") {
            $destination = Join-Path $englishDir $pdfFile
            if (Test-Path $destination) { Remove-Item $destination -Force }
            Move-Item -Path $pdfFile -Destination $destination -Force
            Write-Host "$texFile : PDF nach English verschoben." -ForegroundColor Green
        } else {
            $destination = Join-Path $deutschDir $pdfFile
            if (Test-Path $destination) { Remove-Item $destination -Force }
            Move-Item -Path $pdfFile -Destination $destination -Force
            Write-Host "$texFile : PDF nach Deutsch verschoben." -ForegroundColor Green
        }
        $successCount++
    } else {
        $failedCompilations += $texFile
        Write-Host "$texFile : Kein PDF erzeugt." -ForegroundColor Red
    }
}

# Aufräumen
Get-ChildItem -Path .\ -Include *.aux, *.log, *.out, *.toc, *.synctex.gz, *.fls, *.fdb_latexmk, latex_output.txt, latex_error.txt -Recurse | Remove-Item -Force -ErrorAction SilentlyContinue

# Zusammenfassung
Write-Host "`n=== Zusammenfassung ===" -ForegroundColor Yellow
Write-Host "Erfolgreich: $successCount / $($changedFiles.Count)" -ForegroundColor Green

if ($failedCompilations.Count -gt 0) {
    Write-Host "Fehlgeschlagen:" -ForegroundColor Red
    $failedCompilations | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
} else {
    Write-Host "Alle geaenderten Dokumente erfolgreich kompiliert!" -ForegroundColor Green
}
