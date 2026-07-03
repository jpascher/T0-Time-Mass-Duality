#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Allpass und die drei Kanaele -- numerisch, fuer die Z3-Orbit-Winkel {1/9,2/9,4/9}.

Ein Allpass (Blaschke-Produkt) B_theta(z) = prod_k (z^-1 - conj(a_k))/(1 - a_k z^-1),
mit Polen a_k = r*exp(i(theta + 2pi k/3)) (Z3-symmetrisch, um Basiswinkel theta rotiert).

Gezeigt wird die Drei-Wege-Aufspaltung:
  (1) BETRAG    |B_theta| = 1 ueberall            -> blind gegen theta
  (2) WINDUNG   (1/2pi) * Gesamt-Phasenhub = 3    -> flach-topologisch, blind gegen theta
  (3) PHASE     arg B_theta(omega) am Referenzpunkt -> traegt theta, unterscheidet den Orbit

Das ist die Eliminationskette am Allpass: Betrag und ganzzahlige Windung koennen 2/9
nicht von 1/9, 4/9 trennen; nur das stetige (dynamische) Phasenprofil kann es.
Es ist eine STRUKTUR-Illustration, keine Herleitung des Wertes 2/9.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

r = 0.5                                   # Polradius (|a|<1, stabil)
w = np.linspace(0, 2*np.pi, 200001)       # Frequenzachse (feines Gitter)
z = np.exp(1j*w)

def allpass(theta, r=r):
    a = r*np.exp(1j*(theta + 2*np.pi*np.arange(3)/3))   # drei Z3-Pole
    B = np.ones_like(z)
    for ak in a:
        B *= (z**-1 - np.conj(ak))/(1 - ak*z**-1)
    return B

orbit = {"1/9": 1/9, "2/9": 2/9, "4/9": 4/9}
print("Allpass B_theta, Z3-Pole (r=0.5), Orbit-Winkel in rad")
print("="*66)
print(f"{'theta':>6} | {'max||B|-1|':>12} | {'Windung':>8} | {'arg B(0) [rad]':>15} | {'Gruppenlauf@0':>13}")
print("-"*66)
results={}
for name,th in orbit.items():
    B = allpass(th)
    mag_err = np.max(np.abs(np.abs(B)-1))                 # (1) Betrag = 1?
    phase = np.unwrap(np.angle(B))
    winding = (phase[0]-phase[-1])/(2*np.pi)              # (2) Windung (Vorzeichen: fallend)
    argB0 = np.angle(allpass(th, r)[0])                   # (3) Phase am Referenzpunkt omega=0
    # Gruppenlaufzeit -d(arg)/d(omega) am Referenzpunkt
    gd = -(phase[1]-phase[0])/(w[1]-w[0])
    results[name]=(mag_err,winding,argB0,gd)
    print(f"{name:>6} | {mag_err:12.2e} | {winding:8.3f} | {argB0:15.4f} | {gd:13.4f}")

print("-"*66)
print("(1) Betrag: alle |B|=1 bis ~1e-15  -> MAGNITUDE ist counter-blind.")
print("(2) Windung: fuer alle theta = 3 (drei Pole) -> FLACHE TOPOLOGIE ist counter-blind.")
print("(3) arg B(0) / Gruppenlaufzeit: verschieden fuer 1/9, 2/9, 4/9")
print("    -> nur das stetige (DYNAMISCHE) Phasenprofil traegt theta.")
print()
# Symmetrischer (Betrags-)Funktional vs. Phasen-Funktional
print("Kontrast: ein SYMMETRISCHER Funktional vs. ein PHASEN-Funktional")
for name,th in orbit.items():
    B=allpass(th)
    sym = np.sum(np.abs(B)**2)*(w[1]-w[0])/(2*np.pi)      # int |B|^2 -- betrags/energie
    argref = np.angle(allpass(th,r)[0])            # phase am referenzpunkt
    print(f"  theta={name:>4}:  int|B|^2/2pi = {sym:.6f} (gleich!)   arg B(0) = {argref:+.4f} (verschieden)")
print()
print("Fazit: 2/9 ist im Betrag und in der ganzzahligen Windung NICHT von 1/9,4/9")
print("zu trennen; die Distinktion lebt allein im dynamischen Phasenprofil des Allpass.")
print("Zum Auswaehlen von 2/9 braucht es eine dynamische Phasen-Referenz (Holonomie/Carrier)")
print("-- nicht ableitbar aus Betrag oder Windungszahl. (Struktur, kein Wert-Beweis.)")
