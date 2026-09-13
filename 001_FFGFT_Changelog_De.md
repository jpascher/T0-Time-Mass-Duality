# FFGFT Changelog — laufend ab v1.3.4

**Grundlage:** Dok. 190 (Korrekturregister)  
**Archiv bis v1.3.3:** [`000_FFGFT_Changelog_De.md`](000_FFGFT_Changelog_De.md)

Neue Einträge werden hier oben eingefügt (neueste zuerst).

---
---

## 5. September 2026 — Dok. 006 Sprachkorrektur v (R112)

### Dok. 006 — v = 246 GeV präzisiert (De+En)

Zwei Stellen in Dok. 006 ergänzt (R112):

- Zeile „wobei v = 246 GeV der Higgs-Vakuumerwartungswert ist" →
  Zusatz: „(SM-Definition: v ≡ (√2·G_F)^(−1/2); kein unabhängiges Observable, Dok. 351/R112)"
- Zeile „Wir verwenden v = 246 GeV" →
  Zusatz: „(SM-Definition aus G_F, Dok. 351/R112)"

Keine Zahlenänderung. Dok. 231 und 344 waren bereits korrekt formuliert.


## 12. September 2026 — Dok. 361: Kagome-RVB-Polaronen und Frobenius-Struktur

### Dok. 361 — Pei et al. (PRL 137, 106702) im Vergleich mit FFGFT (De/En)

Fallstudie zu Pei, Chen, Castelnovo, Moessner (PRL 137, 106702, 31. Aug. 2026,
Open Access): einfach dotiertes Hubbard-Modell mit unendlicher Abstoßung auf dem
Kagome-Gitter — RVB-Polaronen, Selbstlokalisierung (Bandmasse +6 Größenordnungen),
Übergang zu √3×√3-Ordnung, gemessen am Drei-Zustands-Potts-Modell.
Alle Zitate wörtlich [Q].

**Vier strukturelle Parallelen, alle [S]:**
1. Frobenius-Orbits — dreizählige Struktur des Kagome-Dreiecks ↔ φ: x↦x³ der Ordnung 3
2. Drei-Zustands-Potts = GF(3) = Fixkörper des Frobenius
3. Masse = eingefrorene kinetische Energie (Selbstfalle ↔ T̃·m = 1)
4. π-Fluss = Berry-Phase = Wicklungszahl (Dok. 314)

Gemeinsame algebraische Wurzel aller vier: der Frobenius-Automorphismus der Ordnung 3.
Abschnitt „Was nicht übereinstimmt" enthalten.

**Prüfskript:** `2/python/Dok361_Skripte/pruef_361_kagome_frobenius.py` — 20/20.

**Register:** kein Eintrag (Einordnung, keine Korrektur älterer Dokumente).

---

## 12. September 2026 — Dok. 362: Die BAW-Ising-Maschine als Resonanzrechner

### Dok. 362 — Vadde et al. (Commun. Phys. 9:290) im Licht von Dok. 173, 328, 343 (De/En, je 9 S.)

Fallstudie zu Vadde, Ovcharov, González, Khymyn, Litvinenko, Åkerman
(Commun. Phys. 9:290, 8. Sept. 2026, CC-BY, DOI 10.1038/s42005-026-02846-7):
zeitmultiplexte Ising-Maschine mit 2048 Spins auf zwei Quarz-Volumenschallwellen-
Verzögerungsleitungen; MAX-CUT, Number Partitioning, Sudoku. Alle Zitate wörtlich [Q].

**Fünf Einordnungen, alle [S]:**
1. Spin = Phase 0/π eines Pulses ↔ Ising-Maschine = Resonator (Dok. 173)
2. Barkhausen „Phase = 2πn" ↔ Wicklungsquantisierung auf S¹ (Dok. 314)
3. PSA bei 2ω → {0,π} ↔ Z₂-Fixpunkte {+1,−1} (Dok. 339/336);
   Pumpen bei 3ω ergäbe Z₃/Potts-Maschine
4. Kopplung 5–30 % mit Chaosgrenze ↔ Adler-Regime (Dok. 328)
5. **Auflösungsboden (quantitativ deutlichste Einordnung):** 99,9 %-Näherungen zuverlässig,
   exakte Lösungen (E = 0) mit wachsender Problemgröße nicht mehr (Fig. 5b: ~90 % bei 32
   Zahlen → ~0 bei 2048); Sudoku bei 99,42 % Grundzustandsenergie noch ungültig
   ↔ N_max ≈ 1/ε (Dok. 343 §G′)

