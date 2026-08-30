# Versionshinweise — v1.3.5 (August 2026)

**DOI:** wird bei Zenodo-Publikation vergeben — ersetzt v1.3.3 und v1.3.4  
Laufendes Korrekturregister: **[2/pdf/190_T0_Korrekturen_De.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_De.pdf)**  
Archiviertes Register: **[2/pdf/190_T0_Korrekturen_Archiv_De.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_Archiv_De.pdf)**  
Änderungsprotokoll: **[000_FFGFT_Changelog_De.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/000_FFGFT_Changelog_De.md)**  
A-Serien-Protokoll: **[A_Serie_Export/A_SERIE_CHANGELOG.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/A_Serie_Export/A_SERIE_CHANGELOG.md)**

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** zeigt: alle Standardmodellkonstanten folgen aus einem einzigen dimensionslosen Parameter **ξ = 4/30000** auf einem kompakten 4D-Torus T⁴. Die Grundrelation lautet **T̃ · m = 1** — intrinsische Zeit und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Diese Version konsolidiert die Arbeit seit v1.3.3: fünf neue Dokumente (328–339,
ohne 331), die explizite Deklaration der Ableitungsgeschlossenheitsbedingung für
[K]- und [B]-Marker (R103) sowie zwei Dokumente, die erstmals vollständige
Marker-Abdeckung erhalten (Dok. 335, 339).

**Der Schwerpunkt liegt auf drei Bereichen.**

Dok. 336 und 338–339 erweitern das algebraische Programm in die
Galois-Feldstruktur: GF(9) als FFGFT-Brücke zwischen dem T⁴/ℤ₃-Orbifold und den
Eichgruppen des Standardmodells, sowie der Frobenius-Automorphismus auf GF(27) als
einzige algebraische Quelle für Photon, massiven Sektor und acht Gluonen — alle
Teilchenzahlen algebraisch erzwungen, keine freien Parameter.

Dok. 335 schließt die Interferometriefrage, die seit den Holometer-Ergebnissen
offen war: nicht ein konstruktionsbedingter blinder Fleck, sondern die
massegebundene Zeitskala T̃ · m = 1 erklärt, warum Holometer-artige Experimente
bei ihrer derzeitigen Empfindlichkeit kein Diskretheitssignal finden können.
Das Hawking-Quant und die Interferometerfrequenz liegen 13 Größenordnungen
auseinander.

Dok. 190 erhält seinen ersten Spezifikationszusatz seit der Registerumstrukturierung:
Die Ableitungsgeschlossenheitsbedingung für [K]- und [B]-Marker wird jetzt
explizit deklariert (R103), wodurch die Audit-Architektur unabhängig prüfbar wird.

---

## Einstiegspunkt für neue Leser

Dok. 205 „FFGFT in einfacher Sprache" (DE+EN, 13–14 Seiten) bleibt der empfohlene
Einstiegspunkt. Der einzige offene Falsifikationstest ist unverändert und explizit
benannt: m_τ = 1776,97 MeV, zu entscheiden durch Belle II, ohne Ausweichroute.

## Was sich nicht geändert hat

ξ, die Grundrelation T̃ · m = 1 und alle Ableitungsketten aus v1.3.3 sind
unverändert. R103 spezifiziert, was in der Praxis bereits eingehalten wurde;
kein Zahlenwert ändert sich.

---

## Neue Dokumente seit v1.3.3

### Dok. 328 — Kopplungsregime und Resonanzgeometrie (DE+EN)

Herleitung der Kopplungsregimeübergänge aus der T⁴/ℤ₃-Resonanzstruktur.
Starkes, elektroschwaches und gravitatives Regime als Konsequenzen von
Windungszahlschwellen auf den kompakten Richtungen.

→ [DE](2/pdf/328_Kopplungsregime_Resonanz_De.pdf) · [EN](2/pdf/328_Kopplungsregime_Resonanz_En.pdf)

### Dok. 329 — Ist die Stabilitätsschwelle n_thresh universell? (DE+EN, 7 S. je)

*(Bereits in v1.3.3 dokumentiert; hier der Vollständigkeit halber wiederholt.)*

→ [DE](2/pdf/329_nthresh_Skalenanalyse_De.pdf) · [EN](2/pdf/329_nthresh_Skalenanalyse_En.pdf)

