#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_392b_mitfuehrung.py -- Dok. 392, Teil B: Mitführung (Lense-Thirring) und die flache Darstellung.

Frage: Können Takt (skalares Massenfeld m(x)) und fraktale Wegverlängerung (skalarer Index n(x))
die Mitführung durch rotierende Massen tragen? Die Mitführung steckt in g_0i (Dok. 312).

Rechnet nach:
  1. GP-B-Vorhersagen (geodätisch, Mitführung) aus Erdparametern; Messwerte [Q] Everitt u.a. 2011.
  2. Ein statisches skalares Feldpaar (m, n) hat g_0i = 0 -> Mitführung 0; GP-B schließt 0 mit
     5 sigma aus, LAGEOS (Ciufolini & Pavlis 2004, Nature 431, 958) mit ~10 sigma.
  3. Ein Skalarfeld kann J nicht enthalten: Quelle ist die Massendichte (Skalar); J entsteht erst
     aus dem Massenstrom (Vektor). Symbolisch: Präzession aus skalarem Potential ist ~ x × v,
     unabhängig von omega des Zentralkörpers.
  4. Was die flache Darstellung liefern muss: eine mitgeführte Wegverlängerung. Gordon-Metrik
     eines bewegten Mediums: g~_0i = -(1 - 1/n^2) u_i/c ~ -2(n-1) u_i/c. Mit n - 1 = 2U (gamma = 1)
     und dem ART-Wert g_0i = -2G (J x x)_i/(c^3 r^3) folgt u = (J x x)/(2 M r^2).
  5. Zahlen: Erde und Sonne -- das Mediumfeld läuft am Äquator mit I/(2 M R^2) der
     Rotationsgeschwindigkeit mit und fällt wie 1/r ab.
