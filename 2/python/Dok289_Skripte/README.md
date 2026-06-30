# Dok 289 — Skripte (Magnitude/Phase-Karte der vier Fermion-Sektoren)

Reproduzierbare numpy-only-Skripte zu Dok. 289, Seed 20780458. `python3 <datei>.py`.

- `koide_q_sektoren.py` — Koide Q und r=√(6Q−2) für die drei bildbaren Triplette:
  geladene Leptonen (Q=2/3, r=√2, speziell), up-Quarks (Q≈0,85, r≈1,76), down-Quarks
  (Q≈0,73, r≈1,54); Neutrinos nicht bildbar (nur Δm² gemessen). Quarkwerte MS-bar,
  skalenabhängig — nur Illustration.
- `neutrino_allpass.py` — Neutrinos als reiner Allpass-Sektor: entartete Massen =
  flaches Betragsspektrum (trägt keine Oszillation); die benötigten Δm²-Oszillations-
  phasen bei Benchmark-L/E (T2K-artig: Δφ31≈1,557 rad) als konkrete, falsifizierbare
  Testforderung an FFGFTs geometrische Phase; Allpass-Demo |H|=1.
- `ckm_pmns_kontrast.py` — CKM- vs PMNS-Mischung als Off-Diagonal-Gewicht der |U|²-Matrix:
  CKM 0,035 (klein) vs PMNS 0,554 (groß), Faktor ~16 → Quarks betrags-dominiert,
  Neutrinos phasen-dominiert.

## Befund
Die Magnitude/Phase-Zerlegung gibt eine gemeinsame Karte: nur die geladenen Leptonen
sitzen am speziellen Punkt r=√2; Quarks betrags-dominiert daneben (nicht speziell,
skalenabhängig); Neutrinos als phasen-dominierter Allpass-Sektor. FFGFTs eigene
Neutrino-Hypothese (Entartung + geometrische Phasen-Oszillation) erhält damit eine
falsifizierbare Form. Ehrlich: Diagnose und Test, keine Massenherleitung (P35); der
Neutrino-Sektor bleibt spekulativ (Dok 007).

---
EN: numpy-only scripts for Doc. 289. Koide Q/r per sector (only charged leptons at the
special r=√2), neutrinos as a pure all-pass/phase sector with a falsifiable Δm² test on
FFGFT's geometric phase, and the CKM/PMNS contrast as magnitude vs phase dominance
(factor ~16). Diagnosis and test, not a mass derivation (P35).