### Dok. 330 — T⁴-Operationen und Randbedingungen (DE+EN)

Systematische Behandlung zulässiger Operationen auf der T⁴/ℤ₃-Struktur und ihrer
Randbedingungen. Legt fest, welche Transformationen intern zum Framework gehören
und welche eine explizite [SETZUNG]-Deklaration erfordern.

→ [DE](2/pdf/330_Operationen_T4_Abgrenzung_De.pdf) · [EN](2/pdf/330_Operationen_T4_Abgrenzung_En.pdf)

### Dok. 332 — Kontinuumskonstruktionen aus dem diskreten Substrat (DE+EN)

Herleitung kontinuumsfeldtheoretischer Strukturen aus dem diskreten T⁴/ℤ₃-Substrat.
Behandelt den Übergang vom Gitter zur effektiven Feldtheorie ohne Einführung neuer
Parameter.

→ [DE](2/pdf/332_Kontinuumskonstruktionen_De.pdf) · [EN](2/pdf/332_Kontinuumskonstruktionen_En.pdf)

### Dok. 333 — K_frak-Dualität und die fraktale Korrektur (DE+EN)

Zeigt, dass die K_frak-Korrektur K_frak = 1 − 100ξ eine notwendige Konsequenz
der T̃·m=1-Dualität angewendet auf SI-Einheitenausdrücke ist. Die Korrektur wirkt
ausschließlich auf absolute SI-Werte, nicht auf die Pullback-Isometrie selbst
(R96, R98).

- **Zentrales Ergebnis [B]:** K_frak ist algebraisch durch die Dualität erzwungen;
  sie kann nicht auf null gesetzt werden, ohne T̃·m=1 in der SI-Darstellung zu
  widersprechen.

→ [DE](2/pdf/333_Kfrak_Dualitaet_De.pdf) · [EN](2/pdf/333_Kfrak_Dualitaet_En.pdf)

### Dok. 334 — Superposition ohne Zeit (DE+EN)

Analyse der Quantensuperposition im FFGFT-Rahmen, in dem Zeit kein unabhängiger
Hintergrundparameter ist, sondern eine aus T̃·m=1 abgeleitete Größe.

→ [DE](2/pdf/334_Superposition_ohne_Zeit_De.pdf) · [EN](2/pdf/334_Superposition_ohne_Zeit_En.pdf)

### Dok. 335 — Massegebundene Zeitskalen und Interferometrie (DE+EN, 6 S. je)

Schließt die Frage, warum Holometer-artige Experimente kein Diskretheitssignal
finden.

Die relevante Frequenzskala der Raumquantisierung in FFGFT ist nicht
f ~ c/(2ℓ_P) (universelle Planck-Frequenz), sondern f_m = mc²/h
(massegebundene Comptonfrequenz). Diese Skala ist für jedes Teilchen verschieden
und liegt für alle stabilen Teilchen um mindestens 13 Größenordnungen über den
Messfrequenzen derzeitiger Interferometer.

- **Comptonfrequenzen [K]:** f_e = 1,2356×10²⁰ Hz, f_p = 2,2687×10²³ Hz —
  aus T̃·m=1 hergeleitet, keine freien Parameter.
- **Frequenzlücke [K]:** f_e/f_c(Holometer) ≈ 3,3×10¹³;
  f_e/f_c(QUEST) ≈ 1,5×10¹².
- **Gitter-Dispersion [K]:** an der Elektron-Compton-Skala beträgt die Korrektur
  ~10⁻⁴⁴ — für kein derzeitiges Instrument messbar.
- **K_frak-Korrektur [K]:** Δf_e/f_e = 100ξ ≈ 1,33 % — spektroskopisch im
  Prinzip zugänglich (Hartröntgenbereich), nicht interferometrisch.
- **Falsifizierbarkeit [K]:** Ein Interferometersignal bei f würde ein masseloses
  Feld mit m = hf/c² erfordern; bei 3,75 MHz ergibt das m ≈ 3×10⁻¹⁴ m_e —
  kein bekanntes Teilchen.

Externe Eingaben als [SETZUNG] deklariert: PDG-Massen für e, μ, p, n; h und c
als SI-Ausdrücke ξ-abgeleiteter Größen.

