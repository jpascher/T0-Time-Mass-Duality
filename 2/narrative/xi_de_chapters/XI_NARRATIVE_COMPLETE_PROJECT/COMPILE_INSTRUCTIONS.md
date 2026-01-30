# KOMPILIER-ANLEITUNG

## Voraussetzungen

**LaTeX:**
```bash
sudo apt install texlive-full  # Linux
brew install --cask mactex     # macOS
```

**Fonts:**
```bash
sudo apt install fonts-inter fonts-jetbrains-mono fonts-libertinus
```

## Kompilieren

```bash
lualatex Xi_Narrative_Master_De_COMPLETE_REBUILD.tex
lualatex Xi_Narrative_Master_De_COMPLETE_REBUILD.tex
```

⚠️ **WICHTIG:** Verwende LuaLaTeX (NICHT pdflatex)!

## Ergebnis

✅ PDF: Xi_Narrative_Master_De_COMPLETE_REBUILD.pdf  
✅ ~150-200 Seiten, 6×9" Buchformat

## Bei Problemen

**Font-Fehler:**
```bash
fc-cache -fv  # Font-Cache aktualisieren
```

**Compilation-Fehler:**
```bash
# Prüfe Log-Datei:
less Xi_Narrative_Master_De_COMPLETE_REBUILD.log
```
