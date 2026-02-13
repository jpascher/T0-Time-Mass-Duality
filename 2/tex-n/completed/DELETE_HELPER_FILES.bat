@echo off
REM ==================================================================
REM Loesche alte LaTeX Hilfsdateien (Fix fuer Counter too large)
REM ==================================================================

echo ===================================================================
echo LOESCHE ALTE LATEX HILFSDATEIEN
echo ===================================================================
echo.
echo Dieses Skript loescht:
echo   - .toc (Table of Contents mit alten Alph27, Alph28...)
echo   - .lot (List of Tables mit Counter-Problemen)
echo   - .lof (List of Figures)
echo   - .aux (Auxiliary Files)
echo   - .out (Hyperref Files)
echo.
echo WICHTIG: Fuehren Sie dies im gleichen Verzeichnis wie Teil3_En.tex aus!
echo.

pause

echo.
echo Loesche Hilfsdateien...
echo.

del /Q Teil3_En.toc 2>nul
del /Q Teil3_En.lot 2>nul
del /Q Teil3_En.lof 2>nul
del /Q Teil3_En.aux 2>nul
del /Q Teil3_En.out 2>nul

del /Q Teil3_De.toc 2>nul
del /Q Teil3_De.lot 2>nul
del /Q Teil3_De.lof 2>nul
del /Q Teil3_De.aux 2>nul
del /Q Teil3_De.out 2>nul

del /Q Teil2_En.toc 2>nul
del /Q Teil2_En.lot 2>nul
del /Q Teil2_En.lof 2>nul
del /Q Teil2_En.aux 2>nul
del /Q Teil2_En.out 2>nul

del /Q Teil2_De.toc 2>nul
del /Q Teil2_De.lot 2>nul
del /Q Teil2_De.lof 2>nul
del /Q Teil2_De.aux 2>nul
del /Q Teil2_De.out 2>nul

del /Q Teil1_En.toc 2>nul
del /Q Teil1_En.lot 2>nul
del /Q Teil1_En.lof 2>nul
del /Q Teil1_En.aux 2>nul
del /Q Teil1_En.out 2>nul

del /Q Teil1_De.toc 2>nul
del /Q Teil1_De.lot 2>nul
del /Q Teil1_De.lof 2>nul
del /Q Teil1_De.aux 2>nul
del /Q Teil1_De.out 2>nul

echo.
echo ===================================================================
echo FERTIG!
echo ===================================================================
echo.
echo Hilfsdateien geloescht. Kompilieren Sie jetzt neu:
echo   1. Oeffnen Sie Teil3_En.tex in TeXstudio
echo   2. Druecken Sie F5 (oder Build and View)
echo   3. Kompilieren Sie ZWEIMAL (fuer Referenzen)
echo.
echo Der Counter-too-large Fehler sollte jetzt weg sein!
echo.

pause
