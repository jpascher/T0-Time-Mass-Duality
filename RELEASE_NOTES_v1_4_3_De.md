# Release Notes — v1.4.3 (2. Oktober 2026)

**DOI:** wird bei der Zenodo-Veröffentlichung vergeben — ersetzt v1.4.2
Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Änderungsprotokoll: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**
Kurzfassung des Korpus: **[2/pdf/384_FFGFT_Kurzfassung_De.pdf](2/pdf/384_FFGFT_Kurzfassung_De.pdf)** (auch als [HTML](2/html/384_FFGFT_Kurzfassung_De.html))

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** ist in erster Linie eine
verhältnisbasierte Theorie. In natürlichen Einheiten mit α = 1 gibt es einen einzigen
dimensionslosen Parameter **ξ = 4/30000** auf einem kompakten 4D-Torus T⁴/ℤ₃; die
Grundrelation lautet **T̃·m = 1** — intrinsische Zeit und Masse sind invers gekoppelt.
Erst die Übersetzung in SI braucht einen Messwert als Anker.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Diese Version fasst die Arbeit vom 28. September bis 2. Oktober 2026 zusammen. Im
Mittelpunkt steht die **vollständige Nachrechnung des Korpus**: Alle Dokumente bis
Nr. 300 und die A-Serie wurden durchgerechnet, rund 235 Dokumente tragen seitdem
einen Korrekturkasten, jede korrigierte Stelle hat einen datierten Hinweis mit dem
vorherigen Wert (R133, R140, R142). Dazu kommen **zehn neue Dokumente (Dok. 379–388)**,
darunter die **Kurzfassung des gesamten Korpus (Dok. 384)**, die **A-Serie v1.5** mit
dem neuen Dokument **A125 (φ-Skelett)** und zwanzig Registereinträge (R128–R147).

Die Rechenprüfung hat mehrere frühere Ansprüche zurückgenommen; sie sind in Dok. 384
im Abschnitt „Was nicht mehr gilt“ gesammelt. Grundrelation und ξ sind unverändert.

---

## Die Rechenprüfung (R133–R146)

Vom 29. September bis 1. Oktober 2026 wurde der Korpus nachgerechnet. Seit R133
werden die Quelldokumente selbst korrigiert, statt die Korrekturen nur im Register zu
führen. Die wichtigsten Folgen für die Einstufung:

- **α, E₀ und K_frak (R135):** Die Übereinstimmung des SI-Werts von α ist eine
  Eigenschaft des gewählten Ankers, keine unabhängige Vorhersage. Der Wert
  K_frak = 74/75 bleibt bestätigt; zwischen dem von α verlangten Faktor 0,98650 und
  74/75 bleibt ein Rest von 1,7·10⁻⁴.
- **Präzisionstabellen (R138):** Tabellen älterer Dokumente, in denen Vorfaktoren an
  Messwerte angepasst waren, sind keine Belege.
- **Gravitationskonstante (R132, R141):** Rechnungen korrigiert; die Übereinstimmung
  mit CODATA auf 0,003 % entsteht erst mit dem Rest der Ein-Anker-Kette in C_conv und
  ist kein eigener Präzisionsbeleg.
- **Quantenmechanik (R142, R143):** Die Bell-Verletzung bleibt; ein mit heutiger
  Hardware messbarer ξ-Effekt existiert nicht. Unbelegte CHSH-Daten und ein daran
  angepasstes ξ sind entfernt.
- **Kosmos (R136, R137):** Die Casimir-CMB-Verbindung ist eine Identität, kein
  Messbeleg; CMB-Temperatur, Rotverschiebung, H₀ und Λ sind präziser eingestuft.
- **Form von K_frak (R139):** Die Form (additiv 1 − 100ξ oder multiplikativ) ist
  wieder offen; der Ikosaeder-Leak ist mit δ* nicht verträglich.
- **Präzisierungen (R144–R146):** Schwarze Löcher (R93/R94), Selbstadjungiertheit von
  F̂ nur auf dem ℤ₃-invarianten Sektor, Gell-Mann-Nishijima nicht vollständig
  geschlossen (Hyperladung der geladenen Leptonen offen).

---

## Neue Dokumente (Dok. 379–388)

