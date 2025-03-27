@echo off
cd /d %~dp0
git status
git add .
git commit -m "Neue Dateien hinzugefügt und Änderungen übernommen"
git push
pause
