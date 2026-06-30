#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 288 -- Hebel 2: Koide Q in zwei Parseval-Zeilen, manifest phasenunabhaengig.

Mit sqrt(m_k) = Eigenwerte des Z3-Zirkulants (= DFT von c) gilt nach Parseval
    sum_k sqrt(m_k) = 3 * c_0                     (nur der DC-Term)
    sum_k m_k       = 3 * sum_j |c_j|^2           (Parseval)
also
    Q = sum m / (sum sqrt m)^2 = 3*sum|c_j|^2 / (3 c_0)^2.
Mit c_0 = 1 und |c_1|^2 = |c_2|^2 = (r/2)^2 = 1/2  ->  Q = 6/9 = 2/3,
und das haengt NUR an r (Betrag), nicht an theta (Phase).

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

w = np.exp(2j*np.pi/3)

def koide_Q(r, th):
    c = np.array([1.0, (r/2)*np.exp(1j*th), (r/2)*np.exp(-1j*th)])
    lam = np.array([sum(c[j]*w**(j*k) for j in range(3)) for k in range(3)]).real
    m, sqm = lam**2, lam
    Q_direct = m.sum() / sqm.sum()**2
    # Parseval-Kurzform:
    Q_parseval = (3*np.sum(np.abs(c)**2)) / (3*c[0].real)**2
    return Q_direct, Q_parseval

r = np.sqrt(2)
Qd, Qp = koide_Q(r, 2/9)
print(f"Q direkt      = {Qd:.6f}")
print(f"Q Parseval    = {Qp:.6f}   (2/3 = {2/3:.6f})")
print()

# Phasenunabhaengigkeit explizit: Q ueber ganz theta
ths = np.linspace(0, 2*np.pi, 25)
Qs = [koide_Q(r, t)[0] for t in ths]
print(f"Q ueber theta in [0,2pi):  min..max = {min(Qs):.6f} .. {max(Qs):.6f}")
print("-> Q ist exakt phasenunabhaengig; nur der Betrag r=sqrt(2) erzeugt Q=2/3.")
print()

# Kontrolle: anderer Betrag -> anderes Q (Q haengt am Betrag)
for rr in [1.0, np.sqrt(2), 1.6]:
    print(f"  r = {rr:.4f}  ->  Q = {koide_Q(rr, 2/9)[0]:.6f}")
print()
print("Hebel: der radial/angular-Schluss faellt als triviale Parseval-Folge heraus.")