Standardbibliothek + sympy.
"""
import math
import sympy as sp

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

c = 299792458.0; G = 6.67430e-11
mas_per_yr = 180/math.pi*3600e3*365.25*86400
# Erde (IERS): GM, R, Trägheitsmoment C = 0,3307 M R^2, omega
GMe = 3.986004418e14; Me = GMe/G; Re = 6.3781e6; Ie = 0.3307*Me*Re**2; we = 7.292115e-5
Je = Ie*we
# Sonne: GM, R, I = 0,070 M R^2 (Standardsonnenmodell), siderische Äquatorrotation 25,4 d
GMs = 1.32712440018e20; Ms = GMs/G; Rsun = 6.957e8; Is = 0.070*Ms*Rsun**2; ws = 2*math.pi/(25.4*86400)

print("1. Gravity Probe B (polare Bahn, a = 7027,4 km)")
a = 7027.4e3
geo = 1.5*GMe**1.5/(c**2*a**2.5)*mas_per_yr
fd = G*Je/(2*c**2*a**3)*mas_per_yr          # Mittel über die polare Bahn
check("geodätisch ~6606 mas/Jahr (Everitt: 6606,1)", abs(geo - 6606) < 10, f"{geo:.1f}")
check("Mitführung ~39 mas/Jahr (Everitt: 39,2; Abweichung < 5 % durch Bahn-/Leitsterngeometrie)",
      abs(fd - 39.2)/39.2 < 0.05, f"{fd:.1f}")

print("2. Skalares Feldpaar (m, n) statisch: g_0i = 0  ->  Mitführung = 0")
fd_meas, fd_err = 37.2, 7.2
check("GP-B misst 37,2 +- 7,2 mas/Jahr: Null liegt 5,2 sigma daneben", fd_meas/fd_err > 5, f"{fd_meas/fd_err:.1f} sigma")
lag_ratio, lag_err = 0.99, 0.10
check("LAGEOS: Verhältnis Messung/ART = 0,99 +- 0,10: Null liegt ~10 sigma daneben", lag_ratio/lag_err > 9.5)

print("3. Skalar kann J nicht tragen (symbolisch)")
x, y, z, vx, vy, vz, w, Mx = sp.symbols('x y z v_x v_y v_z omega M', real=True)
r = sp.sqrt(x**2+y**2+z**2)
Phi = -Mx/r                                  # skalares Potential einer starr rotierenden Kugel: hängt nicht von omega ab
grad = sp.Matrix([sp.diff(Phi, q) for q in (x, y, z)])
Om_scalar = sp.Matrix([vx, vy, vz]).cross(grad)*sp.Rational(3, 2)   # geodätische (Thomas/de-Sitter-)Form ~ v x grad Phi
check("Massendichte einer starr rotierenden Kugel ist stationär wie die der ruhenden: das skalare "
      "Potential und die daraus folgende Präzession enthalten omega nicht (Modellaussage)",
      all(sp.diff(comp, w) == 0 for comp in Om_scalar))
Jv = sp.Matrix([0, 0, sp.Symbol('J')]); X = sp.Matrix([x, y, z])
A = Jv.cross(X)/r**3                         # gravitomagnetisches Vektorpotential ~ J x x / r^3
B = sp.Matrix([sp.diff(A[2], y)-sp.diff(A[1], z), sp.diff(A[0], z)-sp.diff(A[2], x), sp.diff(A[1], x)-sp.diff(A[0], y)])
check("Mitführung braucht ein Vektorfeld: rot(J x x / r^3) != 0 (Dipolfeld), aus einem Skalar nicht erzeugbar",
      sp.simplify(B[2].subs({x: 0, y: 0, z: 1})) != 0, f"B_z(0,0,1) = {sp.simplify(B[2].subs({x:0,y:0,z:1}))}")

print("4. Mitgeführte Wegverlängerung (Gordon-Metrik)")
nn, uu, cc, U_ = sp.symbols('n u c U', positive=True)
g0i_gordon = -(1 - 1/nn**2)*uu/cc
lin = sp.series(g0i_gordon.subs(nn, 1 + 2*U_), U_, 0, 2).removeO()
check("g~_0i = -(1 - 1/n^2) u/c mit n = 1 + 2U (gamma = 1) ergibt -4 U u/c in erster Ordnung",
      sp.simplify(lin + 4*U_*uu/cc) == 0, f"{sp.simplify(lin)}")
GG, MM, JJ, rr = sp.symbols('G M J r', positive=True)
u_req = sp.solve(sp.Eq(4*(GG*MM/(cc**2*rr))*uu/cc, 2*GG*JJ*rr/(cc**3*rr**3)), uu)[0]
check("Gleichsetzen mit ART g_0i = -2G (J x x)/(c^3 r^3) (Äquator): u = J/(2 M r)",
      sp.simplify(u_req - JJ/(2*MM*rr)) == 0, f"u = {u_req}")

print("5. Zahlen")
uE = Je/(2*Me*Re); vE = we*Re
uS = Is*ws/(2*Ms*Rsun); vS = ws*Rsun
print(f"     Erde: u(Äquator) = {uE:.1f} m/s, Rotation {vE:.0f} m/s, Verhältnis {uE/vE:.3f}")
print(f"     Sonne: u(Äquator) = {uS:.1f} m/s, Rotation {vS:.0f} m/s, Verhältnis {uS/vS:.3f}")
check("Erde: Mediumfeld am Äquator ~77 m/s = I/(2MR^2) = 0,165 der Rotationsgeschwindigkeit",
      abs(uE - 77) < 2 and abs(uE/vE - 0.3307/2) < 1e-9)
check("Sonne: ~0,035 der Rotationsgeschwindigkeit (stärker zum Kern konzentriert)", abs(uS/vS - 0.035) < 1e-9)
check("Abfall u ~ 1/r: in GP-B-Höhe u = u_R * R/a", abs(Je/(2*Me*a) - uE*Re/a) < 1e-9, f"{Je/(2*Me*a):.1f} m/s")

print(f"\n{ok}/{n} Prüfungen bestanden")
raise SystemExit(0 if ok == n else 1)
