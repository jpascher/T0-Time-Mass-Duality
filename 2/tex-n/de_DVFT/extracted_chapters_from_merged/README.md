# Extrahierte Kapitel aus Merged-Versionen

Dieses Verzeichnis enthält einzelne Kapitel-Dateien, die aus den zusammengeführten DVFT-Dateien extrahiert wurden.

## Herkunft

Die Kapitel wurden automatisch aus folgenden Merged-Dateien extrahiert:
- `202_12-15_De.tex` (Kapitel 12-15)
- `202_16-19_De.tex` (Kapitel 16, 18-19)
- `202_20-32_De.tex` (Kapitel 20-32)
- `202_33-43_De.tex` (Kapitel 33-43)

## Inhalt

Insgesamt 31 Kapitel wurden extrahiert:

### Kosmologie und Frühe Universums (12-15)
- **Kapitel 12:** Kosmologie, Big Bang und Geburt des Universums
- **Kapitel 13:** Chronologie der Universumsschöpfung
- **Kapitel 14:** Raum-Schöpfungsgeschwindigkeit und kosmische Grenze
- **Kapitel 15:** Merkur-Perihel-Präzession

### Gravitationsphänomene (16, 18-19)
- **Kapitel 16:** Ableitung der Hubble-Spannung
- **Kapitel 18:** Ableitung der Schrödinger-Gleichung
- **Kapitel 19:** Heisenbergsche Unschärferelation

### Quantentheorie und Teilchenphysik (20-32)
- **Kapitel 20:** Lösung des Yang-Mills-Massenlücken-Problems
- **Kapitel 21:** Ron Folmans T-cube-Quantengravitationsexperiment
- **Kapitel 22:** Maximale Masse für Quantenüberlagerung
- **Kapitel 23:** Neutronenlebensdauer-Diskrepanz gelöst
- **Kapitel 24:** Koide-Massenformel für Leptonen
- **Kapitel 25:** Neutrinomassen-Problem gelöst
- **Kapitel 26:** Lösung der Baryonischen Asymmetrie
- **Kapitel 27:** Teilchen-Massenhierarchie und Gravitationsschwäche
- **Kapitel 28:** Warum Newtons Gesetz nicht für Quantenteilchen gilt
- **Kapitel 29:** Delayed-Choice-Quantum-Eraser-Experiment
- **Kapitel 30:** Warum Quantenprozesse im Gehirn machbar sind
- **Kapitel 31:** Photoelektrischer Effekt und Laserphysik
- **Kapitel 32:** Reaktor-Antineutrino-Anomalie

### Fortgeschrittene Themen (33-43)
- **Kapitel 33:** Ableitung des Pauli'schen Ausschlussprinzips
- **Kapitel 34:** Lösung des Strong-CP-Problems
- **Kapitel 35:** Erklärung quantenmechanischer Phänomene
- **Kapitel 36:** Warum QFT nie eine Gravitationstheorie wurde
- **Kapitel 37:** Intrinsische Eigenschaften des Vakuumfeldes
- **Kapitel 38:** Schwarze Löcher und Quantensingularitäten
- **Kapitel 39:** Entropie
- **Kapitel 40:** Glaubwürdige Alternative zu GR und QFT
- **Kapitel 41:** Intrinsische Eigenschaften des Vakuumfeldes
- **Kapitel 42:** Planck-Einheiten und universelle Konstanten
- **Kapitel 43:** Fundamentale Axiome und Konstanten

## Dateiformat

Jede Datei ist ein eigenständiges LaTeX-Dokument:
- Vollständige Präambel mit allen notwendigen Paketen
- Titel spezifisch für das Kapitel
- Kapitelnummer und -titel im Dateinamen: `kapitel_XX_merged.tex`
- Kann einzeln kompiliert werden

## Unterschied zu anderen Versionen

Es gibt drei verschiedene Versionen der Kapitel im Repository:

1. **Einzelne Kapitel (tex_DVFT_T0/):**
   - Technisch, detaillierte mathematische Ableitungen
   - 5-22 Gleichungen pro Kapitel
   - Für akademisches Publikum

2. **Merged Kapitel (202_XX-YY_De.tex):**
   - Narrative Zusammenfassungen
   - 0-3 Gleichungen pro Kapitel
   - Für allgemeines Verständnis
   - Diese Dateien sind die Quelle für die extrahierten Kapitel

3. **Extrahierte Kapitel (extracted_chapters_from_merged/):**
   - Eigenständige Dateien aus den Merged-Versionen
   - Gleicher Inhalt wie Merged-Versionen, aber als separate Dateien
   - **Dieses Verzeichnis**

## Verwendung

Um ein einzelnes Kapitel zu kompilieren:

```bash
cd extracted_chapters_from_merged
pdflatex kapitel_20_merged.tex
```

## Erstellung

Die Kapitel wurden automatisch mit dem Skript `extract_chapters_from_merged.py` erstellt:

```bash
python3 ../../../extract_chapters_from_merged.py
```

## Hinweise

- Die extrahierten Kapitel sind **narrative Versionen** mit konzeptuellem Fokus
- Für detaillierte mathematische Ableitungen siehe `tex_DVFT_T0/`
- Alle Versionen sind theoretisch konsistent mit T0-Fundamenten
- Fehlende Kapitelnummern (z.B. 17, 44) waren nicht in den Merged-Dateien vorhanden

## Datum

Erstellt: 29. Dezember 2025
