@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: Branch Management Script - Close/Delete Branches
:: Skript zum Verwalten und Löschen von Git-Branches

echo ================================
echo Branch Management Script
echo Branches Schließen/Löschen
echo ================================
echo.

:: Check if this is a Git repository
if not exist .git (
    echo [FEHLER] Dies ist kein Git-Repository.
    echo [ERROR] This is not a Git repository.
    pause
    exit /b 1
)

:: Get current branch
for /f %%i in ('git branch --show-current') do set current_branch=%%i
if "%current_branch%"=="" (
    echo [FEHLER] Konnte aktuellen Branch nicht ermitteln.
    echo [ERROR] Could not determine current branch.
    pause
    exit /b 1
)

echo Aktueller Branch / Current branch: %current_branch%
echo.

:menu
cls
echo ================================
echo Was möchten Sie tun?
echo What would you like to do?
echo ================================
echo 1. Alle Branches anzeigen / List all branches
echo 2. Einen lokalen Branch löschen / Delete a specific local branch
echo 3. Alle lokalen Branches außer main löschen / Delete all local branches except main
echo 4. Einen Remote-Branch löschen / Delete a specific remote branch
echo 5. Alle Remote-Branches außer main löschen / Delete all remote branches except main
echo 6. Veraltete Remote-Referenzen aufräumen / Clean up stale remote references
echo 7. Gemergede Branches anzeigen / Show merged branches
echo 8. Nicht gemergede Branches anzeigen / Show unmerged branches
echo 9. Beenden / Exit
echo ================================
set /p choice="Wähle Option / Choose option (1-9): "
echo.

if "%choice%"=="1" goto list_branches
if "%choice%"=="2" goto delete_local_branch
if "%choice%"=="3" goto delete_all_local
if "%choice%"=="4" goto delete_remote_branch
if "%choice%"=="5" goto delete_all_remote
if "%choice%"=="6" goto cleanup_stale
if "%choice%"=="7" goto show_merged
if "%choice%"=="8" goto show_unmerged
if "%choice%"=="9" goto end
echo Ungültige Option / Invalid option
pause
goto menu

:list_branches
echo [Lokale Branches / Local branches:]
git branch
echo.
echo [Remote-Branches / Remote branches:]
git branch -r
echo.
pause
goto menu

:delete_local_branch
set /p branch_name="Branch-Name eingeben / Enter branch name: "
if "%branch_name%"=="" (
    echo Kein Branch-Name angegeben / No branch name provided
    pause
    goto menu
)
if "%branch_name%"=="main" (
    echo [FEHLER] Kann main Branch nicht löschen!
    echo [ERROR] Cannot delete main branch!
    pause
    goto menu
)
if "%branch_name%"=="master" (
    echo [FEHLER] Kann master Branch nicht löschen!
    echo [ERROR] Cannot delete master branch!
    pause
    goto menu
)

set /p force="Erzwingen (j/n)? / Force delete (y/n)? "
if /i "%force%"=="j" goto force_delete_local
if /i "%force%"=="y" goto force_delete_local
git branch -d "%branch_name%"
if errorlevel 1 (
    echo Fehler beim Löschen / Error deleting branch
) else (
    echo Branch gelöscht / Branch deleted: %branch_name%
)
pause
goto menu

:force_delete_local
git branch -D "%branch_name%"
if errorlevel 1 (
    echo Fehler beim Löschen / Error deleting branch
) else (
    echo Branch gelöscht / Branch deleted: %branch_name%
)
pause
goto menu

:delete_all_local
echo.
echo [WARNUNG / WARNING]
echo Dies löscht ALLE lokalen Branches außer main!
echo This will delete ALL local branches except main!
echo.
set /p confirm="Sind Sie sicher? (ja/nein) / Are you sure? (yes/no): "
if /i not "%confirm%"=="ja" if /i not "%confirm%"=="yes" (
    echo Abgebrochen / Cancelled
    pause
    goto menu
)

:: Switch to main if not already there
if not "%current_branch%"=="main" (
    echo Wechsle zu main Branch / Switching to main branch...
    git checkout main
    if errorlevel 1 (
        echo Fehler beim Wechsel zu main / Error switching to main
        pause
        goto menu
    )
)

set /p force="Erzwingen (j/n)? / Force delete (y/n)? "
echo.
echo Lösche Branches / Deleting branches...
echo.

