@echo off
REM Script to create standalone-tree branch with current repository state
REM This script creates a snapshot of the current local state (including any uncommitted changes)
REM as a new branch without modifying existing branches

echo Creating standalone-tree branch...

REM Step 1: Show current status
echo Step 1: Checking current status...
git status --short

REM Step 2: Create and checkout new branch
echo Step 2: Creating new branch 'standalone-tree'...
git checkout -b standalone-tree

REM Step 3: Add all files (including any uncommitted changes)
echo Step 3: Adding all files...
git add -A

REM Step 4: Create snapshot commit
echo Step 4: Creating snapshot commit...
git commit -m "Snapshot: standalone LaTeX narrative (Teil1–3 und Kapitelstand lokal)"

REM Step 5: Push branch to origin
echo Step 5: Pushing branch to origin...
git push -u origin standalone-tree

echo Done! Branch 'standalone-tree' has been created and pushed.
echo You are now on the standalone-tree branch.

pause
