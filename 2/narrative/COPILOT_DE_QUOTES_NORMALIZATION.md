# Copilot Task: Normalize German Quotes in DE Narrative Files

Branch: `copilot/reset-copilot-narrative` 
Directory: `2/narrative`

Ziel: In allen deutschen narrativen Dateien sollen Anführungszeichen konsequent im LaTeX-Format ``Text'' verwendet werden. Gemischte Unicode-Anführungszeichen („…“) und einfache ASCII-Doppelt-Anführungszeichen `"Text"` sollen systematisch ersetzt werden.

---

## 1. Geltungsbereich

Bearbeite **nur** folgende Verzeichnisse/Dateien:

- Deutsche Kapitel:
 - `2/narrative/de_chapters/Kapitel_XX_Narrative_De.tex`
- Deutsche Standalones:
 - `2/narrative/de_standalone/Kapitel_XXa_Narrative_De.tex`

Dabei gilt:
- **Keine** Änderungen in EN-Dateien.
- **Keine** Änderungen an den Master-Dokumenten (`FFGFT_Narrative_Master_*.tex`).
- **Keine** Änderungen an README oder anderen Hilfsdateien.

---

## 2. Ziel-Format für Anführungszeichen

Nach der Bereinigung sollen Anführungszeichen in den deutschen Narrativen nur noch so aussehen:

- LaTeX-Variante: 
 ```latex
 ``Text'
 ```

Unicode- und ASCII-Varianten sind zu vermeiden:

- `„Text“` (typografische Anführungszeichen) → **ersetzen**
- `"Text"` (einfache ASCII-Doppelt-Anführungszeichen) → **ersetzen**

---

## 3. Ersetzungsschema

### 3.1 Unicode-Anführungszeichen → LaTeX-Quotes

Ersetze in allen **DE-Kapitel- und DE-Standalone-Dateien** systematisch:

- `„` → `` (zwei Backticks)
- `“` → ' (zwei einfache Hochkommas)
- `”` → ' (falls vorhanden)

Beispiele:

- `„fraktale Geometrie“` → ``fraktale Geometrie'
- `„kosmisches Gehirn"` (gemischt) → zunächst Unicode bereinigen, dann ASCII, bis ` ``kosmisches Gehirn' ` entsteht.

### 3.2 ASCII-Doppelt-Anführungszeichen → LaTeX-Quotes

Ersetze **paarweise** einfache `"..."`-Anführungszeichen nur im Fließtext:

- `"Text"` → ``Text'

Dabei vorsichtig vorgehen:
- Nur solche Vorkommen ersetzen, bei denen auf **derselben Zeile** ein klarer Anfang und ein klares Ende `"` vorhanden sind.
- Vorkommen in Matheumgebungen und in Kommandos mit besonderer Syntax sind zu vermeiden (s.u.).

---

## 4. Bereiche, die NICHT verändert werden sollen

Bei allen Ersetzungen **keine** Änderungen vornehmen:

- Innerhalb von Mathe-Umgebungen:
 - Inline-Math: `$...$`, `\(...\)`
 - Display-Math: `\[...\]`, `equation`, `align`, `gather`, etc.
- In URL- oder Link-Kommandos:
 - `\url{...}`
 - `\href{...}{...}`
- In sonstigen LaTeX-Kommandos, bei denen `"` o.ä. bewusst verwendet werden könnte.

Falls unsicher, lieber das konkrete Vorkommen unverändert lassen.

---

## 5. Vorgehensvorschlag (Implementierung)

1. Schreibe ein kleines Skript (z.B. in Python), das:
  - Alle Dateien unter `de_chapters` und `de_standalone` mit Namen `Kapitel_*_Narrative_De.tex` durchläuft.
  - Den Inhalt einliest (UTF-8).
  - Zuerst alle Unicode-Anführungszeichen `„`, `“`, `”` durch ihre LaTeX-Entsprechungen ersetzt.
  - Anschließend einfache ASCII-Paare `"Text"` im Fließtext konvertiert zu ``Text'.

2. Achte darauf, dass Mathe- und URL-Bereiche (siehe Abschnitt 4) entweder übersprungen oder mit einem robusten Parser erkannt werden.

3. Schreibe die geänderten Inhalte zurück, **nur wenn** sich etwas verändert hat.

---

## 6. Kontrolle und Validierung

1. Nach der Ersetzung:
  - Führe `grep`-Checks aus, z.B.:
   - Suche nach verbliebenen `„`, `“`, `”` in `de_chapters` und `de_standalone`.
   - Suche nach isolierten `"` in denselben Verzeichnissen.

2. Stichprobenartig mehrere Kapitel öffnen (z.B. 5, 12, 13, 28, 35) und visuell prüfen, ob:
  - Anführungszeichen überall als ``Text' erscheinen.
  - Keine kaputten LaTeX-Konstrukte (z.B. in Mathe-Umgebungen) entstanden sind.

3. Danach (optional, aber empfohlen):
  - `FFGFT_Narrative_Master_De.tex` im Ordner `2/narrative` mehrfach kompilieren:
   ```bash
   cd 2/narrative
   for i in {1..3}; do
    pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_De.tex
   done
   ```
  - Das `.log`-File prüfen, ob **neue** Fehler durch die Quote-Anpassungen entstanden sind; falls ja, die betroffenen Stellen minimal korrigieren.

---

## 7. Versionierung

1. Nach erfolgreicher Normalisierung und Prüfung:
  - Nur diese Pfade zum Commit hinzufügen:
   - `2/narrative/de_chapters/*.tex`
   - `2/narrative/de_standalone/*.tex`

2. Commit-Message (Vorschlag):
  - `Normalize German quotes in DE narrative chapters/standalones to ``...'`

3. Änderungen nach `copilot/reset-copilot-narrative` pushen.

---

## 8. Erwartetes Ergebnis

- Alle deutschen narrativen Kapitel und Standalone-Dateien verwenden **einheitlich** LaTeX-Anführungszeichen im Format ``Text'.
- Es gibt keine gemischten Unicode-Quotes mehr, und der optische Eindruck der Anführungszeichen (inkl. Abstände) ist konsistent.
- `FFGFT_Narrative_Master_De.tex` kompiliert weiterhin fehlerfrei.