Prüfskript: `325_paul_frequenzen.py` (5 Assertionen).

→ [DE](2/pdf/335_Frequenzskalen_De.pdf) · [EN](2/pdf/335_Frequenzskalen_En.pdf)

### Dok. 336 — GF(9) als FFGFT-Brücke (DE+EN)

GF(9) = GF(3²) als algebraische Brücke zwischen der T⁴/ℤ₃-Orbifold-Struktur und
der Eichalgebra des Standardmodells. Die Erweiterung GF(3) → GF(9) erzeugt die
schwache SU(2)-Isospinstruktur algebraisch, ohne zusätzlichen Input.

- **Zentrale Brücke [B]:** Die multiplikative Gruppe GF(9)* ≅ ℤ₈ kodiert die
  elektroschwache Dublett-Struktur; der Frobenius auf GF(9) erzeugt die
  Teilchen-Antiteilchen-Paarung.
- **Eichemergienz [B]:** U(1)_Y × SU(2)_L entsteht aus der GF(9)-Feldstruktur
  angewendet auf die T⁴/ℤ₃-Windungsmoden.

Prüfskript: 48 [B]-Assertionen.

→ [DE](2/pdf/336_GF9_FFGFT_Bruecke_De.pdf) · [EN](2/pdf/336_GF9_FFGFT_Bruecke_En.pdf)

### Dok. 337 — Zeitemergienz in FFGFT und GALG (DE+EN)

Vergleich des Zeitentstehungsbilds in FFGFT (T̃·m=1) mit dem GALG-Framework.
Legt fest, wo die beiden Ansätze strukturell übereinstimmen und wo sie divergieren.

→ [DE](2/pdf/337_Zeit_Emergenz_FFGFT_GALG_De.pdf) · [EN](2/pdf/337_Zeit_Emergenz_FFGFT_GALG_En.pdf)

### Dok. 338 — Galois-Feldmassen in FFGFT (DE+EN)

Massenherleitung für das Teilchenspektrum aus der Galois-Feldhierarchie
GF(3) ⊂ GF(9) ⊂ GF(27). Fermion-Generationsstruktur aus dem Erweiterungsgrad;
Massenverhältnisse aus den Feldordnungen.

- **Generationszahl [K]:** Drei Fermionengenerationen = Erweiterungsgrad 3 von
  GF(3) → GF(27), algebraisch erzwungen.
- **Massenverhältnisse [K]:** Aus |GF(9)*| = 8 und |GF(27)*| = 26 hergeleitet.

Prüfskript: 9 [K]-Assertionen.

→ [DE](2/pdf/338_Galois_Massen_FFGFT_De.pdf) · [EN](2/pdf/338_Galois_Massen_FFGFT_En.pdf)

### Dok. 339 — Frobenius-Trennung auf GF(27) (DE+EN, 4 S. je)

Der Frobenius-Automorphismus φ: x ↦ x³ auf GF(27)* = ℤ₂₆ trennt die 26
Nicht-Einheits-Elemente in genau drei Sektoren: ein Fixkörper GF(3)* = ℤ₂
(zwei Fixpunkte), vier Orbits der Länge 3 auf ℤ₁₃ (acht Elemente) und die
verbleibende Struktur, die genau 8 dreistellige Orbits in ℤ₂₆ ergibt.

Alle drei Teilchenzahlen — Photon, massiver Sektor, acht Gluonen — folgen aus
|GF(27)| = 3³ und dem Frobenius der Ordnung 3 auf ℤ₁₃ allein. Kein
Standardmodell-Input wird verwendet.

| GF(27)-Sektor | Physikalischer Sektor | Symmetrie |
|---|---|---|
| GF(3)* = ℤ₂ — Fixpunkte {+1,−1} | Photon | U(1) |
| Fixpunkte {+1,−1} ⊂ GF(27)* | Massive Teilchen/Antiteilchen | ℤ₂ |
| 4×2 Dreier-Orbits in GF(27)* | 8 Gluonen | SU(3)_adj |

- **Frobenius-Zerlegung [B]:** Algebraisch exakt, auf Maschinengenauigkeit geprüft.
- **Orbit-Tabelle [B]:** Vollständig; alle 26 Elemente erfasst.
- **Teilchenzuordnung [K]:** Fixpunkte = massiver Sektor folgt aus der
  T̃·m=1-Dualität (kompakter Torus = massiv, masselos = Windungsmode).
