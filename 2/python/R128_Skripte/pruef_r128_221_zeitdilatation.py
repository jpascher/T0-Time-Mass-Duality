#!/usr/bin/env python3
"""Prüfskript R128: Dok. 221, Signatur 3 und Falsifikationskriterium 3.

Frage: Folgt aus dem Energieverlustgesetz E(x)=E0*exp(-xi0*x) (Dok. 221,
Gl. energieverlust) eine Abweichung der SN-Lichtkurvendehnung von (1+z)
bei z>2, wie Dok. 221 behauptet (T_obs/T0 = 1+z+z^2/2+...)?
"""
import sympy as sp

xi, x, z, T0, E0 = sp.symbols('xi0 x z T0 E0', positive=True)
ok = 0; n = 0
def check(name, cond):
    global ok, n
    n += 1
    print(f"[{'OK' if cond else 'FEHLER'}] {name}")
    ok += bool(cond)

E = E0*sp.exp(-xi*x)
# Definition der Rotverschiebung: 1+z = E_emit/E_obs
one_plus_z = sp.simplify(E0/E)
check("1+z = exp(xi0 x) exakt aus Gl. energieverlust",
      sp.simplify(one_plus_z - sp.exp(xi*x)) == 0)

# Periode T ~ h/E: gleiche Buchung (T*m=1) -> T_obs/T0 = E0/E
T_ratio = sp.simplify((1/E)/(1/E0))
check("T_obs/T0 = 1+z exakt für alle z (keine z^2-Abweichung)",
      sp.simplify(T_ratio - one_plus_z) == 0)

# Die Reihe 1+z+z^2/2 entsteht nur durch Einsetzen der Linearnäherung xi0 x = z
fehl = sp.series(sp.exp(z), z, 0, 3).removeO()
check("Dok.-221-Reihe = exp(z), d.h. xi0 x := z eingesetzt",
      sp.simplify(fehl - (1+z+z**2/2)) == 0)

# Bei z=2: konsistent ist xi0 x = ln 3, nicht 2
zval = 2
x_kons = sp.log(1+zval)
check("z=2: konsistentes xi0 x = ln3 ≈ 1,099 ≠ 2",
      abs(float(x_kons) - 1.0986) < 1e-3 and float(x_kons) != 2)
check("z=2: konsistente Dehnung = 3,00 (nicht 5 bzw. Faktor 1,5)",
      float(sp.exp(x_kons)) == 3.0)

# Zweite Definition in Sig. 3: (1+z) = 1/(1 - xi0 x) -> weicht ab O((xi0 x)^2)
d2 = sp.series(1/(1-xi*x) - sp.exp(xi*x), x, 0, 3).removeO()
check("1/(1-xi0 x) ≠ exp(xi0 x) ab 2. Ordnung (Definitionen in 221 uneinheitlich)",
      sp.simplify(d2) != 0)

# Nulltest: identische Wellenlängen- und Zeitdehnung -> kein diskriminierender Test
for zz in [0.5, 2, 5, 10]:
    lam = zz + 1
    tdil = float(sp.exp(sp.log(1+zz)))
    check(f"Nulltest z={zz}: Zeitdehnung = Wellenlängendehnung",
          abs(tdil - lam) < 1e-12)

# Tolman bleibt unverändert: (1+z)^-1 * (1+z)^-1 * (1+z)^-2
check("Tolman-Produkt (1+z)^-4 unberührt",
      sp.simplify((1+z)**-1*(1+z)**-1*(1+z)**-2 - (1+z)**-4) == 0)

# DES b = 1.003 ± 0.011 (White et al. 2024) verträglich mit b=1
b, sb = 1.003, 0.011
check("DES b=1,003±0,011 verträglich mit b=1 (<1σ)", abs(b-1)/sb < 1)

print(f"\nErgebnis: {ok}/{n}")
raise SystemExit(0 if ok == n else 1)
