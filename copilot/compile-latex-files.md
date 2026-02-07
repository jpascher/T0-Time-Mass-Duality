# FINAL TASK: Refactor all standalone T0 documents with backups, new directories, and strict content rules

## 0. Ausgangspunkt: immer sauberer `origin/main`

1. Im Repository-Root (dort, wo `.git` liegt) ausführen:
   ```bash
   git fetch origin
   git reset --hard origin/main
   ```
2. Alle folgenden Pfadangaben sind relativ zu diesem Root.

---

## 1. Verzeichnisstruktur

### 1.1. BACKUP-Verzeichnisse (nur lesen, NIEMALS ändern)

Erzeuge, falls nicht vorhanden:

- `2/tex-n/de_standalone_orig/`      – Backups aller ursprünglichen DE-Standalones  
- `2/tex-n/en_standalone_orig/`      – Backups aller ursprünglichen EN-Standalones  
- `2/tex-n/de_chapters_orig/`        – Backups aller ursprünglichen DE-Chapters (`de_chapters_new`)  
- `2/tex-n/en_chapters_orig/`        – Backups aller ursprünglichen EN-Chapters (`en_chapters_new`)

Regel: Diese `_orig`-Verzeichnisse sind Archiv; Dateien dort werden nach dem Kopieren **nie mehr verändert**.

### 1.2. NEUE überarbeitete Dokumente mit Preambel

Erzeuge zusätzlich:

- `2/tex-n/de_standalone_new/`       – neue, bereinigte DE-Standalones  
- `2/tex-n/en_standalone_new/`       – neue, bereinigte EN-Standalones  
- `2/tex-n/de_chapters_new_ref/`     – neue, bereinigte DE-Chapters  
- `2/tex-n/en_chapters_new_ref/`     – neue, bereinigte EN-Chapters  

Regel:
- Die **Dateinamen bleiben exakt gleich**, nur das Verzeichnis ändert sich (z.B. `016_T0_Vollstaendige_Berchnungen_De.tex` bleibt so).
- In `_new` / `_new_ref` enthalten die Dateien eine **vollständige Preambel** (aktuelle Standard-Preambel, z.B. `\documentclass[...]` + `\input{T0_preamble_standalone_De}` bzw. En).

---

## 2. Dokumente im Scope

Quellverzeichnisse:

- DE Standalones:  `2/tex-n/de_standalone/*.tex`  
- EN Standalones:  `2/tex-n/en_standalone/*.tex`  
- DE Chapters:     `2/tex-n/de_chapters_new/*.tex`  
- EN Chapters:     `2/tex-n/en_chapters_new/*.tex`

Für **jede** dieser Quelldateien `FILENAME.tex` gilt:

1. Vollständige Kopie ins passende `_orig`-Verzeichnis.  
2. Neues, überarbeitetes Dokument mit **gleichem Namen** in `_new` / `_new_ref` erzeugen.

---

## 3. Kanonische PDF-Liste (zentrale Referenz)

1. Bestimme aus den Standalone-Dateinamen die kanonischen PDF-Namen:
   - Für jedes `2/tex-n/de_standalone/NNN_Base_De.tex` bzw. `...En.tex`:
     - Kanonische PDF: `NNN_Base_De.pdf` bzw. `NNN_Base_En.pdf`
2. Nur diese `NNN_Base_Lang.pdf` sind in **allen** neuen `.tex`-Dateien als interne T0-PDF-Verweise erlaubt.
3. Abweichungen (ohne Prefix, falsches `De/En`, Bindestrich statt Unterstrich etc.) müssen:
   - Auf einen dieser kanonischen Namen gemappt werden (wenn eindeutig zuordenbar), oder
   - entfernt / auskommentiert werden, falls kein Standalone dazu existiert.

---

## 4. KONZEPT-PHASE pro Dokument (Pflicht vor Inhaltstransfer)

Für **jedes** ursprüngliche Standalone (und analog sein Chapter):

1. Erstelle vor der eigentlichen Überarbeitung eine kurze **Konzept-Notiz** (z.B. als Kommentar oder externe Notiz, Format optional), die mindestens enthält:
   - **Kerninhalt** des Dokuments:
     - Welche zentrale Idee / Gleichung / Ableitung MUSS erhalten bleiben?
   - **Zu verschiebende Themen**:
     - g‑2‑Inhalte → sollen in Dokument 018 konzentriert werden.
     - Rotverschiebungs‑/cosmology‑Inhalte → sollen in Dokument 026 konzentriert werden.
   - **Doppelte Inhalte**:
     - Welche Abschnitte sind in anderen Dokumenten bereits in fast identischer Form vorhanden und können hier durch kurze Verweise ersetzt werden?
   - **Einzigartige Perspektiven**:
     - Welche Perspektive dieses Dokuments ist wirklich neu (z.B. andere Darstellung, andere Motivation) und muss daher erhalten bleiben?

