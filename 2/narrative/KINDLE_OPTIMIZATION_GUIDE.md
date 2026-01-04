# Kindle/KDP-Optimierungs-Richtlinien für FFGFT Narrative Edition

## Übersicht

Dieses Dokument beschreibt alle notwendigen Schritte und Anforderungen zur Optimierung der FFGFT Narrative Edition PDFs für Amazon Kindle Direct Publishing (KDP).

---

## 1. Seitenformat und Ränder

### 1.1 Seitenformat
- **Format:** 6" × 9" (15.24 × 22.86 cm) - US Trade Book Standard
- **LaTeX-Code:**
  ```latex
  \usepackage[paperwidth=6in, paperheight=9in, ...]{geometry}
  ```

### 1.2 KDP-konforme Ränder
Für Bücher mit 200-270 Seiten gelten folgende **Mindestanforderungen**:
- **Innerer Rand (Bundsteg):** Minimum 0.5" (12.7 mm)
- **Äußerer Rand:** Minimum 0.25" (6.35 mm)
- **Oberer Rand:** Minimum 0.25" (6.35 mm)
- **Unterer Rand:** Minimum 0.25" (6.35 mm)

### 1.3 Empfohlene Ränder (mit Sicherheitsmargen)
```latex
\usepackage[
  paperwidth=6in, 
  paperheight=9in, 
  inner=0.625in,  % 25% über Minimum
  outer=0.625in,  % 150% über Minimum
  top=0.625in,    % 150% über Minimum
  bottom=1.0in,   % 300% über Minimum (Platz für Seitenzahlen!)
  twoside         % Für korrekte Buchbindung
]{geometry}
```

**Wichtig:** `twoside` aktiviert korrekte Rand-Verteilung für linke/rechte Seiten.

---

## 2. Formel-Optimierung für Kindle-Lesbarkeit

### 2.1 Problem
- Kindle/KDP lehnt PDFs mit Text < 7pt ab
- Standard LaTeX verkleinert Inline-Formeln automatisch
- Subscripts/Superscripts werden zu klein (< 7pt)

### 2.2 Lösung: Zweistufiger Ansatz

#### Schritt 1: displaystyle für Hauptformeln
```latex
\everymath{\displaystyle}      % Inline-Formeln in voller Größe
\everydisplay{\displaystyle}   % Display-Formeln optimiert
\relpenalty=10                 % Zeilenumbrüche bei Relationen erlauben
\binoppenalty=10               % Zeilenumbrüche bei binären Operatoren
```

**Effekt:**
- Inline-Formeln `$\frac{a}{b}$` werden NICHT verkleinert
- Brüche, Summen, Integrale ≥ 11pt
- Formeln können über mehrere Zeilen umbrechen

#### Schritt 2: DeclareMathSizes für Subscripts/Superscripts
```latex
\DeclareMathSizes{11}{11}{9}{8}     % Base 11pt: script=9pt, scriptscript=8pt
\DeclareMathSizes{10.95}{11}{9}{8}  % Für normalsize
```

**Effekt:**
- **Subscripts:** 9pt statt 7pt (+30%)
- **Superscripts:** 8pt statt 6pt (+33%)
- **ALLE** mathematischen Zeichen ≥ 8pt (deutlich über 7pt Minimum)

---

## 3. Tabellen-Optimierung

### 3.1 Problem
- Breite Tabellen gehen über Seitenränder hinaus
- KDP lehnt "Text außerhalb Ränder" ab

### 3.2 Lösung: resizebox
```latex
\resizebox{\textwidth}{!}{
  \begin{tabular}{...}
    % Tabelleninhalt
  \end{tabular}
}
```

**Effekt:**
- Tabelle passt sich automatisch an Seitenbreite an
- Verhältnis bleibt erhalten (Höhe skaliert mit)
- Text bleibt lesbar

