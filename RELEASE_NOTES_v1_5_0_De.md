# Release Notes — v1.5.0 (26. November 2026)

**DOI:** wird bei der Zenodo-Veröffentlichung vergeben — ersetzt v1.4.6 (v1.4.7 bis v1.4.9 wurden nur auf GitHub angelegt; ihre Archivierung auf Zenodo ist gescheitert, der Inhalt ist derselbe)
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

v1.5.0 führt formale Beweise in den Korpus ein. Die algebraischen Kerne von Dok. 339,
340, 342 und 343 sind jetzt zusätzlich im Beweisassistenten Lean 4 bewiesen; der
Lean-Prüfkern hat jeden Schritt nachvollzogen, und eine GitHub-Action prüft die Beweise
bei jeder Änderung neu. Dafür gibt es den neuen Statusmarker **[L]**. Die formale
Prüfung hat zugleich eine Präzisierung zur Majorana-Zuordnung ergeben, die in Dok. 340,
343, 346 und im Korrekturregister (R164) eingearbeitet ist. ξ und T̃·m = 1 sind
unverändert, es kommt kein neues Korpusdokument hinzu. Für die übrigen Änderungen seit
v1.4.6 gelten das Änderungsprotokoll und Dok. 190.

---

## Formale Beweise in Lean 4

Der neue Ordner `2/lean/` enthält das Lean-Projekt `Dok339_Pilot` mit drei Modulen. Es
kommt ohne die Bibliothek Mathlib aus: Der Körper GF(27) wird als GF(3)[x]/(x³+2x+1)
selbst aufgebaut, und alle Aussagen über endliche Strukturen werden im Prüfkern
vollständig durchgerechnet. Die Action `.github/workflows/lean.yml` baut das Projekt bei
jedem Push, der `2/lean/` betrifft; ein grüner Lauf bedeutet, dass alle Sätze bewiesen
sind. Lokal ist nichts zu installieren. Die README in `2/lean/` beschreibt die Module im
Einzelnen.

Das Modul `GF27.lean` sichert Dok. 339: Das Modell ist ein Körper mit 27 Elementen,
GF(27)* ist zyklisch der Ordnung 26, unter dem Frobenius x ↦ x³ bleiben genau +1 und −1
fest, und die übrigen 24 Einheiten zerfallen in genau acht Dreier-Orbits. Damit ist auch
die Zyklizität bewiesen, die das Python-Prüfskript von Dok. 339 nur voraussetzt.

Das Modul `Dok342.lean` sichert Satz A von Dok. 342 und Satz E von Dok. 343. Es gibt
über GF(3) genau acht irreduzible Kubiken, und es sind genau die Polynome der Tabelle in
Dok. 342; f₁–f₄ sind die angegebenen Frobenius-Klassen mit Wurzeln der Ordnung 26,
g₁–g₄ ihre Vorzeichenpartner mit Ordnung 13. Für die Eintrittsregel ist bewiesen, dass
13, 5, 11 und 7 die einzigen Primzahlen mit ord_p(3) = 3, 4, 5 bzw. 6 sind, für alle
natürlichen Zahlen und ohne obere Schranke.

Das Modul `Dok340.lean` sichert die Orbit-Algebra von Dok. 340 (Summen, Produkte,
Orbit₄ = 2⁻¹·Orbit₁, Inversen-Tabelle) und klärt die Rolle des Erzeugers in Satz D‴ von
Dok. 343.

## Neuer Statusmarker [L]

Die verbindliche Legende `2/Sources/ch/000_Statusmarker_Legende_De/En_ch.tex` hat eine
neue Zeile: [L] bedeutet, dass eine [B]-Aussage zusätzlich in Lean 4 formal bewiesen ist.
Der Marker betrifft nur die mathematische Aussage, nicht ihre physikalische Zuordnung.
Das Korpus-Prüfskript `pruef_statusmarker.py` und das Abgleichskript für Dok. 190 kennen
den Marker; beide melden 0 Befunde. Die Dokumente 339, 340, 342 und 343 tragen [L] an den
bewiesenen Stellen und einen Vermerk „Formale Prüfung" mit Verweis auf das jeweilige
Modul. Die übrigen Dokumente, die die Legende einbinden, zeigen die neue Zeile, sobald
ihr PDF das nächste Mal erzeugt wird.

## Präzisierung zur Majorana-Zuordnung (R164)

Das Majorana-Kriterium aus Dok. 340 — ein Orbit ist unter k ↦ k⁻¹ (mod 13) in sich
abgeschlossen — arbeitet mit Exponenten und hängt damit vom gewählten Erzeuger von
GF(27)* ab. Lean zeigt für alle zwölf Erzeuger: Unabhängig vom Erzeuger ist nur die
Aufteilung der vier primitiven Klassen in die Schichten {f₁, f₂} und {f₃, f₄}. Welche
Schicht Majorana heißt, folgt aus der Klasse des Erzeugers; mit einem Erzeuger aus f₃
oder f₄ tauschen die Etiketten. Die Zuordnung im Korpus beruht auf der Konvention aus
Dok. 342, den Erzeuger als Wurzel von f₁ zu wählen; sie ist jetzt als [SETZUNG]
gekennzeichnet. Dok. 343 (Satz D‴) trägt die Präzisierung ausführlich, Dok. 340 und 346
als Vermerk, und R164 in Dok. 190 präzisiert die frühere Formulierung von R108, die die
Majorana-Schicht als kanonisch bezeichnet hatte.

## Stand der Riemann-Vermutung

Am 20. November 2026 wurde ein formaler Lean-4-Beweis der Riemann-Vermutung vorgelegt,
der auch die verallgemeinerte Vermutung für Dirichlet-L-Funktionen umfasst (L. Alpöge);
die Fachbegutachtung läuft noch. Dok. 343 führt die nicht-trivialen Nullstellen von
L(s, χ₀) deshalb nicht mehr als „angenommen", sondern mit Quellenangabe [Q]; das gilt
auch für L(s, χ₁) mod 3. Dok. 316 hat einen Nachtrag: Der Beweis ist arithmetisch und
kommt ohne Torus und ohne ξ aus, was die Einordnung des Dokuments bestätigt; die dort
ausgeschlossenen geometrischen Zugänge bleiben ausgeschlossen.

## Was sich nicht geändert hat

ξ und T̃·m = 1 sind unverändert. Die Rechnungen und Ergebnisse von v1.4.6 gelten weiter;
die Präzisierung zur Majorana-Zuordnung ändert keine Zahl, sondern macht eine bisher
stillschweigende Wahl als Setzung sichtbar.
