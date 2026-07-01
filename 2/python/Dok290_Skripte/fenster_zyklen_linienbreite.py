#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Fensterwirkung, Zyklenzahl und natuerliche Linienbreite.

Ein zeitlich begrenztes Paket behaelt den DEFINITEN Traeger f0; die Begrenzung
erzeugt ein Band Delta_f ~ 1/Delta_t (Fensterwirkung), kein neues Spektrum.

Kernfrage: ist die Zyklenzahl frequenzunabhaengig?
  N = f * Delta_t.
  - festes Zeitfenster Delta_t  -> N ~ f      (frequenz-ABHAENGIG)
  - feste Zyklenzahl N          -> Delta_f/f = 1/N  (frequenz-UNABHAENGIG)
Die dimensionslose Zyklenzahl N ist der skalen-invariante Kennwert; Delta_t (s)
und Delta_f (Hz) sind dimensional und skalieren mit f.

Photon aus Energiesprung + endliche Lebensdauer tau = natuerliche Linienbreite:
  gedaempfte Schwingung exp(-t/2tau) cos(w0 t) -> Lorentz, Q = w0*tau = 2*pi*N.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)
c = 2.99792458e8

print("(A) festes Zeitfenster dt -> N = f*dt skaliert mit f")
dt = 1e-9
for name, f in [("Radio 1 GHz", 1e9), ("THz", 1e12), ("optisch 600 THz", 6e14)]:
    print(f"   {name:18s} dt={dt*1e9:.0f} ns -> N = {f*dt:11.3e} Zyklen")
print("   -> bei festem Fenster: mehr Zyklen bei hoeherer Frequenz.")
print()

print("(B) feste Zyklenzahl N -> Delta_f/f = 1/N (frequenz-UNABHAENGIG)")
for N in [5, 10, 100]:
    print(f"   N={N:4d}: Delta_f/f = 1/N = {1/N:.4f}")
    for name, f in [("Radio 1 GHz", 1e9), ("optisch 600 THz", 6e14)]:
        dt = N/f; df = 1/dt
        print(f"       {name:18s} dt=N/f={dt:.3e} s, df={df:.3e} Hz, df/f={df/f:.4f}")
print("   -> die ZYKLENZAHL ist der dimensionslose, skalen-invariante Kennwert.")
print()

print("(C) Energiesprung + Lebensdauer tau = natuerliche Linienbreite")
tau = 10e-9; f0 = 5e14; w0 = 2*np.pi*f0
N = f0*tau; Q = w0*tau; df = f0/Q
print(f"   tau={tau*1e9:.0f} ns, f0={f0:.2e} Hz:")
print(f"     N = f0*tau = {N:.3e} Zyklen,  Q = w0*tau = 2*pi*N = {Q:.3e}")
print(f"     natuerliche Linienbreite df = f0/Q = {df:.3e} Hz ({df/1e6:.1f} MHz)")
print(f"     fraktional df/f0 = 1/Q = {1/Q:.2e}")
print("   -> definiter Traeger (Energiesprung) + Fenster (Lebensdauer) = Band.")
print()
print("Befund: der absolute, frequenz-unabhaengige Gehalt ist die dimensionslose")
print("        Zyklenzahl N (bzw. df/f=1/N, Q=2*pi*N); dt, df, E sind dimensionales")
print("        Beiwerk und skalieren mit dem Traeger.")