### 3.3 Betroffene Kapitel
- Kapitel 4, 6, 7, 8, 9, 10, 11, 12, 13 (De + En)
- Jeweils 1-2 Tabellen pro Kapitel

---

## 4. Lange Formeln umbrechen

### 4.1 Problem
- Lange Formeln gehen über Seitenrand hinaus
- Overfull hbox Warnungen

### 4.2 Lösungen

#### Option 1: align* für mehrzeilige Formeln
```latex
\begin{align*}
  \text{Teil 1} &= \text{Ausdruck 1} \\
  &= \text{Ausdruck 2} \\
  &= \text{Ergebnis}
\end{align*}
```

#### Option 2: split innerhalb von equation
```latex
\begin{equation}
  \begin{split}
    \text{Lange Formel} &= \text{Teil 1} \\
    &\quad + \text{Teil 2}
  \end{split}
\end{equation}
```

#### Option 3: allowbreak in Inline-Formeln
```latex
$\text{Teil1} \allowbreak + \text{Teil2} \allowbreak + \text{Teil3}$
```

---

## 5. Zentrale Zeichenerklärung

### 5.1 Problem
- tcolorbox-Zeichenerklärungen in jedem Kapitel sind zu breit
- Wiederholungen erhöhen Seitenzahl unnötig

### 5.2 Lösung
- **Eine** zentrale Zeichenerklärung am Anfang (nach TOC)
- Einfache `itemize`-Liste statt tcolorbox
- Automatischer Seitenumbruch

### 5.3 Implementierung
Separate Dateien:
- `Zentrale_Zeichenerklaerung_De.tex` (Deutsch)
- `Zentrale_Zeichenerklaerung_En.tex` (Englisch)

Einbindung in Master-Dokument:
```latex
\tableofcontents
\input{Zentrale_Zeichenerklaerung_De}  % Nach TOC
\chapter{...}  % Erstes Kapitel
```

---

## 6. siunitx Custom Units

### 6.1 Erforderliche Definitionen
```latex
\DeclareSIUnit\gigalightyear{Gly}
\DeclareSIUnit\lightyear{ly}
\DeclareSIUnit\mev{MeV}
\DeclareSIUnit\gev{GeV}
```

### 6.2 Verwendung
```latex
\SI{13.8}{\gigalightyear}  % 13.8 Gly
\SI{4.2}{\lightyear}       % 4.2 ly
\SI{938}{\mev}             % 938 MeV
\SI{14}{\gev}              % 14 GeV
```

---

## 7. Iterative PDF-Kompilierung

### 7.1 Kompilierungs-Prozess
```bash
cd 2/narrative

# Deutsche PDF (4 Pässe mit sudo)
for i in {1..4}; do
  sudo pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_De.tex
done

# Englische PDF (4 Pässe mit sudo)
for i in {1..4}; do
  sudo pdflatex -interaction=nonstopmode FFGFT_Narrative_Master_En.tex
done
```

**Warum 4 Pässe?**
1. Pass: Erste Kompilierung, TOC erstellen
2. Pass: Referenzen auflösen
3. Pass: Seitenzahlen aktualisieren
4. Pass: Finale Version mit allen Referenzen

### 7.2 Warnungen Analysieren
```bash
# Overfull hbox Warnungen finden
grep "Overfull" FFGFT_Narrative_Master_De.log | grep "hbox"

# Underfull hbox Warnungen finden
grep "Underfull" FFGFT_Narrative_Master_De.log | grep "hbox"

# Nach Kapitel sortieren
grep "Overfull" *.log | grep -o "line [0-9]*" | sort | uniq -c
```

### 7.3 Kritische vs. Harmlose Warnungen

#### Kritisch (müssen behoben werden):
- **Overfull hbox > 5pt**: Text geht über Seitenrand hinaus
- **"Text außerhalb Ränder"** in KDP-Prüfung