| Dok. | Titel | Seiten De/En | Prüfskript |
|------|-------|--------------|------------|
| 379 | Das akustische Plenum und das Photon — Lien (2026) als Fallstudie | 8/8 | 20/20 |
| 380 | Warum D₄ — Spezifität des Trägers gegen angepasste Vergleichsgitter | 7/7 | 13/13 |
| 381 | Die laufende Rekursion exakt aufsummiert | 7/7 | 14/14 |
| 382 | Myon g−2: Stand 2025 | 8/8 | 21/21 |
| 383 | Massen und Planck-Skala ohne v — eine Kette, ein Anker | 8/8 | 20/20 |
| 384 | FFGFT in Kurzfassung — Grundlagen, Ergebnisse und Status nach der Rechenprüfung | 23/23 | 117/117 |
| 385 | Der Higgs-Vakuum-Weg zu ξ | 8/8 | 17/17 |
| 386 | Wo α steckt — Ladungseinheit, zwei Kugeln und ξ als Fläche | 8/8 | 25/25 |
| 387 | Die Abweichungen im Überblick — Verhältnisse, SI-Übersetzung und Korrekturgrößen | 8/8 | 27/27 |
| 388 | Die CMB-Temperatur in der Grundform — eV-Relation, Verhältnis zur Elektronenmasse und die H₀-Formen | 8/8 | 27/27 |

Prüfskripte unter `2/python/DokNNN_Skripte/`.

---

## Wichtige neue Ergebnisse

### Kurzfassung des Korpus (Dok. 384)
Der ganze Korpus (Dok. 001–387, A-Serie) auf dem Stand nach der Rechenprüfung, von
der Grundform her aufgebaut: zuerst die Verhältnisse in natürlichen Einheiten, dann
die Übersetzung in SI. Der leitende Gedanke ist Resonanz: Teilchen sind Schwingungsmoden,
ξ ist ein Punkt im Eulerschen Tonnetz (1/ξ = 2²·3·5⁴), und die fraktale Korrektur ist das
Komma der Einbettung ins Kontinuum. Für jedes Ergebnis Formel, Zahlenwert, Vergleichswert, Status
und tragende Dokumente; dazu Tabellen der prüfbaren Aussagen, eine Statusbilanz, die
offenen Brücken und ein Abschnitt „Was nicht mehr gilt“. Neu formatiert mit farbigen
Statusmarkern und Kästen für die Kernformeln; zusätzlich als eigenständige HTML-Seite.
Empfohlener Einstieg in den heutigen Stand.

### φ-Skelett der Leptonmassen [B]/[K] (Dok. 384, A125)
Die Gewichte der ikosaedrischen Fünffach-Drehung stehen exakt wie p₁/p₂ = φ⁸ und
p₀/p₂ = 2φ⁴ [B]. Damit trifft **m_τ/m_e = (74 + 1/45)·φ⁸ = 3477,469** den Messwert
3477,37 ± 0,18 auf 3·10⁻⁵ (0,6σ) [K] — so genau wie die Koide-Formel, als reines
Verhältnis ohne Anker. Die Faktoren 74 und 1/45 sind beobachtet, nicht hergeleitet
[S]; die 37 in 74 kommt nachweislich nicht aus dem Ikosaeder. Für m_μ/m_e gibt es
keinen φ-Weg auf diesem Niveau.

### Die CMB-Temperatur in der Grundform [S] (Dok. 388)
Die Relation T_CMB = (16/9)ξ(1 − 275ξ/4) eV trifft nur in der Einheit eV, und das eV bringt
die Elektronenmasse als zweiten Anker mit. In der Grundform hängt T_CMB/m_e an einer
einzigen Zahl; der Kandidat T_CMB/m_e = (8π)^(1/4)·ξ^(5/2) trifft den FIRAS-Wert auf 0,12σ.
Mit der H₀-Form des Korpus folgt T_CMB⁴ = 16·H₀·m_e³, also H₀ = 66,81 ± 0,06 km/s/Mpc aus
der CMB-Temperatur, und L_ξ ist ohne die CMB festgelegt. Die ältere H₀-Form mit dem
Exponenten 41/4 liegt dann 11σ daneben. Vorfaktor und Exponent 10 sind nicht hergeleitet.

### Wo α steckt [B] (Dok. 386)
Mit ħ = c = ε₀ = 1 und α = 1 ist e = √(4π); α wandert in die Ladungseinheit,
α = (e_hist/e_geo)² = r_e/λ_C, das Verhältnis von Coulomb- und Compton-Kugel des
Elektrons. In der Grundform lautet die Brücke ξE₀² = 1, also E₀² = 1/ξ = 7500, und
geometrisch ist ξ = λ_e·λ_μ die Fläche der Compton-Kugeln von Elektron und Myon.
Die fraktale Korrektur tritt erst in der SI-Übersetzung auf; das MeV ist eine Einheit
der SI-Kette [Q].

