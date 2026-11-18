#!/usr/bin/env python3
"""Prüfskript zu Dok. 398: |psi|^2 als Energiedichte und der Einwand der Selbstwechselwirkung.

Prüft:
1. Gaos Stärkemaße der Selbstwechselwirkung für ein freies Elektron:
   elektrostatisch eps^2 = (4 k e^2 / hbar c)^2 = (4 alpha)^2,
   gravitativ eps^2 = (4 G m_e^2 / hbar c)^2.
2. Coulomb-Selbstenergie der 1s-Dichte des Wasserstoffs, J = 5/8 Hartree = 17,0 eV,
   numerisch integriert, gegen die Bindungsenergie 13,6 eV und die
   Messgenauigkeit der 1S-2S-Linie.
3. Gravitative Selbstenergie derselben Dichte (Schrödinger-Newton-Größenordnung).
4. Normalordnung: Ein Zweikörperterm V_ij :n_i n_j: hat in jedem
   Einteilchenzustand den Erwartungswert 0, in Zweiteilchenzuständen nicht
   (Gitter mit Fermionen, exakte Diagonalisierung in der Fock-Basis).
5. Dok. 230: Die Quotienten |alpha|^2 = (1+z)/2 und r^2 = 4|alpha|^2|beta|^2
   liegen auf der Zylinderachse, nicht als zwei getrennte Ladungswolken im Ortsraum.

Aufruf aus der Repo-Wurzel:
    python3 2/python/Dok398_Skripte/pruef_398_dichte_selbstwechselwirkung.py
"""
import itertools
import math

import numpy as np
from scipy import integrate

ok = n = 0


def check(name, cond, info=""):
    global ok, n
    n += 1
    ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FEHLER'}] {name}" + (f"  ({info})" if info else ""))


# CODATA 2022
alpha = 7.2973525643e-3
hbar = 1.054571817e-34
c = 299792458.0
G = 6.67430e-11
m_e = 9.1093837139e-31
e = 1.602176634e-19
a0 = 5.29177210544e-11
Eh_eV = 27.211386245981

print("1. Stärkemaße nach Gao (Salzman-Maß)")
eps2_el = (4 * alpha) ** 2
check("elektrostatisch (4 alpha)^2 = 8,5e-4 (Gao: etwa 1e-3)", abs(eps2_el - 8.52e-4) < 0.01e-4, f"{eps2_el:.3e}")
eps2_gr = (4 * G * m_e ** 2 / (hbar * c)) ** 2
check("gravitativ (4 G m_e^2/hbar c)^2 = 4,9e-89 (Gao: etwa 4e-89)", 4.0e-89 < eps2_gr < 5.5e-89, f"{eps2_gr:.2e}")
check("Verhältnis elektrostatisch/gravitativ = (alpha/(G m_e^2/hbar c))^2 ~ 1e85",
      84 < math.log10(eps2_el / eps2_gr) < 86, f"10^{math.log10(eps2_el/eps2_gr):.1f}")

print("\n2. Coulomb-Selbstenergie der 1s-Dichte (atomare Einheiten)")
# rho(r) = exp(-2r)/pi; Potential der Kugelschale: Phi(r) = (1/r)[1-(1+r)e^{-2r}]
rho = lambda r: math.exp(-2 * r) / math.pi
phi = lambda r: (1 - (1 + r) * math.exp(-2 * r)) / r if r > 0 else 1.0
norm, _ = integrate.quad(lambda r: 4 * math.pi * r * r * rho(r), 0, 60)
check("1s-Dichte ist normiert", abs(norm - 1) < 1e-10, f"{norm:.12f}")
J, _ = integrate.quad(lambda r: 4 * math.pi * r * r * rho(r) * phi(r), 0, 60)
check("J = <Phi> = 5/8 Hartree", abs(J - 5 / 8) < 1e-9, f"{J:.10f}")
J_eV = J * Eh_eV
check("J = 17,0 eV, größer als die Bindungsenergie 13,6 eV", abs(J_eV - 17.007) < 0.01 and J_eV > 13.6,
      f"{J_eV:.3f} eV")
# Selbstenergie als (1/2) Integral rho Phi; sie erschiene in der Energie nur mit Faktor 1/2,
# in der Schrödinger-Gleichung (Eq. 2 bei Gao) aber das volle Potential.
check("halbe Selbstenergie 8,5 eV, immer noch 63 % der Bindungsenergie", abs(J_eV / 2 / 13.6057 - 0.625) < 0.001,
      f"{J_eV/2:.2f} eV")
