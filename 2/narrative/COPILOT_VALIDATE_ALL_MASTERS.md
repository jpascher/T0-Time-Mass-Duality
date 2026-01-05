# Copilot Task: Recursively Validate and Fix All FFGFT Documents

Branch: `copilot/reset-copilot-narrative`  
Base directory: `2/narrative`

Ziel: Sicherstellen, dass **alle relevanten FFGFT-Dokumente** (DE und EN) nach den Umbenennungen von T0-Theorie → FFGFT **sauber kompilieren**.  
Wenn Fehler auftreten, wurden sie mit hoher Wahrscheinlichkeit durch die Text-Ersetzungen ausgelöst und müssen gezielt behoben werden, **ohne** die mathematischen Inhalte oder das 6x9"-Kindle-Layout zu ändern.

---

## 1. Zu prüfende Hauptdokumente

Derzeit bekannte Master im Verzeichnis `2/narrative`:

1. **Anwendungen Deutsch (DE):**
   - `2/narrative/completted/T0_Anwendungen_De.tex`
   - bindet Kapitel aus `2/narrative/de_chapters_new/*.tex` ein

2. **Anwendungen Englisch (EN):**
   - `2/narrative/completted/T0_Anwendungen_En.tex`
   - bindet Kapitel aus `2/narrative/en_chapters_new/*.tex` ein

Falls weitere Narrative-Master für FFGFT existieren (z.B. unter `2/narrative/*Narrative*_*.tex`), wende dieselbe Strategie rekursiv an. **Die Dateinamen müssen aktuell nicht umbenannt werden**, nur der Inhalt muss konsistent sein.

---

## 2. Allgemeine Regeln

1. **LaTeX-Struktur nicht verändern:**
   - Belasse `\documentclass`, `\input{../../../T0_preamble_shared_*}` und alle Kindle-/Geometry-Einstellungen **unverändert**.
   - Die gemeinsame Preambel stellt das 6x9"-Layout und alle Physik-/Mathepakete bereit.

2. **Nur Text-Folgen korrigieren, keine Formeln:**
   - Wenn Fehler auftreten, zuerst prüfen, ob sie von Ersetzungen in Überschriften, Tabellenköpfen oder Fließtext stammen (z.B. zusätzliche Klammern, `\\` in `\textbf{...}` usw.).
   - Mathematische Ausdrücke, Symbole, Indizes (`T_0`, `T0`, `\xi`, etc.) **nicht semantisch verändern**.

3. **Keine Änderung der Page-Styles außer explizit gewünscht:**
   - `T0_Anwendungen_De.tex` und `T0_Anwendungen_En.tex` verwenden aktuell `\pagestyle{plain}`, d.h. **keine fancy Kopfzeile**, aber **Seitenzahlen im Fuß**.  
   - Diesen Zustand **beibehalten**.

---

## 3. Kompilationsstrategie (rekursiv & iterativ)

### 3.1 Grundschleife

Für beide Master (**DE** und **EN**) führe folgende Schleife aus:

```bash
cd 2/narrative/completted

for i in 1 2 3; do
  pdflatex -interaction=nonstopmode T0_Anwendungen_De.tex || true
  pdflatex -interaction=nonstopmode T0_Anwendungen_En.tex || true
done
```

Anschließend:

- Durchsuche die `.log`-Dateien (`T0_Anwendungen_De.log`, `T0_Anwendungen_En.log`) nach:
  - `! LaTeX Error:`
  - `Missing } inserted`
  - `Extra }, or forgotten \endgroup`
  - `Undefined control sequence`

### 3.2 Fehler-Quellen lokalisieren

1. Wenn ein Fehler gemeldet wird (z.B. in `028_T0_7-fragen-3_*.tex`, `030_T0_penrose_*.tex` usw.):
   - Öffne die angegebene Kapiteldatei unter:
     - DE: `2/narrative/de_chapters_new/<Datei>.tex`
     - EN: `2/narrative/en_chapters_new/<Datei>.tex`

