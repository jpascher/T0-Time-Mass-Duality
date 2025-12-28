# Branch Management - Komplette Übersicht / Complete Overview

## 📚 Verfügbare Ressourcen / Available Resources

### 📖 Dokumentation / Documentation

1. **[BRANCH_MANAGEMENT_DE.md](BRANCH_MANAGEMENT_DE.md)** (4.7KB)
   - 🇩🇪 Vollständige Anleitung auf Deutsch
   - Alle Methoden zum Löschen von Branches
   - Sicherheits-Checkliste
   - Troubleshooting-Tipps

2. **[BRANCH_MANAGEMENT_EN.md](BRANCH_MANAGEMENT_EN.md)** (4.2KB)
   - 🇬🇧 Complete guide in English
   - All methods for deleting branches
   - Safety checklist
   - Troubleshooting tips

3. **[QUICK_REFERENCE_BRANCHES.md](QUICK_REFERENCE_BRANCHES.md)** (2.0KB)
   - 🇩🇪🇬🇧 Bilingual quick reference
   - Most common commands
   - Fast access to essential operations

4. **[BRANCH_WORKFLOW.md](BRANCH_WORKFLOW.md)** (12KB)
   - 🇩🇪🇬🇧 Visual workflow guides
   - Step-by-step processes
   - Common scenarios with examples
   - Safety tips

### 🛠️ Interaktive Skripte / Interactive Scripts

1. **close_branches.sh** (8.2KB)
   - 🐧 Für Linux/Mac
   - Interaktives Menü
   - Sichere Bestätigungen
   - Farbige Ausgabe

2. **close_branches.bat** (7.6KB)
   - 🪟 Für Windows
   - Interaktives Menü
   - Sichere Bestätigungen
   - UTF-8-Unterstützung

3. **manage_current_branch.bat** (bereits vorhanden / existing)
   - 🪟 Erweiterte Branch-Verwaltung
   - Commit und Push Funktionen
   - Für fortgeschrittene Benutzer

## 🚀 Schnellstart / Quick Start

### Anfänger / Beginners
```bash
# Windows
close_branches.bat

# Linux/Mac
./close_branches.sh
```
Folgen Sie einfach dem interaktiven Menü!
Just follow the interactive menu!

### Fortgeschrittene / Advanced
Siehe [QUICK_REFERENCE_BRANCHES.md](QUICK_REFERENCE_BRANCHES.md) für direkte Git-Befehle.
See [QUICK_REFERENCE_BRANCHES.md](QUICK_REFERENCE_BRANCHES.md) for direct Git commands.

## 📋 Häufige Fragen / FAQ

### 🇩🇪 Deutsch

**Q: Wie lösche ich alle Branches außer main?**
```bash
git checkout main
git branch | grep -v "main" | xargs git branch -D
```
Oder verwenden Sie `close_branches.sh/bat` Option 3.

**Q: Wie lösche ich einen Remote-Branch?**
```bash
git push origin --delete branch-name
```
Oder verwenden Sie `close_branches.sh/bat` Option 4.

**Q: Wie sehe ich, welche Branches gemerged sind?**
```bash
git branch --merged
```
Oder verwenden Sie `close_branches.sh/bat` Option 7.

**Q: Kann ich gelöschte Branches wiederherstellen?**
Ja, wenn Sie den Commit-Hash kennen:
```bash
git checkout -b branch-name commit-hash
```

**Q: Was ist sicherer: -d oder -D?**
- `-d`: Löscht nur gemergede Branches (sicher)
- `-D`: Erzwingt das Löschen (Vorsicht!)

### 🇬🇧 English

**Q: How do I delete all branches except main?**
```bash
git checkout main
git branch | grep -v "main" | xargs git branch -D
```
Or use `close_branches.sh/bat` option 3.

**Q: How do I delete a remote branch?**
```bash
git push origin --delete branch-name
```
Or use `close_branches.sh/bat` option 4.

**Q: How do I see which branches are merged?**
```bash
git branch --merged
```
Or use `close_branches.sh/bat` option 7.

**Q: Can I restore deleted branches?**
Yes, if you know the commit hash:
```bash
git checkout -b branch-name commit-hash
```

**Q: Which is safer: -d or -D?**
- `-d`: Only deletes merged branches (safe)
- `-D`: Forces deletion (caution!)

## 🎯 Empfohlener Workflow / Recommended Workflow

### Für Einsteiger / For Beginners
1. ✅ Lesen Sie [BRANCH_WORKFLOW.md](BRANCH_WORKFLOW.md)
2. ✅ Verwenden Sie die interaktiven Skripte
3. ✅ Starten Sie mit Option 1 (Liste anzeigen)
4. ✅ Üben Sie mit einem Test-Repository

### Für Fortgeschrittene / For Advanced Users
1. ✅ Verwenden Sie [QUICK_REFERENCE_BRANCHES.md](QUICK_REFERENCE_BRANCHES.md)
2. ✅ Kombinieren Sie Git-Befehle
3. ✅ Automatisieren Sie mit eigenen Skripten
4. ✅ Siehe [BRANCH_MANAGEMENT_*.md](BRANCH_MANAGEMENT_DE.md) für Details

