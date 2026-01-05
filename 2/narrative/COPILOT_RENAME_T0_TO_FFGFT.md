# Copilot Task: Rename "T0-Theorie" to FFGFT in All Chapter Documents

Branch: `copilot/reset-copilot-narrative`  
Base directory: `2/narrative`

Ziel: Die Theorie, die bisher als **T0-Theorie (Time-Mass-Duality)** bezeichnet wurde, soll in allen relevanten Kapiteln und Master-Dokumenten konsistent in **FFGFT** umbenannt werden:

- Deutsch: **Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT)**  
- Englisch: **Fundamental Fractal-Geometric Field Theory (FFGFT)**

Dabei dürfen **mathematische Symbole** wie `T_0`, `T0` in Formeln oder Parametern **nicht verändert** werden.

---

## 1. Geltungsbereich

### 1.1 Deutsche Dokumente

Bearbeite mindestens:

- Kapitel (Anwendungen):
  - `2/narrative/de_chapters_new/*.tex`
- Master-Dokument Anwendungen (DE):
  - `2/narrative/completted/T0_Anwendungen_De.tex`
- Falls vorhanden und relevant: deutsche Narrative-Master und Kapitel (z.B. `2/narrative/de_standalone/...`), **ohne** dabei die Kindle-spezifische Preambel oder Seitengröße zu verändern.

### 1.2 Englische Dokumente

Bearbeite mindestens:

- Kapitel (Anwendungen):
  - `2/narrative/en_chapters_new/*.tex`
- Master-Dokument Anwendungen (EN):
  - `2/narrative/completted/T0_Anwendungen_En.tex`
- Falls vorhanden und relevant: englische Narrative-Master und Kapitel.

**Shared-Preambeln `T0_preamble_shared_*.tex` nicht umbenennen oder inhaltlich verändern**, außer es geht um reine Textteile (z.B. Beschreibung im Kommentar), die die Theorie benennen.

---

## 2. Umbenennungsregeln (Deutsch)

### 2.1 Grundformulierung

Neue Standardbezeichnung:

> **Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT)**

Ergänzende Einleitungssätze (z.B. für Einleitung, Klappentext, Vorwort):

> "Die Theorie, die früher als T0-Theorie (Time-Mass-Duality) bekannt war, wird nun einheitlich Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT) genannt."

### 2.2 Konkrete Ersetzungen

Suche in deutschen Kapiteln und Masters nach Formulierungen wie (nicht abschließend):

- `T0-Theorie`
- `T0 Theorie`
- `die T0-Theorie`
- `T0-Theorie der Zeit-Masse-Dualität`
- `T0-Theorie (Time-Mass-Duality)`
- `T0-Theorie der Time-Mass-Duality`

**Ersetze** wie folgt (sinngemäß, Grammatik beachten):

1. **Erste Nennung im Dokument (oder im Einleitungskapitel):**
   - Beispiel:
     ```latex
     Die T0-Theorie der Zeit-Masse-Dualität ...
     ```
   - Ersetze durch:
     ```latex
     Die Theorie, die früher als T0-Theorie (Time-Mass-Duality) bekannt war, wird nun einheitlich Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT) genannt. Im Folgenden sprechen wir kurz von der FFGFT.
     ```
   - Passe den Satzbau so an, dass der Text stilistisch flüssig bleibt.

2. **Weitere Vorkommen im Fließtext:**
   - `die T0-Theorie` → `die FFGFT`
   - `in der T0-Theorie` → `in der FFGFT`
   - `T0-Theorie-basiert` → `FFGFT-basiert`

3. **Überschriften und Kapitel-Titel (DE):**
   - Wenn in Überschriften explizit `T0-Theorie` steht, ersetze durch:
     - `... in der Fundamentalen Fraktal-Geometrischen Feldtheorie (FFGFT)`
   - Beispiel:
     ```latex
     \section{T0-Theorie und die sieben Rätsel}
     ```
     →
     ```latex
     \section{Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT) und die sieben Rätsel}
     ```

**Wichtig:**
- **Nicht** ändern: Symbole wie `T_0`, `T0` in Gleichungen, Indizes, Parametern oder Funktionsnamen.
- **Nicht** ändern: Zitations-Keys wie `pascher2025t0`, Dateinamen, Labels.

---

## 3. Umbenennungsregeln (Englisch)

### 3.1 Grundformulierung

Neue Standardbezeichnung:

> **Fundamental Fractal-Geometric Field Theory (FFGFT)**

Übergangssatz für Einleitung, Abstract, Klappentext o.ä.:

