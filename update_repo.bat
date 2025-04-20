@echo off
cd /d %~dp0
git status
git add .
git diff --cached --quiet
if %errorlevel%==1 (
    git commit -m "Neue Dateien hinzugefügt und Änderungen übernommen"
    git push
) else (
    echo Keine Änderungen zum Commit vorhanden.
)
pause
