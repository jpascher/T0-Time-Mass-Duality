# Versionshinweise — v1.3.6 (September 2026)

**DOI:** wird bei Zenodo-Publikation vergeben — ersetzt v1.3.5  
Laufendes Korrekturregister: **[2/pdf/190_T0_Korrekturen_De.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_De.pdf)**  
Archiviertes Register: **[2/pdf/190_T0_Korrekturen_Archiv_De.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_Archiv_De.pdf)**  
Änderungsprotokoll: **[001_FFGFT_Changelog_De.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/001_FFGFT_Changelog_De.md)**  
A-Serien-Protokoll: **[A_Serie_Export/A_SERIE_CHANGELOG.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/A_Serie_Export/A_SERIE_CHANGELOG.md)**

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** zeigt: alle Standardmodellkonstanten folgen aus einem einzigen dimensionslosen Parameter **ξ = 4/30000** auf einem kompakten 4D-Torus T⁴. Die Grundrelation lautet **T̃ · m = 1** — intrinsische Zeit und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Diese Version fügt Dok. 341 (GF(27) in GALG — algebraische Brücke FFGFT↔GALG),
die nachträgliche Marker-Zertifizierung R105 für neun Dokumente vor dem
Marker-System sowie ein vollständig verifiziertes Galois-Bündel (Dok. 317–341,
23 Prüfskripte, alle bestanden) hinzu.

**Schwerpunkt: zwei Bereiche.**

Dok. 341 schließt den algebraischen Vergleich zwischen FFGFT und Doug Matzkes
GALG-Framework. Das zentrale Ergebnis: Dougs Suchergebnis „Attempted 6561 with
0 found" ist algebraisch notwendig — GF(27) kann in G(3) nicht auftreten weil
13 ∤ |GF(81)*|. In G(6) existieren Elemente der Ordnung 26 und werden explizit
in GALG-Blade-Notation angegeben, direkt nachprüfbar. Die Vakuumstruktur-Analyse
bestätigt dass GALGs Witt-Paar-Vakuum exakt der FFGFT-Frobenius-Trennung aus
Dok. 339 entspricht.

R105 vervollständigt die Prüfkette für das Galois-Programm: neun Dokumente vor
dem Marker-System (Dok. 006, 011, 070, 182, 231, 257, 285, 306, 307) werden
nachträglich via Dok. 190 als [K] oder [B] zertifiziert, sodass abhängige
Dokumente (336, 338, 339, 340, 341) ihre Ergebnisse als auditierbare Kettenglieder
behandeln können.

---

## Einstiegspunkt für neue Leser

Dok. 205 „FFGFT in einfacher Sprache" (DE+EN, 13–14 Seiten) bleibt der empfohlene
Einstiegspunkt. Der einzige offene Falsifikationstest ist unverändert:
m_τ = 1776,97 MeV, zu entscheiden durch Belle II, ohne Ausweichroute.

## Was sich nicht geändert hat

ξ, die Grundrelation T̃ · m = 1 und alle Ableitungsketten aus v1.3.5 sind
unverändert. R105 spezifiziert was in der Praxis bereits eingehalten wurde;
kein Zahlenwert ändert sich.

---

## Neues Dokument seit v1.3.5

### Dok. 341 — GF(27) in GALG: algebraische Brücke FFGFT↔GALG (DE+EN)

Zentrale Frage: Kann GF(27)-Struktur in Doug Matzkes GALG-Framework G(6,ℤ₃ℂ)
auftreten, und wenn ja, wo?

**Satz A [B]:** G(3) ≅ M₂(GF(9)) ⊕ M₂(GF(9)) — Ordnungen teilen 80·3.
Da 13 ∤ |GF(81)*| = 80 sind Ordnung-26-Elemente in G(3) algebraisch unmöglich.
Dougs „Attempted 6561 with 0 found" ist kein Suchfehler — es ist eine strukturelle
Notwendigkeit.

**Satz B [B]:** In G(6) ≅ M₈(GF(9)) existieren Elemente der Ordnung 26.
Explizite Konstruktion über die Begleitmatrix von f(x) = x³+2x+1 über GF(3),
die irreduzibel und primitiv ist (Ordnung 26 = |GF(27)*|). Ein konkretes
5-Blade-Element in GALG-Notation zur direkten Verifikation:

    X = −(1+i)·(e1∧e2) + (1+i)·(e1∧e2∧e3∧e6) + (1−i)·(e1∧e2∧e5∧e6)
        + (1+i)·(e1∧e4∧e5∧e6) − (e1∧e2∧e3∧e4∧e6);   X^26 = 1, X^13 ≠ 1

Ordnung-26-Elemente benötigen mindestens 5 Blades; sie fehlen in spärlichen
(2–4 Blade-)Elementen, treten aber bei ~18–37% der invertierbaren Elemente
mit ≥6 Blades auf.

**Satz C [B]:** GF(27) bettet sich genau dann als Teilkörper in M_n(GF(9)) ein
wenn 3 | n. Da G(3) → n=2 und G(6) → n=8, trägt keines GF(27) als Teilkörper.
GF(27) ist in G(6) als Ordnungsstruktur präsent, nicht als Teilkörper.

**Konsequenz:** α = 1/(137,037) ist auf der G(3)/GF(9)-Ebene formulierbar;
die Leptonen-Massenschicht braucht G(6) mit Ordnung-26-Elementen. Dougs Aussage
„not working on mass" und sein Suchergebnis sind beide konsistent mit dieser
Trennung.

