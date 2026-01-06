# Creating the standalone-tree Branch

This document describes how to create the `standalone-tree` branch that captures a snapshot of the current repository state.

## Purpose

The `standalone-tree` branch is designed to:
- Capture the complete current state of the repository
- Include all uncommitted changes as a snapshot
- Serve as a standalone development branch
- Not affect any existing branches

## Automated Scripts

Two scripts are provided to automate the branch creation process:

### For Linux/macOS:
```bash
./create_standalone_tree_branch.sh
```

### For Windows:
```batch
create_standalone_tree_branch.bat
```

## Manual Steps

If you prefer to create the branch manually, follow these steps:

```bash
# 1. Check current status
git status --short

# 2. Create and checkout new branch
git checkout -b standalone-tree

# 3. Add all files (including uncommitted changes)
git add -A

# 4. Create snapshot commit
git commit -m "Snapshot: standalone LaTeX narrative (Teil1–3 und Kapitelstand lokal)"

# 5. Push branch to origin
git push -u origin standalone-tree
```

## What These Commands Do

1. **git status --short**: Shows the current status of your working directory in short format
2. **git checkout -b standalone-tree**: Creates a new branch named `standalone-tree` and switches to it
3. **git add -A**: Stages all changes (modified, new, and deleted files)
4. **git commit -m "..."**: Creates a commit with all staged changes
5. **git push -u origin standalone-tree**: Pushes the new branch to the remote repository and sets up tracking

## After Creation

Once the branch is created and pushed:
- You will be on the `standalone-tree` branch
- All further work should be done on this branch
- The branch contains a complete snapshot of your local state at the time of creation
- Original branches remain unchanged

## Note

The branch `standalone-tree` was created in the CI environment but cannot be pushed directly due to authentication constraints. The repository owner should run one of the provided scripts in their local environment to create and push the branch.

Alternatively, the branch has already been created locally in this workspace as a demonstration. To push it from the local repository, navigate to your repository directory and run:

```bash
cd C:\users\johann\B15  # Or your actual repository path
git checkout standalone-tree  # If not already on this branch
git push -u origin standalone-tree
```
