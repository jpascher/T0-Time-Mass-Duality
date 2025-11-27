@echo off
REM Compile all standalone LaTeX documents to PDF (Windows)
REM Usage: compile_all.bat [language]
REM Examples:
REM   compile_all.bat        - Compile all languages
REM   compile_all.bat en     - Compile only English
REM   compile_all.bat de     - Compile only German

setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"

if "%1"=="" (
    set "LANGUAGES=en de fr es it"
) else (
    set "LANGUAGES=%1"
)

echo T0 Standalone Document Compiler
echo ================================
echo.

for %%L in (%LANGUAGES%) do (
    call :compile_language %%L
)

echo ==========================================
echo Compilation complete!
echo ==========================================
goto :eof

:compile_language
set "LANG=%1"
set "LANG_DIR=%SCRIPT_DIR%%LANG%"

if not exist "%LANG_DIR%" (
    echo Directory %LANG_DIR% not found, skipping...
    goto :eof
)

echo ==========================================
echo Compiling %LANG% documents...
echo ==========================================

cd /d "%LANG_DIR%"

set /a count=0
set /a success=0
set /a failed=0

for %%F in (*.tex) do (
    set /a count+=1
    echo [!count!] Compiling %%F...
    
    pdflatex -interaction=nonstopmode "%%F" > nul 2>&1
    if !errorlevel! equ 0 (
        pdflatex -interaction=nonstopmode "%%F" > nul 2>&1
        set /a success+=1
        echo   Success: %%~nF.pdf
    ) else (
        set /a failed+=1
        echo   Failed: %%F
    )
    
    REM Clean up auxiliary files
    del /q "%%~nF.aux" "%%~nF.log" "%%~nF.out" "%%~nF.toc" "%%~nF.lof" "%%~nF.lot" "%%~nF.bbl" "%%~nF.blg" 2>nul
)

echo.
echo Results for %LANG%: !success! success, !failed! failed out of !count! files
echo.
goto :eof
