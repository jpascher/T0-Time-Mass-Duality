#!/bin/bash
set -e

# Script to create standalone-tree branch with current repository state
# This script creates a snapshot of the current local state (including any uncommitted changes)
# as a new branch without modifying existing branches

echo "Creating standalone-tree branch..."

# Step 1: Show current status
echo "Step 1: Checking current status..."
git status --short

# Step 2: Create and checkout new branch
echo "Step 2: Creating new branch 'standalone-tree'..."
# Check if branch already exists
if git rev-parse --verify standalone-tree >/dev/null 2>&1; then
    echo "Error: Branch 'standalone-tree' already exists. Please delete it first or use a different branch name."
    exit 1
fi
git checkout -b standalone-tree

# Step 3: Add all files (including any uncommitted changes)
echo "Step 3: Adding all files..."
git add -A

# Step 4: Create snapshot commit
echo "Step 4: Creating snapshot commit..."
git commit -m "Snapshot: standalone LaTeX narrative (Teil1–3 und Kapitelstand lokal)"

# Step 5: Push branch to origin
echo "Step 5: Pushing branch to origin..."
git push -u origin standalone-tree

echo "Done! Branch 'standalone-tree' has been created and pushed."
echo "You are now on the standalone-tree branch."