- **Algebraische Notwendigkeit [B]:** 8·3 = 24 = Kissing(D₄) algebraisch erzwungen
  (3³−3 = 24); Verbindung zur D₄-Geometrie bleibt offen [S].

Prüfskript: `pruef_339_frobenius.py` (6/6 Assertionen).

→ [DE](2/pdf/339_Frobenius_Trennung_De.pdf) · [EN](2/pdf/339_Frobenius_Trennung_En.pdf)

---

## Markersystem — Spezifikationszusätze

### R103 — Ableitungsgeschlossenheitsbedingung für [K] und [B] explizit deklariert

*Anlass: Korrespondenz mit S. Vossen, August 2026
(Thread: „substrate standing and ontological constitution").*

Ein Ergebnis trägt **[K]** oder **[B]** nur dann, wenn seine vollständige
Ableitungskette von ξ aus lückenlos verfolgbar ist. Zulässige Kettenglieder:

1. Geometrische Konsequenzen der festgelegten T⁴/ℤ₃-Struktur
2. Algebraische Konsequenzen eines vorangehenden Kettenglieds
3. Deklarierte externe Eingaben ([SETZUNG]) einschließlich PDG-Werte und
   SI-Größen, die ihrerseits ξ-abgeleitete Größen in SI-Darstellung sind

Ein Ergebnis, das einen nicht so verankerten externen Parameter benötigt, trägt
weder [K] noch [B], unabhängig davon ob es einen korrekten Zahlenwert erreicht.

Diese Bedingung war in der Praxis durchgehend eingehalten (vgl. Dok. 320, 323,
333, 335, 339), aber in den Marker-Definitionen nicht explizit als separates
Kriterium deklariert. Zukünftige dokumentlokale Marker-Erklärungen sollen die
Kettenschlussbedingung explizit nennen; Dok. 190 registriert Anlass und Datum.

**Korollar — zwei Arten von Geschlossenheit:**

- *ξ-interne Geschlossenheit* — jede Größe wird intern aus ξ erzeugt, kein
  externer Input; gilt wo erreichbar; [K] ohne [SETZUNG] im Pfad.
- *Auditierbare Geschlossenheit innerhalb eines deklarierten Rahmens* — externe
  Standard- oder empirische Eingaben sind zulässig, sofern jede Abhängigkeit
  lokalisiert und als [SETZUNG] deklariert oder als [Q] zitiert ist. Gilt in
  Dokumenten wie A155 und Dok. 335.

**Korollar — Pfadabhängigkeit von [S]:**

Ein offener [S]-Punkt suspendiert [K]- oder [B]-Standing nur dort, wo der
Ableitungspfad dieses Ergebnisses durch den unaufgelösten [S]-Punkt läuft.
Die Kontamination ist pfadabhängig, nicht global durch das Dokument oder den
Corpus.

---

## Vollständiges Markerregister (Stand v1.3.5)

| Marker | Bedeutung | Eingeführt |
|--------|-----------|------------|
| [SETZUNG] | Deklarierter Ausgangspunkt oder Axiom | A010 |
| [B] | Algebraisch/mathematisch aus deklarierten Grundlagen bewiesen | A010 |
| [K] | Aus ξ hergeleitet, numerisch geprüft, Kettenschlussbedingung erfüllt | A010 |
| [S] | Plausibilitätsskizze, noch nicht vollständig ausgeführt | A010 |
| [Q] | Korpusexterne Primärquelle oder gemessener/bewiesener Wert | A271, Dok. 315+ |
| [H] | Offene Forschungsfrage | A270 |
| [X] | Ausschluss auf Satzebene / abgeschlossen negativ | Dok. 316+ |
| [E] | Kontextabhängig: externe Physik als Grundlage (Dok. 328) oder extern gescheiterter Test (Dok. 330) | Dok. 328+ |

---

## Korrekturen — R93 bis R103

**R93–R98** (Aug. 2026): K_frak-Korrekturen und SI-Einheitenbrücken-Klarstellungen
(Dok. 333, 190). Die K_frak-Korrektur ist algebraisch erzwungen [B]; sie wirkt nur
auf SI-Werte, nicht auf die Pullback-Isometrie. ħ und c sind ξ-abgeleitete Größen
in SI-Darstellung; ihr Status als SI-Umrechnungsfaktoren ist sekundär und
pragmatisch, kein unabhängiges Postulat.

**R99–R102** (Aug. 2026): Galois-Feldprogramm — GF(9)-Brücke [B] (Dok. 336);
Galois-Massen [K] (Dok. 338); Frobenius-Trennung [B] (Dok. 339);
1/α = 3700/27 = 137,037 (7,6 ppm) rein aus Galois-Gruppenordnungen [K]
(Dok. 338). Neue Beobachtung: m_e · m_μ = 54 = |GF(3)*|·|GF(27)| MeV²
(0,016 %; Dok. 011 begründet geometrisch). |GF(27)| kürzt sich heraus;
kein ξ, kein v, kein m_e als expliziter Eingang.

**R103** (29. Aug.): Ableitungsgeschlossenheitsbedingung für [K] und [B] explizit
deklariert. In der Praxis bereits eingehalten; jetzt prospektiv in dokumentlokalen
Marker-Erklärungen gefordert. Anlass: Vossen-Korrespondenz, Substrat-Standing-Thread.
Siehe Markerspezifikationsabschnitt oben.

---

## Geschlossene Brücken in dieser Version

| Brücke | vorher | nachher | Dok. |
|--------|--------|---------|------|
| Interferometrie-Nullergebnisse erklärt | [S] | **[K]** massegebundene Zeitskala | 335 |
| GF(9) als elektroschwache Brücke | — | **[B]** | 336 |
| Drei Fermionengenerationen aus Galois-Erweiterung | implizit | **[K]** | 338 |
| Frobenius-Trennung: Photon, Massives, Gluonen | — | **[B]** | 339 |
| 8 Gluonen aus GF(27)* algebraisch | — | **[B]** | 339 |
| K_frak algebraisch durch T̃·m=1 erzwungen | [S] | **[B]** | 333 |
| Kettenschlussbedingung für [K]/[B] | implizit | **deklariert** | R103 |

## Verbleibende offene Brücken

| Brücke | Status |
|--------|--------|
| Δm²₃₂ (+16,0 % nach R87; Mischterm F₅–F₇) | [S] |
| 2-Schleifen-Korrekturen zu α_s(M_Z) | [S] |
| m_Pl und α_em(M_Z) aus ξ | [S] |
| Quark-/Hadronsektor | offen (Dok. 318, R76) |
| Graukörper-Faktoren; Rückreaktion auf Fixpunkte | [S] (R85) |
| Vorwärtsableitung des kosmischen Exponenten 41/4 (P20) | offen — größter Hebel |
| CMB-Peaks {1,6,14,26}; \|n\|²=30 | offen (P29/P31) |
| C_ℓ Quell-/Fensterfunktion | offen (P30) |
| Ω_DM quantitativ, modellneutral | offen (P17) |
| Spektraldimension d_s = 1,86 vs. ≈ 2 | offen |
| H₀ Sprachbereinigung; Überarbeitung Dok. 026 | offen (P34/P16) |
| ξ als Linienbreite; ι-Einbettung HLV ⊂ FFGFT | vorregistriert (P44, Dok. 297) |
| D₄-geometrische Verbindung zu Kissing(D₄) = 24 | [S] (Dok. 339) |

---

## Prüfskripte (neu in dieser Version)

`python/Dok325_Skripte/`:
- `325_paul_frequenzen.py` — massegebundene Frequenzen, Frequenzlücke, Dispersion,
  K_frak spektroskopisches Fenster, Falsifizierbarkeit (5)

`python/Dok332_Skripte/`:
- `pruef_332_krueger_periodizitaet.py` — Kontinuumskonstruktions-Assertionen
- `pruef_335_paul_frequenzen.py` — Dok. 335-Verifikation (5)
- `pruef_339_frobenius.py` — Frobenius-Trennung, Orbit-Tabelle, Teilchenzahlen (6)
- `pruef_marcel_h1_sobolev.py` — Sobolev-Randbedingungen

---

## Lizenz

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

*Etablierte Ergebnisse sind im Corpus dokumentiert; offene Vorhersagen unterliegen
der experimentellen Überprüfung.*
