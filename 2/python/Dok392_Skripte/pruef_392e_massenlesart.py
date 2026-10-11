#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_392e_massenlesart.py -- Dok. 392, Teil E: Was für die Massenlesart spricht.

Gegenstück zu 392a-d. Rechnet nach:
  1. Die zeitliche Hälfte (g00 = (m/m0)^2) ist in JEDER zugelassenen Darstellung enthalten und trägt
     allein: Newtonsche Dynamik, Rotverschiebung, Uhrengang. Messwerte [Q]: Pound-Rebka 1960;
     Gravity Probe A (Vessot u.a. 1980, 7e-5); Galileo 5/6 (Delva u.a. 2018 PRL 121, 231101 und
     Herrmann u.a. 2018 PRL 121, 231102, Abweichung <= 2,5e-5); optische Uhren 33 cm
     (Chou u.a. 2010, Science 329, 1630); GPS-Uhrenkorrektur.
  2. Weyl-Tensor: reine Massenvariation (alle Takte und Längen ~ 1/m) ist eine konforme Skalierung
     des flachen Raums, Weyl = 0. Das FRW-Universum ist konform flach (Weyl = 0) -> die Massenlesart
     ist dort EXAKT, nicht genähert. Das Feld eines Sterns hat Weyl != 0 -> dort braucht es die
     räumliche Hälfte zusätzlich.
  3. Kosmos: flaches FRW = a(eta)^2 * Minkowski; im statischen Rahmen m(eta) = m0 a(eta);
     1 + z = m_heute/m_Emission = a0/a (Wetterich 2013).
  4. Vorzeichen der Maßstäbe: kosmisch Längen ~ 1/m (Compton/Bohr, Tolman k = 4 aus 392d),
     im statischen Feld verlangt gamma = 1 Eigenlängen ~ m (Dok. 389 §7) -- die räumliche Hälfte
     folgt dort nicht aus der Massenskalierung.
