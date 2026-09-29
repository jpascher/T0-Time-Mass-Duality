#!/usr/bin/env python3
"""
pruef_091b_casimir_epstein.py
Exakte Zeta-regularisierte Nullpunktsenergie auf T4 und T4/Z3 (Dok. 091, Anhang "Zeta-Regularisierung").

Dok. 091 setzt E_0^reg = (hbar c / 2) * zeta(-1) mit zeta(s) = sum'_k |k|^-s, führt die Auswertung
aber nur als Skizze. Hier wird zeta(-1) für das Impulsgitter K exakt bestimmt:

    zeta_K(-1) = Z_K(nu = -1)      (Epstein-Zeta, analytisch fortgesetzt)

auf drei unabhängigen Wegen:
  (1) EpsteinLib (Buchheit et al., analytische Fortsetzung numerisch)
  (2) geschlossene Form über die Thetareihe:
        Z_Z4(nu) = 8 (1 - 4^(1-s)) zeta(s) zeta(s-1),              s = nu/2
        Z_D4(nu) = 24 * 2^-s (1 - 2^(1-s)) zeta(s) zeta(s-1)
  (3) Funktionalgleichung  pi^(-nu/2) G(nu/2) Z_K(nu) = pi^(-(d-nu)/2) G((d-nu)/2) Z_K*(d-nu) / covol(K)
      mit dem dualen Gitter K* (konvergente Summe bei d - nu = 5)
Konvention: Impulsgitter K = D4 (Korpus), Orbifold T4/Z3 = fixpunktfreie Z3 (Dok. 314/330).
Da die Z3 auf allen Impulsen != 0 frei wirkt, trägt der Orbifold (invariante Moden eines
Skalarfelds, ohne getwistete Sektoren) genau ein Drittel: zeta_orb(-1) = Z_D4(-1)/3.
Physikalische Energie: E_0^reg = (hbar c / 2) * (2 pi / L) * zeta_K(-1) bei Gitterkonstante L;
verglichen wird hier der dimensionslose Koeffizient.
"""
import numpy as np
import mpmath as mp
from epsteinlib import epstein_zeta

mp.mp.dps = 40
ok = n_t = 0


def check(name, cond, info=""):
    global ok, n_t
    n_t += 1
    ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))


z4 = np.zeros(4)


def Z(nu, B):
    return epstein_zeta(float(nu), np.asarray(B, float), z4, z4).real


D4 = np.array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 1, 1]], float).T
Z4 = np.eye(4)
A4 = np.linalg.cholesky(np.array([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]], float)).T
w = np.exp(2j * np.pi / 3)
A2A2 = np.array([[1, 0, 0, 0], [w.real, w.imag, 0, 0], [0, 0, 1, 0], [0, 0, w.real, w.imag]]).T

s = mp.mpf(-1) / 2
cf_Z4 = 8 * (1 - mp.mpf(4) ** (1 - s)) * mp.zeta(s) * mp.zeta(s - 1)
cf_D4 = 24 * mp.mpf(2) ** (-s) * (1 - mp.mpf(2) ** (1 - s)) * mp.zeta(s) * mp.zeta(s - 1)

print("=" * 76)
print("1. Nulltests: EpsteinLib bei konvergentem nu gegen geschlossene Formeln")
print("=" * 76)
for nu in (6, 8):
    ss = mp.mpf(nu) / 2
    a = 8 * (1 - mp.mpf(4) ** (1 - ss)) * mp.zeta(ss) * mp.zeta(ss - 1)
    b = 24 * mp.mpf(2) ** (-ss) * (1 - mp.mpf(2) ** (1 - ss)) * mp.zeta(ss) * mp.zeta(ss - 1)
    check(f"nu = {nu}: Z4 und D4 auf 1e-12", abs(Z(nu, Z4) - a) < 1e-12 and abs(Z(nu, D4) - b) < 1e-12)

print("\n" + "=" * 76)
print("2. zeta_K(-1) auf drei Wegen")
print("=" * 76)
e_D4, e_Z4 = Z(-1, D4), Z(-1, Z4)
print(f"  D4:  EpsteinLib {e_D4:.15f}   geschlossen {mp.nstr(cf_D4, 15)}")
print(f"  Z4:  EpsteinLib {e_Z4:.15f}   geschlossen {mp.nstr(cf_Z4, 15)}")
check("D4: EpsteinLib = 24*sqrt2*(1-2^(3/2)) zeta(-1/2) zeta(-3/2)", abs(e_D4 - cf_D4) < 1e-12)
check("Z4: EpsteinLib = -56 zeta(-1/2) zeta(-3/2)", abs(e_Z4 - cf_Z4) < 1e-12)


