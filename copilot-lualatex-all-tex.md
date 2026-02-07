# Copilot Instructions: Alle LaTeX-Dokumente rekursiv bereinigen und kompilieren

Diese Datei beschreibt, wie ein Copilot‑Agent (z.B. auf GitHub Actions) **alle relevanten LaTeX‑Quellen** im Repository rekursiv bereinigt und mit **LuaLaTeX** kompiliert, ohne PDFs zu löschen.

## 1. Ziel

- Finde alle LaTeX‑Dateien, die **eigenständige Dokumente** sind (mit `\\documentclass`).
- Kompiliere jedes dieser Dokumente mit LuaLaTeX (vorzugsweise über `latexmk -lualatex`).
- Lege alle PDFs an den projektüblichen Orten ab (insb. unter `2/pdf`) **ohne bestehende PDFs zu löschen**.
- Bereinige rekursiv nur **LaTeX‑Fehler**, insbesondere durch frühere automatische Edits (Claude), mit minimalen Änderungen an den Quellen.

## 2. Benötigte LaTeX-Umgebung (GitHub Actions / Linux)

Installiere eine vollständige LuaLaTeX‑Umgebung (analog zu den bestehenden Copilot‑Anleitungen):

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

Annahmen:

- Kompilation mit `latexmk -lualatex -interaction=nonstopmode -halt-on-error`.
- Preambeln nutzen `fontspec` und sind bereits auf LuaLaTeX abgestimmt (siehe bestehende Preambel‑Dateien wie `T0_preamble_shared_*.tex`).

## 3. Suchraum für LaTeX-Dokumente

Betrachte mindestens folgende Verzeichnisse:

- `2/tex-n` (Bücher, Standalones, Tabellen, FFGFT‑Dokumente)
- `2/narrative` (Narrative FFGFT‑Bücher und Kapitel)

Innerhalb dieser Verzeichnisse:

- Unterscheide zwischen **Master‑/Standalone‑Dokumenten** (mit `\\documentclass`) und **Kapitel‑Schnipseln** (ohne `\\documentclass`).
- Nur Dateien mit `\\documentclass` werden direkt kompiliert; Kapitel werden über ihre jeweiligen Master‑Dokumente eingebunden.

Beispiele für bereits definierte Master‑Dokumente (siehe andere Copilot‑Anleitungen):

- Narrative:
 - `2/narrative/FFGFT_Narrative_Master_De.tex`
 - `2/narrative/FFGFT_Narrative_Master_En.tex`
- Bücher (fertige Manuskripte):
 - `2/tex-n/completed/Teil1a_De.tex`, `Teil1a_En.tex`, `Teil2_*.tex`, `Teil3_*.tex`, `T0_Anwendungen_*.tex`
- Diverse Standalone‑Dokumente (z.B. in `2/tex-n/de_standalone`, `2/tex-n/en_standalone`, `2/tex-n/*_standalone_pdflatex`).

## 4. Automatisches Auffinden der zu kompilierenden Dokumente

1. Wechsle ins Repository‑Root:

  ```bash
  cd "$GITHUB_WORKSPACE"
  ```

2. Erzeuge eine Liste aller potentiell eigenständigen Dokumente unter `2/`:

  ```bash
  find 2 -name "*.tex" -print0 | \
   xargs -0 rg -n "^\\\documentclass" --glob "*.tex" --no-messages \
   > tex_documentclass_files.txt
  ```

  - Jede Zeile enthält Pfad + Zeilennummer + die `\\documentclass`‑Zeile.

3. Extrahiere die eindeutigen Dateipfade:

  ```bash
  cut -d":" -f1 tex_documentclass_files.txt | sort -u > tex_master_files.txt
  ```

4. Optional: Filtere (falls nötig) Dateien heraus, die **nur als Kapitel** gedacht sind und über bekannte Master‑Dokumente inkludiert werden (siehe projektinterne Konventionen). Standardmäßig können aber alle in `tex_master_files.txt` aufgeführten Dateien nacheinander kompiliert werden.

## 5. Kompilationsstrategie (rekursives Bereinigen)

Für jede Datei `F` in `tex_master_files.txt`:

1. Bestimme ein sinnvolles Ausgabe‑Verzeichnis:

  - Für Narrative‑Master: `2/pdf`
  - Für fertige Bücher unter `2/tex-n/completed`: ebenfalls `2/pdf`
  - Für Standalones: entweder `2/pdf` oder ein lokales Unterverzeichnis (z.B. `2/tex-n/pdf_standalone`), **ohne bestehende PDFs zu löschen**.

  Beispiel (einfacher globaler Ansatz):

  ```bash
  outdir="2/pdf"
  mkdir -p "$outdir"

  while read -r F; do
   latexmk -lualatex -interaction=nonstopmode -halt-on-error \
    -output-directory="$outdir" "$F" || echo "Kompilationsfehler in $F" >> tex_compile_errors.txt
  done < tex_master_files.txt
  ```

2. **Wichtig:**

  - Keine PDFs löschen (weder vor noch nach der Kompilation).
  - Wenn ein PDF bereits existiert, darf es **überschrieben**, aber nicht explizit gelöscht werden.

3. Bei Kompilationsfehlern (Dateien in `tex_compile_errors.txt`):

  - Öffne die zugehörige `.log`‑Datei im Ausgabeverzeichnis.
  - Identifiziere die erste signifikante Fehlermeldung (z.B. `Undefined control sequence`, `Missing \end{}`, Encoding‑Fehler).
  - Navigiere zur entsprechenden `.tex`‑Datei und führe **nur die minimal nötige Korrektur** durch.

## 6. Typische Claude-/Auto-Edit-Fehler bereinigen

Beim Bereinigen von Fehlern besonders auf folgende Muster achten (aus früheren Claude‑Edits bekannt):

- **Encoding‑Artefakte** in deutschen Texten (z.B. `k\u0000f6nnen`, `Verh\u0000e4ltnisse`):
 - Zurücksetzen auf gültige UTF‑8‑Umlaute oder klassische TeX‑Schreibweisen (`k\"onnen`, `Verh\"altnisse`).
- **Zerbrochene Befehle/Umgebungen**:
 - Unvollständige `\\begin{}`/`\\end{}`‑Paare.
 - Mischungen aus alten und neuen Preambeln.
- **Falsche oder doppelte `\\documentclass`‑Zeilen** bei Kapiteln, die eigentlich über einen Master eingebunden werden sollten.

Projekt­spezifische inhaltliche Richtlinien sind einzuhalten, z.B.:

- Detaillierte g‑2‑Formeln und numerische Vorhersagen gehören ausschließlich in die Anomalie‑Dokumente `018_T0_Anomale-g2-10_De.tex` / `018_T0_Anomale-g2-10_En.tex`.
- Andere Dokumente dürfen g-2 nur qualitativ erwähnen oder dorthin verweisen.

**Wichtig:** Physikalischer Inhalt und Argumentation sollen nicht verändert werden, außer wo explizit projektintern festgelegt (z.B. g‑2‑Zentralisierung); Fokus dieser Anleitung ist die **LaTeX‑Korrektur**.

## 7. Iteratives Vorgehen

1. Erster Durchlauf: Alle Master‑/Standalone‑Texte nach obigem Schema kompilieren; fehlschlagende Dateien in `tex_compile_errors.txt` sammeln.
2. Zweiter Durchlauf: Für jede fehlerhafte Datei:
  - `.log` analysieren,
  - minimal korrigieren,
  - erneut kompilieren.
3. Prozess wiederholen, bis **alle** Master‑/Standalone‑Dokumente ohne Fehler durchlaufen und ihre PDFs (neu) erzeugt wurden.

Dabei gilt immer:

- **Keine Quellen oder PDFs löschen oder umbenennen**, es sei denn, dies ist explizit durch das Projekt oder einen Maintainer angeordnet.
- Änderungen möglichst klein und klar begründet halten (z.B. in Commits: `Fix LuaLaTeX error in <Datei>`).

## 8. Ergebnis

Am Ende dieses Prozesses sollen:

- Alle eigenständig kompilierbaren LaTeX‑Dokumente im Repository mit LuaLaTeX auf GitHub gebaut worden sein.
- Alle zugehörigen PDFs an den vorgesehenen Orten (insb. `2/pdf`) vorliegen.
- Alle von Claude oder anderen Tools verursachten LaTeX‑Syntax‑ oder Encoding‑Fehler rekursiv und minimalinvasiv behoben sein.

## 9. Direkt einsetzbarer Prompt für den Copilot‑Assistenten

Den folgenden Prompt kannst du im GitHub‑Copilot‑Fenster (oder einem vergleichbaren Assistenten) auf `main` verwenden, um den hier beschriebenen Prozess auszuführen:

