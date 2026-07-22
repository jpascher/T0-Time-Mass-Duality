# A-Serie Workflow — Anweisungen für Erweiterungen

Dieses Dokument beschreibt den vollständigen Arbeitsablauf für:
- Ein neues A-Dokument anlegen
- Ein bestehendes A-Dokument überarbeiten
- ZIP-Release erstellen

Alle Pfade relativ zu: `/home/claude/ffgft/A_Serie_Komplett/`

---

## 1. Neues Dokument anlegen

### 1a. Nummer wählen

- Block 0: A010–A095 (Grundlage)
- Block 1: A100–A192 (Sektoren)
- Block 2: A200–A250 (Methodik)
- Block 3: A260–: Erweiterungen (kein Rückverweis aus Block 0/1 nötig)
- Zwischennummer (z.B. A095) nur wenn das neue Doc von einem bestehenden verwiesen wird
- Sonst: nächste freie Nummer in Block 3 (A268, A270, ...)

### 1b. De-Quelldatei anlegen

```
ch/AXXX_Titel_De_ch.tex
```

Pflichtstruktur:

```latex
\section{Worum es geht}
\textbf{[SETZUNG]} ...

% weitere Sektionen mit [SETZUNG]/[K]/[B]/[S]-Markierungen

\section{Prüfskript}
\begin{itemize}
  \item \texttt{python/A\_Serie\_Skripte/aXXX\_*.py}
\end{itemize}

\section{Zeichenerklärung}   % falls neue Symbole

\section{Was offen bleibt}
\textbf{Erstens ...}

\section{Ersetzt}
Dieses Dokument nimmt auf: Dok.~NNN (...).

\section{Verwendung von KI-Werkzeugen}
Dieses Dokument ist unter Verwendung KI-gestützter Werkzeuge entstanden. Die
Fragestellungen, die Setzungen und alle inhaltlichen Entscheidungen stammen vom
Autor; die Werkzeuge formulieren aus, rechnen nach und erstellen Prüfskripte.
Die Verantwortung für Inhalt und Fehler liegt vollständig beim Autor. Der
ausführliche Wortlaut steht in A010.
```

**Ausnahme A010:** KI-Abschnitt steht ganz am Anfang (vor allen anderen Sektionen).

### 1c. En-Quelldatei anlegen

```
ch/AXXX_Titel_En_ch.tex
```

Entspricht De-Datei mit:
- `[SETZUNG]` → `[STIPULATION]`
- `{,}` → `{.}` (Dezimalkomma)
- KI-Disclaimer: `This document was created with the assistance of AI tools. ...`
- `\section{Worum es geht}` → `\section{Purpose}`
- `\section{Was offen bleibt}` → `\section{Open Questions}`
- `\section{Zeichenerklärung}` → `\section{Symbol Glossary}`
- `\section{Prüfskripte}` → `\section{Verification Scripts}`
- `\section{Ersetzt}` → `\section{Supersedes}`
- `\section{Verwendung von KI-Werkzeugen}` → `\section{Use of AI Tools}`
- Tabellenkopf `Bedeutung` → `Meaning`
- Alle Fließtext-Abschnitte auf Englisch übersetzen

### 1d. Wrapper anlegen

**De-Wrapper** (`wr_standalone_A4/AXXX_Titel_De.tex`):
```latex
\documentclass[11pt]{report}
\input{../pri-end/T0_preamble_standalone_A4_De}
\input{../pri-end/T0_preamble_patches.tex}
\title{AXXX -- Deutscher Titel}
\author{Johann Pascher}
\date{Juli 2026}
\begin{document}\maketitle\tableofcontents
\input{../ch/AXXX_Titel_De_ch}
\end{document}
```

**En-Wrapper** (`wr_standalone_A4/AXXX_Titel_En.tex`):
```latex
\documentclass[11pt]{report}
\input{../pri-end/T0_preamble_standalone_A4_En}
\input{../pri-end/T0_preamble_patches.tex}
\title{AXXX -- English Title}
\author{Johann Pascher}
\date{July 2026}
\begin{document}\maketitle\tableofcontents
\input{../ch/AXXX_Titel_En_ch}
\end{document}
```

