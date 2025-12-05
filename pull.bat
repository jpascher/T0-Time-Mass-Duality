@echo off
echo ======================================
echo    Safe Latex Workflow Branch Switch
echo ======================================

setlocal enabledelayedexpansion

echo 1. Sichere lokale Änderungen...
call :push_current_changes

echo.
echo 2. Hole neueste Branches von GitHub...
git fetch origin

echo.
echo 3. Wechsle zu Latex Workflow Branch...
git checkout -b copilot/add-latex-build-workflow origin/copilot/add-latex-build-workflow

if errorlevel 1 (
    echo.
    echo ❌ Fehler! Verfügbare Latex-Branches:
    git branch -r | findstr /i "latex"
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Erfolg! Du bist jetzt auf: copilot/add-latex-build-workflow
git branch --show-current
echo.
echo Branch-Inhalt:
dir /b
pause
exit /b

:push_current_changes
REM Funktion: Pushe aktuelle Änderungen
for /f "tokens=*" %%a in ('git symbolic-ref --short HEAD') do set branch=%%a

git status --porcelain | findstr "." >nul
if not errorlevel 1 (
    echo ⚠️  Ungespeicherte Änderungen auf %branch% gefunden!
    echo.
    git add .
    git commit -m "Auto-save: Lokale Änderungen vor Branch-Wechsel"
    echo.
)

git log --oneline origin/!branch!..!branch! | findstr "." >nul
if not errorlevel 1 (
    echo 📤 Pushe Commits zu origin/!branch!...
    git push origin !branch!
    echo ✅ Gepusht.
)
goto :eof