# Copilot Task: Fix LaTeX Errors and Compile T0_Anwendungen Masters (Kindle-Compatible)

Branch: `copilot/reset-copilot-narrative`  
Base directory: `2/narrative`

Ziel: Alle LaTeX-Fehler in den **T0_Anwendungen**-Kapiteldateien beheben und anschließend die beiden Master-Dokumente

- `2/narrative/de_standalone/T0_Anwendungen_De.tex`
- `2/narrative/en_standalone/T0_Anwendungen_En.tex`

vollständig und **Kindle/KDP-kompatibel** kompilieren (analog zu den Narrative-Mastern).

---

## 1. Geltungsbereich

### 1.1 Master-Dokumente

- Deutsch: `2/narrative/de_standalone/T0_Anwendungen_De.tex`
- Englisch: `2/narrative/en_standalone/T0_Anwendungen_En.tex`

Diese binden kapitelweise Dateien ein (`*_De_ch.tex`, `*_En_ch.tex`).

### 1.2 Kapiteldateien

- Deutsche Kapitel (neu):
  - `2/narrative/de_chapters_new/*.tex`, insbesondere:
    - `028_T0_7-fragen-3_De_ch.tex`
    - `029_T0_threeclock_De_ch.tex`
    - `030_T0_penrose_De_ch.tex`
    - `036_T0_peratt_De_ch.tex`
    - `037_Hannah_De_ch.tex`
    - `038_Markov_De_ch.tex`
    - `039_Zwei-Dipole-CMB_De_ch.tex`
- Englische Kapitel (falls analog vorhanden):
  - `2/narrative/en_chapters_new/*.tex`

**Wichtig:**
- Nur diese Kapitel- und Masterdateien bearbeiten.  
- Narrative-Master (`FFGFT_Narrative_Master_*.tex`) und deren Kapitel **nicht** verändern.

---

## 2. Fehlerklassen, die zu beheben sind

### 2.1 Kritische LaTeX-Fehler (müssen 0 werden)

Behebe alle Fehler, die das Kompilieren stoppen, insbesondere:

1. **`Improper \halign inside $$\'s. \end{align}`** (mehrfach in z.B. `028_T0_7-fragen-3_De_ch.tex`, `030_T0_penrose_De_ch.tex`, `037_Hannah_De_ch.tex`, `039_Zwei-Dipole-CMB_De_ch.tex`)
   - Ursache: Tabellen/Align-Strukturen innerhalb von `$$ ... $$` oder verschachtelte Align/Tabellen in Math-Modus.  
   - Maßnahmen:
     - Suche in den betroffenen Kapiteln nach `$$` und entferne sie konsequent.
     - Ersetze `$$ ... $$` durch:
       - `\[ ... \]` **oder**
       - eine passende Umgebung wie `equation`, `align`, `gather` etc.
     - Stelle sicher, dass `\begin{align} ... \end{align}` **nicht** innerhalb von `$$ ... $$` steht.
     - Falls Tabellen mit `&` Spalten in Mathe-Modus stehen:
       - Verwende `\begin{align}` / `\begin{aligned}` im Math-Modus **oder** `tabular`/`array` außerhalb von `$$` mit sauberer Umgebung.

2. **`Command \textdegree invalid in math mode`** (u.a. in `030_T0_penrose_De_ch.tex`)
   - In Math-Umgebungen `\textdegree` **nicht** verwenden.  
   - Maßnahmen:
     - In Formeln: ersetze `\textdegree` durch `^{\circ}` oder `\ang{...}` (siunitx) je nach Kontext.
     - Im Fließtext (außerhalb von `$...$`): `\textdegree` ist ok, ggf. mit kleinem Abstand `\textdegree\,`.

3. **Sonstige harte Fehler**
   - Unbalancierte `\begin{...}` / `\end{...}`.  
   - Nicht geschlossene Klammern `{ ... }`.  
   - Falsche Umgebungskombinationen.

Ziel: **Kein einziger `! LaTeX Error: ...`** mehr beim Kompilieren der beiden Master.

### 2.2 Wichtige Layout-/KDP-Vorgaben (analog zur Narrative-Kindle-Konfiguration)

- Seitenlayout **nicht verändern** (wird durch `T0_preamble_shared_*.tex` vorgegeben; enthält 6"x9"-Layout und Kindle-Optimierung).
- Es dürfen **keine Overfull \hbox**-Warnungen übrig bleiben, die sichtbar über den Rand hinaus laufen.  
  - Bei Overfull-Boxen:
    - Zeilen sinnvoll umbrechen oder Formulierungen leicht umstellen.
    - `\allowbreak` oder `\linebreak` an geeigneten Stellen verwenden (sparsam).
- Keine `\resizebox{\textwidth}{!}{...}`-Konstruktionen, die Tabellen breiter als den Text machen.  
  - Tabellen an **Textbreite** ausrichten.

