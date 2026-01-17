# Copilot Instructions: Compile Books with LuaLaTeX

Diese Datei dient als exakte Anweisung für einen Copilot-Agenten oder ein CI-Setup, um **alle fertigen Bücher** mit **LuaLaTeX** zu kompilieren.

## 1. Ziel

- Kompiliere alle fertigen Buch-Quellen unter `2\tex-n\completed` mit **LuaLaTeX**.
- Erzeuge für jede `.tex`-Datei ein passendes PDF unter `2\pdf` (Dateinamen wie im Repository bereits etabliert).
- Nutze dasselbe Preambel-/Font-Setup wie bereits für die Standalone-Dokumente (LuaLaTeX, moderne Fonts, Sprachpakete).

## 2. Benötigte LaTeX-Umgebung (Server, z.B. GitHub Actions Ubuntu)

Installiere vor der ersten Kompilierung ein vollständiges LuaLaTeX-Setup, inkl. **`siunitx`** und Sprachpakete für Deutsch/Englisch:

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

Annahme:
- LuaLaTeX wird über `lualatex` oder `latexmk -lualatex` aufgerufen.
- Die Buch-Preambeln nutzen `fontspec` und sind für LuaLaTeX vorbereitet (analog zu den Standalone-Fixes).

## 3. Zu kompilierende Buch-Quellen

Folgende Hauptdateien gelten als fertige Buch-Manuskripte und sollen vollständig mit LuaLaTeX gebaut werden:

- `2\tex-n\completed\Teil1a_De.tex`
- `2\tex-n\completed\Teil1a_En.tex`
- `2\tex-n\completed\Teil1.ebook_De.tex`
- `2\tex-n\completed\Teil1.ebook_En.tex`
- `2\tex-n\completed\Teil2_De.tex`
- `2\tex-n\completed\Teil2_En.tex`
- `2\tex-n\completed\Teil2.ebook_De.tex`
- `2\tex-n\completed\Teil2.ebook_En.tex`
- `2\tex-n\completed\Teil3a_De.tex`
- `2\tex-n\completed\Teil3a_En.tex`
- `2\tex-n\completed\Teil3.ebook_De.tex`
- `2\tex-n\completed\Teil3.ebook_En.tex`
- `2\tex-n\completed\T0_Anwendungen_De.tex`
- `2\tex-n\completed\T0_Anwendungen_En.tex`

Die resultierenden PDFs sollen im Verzeichnis `2\pdf` liegen (z.B. analog zu bereits vorhandenen Buch-PDFs).

## 4. Vorgehen für Copilot / Agent

1. **Repository auschecken** und in das Projektverzeichnis wechseln.
2. **TeX-Umgebung installieren** wie in Abschnitt 2 (nur falls noch nicht vorhanden).
3. Für jede Datei aus Abschnitt 3:
   - Im Verzeichnis `2/tex-n/completed` (auf Linux) `latexmk -lualatex -interaction=nonstopmode -halt-on-error <Datei>.tex` ausführen.
   - Sicherstellen, dass das PDF im Zielverzeichnis `2/pdf` landet (ggf. mit `-output-directory=../../pdf` oder angepassten Makefiles/Skripten).
4. Bei Kompilationsfehlern:
   - Logdateien (`*.log`) analysieren.
   - Nur die **minimale notwendige Änderung** an der betreffenden `.tex`-Datei oder der verwendeten Preambel vornehmen (z.B. fehlende Pakete nachladen wie `\usepackage{siunitx}` oder Sprachoptionen für `babel`/`polyglossia` korrigieren).
   - Änderungen committen und den Kompilationslauf für das betroffene Buch wiederholen.
5. Den Prozess wiederholen, bis **alle Buch-PDFs** fehlerfrei mit LuaLaTeX erzeugt werden.

## 5. Wichtige Randbedingungen

- **Keine Quellen löschen oder umbenennen**, außer explizit angewiesen.
- Bei Paketproblemen zuerst prüfen, ob die benötigten Pakete durch TeX Live installiert werden können, bevor Workarounds im Quelltext eingebaut werden.
- Physikalische Aussagen und Notation **nie inhaltlich verändern**, nur LaTeX-syntaktische oder paketbezogene Probleme beheben.
