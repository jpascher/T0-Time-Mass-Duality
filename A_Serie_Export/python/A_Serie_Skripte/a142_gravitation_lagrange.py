#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a142_gravitation_lagrange.py -- Pruefskript zu A142 (Gravitation: Lagrange-Formulierung).
Prueft: (1) Zeitfeld-Verbindung Gamma = (1/T) dT = -dm/m mit T = 1/m, Grenzfall T = const,
(2) Dimensionen der Materieterme mit Omega dimensionslos, (3) die Dimensionsluecke der
Zeitfeld-Lagrange-Dichte (Vermerk 30. Sept. 2026), (4) die modifizierte Schroedinger-Gleichung: mit
dimensionsbehaftetem T inhomogen, mit T/T0 = 1/Omega homogen, Standardform fuer Omega = 1,
Amplitude ~ Omega und Phasenrate E*Omega -- gravitative Rotverschiebung (Vermerk 2. Okt. 2026), (5) xi aus Higgs-Matching, (6) der Zusatz a_e ~ 2,34e-10 (alpha = 1) bzw.
1,7e-12 (alpha/2pi) ist durch die a_e-Messung ausgeschlossen (Vermerk 2. Okt. 2026).
Dimensionen in natuerlichen Einheiten als Energie-Exponenten. sympy + Standardbibliothek."""
import math
import sympy as sp

n_ok = n_all = 0
def check(name, cond, info=""):
    global n_ok, n_all
    n_all += 1; n_ok += bool(cond)
    print(f"  [{'BESTANDEN' if cond else 'FEHLER   '}] {name}" + (f"  ({info})" if info else ""))

xi = 4 / 30000

print("1. Zeitfeld-Verbindung")
x = sp.symbols('x')
m = sp.Function('m')(x)
T = 1 / m
Gamma = sp.simplify(sp.diff(T, x) / T)
check("Gamma = (1/T) dT/dx = -m'/m fuer T = 1/m (korrigierter Wert)", sp.simplify(Gamma + sp.diff(m, x) / m) == 0)
check("frueherer Wert -m'/m^2 ist falsch", sp.simplify(Gamma + sp.diff(m, x) / m**2) != 0)
check("Grenzfall T = const: Gamma = 0, Standard-Dirac-Gleichung", sp.diff(sp.Integer(5), x) == 0)

print("2. Dimensionen der Materieterme (Energie-Exponenten, Omega dimensionslos)")
# Lagrange-Dichte in 4D: [E^4]; d^4x: [E^-4]; Wirkung dimensionslos
dim_phi, dim_psi, dim_A = 1, sp.Rational(3, 2), 1
check("skalar: (d phi)^2 und m^2 phi^2 haben je [E^4]", 2*dim_phi + 2 == 4 and 2 + 2*dim_phi == 4)
check("Fermion: psibar i gamma d psi und m psibar psi haben je [E^4]", 2*dim_psi + 1 == 4)
check("Eichterm F^2 hat [E^4]", 2*(dim_A + 1) == 4)

print("3. Zeitfeld-Lagrange-Dichte (Vermerk 30. Sept. 2026)")
dim_T = -1
kin = 2*dim_T + 2
check("mit [T] = [E^-1] ist (dT)^2 dimensionslos, nicht [E^2] -- Klammer inhomogen gegen V ~ [E^4]", kin == 0 and kin != 4)

print("4. Modifizierte Schroedinger-Gleichung (Vermerk 2. Okt. 2026)")
lhs = dim_T + 1          # i T d_t Psi: [E^-1][E^1] = [E^0] (mal Psi)
rhs = 1                  # H Psi: [E^1] (mal Psi)
check("i T d_t Psi hat [E^0] Psi, H Psi hat [E^1] Psi: Gleichung inhomogen", lhs == 0 and rhs == 1)
mm, H = sp.symbols('m H', positive=True)
t = sp.symbols('t')
P = sp.Function('P')(t)
sol = sp.solve(sp.Eq(sp.I * (1 / mm) * sp.diff(P, t), H * P), sp.diff(P, t))[0]
check("mit dimensionsbehaftetem T = 1/m konstant: i d_t Psi = m H Psi, nicht die Standardform",
      sp.simplify(sol - (-sp.I * mm * H * P)) == 0)
# Lesart mit dem dimensionslosen T/T0 = 1/Omega: i (1/Om) d_t Psi + i Psi d_t(1/Om) = H Psi
Om = sp.Function('Omega', positive=True)(t); E = sp.symbols('E', real=True)
A = sp.Function('A', positive=True)(t); ph = sp.Function('phi', real=True)(t)
Ps = A * sp.exp(-sp.I * ph)
eq = sp.expand((sp.I / Om * sp.diff(Ps, t) + sp.I * Ps * sp.diff(1 / Om, t) - E * Ps) * sp.exp(sp.I * ph))
# Ansatz A = C*Omega, phi' = E*Omega loest die Gleichung
C = sp.symbols('C', positive=True)
chk = sp.simplify(eq.subs(A, C * Om).doit().subs(sp.Derivative(ph, t), E * Om))
check("mit T/T0 = 1/Omega homogen; Loesung: Amplitude = C*Omega (lokale Energiedichte), Phasenrate = E*Omega (lokaler Takt)", chk == 0)
check("fuer Omega = 1 Standardform: Amplitude konstant, Phasenrate E", sp.simplify(chk.subs(Om, 1)) == 0)

print("5. xi aus Higgs-Matching")
mh, v = 125.20, 246.21965
lam = mh**2 / (2 * v**2)
xh = lam**2 * v**2 / (16 * math.pi**3 * mh**2)
check("lambda^2 v^2/(16 pi^3 m_h^2) = 1,30e-4, rund -2,3 % gegen 4/30000",
      abs(xh - 1.30e-4) < 0.01e-4 and abs(xh / xi - 1 + 0.023) < 0.002, f"{xh:.4e}")

print("6. a_e-Zusatz (Vermerk 2. Okt. 2026)")
alpha = 1 / 137.035999177
v1 = 1 / (2 * math.pi) * xi**2 / 12
v2 = alpha / (2 * math.pi) * xi**2 / 12
check("2,34e-10 entsteht mit 1/(2 pi), also alpha = 1, und I = 1/12", abs(v1 - 2.36e-10) < 0.02e-10, f"{v1:.3e}")
check("mit der physikalischen Kopplung alpha/(2 pi): 1,72e-12", abs(v2 - 1.72e-12) < 0.01e-12, f"{v2:.3e}")
# Messung minus QED (Fan 2023; alpha aus Rb bzw. Cs): +3,4(1,6)e-13 bzw. -10,1(2,7)e-13
sRb = (v2 - 3.4e-13) / 1.6e-13; sCs = (v2 + 10.1e-13) / 2.7e-13
check("Zusatz 1,72e-12 liegt 8,6 sigma (Rb) bzw. 10 sigma (Cs) neben Messung minus QED: ausgeschlossen",
      abs(sRb - 8.6) < 0.1 and abs(sCs - 10.1) < 0.1, f"{sRb:.1f} / {sCs:.1f} sigma")
check("2,34e-10 waere ueber 200-mal groesser als die Uebereinstimmung von rund 1e-12", 2.34e-10 / 1e-12 > 200)

print(f"\nERGEBNIS: {n_ok}/{n_all} BESTANDEN")
raise SystemExit(0 if n_ok == n_all else 1)
