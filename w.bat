@echo off
cd /d %~dp0

:: ---------------------------
:: 1. .gitignore prüfen/erstellen
:: ---------------------------
if not exist .gitignore (
    echo *.aux > .gitignore
    echo *.log >> .gitignore
    echo *.out >> .gitignore
    echo *.synctex.gz >> .gitignore
    echo .gitignore erstellt mit Standard-LaTeX-Ausschlüssen.
)

:: ---------------------------
:: 2. Git-Status prüfen
:: ---------------------------
git status

:: ---------------------------
:: 3. Alte Version der Datei wiederherstellen
:: ---------------------------
:: Trage hier den Commit-Hash ein, der die alte Version enthält
set OLDCOMMIT=<hier_commit_hash_einfügen>
git checkout %OLDCOMMIT% -- T0-Charakteristische_Laengen.tex
echo Alte Version von T0-Charakteristische_Laengen.tex aus Commit %OLDCOMMIT% wiederhergestellt.

:: ---------------------------
:: 4. Alle Änderungen stage’n
:: ---------------------------
git add .
git add 2/html/

:: ---------------------------
:: 5. Commit und Push
:: ---------------------------
git diff --cached --quiet
if %errorlevel%==1 (
    git commit -m "Automatischer Commit: Änderungen im gesamten Repository und alte Version von T0-Charakteristische_Laengen.tex wiederhergestellt vom %date% %time%"
    git push origin main || (
        echo Fehler beim Pushen zum Repository.
        pause
        exit /b 1
    )
    echo Änderungen erfolgreich committet und gepusht.
) else (
    echo Keine Änderungen zum Commit vorhanden.
)

pause
