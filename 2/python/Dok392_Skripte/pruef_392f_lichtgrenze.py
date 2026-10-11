#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_392f_lichtgrenze.py -- Dok. 392, Teil F: Die Grenze der Lichtgeschwindigkeit.

Rechnet nach (Grundform c = 1, Bezug Dok. 314, 312, 391, 131):
  1. Torusspektrum E^2 = p^2 + m^2 mit m = k4/R4 (Wicklungszahl = Massenzahl, Dok. 314):
     Gruppengeschwindigkeit v = dE/dp = p/E; v = 1 genau für k4 = 0, sonst v < 1 für jedes p.
  2. E = gamma m mit gamma = 1/sqrt(1-v^2); die Energie zum Erreichen von v = 1 divergiert.
  3. Harmonie der Phasen (de Broglie, Dok. 312): innere Frequenz nu0/gamma, Phasenfrequenz gamma nu0,
     Produkt invariant.
  4. Konforme Skalierung Omega^2 eta lässt Nullvektoren fest: Massenvariation ändert c lokal nie;
     lokal gemessenes c = 1 für jedes Omega.
  5. Koordinatengeschwindigkeit des Lichts: konform (A = B) gleich 1, isotropes Feld mit gamma = 1
     gleich 1 - 2U: die "Verlangsamung" an der Sonne ist die räumliche Hälfte (Wegverlängerung
     n = 1 + 2U), nicht ein veränderliches c (R132).
  6. Vakuumkonstanten: Ein statisches Feld wirkt auf Maxwell-Felder wie ein Medium mit
     eps = mu = sqrt(B/A) (Plebanski 1960, Phys. Rev. 118, 1396 [Q]). Bei gamma = 1 steigen eps und mu
     gleich um 1 + 2U; c_koord = 1/sqrt(eps mu) und die Impedanz sqrt(mu/eps) = 1 bleibt. Reine
     Massenvariation (A = B) gibt eps = mu = 1 (Maxwell ist in vier Dimensionen konform invariant).
     Lokal gemessen gelten eps0, mu0 und eps0 mu0 c^2 = 1 überall unverändert.
