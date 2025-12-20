@echo off
setlocal

:menu
cls
echo.
echo ================================
echo Git Simple - 3 Functions
echo ================================
echo.
echo m - Merge to Main
echo h - Pull Hard
echo p - Push All
echo x - Exit
echo.
echo ================================
echo.
set /p choice=Enter choice: 

if /i "%choice%"=="m" goto merge
if /i "%choice%"=="h" goto hard
if /i "%choice%"=="p" goto push
if /i "%choice%"=="x" goto end
goto menu

:merge
echo.
echo Executing merge workflow...
echo.
git checkout main && git pull origin main && git merge --no-ff copilot/add-latex-build-workflow && git push origin main && git checkout copilot/add-latex-build-workflow
echo.
if errorlevel 1 (
    echo [ERROR] Merge failed - you may need to resolve conflicts
    echo Current branch:
    git branch --show-current
) else (
    echo [DONE] Merge complete - returned to working branch
)
pause
goto menu

:hard
echo.
echo Fetching from origin...
git fetch origin
echo.
echo Hard resetting to remote...
git reset --hard origin/copilot/add-latex-build-workflow
echo.
echo [DONE] Pull hard complete
pause
goto menu

:push
echo.
echo Staging all changes...
git add .
echo.
echo Committing with timestamp...
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do set mydate=%%c-%%a-%%b
for /f "tokens=1-2 delims=: " %%a in ('time /t') do set mytime=%%a:%%b
git commit -m "Auto-commit %mydate% %mytime%"
echo.
echo Pushing to branch...
git push origin copilot/add-latex-build-workflow
echo.
echo [DONE] Push complete
pause
goto menu

:end
echo.
echo Exiting...
exit /b 0
