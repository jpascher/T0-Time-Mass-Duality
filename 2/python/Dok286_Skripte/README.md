# Dok 286 — Skripte (dynamischer Sektor + θ=2/9-Eliminationskette)

Reproduzierbare numpy-Skripte zu Dok. 286 (kinetischer Sektor) und der
θ=2/9-Untersuchung in Dok. 282. numpy-only, Seed 20780458, keine externen
Datensätze. Jedes Skript ist eigenständig ausführbar (`python3 <datei>.py`).

## Kinetischer Sektor (Dok. 286)
- `kinetik_xi_anteil.py` — kinetischer ξ-Anteil, Aufstellung.
- `schliesse_omega.py` — Schließung von ω; das ½ als AM-Seitenband-Faktor.
- `xi1_eigenwert.py` — ξ¹-Anhebung des Nullmodes durch das Dimensions-Defizit.
- `am_seitenband_modelock.py` — AM-Seitenband ½ (solide) + Mode-Locking-Kandidat.

## θ=2/9 — Aufbau (nachrichtentechnische Lesart)
- `z3_modelock_test.py` — Z₃-Protektion: Z₃-Antrieb verbreitert die 3er-Nenner-Zungen
  selektiv (Nenner 9 erklärt; Zähler offen).
- `z3_holonomie_test.py` — eine Holonomie-Phase bricht die 9er-Familie auf; 2/9 ist
  das abspaltende Singulett (1/9, 4/9 bleiben gepaart).
- `eine_fraktale_quelle.py` — eine fraktale Korrektur, zwei orthogonale Phasen:
  Zeit-Phase liest den Mittelwert ⟨f⟩ (DC), Holonomie liest die Harmonischen-Phasen.

## θ=2/9 — Eliminationskette (Dok. 282)
- `kann_topologie_2_9_erzwingen.py` — Transzendenz: 2/9 rad ist transzendent in 2π
  (Lindemann–Weierstrass) → keine Einheitswurzel → kein Abzähl-/Fluss-Mechanismus.
- `einfachstes_prinzip_2_9.py` — der cos3θ-Satz: die gesamte θ-Abhängigkeit läuft nur
  über cos3θ; jedes Z₃-invariante Funktional extremiert bei nπ/3, nie bei 2/9.
- `symmetriebrechung_2_9.py` — das Z₃-Brechen (3′-Kopplung) *erreicht* 2/9, aber bei
  freier Brechungsstärke δ (nicht punkt-hergeleitet).
- `fixpunkt_radial_vs_winkel.py` — der Fixpunkt (Dok. 203) fixiert ξ₀ radial; θ kommt
  in der Fixpunktbedingung nicht vor → radialer und Winkel-Sektor orthogonal.
- `ikosaeder_winkel_2_9.py` — 2/9 rad = 12,73° ist *kein* Ikosaeder-Achsenwinkel
  (streng geprüft; Kontrolle arccos(1/√5)=63,43° trifft C₅–C₅ exakt).

## Befund
Alles, was FFGFT determiniert, ist radial (ξ, Hierarchie, Q=2/3=√2, ⟨f⟩); θ=2/9 ist
angular. Die Elimination zeigt: θ ist nicht symmetrisch (cos3θ), nicht abzählend-
topologisch (Transzendenz), nicht radial (Fixpunkt), nicht statisch-geometrisch
(Ikosaeder). Übrig bleibt die dynamische schief-adjungierte Phase R (HLV-Seite,
BD17A) — die Allpass-/Phasenstufe, die der reellen FFGFT-Rekursion fehlt.

---
EN: numpy-only reproducibility scripts for Doc. 286 (kinetic sector) and the θ=2/9
elimination chain in Doc. 282. Seed 20780458, no external data. The elimination shows
θ=2/9 is not symmetric (cos3θ theorem), not counting-topological (transcendence), not
radial (fixed point), not static-geometric (icosahedral check); the surviving route is
HLV's dynamical skew-adjoint phase R (BD17A) — the all-pass/phase stage absent from the
real-valued FFGFT recursion.
