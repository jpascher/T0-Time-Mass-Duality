# Copilot Task: Fix DE Chapter 028 Table Header (T0_Anwendungen_De)

Branch: `copilot/reset-copilot-narrative`  
Base directory: `2/narrative`

Ziel: Die LaTeX-Fehler im deutschen Kapitel `028_T0_7-fragen-3_De_ch.tex` beheben, damit der Master `T0_Anwendungen_De.tex` fehlerfrei kompiliert, ohne inhaltliche Änderungen vorzunehmen.

---

## 1. Betroffene Dateien

- DE-Master:
  - `2/narrative/de_standalone/T0_Anwendungen_De.tex`
- DE-Kapitel:
  - `2/narrative/de_chapters_new/028_T0_7-fragen-3_De_ch.tex`

Andere Kapitel in `de_chapters_new` **nicht** anfassen, außer sie verursachen neue harte Fehler.

---

## 2. Konkreter Fehler aus dem Log

Auszug aus `T0_Anwendungen_De.log`:

- Mehrfache Meldungen der Form:
  - `028_T0_7-fragen-3_De_ch.tex: Fehler: 181: Missing } inserted. \textbf{Physikalisches\\Phänomen}`
  - `028_T0_7-fragen-3_De_ch.tex: Fehler: 181: Extra }, or forgotten \endgroup. \textbf{Physikalisches\\Phänomen}`

Dies weist darauf hin, dass in der Tabellenkopfzeile der Spalte **"Physikalisches Phänomen"** ein Zeilenumbruch (`\\`) innerhalb von `\textbf{...}` und zusammen mit `&` problematische Gruppen/Spalten erzeugt.

In `028_T0_7-fragen-3_De_ch.tex` befindet sich im Bereich der Koide-Zusammenfassung aktuell eine Tabelle ähnlich zu:

```latex
\begin{table}[htbp]
  \centering
  \small
  \begin{tabular}{@{}p{0.36\textwidth}@{\hspace{2mm}}p{0.21\textwidth}@{\hspace{2mm}}p{0.19\textwidth}@{\hspace{2mm}}p{0.14\textwidth}@{}}
    \toprule
    \textbf{Physikalisches\\Phänomen} & \textbf{T0-Vorhersage} & \textbf{Experiment} & \textbf{Abweichung} \\
    \midrule
    ...
  \end{tabular}
\end{table}
```

Genau diese Kopfzeile verursacht die Klammerfehler.

---

## 3. Gewünschte Korrektur der Tabellenkopfzeile

Ziel: **Keine LaTeX-Fehler** und **keine Overfull-Box** – gleichzeitig die Spaltenüberschrift verständlich halten.

### 3.1 Minimal-invasive Variante (empfohlen)

1. Ersetze die Kopfzeile durch eine Version **ohne** `\\` innerhalb von `\textbf{...}`:

   ```latex
   \toprule
   \textbf{Physikalisches Phänomen} & \textbf{T0-Vorhersage} & \textbf{Experiment} & \textbf{Abweichung} \\
   \midrule
   ```

2. Prüfe, ob dadurch wieder eine Overfull-\hbox-Warnung auftritt:
   - Falls **keine** Overfull-Warnung: so belassen.

### 3.2 Falls die Kopfzeile wirklich zweizeilig sein muss

Wenn die Kopfzeile optisch zu breit ist, verwende eine **saubere** Zweizeilen-Lösung ohne kaputten Gruppenaufbau. Zwei mögliche Ansätze:

1. **Mit `\shortstack` in der Zelle:**

   ```latex
   \toprule
   \textbf{\shortstack{Physikalisches \\ Phänomen}} & \textbf{T0-Vorhersage} & \textbf{Experiment} & \textbf{Abweichung} \\
   \midrule
   ```

   - Vorteil: `\shortstack` kapselt die Zeilenumbrüche, ohne die `tabular`-Struktur zu zerstören.

2. **Oder: Breite der ersten Spalte leicht vergrößern** und auf `\\` verzichten:

   - Beispiel: passe `p{0.36\textwidth}` auf `p{0.38\textwidth}` an, und verkleinere dafür die letzte Spalte minimal, sodass die Summe ≈ 1.0·\textwidth bleibt.

   ```latex
   \begin{tabular}{@{}p{0.38\textwidth}@{\hspace{2mm}}p{0.21\textwidth}@{\hspace{2mm}}p{0.19\textwidth}@{\hspace{2mm}}p{0.12\textwidth}@{}}
   ```

   - Dann kann die Kopfzeile einzeilig bleiben.

Wichtig: Nur eine dieser Varianten verwenden – keine rohen `\\`-Einfügungen direkt in `\textbf{...}` vor einem `&`.

---

## 4. Validierungsschritte

1. **Kompilierung des DE-Masters:**

   ```bash
   cd 2/narrative/de_standalone
   for i in 1 2 3; do
     pdflatex -interaction=nonstopmode T0_Anwendungen_De.tex || true
   done
   ```

2. **Erwartete Ergebnisse:**
   - Keine `Missing } inserted`- oder `Extra }, or forgotten \endgroup`-Fehler mehr aus `028_T0_7-fragen-3_De_ch.tex`.
   - Keine neuen harten LaTeX-Fehler.
   - Falls Overfull-\hbox-Warnungen für diese Tabelle auftreten:
     - Ggf. `\shortstack`-Variante oder leichte Spaltenanpassung gemäß Abschnitt 3.2 verwenden, bis keine sichtbaren Überbreiten mehr vorliegen.

3. **Kindle-Rahmen beibehalten:**
   - Seitengröße und Ränder stammen aus `T0_preamble_shared_De.tex` (6"x9"); diese Datei **nicht ändern**.

---

## 5. Commit & Push

1. Betroffene Datei(en) hinzufügen:

   - `2/narrative/de_chapters_new/028_T0_7-fragen-3_De_ch.tex`

2. Commit-Message (Vorschlag):

   - `Fix DE chapter 028 Koide summary table header (no LaTeX errors)`

3. Push nach:

   - `copilot/reset-copilot-narrative`

---

## 6. Endzustand

- `T0_Anwendungen_De.tex` kompiliert ohne LaTeX-Fehler.  
- Die Koide-Zusammenfassungstabelle in Kapitel 028 hat eine saubere, ggf. zweizeilige Kopfzeile für "Physikalisches Phänomen", ohne `Missing }`-/`Extra }`-Fehler und ohne sichtbare Overfull-Box.