2. Typische Fehler nach den Umbenennungen / Textänderungen:
   - Zeilenumbrüche `\\` innerhalb von `\textbf{...}` oder Tabellenköpfen vor einem `&` (führt zu `Missing } inserted`).
   - Unbalancierte Klammern `{` / `}` nach eingefügten Zusätzen wie "früher bekannt als ...".
   - Zu lange Tabellenköpfe nach erweiterter Bezeichnung von FFGFT (Overfull-Boxen).

3. **Behebung:**
   - **Behalte den Sinn der Formulierung**, aber repariere die LaTeX-Syntax:
     - Verwende z.B. `\shortstack{... \\ ...}` für zweizeilige Tabellenüberschriften, statt roher `\\` in `\textbf{}`.
     - Kürze Formulierungen leicht, wenn sie Tabellen zu breit machen (semantisch gleich lassen).

4. Nach jeder Korrektur:
   - Erneut den jeweiligen Master 2–3 Mal kompilieren.
   - Solange wiederholen, bis kein LaTeX-Fehler mehr auftritt.

---

## 4. Spezifische Prüfungen nach dem globalen T0→FFGFT-Umbenennen

Nachdem alle Ersetzungen laut `COPILOT_RENAME_T0_TO_FFGFT.md` durchgeführt wurden:

1. **DE-Master:** `T0_Anwendungen_De.tex`
   - Prüfen, ob:
     - Einleitung und Kapiteltexte die neue Bezeichnung **Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT)** verwenden.
     - Genau **eine** klare Übergangsformulierung enthalten ist ("früher als T0-Theorie ... bekannt").
     - Alle Kapitel fehlerfrei eingebunden sind (keine `! LaTeX Error` im Log).

2. **EN-Master:** `T0_Anwendungen_En.tex`
   - Prüfen, ob:
     - Einleitung und Kapiteltexte die neue Bezeichnung **Fundamental Fractal-Geometric Field Theory (FFGFT)** verwenden.
     - Genau **eine** klare Übergangsformulierung enthalten ist ("previously known as T0 theory ...").
     - Alle Kapitel fehlerfrei eingebunden sind.

3. **Overfull-Boxen minimieren:**
   - Insbesondere in Tabellen mit langen neuen Begriffen (z.B. FFGFT-Ausschreibung) sicherstellen, dass keine sichtbaren Overfull-\hbox-Fehler auftreten.  
   - Falls erforderlich: leichte Umformulierungen oder `\shortstack` nutzen, bis die Tabelle auf Seitenbreite passt.

---

## 5. Abschluss & Commit

Wenn beide Master **ohne LaTeX-Fehler** kompilieren und nur tolerierbare Warnungen (z.B. fehlende Zitate, Unicode in Bookmarks) verbleiben:

1. Stelle sicher, dass folgende Dateien im Commit enthalten sind:

   - `2/narrative/completted/T0_Anwendungen_De.tex`
   - `2/narrative/completted/T0_Anwendungen_En.tex`
   - Alle geänderten Kapitel:
     - `2/narrative/de_chapters_new/*.tex`
     - `2/narrative/en_chapters_new/*.tex`

2. Commit-Message (Vorschlag):

   - `Fix LaTeX errors after T0→FFGFT rename and validate DE/EN applications`

3. Push nach:

   - `copilot/reset-copilot-narrative`

---

## 6. Ergebnis

- Alle Kapitel- und Master-Dokumente (DE/EN) der FFGFT-Anwendungen kompilieren **fehlerfrei** im 6x9"-Format.  
- Alle Fehler, die durch die T0→FFGFT-Textumbenennungen entstanden sind, wurden gezielt in den jeweiligen Kapiteldateien behoben, ohne die mathematischen Inhalte zu verändern.  
- Die PDFs im Verzeichnis `2/narrative/completted` sind konsistent und KDP-tauglich.

