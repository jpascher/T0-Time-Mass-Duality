#!/bin/bash

# Branch Management Script - Close/Delete Branches
# Skript zum Verwalten und Löschen von Git-Branches

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "================================"
echo "Branch Management Script"
echo "Branches Schließen/Löschen"
echo "================================"

# Check if we're in a git repository
if [ ! -d .git ]; then
    echo -e "${RED}Error: This is not a Git repository.${NC}"
    echo -e "${RED}Fehler: Dies ist kein Git-Repository.${NC}"
    exit 1
fi

# Get current branch
current_branch=$(git branch --show-current)
if [ -z "$current_branch" ]; then
    echo -e "${RED}Error: Could not determine current branch.${NC}"
    exit 1
fi

echo -e "${GREEN}Current branch / Aktueller Branch: ${current_branch}${NC}"
echo ""

# Main menu
show_menu() {
    echo "================================"
    echo "What would you like to do?"
    echo "Was möchten Sie tun?"
    echo "================================"
    echo "1. List all branches / Alle Branches anzeigen"
    echo "2. Delete a specific local branch / Einen lokalen Branch löschen"
    echo "3. Delete all local branches except main / Alle lokalen Branches außer main löschen"
    echo "4. Delete a specific remote branch / Einen Remote-Branch löschen"
    echo "5. Delete all remote branches except main / Alle Remote-Branches außer main löschen"
    echo "6. Clean up stale remote references / Veraltete Remote-Referenzen aufräumen"
    echo "7. Show merged branches / Gemergede Branches anzeigen"
    echo "8. Show unmerged branches / Nicht gemergede Branches anzeigen"
    echo "9. Exit / Beenden"
    echo "================================"
    read -p "Choose option / Wähle Option (1-9): " choice
    echo ""
}

# Function to list all branches
list_branches() {
    echo -e "${GREEN}Local branches / Lokale Branches:${NC}"
    git branch
    echo ""
    echo -e "${GREEN}Remote branches / Remote-Branches:${NC}"
    git branch -r
    echo ""
}

# Function to delete a specific local branch
delete_local_branch() {
    read -p "Enter branch name to delete / Branch-Name eingeben: " branch_name
    if [ -z "$branch_name" ]; then
        echo -e "${RED}No branch name provided / Kein Branch-Name angegeben${NC}"
        return
    fi
    
    if [ "$branch_name" = "main" ] || [ "$branch_name" = "master" ]; then
        echo -e "${RED}Cannot delete main/master branch!${NC}"
        echo -e "${RED}Kann main/master Branch nicht löschen!${NC}"
        return
    fi
    
    read -p "Force delete (y/n)? / Erzwingen (j/n)? " force
    if [ "$force" = "y" ] || [ "$force" = "j" ]; then
        git branch -D "$branch_name" && echo -e "${GREEN}Branch deleted / Branch gelöscht: $branch_name${NC}"
    else
        git branch -d "$branch_name" && echo -e "${GREEN}Branch deleted / Branch gelöscht: $branch_name${NC}"
    fi
}

# Function to delete all local branches except main
delete_all_local_except_main() {
    echo -e "${YELLOW}WARNING: This will delete all local branches except main!${NC}"
    echo -e "${YELLOW}WARNUNG: Dies löscht alle lokalen Branches außer main!${NC}"
    
    read -p "Are you sure? (yes/no) / Sind Sie sicher? (ja/nein): " confirm
    if [ "$confirm" != "yes" ] && [ "$confirm" != "ja" ]; then
        echo "Cancelled / Abgebrochen"
        return
    fi
    
    # Switch to main if not already there
    if [ "$current_branch" != "main" ]; then
        echo "Switching to main branch / Wechsle zu main Branch..."
        git checkout main
    fi
    
    # Delete all branches except main
    branches_to_delete=$(git branch | grep -v "main" | grep -v "\*" | tr -d ' ')
    
    if [ -z "$branches_to_delete" ]; then
        echo -e "${GREEN}No branches to delete / Keine Branches zum Löschen${NC}"
        return
    fi
    
    echo "Branches to delete / Zu löschende Branches:"
    echo "$branches_to_delete"
    echo ""
    
    read -p "Force delete? (y/n) / Erzwingen? (j/n): " force
    
    for branch in $branches_to_delete; do
        if [ "$force" = "y" ] || [ "$force" = "j" ]; then
            git branch -D "$branch" && echo -e "${GREEN}Deleted / Gelöscht: $branch${NC}"
        else
            git branch -d "$branch" && echo -e "${GREEN}Deleted / Gelöscht: $branch${NC}" || echo -e "${YELLOW}Skipped (not merged) / Übersprungen (nicht gemerged): $branch${NC}"
        fi
    done
}

