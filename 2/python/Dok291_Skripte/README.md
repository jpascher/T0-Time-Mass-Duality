# Dok 291 -- Skripte: Der dynamische Ort von theta=2/9

Reproduzierbare numpy-only-Skripte (Seed 20780458).

- `forced_vs_contingent.py` -- Q(theta)=2/3 exakt (theta-blind; 2/9 unter dem Q-Bereich
  [1/3,1]); theta*(delta) waldert monoton mit dem freien delta (chi=pi/2: 2/9 bei delta~0.24,
  dtheta*/ddelta~0.31 != 0, erreichter Bereich [0.05,0.52], 2/9 innen); Kontrast c =
  parameterfreier Rand (dc/dlambda=0). Fazit: 2/9 kontingent, nicht erzwungen wie c.

- `allpass_theta.py` -- Z3-symmetrischer Allpass B_theta, drei Kanaele: Betrag |B|=1 und
  Windungszahl=3 (beide counter-blind gegen theta), nur das stetige Phasenprofil
  (arg B(0)=0.093/0.171/0.249; Gruppenlaufzeit) traegt theta. Auch int|B|^2 ist blind.

- `allpass_carrier_selection.py` -- illustrativer Auswahlmechanismus: eine Carrier-Holonomie
  Phi waehlt 2/9 <=> Phi im 2/9-Basin [0.132,0.210]; zufaelliges Phi trifft 2/9 mit ~1/3.
  chi ist die Holonomie-Phase, delta ihre freie Tiefe. Struktur-Illustration, kein Wert-Beweis.

Alle drei stuetzen die Bilanz: die Selektion von 2/9 lebt allein im dynamischen Phasenkanal
(Holonomie), nicht im Betrag und nicht in einer flachen Windungszahl. Die offene Frage ist, ob
die T^4-Topologie die Holonomie-Phase chi aus einem Fixpunkt erzwingt (BD17A).

## ffgft_stage10_verdict_harness.py (eingefroren 2. Juli 2026)

FFGFT-seitiges Verdikt-Harness fuer Marcels Stage-10-Lauf (blinder
theta*=2/9-Vergleich mit der eingefrorenen Stage-9-Klasse). Gebaut und
eingefroren VOR Ankunft der Stage-10-Daten, damit keine Auswertungswahl
post hoc bleibt. Kodiert nur den symmetrischen Lock: Extraktor
theta_gamma = 1/2 Arg det W_gamma(C_e) mod 2pi/3 (Radiant), Ziel 2/9;
Primaerkriterium = naechstes-Orbit-Glied-Klassifikation {0, 1/9, 2/9, 4/9};
Verdikt ADMITTED / RESIDUAL / BLOCKED wie im Skriptkopf definiert.
Selbsttest (synthetisch, seed 20780458): BESTANDEN (3/3).
Eingabe: CSV (model,seed,theta_gamma) oder JSON.
SHA256 (Lock-Nachweis): 99e11399f23377702c5878784d791f8fc90a350e7999f8c2906bf99221aab246
Aenderungen nach Dateneingang sind unzulaessig (Lock-Bruch, im Ledger zu vermerken).
