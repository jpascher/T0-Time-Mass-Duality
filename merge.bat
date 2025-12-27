@echo off
echo ============================================
echo      Git Delete/Merge Conflict Resolver
echo ============================================
echo.
echo AKTUELLER STATUS:
echo - 2/tex/en_standalone/003_T0_Grundlagen_En.tex: "deleted by us"
echo - 2/pdf/111_T0_Grundlagen_En.pdf: gelöscht (unstaged)
echo - 2/tex/en_standalone/003_T0_Grundlagen_En.pdf: neu (untracked)
echo.
echo.

echo WÄHLE EINE OPTION:
echo [1] Datei löschen (behalte "deleted by us" - lösche aus merge)
echo [2] Datei wiederherstellen (behalte Version aus anderem Branch)
echo [3] Merge komplett abbrechen
echo [4] Status anzeigen
echo.

set /p choice="Deine Wahl (1-4): "

if "%choice%"=="1" (
    echo.
    echo OPTION 1: Datei löschen...
    echo Dies bestätigt die Löschung der Datei.
    git rm "2/tex/en_standalone/003_T0_Grundlagen_En.tex"
    
    echo Merge fortsetzen...
    git commit -m "Resolve delete conflict: remove 003_T0_Grundlagen_En.tex"
    
    echo Auf main wechseln...
    git checkout main
    
    echo Push durchführen...
    git push origin main
    
    echo.
    echo ✅ Datei gelöscht und Merge abgeschlossen!
    
) else if "%choice%"=="2" (
    echo.
    echo OPTION 2: Datei wiederherstellen...
    echo Dies holt die Datei aus dem anderen Branch zurück.
    
    echo Merge abbrechen und Datei wiederherstellen...
    git merge --abort
    
    echo Zurück zu main...
    git checkout main
    
    echo Datei aus anderem Branch holen...
    git checkout copilot/standardize-latex-documents-another-one -- "2/tex/en_standalone/003_T0_Grundlagen_En.tex"
    
    echo Änderungen committen...
    git add "2/tex/en_standalone/003_T0_Grundlagen_En.tex"
    git commit -m "Restore 003_T0_Grundlagen_En.tex from copilot branch"
    
    echo Push durchführen...
    git push origin main
    
    echo.
    echo ✅ Datei wiederhergestellt und gepusht!
    
) else if "%choice%"=="3" (
    echo.
    echo OPTION 3: Merge abbrechen...
    git merge --abort
    git checkout main
    echo ✅ Merge abgebrochen, zurück auf main.
    
) else if "%choice%"=="4" (
    echo.
    echo OPTION 4: Detaillierter Status...
    git status --verbose
) else (
    echo.
    echo ❌ Ungültige Auswahl.
)

echo.
echo Drücke eine beliebige Taste zum Beenden...
pause > nul