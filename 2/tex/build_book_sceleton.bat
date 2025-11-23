@echo off
REM Skeleton-Build für das englische Buch (nutzt 1_sceleton.py)

cd /d "%~dp0"
py 1_sceleton.py
if errorlevel 1 (
  echo [ERROR] 1_sceleton.py ist fehlgeschlagen.
  exit /b 1
)

pdflatex -interaction=nonstopmode T0_Book_En_sceleton.tex
