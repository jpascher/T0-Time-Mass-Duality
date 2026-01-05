# Copilot Task: Validate ALL FFGFT Chapter Documents (Not Only Anwendungen)

Branch: `copilot/reset-copilot-narrative`  
Base directory: `2/narrative`

Ziel: **Alle** Kapitel-Dokumente (DE und EN), nicht nur jene, die aktuell im Anwendungen-Master eingebunden sind, müssen LaTeX-fehlerfrei kompilieren und das 6x9"-Kindle-Layout respektieren.

Diese Aufgabe ergänzt `COPILOT_RENAME_T0_TO_FFGFT.md` und `COPILOT_VALIDATE_ALL_MASTERS.md` und weitet die Prüfung explizit auf **alle Kapiteldateien** aus.

---

## 1. Kapitel-Suchraum

Suche rekursiv unter `2/narrative` nach Kapiteldateien, mindestens:

- Deutsche Kapitel:
  - `2/narrative/de_chapters_new/*.tex`
  - weitere `*_De_ch.tex` unter `2/narrative/**`
- Englische Kapitel:
  - `2/narrative/en_chapters_new/*.tex`
  - weitere `*_En_ch.tex` unter `2/narrative/**`

Ignoriere dabei Master-Dokumente wie `T0_Anwendungen_De.tex`, `T0_Anwendungen_En.tex`, die bereits durch `COPILOT_VALIDATE_ALL_MASTERS.md` abgedeckt werden.

---

## 2. Kompilationsstrategie für Einzelkapitel

Viele Kapitel werden nur über Master-Dokumente eingebunden. Für Kapitel, die **nicht** in einem Master referenziert werden (oder zusätzlich zur Master-Prüfung), verwende einen **temporären, minimalen Wrapper**, z.B.:

```latex
% TEMP_WRAPPER_<NAME> (nicht einchecken)
\documentclass[12pt]{book}
\input{../../../T0_preamble_shared_De} % oder _En je nach Sprache
\begin{document}
\pagestyle{plain}
\input{<RELATIVER/PFAD/ZUM/KAPITEL>.tex}
\end{document}
```

Richtlinien:

- Verwende für **DE-Kapitel** die deutsche Preambel `T0_preamble_shared_De.tex`.
- Verwende für **EN-Kapitel** die englische Preambel `T0_preamble_shared_En.tex`.
- Belasse die 6x9"-Geometrie aus der Preambel unverändert.
- Diese temporären Wrapper dienen nur der Validierung und sollen **nicht** dauerhaft im Repo bleiben (lokal testen, dann löschen).

---

## 3. Fehlererkennung und -behebung

Für jedes Kapitel (egal ob über Master oder temporären Wrapper kompiliert):

1. Kompiliere mindestens 2–3 Mal mit:
   ```bash
   pdflatex -interaction=nonstopmode <WRAPPER ODER MASTER>.tex || true
   ```

2. Analysiere das `.log`:
   - Suche nach harten Fehlern:
     - `! LaTeX Error:`
     - `Missing } inserted`
     - `Extra }, or forgotten \endgroup`
     - `Undefined control sequence`
   - Lokalisierung über Dateinamen/Zeilennummer in den entsprechenden Kapiteldateien `*_De_ch.tex` bzw. `*_En_ch.tex`.

3. **Behebe Fehler ausschließlich im Kapitel**, z.B. durch:
   - Korrektur von unbalancierten `{`/`}` nach eingefügten FFGFT-Texten.
   - Reparatur von Tabellenköpfen (z.B. `\textbf{...}` + Zeilenumbruch → ggf. `\shortstack{... \\ ...}`).
   - Leichte stilistische Kürzung von zu langen Bezeichnungen, wenn diese Tabellen über den Rand hinaustreiben – Sinn und Inhalt beibehalten.

4. **Nicht ändern:**
   - Mathematische Symbole, Gleichungen und Notation (`T_0`, `T0`, `\xi`, etc.).
   - 6x9"-Layoutvorgaben aus der gemeinsamen Preambel.
   - BibTeX-Keys, Label-Namen und Dateinamen.

---

## 4. Vollständigkeitsprüfung

1. Erzeuge eine Liste aller gefundenen Kapiteldateien (z.B. Pfade zu `*_De_ch.tex` und `*_En_ch.tex`).
2. Markiere für jedes Kapitel, dass es mindestens einmal:
   - Entweder über einen Master (z.B. `T0_Anwendungen_*.tex`) erfolgreich kompiliert wurde, oder
   - Über einen temporären Wrapper fehlerfrei kompiliert hat.
3. Stelle sicher, dass **kein Kapitel mit FFGFT-Inhalt** übrig bleibt, das noch nie erfolgreich kompiliert wurde.

---

## 5. Ergebnis & Berichterstattung

Am Ende:

- Alle Kapiteldateien `*_De_ch.tex` und `*_En_ch.tex` unter `2/narrative` kompilieren fehlerfrei, entweder im Kontext ihrer Master oder über temporäre Wrapper.  
- Die Umbenennung von T0-Theorie → FFGFT hat **keine** offenen LaTeX-Fehler hinterlassen.  
- In einem kurzen Kommentar/Commit-Text sollte festgehalten werden, dass nun **alle Kapitel** syntaktisch sauber und KDP-kompatibel sind.