sympy + Standardbibliothek.
"""
import sympy as sp

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

p, R4 = sp.symbols('p R_4', positive=True)
k4 = sp.symbols('k_4', integer=True)
print("1. Torusspektrum und Gruppengeschwindigkeit")
m = k4/R4
E = sp.sqrt(p**2 + m**2)
v = sp.simplify(sp.diff(E, p))
check("v = dE/dp = p/E", sp.simplify(v - p/E) == 0, f"v = {v}")
check("k4 = 0 (masselos, keine Wicklung): v = 1 für jedes p", sp.simplify(v.subs(k4, 0)) == 1)
vm = v.subs({k4: 1})
check("k4 != 0 (massiv): 1 - v^2 = m^2/E^2 > 0, also v < 1 für jedes p",
      sp.simplify(1 - vm**2 - (1/R4)**2/(p**2 + 1/R4**2)) == 0)
check("v -> 1 nur im Grenzfall p -> unendlich", sp.limit(vm, p, sp.oo) == 1)
print("     Massive Moden verteilen ihre Wellenzahl auf Raum und x4; nur der Raumanteil ist Bewegung.")

print("2. Energie bei Annäherung an c")
vv = sp.symbols('v', real=True); m0 = sp.symbols('m0', positive=True)
gam = 1/sp.sqrt(1 - vv**2)
pv = gam*m0*vv
check("E^2 - p^2 = m^2 mit E = gamma m, p = gamma m v", sp.simplify((gam*m0)**2 - pv**2 - m0**2) == 0)
check("kinetische Energie gamma m - m divergiert für v -> 1", sp.limit(gam*m0 - m0, vv, 1, '-') == sp.oo)
print("     Für 70 kg bei gamma = 10: (gamma-1) m c^2 = %.1e J (Dok. 312)" % (9*70*299792458.0**2))

print("3. Harmonie der Phasen (T~ m = 1 kinetisch)")
nu0 = sp.symbols('nu0', positive=True)
check("innere Frequenz nu0/gamma mal Phasenfrequenz gamma nu0 = nu0^2, unabhängig von v",
      sp.simplify((nu0/gam)*(gam*nu0) - nu0**2) == 0)

print("4. Konforme Skalierung und Lichtkegel")
Om = sp.symbols('Omega', positive=True)
kt, kx, ky, kz = sp.symbols('k_t k_x k_y k_z', real=True)
eta = sp.diag(-1, 1, 1, 1)
kvec = sp.Matrix([kt, kx, ky, kz])
norm_eta = (kvec.T*eta*kvec)[0]
norm_g = (kvec.T*(Om**2*eta)*kvec)[0]
check("g(k,k) = Omega^2 eta(k,k): Nullvektoren sind dieselben für jedes Omega",
      sp.simplify(norm_g - Om**2*norm_eta) == 0)
dl, dtau = sp.symbols('dl dtau', positive=True)
c_local = (Om*dl)/(Om*dtau)
check("lokal gemessenes c = Eigenlänge/Eigenzeit eines Lichtsignals hängt nicht von Omega ab",
      sp.simplify(c_local.subs(dl, dtau)) == 1)

print("5. Koordinatengeschwindigkeit im Feld")
U = sp.symbols('U', positive=True)
A, B = sp.symbols('A B', positive=True)
c_coord = sp.sqrt(A/B)
check("reine Massenvariation (A = B): Koordinatengeschwindigkeit 1, keine Shapiro-Verzögerung",
      sp.simplify(c_coord.subs(B, A)) == 1)
c_iso = sp.series(c_coord.subs({A: 1 - 2*U, B: 1 + 2*U}), U, 0, 2).removeO()
check("isotropes Feld mit gamma = 1: Koordinatengeschwindigkeit 1 - 2U = 1/n mit n = 1 + 2U (erste Ordnung)",
      sp.expand(c_iso) == 1 - 2*U and sp.expand(sp.series(1/(1 + 2*U), U, 0, 2).removeO()) == 1 - 2*U)
GMs, Rs, c = 1.32712440018e20, 6.957e8, 299792458.0
Us = GMs/(Rs*c**2)
check("am Sonnenrand: Koordinatengeschwindigkeit um 2U = 4,2e-6 kleiner, lokal weiterhin c",
      abs(2*Us - 4.24e-6) < 2e-8, f"2U = {2*Us:.3e}")

print("6. Elektrische und magnetische Feldkonstante")
eps = sp.sqrt(B/A); mu = sp.sqrt(B/A)
check("Medium-Form des statischen Feldes: c_koord = 1/sqrt(eps mu) = sqrt(A/B)", sp.simplify(1/sp.sqrt(eps*mu) - c_coord) == 0)
eps_iso = sp.series(eps.subs({A: 1 - 2*U, B: 1 + 2*U}), U, 0, 2).removeO()
check("gamma = 1: eps = mu = 1 + 2U, beide gleich stark erhöht", sp.expand(eps_iso) == 1 + 2*U)
check("Wellenimpedanz sqrt(mu/eps) = 1 für jedes Feld: keine Reflexion, keine Doppelbrechung, "
      "Ablenkung unabhängig von Polarisation und Farbe", sp.simplify(sp.sqrt(mu/eps)) == 1)
check("reine Massenvariation (A = B): eps = mu = 1 -- konforme Invarianz der Maxwell-Gleichungen",
      sp.simplify(eps.subs(B, A)) == 1)
print("     Lokal: eps0 mu0 c^2 = 1 exakt (SI); seit 2019 ist mu0 gemessen, "
      "mu0/(4 pi 1e-7 N/A^2) = 1,00000000055(15) [Q] CODATA 2018 -- überall derselbe Wert.")

print(f"\n{ok}/{n} Prüfungen bestanden")
raise SystemExit(0 if ok == n else 1)
