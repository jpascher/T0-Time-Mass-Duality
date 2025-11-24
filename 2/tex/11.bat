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
del /Q *.aux *.log *.bbl *.blg *.toc *.lof *.lot *.out *.idx *.ilg *.ind *.synctex.gz *.nav *.snm *.loa *.loe *.los 2>nul
del /Q *.fls *.fdb_latexmk 2>nul

rem altes Buch-PDF loeschen
del /Q "%TEXFILE:.tex=.pdf%" 2>nul

rem altes generiertes Buch-TeX loeschen
del /Q "%TEXFILE%" 2>nul

echo [CLEAN]>>"%LOGFILE%"

rem ==== 1) Kapitel mit 11.py erzeugen ====

if not exist "11.py" (
  echo [ERROR] 11.py fehlt>>"%LOGFILE%"
  echo 11.py fehlt.
  goto :EOF
)

echo [RUN] py 11.py>>"%LOGFILE%"
py 11.py >>"%LOGFILE%" 2>&1
if errorlevel 1 (
  echo [ERROR] 11.py ist mit Fehler beendet>>"%LOGFILE%"
  echo Fehler beim Ausführen von 11.py. Details siehe %LOGFILE%.
  goto :EOF
)

set BASENAME=%TEXFILE:.tex=%

rem ==== 2) LaTeX 1 ====

echo [RUN] pdflatex %TEXFILE%>>"%LOGFILE%"
pdflatex -interaction=nonstopmode "%TEXFILE%" >>"%LOGFILE%" 2>&1

echo.
echo === Zusammenfassung aus %LOGFILE% ===
findstr /R /C:"^!" /C:"^LaTeX Warning" /C:"^Package .* Warning" "%LOGFILE%"

endlocal