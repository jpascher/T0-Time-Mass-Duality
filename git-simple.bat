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
echo [1/5] Switching to main...
git checkout main
echo.
echo [2/5] Pulling latest main...
git pull origin main
echo.
echo [3/5] Merging working branch...
git merge --no-ff copilot/add-latex-build-workflow
echo.
echo [4/5] Pushing to main...
git push origin main
echo.
echo [5/5] Returning to working branch...
git checkout copilot/add-latex-build-workflow
echo.
echo [DONE] Merge complete
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
