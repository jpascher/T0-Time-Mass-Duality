
# Skript zum Starten von OneDrive

# Pfad zu OneDrive
$OneDrivePath = "$env:LOCALAPPDATA\Microsoft\OneDrive\OneDrive.exe"

# Überprüfen, ob die Datei existiert
if (Test-Path $OneDrivePath) {
    # OneDrive starten
    Write-Host "Starte OneDrive..."
    & $OneDrivePath
    Write-Host "OneDrive wurde erfolgreich gestartet!"
} else {
    # Fehlermeldung, falls der Pfad nicht gefunden wird
    Write-Host "OneDrive.exe wurde nicht gefunden. Bitte prüfen Sie den Installationspfad." -ForegroundColor Red
}