#### Harmlos (können ignoriert werden):
- **"Improper \halign inside $$'s"**: displaystyle + align* Kompatibilität
- **hyperref PDF string Unicode**: Betrifft nur PDF-Lesezeichen
- **newunicodechar Redefining**: Rein kosmetisch
- **siunitx + physics Konflikt**: Beide Pakete funktionieren

---

## 8. Qualitätssicherung

### 8.1 Automatische Validierung
Check-Script für Dateilängen und Sprachen:
```bash
/tmp/check_files.sh
```

**Prüft:**
- ✅ Alle De-Dateien enthalten deutschen Text
- ✅ Alle En-Dateien enthalten englischen Text
- ✅ Keine versehentlichen Kürzungen
- ✅ Keine falschen Sprach-Kopien

### 8.2 Manuelle Prüfung
- [ ] PDF-Größe: De ~800-900 KB, En ~1.0-1.1 MB
- [ ] Seitenzahl: De ~180-210, En ~250-280
- [ ] Seitenformat: 6" × 9" (432 x 648 pts)
- [ ] Alle Formeln ≥ 8pt
- [ ] Keine Overfull > 5pt
- [ ] Seitenzahlen innerhalb der Ränder

---

## 9. KDP-Upload Checkliste

### 9.1 Vor dem Upload
- [ ] PDF kompiliert ohne kritische Fehler
- [ ] Alle Overfull hbox Warnungen < 5pt oder behoben
- [ ] Ränder überprüft (inner ≥ 0.5", outer/top ≥ 0.25", bottom ≥ 1.0")
- [ ] Formeln visuell geprüft (alle ≥ 7pt)
- [ ] Tabellen passen in Ränder
- [ ] Seitenzahlen sichtbar und innerhalb Ränder

### 9.2 KDP-Prüfung
KDP meldet typischerweise:
1. **"Unleserlicher Text"** → Formeln < 7pt
2. **"Text außerhalb Ränder"** → Overfull hbox
3. **"Unzureichender Bundsteg"** → inner < 0.5"

### 9.3 Bei Ablehnung
1. Log-Dateien analysieren
2. Betroffene Seiten/Zeilen identifizieren
3. Fixes anwenden (siehe Abschnitt 4)
4. Neu kompilieren und testen
5. Erneut hochladen

---

## 10. Wichtige Hinweise

### 10.1 NICHT tun
- ❌ Inline-Formeln manuell mit `\scriptstyle` verkleinern
- ❌ `\tiny`, `\small` für mathematische Symbole verwenden
- ❌ Ränder unter KDP-Minimum setzen
- ❌ tcolorbox-Boxen ohne Umbruch-Fähigkeit
- ❌ Tabellen ohne resizebox über Seitenbreite
- ❌ Deutsche Texte in En-Dateien kopieren (oder umgekehrt)

### 10.2 Best Practices
- ✅ displaystyle + DeclareMathSizes für alle Formeln
- ✅ resizebox für alle breiten Tabellen
- ✅ Zentrale Zeichenerklärung statt Wiederholungen
- ✅ Großzügige Ränder (25%+ über Minimum)
- ✅ 4 Pässe beim Kompilieren
- ✅ Automatische Validierung nach jeder Änderung
- ✅ Iterative Fehlerbehebung

---

## 11. Zusammenfassung

### Erfolgreiche Kindle-Optimierung erfordert:
1. ✅ **6x9" Format** mit KDP-konformen Rändern
2. ✅ **displaystyle** für Hauptformeln
3. ✅ **DeclareMathSizes** für Subscripts/Superscripts
4. ✅ **resizebox** für breite Tabellen
5. ✅ **Zentrale Zeichenerklärung** statt Wiederholungen
6. ✅ **Iterative Kompilierung** mit Warnungs-Analyse
7. ✅ **Automatische Validierung** von Längen und Sprachen
8. ✅ **Manuelle Prüfung** vor KDP-Upload

---

**Erstellt:** Januar 2026  
**Version:** 1.0  
**Autor:** Copilot für FFGFT Narrative Edition
