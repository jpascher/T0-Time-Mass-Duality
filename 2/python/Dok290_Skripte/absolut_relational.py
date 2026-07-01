#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Aufloesung der Spannung absolut/relational.

"Absolut" und "relational" liegen auf verschiedenen Achsen:
  - absolut    = die MENGE/das Mass (dimensionslos, xi-verankert: log2(1/xi))
  - relational = die NATUR eines Datums (Holonomie/Windung: schleifen-/wegabhaengig,
                 kein lokaler Punktwert)
Eine Windungszahl ist das Musterbeispiel fuer BEIDES zugleich:
  (a) relational -- nur als Schleifenintegral definiert, nicht lokal ablesbar;
  (b) absolut    -- eichinvariant und definit (ganzzahlig).
Und die absolute Zahl log2(1/xi) ZAEHLT genau solche relationalen Objekte
(Windungssektoren). Die Absolutheit sitzt im Boden (xi), die Relationalitaet in
den Freiheitsgraden darauf -- kein Widerspruch.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

N = 2000
x = np.linspace(0, 2*np.pi, N, endpoint=False)

def winding(psi):
    ph = np.angle(psi)
    d  = np.diff(np.r_[ph, ph[0]])      # Schleife schliessen
    d  = (d + np.pi) % (2*np.pi) - np.pi # auf (-pi,pi] wickeln
    return np.sum(d)/(2*np.pi)

w_true = 3
s   = 0.8*np.sin(x) + 0.3*np.cos(2*x)    # einwertige, glatte Funktion
psi = np.exp(1j*(w_true*x + s))          # Einheits-Komplexfeld auf dem Kreis

print("(1) relational: die Windung ist ein Schleifenintegral, kein Punktwert")
W = winding(psi)
print(f"    Windungszahl (Schleifenintegral) = {W:.6f} -> {round(W)}")
# lokale Ablesung scheitert: Partialsummen bis zur Haelfte des Kreises
half = winding(np.r_[psi[:N//2], psi[0]])
print(f"    halbe Schleife liefert {half:.3f} -- kein lokaler Punkt legt W fest.")
print()

print("(2) absolut: eichinvariant unter einwertiger Umphasung psi -> psi*exp(i*lam)")
for k in range(3):
    lam = np.random.uniform(0.5, 2.0)*np.sin(np.random.randint(1,5)*x)  # einwertig
    Wg = winding(psi*np.exp(1j*lam))
    print(f"    lam={k+1}: Windung = {round(Wg)}  (unveraendert -- absolut/eichinvariant)")
print()

print("(3) die absolute Zahl zaehlt relationale Objekte (Windungssektoren)")
xi = 4/30000.0; nmax = 1/xi
sectors = 2*nmax + 1
print(f"    n_max ~ 1/xi = {nmax:.0f}; Sektoren |w|<=n_max: {sectors:.0f}")
print(f"    log2(Sektoren) = {np.log2(sectors):.3f} Bit  ~ log2(1/xi) = {np.log2(1/xi):.3f} Bit")
print()
print("Befund: absolut (Menge, xi-Decke) und relational (Natur, Windung/Holonomie)")
print("        sind orthogonal. Eine Windung ist relational definiert UND absolut")
print("        bewertet; die absolute Bit-Zahl zaehlt genau diese relationalen")
print("        Freiheitsgrade. Kein Widerspruch.")
