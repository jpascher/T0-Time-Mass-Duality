@echo off
REM Compile T0 Book LaTeX files to PDF
REM Usage: compile_books.bat [book1|book2|book3|all|clean|help]
REM
REM Examples:
REM   compile_books.bat          - Compile all three books
REM   compile_books.bat book1    - Compile T0_Book1_En.tex only
REM   compile_books.bat book2    - Compile T0_Book_En.tex only
REM   compile_books.bat book3    - Compile T0_Book3_En.tex only
REM   compile_books.bat clean    - Remove auxiliary files

setlocal enabledelayedexpansion

REM Change to script directory
cd /d "%~dp0"

REM Book file definitions
set "BOOK1=T0_Book1_En.tex"
set "BOOK2=T0_Book_En.tex"
set "BOOK3=T0_Book3_En.tex"

if "%1"=="" goto all
if "%1"=="all" goto all
if "%1"=="book1" goto book1
if "%1"=="book2" goto book2
if "%1"=="book3" goto book3
if "%1"=="clean" goto clean
if "%1"=="help" goto help
if "%1"=="--help" goto help
if "%1"=="-h" goto help

echo Unknown option: %1
goto help

:book1
call :compile_book %BOOK1%
goto end

:book2
call :compile_book %BOOK2%
goto end

:book3
call :compile_book %BOOK3%
goto end

:all
echo Compiling all T0 Books...
echo.
call :compile_book %BOOK1%
echo.
call :compile_book %BOOK2%
echo.
call :compile_book %BOOK3%
echo.
echo All books compiled successfully!
goto end

:clean
echo Cleaning auxiliary files...
del /q *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz 2>nul
echo Done.
goto end

:help
echo T0 Book Compilation Script
echo.
echo Usage: %~nx0 [OPTION]
echo.
echo Options:
echo   book1       Compile T0_Book1_En.tex (comprehensive, ~580 pages)
echo   book2       Compile T0_Book_En.tex (original, ~88 pages)
echo   book3       Compile T0_Book3_En.tex (no boxes, ~526 pages)
echo   all         Compile all three books (default)
echo   clean       Remove auxiliary files (.aux, .log, .out, .toc, etc.)
echo   help        Show this help message
echo.
echo Examples:
echo   %~nx0              - Compile all books
echo   %~nx0 book1        - Compile comprehensive book only
echo   %~nx0 clean        - Clean up auxiliary files
goto end

:compile_book
set "book_file=%~1"
set "book_name=%~n1"

if not exist "%book_file%" (
    echo Error: %book_file% not found
    exit /b 1
)

echo Compiling %book_file%...
echo   Pass 1/2...
pdflatex -interaction=nonstopmode "%book_file%" >nul 2>&1
if errorlevel 1 (
    echo   Error in first pass. Running with output...
    pdflatex -interaction=nonstopmode "%book_file%"
    exit /b 1
)

echo   Pass 2/2...
pdflatex -interaction=nonstopmode "%book_file%" >nul 2>&1
if errorlevel 1 (
    echo   Error in second pass. Running with output...
    pdflatex -interaction=nonstopmode "%book_file%"
    exit /b 1
)

echo   Success: %book_name%.pdf
exit /b 0

:end
endlocal
