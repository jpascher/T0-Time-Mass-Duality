@echo off
cd /d %~dp0

:: Überprüfe, ob .gitignore existiert, und erstelle eine, falls nicht vorhanden
if not exist .gitignore (
    echo *.aux > .gitignore
    echo *.log >> .gitignore
    echo *.out >> .gitignore
    echo *.synctex.gz >> .gitignore
    echo .gitignore erstellt mit Standard-LaTeX-Ausschlüssen.
)

:: Überprüfe Git-Status vor dem Staging
echo.
echo === Aktueller Git Status vor dem Staging ===
git status
echo.

:: Stage alle Änderungen im gesamten Repository
git add .

:: Stelle sicher, dass das Unterverzeichnis explizit geaddet wird (inklusive neuer Dateien)
:: Dies ist nach git add . oft redundant, schadet aber nicht.
git add 2/html/

:: Prüfe, ob es gestagte Änderungen gibt
git diff --cached --quiet
if %errorlevel%==1 (
    echo === Änderungen zum Commit vorhanden ===

    :: Optional: Erst pullen, um Konflikte zu vermeiden
    echo Versuche, Änderungen vom Remote zu holen (git pull)...
    git pull origin main || (
        echo Fehler beim 'git pull'. Bitte manuelle Konflikte lösen.
        pause
        exit /b 1
    )

    :: Commit mit detaillierter Nachricht
    git commit -m "Automatischer Commit: Änderungen im gesamten Repository und explizites Update für 2/html/ vom %date% %time%" || (
        echo Fehler beim Erstellen des Commits.
        pause
        exit /b 1
    )

    :: Push mit Fehlerbehandlung
    echo Versuche, Änderungen zum Remote zu pushen (git push)...
    git push origin main || (
        echo Fehler beim Pushen zum Repository. Möglicherweise musst du Konflikte manuell lösen.
        pause
        exit /b 1
    )
    echo.
    echo === Änderungen erfolgreich committet und gepusht. ===
) else (
    echo.
    echo === Keine Änderungen zum Commit vorhanden. ===
)

pause