**Wichtig:** En-Wrapper-Titel muss auf Englisch sein (nicht Deutsch).

### 1e. Prüfskript anlegen

```
python/A_Serie_Skripte/aXXX_kurztitel.py
```

Mindeststruktur:
```python
#!/usr/bin/env python3
"""Prüfskript für AXXX — Kurzbeschreibung."""
import math

XI = 4/30000
K_FRAK = 1 - 100*XI

def test_hauptaussage():
    # ... Rechnung
    assert abs(ergebnis - erwartung) < toleranz, f"Abweichung: {ergebnis}"
    print("BESTANDEN: Hauptaussage")

if __name__ == "__main__":
    test_hauptaussage()
    print("Alle Tests BESTANDEN.")
```

---

## 2. Kompilieren

### Einzelnes Dokument (3 Läufe für korrektes TOC):
```bash
cd wr_standalone_A4
rm -f AXXX_Titel_De.toc AXXX_Titel_De.aux
for i in 1 2 3; do
  lualatex -interaction=nonstopmode -halt-on-error AXXX_Titel_De.tex
done
```

### Alle De-Dokumente prüfen:
```bash
python3 pruef_a_serie.py    # Syntax-/Strukturprüfung
python3 audit_a_serie.py    # Inhaltliche Konsistenz
```

### Alle Docs neu kompilieren (3 Blöcke wegen Timeout):
```bash
cd wr_standalone_A4

# Block 0
for f in A0*_De.tex A0*_En.tex; do
  rm -f "${f%.tex}.toc" "${f%.tex}.aux"
  for i in 1 2 3; do lualatex -interaction=nonstopmode "$f" >/dev/null 2>&1; done
done

# Block 1
for f in A1*_De.tex A1*_En.tex A192*_De.tex A192*_En.tex; do
  rm -f "${f%.tex}.toc" "${f%.tex}.aux"
  for i in 1 2 3; do lualatex -interaction=nonstopmode "$f" >/dev/null 2>&1; done
done

# Block 2+3
for f in A2*_De.tex A2*_En.tex; do
  rm -f "${f%.tex}.toc" "${f%.tex}.aux"
  for i in 1 2 3; do lualatex -interaction=nonstopmode "$f" >/dev/null 2>&1; done
done
```

---

## 3. Pflichtaktualisierungen bei neuem/geändertem Dokument

### A230 (Offene Punkte) aktualisieren
- Neue offene Punkte aus dem neuen Doc eintragen
- Punkte die geschlossen wurden in Abschnitt "Geschlossene Punkte" verschieben
- De + En beide aktualisieren

### A250 (Verweistabelle) aktualisieren
- Neues Dokument + aufgenommene Altdok-Nummern in Tabelle eintragen
- De + En beide aktualisieren

### A240 (Abgrenzung) prüfen
- Falls das neue Doc den Eichsektor, GR oder externe Rahmen berührt: anpassen

### A010 (Aufbau) prüfen
- Block-3-Liste in Abschnitt "Aufbau und Nummerierung" ergänzen

### CHANGELOG.md aktualisieren
```markdown
## vX.Y — YYYY-MM-DD

### Neu
- AXXX Kurztitel (neu): was es leistet

### Geändert
- AXXX bestehend: was geändert wurde, warum
```

### README.md prüfen
- Blockliste ergänzen
- "Neu in dieser Fassung" aktualisieren
- Tabelle der hergeleiteten Größen ergänzen falls relevant

---

## 4. Prüfliste vor ZIP-Release

```
[ ] Neues/geändertes De-Dokument kompiliert ohne Fehler (3 Läufe)
[ ] Neues/geändertes En-Dokument kompiliert ohne Fehler (3 Läufe)
[ ] En-Wrapper-Titel auf Englisch
[ ] Prüfskript läuft durch (BESTANDEN)
[ ] pruef_a_serie.py: 0 Fehler
[ ] A230 aktualisiert (De + En)
[ ] A250 Tabelle aktualisiert (De + En)
[ ] A240 geprüft
[ ] A010 Block-Liste geprüft
[ ] CHANGELOG.md aktualisiert
[ ] README.md aktualisiert
```