**Was nicht übereinstimmt:** klassischer RF-Oszillator (kein Quantenanspruch); ein Zyklus
statt vier; keine Parameteroptimierung in den Benchmarks; 2⁻¹⁵ ≈ 3·10⁻⁵ liegt nur zufällig
in der Größenordnung von ξ — ausdrücklich kein Zusammenhang behauptet.

**Prüfskript:** `2/python/Dok362_Skripte/pruef_362_bawim_zahlen.py` — 23/23.

**Register:** kein Eintrag (Einordnung, keine Korrektur älterer Dokumente).

---

## 13./14. September 2026 — Dok. 363: Hodge-Theorie auf T⁴/Z₃ im Rahmen der FFGFT

### Dok. 363 — Hodge-Theorie auf T⁴/Z₃ im Rahmen der FFGFT (De 9 S., En 8 S.)

Titel am 14.9. geändert (ursprünglich „Die Hodge-Vermutung und die T⁴/Z₃-Geometrie"):
der alte Titel legte einen Beitrag zur allgemeinen Hodge-Vermutung nahe, der nicht
geliefert wird; der neue benennt Spezialfall und tatsächlichen Inhalt (Galois-Struktur).

Anlass: die Millennium-Probleme in der Diskussion um den Navier-Stokes-Forcing-Beweis
(Sept. 2026). Für die FFGFT-Basisgeometrie T⁴/Z₃ wird die Hodge-Vermutung geschlossen.

**Fünf Sätze:**
- **Satz A [E]:** T⁴ als komplexer 2-Torus = abelsche Fläche → Hodge-Vermutung bekannt
  (Lefschetz (1,1), H^{2,2} durch Fundamentalklasse)
- **Satz B [B]:** die 9 Z₃-Fixpunkte sind algebraische 0-Zykel; Witt-Paare (Dok. 341):
  gerade Indizes = Fixpunkte, ungerade = Dreier-Orbits
- **Satz C [B]:** Frobenius x↦x³ auf GF(27)* = algebraischer Frobenius auf H¹_ét
  (Eigenwerte = 26. Einheitswurzeln; Gal(GF(27)/GF(3)) ≅ Z₃)
- **Satz D [B]:** Sektorpaarung (Dok. 343 Satz D) = Hodge-Symmetrie H^{p,q} ↔ H^{q,p};
  f₁↔f₂ und f₃↔f₄
- **Satz E [B]:** die 8 irreduziblen Kubiken über GF(3) (Dok. 342) bilden eine
  Q-Basis der algebraischen Zykel

**Hauptsatz [B]:** Alle Hodge-Klassen auf T⁴/Z₃ sind rationale Linearkombinationen
algebraischer Zykel. Das allgemeine Millennium-Problem (beliebige glatte projektive
Varietäten) ist davon **nicht** berührt. Keine Singularitäten in der FFGFT-Lesart:
FFGFT arbeitet auf dem glatten T⁴ mit Z₃ als Gittersymmetrie der Moden (Dok. 314);
der Quotient hätte nach Dok. 330 (Eigenwerte {ω,ω²}, det = 1 ⇒ SU(2)) nur A₂-Punkte,
krepant auflösbar zur K3-Fläche — in beiden Lesarten kein Hindernis [B/E].
Chen–Ruan-Erweiterung [S]. §8 „Prämisse und Repräsentationsebene": alle Sätze
sind Typ-III-Übersetzungen (Dok. 270/330) — Galois-Sprache ↔ Hodge-Sprache, bijektiv,
verlustfrei; keine Typ-I/II-Operation, keine Aussage über Beobachtbarkeit einzelner Zykel
(Projektionstheorie Dok. 285/330/333).

**Lesehilfe zu Dok. 343/344 (keine Korrektur):** „Sektorpaarung k↦−k" ist die Inversion
g^k↦g^{−k} (Exponentennegation in Z₂₆), nicht die Körpernegation e↦−e = e·g¹³.
Letztere schickt jeden Ord.-26-Orbit auf einen Ord.-13-Orbit und wäre keine Paarung
innerhalb der primitiven Klassen. In Dok. 343/344 ist k der Exponent — dort korrekt.

**Prüfskripte:** `2/python/Dok363_Skripte/pruef_363_hodge_t4z3.py` (23/23),
`pruef_363b_luecken.py` (38/38: Ordnungsklassifikation aller 8 Kubiken direkt berechnet;
Frobenius als Ringautomorphismus auf allen 676/729 Paaren; Negation vs. Inversion auf den
Orbits; Z₃-Wirkung in SU(2), 9 Fixpunkte nach Lefschetz), `run_all_363.sh`.

**Register:** kein Eintrag (neues Resultat, keine Korrektur älterer Dokumente, kein als
offen geführter Punkt geschlossen).
