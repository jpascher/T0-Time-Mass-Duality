# AGENTS – Branchanweisungen für `copilot/fix-copilot-narrative-issues`

## Kontext
- Dieser Branch dient dazu, die README-Dateien an den aktuellen Stand der Bücher im Projekt **T0-Time-Mass-Duality** anzupassen.
- Hauptänderungen: Es gibt neue Bücher, die auf **Kindle veröffentlicht** wurden und zusätzlich als **PDF im Repository** verfügbar sind (z.B. unter `2\pdf\` und `2\tex-n\completed\`).

## Aufgaben für Copilot in diesem Branch

1. **Änderungen im Repository analysieren**
   - Wenn der Nutzer nach README-/Dokumentations-Updates fragt, untersuche die Änderungen relativ zu `origin/main` (z.B. mit `git diff --name-status origin/main...HEAD`).
   - Identifiziere insbesondere neue oder geänderte Dateien, die Bücher betreffen:
     - PDF-Dateien unter `2\pdf\`
     - Fertige Buch-/Kapitel-Quellen unter `2\tex-n\completed\` (oder vergleichbaren Verzeichnissen)
   - Erstelle eine kurze Zusammenfassung, welche neuen Bücher/Konfigurationen hinzugekommen sind.

2. **Vorschläge für README-Updates erstellen**
   - Erarbeite auf Basis der gefundenen Änderungen Vorschläge für:
     - `README.md`
     - `README_de.md`
     - `README-TEST.md`
   - Ziel der Änderungen:
     - Neue Bücher aufführen (Titel, Sprache, Format: Kindle, PDF).
     - Klare Hinweise geben, wo die PDFs im Repo liegen (Windows-Pfade mit Backslashes benutzen).
     - Optional auf den Veröffentlichungsstatus (z.B. „auf Kindle verfügbar“) hinweisen.

3. **Arbeitsweise bei Dateiänderungen**
   - Bevor du eine dieser README-Dateien änderst:
     - Erkläre in **3–5 Stichpunkten**, welche Inhalte du ändern oder ergänzen willst und in welcher Datei.
     - Zeige, falls sinnvoll, kurze Text-Snippets als Vorschau.
     - Warte auf eine **eindeutige Bestätigung** des Nutzers, bevor du `edit`-Aktionen auf den Dateien ausführst.

4. **Stilvorgaben für Texte**
   - Formulierungen sollen **präzise und wissenschaftlich klingend** sein.
   - Keine Vereinfachungen, die die physikalische oder konzeptionelle Intention verfälschen.
   - Neue Konzepte immer zuerst inhaltlich/physikalisch kurz einordnen, danach technische Details (Dateistruktur, Skripte, Build-Schritte).

5. **Technische Details beachten**
   - Pfade im Text immer mit **Backslashes** angeben (Windows-Konvention), z.B. `2\pdf\Teil1a_De.pdf`.
   - Bei längeren technischen Erklärungen: Schritt-für-Schritt-Vorgehen bevorzugen.
   - Wenn du Tabellen in Markdown vorschlägst, halte Zeilen möglichst unter 80 Zeichen und nutze `<br>` oder mehrzeilige Zellen für Umbrüche.

---

Diese Anweisungen gelten speziell für Arbeiten im Branch `copilot/fix-copilot-narrative-issues`, insbesondere wenn es um das **Aktualisieren der README-Dateien im Zuge neuer Bücher/Publikationen** geht.