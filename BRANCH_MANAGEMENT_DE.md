# Branch Management Guide - Branches Schließen/Löschen

## Wie schließe ich alle Branches?

### Wichtiger Hinweis
⚠️ **VORSICHT**: Das Löschen von Branches ist eine permanente Aktion. Stellen Sie sicher, dass alle wichtigen Änderungen in den main-Branch gemerged oder anderweitig gesichert wurden.

## Methoden zum Schließen/Löschen von Branches

### 1. Einzelnen lokalen Branch löschen

```bash
# Branch löschen (nur wenn er gemerged wurde)
git branch -d branch-name

# Branch erzwingen zu löschen (auch wenn nicht gemerged)
git branch -D branch-name
```

### 2. Einzelnen Remote-Branch löschen

```bash
# Remote-Branch löschen
git push origin --delete branch-name

# Alternative Syntax
git push origin :branch-name
```

### 3. Alle lokalen Branches (außer main) löschen

**Schritt 1: Wechseln Sie zum main-Branch**
```bash
git checkout main
```

**Schritt 2: Alle anderen lokalen Branches löschen**
```bash
# Alle Branches außer main löschen (nur gemergede)
git branch | grep -v "main" | xargs git branch -d

# Alle Branches außer main erzwingen zu löschen
git branch | grep -v "main" | xargs git branch -D
```

### 4. Alle verwaisten Remote-Tracking-Branches löschen

```bash
# Zeigt veraltete Remote-Branches an
git remote prune origin --dry-run

# Löscht veraltete Remote-Branches
git remote prune origin
```

### 5. Alle Remote-Branches (außer main) löschen

**⚠️ SEHR VORSICHTIG VERWENDEN - DIES LÖSCHT BRANCHES AUF GITHUB!**

```bash
# Liste alle Remote-Branches (außer main)
git branch -r | grep -v "main" | sed 's/origin\///' | xargs -I {} echo "git push origin --delete {}"

# Führe das tatsächliche Löschen durch (entfernen Sie echo zum Ausführen)
git branch -r | grep -v "main" | sed 's/origin\///' | xargs -I {} git push origin --delete {}
```

## Verwendung des Branch-Management-Scripts

Das Repository enthält bereits ein Script `manage_current_branch.bat` für Windows-Benutzer. Für das Löschen von Branches verwenden Sie die Git-Befehle oben.

## Empfohlener Workflow

### Vor dem Löschen:
1. **Backup erstellen**: Stellen Sie sicher, dass wichtige Daten gesichert sind
2. **Branches prüfen**: 
   ```bash
   # Lokale Branches anzeigen
   git branch
   
   # Remote-Branches anzeigen
   git branch -r
   
   # Alle Branches anzeigen
   git branch -a
   ```
3. **Merge-Status prüfen**: Prüfen Sie, ob Branches bereits gemerged wurden
   ```bash
   # Gemergede Branches anzeigen
   git branch --merged
   
   # Nicht gemergede Branches anzeigen
   git branch --no-merged
   ```

### Nach dem Löschen:
1. **Verifizieren**: Prüfen Sie, ob die Branches erfolgreich gelöscht wurden
   ```bash
   git branch -a
   ```
2. **Aufräumen**: Bereinigen Sie lokale Referenzen
   ```bash
   git fetch --prune
   ```

## Häufige Szenarien

### Szenario 1: Alle Feature-Branches nach dem Release löschen
```bash
# Wechseln zu main
git checkout main

# Lokale Feature-Branches löschen
git branch | grep "feature/" | xargs git branch -D

# Remote Feature-Branches löschen
git branch -r | grep "feature/" | sed 's/origin\///' | xargs -I {} git push origin --delete {}
```

### Szenario 2: Alle Copilot-Branches löschen
```bash
# Lokale Copilot-Branches löschen
git branch | grep "copilot/" | xargs git branch -D

# Remote Copilot-Branches löschen
git branch -r | grep "copilot/" | sed 's/origin\///' | xargs -I {} git push origin --delete {}
```

### Szenario 3: Nur gemergede Branches löschen
```bash
# Alle gemergeden lokalen Branches löschen (außer main)
git branch --merged main | grep -v "main" | xargs git branch -d
```

## Sicherheits-Checkliste

- [ ] Alle wichtigen Änderungen sind committed
- [ ] Alle wichtigen Branches sind in main gemerged
- [ ] Backup ist erstellt (falls nötig)
- [ ] Sie sind auf dem main-Branch
- [ ] Sie haben die Branch-Liste überprüft
- [ ] Sie verstehen, dass gelöschte Remote-Branches für alle Team-Mitglieder gelöscht werden

## Troubleshooting

### Fehler: "Cannot delete branch - not fully merged"
**Lösung**: Verwenden Sie `-D` statt `-d` zum erzwungenen Löschen, oder mergen Sie den Branch zuerst.

### Fehler: "Remote branch not found"
**Lösung**: Der Branch existiert möglicherweise nur lokal. Prüfen Sie mit `git branch -a`.

### Fehler: "Permission denied"
**Lösung**: Sie haben möglicherweise keine Berechtigung, Remote-Branches zu löschen. Kontaktieren Sie den Repository-Administrator.

## Zusätzliche Ressourcen

- Git Dokumentation: https://git-scm.com/docs
- GitHub Branch Management: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches

## Kontakt

Bei Fragen wenden Sie sich an:
- **Email**: johann.pascher@gmail.com