for /f "tokens=*" %%a in ('git branch ^| findstr /v "main" ^| findstr /v "*"') do (
    set "branch=%%a"
    set "branch=!branch:~2!"
    if /i "%force%"=="j" goto force_delete_all_local_one
    if /i "%force%"=="y" goto force_delete_all_local_one
    git branch -d "!branch!"
    if errorlevel 1 (
        echo Übersprungen (nicht gemerged) / Skipped (not merged): !branch!
    ) else (
        echo Gelöscht / Deleted: !branch!
    )
    goto continue_delete_all_local
    
    :force_delete_all_local_one
    git branch -D "!branch!"
    if errorlevel 1 (
        echo Fehler / Failed: !branch!
    ) else (
        echo Gelöscht / Deleted: !branch!
    )
    
    :continue_delete_all_local
)

echo.
echo Fertig / Done
pause
goto menu

:delete_remote_branch
set /p branch_name="Remote-Branch-Name eingeben / Enter remote branch name: "
if "%branch_name%"=="" (
    echo Kein Branch-Name angegeben / No branch name provided
    pause
    goto menu
)
if "%branch_name%"=="main" (
    echo [FEHLER] Kann main Branch nicht löschen!
    echo [ERROR] Cannot delete main branch!
    pause
    goto menu
)
if "%branch_name%"=="master" (
    echo [FEHLER] Kann master Branch nicht löschen!
    echo [ERROR] Cannot delete master branch!
    pause
    goto menu
)

echo.
echo [WARNUNG / WARNING]
echo Dies löscht den Branch auf GitHub!
echo This will delete the branch on GitHub!
echo.
set /p confirm="Sind Sie sicher? (ja/nein) / Are you sure? (yes/no): "
if /i not "%confirm%"=="ja" if /i not "%confirm%"=="yes" (
    echo Abgebrochen / Cancelled
    pause
    goto menu
)

git push origin --delete "%branch_name%"
if errorlevel 1 (
    echo Fehler beim Löschen / Error deleting remote branch
) else (
    echo Remote-Branch gelöscht / Remote branch deleted: %branch_name%
)
pause
goto menu

:delete_all_remote
echo.
echo [GEFAHR / DANGER]
echo Dies löscht ALLE Remote-Branches außer main auf GitHub!
echo This will delete ALL remote branches except main on GitHub!
echo.
set /p confirm="Tippen Sie 'ALLES LÖSCHEN' oder 'DELETE ALL' zur Bestätigung / Type 'DELETE ALL' to confirm: "
if /i not "%confirm%"=="ALLES LÖSCHEN" if /i not "%confirm%"=="DELETE ALL" (
    echo Abgebrochen / Cancelled
    pause
    goto menu
)

echo.
echo Remote-Branches die gelöscht werden / Remote branches to be deleted:
echo.
for /f "tokens=*" %%a in ('git branch -r ^| findstr /v "main" ^| findstr /v "HEAD"') do (
    set "branch=%%a"
    set "branch=!branch:~2!"
    set "branch=!branch:origin/=!"
    echo !branch!
)
echo.

set /p final_confirm="Letzte Bestätigung (ja/nein) / Final confirmation (yes/no): "
if /i not "%final_confirm%"=="ja" if /i not "%final_confirm%"=="yes" (
    echo Abgebrochen / Cancelled
    pause
    goto menu
)

echo.
echo Lösche Remote-Branches / Deleting remote branches...
echo.

for /f "tokens=*" %%a in ('git branch -r ^| findstr /v "main" ^| findstr /v "HEAD"') do (
    set "branch=%%a"
    set "branch=!branch:~2!"
    set "branch=!branch:origin/=!"
    git push origin --delete "!branch!"
    if errorlevel 1 (
        echo Fehlgeschlagen / Failed: !branch!
    ) else (
        echo Gelöscht / Deleted: !branch!
    )
)

echo.
echo Fertig / Done
pause
goto menu

:cleanup_stale
echo Räume veraltete Remote-Referenzen auf...
echo Cleaning up stale remote references...
echo.
git remote prune origin
git fetch --prune
echo.
echo Aufräumen abgeschlossen / Cleanup completed
pause
goto menu

:show_merged
echo [Gemergede Branches / Merged branches:]
git branch --merged main
echo.
pause
goto menu

:show_unmerged
echo [Nicht gemergede Branches / Unmerged branches:]
git branch --no-merged main
echo.
pause
goto menu

:end
echo Beenden / Exiting...
pause
exit /b 0