```text
Du bist ein LaTeX‑Build‑Assistent in meinem GitHub‑Repository. Bitte arbeite ausschließlich auf dem aktuellen Stand von `main` und führe alle Schritte im GitHub‑Runner aus, nicht lokal auf meinem Rechner.

Ziel:
- Alle eigenständig kompilierbaren LaTeX‑Dokumente (mit `\documentclass`) im Repository rekursiv finden, LaTeX‑Fehler minimal korrigieren und mit LuaLaTeX kompilieren.
- Besonders wichtig: Alle Standalone‑Dokumente (de/en, *_standalone, *_standalone_pdflatex) und alle Buch‑Master (unter `2/tex-n/completed` sowie Narrative‑Master unter `2/narrative`) sollen erfolgreich durchlaufen und ihre PDFs behalten/aktualisieren.
- PDFs dürfen überschrieben, aber nicht explizit gelöscht werden.

Vorgehen:
1. Wechsle ins Repo‑Root und stelle sicher, dass `main` aktuell ist:
  - `git checkout main`
  - `git pull --ff-only`
2. Installiere eine vollständige LuaLaTeX‑Umgebung:
  - `sudo apt-get update`
  - `sudo apt-get install -y texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra texlive-luatex texlive-lang-german texlive-lang-english texlive-science latexmk ripgrep`
3. Finde alle `.tex`‑Dateien mit `\documentclass` unterhalb von `2/`:
  - `cd "$GITHUB_WORKSPACE"`
  - `find 2 -name "*.tex" -print0 | xargs -0 rg -n "^\\documentclass" --glob "*.tex" --no-messages > tex_documentclass_files.txt`
  - `cut -d":" -f1 tex_documentclass_files.txt | sort -u > tex_master_files.txt`
4. Kompiliere alle in `tex_master_files.txt` gelisteten Dateien mit `latexmk -lualatex` in ein gemeinsames Ausgabe‑Verzeichnis (z.B. `2/pdf`), ohne PDFs zu löschen:
  - `mkdir -p 2/pdf`
  - `> tex_compile_errors.txt`
  - `while read -r F; do latexmk -lualatex -interaction=nonstopmode -halt-on-error -output-directory="2/pdf" "$F" || echo "$F" >> tex_compile_errors.txt; done < tex_master_files.txt`
5. Für jede Datei in `tex_compile_errors.txt`:
  - Öffne die `.log`‑Datei im Output‑Verzeichnis (`2/pdf`).
  - Finde die erste echte Fehlermeldung (`! LaTeX Error:`, `Undefined control sequence`, `Missing \end{}`, Encoding‑Fehler, etc.).
  - Korrigiere den Fehler direkt in der entsprechenden `.tex`‑Datei mit einer minimalen Änderung.
  - Kompiliere das betroffene Dokument erneut mit `latexmk -lualatex`.
  - Entferne die Datei aus `tex_compile_errors.txt`, sobald sie erfolgreich durchläuft.
6. Wiederhole Schritt 5 iterativ, bis `tex_compile_errors.txt` leer ist und alle Master‑/Standalone‑Dokumente ohne Fehler durchlaufen.

Inhaltliche/g‑2‑Spezialregeln:
- Detaillierte g‑2/anomale magnetische Momente‑Formeln, numerische Vorhersagen und genaue Werte dürfen nur in den zentralen Anomalie‑Dokumenten `018_T0_Anomale-g2-10_De.tex` und `018_T0_Anomale-g2-10_En.tex` stehen.
- In allen anderen Dokumenten sind Erwähnungen von g‑2 erlaubt, aber ohne falsche oder veraltete exakte Zahlenvorhersagen; bei Bedarf stattdessen qualitativ formulieren oder explizit auf das entsprechende Anomalie‑Dokument verweisen.
- Physikalischen Inhalt im Übrigen nicht verändern; der Fokus liegt ausschließlich auf der Beseitigung von LaTeX‑Fehlern und der korrekten Kompilation.

Wenn du Änderungen an `.tex`‑Dateien vornimmst, fasse sie in kleinen, sinnvollen Commits zusammen (z.B. `Fix LuaLaTeX error in <Dateiname>`) und pushe sie zurück auf `main`, sobald alle betroffenen Dokumente sauber durchkompiliert sind.
```