### Eine Kette, ein Anker (Dok. 383)
v ist Zwischengröße: v/E_P = ξ⁴/(5π) und m_i/E_P = r_i/(5π)·ξ^{p_i+4} [B]. Mit einem
einzigen Messwert als Anker folgen E_P, G, ℓ_P und L₀; die Streuung je nach Ankerwahl
ist der bekannte Rest der Leiter [K]. Der Faktor 10 in der Formel für v ist an den
Messwert angepasst (Dok. 387).

### Die Abweichungen im Überblick (Dok. 387)
Alle Abweichungen mit Messunsicherheit an einem Ort: die Verhältnisse der Grundform,
die SI-Übersetzung, β_T (schon in den frühesten Dokumenten mit α = 1 neben β_T = 1),
die Varianten von K_frak (74/75 als einzige mit ganzer Umlaufzahl) und der Faktor 10
(mit nacktem v der Leiter wird er zu 10·K_frak ≈ π² [S]). Die Messgenauigkeit trägt
für Leptonen, α und v/E_P nur minimal bei.

### Higgs-Vakuum-Weg (Dok. 385)
Herkunft der Formel ξ_EFT = m_h²/(64π³v²) = 1,30·10⁻⁴ aus der Vakuumformel von 2025;
ausgeschrieben ist sie ξ_EFT·α, mit α = 1 derselbe Ausdruck [B]. Gegen 4/30000 rund
−2,3 % (PDG 2024): eine Konsistenzprüfung auf wenige Prozent, keine exakte Herleitung.

### Rekursion, Träger und g−2 (Dok. 380–382)
Teleskopprodukt der Rekursion exakt [B], Rotationszahl 74/75; D₄ hat unter den
geprüften Vergleichsträgern die kleinste Gitterenergie [K], bleibt aber motivierte
Setzung [S]. Myon g−2 nach dem Stand 2025: Die Anomalie ist auf etwa 0,6σ
geschrumpft, ein fester FFGFT-Zusatz Δa_μ = 251·10⁻¹¹ ist überholt [X]; die
Verhältnis-Linie für a_τ bleibt.

---

## A-Serie v1.5

- **Neu: A125 — φ-Skelett: von den Gewichten zu den Massenverhältnissen** (De/En, je
  6 Seiten, Prüfskript 32/32). Schließt die in A120 offene Kante zwischen den
  Ikosaeder-Gewichten und den Massenverhältnissen, soweit der Korpus sie heute
  schließt; nimmt Dok. 364 und 367–370 auf.
- **A120:** Vermerke (der Leak (7−3φ)/9 ist mit δ* nicht verträglich, R139; Verweis
  auf A125). A010, A230, A250, README und CHANGELOG nachgezogen; jetzt 49 Dokumente.
- **A075, A142:** Vermerke vom 2. Okt. 2026 — der SM-Grenzfall ist nur für das Skalarfeld gezeigt ([K] → [S]); die modifizierte Schrödinger-Gleichung in A142 ist dimensional inhomogen ([B] → [S]); der a_e-Zusatz 2,34·10⁻¹⁰ ist durch die Messung ausgeschlossen. Das in A142 genannte, bisher fehlende Prüfskript `a142_gravitation_lagrange.py` ist ergänzt (12/12).
- Die A-Serie trägt seit der Rechenprüfung datierte Hinweise im Text (R140).

---

## Bezeichnung f (R147)

Das Symbol f trägt im Korpus vier Bedeutungen: die Grundwindungszahl f = 1/ξ, eine
Frequenz, den Strukturfaktor f(n,l,j) und weitere Funktionen. In über 80 Dokumenten
(De/En) steht jetzt an der ersten Stelle ein Vermerk, dass f dort keine Frequenz ist.
Die Grundwindungszahl ist in natürlichen Einheiten nur eine andere Lesart der Dualität
T·m = 1 und lässt sich als dimensionsloses Verhältnis nicht begründet auf 1 setzen
(A135).

---

## Korrekturen (Dok. 190, R128–R147)

