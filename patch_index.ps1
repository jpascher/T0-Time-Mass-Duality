# patch_index.ps1
# PowerShell Patch Script für automatisches Kopieren der Index-Dateien
# Ausführung: .\patch_index.ps1

Write-Host "PowerShell T0-Framework Index Patch Script" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan

# Aktuelle Verzeichnisse definieren
$currentDir = Get-Location
$userProfile = [Environment]::GetFolderPath("UserProfile")
$downloadsDir = Join-Path $userProfile "Downloads"
$targetRoot = $currentDir  # Root-Verzeichnis (aktuelles Verzeichnis)
$targetDir2 = Join-Path $currentDir "2"
$targetDirHtml = Join-Path $currentDir "2\html"

Write-Host "Aktuelles Verzeichnis: $currentDir" -ForegroundColor Yellow
Write-Host "User Profile: $userProfile" -ForegroundColor Yellow
Write-Host "Download-Verzeichnis: $downloadsDir" -ForegroundColor Yellow
Write-Host "Ziel Root (.): $targetRoot" -ForegroundColor Yellow
Write-Host "Ziel ./2: $targetDir2" -ForegroundColor Yellow
Write-Host "Ziel ./2/html: $targetDirHtml" -ForegroundColor Yellow

# Prüfe ob Downloads-Verzeichnis existiert
if (-not (Test-Path $downloadsDir)) {
    Write-Host "FEHLER: Downloads-Verzeichnis nicht gefunden!" -ForegroundColor Red
    Write-Host "Versucht: $downloadsDir" -ForegroundColor Red
    
    # Alternative: Suche im aktuellen Verzeichnis
    $alternativeSource = Join-Path $currentDir "index.html"
    if (Test-Path $alternativeSource) {
        Write-Host "Alternative gefunden: index.html im aktuellen Verzeichnis" -ForegroundColor Yellow
        $downloadsDir = $currentDir
    } else {
        Write-Host "Keine index.html gefunden. Bitte lege die Datei in eines dieser Verzeichnisse:" -ForegroundColor Red
        Write-Host "  1. $downloadsDir" -ForegroundColor Yellow
        Write-Host "  2. $currentDir" -ForegroundColor Yellow
        exit 1
    }
}

# Suche nach index.html im Downloads-Verzeichnis
$sourceFile = Join-Path $downloadsDir "index.html"
if (-not (Test-Path $sourceFile)) {
    Write-Host "FEHLER: index.html nicht gefunden!" -ForegroundColor Red
    Write-Host "Gesuchte Datei: $sourceFile" -ForegroundColor Red
    
    # Liste alle HTML-Dateien im Downloads-Verzeichnis auf
    Write-Host "Verfügbare HTML-Dateien im Downloads-Verzeichnis:" -ForegroundColor Yellow
    Get-ChildItem $downloadsDir -Filter "*.html" | ForEach-Object {
        Write-Host "  - $($_.Name)" -ForegroundColor Green
    }
    exit 1
}

Write-Host "OK: Quelldatei gefunden: $sourceFile" -ForegroundColor Green

# Zeige Dateigröße
$sourceSize = (Get-Item $sourceFile).Length
Write-Host "Dateigröße: $sourceSize bytes" -ForegroundColor Cyan

# Erstelle Zielverzeichnisse falls sie nicht existieren
if (-not (Test-Path $targetDir2)) {
    New-Item -ItemType Directory -Path $targetDir2 -Force | Out-Null
    Write-Host "Verzeichnis ./2 erstellt" -ForegroundColor Green
}

if (-not (Test-Path $targetDirHtml)) {
    New-Item -ItemType Directory -Path $targetDirHtml -Force | Out-Null
    Write-Host "Verzeichnis ./2/html erstellt" -ForegroundColor Green
}

try {
    # Kopiere index.html ins Root-Verzeichnis (.)
    $targetRoot = Join-Path $currentDir "index.html"
    Copy-Item $sourceFile $targetRoot -Force
    Write-Host "OK: index.html nach ./index.html kopiert (ROOT)" -ForegroundColor Green

    # Kopiere index.html nach ./2/
    $target1 = Join-Path $targetDir2 "index.html"
    Copy-Item $sourceFile $target1 -Force
    Write-Host "OK: index.html nach ./2/index.html kopiert" -ForegroundColor Green

    # Kopiere index.html nach ./2/html/
    $target2 = Join-Path $targetDirHtml "index.html"
    Copy-Item $sourceFile $target2 -Force
    Write-Host "OK: index.html nach ./2/html/index.html kopiert" -ForegroundColor Green

    # Kopiere als website.html nach ./2/
    $target3 = Join-Path $targetDir2 "website.html"
    Copy-Item $sourceFile $target3 -Force
    Write-Host "OK: index.html nach ./2/website.html kopiert" -ForegroundColor Green

    Write-Host "" -ForegroundColor White
    Write-Host "PATCH ERFOLGREICH ABGESCHLOSSEN!" -ForegroundColor Green
    Write-Host "================================================" -ForegroundColor Cyan
    Write-Host "Zusammenfassung:" -ForegroundColor Yellow
    Write-Host "  [OK] ./index.html (ROOT)" -ForegroundColor Green
    Write-Host "  [OK] ./2/index.html" -ForegroundColor Green
    Write-Host "  [OK] ./2/html/index.html" -ForegroundColor Green  
    Write-Host "  [OK] ./2/website.html" -ForegroundColor Green
    Write-Host "" -ForegroundColor White
    Write-Host "Die Website-Dateien sind jetzt synchronisiert!" -ForegroundColor Cyan

} catch {
    Write-Host "FEHLER beim Kopieren der Dateien:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}

# Optionale Verifikation
Write-Host "" -ForegroundColor White
Write-Host "Verifikation der kopierten Dateien:" -ForegroundColor Yellow

$files = @(
    (Join-Path $currentDir "index.html"),
    (Join-Path $targetDir2 "index.html"),
    (Join-Path $targetDirHtml "index.html"),
    (Join-Path $targetDir2 "website.html")
)

foreach ($file in $files) {
    if (Test-Path $file) {
        $size = (Get-Item $file).Length
        $relativePath = $file.Replace($currentDir, ".")
        Write-Host "  [OK] $relativePath ($size bytes)" -ForegroundColor Green
    } else {
        Write-Host "  [FEHLER] $file (nicht gefunden)" -ForegroundColor Red
    }
}

Write-Host "" -ForegroundColor White
Write-Host "Patch abgeschlossen. Druecke Enter zum Beenden..." -ForegroundColor Cyan
Read-Host