2. Diese Konzept-Notiz dient als Referenz beim Erzeugen der neuen Version:
   - Nur Kerninhalte + einzigartige Perspektiven bleiben vollständig.
   - Doppelungen und ausgelagerte Themen werden entsprechend gekürzt oder entfernt.

---

## 5. Transformation pro Standalone

Für jede DE-Standalone-Quelle `2/tex-n/de_standalone/NNN_Name_De.tex`:

### 5.1. Backup

- Kopiere das Original unverändert:
  - `2/tex-n/de_standalone/NNN_Name_De.tex → 2/tex-n/de_standalone_orig/NNN_Name_De.tex`

### 5.2. Neues Dokument mit Preambel

- Erzeuge `2/tex-n/de_standalone_new/NNN_Name_De.tex` mit:
  1. Vollständiger, aktueller DE-Standalone-Preambel (z.B. `\documentclass[12pt,a4paper]{report}` + `\input{T0_preamble_standalone_De}`).
  2. Übernommenem Inhaltskörper aus dem Original, aber **bereinigt nach folgenden Regeln**:

#### 5.2.1. Struktur und Mathematik erhalten

- Beibehalten:
  - `\chapter`, `\section`, `\subsection`, `\subsubsection`, Labels, Referenzen.
  - Alle mathematischen Formeln und Umgebungen: `equation`, `align`, `gather`, `multline`, `\[...\]`, `$...$`, Tabellen, Figuren.
- Nicht ändern:
  - Labels, Gleichungsnummern, Kapitel- und Abschnittsstruktur (nur Inhalt darin bereinigen).

#### 5.2.2. Keine Zusammenfassungen, Ausblicke, Versuchs-/Experimentvorschläge

- Entfernen/auskommentieren:
  - Sektionen/Abschnitte mit Titeln wie:
    - DE: `Zusammenfassung`, `Schlussfolgerung`, `Ausblick`, `Zukünftige Arbeiten`, `Experiment`, `Experimente`, `Messung(en)`, `Vorhersagen` etc.
    - EN: `Summary`, `Conclusion(s)`, `Outlook`, `Future Work`, `Experiments`, `Tests`, `Predictions` etc.
  - Narrative Absätze, die nur:
    - Zusammenfassen,
    - spekulieren,
    - zukünftige Experimente/Messungen vorschlagen.
- Übrig bleiben soll:
  - Der mathematische/konzeptionelle Kern, ohne „Storytelling“, Spekulation oder Versuchsanleitungen.

#### 5.2.3. g‑2-Inhalte isolieren (nur in Dokument 018)

- Nur Dokument `018_T0_Anomale-g2-10_*` (DE/EN) darf:
  - Vollständige g‑2‑Herleitungen, numerische Resultate, Fits, Vergleich mit Experiment, g‑2‑Plots etc. enthalten.
- In **allen anderen** neuen Standalones / Chapters:
  - g‑2‑Passagen entfernen oder stark kürzen.
  - Maximal ein knapper Verweis wie:
    - DE: “Details zum anomalen magnetischen Moment des Myons siehe Dokument 018.”
    - EN: “For details on the muon g‑2 anomaly see document 018.”

#### 5.2.4. Rotverschiebung isolieren (nur in Dokument 026)

- Nur Dokument `026_T0_Kosmologie_*` (DE/EN) darf:
  - Ausführliche Rotverschiebungs-/Hubble-/Beobachtungs-Kosmologie enthalten.
- In **allen anderen** neuen Standalones / Chapters:
  - Explizite Rotverschiebungs-/redshift-Diskussionen entfernen.
  - Falls nötig: neutrale, kurze Hinweise auf 026, ohne nochmalige Details.

#### 5.2.5. Dopplungen entfernen, unterschiedliche Sichtweisen erhalten

- Wenn die gleiche lange Herleitung/Erklärung nahezu identisch in mehreren Dokumenten erscheint:
  - Nur in einem gewählten „Heimatdokument“ volles Detail lassen.
  - In den anderen Dokumenten: durch kurze Zusammenfassung + Referenz auf das Heimatdokument ersetzen.
