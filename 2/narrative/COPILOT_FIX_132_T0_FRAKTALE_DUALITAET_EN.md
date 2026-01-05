# Copilot Task: Fix EN Chapter 132 and Related LaTeX Issues (T0_Anwendungen_En)

Branch: `copilot/reset-copilot-narrative`  
Base directory: `2/narrative`

Ziel: Die LaTeX-Fehler im englischen Kapitel `132_T0_Fraktale_Dualitaet_En_ch.tex` sowie weitere EN-spezifische Warnungen im `T0_Anwendungen_En`-Master beheben, ohne Inhalt zu verändern, und den EN-Master fehlerfrei (Kindle-kompatibel) kompilieren.

---

## 1. Geltungsbereich

### 1.1 Betroffene Dateien

- EN-Master:
  - `2/narrative/en_standalone/T0_Anwendungen_En.tex`

- EN-Kapiteldateien (mindestens diese):
  - `2/narrative/en_chapters_new/132_T0_Fraktale_Dualitaet_En_ch.tex`
  - `2/narrative/en_chapters_new/030_T0_penrose_En_ch.tex`
  - `2/narrative/en_chapters_new/028_T0_7-fragen-3_En_ch.tex`
  - `2/narrative/en_chapters_new/029_T0_threeclock_En_ch.tex`
  - `2/narrative/en_chapters_new/037_Hannah_En_ch.tex`
  - `2/narrative/en_chapters_new/038_Markov_En_ch.tex`

**Wichtig:** Narrative-Master und narrative Kapitel **nicht** bearbeiten. Nur die oben genannten EN-Anwendungsdateien.

---

## 2. Konkrete Fehler aus dem Log

Auszug aus `T0_Anwendungen_En.log`:

1. **Harte Fehler in `132_T0_Fraktale_Dualitaet_En_ch.tex`**
   - Viele Meldungen der Form:
     - `Missing } inserted. \end{tabularx}` (Zeile ~88)
     - `Extra }, or forgotten \endgroup. \end{tabularx}`
   - Ursache: Modifizierte Tabellenköpfe mit Zeilenumbrüchen (`\\`) und Sonderzeichen (`&`) innerhalb der `tabularx`-Umgebung, die die Gruppenstruktur stören.

2. **Warnungen in anderen EN-Kapiteln (derzeit tolerierbar, aber optional zu entschärfen):**
   - `030_T0_penrose_En_ch.tex`: viele `Command \textdegree invalid in math mode`-Warnungen.
   - `028_T0_7-fragen-3_En_ch.tex`, `029_T0_threeclock_En_ch.tex`, `037_Hannah_En_ch.tex`, `038_Markov_En_ch.tex`: `Token not allowed in a PDF string (Unicode)` für Mathe in Bookmarks.

Ziel dieses Auftrags:
- **Alle harten Fehler in Kapitel 132 vollständig beheben**.  
- Optional (empfohlen): die `\textdegree`-Warnungen im Penrose-Kapitel bereinigen.  
- Danach `T0_Anwendungen_En.tex` mehrfach fehlerfrei kompilieren.

---

## 3. Kapitel 132: `132_T0_Fraktale_Dualitaet_En_ch.tex`

### 3.1 Problemstelle: Vergleichstabellen (Tabularx)

Im Bereich um Zeilen ~76–106 befinden sich zwei `tabularx`-Tabellen:

- Erste Tabelle: "Table 1: First three aspects" (Kommentarzeile `% Table 1: First three aspects`).
- Zweite Tabelle: "Table 2: Additional aspects".

Dort wurden Kopfzeilen mit Zeilenumbrüchen verändert, z.B.:

```latex
\textbf{Calculation Aspect} & \textbf{T0 Theory} & \textbf{DoT Theory} & \textbf{Parallel /\\ Commonality} \\
...
\textbf{Time Duality \\& Modulus} & ...
```

Diese Kombination aus `\\` und `&` innerhalb der `tabularx`-Zelle führt zu Gruppen-/Spaltenkonflikten und erzeugt die `Missing } inserted`-Fehler.

### 3.2 Gewünschte Korrekturstrategie

1. **Kopfzeilen reparieren (semantisch unverändert):**
   - Stelle die Kopfzeilen so her, dass sie **ohne verschachtelte `\\` vor `&`** auskommen.  
   - Vorschlag für die erste Tabelle:
     ```latex
     \begin{tabularx}{\textwidth}{XXXX}
       \toprule
       \textbf{Calculation Aspect} & \textbf{T0 Theory} & \textbf{DoT Theory} & \textbf{Parallel / Commonality} \\
       \midrule
       \textbf{Time Duality \& Modulus} & ...
     ```
   - Wenn ein Zeilenumbruch in der letzten Spaltenüberschrift nötig ist (Breite), verwende z.B. `\shortstack` oder eine `X`-Spalte mit `\\` **ohne zusätzliches `&`** in dieser Zelle, z.B.:
     ```latex
     \textbf{\shortstack{Parallel / \\ Commonality}}
     ```

