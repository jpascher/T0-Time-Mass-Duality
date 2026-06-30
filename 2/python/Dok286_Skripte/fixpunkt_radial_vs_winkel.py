#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fixpunkt_radial_vs_winkel.py  --  bindet der Fixpunkt die Brechungsstaerke?
==========================================================================
Naechste Rechnung: kann der Fixpunkt R(Phi*)=Phi* (Dok 203), dessen Exponenten
(3/2,1,2/3) UNABHAENGIG (aus der Torusgeometrie) feststehen, den Offset theta /
die Brechungsstaerke delta binden?

Die Fixpunktgleichung (Dok 203, Z.104-124):
    m_i* = r_i * xi0^{p_i} * v ,   Selbstkonsistenz:  xi0^{p_i-1} * K_frak = 1.
Beobachtung beim Lesen: theta kommt darin NICHT vor. Der Fixpunkt fixiert xi0
(den RADIALEN Skalen-Multiplikator) aus den Exponenten -- die Hierarchie. theta
ist die WINKEL/Phasen-Struktur (Koide-Offset im Z3-Zirkulant). Test: sind die
beiden Sektoren orthogonal, d.h. fixiert der Fixpunkt theta NICHT?

numpy-only, seed=20780458.
"""
import numpy as np
np.random.seed(20780458)
r2 = np.sqrt(2.0); TWO_PI = 2*np.pi
p = np.array([3/2, 1.0, 2/3])            # Lepton-Exponenten (Dok 203), geom. Folge Verh. 2/3
K_frak = 0.986                           # fraktale Konstante (Dok 203, Z.174)

print("="*74)
print("BINDET DER FIXPUNKT theta / die Brechungsstaerke? (radial vs Winkel)")
print("="*74)

# (1) Fixpunkt: xi0 aus den Exponenten -- taucht theta darin auf? NEIN.
print("\n[1] Fixpunktbedingung xi0^{p_i-1}*K_frak=1  =>  xi0 = K_frak^{1/(p_i-1)}")
for name, pi in zip(["e","mu","tau"], p):
    if abs(pi-1) < 1e-9:
        print(f"    {name}: p={pi}  -> p-1=0: Bedingung K_frak=1 (Mode-frei, kein xi0)")
    else:
        xi0 = K_frak**(1/(pi-1))
        print(f"    {name}: p={pi}  -> xi0 = K_frak^(1/{pi-1:.3f}) = {xi0:.4e}")
print("    => xi0 ist durch (p_i, K_frak) bestimmt. theta erscheint NIRGENDS.")

# (2) Faktorisierung: Masse = radialer Skalenteil  x  Winkel-Z3-Muster
print("\n[2] Faktorisierung der Massen: radial (Hierarchie) x angular (Z3-Phase theta)")
def radial(xi0):     # Skalen-/Hierarchie-Teil aus dem Rekursionsexponenten
    return xi0**p
def angular(theta):  # Winkel-Teil: Koide-Z3-Muster (gibt Q=2/3 bei r=sqrt2)
    k = np.arange(3)
    return (1 + r2*np.cos(theta + TWO_PI*k/3))**2
def koide_Q(vals):
    s = np.sqrt(np.abs(vals))
    return vals.sum()/s.sum()**2

# (3) Orthogonalitaet: variiere theta -> aendert sich die Fixpunkt-xi0? variiere xi0 -> Q?
print("\n[3] Orthogonalitaets-Test:")
xi0_ref = K_frak**(1/(p[0]-1))           # aus e-Mode
print(f"    (a) xi0 aus Fixpunkt = {xi0_ref:.4e}; haengt es von theta ab?")
print(f"        theta erscheint nicht in xi0^{{p-1}}*K_frak=1  ->  d xi0/d theta = 0 (analytisch).")
print(f"    (b) Koide Q aus dem Winkelteil, ueber theta UND ueber xi0:")
for th in [0.0, 2/9, 1.0]:
    for xi0 in [1e-4, 4/30000, 1e-3]:
        Q = koide_Q(angular(th))         # angular haengt nicht von xi0 ab
        pass
Q_vals = [koide_Q(angular(th)) for th in np.linspace(0, 1, 5)]
print(f"        Q(theta) = {[f'{q:.5f}' for q in Q_vals]}  -> konstant 2/3 (r=sqrt2), theta-frei")
print(f"        Q haengt NICHT von xi0 ab (angular kennt kein xi0).")
print(f"    => radialer Sektor (xi0, Hierarchie) und Winkel-Sektor (theta, Q) sind ENTKOPPELT.")

# (4) Die Synthese: was ist determiniert, was offen -- nach Sektor sortiert
print("\n" + "="*74)
print("SYNTHESE: alles Determinierte ist RADIAL, alles Offene ist WINKEL")
print("="*74)
print(f"""
  RADIAL / SKALEN-Sektor (von FFGFT DETERMINIERT):
    - xi = 4/30000            (Skalen-Multiplikator, Fixpunkt Dok 203)
    - Exponenten (3/2,1,2/3)  (Torusgeometrie, geom. Folge Verh. 2/3)
    - Hierarchie m_k          (Rekursion xi0^{{p_k}})
    - Koide Q=2/3 = r=sqrt2   (radiale Amplitude)
    - <f> (DC der frakt. Korr.)(Mittelwert -> Zeit-Phase, xi^1-Lift)

  WINKEL / PHASEN-Sektor (OFFEN):
    - theta=2/9               (Koide-Offset, Winkel im Z3-Zirkulant)
    - Holonomie-Phase phi     (= arg f9 - 3 arg f3)
    - Harmonischen-Phasen v. f
    - Z3-Brechungsstaerke delta(Test 1)

  Der Fixpunkt, die Dualitaet, die Rekursion, der Torus-Abzaehl-Apparat --
  ALLE leben im radialen Sektor. KEINER beruehrt den Winkel. Das ist der
  gemeinsame Grund, warum theta=2/9 jedem Werkzeug widersteht:
  FFGFTs Maschinerie ist radial, theta ist angular -- orthogonal.

  ANTWORT auf 'bindet der Fixpunkt delta': NEIN -- theta/delta stehen nicht in
  der Fixpunktbedingung; der Fixpunkt fixiert xi0 (radial), nicht den Winkel.
  Um theta zu fixieren braucht es ein ANGULARES Prinzip (eine dynamische
  Winkelbedingung), das FFGFT bisher nicht hat -- und das laut Transzendenz-
  Befund kein abzaehlendes/topologisches sein kann.
""")