# Function to delete a specific remote branch
delete_remote_branch() {
    read -p "Enter remote branch name to delete / Remote-Branch-Name eingeben: " branch_name
    if [ -z "$branch_name" ]; then
        echo -e "${RED}No branch name provided / Kein Branch-Name angegeben${NC}"
        return
    fi
    
    if [ "$branch_name" = "main" ] || [ "$branch_name" = "master" ]; then
        echo -e "${RED}Cannot delete main/master branch!${NC}"
        echo -e "${RED}Kann main/master Branch nicht löschen!${NC}"
        return
    fi
    
    echo -e "${YELLOW}WARNING: This will delete the branch on GitHub!${NC}"
    echo -e "${YELLOW}WARNUNG: Dies löscht den Branch auf GitHub!${NC}"
    
    read -p "Are you sure? (yes/no) / Sind Sie sicher? (ja/nein): " confirm
    if [ "$confirm" = "yes" ] || [ "$confirm" = "ja" ]; then
        git push origin --delete "$branch_name" && echo -e "${GREEN}Remote branch deleted / Remote-Branch gelöscht: $branch_name${NC}"
    else
        echo "Cancelled / Abgebrochen"
    fi
}

# Function to delete all remote branches except main
delete_all_remote_except_main() {
    echo -e "${RED}DANGER: This will delete ALL remote branches except main on GitHub!${NC}"
    echo -e "${RED}GEFAHR: Dies löscht ALLE Remote-Branches außer main auf GitHub!${NC}"
    
    read -p "Type 'DELETE ALL' to confirm / Tippen Sie 'ALLES LÖSCHEN' zur Bestätigung: " confirm
    if [ "$confirm" != "DELETE ALL" ] && [ "$confirm" != "ALLES LÖSCHEN" ]; then
        echo "Cancelled / Abgebrochen"
        return
    fi
    
    # Get all remote branches except main
    remote_branches=$(git branch -r | grep -v "main" | grep -v "HEAD" | sed 's/origin\///' | tr -d ' ')
    
    if [ -z "$remote_branches" ]; then
        echo -e "${GREEN}No remote branches to delete / Keine Remote-Branches zum Löschen${NC}"
        return
    fi
    
    echo "Remote branches to delete / Zu löschende Remote-Branches:"
    echo "$remote_branches"
    echo ""
    
    read -p "Final confirmation (yes/no) / Letzte Bestätigung (ja/nein): " final_confirm
    if [ "$final_confirm" = "yes" ] || [ "$final_confirm" = "ja" ]; then
        for branch in $remote_branches; do
            git push origin --delete "$branch" && echo -e "${GREEN}Deleted / Gelöscht: origin/$branch${NC}" || echo -e "${RED}Failed / Fehlgeschlagen: origin/$branch${NC}"
        done
    else
        echo "Cancelled / Abgebrochen"
    fi
}

# Function to clean up stale remote references
cleanup_stale_refs() {
    echo "Cleaning up stale remote references..."
    echo "Räume veraltete Remote-Referenzen auf..."
    git remote prune origin
    git fetch --prune
    echo -e "${GREEN}Cleanup completed / Aufräumen abgeschlossen${NC}"
}

# Function to show merged branches
show_merged_branches() {
    echo -e "${GREEN}Merged branches / Gemergede Branches:${NC}"
    git branch --merged main
    echo ""
}

# Function to show unmerged branches
show_unmerged_branches() {
    echo -e "${YELLOW}Unmerged branches / Nicht gemergede Branches:${NC}"
    git branch --no-merged main
    echo ""
}

# Main loop
while true; do
    show_menu
    
    case $choice in
        1)
            list_branches
            ;;
        2)
            delete_local_branch
            ;;
        3)
            delete_all_local_except_main
            ;;
        4)
            delete_remote_branch
            ;;
        5)
            delete_all_remote_except_main
            ;;
        6)
            cleanup_stale_refs
            ;;
        7)
            show_merged_branches
            ;;
        8)
            show_unmerged_branches
            ;;
        9)
            echo "Exiting / Beenden..."
            exit 0
            ;;
        *)
            echo -e "${RED}Invalid option / Ungültige Option${NC}"
            ;;
    esac
    
    echo ""
    read -p "Press Enter to continue / Drücken Sie Enter zum Fortfahren..."
    echo ""
done