---

## 5. ZIP-Release erstellen

```bash
BASE=/home/claude/ffgft/A_Serie_Komplett

cd /tmp && rm -rf A_Serie_Export && mkdir -p \
  A_Serie_Export/Sources/ch \
  A_Serie_Export/Sources/pri-end \
  A_Serie_Export/Sources/wr_standalone_A4 \
  A_Serie_Export/pdf \
  A_Serie_Export/python/A_Serie_Skripte

# Quelltexte
cp $BASE/ch/A*_De_ch.tex          A_Serie_Export/Sources/ch/
cp $BASE/ch/A*_En_ch.tex          A_Serie_Export/Sources/ch/
cp $BASE/pri-end/*.tex             A_Serie_Export/Sources/pri-end/
cp $BASE/wr_standalone_A4/A*_De.tex A_Serie_Export/Sources/wr_standalone_A4/
cp $BASE/wr_standalone_A4/A*_En.tex A_Serie_Export/Sources/wr_standalone_A4/

# PDFs (De + En zusammen)
cp $BASE/wr_standalone_A4/A*_De.pdf A_Serie_Export/pdf/
cp $BASE/wr_standalone_A4/A*_En.pdf A_Serie_Export/pdf/

# Prüfskripte
cp $BASE/python/A_Serie_Skripte/*.py A_Serie_Export/python/A_Serie_Skripte/

# Dokumentation
cp $BASE/README.md    A_Serie_Export/
cp $BASE/CHANGELOG.md A_Serie_Export/

# ZIP (direkt schreiben, nie cp auf bestehende Datei!)
DATUM=$(date +%Y-%m-%d)
rm -f /mnt/user-data/outputs/A_Serie_Komplett_${DATUM}.zip
zip -qr /mnt/user-data/outputs/A_Serie_Komplett_${DATUM}.zip A_Serie_Export/

echo "Fertig: $(unzip -l /mnt/user-data/outputs/A_Serie_Komplett_${DATUM}.zip | tail -1 | awk '{print $2}') Einträge"
```

**Wichtig:** ZIP immer direkt nach `/mnt/user-data/outputs/` schreiben, nie über `cp` auf eine bestehende Datei — sonst wird der ZIP angehängt statt ersetzt.

---

## 6. Häufige Fehler und Lösungen

| Problem | Ursache | Lösung |
|---------|---------|--------|
| TOC fehlt / falsch | Nur 1 LaTeX-Lauf | Mindestens 3 Läufe, `.toc` vorher löschen |
| `Missing $` im En-PDF | Mathematik in `\section{}` ohne `\texorpdfstring` | `\section{\texorpdfstring{$x$}{x}}` |
| ZIP hat doppelte Einträge | `cp` auf bestehende ZIP-Datei | ZIP löschen, dann neu erstellen |
| En-Wrapper-Titel Deutsch | Wrapper-Skript hatte Fehler | Wrapper-Datei manuell prüfen, `\title{}` korrigieren |
| `! File ended while scanning \title` | Titel enthält `\` ohne Escaping | Titel vereinfachen, keine Zeilenumbrüche in `\title{}` |
| `lualatex` Timeout | Zu viele Docs auf einmal | In 3 Blöcken kompilieren (Block 0, Block 1, Block 2+3) |

---

## 7. Schicht-Entscheide (Referenz)

| War | Jetzt | Bedingung |
|-----|-------|-----------|
| [S] | [B] | Algebraischer Beweis vorhanden |
| [S] | [K] | Numerische Verifikation + Ableitung aus ξ |
| [B] | [K] | Zusätzlich direkt aus ξ hergeleitet |
| offen | deklariert | Entscheid: nicht beweisbar / nicht gefordert |

Wenn ein Punkt von [S] auf [B] oder höher angehoben wird:
1. Markierung im betreffenden Dokument ändern
2. In A230 unter "Geschlossene Punkte" vermerken
3. CHANGELOG.md aktualisieren

---

*Erstellt 2026-07-22. KI-gestützt; Verantwortung beim Autor.*
