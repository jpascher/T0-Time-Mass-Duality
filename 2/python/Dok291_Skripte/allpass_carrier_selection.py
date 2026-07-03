#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Illustrative selecting mechanism: eine dynamische Phasen-Referenz (Carrier-Holonomie)
greift EINEN Orbit-Member heraus -- Vorschau auf das, was BD17A leisten muesste.

WICHTIG (P35): rein illustrativ. Es zeigt die FORM des Auswahlmechanismus (externe
dynamische Phase -> Basin-Auswahl). Es leitet den Wert 2/9 NICHT her, behauptet NICHT,
dass die Carrier-Holonomie diesen Wert hat, und modelliert NICHT Marcels tatsaechlichen
Carrier (Nicht-Zirkularitaet).

Aufbau:
  - Die drei Z3-Orbit-Winkel {1/9,2/9,4/9} haben je eine Allpass-Phase psi_a (aus
    allpass_theta.py, am Referenzpunkt omega=0).
  - Ein Carrier akkumuliert eine Holonomie Phi (eine dynamische Phase).
  - Kopplung: der Carrier phasen-lockt auf den NAECHSTEN Orbit-Member (min. Phasen-
    Mismatch) -- Standard-Locking an die naechste Mode.
  - Ergebnis: jeder Member hat ein Basin; 2/9 wird ausgewaehlt <=> Phi liegt im 2/9-Basin.
    Welches Basin der Carrier trifft, ist EXTERNE, kontingente Eingabe -- nicht von FFGFT
    fixiert. Genau das muesste BD17A HLV-intern liefern.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

r = 0.5
zref = np.exp(1j*0.0)   # Referenzpunkt omega=0

def allpass_phase(theta, r=r):
    a = r*np.exp(1j*(theta + 2*np.pi*np.arange(3)/3))
    B = np.prod((zref**-1 - np.conj(a))/(1 - a*zref**-1))
    return np.angle(B)

orbit = {"1/9":1/9, "2/9":2/9, "4/9":4/9}
psi = {name: allpass_phase(th) for name,th in orbit.items()}
print("Allpass-Phasen der Orbit-Member (Referenzpunkt omega=0):")
for name,p in psi.items(): print(f"   psi({name}) = {p:+.4f} rad")
print()

names = list(orbit); vals = np.array([psi[n] for n in names])

def selected(Phi):
    # naechster Orbit-Member (zirkulaere Distanz)
    d = np.angle(np.exp(1j*(vals-Phi)))
    return names[np.argmin(np.abs(d))]

# Basins durch feinen Sweep
Phi_grid = np.linspace(-0.2, 0.5, 700001)
sel = np.array([selected(P) for P in Phi_grid])
print("Basins (Phi-Bereich, der jeden Member auswaehlt):")
basins={}
for n in names:
    mask = sel==n
    lo, hi = Phi_grid[mask].min(), Phi_grid[mask].max()
    basins[n]=(lo,hi)
    print(f"   {n}:  Phi in [{lo:+.4f}, {hi:+.4f}]  (Breite {hi-lo:.4f} rad)")
print()
lo2,hi2 = basins["2/9"]
print(f"==> Der Carrier waehlt 2/9  <=>  seine Holonomie Phi in [{lo2:+.4f}, {hi2:+.4f}] rad.")
print(f"    Mittelpunkte der Nachbarn: ({(psi['1/9']+psi['2/9'])/2:.4f}, {(psi['2/9']+psi['4/9'])/2:.4f})")
print()

# Kontroll-Check: eine ZUFAELLIGE Carrier-Holonomie -- wie oft 2/9?
Nrand=100000
Phir = np.random.uniform(vals.min()-0.05, vals.max()+0.05, Nrand)
hits = np.mean([selected(P)=="2/9" for P in Phir[:2000]])  # Stichprobe
print(f"Zufaellige Phi (gleichverteilt ueber den Orbit-Bereich): P(2/9) ~ {hits:.2f}")
print("   -> ~1/3, wie erwartet: ohne Grund landet der Carrier nicht bevorzugt bei 2/9.")
print()
print("FORM des Mechanismus (illustrativ):")
print("  - Auswahl ist KONTINGENT auf die externe dynamische Phase Phi (Holonomie).")
print("  - 2/9 hat ein eigenes Basin wie jeder Member; nichts an Betrag/Windung bevorzugt es.")
print("  - BD17A muesste HLV-INTERN eine Holonomie liefern, die im 2/9-Basin liegt --")
print("    und zwar aus einem erzwungenen HLV-Grund, nicht per Hand (sonst BLOCKED).")
print("  - Analog zur Brechungsbedingung (delta,chi)~(0.24,pi/2): chi IST die Holonomie-Phase.")
print("  (Kein Wert-Beweis, keine Modellierung von HLVs Carrier.)")
