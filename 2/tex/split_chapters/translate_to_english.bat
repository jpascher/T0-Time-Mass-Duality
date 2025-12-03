@echo off
REM ============================================================
REM T0 LaTeX Translation Script - German to English
REM Verwendet Microsoft Azure Translator API
REM ============================================================

setlocal enabledelayedexpansion

REM === KONFIGURATION ===
set "KEY=5OfPzHviDzSPW4inYDJ3uokfadGiGTo1hQustQAnopshEU1zRW0mJQQJ99BLAC5RqLJXJ3w3AAAbACOGl4nH"
set "ENDPOINT=https://api.cognitive.microsofttranslator.com"
set "REGION=global"

REM Wechsle ins Verzeichnis mit den LaTeX-Dateien
cd /d "%~dp0"

echo ============================================================
echo T0 LaTeX Uebersetzung: Deutsch - Englisch
echo ============================================================
echo.

REM Zaehler
set /a count=0
set /a success=0
set /a failed=0

REM Erstelle Ausgabeverzeichnis
if not exist "translated" mkdir translated

REM Durchlaufe alle deutschen LaTeX-Dateien
for %%f in (*_De.tex) do call :process "%%f"

REM Aufraeumen
del temp_de.txt 2>nul
del temp_request.json 2>nul
del temp_response.json 2>nul

echo.
echo ============================================================
echo Fertig!
echo Gesamt: %count% Dateien
echo Erfolgreich: %success%
echo Fehlgeschlagen: %failed%
echo.
echo Uebersetzte Texte in: translated\
echo ============================================================

pause
goto :eof

:process
set /a count+=1
set "fullname=%~1"
set "filename=%~n1"
set "basename=!filename:_De=!"

echo [!count!] Uebersetze: %fullname%

REM 1. Text extrahieren mit pandoc
pandoc "%fullname%" -t plain -o "temp_de.txt" 2>nul

if not exist "temp_de.txt" (
    echo     FEHLER: Konnte Text nicht extrahieren
    set /a failed+=1
    goto :eof
)

REM 2. Text lesen und fuer JSON vorbereiten
set "text="
for /f "usebackq delims=" %%a in ("temp_de.txt") do (
    set "line=%%a"
    set "line=!line:\=\\!"
    set "line=!line:"=\"!"
    set "text=!text!!line! "
)

REM 3. API-Aufruf mit curl
echo [{"Text":"!text!"}]> temp_request.json

curl -s -X POST "%ENDPOINT%/translate?api-version=3.0&from=de&to=en" -H "Ocp-Apim-Subscription-Key: %KEY%" -H "Ocp-Apim-Subscription-Region: %REGION%" -H "Content-Type: application/json; charset=UTF-8" -d @temp_request.json -o temp_response.json

REM 4. Uebersetzung extrahieren
jq -r ".[0].translations[0].text" temp_response.json > "translated\!basename!_En_translated.txt" 2>nul

if exist "translated\!basename!_En_translated.txt" (
    echo     OK: translated\!basename!_En_translated.txt
    set /a success+=1
) else (
    echo     FEHLER: Uebersetzung fehlgeschlagen
    set /a failed+=1
)

goto :eof
