@echo off
echo ========================================
echo Git Push Skript - Lokale Aenderungen pushen
echo ========================================
echo.

REM Aktuellen Status anzeigen
echo --- Git Status ---
git status
echo.

REM Alle Aenderungen adden
echo --- Aenderungen werden gestaged ---
git add .
echo.

REM Commit-Nachricht abfragen (interaktiv)
set /p commit_msg="Commit-Nachricht eingeben: "
if "%commit_msg%"=="" set commit_msg=Standardized LaTeX documents (local einge latex hinzugefügt)

REM Commit ausfuehren
echo --- Commit wird erstellt ---
git commit -m "%commit_msg%"
echo.

REM Push zum Remote-Branch
echo --- Push zu origin/copilot/standardize-latex-documents ---
git push origin copilot/standardize-latex-documents-another-one
echo.

echo ========================================
echo Fertig! Ueberpruefe ggf. mit 'git log --oneline'
echo ========================================
pause