- Falls zwei Dokumente dieselbe Sache aus anderer Perspektive erklären (z.B. SI-Einheiten vs. geometrische Sicht):
  - Beide Perspektiven beibehalten (nicht wegkürzen).

#### 5.2.6. PDF-Verweise nur über kanonische Liste

- Alle internen T0-PDF-Verweise (in Text oder Bibliographie) müssen:
  - Auf `NNN_Base_Lang.pdf` aus der kanonischen Liste (Abschnitt 3) vereinheitlicht werden.
- Variationen (ohne Prefix, andere Schreibweisen) entsprechend mappen oder entfernen, falls kein Standalone existiert.

### 5.3. Kompilierung des neuen Standalones

- Vom Repo-Root:
  ```bash
  cd 2/tex-n/de_standalone_new
  lualatex -interaction=nonstopmode NNN_Name_De.tex
  lualatex -interaction=nonstopmode NNN_Name_De.tex
  ```
- Bei Fehlern:
  - In `compile_errors_de_new.txt` (in `de_standalone_new`) einen Eintrag anfügen:
    - `NNN_Name_De.tex: <kurze Fehlermeldung>`

EN-Standalones analog mit:

- Backup: `en_standalone → en_standalone_orig`
- Neu:    `en_standalone_new/NNN_Name_En.tex`
- Preambel: EN-Standalone-Preambel (`T0_preamble_standalone_En`)

---

## 6. Transformation pro Chapter

Für jedes DE-Chapter `2/tex-n/de_chapters_new/NNN_Name_De_ch.tex`:

1. **Backup**:
   - `2/tex-n/de_chapters_new/NNN_Name_De_ch.tex → 2/tex-n/de_chapters_orig/NNN_Name_De_ch.tex`
2. **Neues Chapter**:
   - Erzeuge `2/tex-n/de_chapters_new_ref/NNN_Name_De_ch.tex`:
     - Mit passender Chapter-Preambel (gemäß aktuellem System).
     - Inhaltskörper wie beim zugehörigen Standalone bereinigen:
       - Keine Zusammenfassung/Ausblick/Versuchsvorschläge,
       - g‑2 nur in 018, Rotverschiebung nur in 026,
       - Dopplungen vermeiden, Perspektiven erhalten,
       - PDF-Verweise über kanonische Liste.
3. **Kompilieren**:
   ```bash
   cd 2/tex-n/de_chapters_new_ref
   lualatex -interaction=nonstopmode NNN_Name_De_ch.tex
   lualatex -interaction=nonstopmode NNN_Name_De_ch.tex
   ```
   - Fehler in `compile_errors_de_ch_new.txt` eintragen.

EN-Chapters analog mit:

- Backup: `en_chapters_new → en_chapters_orig`
- Neu:    `en_chapters_new_ref/NNN_Name_En_ch.tex`

---

## 7. Reihenfolge und Rekursion

Für jedes Dokumenten-Paar (Standalone + Chapter):

1. Konzept-Notiz erstellen (Kerninhalt, zu verschiebende Themen, Dopplungen, Perspektiven).  
2. Backup in `_orig` anlegen.  
3. Neue Standalone-Version in `_new` erzeugen (mit Preambel, nach allen inhaltlichen Regeln).  
4. Neue Standalone-Version 2× kompilieren, Fehler loggen.  
5. Neues Chapter in `_new_ref` erzeugen (analog bereinigt).  
6. Neues Chapter 2× kompilieren, Fehler loggen.  
7. Nächstes Dokumenten-Paar.

Am Ende:

- `_orig` enthält unveränderte Originalquellen.  
- `_new` / `_new_ref` enthalten bereinigte, aktuelle Versionen mit einheitlicher Preambel.  
- `compile_errors_de_new.txt`, `compile_errors_en_new.txt`, `compile_errors_de_ch_new.txt`, `compile_errors_en_ch_new.txt` listen alle nicht erfolgreich kompilierten Dateien mit Kurzfehlern.

---

## 8. Wichtige Einschränkungen

- Keine Dateinamen ändern, nur Verzeichnisse (`*_orig`, `*_new`, `*_new_ref`).  
- Keine neuen Dokumente erfinden, nur vorhandene transformieren.  
- Labels, Gleichungsnummern, zentrale mathematische Inhalte müssen erhalten bleiben.  
- Änderungen nur gemäß der oben genannten Regeln (Entfernen von Zusammenfassungen/Ausblicken/Tests, Isolierung von g‑2 und Rotverschiebung, Entdoppelung, Vereinheitlichung der PDF-Verweise).