> "The theory previously known as T0 theory (Time-Mass Duality) will now be referred to consistently as the Fundamental Fractal-Geometric Field Theory (FFGFT)."

### 3.2 Konkrete Ersetzungen

Suche in englischen Kapiteln und Masters nach Formulierungen wie (nicht abschließend):

- `T0 theory`
- `T0 Theory`
- `the T0 theory`
- `T0 theory of time-mass duality`
- `T0 theory (Time-Mass Duality)`

**Ersetze** wie folgt (Stil und Grammatik wahren):

1. **Erste Nennung im Dokument (oder im Einleitungskapitel):**
   - Beispiel:
     ```latex
     The T0 theory of time-mass duality explains ...
     ```
   - Ersetze durch:
     ```latex
     The theory previously known as T0 theory (Time-Mass Duality) will now be referred to consistently as the Fundamental Fractal-Geometric Field Theory (FFGFT). In what follows, we simply write FFGFT.
     ```

2. **Weitere Vorkommen im Fließtext:**
   - `the T0 theory` → `the FFGFT`
   - `within T0 theory` → `within the FFGFT`
   - `T0-theory-based` → `FFGFT-based`

3. **Überschriften und Kapitel-Titel (EN):**
   - Wenn Überschriften `T0 theory` enthalten, ersetze durch:
     - `... in the Fundamental Fractal-Geometric Field Theory (FFGFT)`
   - Beispiel:
     ```latex
     \section{T0 Theory and the Seven Mysteries}
     ```
     →
     ```latex
     \section{Fundamental Fractal-Geometric Field Theory (FFGFT) and the Seven Mysteries}
     ```

**Auch hier gilt:**
- **Nicht** ändern: mathematische Symbole `T_0`, `T0`, Parameter, Indizes.  
- **Nicht** ändern: Bib-Keys, Dateinamen, Labels mit `t0`.

---

## 4. Spezielle Stellen: Einleitungen & Klappentext-artige Abschnitte

In den Einleitungen der Master-Dokumente (`T0_Anwendungen_De.tex`, `T0_Anwendungen_En.tex`) sowie ggf. in den Einleitungen der Narrative-Master:

1. Füge nach der ersten Erwähnung der Theorie jeweils einen kurzen Übergangssatz ein:

   **Deutsch:**
   ```latex
   Die Theorie, die früher als T0-Theorie (Time-Mass-Duality) bekannt war, wird nun einheitlich Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT) genannt.
   ```

   **Englisch:**
   ```latex
   The theory previously known as T0 theory (Time-Mass Duality) will now be referred to consistently as the Fundamental Fractal-Geometric Field Theory (FFGFT).
   ```

2. Achte darauf, dass die Formulierungen nicht zu oft wiederholt werden – pro Dokument ein klarer Übergangssatz genügt, danach nur noch `FFGFT` verwenden.

---

## 5. Technische Randbedingungen

- **LaTeX-Struktur nicht verändern:**
  - Keine Änderungen an `\documentclass`, `\geometry`, Kindle-spezifischen Einstellungen oder den gemeinsamen Preambeln, außer in Kommentaren/Beschreibungstexten.
- **Formeln und Mathe-Umgebungen nicht anfassen**, außer es geht um reinen Fließtext außerhalb von `$...$`, `\[...\]`, `align`, etc.

---

## 6. Validierung

Nach den Textanpassungen:

1. Kompiliere jeweils die Master-Dokumente mehrmals:

   ```bash
   cd 2/narrative/completted
   for i in 1 2 3; do
     pdflatex -interaction=nonstopmode T0_Anwendungen_De.tex || true
     pdflatex -interaction=nonstopmode T0_Anwendungen_En.tex || true
   done
   ```

2. Stelle sicher, dass:
   - Keine neuen LaTeX-Fehler auftreten.
   - Nur narrative Textstellen und Überschriften geändert wurden; Formeln, Gleichungen und Symbole mit `T_0`/`T0` sind unverändert.

3. Commit-Message (Vorschlag):
   - `Rename T0-Theorie to FFGFT in DE/EN chapters and applications masters`

---

## 7. Ergebnis

- In allen relevanten DE- und EN-Kapiteln sowie in den Anwendungs-Masterdokumenten ist die Theorie konsistent als
  - Deutsch: **Fundamentale Fraktal-Geometrische Feldtheorie (FFGFT)**  
  - Englisch: **Fundamental Fractal-Geometric Field Theory (FFGFT)**
  bezeichnet.  
- Alte Bezeichnung **T0-Theorie / T0 theory** bleibt nur in der erklärenden Übergangsformulierung als historischer Name erhalten ("früher bekannt als...").

