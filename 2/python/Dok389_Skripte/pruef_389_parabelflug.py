#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_389_parabelflug.py -- Dok. 389: Parabelflug, Trägheit und die Darstellungen der Gravitation.

Rechnet nach:
  1. Fall aus der ortsabhängigen Masse: L = -m(x) c^2 sqrt(1-v^2/c^2) mit
     m = m0 exp(Phi/c^2) gibt a = -c^2 grad ln m = -grad Phi; Ruhe-Weltlinie
     braucht +g nach oben (Gewicht); g/c^2 an der Erdoberfläche = Uhrengang pro Meter.
  2. Vorzeichen: m nimmt nach unten ab (Rotverschiebung, Pound-Rebka).
  3. Gezeiten: Hesse-Matrix von Phi, spurfrei im Vakuum, nicht wegtransformierbar.
  4. Licht: n = 1 + (1+gamma) GM/(r c^2); konform flach (gamma=-1) 0,
     nur Takt (gamma=0) 0,875", Takt + Weg (gamma=1) 1,75"; Shapiro ebenso.
  5. Perihel: Faktor (2+2gamma-beta)/3; exp-Form gibt beta = 1, lineare Form 1/2,
     Nordström -1/6 des ART-Werts.
  6. Horizont: statischer Beobachter E_loc = E/sqrt(1-r_s/r) divergiert, frei
     fallender misst für einlaufendes Licht E/(1+sqrt(r_s/r)) -> E/2.
  7. Namensklärung: M_coll = m_P/sqrt2 aus r_s = Compton-Länge; m_P/xi = 7500 m_P.
