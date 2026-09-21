#!/usr/bin/env python3
"""
ffgft_371_faktor_vier_drittel.py — Prüfskript zu Dok. 371
Der Faktor 4/3: Kugelvolumen, Casimir-Operatoren, elektromagnetische
Masse, 3-4-5-Dreieck und xi.

Alle Prüfungen exakt (Fraction) oder numerisch mit expliziter Toleranz.
"""
from fractions import Fraction as F
from math import pi, sin, cos, atan, degrees, sqrt
import numpy as np

ok_all = True
def check(name, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print(f"[{'OK' if cond else 'FEHLER'}] {name}  {detail}")

print("=== P1 Kugelvolumen: V / (pi r^3) = 4/3 [E] ===")
# V = (4/3) pi r^3 ; Archimedes: V = (1/3) r S mit S = 4 pi r^2
r = F(1); S_over_pi = 4 * r**2; V_over_pi = F(1,3) * r * S_over_pi
check("V/(pi r^3) = 4/3", V_over_pi == F(4,3), str(V_over_pi))

print("\n=== P2 Casimir C2(SU(N), fund) = (N^2-1)/(2N) [E] ===")
C2 = lambda N: F(N*N - 1, 2*N)
check("C2(SU(2)) = 3/4", C2(2) == F(3,4), str(C2(2)))
check("C2(SU(3)) = 4/3", C2(3) == F(4,3), str(C2(3)))
check("C2(SU(2))*C2(SU(3)) = 1 (Kehrwertpaar)", C2(2)*C2(3) == 1)
check("Spin-1/2: s(s+1) = 3/4", F(1,2)*F(3,2) == F(3,4))
check("Nur N=2,3 liefern Kehrwerte: C2(N)*C2(N+1)=1 <=> N=2",
      [N for N in range(2,50) if C2(N)*C2(N+1) == 1] == [2])

print("\n=== P3 Elektromagnetische Masse: Impulsfaktor 4/3 [E] ===")
# Feldimpuls einer langsam bewegten Kugelschale (Abraham/Lorentz):
# p = (eps0/c^2) v * Int (E^2 - E_z^2) dV ; U = (eps0/2) Int E^2 dV
# => p = (4/3) (U/c^2) v  genau dann, wenn Int E_z^2 / Int E^2 = 1/3.
# Winkelmittel von cos^2(theta) über die Kugel: exakt 1/3.
theta = np.linspace(0, pi, 200001)
w = np.sin(theta)
cos2_mean = np.trapezoid(np.cos(theta)**2 * w, theta) / np.trapezoid(w, theta)
check("<cos^2 theta>_Kugel = 1/3 (numerisch)", abs(cos2_mean - 1/3) < 1e-9,
      f"{cos2_mean:.12f}")
faktor = 2 * (1 - cos2_mean)   # p/(U v/c^2) = 2 (1 - 1/3) = 4/3
check("p / (U v / c^2) = 4/3", abs(faktor - 4/3) < 1e-9, f"{faktor:.12f}")
check("Ursache: jede der 3 Feldkomponenten trägt 1/3 der Energie",
      abs(cos2_mean*3 - 1) < 1e-8)

print("\n=== P4 3-4-5-Dreieck [E] ===")
check("3^2 + 4^2 = 5^2", 3**2 + 4**2 == 5**2)
check("tan(alpha) = 4/3, cot(alpha) = 3/4, Produkt 1",
      F(4,3) * F(3,4) == 1)
alpha = atan(4/3)
check("alpha = 53.13 Grad, sin=4/5, cos=3/5",
      abs(sin(alpha) - 0.8) < 1e-12 and abs(cos(alpha) - 0.6) < 1e-12,
      f"alpha = {degrees(alpha):.4f} Grad")
# arithmetische Progression: a, a+d, a+2d rechtwinklig  =>  a = 3d
# a^2 + (a+d)^2 = (a+2d)^2  <=>  a^2 - 2ad - 3d^2 = 0  <=> (a-3d)(a+d)=0
a_over_d = [x for x in range(1, 100) if F(x)**2 + F(x+1)**2 == F(x+2)**2]
check("einziges rechtwinkliges Dreieck in arithm. Folge: a=3d -> 3:4:5",
      a_over_d == [3])
check("Inkreisradius (3+4-5)/2 = 1", F(3+4-5, 2) == 1)
z = complex(2, 1)**2
check("(2+i)^2 = 3+4i", z == complex(3, 4), str(z))
# Berggren: die drei Matrizen aus (3,4,5) erzeugen (5,12,13),(21,20,29),(15,8,17)
A = np.array([[1,-2,2],[2,-1,2],[2,-2,3]])
B = np.array([[1,2,2],[2,1,2],[2,2,3]])
C = np.array([[-1,2,2],[-2,1,2],[-2,2,3]])
root = np.array([3,4,5])
kinder = [tuple(M @ root) for M in (A,B,C)]
check("Berggren-Kinder von (3,4,5): (5,12,13),(21,20,29),(15,8,17)",
      kinder == [(5,12,13),(21,20,29),(15,8,17)], str(kinder))
check("alle Kinder pythagoreisch",
      all(x*x+y*y==zz*zz for x,y,zz in kinder))
# Fixpunkt-Test: ist (3,4,5) Fixpunkt oder Wurzel? Es ist Wurzel:
# keine Matrix bildet ein kleineres Tripel auf (3,4,5) ab (Inverse ganzzahlig, negativ)
inv = [np.linalg.inv(M).round().astype(int) @ root for M in (A,B,C)]
check("(3,4,5) hat kein positives Elterntripel (Wurzel des Baums)",
      all((v <= 0).any() for v in inv), str([tuple(v) for v in inv]))

print("\n=== P5 xi = 4/3 * 10^-4 und Leptonverhältnis (Dok. 006) [K] ===")
xi = F(4,3) * F(1, 10**4)
check("xi = 4/30000", xi == F(4, 30000))
check("1/xi = 7500", 1/xi == 7500)
m_mu_me = float(F(16,5) / F(4,3)) * float(xi)**(-0.5)
exp_ratio = 206.7682830
dev = (m_mu_me/exp_ratio - 1) * 100
check("m_mu/m_e = (16/5)/(4/3) xi^-1/2 innerhalb 1 %", abs(dev) < 1.0,
      f"{m_mu_me:.3f} vs {exp_ratio} ({dev:+.2f} %)")

print("\n=== P6 Der Winkel arctan(4/3) im D-Gitter ===")
import itertools
# (a) unter den kürzesten Vektoren (Norm^2 = 2) tritt er NICHT auf [X]
d3 = [np.array(v) for v in [(1,1,0),(1,-1,0),(1,0,1),(0,1,1)]]
d4 = [np.array(v) for v in [(1,1,0,0),(1,0,1,0),(1,0,0,1),(0,1,1,0),(1,-1,0,0)]]
def winkel(vs):
    out=set()
    for i in range(len(vs)):
        for j in range(i+1,len(vs)):
            c = vs[i]@vs[j]/(np.linalg.norm(vs[i])*np.linalg.norm(vs[j]))
            out.add(round(degrees(np.arccos(c)),4))
    return sorted(out)
w3, w4 = winkel(d3), winkel(d4)
print("   kürzeste Vektoren — D3-Winkel:", w3, " D4-Winkel:", w4)
check("kürzeste Vektoren: 53.13 Grad tritt nicht auf [X]",
      all(abs(x-53.1301) > 0.1 for x in w3+w4))
# (b) auf der Schale Norm^2 = 10 tritt er auf: (3,1,0,0) und (1,3,0,0) [B]
shells = {}
vecs = [np.array(v) for v in itertools.product(range(-3,4), repeat=4)
        if sum(v) % 2 == 0 and 0 < sum(x*x for x in v) <= 12]
for a in vecs:
    for b in vecs:
        na, nb, d = int(a@a), int(b@b), int(a@b)
        if na == nb and d > 0 and F(d*d, na*nb) == F(9,25):
            shells.setdefault(na, (tuple(int(x) for x in a), tuple(int(x) for x in b)))
print("   cos = 3/5 in D4, erste Schale:", shells)
check("erste D4-Schale mit cos=3/5 ist Norm^2 = 10 = |1+3i|^2", min(shells) == 10)
# (c) Ursache: D2 = (1+i) Z[i]; (1+i)(2+i) = 1+3i, (1+i)(2-i) = 3+i
u, v = (1+1j)*(2+1j), (1+1j)*(2-1j)
check("(1+i)(2+i) = 1+3i und (1+i)(2-i) = 3+i", u == 1+3j and v == 3+1j)
cosuv = (u.real*v.real + u.imag*v.imag) / (abs(u)*abs(v))
check("Winkel zwischen ihnen = arccos(3/5) = arctan(4/3)",
      abs(cosuv - 0.6) < 1e-12 and abs(degrees(np.arccos(cosuv)) - degrees(alpha)) < 1e-9)
D2 = [(x,y) for x in range(-6,7) for y in range(-6,7) if (x+y) % 2 == 0]
check("D2 = (1+i) Z[i] (jedes Element durch 1+i teilbar)",
      all(((x+y) % 2 == 0) and ((y-x) % 2 == 0) for x,y in D2))

print("\n=== P7 Strahlungsdruck: (u + p)/u = 4/3 bei p = u/3 [E] ===")
check("Enthalpie-Faktor 1 + 1/3 = 4/3", F(1) + F(1,3) == F(4,3))
check("Impulsmasse eines Photonengases: (4/3) E/c^2 — dieselbe Drittelung wie P3",
      F(4,3) == 2*(1 - F(1,3)))

print("\n" + ("ALLE PRÜFUNGEN BESTANDEN" if ok_all else "MINDESTENS EINE PRÜFUNG FEHLGESCHLAGEN"))
