@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: Pruefe, ob es ein Git-Repo ist
if not exist .git (
    echo Fehler: Dies ist kein Git-Repository. Wechsle in das Repo-Verzeichnis.
    pause
    exit /b 1
)

:: Hole aktuellen Branch
for /f %%i in ('git branch --show-current') do set current_branch=%%i
if "%current_branch%"=="" (
    echo Fehler: Kein aktueller Branch gefunden.
    pause
    exit /b 1
)

:menu
cls
echo ================================
echo Branch-Management Script (aktueller Branch: %current_branch%)
echo Hinweis: PDFs werden NICHT hochgeladen (kein .gitignore geaendert).
echo ================================
echo 1. Hart auschecken (hard reset auf origin/%current_branch%)
echo 2. Lokalen Inhalt adden (2/tex/ oder alles ausser PDFs - egal wo PDFs sind)
echo 3. Commit (im aktuellen Branch)
echo 4. Hochladen (push in %current_branch%)
echo 5. Commit in main (alles ausser PDFs - lokaler Branch bleibt unveraendert)
echo 6. Exit
echo ================================
set /p choice="Waehle eine Option (1-6): "

if "%choice%"=="1" goto hard_checkout
if "%choice%"=="2" goto add_content
if "%choice%"=="3" goto commit
if "%choice%"=="4" goto upload
if "%choice%"=="5" goto commit_to_main
if "%choice%"=="6" goto end
echo Ungueltige Wahl. Druecke Enter.
pause
goto menu

:hard_checkout
echo Aktueller Branch: %current_branch%
set /p confirm="Sicher hart auschecken (hard reset auf origin/%current_branch%)? Lokale Aenderungen gehen verloren! (y/n): "
if /i not "%confirm%"=="y" (
    echo Abgebrochen.
    pause
    goto menu
)
echo Fuhre fetch aus...
git fetch origin
if errorlevel 1 (
    echo Fehler beim fetch. Git-Output:
    git status
    pause
    goto menu
)
echo Fuhre hard reset aus...
git reset --hard "origin/%current_branch%"
if errorlevel 1 (
    echo Fehler beim hard reset. Git-Output:
    git status
    pause
) else (
    echo Erfolg: Branch %current_branch% hart ausgecheckt auf origin/%current_branch%. Lokale Aenderungen verworfen.
    git log --oneline -1
)
pause
goto menu

:add_content
echo Was adden? (PDFs werden NICHT hinzugefuegt - egal wo sie sind)
echo 1. 2/tex/
echo 2. Alles ausser PDFs (git add --all && git reset HEAD *.pdf)
set /p add_choice="Waehle (1-2): "
if "%add_choice%"=="1" (
    echo Fuege 2/tex/ hinzu...
    git add 2/tex/
    echo Erfolg: 2/tex/ hinzugefuegt.
) else if "%add_choice%"=="2" (
    echo Fuege alles hinzu und entferne PDFs aus Index...
    git add --all
    git reset HEAD *.pdf
    echo Erfolg: Alles ausser .pdf-Dateien hinzugefuegt.
) else (
    echo Ungueltig. Druecke Enter.
    pause
    goto menu
)
echo Aktueller Status:
git status --short
pause
goto menu

:commit
set /p message="Commit-Message: "
echo Fuhre Commit im Branch %current_branch% aus...
git commit -m "%message%"
if errorlevel 1 (
    echo Fehler beim Commit. Git-Output:
    git status
    pause
) else (
    echo Erfolg: Commit im Branch %current_branch% erstellt mit Message "%message%".
    git log --oneline -1
)
pause
goto menu

:upload
echo Fuhre Push aus...
git push origin "%current_branch%"
if errorlevel 1 (
    echo Fehler beim Push. Git-Output:
    git status
    pause
) else (
    echo Erfolg: Branch %current_branch% erfolgreich hochgeladen (gepusht).
    git log --oneline -1
)
pause
goto menu

:commit_to_main
set /p message="Commit-Message fuer main: "
echo Stashe lokale Aenderungen (falls vorhanden)...
git stash push -m "Temp stash for main commit"
echo Wechsle zu main...
git checkout main
if errorlevel 1 (
    echo Fehler beim Wechsel zu main. Git-Output:
    git status
    pause
    goto menu
)
echo Fuege alles ausser PDFs in main hinzu (PDFs nur aus 2/pdf/)...
git add --all
git reset HEAD *.pdf
echo Fuhre Commit in main aus...
git commit -m "%message%"
if errorlevel 1 (
    echo Fehler beim Commit in main. Git-Output:
    git status
    git checkout "%current_branch%"
    git stash pop
    pause
    goto menu
) else (
    echo Erfolg: Commit in main erstellt mit Message "%message%".
    git log --oneline -1
)
echo Pushe main...
git push origin main
if errorlevel 1 (
    echo Fehler beim Push von main. Git-Output:
    git status
    pause
) else (
    echo Erfolg: main erfolgreich gepusht.
)
echo Wechsle zurueck zu %current_branch%...
git checkout "%current_branch%"
echo Stelle lokale Aenderungen wieder her...
git stash pop
pause
goto menu

:end
echo Script beendet.
pause