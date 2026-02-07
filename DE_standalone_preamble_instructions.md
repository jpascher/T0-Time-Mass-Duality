# Anleitung: DE-Standalone-Preambel reparieren und alle DE-Standalone-Dokumente kompilieren

## Ausgangslage
- Arbeitsverzeichnis: `2/tex-n/de_standalone`
- Alle DE-Standalone-Dokumente binden aktuell `\input{T0_preamble_standalone_De}` ein (Datei liegt im selben Verzeichnis).
- `T0_preamble_standalone_De.tex` ist eine Kopie von `T0_preamble_shared_De.tex` und verwendet LuaLaTeX mit Schriftkonfiguration Inter + JetBrains Mono + Libertinus Math.
- Viele `.tex`-Dateien erzeugen LaTeX-Fehler, weil benötigte Makros/Umgebungen/Pakete noch nicht vollständig oder doppelt definiert sind.

## Ziel
- Eine **stabile, optimierte** `T0_preamble_standalone_De.tex`, die **für alle Dateien in `de_standalone`** funktioniert, ohne dass jede Datei ihre eigene lokale Präambel braucht.
- Alle `.tex`-Dateien in `2/tex-n/de_standalone` sollen mit LuaLaTeX (mindestens 2–3 Durchläufe) durchkompilieren.

## Vorgehen (für den Assistenten)

### 1. Umfeld vorbereiten
1. Wechsle in das Verzeichnis:
  - `cd 2/tex-n/de_standalone`
2. Prüfe, ob `lualatex` im `PATH` verfügbar ist (sonst Fehler zurückgeben und abbrechen).

### 2. Kompilier-Loop über alle DE-Standalone-Dokumente
1. Erzeuge die Liste aller `.tex`-Dateien im Verzeichnis, **ohne** die beiden Präambeldateien:
  - Include: `*.tex`
  - Exclude: `T0_preamble_De.tex`, `T0_preamble_standalone_De.tex`.
2. Für jede dieser Dateien führe einen Kompilier-Loop mit LuaLaTeX aus (mindestens zwei, besser drei Durchläufe) mit `-interaction=nonstopmode` und getrennten Output-/Error-Logs pro Datei und Durchlauf.
3. Teile die Dateien danach in zwei Mengen:
  - **OK**: Alle Durchläufe mit ExitCode `0`.
  - **Fehlerhaft**: Mindestens ein Durchlauf mit ExitCode ≠ 0.
4. Erzeuge eine kurze Zusammenfassung (Liste der fehlerhaften Dateien) und arbeite diese Liste iterativ ab.

### 3. Fehleranalyse pro Datei
Für jede fehlerhafte Datei:
1. Öffne den zugehörigen Error-Log (`latex_error_<Name>_1.txt` o.ä.) und suche nach den ersten „harten“ Fehlern:
  - `Undefined control sequence` (`\foo` nicht definiert).
  - `Environment ... undefined`.
  - Paket-Konflikte (z.B. „Command ... already defined“, inkompatible Optionen).
2. Extrahiere die fehlenden Makros/Umgebungen **und** die Dateinamen/Zeilennummern, in denen sie verwendet werden.

### 4. Zentrale Behebung über `T0_preamble_standalone_De.tex`
Grundprinzip: **So viel wie möglich zentral in der Standalone-Preambel reparieren**, damit alle Standalone-Dokumente davon profitieren.

1. Wenn ein Makro/Umgebung nur „klassisch“ ist (z.B. bekannte LaTeX-Pakete):
  - Finde das passende Paket (z.B. `\includegraphics` → `graphicx`, `\mathbb` → `amsfonts`/`amssymb`), prüfe, ob es bereits geladen wird.
  - Falls nein, ergänze das entsprechende `\usepackage{...}` an der passenden Stelle in `T0_preamble_standalone_De.tex` (unter Beachtung der Reihenfolge-Kommentare in der Datei).
2. Wenn ein Makro/Umgebung T0-spezifisch ist (z.B. `\revolutionaer`, eigene Box-Umgebungen etc.):
  - Verwende eine globale Suche (`rg`/`grep`) im gesamten Repository nach der Makrodefinition (`\newcommand{\foo}`, `\newenvironment{foo}`, `\newtcolorbox{foo}`, etc.).
  - Übertrage die **Definition** (nicht den gesamten Kontext) nach `T0_preamble_standalone_De.tex` in den thematisch passenden Abschnitt (z.B. „T0-spezifische Befehle“, „tcolorbox-Umgebungen“).
  - Achte darauf, Namenskonflikte zu vermeiden (z.B. keine doppelte Definition desselben Makros mit unterschiedlichem Inhalt).
3. Wenn Paket- oder Makro-Konflikte auftreten (z.B. „Command ... already defined“):
  - Prüfe, ob die doppelte Definition in `T0_preamble_standalone_De.tex` oder lokal im Dokument liegt.
  - Bevorzuge die **Preambel-Definition** und entferne/kommentiere die weniger allgemeine/inkompatible Definition (vorzugsweise in der Datei, in der sie nur einmal verwendet wird).
4. Belasse die Schriftkonfiguration (Inter + JetBrains Mono + Libertinus Math) und die grundlegenden Strukturpakete (fontspec, unicode-math, babel, microtype, geometry etc.) unverändert, es sei denn, ein spezifischer Fehler zwingt zur Anpassung.

### 5. Re-Komponenten & Regressionstest
1. Nach jeder Änderung an `T0_preamble_standalone_De.tex`:
  - Re-kompiliere **zunächst nur die vorher fehlerhafte Datei**, um zu prüfen, ob der konkrete Fehler behoben ist.
  - Wenn erfolgreich, führe einen Kurztest mit 2–3 „repräsentativen“ anderen DE-Standalone-Dateien durch (z.B. `025_T0_Kosmologie_De.tex`, `063_cosmic_De.tex`, `201_FFGFT-alles_De.tex`).
2. Wiederhole diesen Zyklus (Fehleranalyse → Präambel anpassen → gezielt neu kompilieren), bis alle Dateien in `de_standalone` fehlerfrei durchlaufen.

### 6. Abgrenzung lokaler Sonderfälle
1. Falls eine bestimmte Datei sehr spezielle Makros oder Pakete benötigt, die **nur** in dieser Datei vorkommen und andere Dokumente potentiell stören würden:
  - Definiere diese Spezialmakros **lokal** am Anfang der betroffenen `.tex`-Datei (direkt nach `\input{T0_preamble_standalone_De}`), statt sie in die globale Präambel zu ziehen.
  - Dokumentiere solche Ausnahmen im Kommentar in der Datei (kurz: „Spezialmakros nur für dieses Dokument“).

### 7. Abschlussbericht
Zum Schluss:
1. Liste alle Dateien auf, die erfolgreich kompiliert wurden, und hebe eventuelle Ausnahmen hervor.
2. Gib eine kurze Zusammenfassung der wichtigsten Anpassungen an `T0_preamble_standalone_De.tex` (z.B. „neue Pakete“, „neue T0-spezifische Umgebungen“, „entfernte Konflikte“).
3. Verweise darauf, dass dieselbe Systematik später auch für `en_standalone` angewendet werden kann (separate englische Standalone-Preambel mit analogem Verfahren).