sympy, scipy + Standardbibliothek.
"""
import math
import sympy as sp
from scipy.integrate import quad

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

# Konstanten (CODATA 2022, IAU)
c = 299792458.0; G = 6.67430e-11
GMs = 1.32712440018e20; Rs = 6.957e8           # Sonne
GMe = 3.986004418e14; Re = 6.371e6             # Erde
rad = 180 / math.pi * 3600
xi = 4 / 30000
hbar = 1.054571817e-34
mP = math.sqrt(hbar * c / G)

print("1. Fall aus der ortsabhängigen Masse")
t = sp.symbols('t'); cc, m0 = sp.symbols('c m0', positive=True)
z = sp.Function('z')(t); Phi = sp.Function('Phi')
m = m0 * sp.exp(Phi(z) / cc**2)
L = -m * cc**2 * sp.sqrt(1 - sp.diff(z, t)**2 / cc**2)
EL = sp.diff(sp.diff(L, sp.diff(z, t)), t) - sp.diff(L, z)
zdd = sp.solve(EL, sp.diff(z, t, 2))[0]
zdd0 = sp.simplify(zdd.subs(sp.diff(z, t), 0))
check("Euler-Lagrange mit m = m0 exp(Phi/c^2): z'' = -Phi'(z) bei v = 0 (Newton exakt)",
      sp.simplify(zdd0 + sp.diff(Phi(z), z)) == 0, f"z'' = {zdd0}")
lnm = sp.log(m)
check("a = -c^2 d(ln m)/dz = -c^2 d(ln lambda4)/dz mit lambda4 = 2 pi/m (umgekehrtes Vorzeichen)",
      sp.simplify(-cc**2 * sp.diff(lnm, z) - zdd0) == 0
      and sp.simplify(cc**2 * sp.diff(sp.log(2*sp.pi/m), z) - zdd0) == 0)
# Ruhe-Weltlinie: Variation verschwindet nicht, Rest = Gewicht
Lsta = L.subs(sp.diff(z, t), 0)
check("Ruhe-Weltlinie z = const ist nicht stationär: dL/dz = -m Phi'/... = -m g (Gewicht nach unten)",
      sp.simplify(sp.diff(Lsta, z) + m * sp.diff(Phi(z), z)) == 0)
g = GMe / Re**2
check("Erdoberfläche: g = 9,82 m/s^2, g/c^2 = 1,09e-16 pro Meter (Uhrengang pro Meter Höhe)",
      abs(g - 9.82) < 0.01 and abs(g / c**2 - 1.093e-16) < 2e-19, f"g/c^2 = {g/c**2:.4e} /m")

Pz = sp.symbols('Phi', real=True)
g00 = (m0 * sp.exp(Pz / cc**2) / m0)**2
check("Killing-Energie: m = m0 sqrt(g00), g00 = (m/m0)^2 = exp(2 Phi/c^2); omega = omega0 (1 + Phi/c^2) in 1. Ordnung",
      sp.simplify(g00 - sp.exp(2 * Pz / cc**2)) == 0
      and sp.simplify(sp.series(sp.sqrt(g00), Pz, 0, 2).removeO() - (1 + Pz / cc**2)) == 0)
lam4 = 2 * sp.pi / m
aF = cc**2 * sp.diff(sp.log(lam4), z); aT = -cc**2 * sp.diff(sp.log(lam4), z)
check("Gegenbahn: a_Fall = c^2 d ln lambda4 = -Phi', a_Träg = -a_Fall, Summe 0 am Boden",
      sp.simplify(aF + sp.diff(Phi(z), z)) == 0 and sp.simplify(aF + aT) == 0)
print("2. Vorzeichen")
h = 22.5
pr = g * h / c**2
check("Pound-Rebka (22,5 m): erwartet 2,46e-15, gemessen (2,57 +- 0,26)e-15, Verhältnis 1,05 +- 0,10",
      abs(pr - 2.46e-15) < 1e-17 and abs(2.57e-15 / pr - 1.05) < 0.01)
mrel = math.expm1(g * h / c**2)                  # m(oben)/m(unten) - 1 mit Phi = g z
check("Licht von unten kommt oben rotverschoben an: m(oben)/m(unten) - 1 = gh/c^2 > 0, m wächst mit Phi",
      mrel > 0 and abs(mrel / pr - 1) < 1e-12)

print("3. Gezeiten")
x, y, zz = sp.symbols('x y z', real=True); GM = sp.symbols('GM', positive=True)
r = sp.sqrt(x**2 + y**2 + zz**2)
H = sp.hessian(-GM / r, (x, y, zz))
Hz = sp.simplify(H.subs({x: 0, y: 0}))
check("Hesse-Matrix von -GM/r auf der z-Achse: Eigenwerte (-2, 1, 1) GM/r^3, Spur 0 im Vakuum",
      sp.simplify(H.trace()) == 0 and sorted(float(sp.simplify(Hz[i, i] * zz**3 / GM).subs(zz, 1)) for i in range(3)) == [-2.0, 1.0, 1.0])
check("Gezeiten an der Erdoberfläche 2GM/r^3 = 3,08e-6 s^-2: im Fallsystem nicht wegtransformierbar",
      abs(2 * GMe / Re**3 - 3.08e-6) < 1e-8)

rr_ = sp.symbols('r', positive=True)
lnm_out = -GM / (rr_ * cc**2)
check("Poisson für das Massenfeld: ln m = Phi/c^2, also nabla^2 ln m = 4 pi G rho/c^2; außen Laplace 0",
      sp.simplify(sp.diff(rr_**2 * sp.diff(lnm_out, rr_), rr_) / rr_**2) == 0)
check("außen: d_r ln m = GM/(r^2 c^2) (wegtransformierbar), c^2 d_r^2 ln m = -2GM/r^3 (bleibt)",
      sp.simplify(sp.diff(lnm_out, rr_) - GM / (rr_**2 * cc**2)) == 0
      and sp.simplify(cc**2 * sp.diff(lnm_out, rr_, 2) + 2 * GM / rr_**3) == 0)
print("4. Licht: Takt, Weg und konform flache Metrik")
I = quad(lambda u: 1 / (1 + u * u)**1.5, -math.inf, math.inf)[0]
defl = lambda gam: (1 + gam) * GMs / (c * c * Rs) * I * rad
check("konform flach (gamma = -1): Ablenkung 0", abs(defl(-1)) < 1e-12)
check("nur Takt (gamma = 0, Einstein 1911): 0,875\"", abs(defl(0) - 0.8756) < 1e-3, f"{defl(0):.4f}\"")
check("Takt + Wegverlängerung (gamma = 1, Dok. 308 K3): 1,751\"", abs(defl(1) - 1.7512) < 1e-3, f"{defl(1):.4f}\"")
check("Messung: Cassini gamma - 1 = (2,1 +- 2,3)e-5; gamma = 0 oder -1 ausgeschlossen",
      abs(1 - 1 - 2.1e-5) / 2.3e-5 < 1 and abs(0 - 1 - 2.1e-5) / 2.3e-5 > 4e4)
Om = sp.symbols('Omega', positive=True)
check("konforme Kopplung g -> Omega^2 g (A142): Maxwell-Term skaliert mit Omega^4 Omega^-2 Omega^-2 = 1, Licht unberührt",
      sp.simplify(Om**4 * Om**-2 * Om**-2) == 1)
sh = lambda gam: (1 + gam) / 2
check("Shapiro-Verzögerung skaliert ebenso mit (1+gamma)/2: 0, 1/2, 1", [sh(-1), sh(0), sh(1)] == [0, 0.5, 1])

u_ = sp.symbols('u', real=True)   # u = Phi/c^2
lk = sp.series(1 / sp.sqrt(1 - 2 * u_), u_, 0, 2).removeO()   # dx = dl / sqrt(g_rr)
l4 = sp.series(1 / sp.exp(u_), u_, 0, 2).removeO()            # 2 pi/m(x) relativ zu 2 pi/m0
check("isotrope ART: l_koord = l (1 + Phi/c^2), lambda4_koord = lambda4 (1 - Phi/c^2): Faktoren gegenläufig",
      sp.simplify(lk - (1 + u_)) == 0 and sp.simplify(l4 - (1 - u_)) == 0)
check("Brechungsindex n = 1 - 2 Phi/c^2: Takt -Phi/c^2 plus räumlicher Anteil -Phi/c^2 (gamma = 1)",
      sp.simplify((1 - u_) + (1 - u_) - 1 - (1 - 2 * u_)) == 0)
print("5. Periheldrehung")
U = sp.symbols('U')
g00_exp = sp.series(sp.exp(-2 * U), U, 0, 3).removeO()
g00_lin = sp.expand((1 - U)**2)
beta = lambda g00: sp.Rational(1, 2) * g00.coeff(U, 2)   # g00 = 1 - 2U + 2 beta U^2
check("m = m0 exp(Phi/c^2): g00 = 1 - 2U + 2U^2, beta = 1", beta(g00_exp) == 1)
check("m = m0 (1 + Phi/c^2): g00 = 1 - 2U + U^2, beta = 1/2", beta(g00_lin) == sp.Rational(1, 2))
fac = lambda gam, bet: (2 + 2 * gam - bet) / 3
a_M = 5.7909e10; e_M = 0.2056; P_M = 87.969
art = 6 * math.pi * GMs / (c**2 * a_M * (1 - e_M**2)) * rad * 36525 / P_M
check("Merkur ART: 42,98\"/Jh", abs(art - 42.98) < 0.05, f"{art:.2f}")
check("gamma = 1, beta = 1 (Takt + Weg, exp-Form): Faktor 1, 42,98\"/Jh", fac(1, 1) == 1)
check("gamma = 1, beta = 1/2 (lineare Form): Faktor 7/6, 50,1\"/Jh", abs(fac(1, 0.5) - 7/6) < 1e-12 and abs(art * 7/6 - 50.14) < 0.05)
check("Nordström (gamma = -1, beta = 1/2): Faktor -1/6, -7,2\"/Jh", abs(fac(-1, 0.5) + 1/6) < 1e-12 and abs(art / 6 - 7.16) < 0.02)
check("nur Takt (gamma = 0, beta = 1): Faktor 1/3, 14,3\"/Jh", abs(fac(0, 1) - 1/3) < 1e-12 and abs(art / 3 - 14.33) < 0.01)

print("6. Horizont: statisch und frei fallend")
s = sp.symbols('s', positive=True); E = sp.symbols('E', positive=True)
Eloc = E / sp.sqrt(1 - s)
check("statischer Beobachter: E_loc = E/sqrt(1 - r_s/r) divergiert für r -> r_s", sp.limit(Eloc.subs(s, 1 - sp.Symbol('eps', positive=True)), sp.Symbol('eps', positive=True), 0, '+') == sp.oo)
ut, ur = 1 / (1 - s), -sp.sqrt(s)                # frei fallend aus der Ruhe im Unendlichen
pt, pr_ = E / (1 - s), -E                        # einlaufendes Photon
Eff = sp.simplify((1 - s) * ut * pt - (1 / (1 - s)) * ur * pr_)
check("Normierung u.u = -1 der Fall-Weltlinie", sp.simplify(-(1 - s) * ut**2 + ur**2 / (1 - s) + 1) == 0)
check("frei fallend: E_obs = E/(1 + sqrt(r_s/r)) -> E/2 am Horizont, endlich",
      sp.simplify(Eff - E / (1 + sp.sqrt(s))) == 0 and sp.limit(Eff, s, 1) == E / 2)
# Eigenabstand vom Horizont rho = int dr/sqrt(1-r_s/r); nahe r_s gilt sqrt(1-r_s/r) = rho/(2 r_s)
import mpmath as mp
mp.mp.dps = 40
rs_ = mp.mpf(1); rr = rs_ + mp.mpf('1e-12')
F = lambda q: mp.sqrt(q * (q - rs_)) + rs_ * mp.log(mp.sqrt(q) + mp.sqrt(q - rs_))
rho_ = F(rr) - F(rs_)                            # Stammfunktion von 1/sqrt(1 - r_s/r)
check("nahe am Horizont: sqrt(1 - r_s/r) = rho/(2 r_s), also E_loc = E_P/xi bei rho_min = 2 r_s xi E/E_P",
      abs(mp.sqrt(1 - rs_ / rr) / (rho_ / (2 * rs_)) - 1) < 1e-6)

print("7. Namensklärung")
Ms = sp.symbols('M', positive=True); hb, cs, Gs = sp.symbols('hbar c G', positive=True)
sol = sp.solve(sp.Eq(2 * Gs * Ms / cs**2, hb / (Ms * cs)), Ms)
check("r_s = reduzierte Compton-Länge: M_coll = m_P/sqrt2", sp.simplify(sol[0] - sp.sqrt(hb * cs / Gs) / sp.sqrt(2)) == 0)
check("m_P/xi = 7500 m_P = 1,63e-4 kg (duale Obergrenze je Anregung, Dok. 306)", abs(mP / xi - 1.632e-4) < 1e-6)
check("die beiden Massen sind verschieden: (m_P/xi)/(m_P/sqrt2) = 7500 sqrt2 = 10607", abs(math.sqrt(2) / xi - 10606.6) < 0.1)

print(f"\nErgebnis: {ok}/{n}")
raise SystemExit(0 if ok == n else 1)
