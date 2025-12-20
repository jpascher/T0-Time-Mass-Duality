@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
color 0A

:MENU
cls
echo ===============================================================
echo   T0 Time-Mass-Duality Repository - Git Workflow Manager
echo ===============================================================
echo.
echo Current Branch: copilot/add-latex-build-workflow
echo.
echo +-------------------------------------------------------------+
echo ^|  1. Pull latest changes from remote                        ^|
echo ^|  2. Hard reset to remote (DISCARD local changes!)          ^|
echo ^|  3. Stage all changes (git add .)                          ^|
echo ^|  4. Commit changes (with custom message)                   ^|
echo ^|  5. Push to current branch                                 ^|
echo ^|  6. Full workflow: Add + Commit + Push                     ^|
echo ^|  7. Merge to main (preserves current branch)               ^|
echo ^|  8. Show git status                                        ^|
echo ^|  9. Show git log (last 5 commits)                          ^|
echo ^|  0. Exit                                                    ^|
echo +-------------------------------------------------------------+
echo.
set /p choice="Select option (0-9): "

if "%choice%"=="1" goto PULL
if "%choice%"=="2" goto HARD_RESET
if "%choice%"=="3" goto ADD
if "%choice%"=="4" goto COMMIT
if "%choice%"=="5" goto PUSH
if "%choice%"=="6" goto FULL_WORKFLOW
if "%choice%"=="7" goto MERGE_TO_MAIN
if "%choice%"=="8" goto STATUS
if "%choice%"=="9" goto LOG
if "%choice%"=="0" goto EXIT
goto MENU

:PULL
echo.
echo ─────────────────────────────────────────────────────────────
echo Pulling latest changes from remote...
echo ─────────────────────────────────────────────────────────────
git pull origin copilot/add-latex-build-workflow
echo.
if %ERRORLEVEL% EQU 0 (
    echo ✓ Pull successful!
) else (
    echo ✗ Pull failed! Error code: %ERRORLEVEL%
)
pause
goto MENU

:HARD_RESET
echo.
echo +===========================================================+
echo ^|  WARNING: This will DISCARD all local changes!           ^|
echo +===========================================================+
echo.
set /p confirm="Are you sure? Type YES to confirm: "
if /i not "%confirm%"=="YES" (
    echo Operation cancelled.
    pause
    goto MENU
)
echo.
echo ─────────────────────────────────────────────────────────────
echo Fetching from remote...
echo ─────────────────────────────────────────────────────────────
git fetch origin copilot/add-latex-build-workflow
echo.
echo ─────────────────────────────────────────────────────────────
echo Resetting to remote state...
echo ─────────────────────────────────────────────────────────────
git reset --hard origin/copilot/add-latex-build-workflow
echo.
if %ERRORLEVEL% EQU 0 (
    echo ✓ Hard reset successful! Repository is now in sync with remote.
) else (
    echo ✗ Hard reset failed! Error code: %ERRORLEVEL%
)
pause
goto MENU

:ADD
echo.
echo ─────────────────────────────────────────────────────────────
echo Staging all changes (git add .)...
echo ─────────────────────────────────────────────────────────────
git add .
echo.
if %ERRORLEVEL% EQU 0 (
    echo ✓ All changes staged!
    echo.
    echo Files staged:
    git diff --cached --name-status
) else (
    echo ✗ Git add failed! Error code: %ERRORLEVEL%
)
pause
goto MENU

:COMMIT
echo.
echo ─────────────────────────────────────────────────────────────
echo Committing changes
echo ─────────────────────────────────────────────────────────────
echo.
set /p commit_msg="Enter commit message: "
if "%commit_msg%"=="" (
    echo ✗ Commit message cannot be empty!
    pause
    goto MENU
)
echo.
git commit -m "%commit_msg%"
echo.
if %ERRORLEVEL% EQU 0 (
    echo ✓ Commit successful!
) else (
    echo ✗ Commit failed! Error code: %ERRORLEVEL%
    echo Note: If nothing to commit, this is normal.
)
pause
goto MENU

:PUSH
echo.
echo ─────────────────────────────────────────────────────────────
echo Pushing to copilot/add-latex-build-workflow...
echo ─────────────────────────────────────────────────────────────
git push origin copilot/add-latex-build-workflow
echo.
if %ERRORLEVEL% EQU 0 (
    echo ✓ Push successful!
) else (
    echo ✗ Push failed! Error code: %ERRORLEVEL%
)
pause
goto MENU