| Eintrag | Betrifft | Inhalt |
|---------|----------|--------|
| R128 | Dok. 221 | Keine Abweichung der Supernova-Zeitdehnung von (1+z) bei hohem z [X] |
| R129 | Dok. 006, 046 | Ungebuchte frühe Änderungen der Quantenzahlentabelle nachgetragen |
| R130 | Dok. 343 | Satz A: Reichweite der Aussage |
| R131 | Dok. 091 | Zeta-Regularisierung der Modensumme für das Korpusgitter geschlossen |
| R132 | Dok. 010, 012, 013 u. a. | Rechnungen zur Gravitationskonstante korrigiert |
| R133 | Dok. 003–300 (Auswahl) | Befunde der Rechenprüfung im Text korrigiert |
| R134 | Dok. 000–002 | Akronym-Auflösung und ξ-Formel in Einleitungsdokumenten |
| R135 | Dok. 011, 041, 044 u. a.; A010, A130 | Einstufung von α, E₀ und K_frak |
| R136 | Dok. 009, 016, 025 u. a.; A260 | Casimir-CMB-Verbindung: Identität, kein Messbeleg |
| R137 | Dok. 008, 025, 026 u. a. | CMB-Temperatur, Rotverschiebung, H₀ und Λ präziser eingestuft |
| R138 | Dok. 006, 009, 012 u. a. | Präzisionstabellen der Massenleiter sind keine Belege |
| R139 | Dok. 268, 291, 293 | CMB-Faktor 3 und Form von K_frak wieder offen |
| R140 | Fortsetzung von R133 | Rechenprüfung auf alle Dokumente bis Nr. 300 und die A-Serie ausgedehnt |
| R141 | Dok. 012, 013, 016 u. a.; A145, A220 | G-Präzision: Rest der Ein-Anker-Kette in C_conv |
| R142 | Fortsetzung von R133 | Rechenprüfung der QM-Dokumente |
| R143 | Dok. 022, 035, 148; A165 | Unbelegte CHSH-Daten und daran angepasstes ξ entfernt |
| R144 | Dok. 325 | R93 und R94 präzisiert (Schwarze Löcher) |
| R145 | Dok. 327, 322, 330 | Selbstadjungiertheit von F̂ nur auf dem ℤ₃-invarianten Sektor |
| R146 | Dok. 347, 346, 356, 357 | Gell-Mann-Nishijima nicht vollständig geschlossen |
| R147 | Dok. 018, 159, 186, 210 u. a. | Bezeichnung f: keine Frequenz; f = 1/ξ nicht auf 1 setzbar |

---

## Offene Brücken (Stand R147, Auswahl)

| Brücke | Status |
|--------|--------|
| τ_μ direkt aus FFGFT (ohne G_F und v) | [S] (R112, Dok. 351) |
| Herkunft der Zahl 100 und des angepassten Faktors 10 in v/E_P | [S] (Dok. 149, 387) |
| Rest 1,7·10⁻⁴ zwischen dem von α verlangten K_frak und 1 − 100ξ; Form des Faktors | [S] (R135, R139) |
| Rest der Ein-Anker-Kette bei G | [S] (R141, Dok. 383) |
| Faktoren 74 und 1/45 des φ-Skeletts; gemeinsame Wurzel von Ikosaeder-Phase und Galois-Ordnung | [S] (Dok. 368, 370, A125) |
| Koide-Amplitude d/c = √2 aus der Geometrie | [S] (Dok. 352 §8) |
| Hyperladung der geladenen Leptonen | [S] (R146) |
| Selbstadjungiertheit von F̂ auf dem ganzen Raum | [S] (R145) |
| Quark-/Hadron-Sektor; K_had | offen (Dok. 318, R76, R123) |
| Kosmischer Exponent vorwärts (P20); CMB-Peaks {1,6,14,26} | offen (P20, P29/P31, R139) |
| Vorfaktor (8π)^(1/4) der CMB-Temperatur | [S] (Dok. 388) |

## Einstieg für neue Leser
**Dok. 384 „FFGFT in Kurzfassung“** (De/En, je 23 S., auch als HTML) ist der
empfohlene Einstieg in den heutigen Stand. Dok. 205 „FFGFT in einfacher Sprache“
bleibt der Einstieg für Laien; das Ikosaeder-Buch *Die Zahl, die niemand erklärte*
der Einstieg in die Leptonmassen.

## Was sich nicht geändert hat
ξ und T̃·m = 1 sind unverändert. Alle Ergebnisse aus v1.4.2 gelten weiter, soweit sie
nicht durch R128–R147 oder die Hinweise der Rechenprüfung präzisiert, eingeschränkt
oder zurückgenommen sind.
