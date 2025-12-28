# Branch Management Guide - Closing/Deleting Branches

## How do I close all branches?

### Important Note
⚠️ **CAUTION**: Deleting branches is a permanent action. Ensure that all important changes have been merged into the main branch or otherwise backed up.

## Methods for Closing/Deleting Branches

### 1. Delete a single local branch

```bash
# Delete branch (only if it has been merged)
git branch -d branch-name

# Force delete branch (even if not merged)
git branch -D branch-name
```

### 2. Delete a single remote branch

```bash
# Delete remote branch
git push origin --delete branch-name

# Alternative syntax
git push origin :branch-name
```

### 3. Delete all local branches (except main)

**Step 1: Switch to the main branch**
```bash
git checkout main
```

**Step 2: Delete all other local branches**
```bash
# Delete all branches except main (only merged ones)
git branch | grep -v "main" | xargs git branch -d

# Force delete all branches except main
git branch | grep -v "main" | xargs git branch -D
```

### 4. Delete all stale remote-tracking branches

```bash
# Show stale remote branches
git remote prune origin --dry-run

# Delete stale remote branches
git remote prune origin
```

### 5. Delete all remote branches (except main)

**⚠️ USE WITH EXTREME CAUTION - THIS DELETES BRANCHES ON GITHUB!**

```bash
# List all remote branches (except main)
git branch -r | grep -v "main" | sed 's/origin\///' | xargs -I {} echo "git push origin --delete {}"

# Execute the actual deletion (remove echo to execute)
git branch -r | grep -v "main" | sed 's/origin\///' | xargs -I {} git push origin --delete {}
```

## Using the Branch Management Script

The repository already contains a script `manage_current_branch.bat` for Windows users. For deleting branches, use the Git commands above.

## Recommended Workflow

### Before Deleting:
1. **Create backup**: Ensure important data is backed up
2. **Check branches**: 
   ```bash
   # Show local branches
   git branch
   
   # Show remote branches
   git branch -r
   
   # Show all branches
   git branch -a
   ```
3. **Check merge status**: Verify if branches have already been merged
   ```bash
   # Show merged branches
   git branch --merged
   
   # Show unmerged branches
   git branch --no-merged
   ```

### After Deleting:
1. **Verify**: Check if branches were successfully deleted
   ```bash
   git branch -a
   ```
2. **Clean up**: Clean local references
   ```bash
   git fetch --prune
   ```

## Common Scenarios

### Scenario 1: Delete all feature branches after release
```bash
# Switch to main
git checkout main

# Delete local feature branches
git branch | grep "feature/" | xargs git branch -D

# Delete remote feature branches
git branch -r | grep "feature/" | sed 's/origin\///' | xargs -I {} git push origin --delete {}
```

### Scenario 2: Delete all copilot branches
```bash
# Delete local copilot branches
git branch | grep "copilot/" | xargs git branch -D

# Delete remote copilot branches
git branch -r | grep "copilot/" | sed 's/origin\///' | xargs -I {} git push origin --delete {}
```

### Scenario 3: Delete only merged branches
```bash
# Delete all merged local branches (except main)
git branch --merged main | grep -v "main" | xargs git branch -d
```

## Safety Checklist

- [ ] All important changes are committed
- [ ] All important branches are merged into main
- [ ] Backup is created (if necessary)
- [ ] You are on the main branch
- [ ] You have reviewed the branch list
- [ ] You understand that deleted remote branches are deleted for all team members

## Troubleshooting

### Error: "Cannot delete branch - not fully merged"
**Solution**: Use `-D` instead of `-d` for forced deletion, or merge the branch first.

### Error: "Remote branch not found"
**Solution**: The branch may only exist locally. Check with `git branch -a`.

### Error: "Permission denied"
**Solution**: You may not have permission to delete remote branches. Contact the repository administrator.

## Additional Resources

- Git Documentation: https://git-scm.com/docs
- GitHub Branch Management: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches

## Contact

For questions, contact:
- **Email**: johann.pascher@gmail.com
