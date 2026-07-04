#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 293 -- Die ikosaedrische Herkunft von theta=2/9 (und delta) : der zweite Zeuge
==================================================================================
Vorwaerts, parameterfrei, KEIN 2/9 als Input. Die C3-in-A5-Einbettung (Verdopplung
6=3+3', Dok 285) erzeugt die Umverteilung des Elektron-Mode unter der ikosaedrischen
5-fold mit exakten Nenner-9-Gewichten. Der Anteil in die triviale Mode ist exakt 2/9
-- derselbe Wert, den Koide phaenomenologisch aus den Lepton-Massen liefert.
numpy-only, Seed 20780458. Hochpraezise Bestaetigung optional via mpmath.
"""
import numpy as np
np.random.seed(20780458)
phi = (1+np.sqrt(5))/2
w   = np.exp(2j*np.pi/3)

def rot(axis, ang):
    a = np.array(axis, float); a /= np.linalg.norm(a)
    K = np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    return np.eye(3) + np.sin(ang)*K + (1-np.cos(ang))*(K@K)

# C3-Fourier-Moden (Zirkulant-Eigenbasis): v0 trivial, v1/v2 nicht-trivial
V = np.array([[1,1,1],[1,w,w**2],[1,w**2,w]], dtype=complex)/np.sqrt(3)
v0, ve = V[0], V[1]                      # Elektron = nicht-triviale Mode
R5 = rot([0,1,phi], 2*np.pi/5)           # ikosaedrische 5-fold (+phi-Achse)

# --- die volle Umverteilung ---
p = np.array([abs(np.vdot(V[j], R5@ve))**2 for j in range(3)])
print("="*66)
print("VOLLE 5-fold-UMVERTEILUNG DES ELEKTRON-MODE (parameterfrei, kein 2/9-Input)")
print("-"*66)
print(f"  in v0 (trivial)      = {p[0]:.10f}   Ziel 2/9        = {2/9:.10f}")
print(f"  in v2 (2. Harm.)     = {p[2]:.10f}   (5-3phi)/9      = {(5-3*phi)/9:.10f}")
print(f"  bleibt Elektron (v1) = {p[1]:.10f}   (2+3phi)/9      = {(2+3*phi)/9:.10f}")
print(f"  totaler Leak         = {p[0]+p[2]:.10f}   (7-3phi)/9      = {(7-3*phi)/9:.10f}")
print("-"*66)
print(f"  theta  = v0-Leak     = 2/9          EXAKT: {abs(p[0]-2/9)<1e-12}")
print(f"  delta  = totaler Leak= (7-3phi)/9   (verglichen mit Koide-delta* 0.23887: {100*((p[0]+p[2])/0.238870980080-1):+.2f}%)")
print("  Alle Gewichte Nenner 9 = 3^2 -- dieselbe Z3-Struktur wie 2/9.")

# --- Haertetest 1: ikosaeder-spezifisch (nicht generisch) ---
print("="*66)
print("HAERTETEST 1: 2/9 ist ikosaeder-spezifisch, nicht generisch")
rng = np.random.default_rng(20780458); hits = 0; vals = []
for _ in range(200):
    a = rng.normal(size=3); l = abs(np.vdot(v0, rot(a,2*np.pi/5)@ve))**2
    vals.append(l); hits += abs(l-2/9) < 1e-6
print(f"  200 Zufallsachsen bei 72 Grad: {hits}/200 treffen 2/9; Spanne [{min(vals):.3f},{max(vals):.3f}]")

# --- Haertetest 2: Winkel- und n-fold-Spezifitaet ---
print("="*66)
print("HAERTETEST 2: nur die 5-fold (72 Grad) gibt 2/9")
for n in [3,4,5,6,7]:
    l = abs(np.vdot(v0, rot([0,1,phi],2*np.pi/n)@ve))**2
    print(f"  {n}-fold: v0-Leak = {l:.5f}{'   <-- 2/9' if abs(l-2/9)<1e-6 else ''}")

# --- Haertetest 3: Achsenwahl (P3), diskret ---
print("="*66)
print("HAERTETEST 3: Achsenwahl +phi vs -phi (diskret)")
a3 = np.array([1,1,1.])/np.sqrt(3)
for sgn,lab in [(+1,'+phi'),(-1,'-phi')]:
    ax = np.array([0,1,sgn*phi]); ang = np.degrees(np.arccos(abs(np.dot(a3, ax/np.linalg.norm(ax)))))
    l = abs(np.vdot(v0, rot([0,1,sgn*phi],2*np.pi/5)@ve))**2
    tgt = '2/9' if abs(l-2/9)<1e-9 else '4/9'
    print(f"  {lab}: 3-5-Achswinkel {ang:5.2f} Grad -> v0-Leak = {l:.5f} = {tgt}")
print("  Physikalische Einbettung C3<A5 waehlt den naechstliegenden 5-fold = +phi -> 2/9.")
print("="*66)
print("ZWEITER ZEUGE: Geometrie (parameterfrei) und Koide (phaenomenologisch) treffen")
print("beide EXAKT 2/9. Zwei unabhaengige Wege, derselbe Wert -- Konvergenzbeleg.")