def via_functional_eq(B):
    d, nu = 4, mp.mpf(-1)
    cov = abs(np.linalg.det(B))
    Bdual = np.linalg.inv(B).T
    rhs = mp.pi ** (-(d - nu) / 2) * mp.gamma((d - nu) / 2) * Z(float(d - nu), Bdual) / cov
    return rhs / (mp.pi ** (-nu / 2) * mp.gamma(nu / 2))


fe_D4, fe_Z4 = via_functional_eq(D4), via_functional_eq(Z4)
check("D4: Funktionalgleichung (duales Gitter, nu* = 5) bestätigt", abs(fe_D4 - cf_D4) < 1e-10,
      f"{mp.nstr(fe_D4, 12)}")
check("Z4: Funktionalgleichung bestätigt", abs(fe_Z4 - cf_Z4) < 1e-10, f"{mp.nstr(fe_Z4, 12)}")
check("Vorzeichen: zeta_D4(-1) < 0 (anziehend, wie Gamma(-1/2) < 0 erwarten lässt)", e_D4 < 0)

print("\n" + "=" * 76)
print("3. Orbifold T4/Z3 (fixpunktfreie Z3, Dok. 314/330)")
print("=" * 76)
orb = cf_D4 / 3
print(f"  zeta_orb(-1) = Z_D4(-1)/3 = 8*sqrt2*(1-2^(3/2)) zeta(-1/2) zeta(-3/2) = {mp.nstr(orb, 15)}")
# Kontrolle der Drittelung bei konvergentem nu durch Bahnaufzählung
a0, a1, a2, a3 = -0.5, 0.5, 0.5, 0.5
Hq = np.array([[a0, -a1, -a2, -a3], [a1, a0, -a3, a2], [a2, a3, a0, -a1], [a3, -a2, a1, a0]])
import itertools
seen, tot = set(), 0.0
for c in itertools.product(range(-6, 7), repeat=4):
    if not any(c):
        continue
    v = D4 @ np.array(c, float)
    key = tuple(np.round(v, 6))
    if key in seen:
        continue
    seen |= {key, tuple(np.round(Hq @ v, 6)), tuple(np.round(Hq @ Hq @ v, 6))}
    tot += (v @ v) ** -6
check("Bahnsumme bei nu = 12 = Z_D4(12)/3 (Drittelung durch freie Wirkung)", abs(tot - Z(12, D4) / 3) < 1e-6,
      f"{tot:.10f} vs {Z(12, D4)/3:.10f}")

print("\n" + "=" * 76)
print("4. Vergleich bei gleichem Volumen der Grundmasche (covol = 1)")
print("=" * 76)
res = {}
for name, B in (("D4", D4), ("A4", A4), ("A2+A2", A2A2), ("Z4", Z4)):
    Bn = B / abs(np.linalg.det(B)) ** 0.25
    res[name] = Z(-1, Bn)
for k in sorted(res, key=lambda k: res[k]):
    print(f"  {k:<6} zeta(-1) = {res[k]: .10f}")
check("alle vier Träger: zeta(-1) < 0", all(v < 0 for v in res.values()))
check("Skalierungsgesetz: Z_{cK}(-1) = c * Z_K(-1) (D4, c = 2^-1/4)",
      abs(res["D4"] - 2 ** -0.25 * e_D4) < 1e-12)
order = sorted(res, key=lambda k: abs(res[k]))
print(f"  Betragsreihenfolge (klein -> groß): {', '.join(order)}")

print("\n" + "=" * 76)
print(f"ERGEBNIS: {ok}/{n_t} Prüfungen bestanden")
print("=" * 76)
print("""
  zeta_D4(-1) = 24*sqrt(2)*(1 - 2*sqrt(2)) * zeta(-1/2) * zeta(-3/2)  (exakt, negativ)
  zeta_T4/Z3(-1) = zeta_D4(-1)/3.
  Damit ist die in Dok. 091 als Skizze geführte Zeta-Regularisierung für das
  Korpusgitter geschlossen ausgewertet; die Physik (Vorzeichen, Skalierung 1/L) ist
  die eines Casimir-Terms, der Koeffizient ist gitterabhängig.
""")
assert ok == n_t
