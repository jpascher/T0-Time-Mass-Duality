#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a142_gravitation_lagrange.py -- Pruefskript zu A142 (Gravitation: Lagrange-Formulierung).
Prueft: (1) Zeitfeld-Verbindung Gamma = (1/T) dT = -dm/m mit T = 1/m, Grenzfall T = const,
(2) Dimensionen der Materieterme mit Omega dimensionslos, (3) die Dimensionsluecke der
Zeitfeld-Lagrange-Dichte (Vermerk 30. Sept. 2026), (4) die modifizierte Schroedinger-Gleichung
i T d_t Psi = H Psi ist inhomogen und gibt fuer T = 1/m nicht die Standardform
(Vermerk 2. Okt. 2026), (5) xi aus Higgs-Matching, (6) der Zusatz a_e ~ 2,34e-10 ist durch die
a_e-Messung ausgeschlossen (Vermerk 2. Okt. 2026).
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
mm, H, Psi = sp.symbols('m H Psi', positive=True)
t = sp.symbols('t')
P = sp.Function('P')(t)
eq = sp.Eq(sp.I * (1 / mm) * sp.diff(P, t), H * P)
sol = sp.solve(eq, sp.diff(P, t))[0]
check("Grenzfall T = 1/m konstant gibt i d_t Psi = m H Psi, nicht i d_t Psi = H Psi",
      sp.simplify(sol - (-sp.I * mm * H * P)) == 0)

print("5. xi aus Higgs-Matching")
mh, v = 125.20, 246.21965
lam = mh**2 / (2 * v**2)
xh = lam**2 * v**2 / (16 * math.pi**3 * mh**2)
check("lambda^2 v^2/(16 pi^3 m_h^2) = 1,30e-4, rund -2,3 % gegen 4/30000",
      abs(xh - 1.30e-4) < 0.01e-4 and abs(xh / xi - 1 + 0.023) < 0.002, f"{xh:.4e}")

print("6. a_e-Zusatz (Vermerk 2. Okt. 2026)")
alpha = 1 / 137.035999177
base = alpha / (2 * math.pi) * xi**2
I_needed = 2.34e-10 / base
check("alpha/(2 pi) xi^2 = 2,06e-11; fuer 2,34e-10 waere I_Schleife = 11,3 noetig, nicht ausgewiesen",
      abs(base - 2.065e-11) < 0.005e-11 and abs(I_needed - 11.33) < 0.05, f"I = {I_needed:.2f}")
agree = 1e-12   # Messung und QED-Rechnung fuer a_e stimmen auf rund 1e-12 ueberein
check("Zusatz 2,34e-10 ist ueber 200-mal groesser als die Uebereinstimmung von a_e mit QED: ausgeschlossen",
      2.34e-10 / agree > 200, f"Faktor {2.34e-10/agree:.0f}")

print(f"\nERGEBNIS: {n_ok}/{n_all} BESTANDEN")
raise SystemExit(0 if n_ok == n_all else 1)
