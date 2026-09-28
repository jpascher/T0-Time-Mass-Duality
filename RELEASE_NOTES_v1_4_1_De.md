# Release Notes — v1.4.1 (28. September 2026)

**DOI:** wird bei der Zenodo-Veröffentlichung vergeben — ersetzt v1.4.0 (https://doi.org/10.5281/zenodo.22790191)
Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Änderungsprotokoll: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** zeigt: Alle Konstanten des
Standardmodells folgen aus einem einzigen dimensionslosen Parameter **ξ = 4/30000**
auf einem kompakten 4D-Torus T⁴/ℤ₃. Die Grundrelation lautet **T̃·m = 1** — intrinsische
Zeit und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Diese Version fasst die Arbeit vom 18. bis 28. September 2026 zusammen: dreizehn neue
Dokumente (Dok. 366–378), drei neue populärwissenschaftliche Bücher und sieben
Registereinträge (R121–R127). Schwerpunkte sind die Leptonmassen über das Ikosaeder
(Koide-Phase θ = 2/9 als Matrixelement), das elektroschwache Bosonspektrum aus v
(Weinberg-Winkel 2/9, Spurregel für die Higgs-Masse) und die Brücken zu anderen Rahmen,
insbesondere Observer Patch Holography (OPH). Grundrelation und ξ sind unverändert;
Korrekturen an älteren Dokumenten sind in Dok. 190 geführt (Abschnitt „Korrekturen").

---

## Neue Bücher

### *Die Zahl, die niemand erklärte / The Number That Nobody Explained*
*(Ikosaeder-Buch, De/En, 75/73 S., 6×9 Zoll, Prolog, 8 Kapitel, Anhang)*

**Quellen:** https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/kdp/IKO_Ikosaeder_Leptonmassen/

Populärwissenschaftliche Erzählung der Befunde aus Dok. 285, 293, 338, 352, 364 und
367–370: warum die Koide-Formel mit θ = 2/9 funktioniert, wie Drei (ℤ₃) und Fünf (φ)
im Ikosaeder zusammenkommen und wo die offene Kante liegt. Kein neues FFGFT-Ergebnis.

### *Felder in der FFGFT / Fields in FFGFT*
*(Buchausgabe von Dok. 366, De/En, je 38 S., 6×9 Zoll)*

**Quellen:** https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/kdp/366_Feldstruktur_FFGFT/

Energie, Fluss und Geometrie am Beispiel der Goubau-Leitung; Poynting- und Ohm-Sicht
als reziproke Projektionen, analog zur Zeit-Masse-Dualität.

### *Dunkle Materie — eine Illusion / Dark Matter — an Illusion*
*(De/En, 20/18 S., 6×9 Zoll, 10 Kapitel)*

**Quellen:** `2/Sources/wr_narrativ/FFGFT_Dunkle_Materie_De/En.tex`, PDFs unter `2/Sources/wr_narrativ/pdf/`

Rotationskurven aus T̃·m = 1 im Trägheitsregime (a ≪ a₀) ohne dunkle Materie als
Substanz; Bullet Cluster und Gravitationslinsen kritisch eingeordnet, ausdrücklich
kein schließender Beweis.

---

## Neue Dokumente (Dok. 366–378)

| Dok. | Titel | Seiten De/En | Prüfskript |
|------|-------|--------------|------------|
| 366 | Felder in der FFGFT: Energie, Fluss und Geometrie | 26/25 | 14/14 |
| 367 | Warum θ = p₀ = 2/9 — Wahrscheinlichkeit und Phase als zwei Lesarten eines Quotienten | 9/9 | 18/18 |
| 368 | Von p₀, p₁, p₂ zu Leptonmassen — φ-Skelett und Galois-Korrekturfaktoren | 8/8 | 18/18 |
| 369 | Vier Wege zu den Leptonmassen — Bestandsaufnahme | 9/9 | 25/25 |
| 370 | Warum das Ikosaeder — Drei, Fünf und das Nicht-Kommutieren | 10/9 | — (Erklärungsdokument) |
| 371 | Der Faktor 4/3 — Kugelvolumen, Casimir-Operatoren, elektromagnetische Masse, (3,4,5) | 12/12 | 28/28 |
| 372 | Das Matrixelement-Prinzip und seine Reichweite | 12/12 | 45/45 |
| 373 | Der Yukawa-Mechanismus als Konsequenz von T̃·m = 1 | 11/11 | 35/35 |
| 374 | Gemeinsamer Anker — Brückengleichungen zu OPH | 9/8 | 30/30 |
| 375 | Die Hierarchie v/E_P — FFGFT und OPH im Vergleich | 6/6 | 11/11 |
| 376 | Der Koeffizient 8π und der Status von Issue 740 | 6/6 | 9/9 |
| 377 | Schnittstellen der FFGFT zu anderen Rahmen | 6/6 | 20/20 |
| 378 | Begutachtung unter heutigen Bedingungen | 12/12 | 25/25 |

Prüfskripte unter `2/python/DokNNN_Skripte/`.

---

## Wichtige neue Ergebnisse

### Koide-Phase als ℤ₃-Quotient [B]/[K] (Dok. 367, 370)
Der Koide-Winkel θ und die ikosaedrische Übergangswahrscheinlichkeit
p₀ = |⟨v₀|R₅ vₑ⟩|² sind derselbe Quotient 2/3² = (nicht-triviale ℤ₃-Moden)/(ℤ₃-Ordnung)².
Der Zusammenhang θ = |A|² hat die Struktur der Born-Regel. Die vollständige Matrix
|⟨v_j|R₅|v_k⟩|² ist doppelt stochastisch; die Zeile der symmetrischen Mode lautet
(5, 2, 2)/9, Spur R₅ = φ. Das Ikosaeder wirkt auf dem ausgerollten ℝ³, nicht auf dem
kompakten T⁴ (5 ∤ 1152); die Fünf tritt als Phase ζ₅ ∈ GF(81) ein.

### φ-Skelett der Leptonmassen [B] (Dok. 368)
Neue exakte Identitäten: p₁/p₂ = φ⁸, p₀/p₂ = 2φ⁴, p₁/p₀ = φ⁴/2.
Näherungen m_τ/m_e ≈ 74·φ⁸ (0,03 %) und m_μ/m_e ≈ 30·φ⁴ (0,56 %) [K] — erste Verbindung
zwischen Dok. 293 und Dok. 338.

### Vier Wege zu den Leptonmassen (Dok. 369)
T0-Leiter, Koide mit θ = 2/9, Galois GF(3ⁿ) und φ-Skelett im direkten Vergleich gegen
PDG 2024. Zwei Genauigkeitsklassen: Prozent und 10⁻³ %. FFGFT sagt die Form des Spektrums
parameterfrei voraus (dimensionslose Verhältnisse); für absolute Werte in MeV braucht sie
einen deklarierten Anker. Zweite Lesart der fraktalen Korrektur ohne QED (R121).

### Matrixelement-Prinzip [B]/[K] (Dok. 372)
A₅ erzeugt in der ℤ₃-Modenbasis genau acht Matrixelement-Betragsquadrate, alle mit
Nenner 9. Daraus: on-shell-Weinberg-Winkel 1 − M_W²/M_Z² = 2/9, Vorhersage
M_W = M_Z·√(7/9) = 80,420 GeV [K]; atmosphärische Mischung sin²θ₂₃ ∈ {4/9, 5/9},
maximale Mischung ausgeschlossen [K]. Negativbefunde ausgewiesen: θ₁₂, θ₁₃ und α_s
liegen nicht in der Achtermenge [X].

### Yukawa-Mechanismus und Spurregel [B]/[K] (Dok. 373)
y_i = m_i/v folgt aus T̃·m = 1 unter der Fluktuation v → v + h(x) für alle Fermionen
zugleich [B]. Das Higgs-Teilchen ist das Schwingungsquant der Gitterskala.
Spurregel M_W² + M_Z² + m_h² = v²/2 auf 0,45 % [K]; mit 2/9 und 11/8 folgt
M_Z²/v² = 288/2113 und damit das elektroschwache Bosonspektrum allein aus v auf
Baumgraphen-Niveau (0,17–0,31 %). Galois-Kette M_Z : m_h : m_t = 1 : 11/8 : (11/8)² [K].
Bestandsaufnahme des Teilchenzoos (Stand 21. September 2026).

### Faktor 4/3 [B]/[E] (Dok. 371)
Der Faktor 4/3 der elektromagnetischen Elektronenmasse (Abraham/Lorentz) ist ein
Dreidimensionalitäts-Effekt, 4/3 = 2·(1 − 1/3). C₂(SU(2)) = 3/4 und C₂(SU(3)) = 4/3
sind Kehrwerte; N = 2 ist der einzige Fall mit C₂(N)·C₂(N+1) = 1 [B].

### Brücke zu Observer Patch Holography [B]/[K] (Dok. 374–376)
Brückengleichungen B1–B4: Zellenenergie = Bitenergie E_bit = ħc/L, Kollapsschwelle an
der Zellkante, Zellentakt T̃ = √P·t_P, L_cell/L₀ = √P/ξ ≈ 9578. Eigene FFGFT-Kette
ξ → G → ℓ_P → E_P: v/E_P = 2,0389·10⁻¹⁷ (+1,10 %, vollständig dem bare-Rest der
Leptonleiter zugeordnet). Der Koeffizient 8π ist auf OPH-Seite abgeleitet; die Aussage,
Issue 740 sei geschlossen, ist zurückgenommen (R124).

### Schnittstellen-Übersicht (Dok. 377)
Elf Rahmen mit Vergleichs- und Brückendokumenten, sieben überschneidende Größen mit
Rechenweg. Nur α⁻¹ und v/E_P werden von mehr als einem Rahmen beziffert; der
Hadronsektor kommt in keinem Vergleich vor.

### Begutachtung unter heutigen Bedingungen (Dok. 378)
Methodische Bestandsaufnahme: was FFGFT-Buchführung (Statusmarker, Dok. 190,
Prüfskripte, Negativbefunde), IPI-Audit-Praxis und Dot-Theory-Governance für ein
Begutachtungs-Regelwerk bereits liefern; zehn Bausteine und gestufte Prüftiefe.
Keine physikalischen Aussagen.

---

## Korrekturen (Dok. 190, R121–R127)

| Eintrag | Betrifft | Inhalt |
|---------|----------|--------|
| R121 | Dok. 352 §10, 369 | Herkunft der ε_i: zweite Lesart ohne QED-Brücke; R113-Brücke nur noch in Lesart A nötig |
| R122 | Dok. 041, 005; 372, 373 | Higgs-Masse und Λ_QCD in Dok. 041/005 nicht haltbar [X]; Kandidaten über Galois-Kette und Spurregel (Dok. 373) |
| R123 | Dok. 160 | Namenskonflikt K_frak: in Dok. 160 als hadronischer Faktor K_had zu lesen |
| R124 | Dok. 374 | Rücknahme der Issue-740-Aussage; Dok. 374 direkt korrigiert |
| R125 | Dok. 085, 176, 179, 186 | Literaturangaben und eine Standardaussage in den Photonik-Dokumenten |
| R126 | Dok. 230 | Zylinderdarstellung des Qubits: Literaturverortung, Begründung der Born-Statistik |
| R127 | Dok. 043, 044, 261 | α = 1 ist keine Einheitenwahl [X]; α wird dimensionslos aus ξ hergeleitet |

---

## Offene Brücken (Stand R127)

| Brücke | Status |
|--------|--------|
| τ_μ direkt aus FFGFT (ohne G_F und v) | [S] (R112, Dok. 351) |
| Warum die rationale Näherung die GF(3ⁿ)-Wicklungszahlen trägt | [S] (Dok. 369 §4, R121) |
| Koide-Amplitude d/c = √2 aus der Geometrie | [S] (Dok. 352 §8) |
| Hadronischer Faktor K_had | [S] (R123) |
| Λ_QCD aus ξ | [X] (R122, Dok. 372) |
| Higgs-Potential V(h) | [S] (Dok. 373) |
| m_Pl und α_em(M_Z) aus ξ | [S] |
| Quark-/Hadron-Sektor | offen (Dok. 318, R76) |
| CMB-Peaks {1,6,14,26}; \|n\|²=30 | offen (P29/P31) |
| Ikosaeder-Phasen (GF(81)) und Galois-Ordnungen (GF(3ⁿ)): gemeinsame Wurzel | [S] (Dok. 370) |

## Einstieg für neue Leser
Dok. 205 „FFGFT in einfacher Sprache" (De/En, 13–14 S.) bleibt der empfohlene
Einstiegspunkt für die Physik. *Quantenmechanik ist deterministisch* bleibt der
empfohlene Einstiegspunkt für die Quantenmechanik- und Quantenrechner-Perspektive.
Das Ikosaeder-Buch *Die Zahl, die niemand erklärte* ist der empfohlene Einstieg in
die Leptonmassen.

## Was sich nicht geändert hat
ξ und T̃·m = 1 sind unverändert. Alle Ergebnisse aus v1.4.0 gelten weiter, soweit sie
nicht durch R121–R127 präzisiert oder korrigiert sind.
Alle Herleitungsketten aus v1.3.6 sind unverändert.
