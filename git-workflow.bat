@echo off
setlocal enabledelayedexpansion
color 0A

:MENU
cls
echo =======================================
echo   Git Workflow - 3 Functions
echo =======================================
echo.
echo   1. Merge to Main
echo   2. Pull Hard
echo   3. Push All
echo   0. Exit
echo.
echo =======================================
set /p choice="Select (1-3 or 0): "

if "%choice%"=="1" goto MERGE_TO_MAIN
if "%choice%"=="2" goto PULL_HARD
if "%choice%"=="3" goto PUSH_ALL
if "%choice%"=="0" goto EXIT
goto MENU

:MERGE_TO_MAIN
echo.
echo [1/5] Switching to main...
git checkout main
echo [2/5] Pulling main...
git pull origin main
echo [3/5] Merging...
git merge --no-ff copilot/add-latex-build-workflow -m "Merge: T0 updates"
echo [4/5] Pushing main...
git push origin main
echo [5/5] Returning to working branch...
git checkout copilot/add-latex-build-workflow
echo.
echo [OK] Merge completed
pause
goto MENU

:PULL_HARD
echo.
echo Fetching and resetting to remote...
git fetch origin
git reset --hard origin/copilot/add-latex-build-workflow
echo [OK] Hard reset completed
pause
goto MENU

:PUSH_ALL
echo.
echo Staging all changes...
git add .
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a:%%b)
git commit -m "Auto-commit %mydate% %mytime%"
echo Pushing...
git push origin copilot/add-latex-build-workflow
echo [OK] Push completed
pause
goto MENU

:EXIT
echo.
echo Goodbye!
timeout /t 1 >nul
exit /b 0