sympy + Standardbibliothek.
"""
import math
import sympy as sp

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

c = 299792458.0; GMe = 3.986004418e14; Re = 6.3781e6; day = 86400.0

print("1. Die zeitliche Hälfte trägt allein (Messungen über g00 = (m/m0)^2)")
g = GMe/Re**2
pr = g*22.5/c**2
check("Pound-Rebka: g h/c^2 = 2,46e-15 über 22,5 m (gemessen 2,57 +- 0,26)", abs(pr-2.455e-15) < 1e-17 and abs(2.57e-15-pr) < 0.26e-15, f"{pr:.3e}")
ch = g*0.33/c**2
check("Optische Uhren 33 cm: g h/c^2 = 3,6e-17 (gemessen 4,1 +- 1,6e-17)", abs(4.1e-17-ch) < 1.6e-17, f"{ch:.2e}")
a_gps = 26_561.75e3
grav = (GMe/Re - GMe/a_gps)/c**2*day*1e6
vel = -0.5*(GMe/a_gps)/c**2*day*1e6
check("GPS: Massen-/Taktanteil +45,7 µs/Tag, Geschwindigkeit -7,2, Summe +38,5", abs(grav-45.7) < 0.2 and abs(grav+vel-38.5) < 0.3,
      f"{grav:.1f} + ({vel:.1f}) = {grav+vel:.1f} µs/Tag")
print("     Gravity Probe A bestätigt den Taktanteil auf 7e-5, Galileo 5/6 auf 2,5e-5 [Q].")
# Newton exakt aus ln m (vgl. Dok. 389): a = -c^2 grad ln m
r = sp.symbols('r', positive=True); GM, cc, m0 = sp.symbols('GM c m0', positive=True)
m = m0*sp.exp(-GM/(r*cc**2))
acc = -cc**2*sp.diff(sp.log(m), r)
check("Fallbeschleunigung aus dem Massengradienten: -c^2 d(ln m)/dr = -GM/r^2 exakt", sp.simplify(acc + GM/r**2) == 0)

print("2. Weyl-Tensor: konform flach oder nicht")
t, th, ph = sp.symbols('t theta phi')
def weyl_trtr(gdiag, coords):
    """C_{trtr} für diagonale Metrik (Signatur -+++), allgemein berechnet."""
    N = 4; gm = sp.diag(*gdiag); gi = gm.inv()
    Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(gm[d, b], coords[cidx]) + sp.diff(gm[d, cidx], coords[b])
            - sp.diff(gm[b, cidx], coords[d]))/2 for d in range(N))) for cidx in range(N)] for b in range(N)] for a in range(N)]
    def Riem(a, b, cc_, d):   # R^a_{b c d}
        return (sp.diff(Gam[a][b][d], coords[cc_]) - sp.diff(Gam[a][b][cc_], coords[d])
                + sum(Gam[a][cc_][e]*Gam[e][b][d] - Gam[a][d][e]*Gam[e][b][cc_] for e in range(N)))
    Rl = lambda a, b, cc_, d: sum(gm[a, e]*Riem(e, b, cc_, d) for e in range(N))
    Ric = sp.Matrix(N, N, lambda b, d: sp.simplify(sum(Riem(a, b, a, d) for a in range(N))))
    Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(N) for b in range(N)))
    a, b, c_, d = 0, 1, 0, 1
    C = (Rl(a, b, c_, d) - (gm[a, c_]*Ric[b, d] - gm[a, d]*Ric[b, c_] - gm[b, c_]*Ric[a, d] + gm[b, d]*Ric[a, c_])/2
         + Rs*(gm[a, c_]*gm[b, d] - gm[a, d]*gm[b, c_])/6)
    return sp.simplify(C)
coords = [t, r, th, ph]
Om = sp.Function('Omega')(r)
C_mass = weyl_trtr([-Om**2, Om**2, Om**2*r**2, Om**2*r**2*sp.sin(th)**2], coords)
check("statische reine Massenvariation Omega(r)^2 * Minkowski: Weyl = 0 für jede Funktion Omega", C_mass == 0, str(C_mass))
aa = sp.Function('a')(t)
C_frw = weyl_trtr([-aa**2, aa**2, aa**2*r**2, aa**2*r**2*sp.sin(th)**2], coords)
check("flaches FRW in konformer Zeit a^2 * Minkowski: Weyl = 0", C_frw == 0, str(C_frw))
U = sp.Function('U')(r)
eps = sp.symbols('epsilon')
C_iso = weyl_trtr([-(1-2*eps*U), 1+2*eps*U, (1+2*eps*U)*r**2, (1+2*eps*U)*r**2*sp.sin(th)**2], coords)
C1 = sp.simplify(sp.series(C_iso, eps, 0, 2).removeO().coeff(eps, 1).subs(U, GM/r))
check("Sternfeld (isotrop, gamma = 1, erste Ordnung, U = GM/r): Weyl != 0", sp.simplify(C1) != 0, f"C_trtr = {C1}*eps")

print("3. Kosmos in der Massenlesart (Wetterich)")
eta_, x_ = sp.symbols('eta x', real=True)
A_ = sp.Function('a')(eta_)
ds2_frw = A_**2*(-1 + sp.Symbol('v')**2)          # ds^2/deta^2 mit v = dx/deta, a^2 * Minkowski
nullv = sp.solve(sp.Eq(ds2_frw, 0), sp.Symbol('v'))
check("Lichtkegel des FRW in konformer Zeit unabhängig von a: ds^2 = 0 <=> dx/deta = +-1 -- "
      "Licht läuft wie im statischen Raum, nur Massen und Takte laufen", set(nullv) == {-1, 1}, str(nullv))
print("     Im statischen Rahmen ist m(eta) = m0 a(eta), Frequenzen ~ m: 1 + z = a0/a_E (Wetterich 2013) [Q].")

print("4. Vorzeichen der Maßstäbe")
Us = sp.symbols('U', positive=True)
mass = 1 - Us                          # m/m0 tief im Potential, vom fernen Bezug aus
compton = sp.series(1/mass, Us, 0, 2).removeO()     # Länge ~ 1/m
eigen = sp.series(1/sp.sqrt(1+2*Us), Us, 0, 2).removeO()   # Koordinatenlänge eines Eigenmaßstabs bei gamma = 1
check("Compton-/Bohr-Länge ~ 1/m wird tief im Potential länger: 1 + U", sp.expand(compton) == 1 + Us)
check("gamma = 1 verlangt Eigenmaßstäbe, die vom fernen Bezug aus kürzer erscheinen: 1 - U (~ m)",
      sp.expand(eigen) == 1 - Us)
check("Die Vorzeichen sind entgegengesetzt (Koeffizient von U: +1 gegen -1): die räumliche Hälfte folgt im "
      "Sternfeld nicht aus der Massenskalierung", sp.expand(compton).coeff(Us, 1) == -sp.expand(eigen).coeff(Us, 1))

print(f"\n{ok}/{n} Prüfungen bestanden")
raise SystemExit(0 if ok == n else 1)
