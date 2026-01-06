# Copilot Task: Fix and Compile LaTeX in `final_corrected`

Branch: `copilot/create-standalone-tree-branch`  
Base directory: `2/fix_tabellen/final_corrected`

Ziel: **Alle** LaTeX-Dokumente in `2/fix_tabellen/final_corrected` sollen LaTeX-fehlerfrei mit `pdflatex` (oder `latexmk -pdf`) kompilieren. Die Dateien stammen aus bereits korrigierten Narrativ-Dokumenten und enthalten in der Regel denselben Typ von Fehlern (Struktur/Formalia), nicht inhaltliche Probleme.

---

## 1. Geltungsbereich

### 1.1 Verzeichnis

- Korrigierte, aber noch nicht fehlerfrei kompilierende LaTeX-Dateien:
  - `2/fix_tabellen/final_corrected/*.tex`

Nur Dateien in diesem Verzeichnis (und ggf. Unterverzeichnissen) bearbeiten. Andere Narrative-/Kapitel-/Master-Dokumente **nicht** ändern.

### 1.2 Annahmen

- Jede Datei in `final_corrected` ist ein vollständiges, eigenständig kompilierbares LaTeX-Dokument (mit eigener `\documentclass` bzw. minimaler Preambel).
- Falls Pakete fehlen, installiere eine vollständige TeX-Distribution (z.B. TeXLive mit Standardpaketen).

---

## 2. Vorbereitung der Umgebung

1. Stelle sicher, dass `pdflatex` verfügbar ist (z.B. via TeXLive oder äquivalente Distribution).
2. Arbeite im Repo-Root:
   ```bash
   cd 2/fix_tabellen
   ```

---

## 3. Kompilationsstrategie (rekursiv und iterativ)

Für **alle** `.tex`-Dateien unter `2/fix_tabellen/final_corrected`:

1. Finde rekursiv alle Ziel-Dateien:
   ```bash
   find final_corrected -name "*.tex" | sort > final_corrected_list.txt
   ```

2. Für jede gefundene Datei `DOC.tex`:
   ```bash
   while read -r f; do
     dir="$(dirname "$f")"
     base="$(basename "$f")"
     cd "$dir"
     # Mehrfach kompilieren, um Referenzen zu stabilisieren
     for i in 1 2 3; do
       pdflatex -interaction=nonstopmode "$base" || true
     done
     cd - >/dev/null 2>&1
   done < final_corrected_list.txt
   ```

3. Sammle für jede Datei das jeweilige `.log` und prüfe auf Fehler (siehe nächste Sektion).

---

## 4. Fehlerklassen, die zu beheben sind

### 4.1 Kritische LaTeX-Fehler (müssen 0 werden)

Behebe alle Fehler, die das Kompilieren stoppen, insbesondere:

- `! LaTeX Error:` aller Art (undefinierte Umgebungen, falsche `\begin`/`\end`, fehlende Klammern usw.).
- `Undefined control sequence` (fehlende Pakete oder Tippfehler in Befehlen).
- `Missing } inserted`, `Extra }, or forgotten \endgroup` (unbalancierte Klammern/Umgebungen).
- Fehler im Zusammenhang mit Tabellen- oder Mathe-Umgebungen (`tabular`, `longtable`, `equation`, `align` etc.).

**Maßgabe:**
- Nur die LaTeX-Struktur reparieren (Umgebungen, Klammern, Paket-Ladereihenfolge, fehlende `$...$` für Mathe, Escaping von `_` usw.).
- Inhaltliche Aussagen, Zahlen und physikalische Formeln **nicht** verändern.

### 4.2 Warnungen: zu breite Tabellen / Overfull Boxes (optional, wenn klar behebbar)

- Warnungen vom Typ **Overfull `\hbox`** oder **Float too large for page** sollen, wo mit einfachen Mitteln möglich, reduziert werden (z.B. Anpassung von Spaltenbreiten oder Zeilenumbrüchen).
- PDF-String-Warnungen (Math in Bookmarks) und geringfügige Underfull-Warnungen dürfen bleiben.

---

## 5. Konkretes Vorgehen pro Datei

Für jede Datei `DOC.tex` in `final_corrected`:

1. Öffne das zugehörige `.log` nach der Kompilation.
2. Suche nach den oben genannten Fehlerklassen.
3. Korrigiere die Ursachen **direkt in der jeweiligen Datei**, z.B.:
   - Fehlende `\usepackage{...}` ergänzen (falls die Datei eigene Preambel hat).
   - Falsch geschachtelte Umgebungen (`\begin{...}`/`\end{...}`) reparieren.
   - Unbalancierte `{`/`}` oder fehlende `$` in Mathe-/Tabellenköpfen säubern.
   - Unerlaubte Unterstriche `_` im Text als `\_` escapen.
4. Kompiliere die Datei erneut (3 Durchläufe wie oben) und prüfe, dass keine `! LaTeX Error:`-Meldungen mehr auftreten.

**Wichtig:**
- Keine globale Preambel aus anderen Dokumenten importieren; jede Datei bleibt ein **Standalone**.
- Inhalt (Formeln, Tabellenwerte, Argumentationslogik) nicht verändern.

---

## 6. Vollständigkeitsprüfung

1. Verwende `final_corrected_list.txt` als Referenzliste aller bearbeiteten Dateien.
2. Stelle sicher, dass für **jede** dort aufgeführte `.tex`-Datei gilt:
   - Mindestens ein vollständiger Kompilationslauf endet **ohne** `! LaTeX Error:`.
3. Falls einzelne Dateien trotz Reparatur noch unklare Fehler aufweisen, liste diese in `final_corrected_unresolved.txt` mit kurzer Fehlerbeschreibung auf.

---

## 7. Abschluss, Commit & Push

1. Prüfe mit `git status`, welche Dateien unter `2/fix_tabellen/final_corrected` geändert wurden.
2. Füge **nur** diese Dateien und diese Task-Datei hinzu:
   ```bash
   git add 2/fix_tabellen/final_corrected/*.tex \
           2/narrative/COPILOT_FIX_FINAL_CORRECTED_LATEX.md
   ```
3. Commit-Message (Vorschlag):
   ```bash
   git commit -m "Fix LaTeX errors in final_corrected standalone documents"
   git push
   ```

Erwartetes Ergebnis: Alle LaTeX-Dokumente in `2/fix_tabellen/final_corrected` kompilieren lokal mit `pdflatex` ohne harte LaTeX-Fehler; nur struktur- und formatbezogene Korrekturen wurden vorgenommen, der inhaltliche Gehalt blieb unverändert.