# Copilot Instructions: Compile Narrative Book with LuaLaTeX

Diese Datei dient als präzise Anweisung für einen Copilot-Agenten oder ein CI-Setup, um das **Narrative FFGFT-Buch** mit **LuaLaTeX** zu kompilieren.

## 1. Ziel

- Kompiliere die narrativen Hauptdokumente unter `2\narrative` mit **LuaLaTeX**.
- Erzeuge für jede Sprachversion ein konsistentes PDF unter `2\pdf`:
  - `FFGFT_Narrative_Master_De.pdf`
  - `FFGFT_Narrative_Master_En.pdf`
- Nutze dasselbe moderne LuaLaTeX-/Font-/Sprach-Setup wie für die restlichen Bücher und Standalone-Dokumente.

## 2. Benötigte LaTeX-Umgebung (Server, z.B. GitHub Actions Ubuntu)

Installiere (falls noch nicht vorhanden) ein vollständiges LuaLaTeX-Setup inkl. Sprach- und Wissenschaftspaketen:

```bash
sudo apt-get update
sudo apt-get install -y \
  texlive-latex-recommended \
  texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-fonts-extra \
  texlive-luatex \
  texlive-lang-german \
  texlive-lang-english \
  texlive-science \
  latexmk
```

Annahmen:
- Kompilation mit `latexmk -lualatex -interaction=nonstopmode -halt-on-error`.
- Preambeln verwenden `fontspec` und sind bereits an LuaLaTeX angepasst (ggf. analog zu den anderen LuaLaTeX-Preambeln im Projekt).

## 3. Zu kompilierende Narrative-Hauptdokumente und Header-Wahl (Buchformat)

**WICHTIG (Schritt 1):** Das Narrative-Buch nutzt dieselben Buch-Preambeln wie die übrigen FFGFT-Hauptdokumente. Die Master-Dokumente sollen daher die gemeinsamen Preambeln

- `T0_preamble_shared_De.tex`
- `T0_preamble_shared_En.tex`

über `\\input{../../T0_preamble_shared_De}` bzw. `\\input{../../T0_preamble_shared_En}` einbinden. Diese Preambeln sind aktuell mit `geometry` auf ein Buchformat von `paperwidth=8.25in` und `paperheight=11in` eingestellt.

Folgende Dateien gelten als Hauptmanuskripte des narrativen FFGFT-Buches und müssen mit LuaLaTeX gebaut werden:

- `2\\narrative\\FFGFT_Narrative_Master_De.tex`
- `2\\narrative\\FFGFT_Narrative_Master_En.tex`

Die Kapiteldateien unter `2\\narrative\\de_chapters`, `2\\narrative\\en_chapters`, `2\\narrative\\de_standalone` und `2\\narrative\\en_standalone` werden jeweils über diese Master-Dokumente eingebunden und müssen nur dann separat kompiliert werden, wenn dies für Fehlersuche notwendig ist.

Die resultierenden PDFs sollen unter `2\\pdf` liegen und die Dateinamen

- `2\pdf\FFGFT_Narrative_Master_De.pdf`
- `2\pdf\FFGFT_Narrative_Master_En.pdf`

tragen (analog zum bestehenden Stand im Repository).

## 4. Vorgehen für Copilot / Agent

1. **Branch auschecken** (z.B. `copilot/fix-latex-standalone-compile` oder `main`, je nach Auftrag).
2. **TeX-Umgebung installieren**, wie in Abschnitt 2 beschrieben (falls auf dem Runner noch nicht vorhanden).
3. In das Verzeichnis `2/narrative` wechseln:

   ```bash
   cd 2/narrative
   ```

4. Für jede der beiden Sprachversionen aus Abschnitt 3 ausführen:

   ```bash
   latexmk -lualatex -interaction=nonstopmode -halt-on-error \
     -output-directory=../pdf \
     FFGFT_Narrative_Master_De.tex

   latexmk -lualatex -interaction=nonstopmode -halt-on-error \
     -output-directory=../pdf \
     FFGFT_Narrative_Master_En.tex
   ```

5. Nach der Kompilierung prüfen:
   - Existieren `2/pdf/FFGFT_Narrative_Master_De.pdf` und `2/pdf/FFGFT_Narrative_Master_En.pdf`?
   - Sind die PDFs vollständig (keine auffälligen Fehlermeldungsseiten am Anfang/Ende)?

6. Bei Kompilationsfehlern:
   - Die zugehörige `.log`-Datei im Ausgabeverzeichnis analysieren.
   - Nur die **minimal notwendige Änderung** an der entsprechenden `.tex`-Datei oder Preambel vornehmen, z.B.:
     - Nachladen fehlender Standardpakete (`siunitx`, weitere Core-Pakete),
     - Anpassen von Sprachoptionen (`babel`/`polyglossia`) für Deutsch/Englisch,
     - Bereinigen von veralteten `pdflatex`-spezifischen Einstellungen, die unter LuaLaTeX nicht mehr gelten.
   - Erneut mit `latexmk -lualatex` kompilieren.

7. Änderungen in sinnvollen, kleinen Batches committen, z.B.:

   - `Fix LuaLaTeX narrative compilation (De)`
   - `Fix LuaLaTeX narrative compilation (En)`

   und anschließend auf den Ziel-Branch pushen.

## 5. Nutzung von vorhandenen Skripten

- Es existiert das Skript `compile_all_narrative.sh` im Repository-Root.
- Dieses Skript darf angepasst werden, um LuaLaTeX zu verwenden (anstelle von `pdflatex`), **sofern** die Änderungen minimal bleiben und nur die Kompilationswerkzeuge betreffen.
- Wenn möglich, orientiere dich an der LuaLaTeX-Umstellung in `compile_standalone_recursive.sh` und `compile_books.py`, um ein konsistentes Verhalten im gesamten Projekt sicherzustellen.

## 6. Randbedingungen

- Keine Quellen oder PDFs löschen oder umbenennen, außer dies ist explizit durch den Auftrag oder bestehende Projektkonventionen vorgegeben.
- **Physikalische, konzeptionelle und narrative Inhalte dürfen nicht verändert werden**; erlaubt sind ausschließlich LaTeX-syntaktische und paketbezogene Anpassungen.
- Bevor neue Workarounds eingeführt werden, orientiere dich an bereits etablierten LuaLaTeX-Lösungen im Projekt (Preambel-Strukturen, Font-Setups, Sprachkonfigurationen).
