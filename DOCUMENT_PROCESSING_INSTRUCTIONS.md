# Anweisungen für die Dokumentenverarbeitung

## WICHTIG: Diese Anweisungen MÜSSEN bei JEDEM Dokument befolgt werden!

## Workflow pro Dokument (EIN Dokument nach dem anderen!)

### 1. ÜBERARBEITUNG VOR der Kompilierung

**BEVOR du kompilierst, MUSS das Dokument überarbeitet werden:**

#### A. Encoding-Artefakte finden und beheben
- Suche nach `\u0000` oder anderen Null-Bytes in Umlauten
- Beispiele:
  - `k\u0000f6nnen` → `können`
  - `Verh\u0000e4ltnisse` → `Verhältnisse`
  - `f\u0000fcr` → `für`
- Methode: Mit `grep` oder manueller Inspektion nach `\u0000` suchen

#### B. Zerbrochene LaTeX-Befehle reparieren
- Prüfe alle `\begin{}` haben ein passendes `\end{}`
- Prüfe auf unvollständige Befehle (z.B. `\textb` ohne `f`)
- Prüfe auf doppelte oder falsche `\documentclass` Zeilen

#### C. g-2-Policy prüfen
- Detaillierte g-2-Formeln und numerische Vorhersagen NUR in:
  - `018_T0_Anomale-g2-10_De.tex`
  - `018_T0_Anomale-g2-10_En.tex`
- In ALLEN anderen Dokumenten:
  - g-2 darf nur qualitativ erwähnt werden
  - ODER mit Verweis auf die 018-Dokumente
  - KEINE exakten numerischen Vorhersagen
- Wenn falsche g-2-Details gefunden werden:
  - Entfernen oder auf qualitative Beschreibung reduzieren
  - Verweis auf 018-Dokumente hinzufügen

#### D. Preamble-Referenz anpassen
- In `de_standalone_processed`: `\input{T0_preamble_standalone_De.tex}`
- In `en_standalone_processed`: `\input{T0_preamble_standalone_En.tex}`

#### E. Physikalischen Inhalt NICHT ändern
- Mathematische Formeln (außer LaTeX-Syntax): UNVERÄNDERT
- Physikalische Argumente: UNVERÄNDERT
- Wissenschaftlicher Inhalt: UNVERÄNDERT

### 2. SPEICHERN der überarbeiteten Version

- Original bleibt in `2/tex-n/de_standalone/` UNVERÄNDERT
- Überarbeitete Version wird in `2/tex-n/de_standalone_processed/` gespeichert
- Gleicher Dateiname wie Original

### 3. KOMPILIERUNG

```bash
cd /home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/tex-n/de_standalone_processed
lualatex -interaction=nonstopmode -synctex=1 DOKUMENT.tex
lualatex -interaction=nonstopmode -synctex=1 DOKUMENT.tex
lualatex -interaction=nonstopmode -synctex=1 DOKUMENT.tex
```

**Mindestens 3 Durchläufe** für Referenzen, Inhaltsverzeichnis, etc.

### 4. FEHLERANALYSE (wenn Kompilierung fehlschlägt)

#### A. .log-Datei öffnen und analysieren
- Suche nach ersten signifikanten Fehler:
  - `! LaTeX Error:`
  - `! Undefined control sequence`
  - `! Missing \end{}`
  - `! Package ... Error:`
  - `! File ... not found`

#### B. Fehler MINIMAL beheben
- NUR den spezifischen Fehler beheben
- Keine anderen Änderungen
- In der überarbeiteten Datei in `*_processed/` korrigieren

#### C. Erneut kompilieren (Schritt 3)

#### D. REKURSIV wiederholen bis keine Fehler mehr

### 5. PDF-AUSGABE

- PDF nach `2/pdf/DOKUMENT.pdf` verschieben
- Bestehende PDFs NICHT löschen, nur überschreiben

### 6. INHALTSPRÜFUNG

- Öffne das PDF kurz
- Prüfe ob g-2-Policy eingehalten wurde
- Prüfe ob physikalischer Inhalt korrekt aussieht

### 7. COMMIT und NEXT

- Commit mit aussagekräftiger Message:
  - `Document X/118: DOKUMENT.tex - reviewed and compiled successfully`
- ERST DANN nächstes Dokument beginnen

## VERBOTEN

- ❌ Mehrere Dokumente gleichzeitig verarbeiten
- ❌ Batch-Processing
- ❌ Dokumente kompilieren ohne vorherige Überarbeitung
- ❌ Physikalischen Inhalt ändern
- ❌ PDFs löschen
- ❌ Originale in `de_standalone/` oder `en_standalone/` ändern

## CHECKLISTE pro Dokument

- [ ] Original aus `de_standalone/` gelesen
- [ ] Encoding-Artefakte gesucht und behoben
- [ ] LaTeX-Syntax geprüft (`\begin{}`/`\end{}` Paare)
- [ ] g-2-Policy geprüft
- [ ] Preamble-Referenz angepasst
- [ ] In `de_standalone_processed/` gespeichert
- [ ] 3x mit LuaLaTeX kompiliert
- [ ] Bei Fehler: .log analysiert und rekursiv behoben
- [ ] PDF nach `2/pdf/` verschoben
- [ ] Inhalt geprüft (g-2, Physik)
- [ ] Committed
- [ ] Nächstes Dokument starten

## Wichtigste Regel

**EIN DOKUMENT NACH DEM ANDEREN!**
**ERST ÜBERARBEITEN, DANN KOMPILIEREN!**
