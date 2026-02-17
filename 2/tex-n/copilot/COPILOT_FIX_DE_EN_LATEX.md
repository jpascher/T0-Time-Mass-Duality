# Copilot Task: Fix and Compile LaTeX in `2/fix/de_en`

Branch: `copilot/create-standalone-tree-branch` 
Base directory: `2/fix/de_en`

Ziel: **Alle** LaTeX-Dokumente in `2/fix/de_en` (DE und EN) sollen LaTeX-fehlerfrei mit `pdflatex` kompilieren. Zusätzlich soll eine Übersicht erstellt werden, welche Dokumente nach der Bereinigung weiterhin **Overfull/Underfull-Box- oder Tabellen-Overflow-Warnungen** haben.

---

## 1. Geltungsbereich

### 1.1 Verzeichnis

- Zu bearbeitende Dateien (rekursiv):
 - `2/fix/de_en/*.tex`
 - `2/fix/de_en/**/*.tex`

Nur Dateien in diesem Verzeichnis (und dessen Unterverzeichnissen) bearbeiten. Andere Narrative-/Kapitel-/Master-Dokumente **nicht** ändern.

### 1.2 Annahmen

- Jede `.tex`-Datei in `2/fix/de_en` ist ein vollständiges, eigenständig kompilierbares LaTeX-Dokument (mit eigener `\documentclass` oder eingebundener gemeinsamer Preambel).
- Falls Pakete fehlen, installiere eine vollständige TeX-Distribution (z.B. TeX Live, inkl. Pakete wie `physics`, `siunitx`, `babel` mit `ngerman`/`english`, `hyperref`, `booktabs`, `longtable`, `amsmath`, `amssymb`).

---

## 2. Vorbereitung der Umgebung

1. Stelle sicher, dass `pdflatex` verfügbar ist (z.B. via `texlive-full` oder äquivalente Distribution).
2. Arbeite im Repo-Root:
  ```bash
  cd 2/fix/de_en
  ```

---

## 3. Kompilationsstrategie (rekursiv und iterativ)

Für **alle** `.tex`-Dateien unter `2/fix/de_en`:

1. Finde rekursiv alle Ziel-Dateien (relative Pfade bezogen auf `2/fix/de_en`):
  ```bash
  cd 2/fix/de_en
  find . -name "*.tex" | sort > fix_de_en_list.txt
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
  done < fix_de_en_list.txt
  ```

3. Sammle für jede Datei das jeweilige `.log` und prüfe auf Fehler und relevante Warnungen (siehe nächste Sektion).

---

## 4. Fehler- und Warnklassen

### 4.1 Kritische LaTeX-Fehler (müssen 0 werden)

Behebe **alle** Fehler, die das Kompilieren stoppen, insbesondere:

- `! LaTeX Error:` aller Art (undefinierte Umgebungen, falsche `\begin`/`\end`, fehlende Klammern usw.).
- `Undefined control sequence` (fehlende Pakete oder Tippfehler in Befehlen).
- `Missing } inserted`, `Extra }, or forgotten \endgroup` (unbalancierte Klammern/Umgebungen).
- `Missing $ inserted`, Fehler in Mathe- oder Tabellenumgebungen.

**Maßgabe:**
- Nur die LaTeX-Struktur reparieren (Umgebungen, Klammern, Paket-Ladereihenfolge, fehlende `$...$` für Mathe, Escaping von `_` usw.).
- Inhaltliche Aussagen, Zahlen und physikalische Formeln **nicht** verändern.

### 4.2 Warnungen zu überbreiten Elementen (Overfull/Overflow)

Zusätzlich zu den Fehlern sollen Warnungen reduziert und protokolliert werden:

- Warnungen vom Typ **Overfull `\hbox`**, **Overfull `\vbox`**, **Float too large for page** oder offensichtlich zu breite Tabellen.
- Erlaubte Maßnahmen:
 - Spaltenbreiten anpassen (`p{...}`, `tabularx`, `arraystretch`),
 - Zeilenumbrüche in Zellen setzen,
 - Tabellen ggf. mit `adjustbox`/`resizebox` auf `\textwidth` skalieren,
 - moderate manuelle Umbrechungen im Text.
