# Copilot Instructions – T0-Time-Mass-Duality Projekt

## Allgemeine Projekt-Regeln
- Dieses Projekt beschäftigt sich mit Konzepten zu Zeit-Masse-Dualität
- Bevorzuge präzise, wissenschaftlich klingende Formulierungen
- Verwende LaTeX für alle mathematischen Ausdrücke und Tabellen
- Keine Vereinfachungen, wenn sie die physikalische Intention verfälschen

## Wichtige technische Regeln
- Bei Markdown-Tabellen: niemals mehr als 80 Zeichen pro Zeile → bei Bedarf Zeilenumbruch mit <br> oder mehrzeilige Zellen
- Overflow-Probleme in gerenderten Markdown-Tabellen vermeiden
- Bei langen LaTeX-Ausdrücken: nutze displaymath ($$ … $$) oder equation-Umgebung
- Dateinamen und Pfade immer mit Backslashes unter Windows schreiben

## Bevorzugte Arbeitsweise
- Bei Code-Vorschlägen: immer PowerShell-kompatibel (kein Bash, wenn nicht explizit gewünscht)
- Bei Erklärungen: Schritt-für-Schritt, mit maximaler Transparenz
- Bei neuen Konzepten: immer erst die physikalische Idee erklären, dann erst die Implementierung

## Datei-Organisation
- Wichtige Notizen und Merkhilfen → in local-copilot-notes.md
- Diese Instructions-Datei ist die primäre Steuerdatei für Copilot-Verhalten im Projekt
- Alle zukünftigen Änderungen an Copilot-Regeln bitte hier dokumentieren

## LaTeX / LuaLaTeX-Kompilierung
- Standard-Kompiler ist **lualatex** (nicht mehr pdflatex).
- Die Skripte `compile_all_tex.sh`, `compile_all_narrative.sh`, `2/narrative/compile_all.sh` und `compile_standalone_recursive.sh` rufen intern `lualatex` auf.
- Vor dem ersten Lauf: vollständige LaTeX-Distribution mit LuaLaTeX und Sprachpaketen für Deutsch/Englisch installieren (z.B. TeX Live full oder äquivalent); fehlende Pakete bei Kompilierfehlern nachinstallieren.
- Für das systematische Testen aller Standalone-Dokumente bevorzugt `compile_standalone_recursive.sh` verwenden und anhand der erzeugten Log-Dateien iterativ die Fehler beheben.

