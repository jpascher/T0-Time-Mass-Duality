# Anleitung: Zentrale Zeichenerklärung Implementieren

## Problem
KDP meldet "Text/Objekte außerhalb der Ränder" weil tcolorbox-Zeichenerklärungen in vielen Kapiteln zu lang sind und nicht umbrechen.

## Lösung
Eine zentrale Zeichenerklärung am Anfang des Buchs als einfache Liste, die automatisch über mehrere Seiten umbricht.

---

## Schritt 1: Zentrale Zeichenerklärung in Master-Dokumente einfügen

### Für Deutsche Version (FFGFT_Narrative_Master_De.tex):

Suche nach `\begin{document}` und füge DIREKT DANACH ein:

```latex
\begin{document}

% Zentrale Zeichenerklärung (ersetzt alle individuellen tcolorbox-Notationen)
\input{Zentrale_Zeichenerklaerung_De}

\maketitle
\tableofcontents
\clearpage
```

### Für Englische Version (FFGFT_Narrative_Master_En.tex):

Suche nach `\begin{document}` und füge DIREKT DANACH ein:

```latex
\begin{document}

% Central Notation Guide (replaces all individual tcolorbox notations)
\input{Zentrale_Zeichenerklaerung_En}

\maketitle
\tableofcontents
\clearpage
```

---

## Schritt 2: Individuelle tcolorbox-Zeichenerklärungen entfernen

### Betroffene Dateien (laut grep-Suche):

Es sind über 100 Dateien betroffen. Hier die systematische Vorgehensweise:

### Automatisches Entfernen mit sed (empfohlen):

```bash
cd /home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/narrative

# Backup erstellen
mkdir -p backup_before_notation_removal
cp Kapitel_*_Narrative_*.tex backup_before_notation_removal/

# Alle tcolorbox-Blöcke entfernen (Deutsche + Englische Varianten)
for file in Kapitel_*_Narrative_De*.tex; do
    # Entferne tcolorbox-Blöcke mit "Notation" oder "Zeichen" im Titel
    sed -i '/\\begin{tcolorbox}.*Notation/,/\\end{tcolorbox}/d' "$file"
    sed -i '/\\begin{tcolorbox}.*Zeichen/,/\\end{tcolorbox}/d' "$file"
    sed -i '/\\begin{tcolorbox}.*Symbol/,/\\end{tcolorbox}/d' "$file"
done

for file in Kapitel_*_Narrative_En*.tex; do
    # Entferne tcolorbox-Blöcke mit "Notation" oder "Symbol" im Titel
    sed -i '/\\begin{tcolorbox}.*Notation/,/\\end{tcolorbox}/d' "$file"
    sed -i '/\\begin{tcolorbox}.*Symbol/,/\\end{tcolorbox}/d' "$file"
done
```

### Manuelle Alternative:

Öffne jede Datei und suche nach:
- `\begin{tcolorbox}[title={Notation` oder
- `\begin{tcolorbox}[title={Zeichen` oder
- `\begin{tcolorbox}[title={Symbol`

Lösche den gesamten Block bis `\end{tcolorbox}`.

---

## Schritt 3: PDFs neu kompilieren

```bash
cd /home/runner/work/T0-Time-Mass-Duality/T0-Time-Mass-Duality/2/narrative

# Deutsche PDF (4 Pässe für vollständiges TOC)
pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_De.tex
pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_De.tex
pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_De.tex
pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_De.tex

# Englische PDF (4 Pässe für vollständiges TOC)
pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_En.tex
pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_En.tex
pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_En.tex
pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_En.tex

# PDFs kopieren nach /2/pdf/
cp FFGFT_Narrative_Master_De.pdf ../pdf/
cp FFGFT_Narrative_Master_En.pdf ../pdf/
```

---

## Schritt 4: Ergebnis überprüfen

Die neuen PDFs sollten haben:
- ✅ Eine zentrale Zeichenerklärung am Anfang (nach Titelseite, vor Inhaltsverzeichnis)
- ✅ Keine tcolorbox-Zeichenerklärungen mehr in den Kapiteln
- ✅ Weniger "Text außerhalb Ränder" Warnungen von KDP
- ✅ Die Zeichenerklärung bricht automatisch über mehrere Seiten um (einfache Liste)

---

## Schritt 5: Wenn noch Probleme bleiben

Falls KDP immer noch "Text außerhalb Ränder" meldet, sind es wahrscheinlich:
1. **Zu lange Formeln** - Lösung: `\allowdisplaybreaks` in Preamble
2. **Zu lange Tabellen** - Lösung: `longtable` statt `tabular` verwenden
3. **Zu große Bilder** - Lösung: `\includegraphics[width=0.9\textwidth]` verwenden

---

## Dateien erstellt:

1. `Zentrale_Zeichenerklaerung_De.tex` - Deutsche zentrale Zeichenerklärung
2. `Zentrale_Zeichenerklaerung_En.tex` - Englische zentrale Zeichenerklärung
3. `ANLEITUNG_Zeichenerklaerung_Entfernen.md` - Diese Anleitung

---

## Vorteile der zentralen Zeichenerklärung:

- ✅ **Einmalig gepflegt** - Änderungen nur an einer Stelle
- ✅ **Keine Box-Überlauf-Probleme** - Einfache Listen brechen automatisch um
- ✅ **Weniger Seiten** - Reduziert Gesamtseitenzahl (weniger Wiederholungen)
- ✅ **Bessere Übersicht** - Leser haben alle Symbole an einem Ort
- ✅ **KDP-kompatibel** - Keine festen Boxen die über Ränder hinausgehen

---

## Backup-Strategie:

Vor dem Entfernen der tcolorboxen wurde empfohlen ein Backup zu erstellen:
```bash
mkdir -p backup_before_notation_removal
cp Kapitel_*_Narrative_*.tex backup_before_notation_removal/
```

Bei Problemen können Sie zurück:
```bash
cp backup_before_notation_removal/* .
```
