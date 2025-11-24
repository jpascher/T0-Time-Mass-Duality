@echo off
setlocal enabledelayedexpansion

REM Compile T0 Books - English and German versions mit Logging
REM Dieses Skript kompiliert T0_Book_En.tex und T0_Book_De.tex

set LOGFILE=compile.log
echo ======================================== > "%LOGFILE%"
echo Kompilierung der T0 Buecher - Start: %date% %time% >> "%LOGFILE%"
echo Compiling T0 Books - Start: %date% %time% >> "%LOGFILE%"
echo ========================================

REM Ueberpruefe, ob pdflatex verfuegbar ist
where pdflatex >nul 2>nul
if %errorlevel% neq 0 (
    echo FEHLER: pdflatex wurde nicht gefunden! >> "%LOGFILE%"
    echo ERROR: pdflatex not found! >> "%LOGFILE%"
    echo.
    echo Bitte installieren Sie eine LaTeX-Distribution:
    echo Please install a LaTeX distribution:
    echo   - MiKTeX: https://miktex.org/
    echo   - TeX Live: https://tug.org/texlive/
    echo FEHLER: pdflatex wurde nicht gefunden! >> "%LOGFILE%"
    echo ERROR: pdflatex not found! >> "%LOGFILE%"
    pause
    exit /b 1
)

echo Gefunden: pdflatex >> "%LOGFILE%"
echo Found: pdflatex >> "%LOGFILE%"
echo.

REM Kompiliere englisches Buch
set TEXFILE=T0_Book_En.tex
echo ---------------------------------------- >> "%LOGFILE%"
echo Kompiliere englisches Buch... >> "%LOGFILE%"
echo Compiling English book... >> "%LOGFILE%"
echo ----------------------------------------
echo [RUN] pdflatex %TEXFILE% >> "%LOGFILE%"
pdflatex -interaction=nonstopmode "%TEXFILE%" >> "%LOGFILE%" 2>&1
if %errorlevel% neq 0 (
    echo WARNUNG: Erster Durchlauf mit Fehlern >> "%LOGFILE%"
    echo WARNING: First pass had errors >> "%LOGFILE%"
)
echo Zweiter Durchlauf fuer Referenzen... >> "%LOGFILE%"
echo Second pass for references... >> "%LOGFILE%"
echo [RUN] pdflatex %TEXFILE% >> "%LOGFILE%"
pdflatex -interaction=nonstopmode "%TEXFILE%" >> "%LOGFILE%" 2>&1
if exist T0_Book_En.pdf (
    echo.
    echo ERFOLG: T0_Book_En.pdf wurde erstellt!
    echo SUCCESS: T0_Book_En.pdf created! >> "%LOGFILE%"
) else (
    echo.
    echo FEHLER: T0_Book_En.pdf konnte nicht erstellt werden!
    echo ERROR: T0_Book_En.pdf could not be created! >> "%LOGFILE%"
)
echo.

REM Kompiliere deutsches Buch
set TEXFILE=T0_Book_De.tex
echo ---------------------------------------- >> "%LOGFILE%"
echo Kompiliere deutsches Buch... >> "%LOGFILE%"
echo Compiling German book... >> "%LOGFILE%"
echo ----------------------------------------
echo [RUN] pdflatex %TEXFILE% >> "%LOGFILE%"
pdflatex -interaction=nonstopmode "%TEXFILE%" >> "%LOGFILE%" 2>&1
if %errorlevel% neq 0 (
    echo WARNUNG: Erster Durchlauf mit Fehlern >> "%LOGFILE%"
    echo WARNING: First pass had errors >> "%LOGFILE%"
)
echo Zweiter Durchlauf fuer Referenzen... >> "%LOGFILE%"
echo Second pass for references... >> "%LOGFILE%"
echo [RUN] pdflatex %TEXFILE% >> "%LOGFILE%"
pdflatex -interaction=nonstopmode "%TEXFILE%" >> "%LOGFILE%" 2>&1
if exist T0_Book_De.pdf (
    echo.
    echo ERFOLG: T0_Book_De.pdf wurde erstellt!
    echo SUCCESS: T0_Book_De.pdf created! >> "%LOGFILE%"
) else (
    echo.
    echo FEHLER: T0_Book_De.pdf konnte nicht erstellt werden!
    echo ERROR: T0_Book_De.pdf could not be created! >> "%LOGFILE%"
)
echo.

REM Bereinige Hilfsdateien (Logs bleiben fuer Debugging)
echo ---------------------------------------- >> "%LOGFILE%"
echo Bereinige Hilfsdateien... >> "%LOGFILE%"
echo Cleaning up auxiliary files... >> "%LOGFILE%"
echo ----------------------------------------
del /Q T0_Book_*.aux T0_Book_*.log T0_Book_*.out T0_Book_*.toc 2>nul
echo ======================================== >> "%LOGFILE%"
echo Kompilierung abgeschlossen! - Ende: %date% %time% >> "%LOGFILE%"
echo Compilation completed! - End: %date% %time% >> "%LOGFILE%"
echo ========================================

echo.
echo ========================================
echo Kompilierung abgeschlossen!
echo Compilation completed!
echo ========================================
echo.
echo Erstellte PDFs:
echo Created PDFs:
if exist T0_Book_En.pdf echo   - T0_Book_En.pdf
if exist T0_Book_De.pdf echo   - T0_Book_De.pdf
echo.
echo Log-Datei: %LOGFILE% (oeffnen Sie sie fuer Details)
echo Log file: %LOGFILE% (open it for details)
echo.

pause