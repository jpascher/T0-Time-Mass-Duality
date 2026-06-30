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

## 7. Beispiel: Installation von LuaLaTeX, Sprachpaketen und siunitx (Ubuntu)

Auf einem GitHub-Actions-Runner oder einem vergleichbaren Ubuntu-System soll Copilot
vor der ersten Kompilierung ein vollständiges LuaLaTeX-Setup installieren, inkl.
Sprachpaketen und **siunitx**:

```bash
sudo apt-get update
sudo apt-get install -y \
 texlive-latex-recommended \
 texlive-latex-extra \
 texlive-fonts-recommended \
 texlive-fonts-extra \
 texlive-luatex \
 texlive-lang-german \
 texlive-lang-english \
 texlive-science \
 latexmk
```

Hinweise:
- Das Paket **siunitx** wird über die TeX-Live-Sammlung (z.B. `texlive-science`)
 bereitgestellt und muss in den relevanten Preambeln mit
 `\usepackage{siunitx}` geladen werden, falls dort noch nicht vorhanden.
- Für weitere Sprachen (z.B. Französisch) sind die entsprechenden
 `texlive-lang-*`-Pakete analog nachzuinstallieren.

## 8. Preambel-Normalisierung und rekursive Standalone-Kompilation

Dieser Abschnitt beschreibt, wie Copilot auf dem Server alle Standalone-Dokumente
vereinheitlicht (Preambeln) und anschließend rekursiv mit LuaLaTeX kompiliert.

### 8.1 Ziel

- Alle `.tex`-Dateien unter `2/tex-n/de_standalone` und `2/tex-n/en_standalone`
 sollen konsistent externe LuaLaTeX-Preambeln verwenden.
- Danach sollen alle betroffenen Dokumente (mit Ausnahme bekannter Sonderfälle)
 rekursiv mit LuaLaTeX kompiliert und die PDFs nach `2/pdf` geschrieben werden.

### 8.2 Preambel-Prüfung in den Standalone-Verzeichnissen

Copilot soll alle `.tex`-Dateien in `2/tex-n/de_standalone` und
`2/tex-n/en_standalone` nach der Art der Preambel-Einbindung durchsuchen:

- **Korrekte externe Preambeln (nicht ändern):**
 - `\input{../../../T0_preamble_shared-ebook_De}` bzw. `..._En`
 - `\input{../../../T0_preamble_shared_De}` bzw. `..._En`
- **Eigene/alte Preambeln (anpassen):**
 - Direkte Paketladungen im Dokumentkopf wie
  `\usepackage[utf8]{inputenc}`, `\usepackage[T1]{fontenc}`,
  `\usepackage{lmodern}` usw.
 - Einbindung lokaler oder FFGFT-spezifischer Preambeln, z.B.:
  - `\input{T0_preamble_De}` / `\input{T0_preamble_En}`
  - `\input{../T0_preamble_shared_De.tex}` /
   `\input{../T0_preamble_shared_En.tex}`
  - andere Varianten, die **nicht** auf die globalen
   `T0_preamble_shared(-ebook)_*.tex` im Repo-Root verweisen.

### 8.3 Preambel-Umstellung in betroffenen Standalone-Dokumenten

Für jedes Standalone-Dokument mit eigener/alter Preambel gilt:

1. Der `\documentclass`-Eintrag (z.B. `article`, `report`) darf bestehen bleiben.
2. Direkt nach `\documentclass` soll eine der globalen LuaLaTeX-Preambeln
  eingebunden werden:
  - DE: `\input{../../../T0_preamble_shared-ebook_De}`
  - EN: `\input{../../../T0_preamble_shared-ebook_En}`
3. Alle internen `\usepackage{...}`-Blöcke, die Standardpakete wie
  `inputenc`, `fontenc`, `lmodern` oder doppelte Sprach-/Font-Konfigurationen
  laden, werden entfernt oder auskommentiert, sofern sie bereits durch die
  globale Preambel abgedeckt sind.
4. Falls ein Dokument zusätzliche FFGFT-spezifische Makros aus älteren
  Preambeln benötigt:
  - Lege eine kleine Zusatzdatei an, z.B.:
   - `2/tex-n/de_standalone/ffgft_macros_De.tex`
   - `2/tex-n/en_standalone/ffgft_macros_En.tex`
  - Übertrage **nur** die benötigten Makrodefinitionen (z.B. `t0box` u.ä.)
   in diese Dateien.
  - Binde diese Datei nach der globalen Preambel ein, z.B. mit
   `\input{ffgft_macros_De}` bzw. `\input{ffgft_macros_En}`.

### 8.4 Bekannte Ausnahme-Dokumente (201er FFGFT)

Die folgenden Dateien sind inhaltlich/strukturell bekannt problematisch und
sollen im aktuellen Durchlauf **nicht** als Kompilationsziele verwendet werden
(nur optionale Preambel-Angleichung ist erlaubt):

- `2/tex-n/de_standalone/201_FFGFT-alles_De.tex`
- `2/tex-n/de_standalone/201a_FFGFT-alles_De.tex`
- `2/tex-n/en_standalone/201_FFGFT-alles_En.tex`
- `2/tex-n/en_standalone/201a_FFGFT-alles_En.tex`

Wenn Skripte wie `compile_standalone_recursive.sh` diese Dateien standardmäßig
antasten, sollen sie beim Kompilieren explizit übersprungen und als
"known failing / excluded" dokumentiert werden.

### 8.5 Rekursive LuaLaTeX-Kompilation der Standalone-Dokumente

Nach der Preambel-Normalisierung soll Copilot auf dem Server folgendes tun:

1. Sicherstellen, dass die TeX-Umgebung wie in Abschnitt 7 installiert ist.
2. Das Skript `compile_standalone_recursive.sh` aus dem Repository-Root
  ausführen.
3. Prüfen, dass das Skript pro Dokument ein `*_compile.log` und eine
  `recursive_compilation.log` erzeugt und bei Erfolg die PDFs nach
  `2/pdf/<basename>.pdf` kopiert.
4. Verbleibende Fehler aus den Log-Dateien analysieren und **minimal-invasive**
  LaTeX-Fixes vornehmen (fehlende Pakete, Optionen, LuaLaTeX-spezifische
  Anpassungen), ohne physikalische Inhalte zu verändern.
5. Für betroffene Dateien den Kompilationslauf erneut starten, bis sie
  fehlerfrei durchlaufen.

### 8.6 Commits

Copilot soll die Änderungen in klar getrennten Commits bündeln, z.B.:

- `Normalize standalone preambles to shared LuaLaTeX (DE/EN)`
- `Fix LuaLaTeX compilation for problematic standalone documents`

Diese Commits werden anschließend auf den jeweils aktiven Branch
(z.B. `copilot/fix-latex-standalone-compile`) gepusht.

