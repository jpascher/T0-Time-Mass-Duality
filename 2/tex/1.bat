@echo off
cls
setlocal

set TEXFILE=T0_Book_En.tex
set LOGFILE=build_full.log

rem ==== 0) Komplett aufraeumen ====

rem altes Build-Log loeschen
del /Q "%LOGFILE%" 2>nul

rem generierte Kapitel loeschen
if exist "chapters_en" del /Q "chapters_en\*.tex" 2>nul

rem LaTeX-Hilfsdateien loeschen
del /Q *.aux *.log *.bbl *.blg *.toc *.lof *.lot *.out *.idx *.ilg *.ind *.synctex.gz *.nav *.snm *.loa *.loe *.los *.loe *.loe 2>nul
del /Q *.fls *.fdb_latexmk 2>nul

rem altes Buch-PDF loeschen
del /Q "%TEXFILE:.tex=.pdf%" 2>nul

rem altes generiertes Buch-TeX loeschen
del /Q "%TEXFILE%" 2>nul

echo [CLEAN]>>"%LOGFILE%"

rem ==== 1) Kapitel mit 1.py erzeugen ====

if not exist "1.py" (
  echo [ERROR] 1.py fehlt>>"%LOGFILE%"
  goto :EOF
)

python 1.py >>"%LOGFILE%" 2>&1
if errorlevel 1 (
  echo [ERROR] 1.py>>"%LOGFILE%"
  goto :EOF
)

set BASENAME=%TEXFILE:.tex=%

rem ==== 2) LaTeX 1 ====
pdflatex -interaction=nonstopmode "%TEXFILE%" >>"%LOGFILE%" 2>&1
findstr /R /C:"^!" /C:"^LaTeX Warning" /C:"^Package .* Warning" "%LOGFILE%"

rem ==== 3) BibTeX ====
rem bibtex "%BASENAME%" >>"%LOGFILE%" 2>&1

rem ==== 4) LaTeX 2 ====
rem pdflatex -interaction=nonstopmode "%TEXFILE%" >>"%LOGFILE%" 2>&1
rem findstr /R /C:"^!" /C:"^LaTeX Warning" /C:"^Package .* Warning" "%LOGFILE%"

rem ==== 5) LaTeX 3 ====
rem pdflatex -interaction=nonstopmode "%TEXFILE%" >>"%LOGFILE%" 2>&1
rem findstr /R /C:"^!" /C:"^LaTeX Warning" /C:"^Package .* Warning" "%LOGFILE%"

endlocal