## ⚠️ Wichtige Warnungen / Important Warnings

### 🇩🇪 Deutsch
- ⚠️ **Remote-Löschungen** betreffen ALLE Team-Mitglieder
- ⚠️ **Gelöschte Branches** können schwer wiederherzustellen sein
- ⚠️ **Löschen Sie NIE** main oder master
- ⚠️ **Prüfen Sie immer** den Merge-Status vor dem Löschen
- ⚠️ **Erstellen Sie Backups** bei wichtigen Daten

### 🇬🇧 English
- ⚠️ **Remote deletions** affect ALL team members
- ⚠️ **Deleted branches** can be hard to restore
- ⚠️ **Never delete** main or master
- ⚠️ **Always check** merge status before deleting
- ⚠️ **Create backups** for important data

## 🔗 Integration in README

Die Branch-Management-Ressourcen sind bereits in den README-Dateien verlinkt:
The branch management resources are already linked in the README files:

- ✅ [README.md](README.md) - Englische Version / English version
- ✅ [README_de.md](README_de.md) - Deutsche Version / German version

Suchen Sie nach dem Abschnitt "Repository Management" / "Repository-Verwaltung".
Look for the "Repository Management" / "Repository-Verwaltung" section.

## 📞 Hilfe & Unterstützung / Help & Support

### Bei Problemen / If you have issues:
1. 📖 Lesen Sie die [vollständige Dokumentation](BRANCH_MANAGEMENT_DE.md)
2. 🔍 Prüfen Sie die [FAQ](#-häufige-fragen--faq) oben
3. 📧 Kontaktieren Sie: johann.pascher@gmail.com

### Bei Fragen zu Git / For Git questions:
- 📚 [Git Dokumentation](https://git-scm.com/docs)
- 🐙 [GitHub Guides](https://guides.github.com/)
- 💬 [Stack Overflow Git Tag](https://stackoverflow.com/questions/tagged/git)

## 📊 Zusammenfassung / Summary

| Ressource | Zweck / Purpose | Zielgruppe / Audience |
|-----------|----------------|---------------------|
| BRANCH_MANAGEMENT_*.md | Vollständige Anleitung / Complete guide | Alle / All |
| QUICK_REFERENCE_BRANCHES.md | Schnelle Befehle / Quick commands | Fortgeschrittene / Advanced |
| BRANCH_WORKFLOW.md | Visuelle Workflows / Visual workflows | Anfänger / Beginners |
| close_branches.sh | Linux/Mac Skript / Linux/Mac script | Alle / All |
| close_branches.bat | Windows Skript / Windows script | Alle / All |
| manage_current_branch.bat | Erweiterte Verwaltung / Advanced management | Fortgeschrittene / Advanced |

## 🎓 Lernpfad / Learning Path

### Stufe 1: Anfänger / Level 1: Beginner
1. Lesen Sie [BRANCH_WORKFLOW.md](BRANCH_WORKFLOW.md)
2. Verwenden Sie die interaktiven Skripte
3. Üben Sie mit einem Test-Repository

### Stufe 2: Fortgeschritten / Level 2: Intermediate
1. Lernen Sie die [Schnellreferenz](QUICK_REFERENCE_BRANCHES.md)
2. Experimentieren Sie mit Git-Befehlen
3. Verstehen Sie Merge-Status

### Stufe 3: Experte / Level 3: Expert
1. Lesen Sie die [vollständige Dokumentation](BRANCH_MANAGEMENT_DE.md)
2. Automatisieren Sie mit eigenen Skripten
3. Integrieren Sie in CI/CD-Pipelines

## 🌟 Best Practices

### 🇩🇪 Deutsch
1. ✅ **Regelmäßig aufräumen** - Löschen Sie alte Feature-Branches
2. ✅ **Merge vor dem Löschen** - Stellen Sie sicher, dass Änderungen integriert sind
3. ✅ **Beschreibende Namen** - Verwenden Sie klare Branch-Namen
4. ✅ **Team koordinieren** - Informieren Sie andere vor Remote-Löschungen
5. ✅ **Dokumentieren** - Halten Sie fest, warum Branches gelöscht wurden

### 🇬🇧 English
1. ✅ **Regular cleanup** - Delete old feature branches
2. ✅ **Merge before deleting** - Ensure changes are integrated
3. ✅ **Descriptive names** - Use clear branch names
4. ✅ **Coordinate with team** - Inform others before remote deletions
5. ✅ **Document** - Record why branches were deleted

---

## 📝 Version & Lizenz / Version & License

**Version**: 1.0.0  
**Datum / Date**: 2025-12-28  
**Autor / Author**: Johann Pascher  
**E-Mail**: johann.pascher@gmail.com  
**Lizenz / License**: © 2025 Johann Pascher. Alle Rechte vorbehalten / All rights reserved.

---

*Erstellt für das T0-Time-Mass-Duality Projekt*  
*Created for the T0-Time-Mass-Duality project*  
🔗 https://github.com/jpascher/T0-Time-Mass-Duality
