# Schnellreferenz: Branches Schließen / Quick Reference: Closing Branches

## 🇩🇪 Deutsch

### Alle Branches anzeigen
```bash
git branch -a
```

### Einzelnen Branch löschen
```bash
# Lokal (nur wenn gemerged)
git branch -d branch-name

# Lokal (erzwingen)
git branch -D branch-name

# Remote (GitHub)
git push origin --delete branch-name
```

### Alle lokalen Branches außer main löschen
```bash
git checkout main
git branch | grep -v "main" | xargs git branch -D
```

### Interaktive Skripte verwenden
```bash
# Windows
close_branches.bat

# Linux/Mac
./close_branches.sh
```

### Siehe auch
- **Vollständige Anleitung**: [BRANCH_MANAGEMENT_DE.md](BRANCH_MANAGEMENT_DE.md)
- **Existing Tool**: `manage_current_branch.bat` (Windows)

---

## 🇬🇧 English

### Show all branches
```bash
git branch -a
```

### Delete a single branch
```bash
# Local (only if merged)
git branch -d branch-name

# Local (force)
git branch -D branch-name

# Remote (GitHub)
git push origin --delete branch-name
```

### Delete all local branches except main
```bash
git checkout main
git branch | grep -v "main" | xargs git branch -D
```

### Use interactive scripts
```bash
# Windows
close_branches.bat

# Linux/Mac
./close_branches.sh
```

### See also
- **Full Guide**: [BRANCH_MANAGEMENT_EN.md](BRANCH_MANAGEMENT_EN.md)
- **Existing Tool**: `manage_current_branch.bat` (Windows)

---

## ⚠️ Wichtige Hinweise / Important Notes

**Deutsch:**
- ✅ Erstellen Sie immer ein Backup wichtiger Daten
- ✅ Prüfen Sie, ob Branches gemerged sind: `git branch --merged`
- ⚠️ Das Löschen von Remote-Branches betrifft alle Team-Mitglieder
- ⚠️ Verwenden Sie `-D` nur, wenn Sie sicher sind

**English:**
- ✅ Always create a backup of important data
- ✅ Check if branches are merged: `git branch --merged`
- ⚠️ Deleting remote branches affects all team members
- ⚠️ Use `-D` only when you're certain

---

**Autor / Author**: Johann Pascher  
**E-Mail**: johann.pascher@gmail.com
