@echo off
setlocal enabledelayedexpansion

:: Wechsel ins Repository
cd /d %~dp0

:: Prüfen, ob Git-Repo vorhanden
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo Fehler: Kein Git-Repository im aktuellen Verzeichnis!
    pause
    exit /b 1
)

:: Datei prüfen
set FILE=T0-Charakteristische_Laengen.tex
echo Letzte Commits der Datei %FILE%:
git log --all --pretty=format:"%%h %%ad %%s" --date=short -- %FILE% > temp_commits.txt

:: Prüfen, ob überhaupt Commits vorhanden
for /f %%i in (temp_commits.txt) do set hascommits=1
if not defined hascommits (
    echo Keine Commits für %FILE% gefunden!
    del temp_commits.txt
    pause
    exit /b 1
)

:: Liste anzeigen und in Variablen speichern
set count=0
for /f "tokens=*" %%a in (temp_commits.txt) do (
    set /a count+=1
    echo [!count!] %%a
    set hash[!count!]=%%a
)

del temp_commits.txt

:: Auswahl des Commits
set /p choice=Gib die Nummer des Commits ein, den du wiederherstellen willst: 
set commit=!hash[%choice%]!
for /f "tokens=1" %%h in ("!commit!") do set commithash=%%h

if "%commithash%"=="" (
    echo Ungültige Auswahl!
    pause
    exit /b 1
)

:: Datei aus altem Commit wiederherstellen
git checkout %commithash% -- %FILE%
if errorlevel 1 (
    echo Fehler beim Wiederherstellen der Datei!
    pause
    exit /b 1
)
echo Datei %FILE% aus Commit %commithash% wiederhergestellt.

:: Commit erstellen (Revert)
git add %FILE%
git commit -m "Revert: Alte Version von %FILE% aus Commit %commithash% wiederhergestellt"
git push origin main
echo Fertig! Alte Version erfolgreich wiederhergestellt und gepusht.

pause
