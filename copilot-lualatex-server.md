# Copilot: Server-seitige LuaLaTeX-Kompilierung (GitHub Actions)

Dieses Dokument beschreibt, wie GitHub Copilot die **server-seitige** LaTeX-Kompilierung mit **LuaLaTeX** über GitHub Actions steuern und für einen iterativen Fehlerbehebungsprozess nutzen soll.

## 1. Ziel

- Alle Standalone-Dokumente unter `2/tex-n/de_standalone` und `2/tex-n/en_standalone` sollen **auf dem GitHub-Server** mit `lualatex` kompiliert werden.
- Fehler (fehlende Pakete, Preambel-Probleme, Sprachpakete) werden **über die CI-Logs** identifiziert und anschließend durch Commits im Repo behoben.
- Der Prozess soll iterativ laufen, bis alle Standalone-Dokumente wieder fehlerfrei kompilieren.

## 2. Relevanter Workflow

- Workflow-Datei: `.github/workflows/latex-standalone-ci.yml`
- Name im GitHub UI: **"LaTeX Standalone (LuaLaTeX)"**
- Trigger:
  - `workflow_dispatch` (manuell auslösbar im GitHub UI)
  - `push` auf Dateien in:
    - `2/tex-n/de_standalone/**.tex`
    - `2/tex-n/en_standalone/**.tex`
    - `compile_standalone_recursive.sh`

## 3. Was der Workflow auf dem Server macht

1. Checkt das Repository aus.
2. Installiert eine TeX-Live-Basis mit LuaLaTeX und Sprachpaketen:
   - `texlive-latex-recommended`, `texlive-latex-extra`
   - `texlive-lang-german`, `texlive-lang-english`
   - `texlive-fonts-recommended`, `texlive-luatex`, `latexmk`
3. Führt `./compile_standalone_recursive.sh` aus (mit `lualatex`).
4. Sammelt alle Log-Dateien aus `/tmp` (`*_compile.log` und `recursive_compilation.log`) und lädt sie als Artifact **`standalone-lualatex-logs`** hoch.
5. Schlägt fehl (`exit 1`), falls in `recursive_compilation.log` mindestens ein Dokument mit `FAILED:` markiert wurde.

## 4. Arbeitsweise für Copilot (iterativer Prozess)

Copilot soll folgenden Ablauf verwenden, wenn Standalone-Dokumente repariert werden müssen:

1. **Workflow auslösen** (vom Nutzer im GitHub-Webinterface oder via `gh workflow run`).
2. **Auf Abschluss des Jobs warten** und dann das Artifact **`standalone-lualatex-logs`** herunterladen.
3. Aus den Log-Dateien:
   - Für jedes `*_compile.log` die ersten relevanten Fehlerblöcke (`^!`-Zeilen und 3–5 Folgezeilen) analysieren.
   - Typische Fehler identifizieren:
     - Fehlende Pakete (z.B. `Package xxx Error: ...`)
     - Encoding-/Font-Probleme (LuaLaTeX-spezifisch)
     - Preambel-/Klassenfehler (z.B. falsche Dokumentklasse, inkompatible Optionen)
4. **Gezielte Korrekturen vornehmen**:
   - LaTeX-Quelle unter `2/tex-n/de_standalone` oder `2/tex-n/en_standalone` minimal anpassen.
   - Falls nötig, Preambel-Dateien (`T0_preamble*_*.tex` oder neue `T0_preamble-o_*`) korrigieren.
   - Keine inhaltlichen Änderungen – nur technische Fixes (Pakete, Encoding, Layout).
5. Änderungen committen und nach `origin/main` pushen.
6. Workflow erneut starten und prüfen, ob sich die Anzahl der `FAILED:`-Einträge in `recursive_compilation.log` reduziert hat.
7. Solange wiederholen, bis **keine `FAILED:`-Zeilen** mehr auftreten.

## 5. Hinweise zu Paketen und Sprachen

- Primärer Compiler: **LuaLaTeX** (`lualatex`).
- Standardmäßig installierte Pakete auf dem GitHub-Runner:
  - Siehe Schritt "Install TeX Live" im Workflow (`texlive-latex-recommended`, `texlive-latex-extra`, Sprachpakete, Fonts, LuaTeX).
- Wenn in Logs fehlende Pakete erscheinen (z.B. `csquotes`, `babel`, `polyglossia`, `microtype`, `fontspec`):
  - Copilot soll **zuerst** versuchen, die Preambel so anzupassen, dass Standard-Paketkombinationen für LuaLaTeX verwendet werden (z.B. `fontspec` statt `inputenc`/`fontenc`).
  - Nur wenn absolut nötig, darf der Workflow erweitert werden, um zusätzliche TeX-Live-Pakete via `apt-get install texlive-*` nachzuinstallieren.

## 6. Konkrete Nutzung durch den Nutzer

- Um alle Standalone-Dokumente auf dem GitHub-Server zu testen:
  1. Änderungen committen und nach `origin/main` pushen.
  2. Im GitHub-Repository unter **Actions** den Workflow **"LaTeX Standalone (LuaLaTeX)"** auswählen.
  3. Auf **"Run workflow"** klicken, ggf. Branch `main` bestätigen.
  4. Nach Abschluss des Jobs das Artifact **`standalone-lualatex-logs`** herunterladen und Copilot zur Auswertung geben.

- Copilot kann dann auf Basis der Log-Inhalte gezielt LaTeX-Dateien im Repo anpassen und den Workflow erneut ausführen lassen, bis der Build grün ist.
