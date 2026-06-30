#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
am_seitenband_modelock.py  --  Dok 286, nachrichtentechnische Lesart
====================================================================
Zwei Aussagen des dynamischen Sektors, nachrichtentechnisch gerechnet:

  (A)  Das 1/2 in  omega = (xi/2) E0  ist der AM-Seitenband-Faktor.
       Ein Traeger cos(w_c t), amplitudenmoduliert mit Index xi, hat
       Seitenbaender bei Amplitude xi/2  (cos*cos = 1/2(Summe+Differenz)).
       -> reproduziert xi/2 ZWINGEND (solide).

  (B)  theta = 2/9 als Mode-Locking-Verhaeltnis (KANDIDAT).
       Die Sinus-Kreisabbildung  t_{n+1} = t_n + Omega - (K/2pi) sin(2pi t_n)
       rastet auf rationale Rotationszahlen p/q ein (Arnold-Zungen,
       Teufelstreppe). Wir messen die Plateau-Breite bei 2/9 gegen kleine
       Nenner -> zeigt ehrlich: 2/9 ist ein SCHMALERES Plateau.

numpy-only. Reproduzierbar (seed=20780458, Marcels Zenodo-Seed).
"""
import numpy as np

np.random.seed(20780458)
XI = 4/30000.0

# ----------------------------------------------------------------------
# (A) AM-Seitenband: omega = (xi/2) E0  ist das erste Seitenband
# ----------------------------------------------------------------------
def am_sideband(xi, fc=50.0, fm=1.0, fs=4096.0, dur=64.0):
    t = np.arange(0, dur, 1/fs)
    carrier = np.cos(2*np.pi*fc*t)
    signal  = carrier * (1.0 + xi*np.cos(2*np.pi*fm*t))
    # Spektrum
    win = np.hanning(len(t))
    S = np.fft.rfft(signal*win)
    f = np.fft.rfftfreq(len(t), 1/fs)
    amp = np.abs(S)
    # Traeger- und Seitenband-Bins
    def bin_amp(freq):
        k = np.argmin(np.abs(f-freq))
        return amp[k-1:k+2].max()
    a_car = bin_amp(fc)
    a_sb  = 0.5*(bin_amp(fc+fm) + bin_amp(fc-fm))
    ratio = a_sb/a_car
    return ratio

# Skala-unabhaengig: das VERHAELTNIS Seitenband/Traeger = xi/2.
# Bei sehr kleinem xi=4/30000 testen wir die Identitaet analytisch + bei
# einem grossen xi numerisch (FFT-Aufloesung), beide gegen xi/2.
print("="*66)
print("(A) AM-SEITENBAND:  omega = (xi/2) E0  ist das erste Seitenband")
print("="*66)
for xi_test in [0.2, 0.05, 0.01]:
    r = am_sideband(xi_test)
    print(f"  xi={xi_test:6.3f}:  Seitenband/Traeger = {r:.6f}   xi/2 = {xi_test/2:.6f}"
          f"   Abw {abs(r-xi_test/2)/(xi_test/2)*100:5.2f}%")
print(f"\n  Identitaet exakt:  cos(a)*[1+xi*cos(b)]"
      f" = cos a + (xi/2)[cos(a+b)+cos(a-b)]")
print(f"  -> fuer FFGFT xi=4/30000:  omega/E0 = xi/2 = {XI/2:.3e}   (zwingend, kein Fit)")
print(f"     m_window/E0 = xi^2/2 = {XI**2/2:.3e}   (zweites Seitenband / Produkt)")

# ----------------------------------------------------------------------
# (B) Mode-Locking: Rotationszahl der Sinus-Kreisabbildung
# ----------------------------------------------------------------------
def rotation_numbers(Omegas, K, n_trans=600, n_avg=3000):
    """Vektorisiert ueber das gesamte Omega-Gitter (numpy)."""
    Om = np.asarray(Omegas, float)
    t = np.full_like(Om, 0.123)
    c = K/(2*np.pi)
    for _ in range(n_trans):
        t = t + Om - c*np.sin(2*np.pi*t)
        t -= np.floor(t)
    tot = np.zeros_like(Om)
    for _ in range(n_avg):
        tn = t + Om - c*np.sin(2*np.pi*t)
        tot += (tn - t)
        t = tn - np.floor(tn)
    return tot/n_avg

def plateau_width(p, q, K, span=0.05, N=601, tol=2e-4):
    """Breite des Omega-Intervalls, in dem rho == p/q (Teufelstreppe-Stufe)."""
    target = p/q
    Omegas = np.linspace(target-span, target+span, N)
    rho = rotation_numbers(Omegas, K)
    locked = np.abs(rho - target) < tol
    if not locked.any():
        return 0.0
    idx = np.where(locked)[0]
    return (Omegas[idx.max()] - Omegas[idx.min()])

print("\n" + "="*66)
print("(B) MODE-LOCKING:  Arnold-Zungen-Breite bei K=1 (kritisch, volle Treppe)")
print("="*66)
K = 1.0
ratios = [(1,2),(1,3),(2,5),(1,4),(2,9)]
widths = {}
for p,q in ratios:
    w = plateau_width(p,q,K)
    widths[(p,q)] = w
    print(f"  rho = {p}/{q} = {p/q:.4f}:  Plateau-Breite ~ {w:.5f}")
w29 = widths[(2,9)]; w13 = widths[(1,3)]
print(f"\n  Befund: 2/9 ist ein SCHMALERES Plateau als kleine Nenner.")
if w13>0 and w29>0:
    print(f"          Breite(1/3)/Breite(2/9) ~ {w13/w29:.1f}x")
print("  -> ehrlich: Mode-Locking liefert rationale Fixpunkte (Quantisierungsregel),")
print("     aber WARUM gerade 2/9 (Nenner 9) einrastet, bleibt offen. Kandidat, keine")
print("     Herleitung. Das Reframing macht es zur testbaren Oszillator-Frage.")
print("="*66)
