# Release Notes — v1.4.6 (10. Oktober 2026)

**DOI:** wird bei der Zenodo-Veröffentlichung vergeben — ersetzt v1.4.5
Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Änderungsprotokoll: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**
Kurzfassung des Korpus: **[2/pdf/384_FFGFT_Kurzfassung_De.pdf](2/pdf/384_FFGFT_Kurzfassung_De.pdf)** (auch als [HTML](2/html/384_FFGFT_Kurzfassung_De.html))

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** ist in erster Linie eine
verhältnisbasierte Theorie. In natürlichen Einheiten (Heaviside-Lorentz, ħ = c = ε₀ = 1)
mit α = 1 gibt es einen einzigen dimensionslosen Parameter **ξ = 4/30000** auf einem
kompakten 4D-Torus T⁴/ℤ₃; die Grundrelation lautet **T̃·m = 1** — intrinsische Zeit und
Masse sind invers gekoppelt. Erst die Übersetzung in SI braucht einen Messwert als Anker.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

v1.4.6 archiviert die Auswertung, die der Revision des Artikels „Galois-Informed HRV
Preprocessing" (Smart Wearable Technology, Einreichung #12080) zugrunde liegt. Das
revidierte Manuskript zitiert diese Version als zitierbare Quelle seiner Skripte und
Ergebnisse. Die Theorie selbst ist unverändert; ξ und T̃·m = 1 bleiben, und es kommt
kein Korpusdokument hinzu.

---

## Revisionsskripte zum SWT-Artikel

Der neue Ordner `2/python/Dok360_Skripte/SWT_Revision/` enthält das Prüfskript
`pruef_swt_revision.py`, das jede im revidierten Manuskript verwendete Zahl aus den
Rohdaten in `2/python/Dok360_Skripte/` nachrechnet (24/24 Assertions), das
Abbildungsskript `swt_revision_figures.py`, die Ergebnisdatei
`pruef_swt_revision_ergebnis.json`, die drei Abbildungen und eine README. Die Skripte
brauchen numpy, scipy und neurokit2 und werden aus diesem Ordner aufgerufen.

Geprüft werden das Nullmodell für Gitternähe (wie oft ein beliebiger Wert zufällig nahe
an einem Gitterelement liegt), die Einheitenabhängigkeit der HRV-Bandgrenzen, die
korrigierte Auflösungsbedingung Δf/f ≤ 100ξ mit der daraus folgenden Mindest-Fensterlänge,
die Neuauswertung der Polar-H10-Aufnahmen, die Test-Retest- und Gleitfenster-Streuung
von LF/HF sowie die Fallzahl des im Artikel vorgeschlagenen prospektiven Tests.

## Neuauswertung der Polar-H10-Aufnahmen

Der R-Zacken-Detektor in `polar_h10_atemfrequenz_scan.py` hat in jeder Aufnahme mit
Atemvorgabe vom 10. September 2026 35–47 % der Herzschläge verpasst. Weil die
verbleibenden RR-Intervalle danach aneinandergehängt wurden, schrumpfte die Zeitachse
auf 49–61 % der echten Aufnahmedauer, und alle Spektralfrequenzen wurden um den Faktor
1,6–2,0 nach oben verschoben. Mit einem validierten Detektor (NeuroKit2) und erhaltener
Zeitachse liegt der dominante Spektralpeak bei 4, 5 und 6 Atemzügen/min innerhalb einer
Frequenzstufe bei der Metronomfrequenz, und der HF-Peak ist deren zweite Harmonische.
Die früher berichteten Galois-Treffer (88/35, 39/35) sind hinfällig; LF/HF-Werte nahe
an Gitterelementen treten nur so oft auf, wie das Nullmodell für Zufall vorhersagt. In
der Spontanaufnahme hatte ein einzelner verpasster Schlag RMSSD von 19,0 ms auf 36,3 ms
angehoben. Die Dateien `PolarH10_4min_A1_ECG.jsonl` und `PolarH10_4min_A2_ECG.jsonl`
sind byte-identisch, es gibt also nur eine Aufnahme mit 4 Atemzügen/min.

Das Originalskript und die Ergebnisdateien vom September bleiben zur
Nachvollziehbarkeit unverändert; ihre Polar-Zahlen sind durch die Werte in
`SWT_Revision/pruef_swt_revision_ergebnis.json` ersetzt. Die Polar-Ergebnisse in
Dok. 360 sind auf dieselbe Weise betroffen und werden im Dokument korrigiert und in
Dok. 190 gebucht.

## Was sich nicht geändert hat

ξ und T̃·m = 1 sind unverändert. Alle Ergebnisse von v1.4.5 gelten weiter; die
Neuauswertung betrifft nur die gemessenen HRV-Daten von Dok. 360, nicht die Theorie.