**Vakuumstruktur-Analyse [B]:** GALGs Witt-Paar-Vakuumstruktur unter ℤ₃
entspricht exakt der FFGFT-Frobenius-Trennung aus Dok. 339:
- Gerade Vakua [0,2,4]: ℤ₃-Fixpunkte (massiver Sektor-Analogon)
- Ungerade Vakua [1,3,5]: ein ℤ₃-Dreier-Orbit (Gluon-Sektor-Analogon)
- Bilaterale ap_i·ap_j verschieben N-Sektor um ±1 mod 3 (Gluon-Rolle)

Prüfskripte: `pruef_341_gf27_in_galg.py` (6/6 [B] Assertionen),
`pruef_341_vakuum_witt_z3.py` (7/7 [B] Assertionen).

→ [DE](2/pdf/341_GF27_GALG_FFGFT_De.pdf) · [EN](2/pdf/341_GF27_GALG_FFGFT_En.pdf)

---

## Markersystem — Spezifikationszusätze

### R105 — Nachträgliche Marker-Zertifizierung für Dokumente vor dem Marker-System
### (1. September 2026)

Neun Dokumente vor Einführung des Marker-Systems (A010) tragen keine eigenen
Marker, sind aber als notwendige Kettenglieder für das Galois-Programm
(Dok. 336, 338, 339, 340, 341) unerlässlich. Nachträglicher Status:

| Dokument | Inhalt | Status |
|----------|--------|--------|
| Dok. 006 | Teilchenmassen, Wicklungszahlen r_i, p_i | **[K]** |
| Dok. 011 | Feinstruktur α, E₀, Grundrelationen | **[K]** |
| Dok. 070 | Mathematische Struktur: K_frak kürzt in Verhältnissen | **[B]** |
| Dok. 182 | Maximale Universum-Skala aus ξ | **[K]** |
| Dok. 231 | Hilbertraum-Erweiterung, L²-Struktur | **[B]** |
| Dok. 257 | Informationseinheit, Bit-Energie-Skala | **[K]** |
| Dok. 285 | FFGFT-HLV-Dimensionsbrücke | **[K]** |
| Dok. 306 | Native Zeit-Energie-Reziprozität aus T̃·m=1 | **[K]** |
| Dok. 307 | Zeit im Zustandsraum | **[K]** |

Abhängige Dokumente können diese Ergebnisse mit Verweis auf R105 als gesichertes
Kettenglied behandeln, ohne die Originaldokumente zu ändern.

---

## Vollständiges Markerregister (Stand v1.3.6)

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

## Korrekturen — R104 bis R105

**R104** (Aug. 2026): v = m_e/((4/3)ξ^(3/2)) = 248,3 GeV [K]; G_F [K];
τ_n [K]; Δm [K]. Prüfskript: pruef_319 (7/7).

**R105** (1. Sept. 2026): Nachträgliche [K]/[B]-Zertifizierung für Dok. 006,
011, 070, 182, 231, 257, 285, 306, 307. Dokumente vor dem Marker-System,
Ableitungen inhaltlich schlüssig. Siehe Markerspezifikationsabschnitt oben.

---

## Galois-Bündel — vollständig verifiziertes Paket

Alle Dokumente und Skripte des Galois-Programms sind im Galois-Bündel (v2,
SHA-256: `a946e9871ea5a38808b54b83dfcc8b250a1f75a1aba2d393cdcfef0219af0354`)
zusammengefasst.

**23/23 Prüfskripte bestanden, 0 fehlgeschlagen.**

Dokumente: 317, 321, 323, 324, 336, 337, 338, 339, 340, 341 (Galois-Kern)
+ 006, 011, 070, 182, 231, 257, 285, 306, 307, 332, 333 (Abhängigkeitskette, R105)

---

## Geschlossene Brücken in dieser Version

| Brücke | vorher | nachher | Dok. |
|--------|--------|---------|------|
| GF(27)-Abwesenheit in GALG G(3) algebraisch bewiesen | — | **[B]** | 341 |
| GF(27)-Ordnungsstruktur in GALG G(6) präsent | — | **[B]** | 341 |
| GALG-Vakuum = FFGFT-Frobenius-Trennung | — | **[B]** | 341 |
| Dokumente vor Marker-System auditierbar | ungeprüft | **R105** | 190 |

## Verbleibende offene Brücken

| Brücke | Status |
|--------|--------|
| Δm²₃₂ Mischterm F₅–F₇ | [S] |
| 2-Schleifen-Korrekturen zu α_s(M_Z) | [S] |
| m_Pl und α_em(M_Z) aus ξ | [S] |
| Quark-/Hadronsektor | offen (Dok. 318, R76) |
| Graukörper-Faktoren; Rückreaktion auf Fixpunkte | [S] (R85) |
| Vorwärtsableitung des kosmischen Exponenten 41/4 (P20) | offen |
| CMB-Peaks {1,6,14,26}; \|n\|²=30 | offen (P29/P31) |
| D₄-geometrische Verbindung zu Kissing(D₄) = 24 | [S] (Dok. 339) |
| GF(27) als Teilkörper in G(6) | strukturell unmöglich (Dok. 341, Satz C) |

---

## Prüfskripte (neu in dieser Version)

`python/Dok341_Skripte/`:
- `pruef_341_gf27_in_galg.py` — GF(27)-Struktur in GALG G(3)/G(6); Sätze A–C; Ordnung-26-Elemente (6 [B] Assertionen)
- `pruef_341_vakuum_witt_z3.py` — Witt-Paar-Vakuum, Triality, ℤ₃-Trennung, Bilaterale (7 [B] Assertionen)

`python/Dok342_Skripte/`:
- `pruef_342_vakuum_witt_z3.py` — Unabhängige Verifikation der Vakuumstruktur (7 [B] Assertionen)

---

## Lizenz

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
