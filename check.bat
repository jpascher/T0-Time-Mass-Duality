@echo off
echo Git Push-Prozess startet...
echo.

echo 1. Git Status:
git status
echo.

echo 2. Pull von GitHub...
git pull origin main
echo.

echo 3. Push zu GitHub...
git push origin main
echo.

if %errorlevel% equ 0 (
    echo Erfolgreich gepusht!
) else (
    echo Fehler beim Pushen!
)
pause