### 2.3 Warnungen, die akzeptabel sind

- **Undefinierte Zitationen** (`Citation ... undefined`) in den Anwendungen-Kapiteln dürfen vorerst bleiben.  
- PDF-String-Warnungen (Math in Bookmarks) sind tolerierbar, solange sie keine Fehler verursachen.

---

## 3. Vorgehen zur Fehlerbehebung

1. **Log-Analyse pro Master:**
   - Kompiliere zunächst lokal (im Repo):
     ```bash
     cd 2/narrative/de_standalone
     pdflatex -interaction=nonstopmode T0_Anwendungen_De.tex || true
     ```
   - Lies das `.log` und identifiziere alle **Fehler** und relevanten **Warnungen** (siehe Liste oben).
   - Notiere die betroffenen Kapiteldateien und Zeilennummern.

2. **Kapitelweise Korrektur:**
   - Öffne jede genannte Kapiteldatei (`*_De_ch.tex`, ggf. `*_En_ch.tex`).
   - Behebe die Fehler **minimal-invasiv**, d.h.:
     - Inhalt/Semantik **nicht** ändern.
     - Nur LaTeX-Struktur reparieren (Umgebungen, Math-Modus, Gradzeichen, `$$` → `equation`/`align` usw.).

3. **Erneutes Kompilieren nach Fixes:**
   - Nach einem Satz von Korrekturen:
     ```bash
     cd 2/narrative/de_standalone
     for i in 1 2 3 4; do
       pdflatex -interaction=nonstopmode T0_Anwendungen_De.tex || true
     done
     ```
   - Prüfe im `.log`:
     - Kein `Improper \halign inside $$\'s` mehr.
     - Keine `Command \textdegree invalid in math mode`-Fehler.
     - Keine weiteren harten LaTeX-Fehler.
     - Overfull-Boxen beseitigt (insbesondere in Tabellen, Formeln, langen URLs).

4. **EN-Master (falls vorhanden) analog behandeln:**
   - Für `T0_Anwendungen_En.tex` entsprechend verfahren:
     ```bash
     cd 2/narrative/en_standalone
     for i in 1 2 3 4; do
       pdflatex -interaction=nonstopmode T0_Anwendungen_En.tex || true
     done
     ```
   - Auch hier: alle harten Fehler beseitigen, Overfull-Boxen verhindern; Semantik nicht ändern.

---

## 4. Kindle/KDP-Kompatibilitätsregeln (aus den Narrative-Dokumenten übernehmen)

- Papiersize: **6" x 9"** (bereits in der gemeinsamen Preambel konfiguriert) – **nicht ändern**.
- Ränder: Beibehalten (inner/outer/top/bottom wie in `T0_preamble_shared_*.tex`).
- Textfluss: Einstellungen wie `\sloppy`, `\emergencystretch`, `\tolerance` etc. aus der Preambel **nicht** entfernen.
- Mathe:
  - Nutze `\displaystyle` bei Bedarf (bereits vorkonfiguriert) für bessere Lesbarkeit.
  - Kein Inhalt darf über den Rand hinausragen.

---

## 5. Abschlussprüfungen

1. **Fehlerfreiheit:**
   - Beide Master (`T0_Anwendungen_De.tex`, `T0_Anwendungen_En.tex`) kompilieren ohne **irgendeinen** `! LaTeX Error`.

2. **Layout-Konsistenz:**
   - Keine Overfull-Boxen in den finalen Logs (besonders in den zuvor problematischen Kapiteln 028, 029, 030, 036, 037, 038, 039).

3. **PDF-Erzeugung:**
   - Die entstandenen PDFs werden **nicht** eingecheckt (sie sollten durch `.gitignore` ausgeschlossen sein).

4. **Commit & Push:**
   - Füge nur die geänderten Kapitel- und Masterdateien hinzu:
     - `2/narrative/de_chapters_new/*.tex`
     - `2/narrative/en_chapters_new/*.tex` (falls betroffen)
     - `2/narrative/de_standalone/T0_Anwendungen_De.tex`
     - `2/narrative/en_standalone/T0_Anwendungen_En.tex`
   - Commit-Message (Vorschlag):
     - `Fix LaTeX errors in T0_Anwendungen chapters and compile DE/EN masters`
   - Push nach `copilot/reset-copilot-narrative`.

---

## 6. Erwartetes Ergebnis

- Beide Master-Dokumente `T0_Anwendungen_De.tex` und `T0_Anwendungen_En.tex` lassen sich mehrfach fehlerfrei kompilieren.  
- Alle gemeldeten `Improper \halign inside $$'s`- und `\textdegree`-Fehler sind behoben.  
- Keine sichtbaren Layout-Probleme (insbesondere keine Overfull-Boxen) verbleiben – die Dokumente sind für Kindle/KDP geeignet.

