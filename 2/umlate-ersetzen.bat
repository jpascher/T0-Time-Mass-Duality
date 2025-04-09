@echo off
setlocal enabledelayedexpansion

REM URL-kodierte Entsprechungen der deutschen Umlaute
set "ae=%C3%A4"
set "oe=%C3%B6"
set "ue=%C3%BC"
set "Ae=%C3%84"
set "Oe=%C3%96"
set "Ue=%C3%9C"
set "sz=%C3%9F"

REM Durchsuche gezielt die beiden Unterverzeichnisse
for /R pdf\Deutsch %%f in (*.tex) do call :processFile "%%f"
for /R pdf\English %%f in (*.tex) do call :processFile "%%f"

echo.
echo Fertig!
pause
exit /b

:processFile
set "file=%~1"
echo Bearbeite Datei: %file%

REM Temporäre Datei
set "tmpfile=%file%.tmp"

REM Datei Zeile für Zeile verarbeiten
> "%tmpfile%" (
    for /f "usebackq delims=" %%l in ("%file%") do (
        set "line=%%l"

        REM Wenn die Zeile eine .jpg enthält, ersetze Umlaute
        echo !line! | findstr /i ".jpg" >nul
        if !errorlevel! == 0 (
            set "line=!line:ä=%ae%!"
            set "line=!line:ö=%oe%!"
            set "line:ü=%ue%!"
            set "line=!line:Ä=%Ae%!"
            set "line=!line:Ö=%Oe%!"
            set "line=!line:Ü=%Ue%!"
            set "line=!line:ß=%sz%!"
        )

        echo(!line!
    )
)

REM Originaldatei überschreiben
move /Y "%tmpfile%" "%file%" >nul
exit /b