:FULL_WORKFLOW
echo.
echo ===============================================================
echo Full Workflow: Add + Commit + Push
echo ===============================================================
echo.
set /p commit_msg="Enter commit message: "
if "%commit_msg%"=="" (
    echo ✗ Commit message cannot be empty!
    pause
    goto MENU
)
echo.
echo [1/3] Staging all changes...
git add .
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Git add failed!
    pause
    goto MENU
)
echo ✓ Changes staged
echo.
echo [2/3] Committing changes...
git commit -m "%commit_msg%"
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Commit failed!
    pause
    goto MENU
)
echo ✓ Commit successful
echo.
echo [3/3] Pushing to remote...
git push origin copilot/add-latex-build-workflow
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Push failed!
    pause
    goto MENU
)
echo ✓ Push successful
echo.
echo ===============================================================
echo SUCCESS: Full workflow completed successfully!
echo ===============================================================
pause
goto MENU

:MERGE_TO_MAIN
echo.
echo ===============================================================
echo Merge copilot/add-latex-build-workflow to main
echo ===============================================================
echo.
echo This will:
echo   1. Switch to main branch
echo   2. Pull latest main changes
echo   3. Merge copilot/add-latex-build-workflow (no fast-forward)
echo   4. Push to main
echo   5. Switch back to copilot/add-latex-build-workflow
echo.
echo The current branch will be PRESERVED for continued work.
echo.
set /p confirm="Continue with merge? Type YES to confirm: "
if /i not "%confirm%"=="YES" (
    echo Operation cancelled.
    pause
    goto MENU
)
echo.
echo ─────────────────────────────────────────────────────────────
echo [1/5] Switching to main branch...
echo ─────────────────────────────────────────────────────────────
git checkout main
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Failed to checkout main branch!
    pause
    goto MENU
)
echo ✓ On main branch
echo.
echo ─────────────────────────────────────────────────────────────
echo [2/5] Pulling latest main changes...
echo ─────────────────────────────────────────────────────────────
git pull origin main
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Failed to pull main!
    echo Attempting to switch back to working branch...
    git checkout copilot/add-latex-build-workflow
    pause
    goto MENU
)
echo ✓ Main updated
echo.
echo ─────────────────────────────────────────────────────────────
echo [3/5] Merging copilot/add-latex-build-workflow into main...
echo ─────────────────────────────────────────────────────────────
git merge --no-ff copilot/add-latex-build-workflow -m "Merge: T0 theory updates (Consciousness documents, Matsas integration, bibliography standardization)"
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Merge failed! You may have conflicts to resolve.
    echo Please resolve conflicts manually, then:
    echo   git commit
    echo   git push origin main
    echo   git checkout copilot/add-latex-build-workflow
    pause
    goto MENU
)
echo ✓ Merge successful
echo.
echo ─────────────────────────────────────────────────────────────
echo [4/5] Pushing main to remote...
echo ─────────────────────────────────────────────────────────────
git push origin main
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Push to main failed!
    echo You may need to push manually:
    echo   git push origin main
    echo.
    echo Switching back to working branch...
    git checkout copilot/add-latex-build-workflow
    pause
    goto MENU
)
echo ✓ Main pushed successfully
echo.
echo ─────────────────────────────────────────────────────────────
echo [5/5] Switching back to copilot/add-latex-build-workflow...
echo ─────────────────────────────────────────────────────────────
git checkout copilot/add-latex-build-workflow
if %ERRORLEVEL% NEQ 0 (
    echo ✗ Failed to switch back! You're still on main.
    echo Use: git checkout copilot/add-latex-build-workflow
    pause
    goto MENU
)
echo ✓ Back on copilot/add-latex-build-workflow
echo.
echo ===============================================================
echo SUCCESS: Merge to main completed successfully!
echo ===============================================================
echo.
echo Your working branch is preserved and ready for continued work.
pause
goto MENU

:STATUS
echo.
echo ─────────────────────────────────────────────────────────────
echo Git Status
echo ─────────────────────────────────────────────────────────────
git status
echo.
pause
goto MENU

:LOG
echo.
echo ─────────────────────────────────────────────────────────────
echo Last 5 Commits
echo ─────────────────────────────────────────────────────────────
git log --oneline -5
echo.
echo ─────────────────────────────────────────────────────────────
echo Detailed view of last commit:
echo ─────────────────────────────────────────────────────────────
git log -1 --stat
echo.
pause
goto MENU

:EXIT
echo.
echo Thank you for using T0 Git Workflow Manager!
echo.
timeout /t 2 >nul
exit /b 0