2. **Zeilenumbrüche in Zellen vorsichtig einsetzen:**
   - Innerhalb einer einzelnen Zelle sind `\\`-Umbrüche nur erlaubt, wenn klar keine zusätzliche Spaltentrennung (`&`) folgt.
   - Vermeide Muster wie `\\&` innerhalb derselben Zelle.

3. **Tabellenbreite beibehalten:**
   - `tabularx` mit Spaltentyp `X` sorgt automatisch für Umbrüche innerhalb der Textbreite.  
   - Nutze diese Eigenschaft statt aggressiver manueller `\\`-Einfügungen, wo möglich.

4. **Nach Korrektur testen:**
   - Kompiliere (innerhalb des Repos):
     ```bash
     cd 2/narrative/en_standalone
     pdflatex -interaction=nonstopmode T0_Anwendungen_En.tex || true
     ```
   - Stelle sicher, dass **keine** `Missing } inserted`- oder `Extra }, or forgotten \endgroup`-Fehler im Log verbleiben.

---

## 4. Penrose-Kapitel: \textdegree in Mathe (
`030_T0_penrose_En_ch.tex`)

Aus dem Log:

- Wiederholte Warnungen
  - `Command \textdegree invalid in math mode` an vielen Stellen (z.B. Zeilen 77, 96, 97, 98, 130, 134, 138, 141, 181, 187, ...).

### 4.1 Korrekturregeln

1. **Im Mathemodus (`$...$`, `\(...\)`, `\[...\]`, `align`, `equation` etc.):**
   - Ersetze `\textdegree` durch **einen echten Gradwinkel-Ausdruck**, z.B.:
     - `^{\circ}`
     - oder falls siunitx passend geladen und verwendet wird: `\ang{<Wert>}`
   - Beispiel:
     ```latex
     90\textdegree \to 90^{\circ}
     ```

2. **Im Fließtext (außerhalb von Mathe):**
   - `\textdegree` ist erlaubt; lasse solche Vorkommen unverändert.

3. **Nach den Ersetzungen:**
   - Erneut den EN-Master 3–4 Mal kompilieren (siehe Abschnitt 5 unten) und prüfen, dass die `\textdegree`-Warnungen verschwinden oder deutlich reduziert sind.

---

## 5. Kompilierung und Abschlussprüfungen für `T0_Anwendungen_En`

1. **Mehrfachkompilierung:**
   ```bash
   cd 2/narrative/en_standalone
   for i in 1 2 3 4; do
     pdflatex -interaction=nonstopmode T0_Anwendungen_En.tex || true
   done
   ```

2. **Erwarteter Status nach den Fixes:**
   - Keine `Missing } inserted`- oder `Extra }, or forgotten \endgroup`-Fehler mehr, insbesondere nicht an `\end{tabularx}` in Kapitel 132.
   - Keine harten LaTeX-Fehler mehr in `T0_Anwendungen_En.tex`.
   - `\textdegree`-Warnungen in `030_T0_penrose_En_ch.tex` weitgehend beseitigt.
   - `Token not allowed in a PDF string (Unicode)`-Warnungen dürfen vorerst bleiben (sie sind Layout-neutral).

3. **Kindle/KDP-Rahmenbedingungen:**
   - Papiersize 6"x9" und Ränder aus `T0_preamble_shared_En.tex` **nicht** ändern.
   - Keine sichtbaren Overfull-Boxen (insb. in den bearbeiteten Tabellen) zulassen.

4. **Commit & Push:**
   - Füge nur die tatsächlich geänderten Dateien hinzu, z.B.:
     - `2/narrative/en_chapters_new/132_T0_Fraktale_Dualitaet_En_ch.tex`
     - `2/narrative/en_chapters_new/030_T0_penrose_En_ch.tex`
   - Commit-Message (Vorschlag):
     - `Fix EN chapter 132 tabularx errors and clean textdegree usage`
   - Push nach `copilot/reset-copilot-narrative`.

---

## 6. Ergebnis

- `T0_Anwendungen_En.tex` kompiliert vollständig **ohne** LaTeX-Fehler.  
- Kapitel 132 enthält funktionierende `tabularx`-Tabellen ohne Gruppen-/Klammerfehler, im 6"x9"-Layout lesbar.  
- Die wichtigsten EN-spezifischen Warnungen (v.a. `\textdegree` in Mathe) sind behoben, ohne die physikalische Aussage oder Formeln zu verändern.