# 2s-Dichte und ihre Selbstenergie: J_2s = 77/512 Hartree
rho2 = lambda r: (2 - r) ** 2 * math.exp(-r) / (32 * math.pi)
q_in = lambda r: integrate.quad(lambda t: 4 * math.pi * t * t * rho2(t), 0, r)[0]
phi2 = lambda r: q_in(r) / r + integrate.quad(lambda t: 4 * math.pi * t * rho2(t), r, 80)[0]
J2, _ = integrate.quad(lambda r: 4 * math.pi * r * r * rho2(r) * phi2(r), 1e-9, 80, limit=200)
check("J_2s = 77/512 Hartree = 4,09 eV", abs(J2 - 77 / 512) < 1e-7, f"{J2:.8f} = {J2*Eh_eV:.3f} eV")
dE = (J - J2) * Eh_eV
E12 = 0.75 * 13.605693
check("1S-2S-Abstand würde um 12,9 eV verschoben, mehr als der Übergang selbst (10,2 eV)",
      abs(dE - 12.92) < 0.02 and dE > E12, f"{dE:.2f} eV gegen {E12:.2f} eV")
# 1S-2S: 2466 THz, gemessen auf etwa 10 Hz (relativ 4e-15)
f1s2s = 2.466061413187e15
rel_mess = 10.0 / f1s2s
check("gemessene 1S-2S-Frequenz ist auf etwa 4e-15 genau, die Verschiebung wäre 127 % davon",
      rel_mess < 1e-14 and abs(dE / E12 - 1.266) < 0.005, f"{rel_mess:.0e}; {dE/E12*100:.0f} %")

print("\n3. Gravitative Selbstenergie derselben Dichte (Schrödinger-Newton-Maßstab)")
U_gr = G * m_e ** 2 / a0 * J  # Joule, gleiche Geometrie
U_gr_eV = U_gr / e
check("gravitative Selbstenergie des Wasserstoffelektrons ~ 4e-42 eV", 3e-42 < U_gr_eV < 5e-42, f"{U_gr_eV:.2e} eV")
check("Verhältnis zu J ist alpha_G/alpha = G m_e^2/(k e^2) ~ 2,4e-43",
      abs(U_gr_eV / J_eV - G * m_e ** 2 / (alpha * hbar * c)) / (U_gr_eV / J_eV) < 1e-6,
      f"{U_gr_eV / J_eV:.2e}")

print("\n4. Normalordnung: Zweikörperterm verschwindet im Einteilchensektor")
L = 6  # Gitterplätze, spinlose Fermionen
V = np.array([[0.0 if i == j else 1.0 / abs(i - j) for j in range(L)] for i in range(L)])

def zustaende(N):
    return [s for s in itertools.product([0, 1], repeat=L) if sum(s) == N]

def H_normal(N):
    """Diagonal: (1/2) sum_{i!=j} V_ij n_i n_j = :rho rho: im Ortsbasis-Fock-Raum."""
    basis = zustaende(N)
    return np.array([0.5 * sum(V[i, j] * s[i] * s[j] for i in range(L) for j in range(L)) for s in basis]), basis

d1, b1 = H_normal(1)
check("alle Einteilchenzustände: <:rho rho:> = 0", np.allclose(d1, 0.0), f"{len(b1)} Zustände")
rng = np.random.default_rng(3)
psi = rng.normal(size=len(b1)) + 1j * rng.normal(size=len(b1))
psi /= np.linalg.norm(psi)
check("auch beliebige Überlagerung eines Teilchens: Erwartungswert 0", abs(np.vdot(psi, d1 * psi)) < 1e-15)
# Gegenprobe: nicht normalgeordnet (1/2) sum V_ij n_i n_j inklusive i=j mit V_ii=Selbstterm
dens = np.abs(psi) ** 2
klass = 0.5 * sum(V[i, j] * dens[i] * dens[j] for i in range(L) for j in range(L))
check("klassische Wolke derselben Dichte hätte Selbstenergie > 0", klass > 0, f"{klass:.4f}")
d2, b2 = H_normal(2)
check("Zweiteilchenzustände: Wechselwirkung vorhanden (min > 0)", d2.min() > 0, f"min {d2.min():.3f}")

print("\n5. Dok. 230: Quotienten auf der Zylinderachse")
for z in [-0.6, 0.0, 0.3, 0.9]:
    a2 = (1 + z) / 2
    b2_ = (1 - z) / 2
    r2 = 1 - z * z
    if not (abs(r2 - 4 * a2 * b2_) < 1e-14 and abs(a2 + b2_ - 1) < 1e-14):
        break
else:
    z = None
check("r^2 = 1 - z^2 = 4|alpha|^2|beta|^2 und |alpha|^2+|beta|^2 = 1 für alle geprüften z", z is None)
check("r^2 ist bei z = 0 maximal (=1) und an den Polen 0", abs((1 - 0.0 ** 2) - 1) < 1e-15 and 1 - 1.0 ** 2 == 0)

print(f"\nErgebnis: {ok}/{n} PASS")
raise SystemExit(0 if ok == n else 1)
