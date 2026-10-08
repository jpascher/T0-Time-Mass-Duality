# Release Notes — v1.4.5 (8. Oktober 2026)

**DOI:** wird bei der Zenodo-Veröffentlichung vergeben — ersetzt v1.4.4
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

v1.4.5 ist die erste Fassung ohne Korrekturvermerke. Alle Dokumente enthalten nur noch
die korrigierte letzte Fassung; wer nachvollziehen will, was sich wann geändert hat,
findet das in Dok. 190 und in v1.4.4, der letzten Fassung mit datierten Vermerken.
Dazu kommen zwei Nachträge zum Korrekturregister (R148, R149), eine vollständige
Überarbeitung der HTML-Seiten mit einem neuen deterministischen Simulator und die
achtbändige Gesamtausgabe als Buch in Deutsch und Englisch. Neue Dokumente gibt es in
dieser Version nicht; Grundrelation und ξ sind unverändert.

---

## Dokumente ohne Korrekturvermerke

Am 6. Oktober 2026 wurden alle Dokumente in fünf Blöcken (Dok. 001–052, 053–150,
152–241, 243–310, 311–389) und die A-Serie (A010–A284) überarbeitet. Korrekturkästen,
datierte Vermerke und ältere Nachträge sind aufgelöst: Der Text sagt jetzt selbst, was
gilt, und widerlegte Aussagen sind so umgeschrieben, dass nur noch das Gültige steht.
Abstracts, Überschriften, Tabellen und Fazits sind angepasst. Korrekturen, die
korpusweit gelten, sind auch dort angewandt, wo der Registereintrag das Dokument nicht
nennt — etwa die achromatische Rotverschiebung, α als Eigenschaft des Ankers E₀ (R135),
die Casimir-CMB-Verbindung als Identität (R136), die G-Präzision (R141) und die
Ordnungssuche statt einer ξ-Resonanz bei der Faktorisierung (R65). Die einzelnen Blöcke
mit den größeren Umbauten stehen im Changelog.

## Nachträge zum Korrekturregister (R148, R149)

**R148** bucht nach, was die Rechenprüfung vom 1. Oktober bei den Dokumenten über
Nr. 300 und einigen älteren Dokumenten ergeben hatte, ohne dass es in einem
Sammeleintrag stand. Die wichtigsten Folgen: Der Higgs-Weg führt nicht auf ξ, er bleibt
Konsistenzprüfung; Trialität und Orbifold-Sektor sind zwei verschiedene ℤ₃; Satz A in
Dok. 349 und Satz C in Dok. 363 sind nicht bewiesen; die Quark-Vorfaktoren in Dok. 373
sind aus Messwerten bestimmt; die Galaxientests in Dok. 308 sind offen.

**R149** führt drei Korrekturen in den Dokumenten selbst aus. Dok. 382 rechnete die
direkten g−2-Formeln mit einem gerundeten k_geom; die Werte folgen jetzt Dok. 018, die
Verhältnis-Linie und die a_τ-Vorhersage sind davon nicht berührt. Dok. 006 vergleicht
die Quarkmassen jetzt mit PDG 2024, wie Dok. 384; die Abweichungen werden größer, beim
Up-Quark innerhalb der großen Unsicherheit dieses Werts, und die Quark-Vorfaktoren
bleiben aus Messwerten bestimmt [S]. In Dok. 073 heißt der numerische
Simulationsparameter σ statt ξ_num, weil er kein Wert von ξ ist (R75). Dok. 384
verweist jetzt auf den Registerstand R149.

## HTML-Seiten

Alle HTML-Seiten unter `2/html/`, `rsa/` und `sig/` sind auf den heutigen Korpusstand
gebracht: Statusangaben wie in Dok. 384, Statusmarker mit Legende, keine überholten
Präzisionsansprüche mehr, α = 1 ausdrücklich als Heaviside-Lorentz-Einheiten. Die
Startseite behält ihre Überschrift.

Der **Quantensimulator** (`2/html/quantum_simulator_deterministic.html`) ist neu
aufgebaut und folgt der deterministischen Messregel aus Dok. 230: Der Ausgang einer
Messung ist A(z, λ) = sgn(z − λ), die Born-Gewichte ergeben sich aus der Verteilung von
λ. Dazu gehören eine neue Hilfeseite (`quantum_help_guide.html`) und eine überarbeitete
Schritt-für-Schritt-Seite (`step_by_step_modules_bilingual.html`). Die Shor- und
Faktorisierungswerkzeuge wurden ein zweites Mal geprüft; Rechen- und Programmfehler
sind behoben. Sie sind als das beschrieben, was sie sind: eine korrekte klassische
Simulation der Ordnungssuche, kein eigenes FFGFT-Verfahren (R65).

## Gesamtausgabe in acht Bänden

Der Korpus erscheint als achtbändige Gesamtausgabe „FFGFT oder T0-Theorie:
Zeit-Masse-Dualität – Gesamtwerk“ (Amazon KDP), jeweils als eBook, Paperback
(8,5 × 11 in) und Hardcover (8,25 × 11 in), in Deutsch und Englisch. Band 1–3 sind die
ursprüngliche Drei-Band-Konzeption, Band 4 reicht bis Dok. 184, Band 5 bis Dok. 262,
Band 6 umfasst Dok. 263–310, Band 7 Dok. 311–343 und Band 8 Dok. 344–389. Die
Innenteile liegen unter `2/pdf/buecher/`, die Umschläge unter `2/kdp/Gesamtserie/`.

Das Korrekturregister Dok. 190 ist nicht mehr in Band 5 abgedruckt. Es wird laufend
weitergeführt; die Einleitung von Band 5 verweist auf die aktuelle Fassung im
Repository. Band 5 wird dadurch rund 30 Seiten kürzer.

| Band | Paperback De | Hardcover De | Paperback En | Hardcover En |
|------|--------------|--------------|--------------|--------------|
| 1 | 450 | 456 | 424 | 432 |
| 2 | 415 | 419 | 383 | 386 |
| 3 | 422 | 428 | 395 | 405 |
| 4 | 365 | 368 | 347 | 350 |
| 5 | 426 | 430 | 407 | 411 |
| 6 | 361 | 372 | 346 | 355 |
| 7 | 339 | 343 | 317 | 321 |
| 8 | 340 | 346 | 322 | 329 |

## Einstieg für neue Leser

**Dok. 384 „FFGFT in Kurzfassung“** (De/En, auch als HTML) bleibt der empfohlene
Einstieg in den heutigen Stand, Dok. 205 „FFGFT in einfacher Sprache“ der Einstieg für
Laien.

## Was sich nicht geändert hat

ξ und T̃·m = 1 sind unverändert. Alle Ergebnisse aus v1.4.4 gelten weiter, soweit sie
nicht durch R148 und R149 präzisiert oder eingeschränkt sind.
