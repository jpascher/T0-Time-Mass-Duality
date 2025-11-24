@echo off
REM Compile T0 Books - English and German versions
REM This script compiles both T0_Book_En.tex and T0_Book_De.tex

echo ========================================
echo Kompilierung der T0 Bücher
echo Compiling T0 Books
echo ========================================
echo.

REM Check if pdflatex is available
where pdflatex >nul 2>nul
if %errorlevel% neq 0 (
    echo FEHLER: pdflatex wurde nicht gefunden!
    echo ERROR: pdflatex not found!
    echo.
    echo Bitte installieren Sie eine LaTeX-Distribution:
    echo Please install a LaTeX distribution:
    echo   - MiKTeX: https://miktex.org/
    echo   - TeX Live: https://tug.org/texlive/
    pause
    exit /b 1
)

echo Gefunden: pdflatex
echo Found: pdflatex
echo.

REM Compile English book
echo ----------------------------------------
echo Kompiliere englisches Buch...
echo Compiling English book...
echo ----------------------------------------
pdflatex -interaction=nonstopmode T0_Book_En.tex
if %errorlevel% neq 0 (
    echo WARNUNG: Erster Durchlauf mit Fehlern
    echo WARNING: First pass had errors
)
echo Zweiter Durchlauf für Referenzen...
echo Second pass for references...
pdflatex -interaction=nonstopmode T0_Book_En.tex

if exist T0_Book_En.pdf (
    echo.
    echo ERFOLG: T0_Book_En.pdf wurde erstellt!
    echo SUCCESS: T0_Book_En.pdf created!
) else (
    echo.
    echo FEHLER: T0_Book_En.pdf konnte nicht erstellt werden!
    echo ERROR: T0_Book_En.pdf could not be created!
)
echo.

REM Compile German book
echo ----------------------------------------
echo Kompiliere deutsches Buch...
echo Compiling German book...
echo ----------------------------------------
pdflatex -interaction=nonstopmode T0_Book_De.tex
if %errorlevel% neq 0 (
    echo WARNUNG: Erster Durchlauf mit Fehlern
    echo WARNING: First pass had errors
)
echo Zweiter Durchlauf für Referenzen...
echo Second pass for references...
pdflatex -interaction=nonstopmode T0_Book_De.tex

if exist T0_Book_De.pdf (
    echo.
    echo ERFOLG: T0_Book_De.pdf wurde erstellt!
    echo SUCCESS: T0_Book_De.pdf created!
) else (
    echo.
    echo FEHLER: T0_Book_De.pdf konnte nicht erstellt werden!
    echo ERROR: T0_Book_De.pdf could not be created!
)
echo.

REM Clean up auxiliary files
echo ----------------------------------------
echo Bereinige Hilfsdateien...
echo Cleaning up auxiliary files...
echo ----------------------------------------
del /Q T0_Book_*.aux T0_Book_*.log T0_Book_*.out T0_Book_*.toc 2>nul

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

pause