- Warnungen wie "Token not allowed in a PDF string (Unicode)" oder leichte Underfull-Warnungen dürfen bleiben.

Erstelle eine Datei `fix_de_en_overflow_warnings.txt` mit einer Zeile pro Dokument, das nach der Bereinigung weiterhin Overfull/Overflow-Warnungen erzeugt:

```text
<relativer/pfad/zur/datei.tex>: <kurze zusammenfassung der verbleibenden Overfull-/Overflow-Warnungen>
```

---

## 5. Konkretes Vorgehen pro Datei

Für jede Datei `DOC.tex` in `2/fix/de_en`:

1. Nach der Kompilation das zugehörige `.log` öffnen.
2. Zuerst **alle `! LaTeX Error:`-Meldungen** beheben (siehe Abschnitt 4.1) und erneut kompilieren, bis mindestens ein Lauf ohne harte Fehler durchläuft.
3. Anschließend die relevanten Overfull-/Overflow-Warnungen prüfen (siehe Abschnitt 4.2) und, wo mit vernünftigem Aufwand möglich, durch Layout-Anpassungen reduzieren.
4. Dateispezifische Anpassungen **direkt in der jeweiligen `.tex`-Datei** durchführen; keine globale Preambel von anderen Dokumenten importieren.

**Wichtig:**
- Jede Datei bleibt ein **Standalone**-Dokument im Kontext von `2/fix/de_en`.
- Inhalt (Formeln, Tabellenwerte, Argumentationslogik) nicht inhaltlich verändern.

---

## 6. Vollständigkeits- und Warnungsprüfung

1. Verwende `fix_de_en_list.txt` als Referenzliste aller bearbeiteten Dateien.
2. Stelle sicher, dass für **jede** dort aufgeführte `.tex`-Datei gilt:
  - Mindestens ein vollständiger Kompilationslauf endet **ohne** `! LaTeX Error:`.
3. Erfasse alle Dateien, bei denen nach der Bereinigung weiterhin Overfull-/Overflow-Warnungen auftreten, in `fix_de_en_overflow_warnings.txt` (siehe oben).
4. Falls einzelne Dateien trotz mehrfacher Versuche noch unklare, nicht-triviale Fehler aufweisen, liste diese zusätzlich in `fix_de_en_unresolved.txt` mit kurzer Fehlerbeschreibung.

---

## 7. Abschluss, Commit & Push

1. Arbeite auf dem Branch `copilot/create-standalone-tree-branch`.
2. Prüfe mit `git status`, welche Dateien unter `2/fix/de_en` und welche Log-/Listen-Dateien geändert oder neu erstellt wurden.
3. Füge **nur** diese Dateien und diese Task-Datei hinzu:
  ```bash
  git add 2/fix/de_en/**/*.tex \
      2/fix/de_en/*.tex \
      2/fix/de_en/fix_de_en_list.txt \
      2/fix/de_en/fix_de_en_overflow_warnings.txt \
      2/fix/de_en/fix_de_en_unresolved.txt \
      2/narrative/COPILOT_FIX_DE_EN_LATEX.md
  ```
4. Commit-Message (Vorschlag):
  ```bash
  git commit -m "Fix LaTeX errors and collect overflow warnings in 2/fix/de_en (DE/EN)"
  git push
  ```

Erwartetes Ergebnis: Alle LaTeX-Dokumente in `2/fix/de_en` kompilieren ohne harte LaTeX-Fehler. Zusätzlich existiert eine klare Übersicht (`fix_de_en_overflow_warnings.txt`), welche Dokumente noch Overfull-/Overflow-Warnungen haben; inhaltliche Aussagen wurden nicht verändert, nur LaTeX-Struktur und Layout wurden bereinigt.
