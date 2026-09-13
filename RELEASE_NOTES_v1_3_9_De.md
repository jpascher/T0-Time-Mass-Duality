# Release Notes — v1.3.9 (14. September 2026)

**DOI:** wird bei Zenodo-Publikation vergeben — ersetzt v1.3.8
Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Änderungsprotokoll: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** zeigt: Alle Konstanten des
Standardmodells folgen aus einem einzigen dimensionslosen Parameter **xi = 4/30000**
auf einem kompakten 4D-Torus T4. Die Grundrelation lautet **T~·m = 1** — intrinsische
Zeit und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Diese Version bringt zwei neue Bücher auf Amazon Kindle, erweitert Dok. 341
(algebraische Brücke FFGFT↔GALG) durch den produktiven Austausch mit Doug Matzke
wesentlich und fügt drei neue Dokumente hinzu (Dok. 361–363). Keine algebraischen
Ergebnisse aus Dok. 342–360 wurden geändert; eine Herabstufung (Dok. 355,
Heptagon-Phasen [B]→[S]) und eine Korrektur (Hyperbit-Buch ch07 Zitierstil)
sind enthalten.

---

## Neue Bücher auf Amazon Kindle

### Bits, Hyperbits und Landauer (De+En, je 93 S.)

Als Kindle-eBook, Taschenbuch und Hardcover auf Amazon KDP verfügbar (alle Märkte).
Das Buch vergleicht die Informationsphysik von Matzkes Hyperbit-Framework mit der FFGFT
und entwickelt die Landauer-Grenze thermodynamisch.
Kernaussage: einem Informationsbit kann keine Energie zugewiesen werden — nur seinem Träger.
Im Hyperbit-Framework sind die 6 Generatoren in G(6) der Träger;
in FFGFT ist es die Wicklungsmode auf dem T4/Z3-Torus.

---

## Neue und erweiterte Dokumente seit v1.3.8

### Dok. 341 — GF(27) in GALG: algebraische Brücke FFGFT↔GALG (De/En, je 15 S.)
*(wesentlich erweitert — war 9 S. in v1.3.8)*

**§5 Vakuum-Struktur (neu):** Vss[0..5] in Cl(6)/GF(9), Witt-Paare {13,26,45},
Z3-Trennung — gerade Vakua = Fixpunkte, ungerade = Dreier-Orbit = Frobenius-Trennung [B].
Neutrino = Vss[0], Bilaterale als Sektorwechsler (Gluon-Rolle).

**§6 Höhere Einheitswurzeln (neu):** Eintrittsskala ord_p(3): 13 (k=3), 5 (k=4),
11 (k=5), 7 (k=6) [K]. Kein root7 mit Z3C-Koeffizienten; Ordnung-7-Element
X7 = C_Phi7 ⊕ I2 in G(6), kompakt: Y (6 Blades, ord 182=2·7·13), X=Y^26 [K/B].
X^27=X ⟺ Spektrum ⊂ GF(27): Körperturm N→r26→X7 [K].
Koeffizientenreinheit: root26 mit reinen Koeffizienten (5 Blades) [B].
E7-Konvention erklärt Matzkes p27-Befund [K].
Jordan-Zerlegung X=S·U: r273, r546, r2184 in G(6) via 6-dim Block ⊕ J2 [K].
r729 erst ab Cl(16)=M256 [K]. Eulers phi: phi(80)=32, phi(182)=72 [K].

**Werkzeug-Vermerk (neu):** Klare Rollentrennung — Autorschaft Pascher+Matzke,
KI als Rechenwerkzeug; Methodik zur Vermeidung erfundener Inhalte.

Prüfskripte: pruef_341_gf27_in_galg · vakuum_witt_z3 · primordnung ·
root7_gf9 · r26_rein_p27 · unipotent_jordan · inverse_minpoly (alle 100%).

### Dok. 355 — SSB auf T4/Z3
Heptagon-Phasen k·360°/7 von [B] auf [S] — Charakteristik 3 kennt keine Winkel.

### Dok. 361 — Kagome-RVB-Polaronen und Frobenius-Struktur (De/En)
Fallstudie zu Pei et al. (PRL 137, 106702, Open Access). Vier Parallelen mit FFGFT [S]:
Frobenius-Orbits, Drei-Zustands-Potts=GF(3), Masse=eingefrorene kin. Energie, pi-Fluss.
Prüfskript: pruef_361_kagome_frobenius.py — 20/20.

### Dok. 362 — BAW-Ising-Maschine als Resonanzrechner (De/En, je 9 S.)
Fallstudie zu Vadde et al. (Commun. Phys. 9:290, CC-BY). Fünf Einordnungen [S].

### Dok. 363 — Hodge-Theorie auf T4/Z3 im Rahmen der FFGFT (De 9 S., En 8 S.)
**Hauptsatz [B]:** Alle Hodge-Klassen auf T4/Z3 sind rationale Linearkombinationen
algebraischer Zykel. Klare Grenze: Millennium-Problem für allgemeine Varietäten offen.
Prüfskripte: 23/23 + 38/38 Assertions.

---

## Korrekturen

- **R115:** Höhere Einheitswurzeln (Dok. 341 §6), E7-Konvention, Heptagon [S] (Dok. 355)
- **Dok. 190:** R115 nur im Changelog
- Hyperbit-Buch ch07: Zitierstil [T1]/[T2] statt BibTeX
- Hyperbit-Rahmen: doppelte Labels entfernt

---

## Register
R115 neu. R100–R114 unverändert seit v1.3.8.

---

## Aktualisierte Brücken seit v1.3.8

| Brücke | v1.3.8 | v1.3.9 |
|--------|--------|--------|
| GALG↔FFGFT algebraische Korrespondenz | [B] partiell | [B] erweitert: Vakuum-Trennung, Einheitswurzeln, Jordan-Zerlegung |
| Heptagon-Phasen k·360°/7 | [B] | [S] — Charakteristik 3 kennt keine Winkel |
| Hodge-Vermutung für T4/Z3 | — | [B] aus FFGFT-Struktur bewiesen |

## Offene Brücken (unverändert seit v1.3.8)

| Brücke | Status |
|--------|--------|
| CKM/PMNS-Winkelwerte (numerisch) | [S] (Dok. 348 Satz D) |
| HRV-Galois-Test: positives Ergebnis | [S] erfordert kontrollierte Atmung ≥13 min, n≥5 |
| Generationszuordnung (Reihenfolge) | [S] (Dok. 346) |
| m_Pl und alpha_em(M_Z) aus xi | [S] |
| Quark-/Hadron-Sektor | offen (Dok. 318, R76) |
| CMB-Peaks {1,6,14,26}; |n|²=30 | offen (P29/P31) |
| Delta m²_32 Mischterm F5–F7 | [S] |
| Torus T4/Z3 als GALG-Polynom | offen |

## Einstieg für neue Leser
Dok. 205 "FFGFT in einfacher Sprache" (De/En, 13–14 S.) bleibt der empfohlene
Einstiegspunkt. Das SWT-Manuskript (`SWT_Galois_HRV_v2.docx`) ist der empfohlene
Einstiegspunkt für die HRV-Anwendung der FFGFT.

## Was sich nicht geändert hat
xi, T~·m=1 und alle algebraischen Ergebnisse aus v1.3.7/v1.3.8 sind unverändert.
Alle Herleitungsketten aus v1.3.6 sind unverändert.
