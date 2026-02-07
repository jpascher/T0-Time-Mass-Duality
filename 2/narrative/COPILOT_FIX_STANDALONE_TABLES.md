# Copilot Task: Fix and Compile Standalone Tables (DE/EN)

Branch: `local-standalone-tree-20260106` 
Base directory: `2/fix_tabellen`

Ziel: **Alle** standalone-Tabellen-Dokumente in `2/fix_tabellen/de_standalone` und `2/fix_tabellen/en_standalone` sollen LaTeX-fehlerfrei mit `pdflatex` kompilieren. Die Tabellen sind als eigenständige `.tex`-Dateien extrahiert und müssen strukturell korrigiert werden, ohne Inhalt oder Aussagen zu verändern.

---

## 1. Geltungsbereich

### 1.1 Verzeichnisse

- Extrahierte Standalone-Tabellen (DE und EN):
 - `2/fix_tabellen/extracted_tables/*.tex`

Nur Dateien in diesem Verzeichnis (und ggf. Unterverzeichnissen) bearbeiten. Andere Narrative-/Kapitel-/Master-Dokumente **nicht** ändern.

### 1.2 Annahmen

- Jede Datei in `de_standalone` / `en_standalone` ist ein vollständiges, eigenständig kompilierbares LaTeX-Dokument (mit eigener `\documentclass` usw.).
- Falls Pakete fehlen (z.B. `standalone`, `booktabs`, `siunitx`), installiere ein vollständiges TeXLive inkl. Standardpaketen.

---

## 2. Vorbereitung der Umgebung

1. Stelle sicher, dass `pdflatex` verfügbar ist (z.B. via `texlive-full` oder äquivalente Distribution).
2. Arbeite im Repo-Root:
  ```bash
  cd 2/fix_tabellen
  ```

---

## 3. Kompilationsstrategie (rekursiv und iterativ)

Für **alle** `.tex`-Dateien unter `de_standalone` und `en_standalone`:

1. Finde rekursiv alle Ziel-Dateien:
  ```bash
  find extracted_tables -name "*.tex" | sort > standalone_tables_list.txt
  ```

2. Für jede gefundene Datei `TABLE.tex`:
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
  done < standalone_tables_list.txt
  ```

3. Sammle für jede Datei das jeweilige `.log` und prüfe auf Fehler (siehe nächste Sektion).

---

## 4. Fehlerklassen, die zu beheben sind

### 4.1 Kritische LaTeX-Fehler (müssen 0 werden)

Behebe alle Fehler, die das Kompilieren stoppen, insbesondere:

- `! LaTeX Error:` aller Art (undefinierte Umgebungen, falsche `\begin`/`\end`, fehlende Klammern usw.).
- `Undefined control sequence` (fehlende Pakete oder Tippfehler in Befehlen).
- `Missing } inserted`, `Extra }, or forgotten \endgroup` (unbalancierte Klammern/Umgebungen).
- Fehler im Zusammenhang mit Tabellenumgebungen (`tabular`, `tabularx`, `longtable` etc.).

**Maßgabe:**
- Nur die LaTeX-Struktur reparieren (Umgebungen, Klammern, Paket-Ladereihenfolge).
- Inhaltliche Aussagen, Zahlen und mathematische Formeln **nicht** verändern.

### 4.2 Warnungen: zu breite Tabellen (bis zu 201 Dokumente korrigieren)

- Warnungen vom Typ **Overfull `\hbox`** oder **Float too large for page** bei Tabellen sollen systematisch reduziert werden, sodass alle Tabellen innerhalb der Textbreite liegen.
- Bearbeite dazu rekursiv bis zu **201** unterschiedliche `.tex`-Dateien aus `2/fix_tabellen/extracted_tables` (Sortierreihenfolge der `standalone_tables_list.txt`).
- Erlaubte Maßnahmen: Spaltenbreiten anpassen (`p{...}`, `tabularx`, `arraystretch`), Zeilenumbrüche in Zellen setzen, Tabellen ggf. mit `adjustbox`/`resizebox` auf `\textwidth` skalieren.
- PDF-String-Warnungen (Math in Bookmarks) und geringfügige Underfull-Warnungen dürfen bleiben.

---

## 5. Konkretes Vorgehen pro Datei

Für jede Datei `TABLE.tex` in `de_standalone` bzw. `en_standalone`:

1. Öffne das zugehörige `.log` nach der Kompilation.
2. Suche nach den oben genannten Fehlerklassen.
3. Korrigiere die Ursachen **direkt in der jeweiligen Standalone-Datei**, z.B.:
  - Fehlende `\usepackage{...}` ergänzen (falls die Datei sich selbst um Pakete kümmert).
  - Falsch geschachtelte Umgebungen (`\begin{tabular}`/`\end{tabular}`) reparieren.
  - Unbalancierte `{`/`}` in Tabellenköpfen säubern.
4. Kompiliere die Datei erneut (3 Durchläufe wie oben) und prüfe, dass keine `! LaTeX Error:`-Meldungen mehr auftreten.

**Wichtig:**
- Keine globale Preambel aus den Narrative-Dokumenten importieren; jede Datei bleibt ein **Standalone**.
- Tabelleninhalte (Spaltenanzahl, Werte, physikalische Größen) nicht logisch verändern.

---

## 6. Vollständigkeitsprüfung

1. Verwende `standalone_tables_list.txt` als Referenzliste aller bearbeiteten Dateien.
2. Stelle sicher, dass für **jede** dort aufgeführte `.tex`-Datei gilt:
  - Mindestens ein vollständiger Kompilationslauf endet **ohne** `! LaTeX Error:`.
3. Dokumentiere ggf. Dateien, bei denen trotz Reparatur noch unklare Fehler verbleiben, z.B. in einer kurzen Textliste `standalone_tables_unresolved.txt`.

---

## 7. Abschluss, Commit & Push

1. Prüfe mit `git status`, welche Dateien unter `2/fix_tabellen/de_standalone` und `2/fix_tabellen/en_standalone` geändert wurden.
2. Füge **nur** diese Standalone-Tabellen und diese Task-Datei hinzu:
  ```bash
  git add 2/fix_tabellen/extracted_tables/*.tex \
      2/narrative/COPILOT_FIX_STANDALONE_TABLES.md
  ```
3. Commit-Message (Vorschlag):
  ```bash
  git commit -m "Fix LaTeX errors in standalone tables (DE/EN)"
  git push
  ```

Erwartetes Ergebnis: Alle Standalone-Tabellen-Dokumente in `2/fix_tabellen/de_standalone` und `2/fix_tabellen/en_standalone` kompilieren lokal mit `pdflatex` ohne harte LaTeX-Fehler; nur strukturbezogene Korrekturen wurden vorgenommen, der Tabelleninhalt blieb inhaltlich unverändert.
