"""
pruef_343g_epstein_satzA.py
Prüft Satz A von Dok. 343 gegen die echte vierdimensionale spektrale Zeta-Funktion.

Satz A rechnet im eindimensionalen Analogon (Zerlegung von zeta(s) nach n mod 3)
und bezeichnet das Ergebnis (1 - 3^-s) zeta(s) = L(s, chi_0) als
"spektrale Zeta-Funktion des T4/Z3-Torus".

Hier wird die spektrale Zeta-Funktion des Laplace-Operators auf T4 und auf dem
Orbifold T4/Z3 direkt als Epstein-Zeta-Funktion berechnet (EpsteinLib,
pip install epsteinlib) und mit (1 - 3^-s) zeta(s) verglichen.

Konventionen:
  Impulsgitter K = D4 = {k in Z^4 : sum k_i gerade} (Korpus-Definition der Moden).
  Eigenwerte des Laplace-Operators: lambda_k = |k|^2 (Faktor 4 pi^2 abgetrennt;
  er ändert nur eine Gesamtskala c^-s und ist unten eigens behandelt).
  zeta_T4(s)  = sum'_{k in K} |k|^{-2s} = Z_K(nu = 2s)          (Epstein)
  Z3 wirkt als lineare Gitterautomorphie g (g^3 = 1). Invariante Eigenfunktionen
  entsprechen Z3-Bahnen der Impulse, also
  zeta_orb(s) = (1/3) [ Z_K(2s) + 2 Z_F(2s) ],   F = {k in K : g k = k}.

Zwei Z3-Wirkungen werden geprüft:
  (c) Korpus-Orbifold: fixpunktfreie Z3 auf D4 (Dok. 314, Klasse Spur -2, halbzahlig,
      |det(1-A)| = 9), hier realisiert durch die Hurwitz-Einheit omega -- maßgeblich.
  (a) Dynkin-Trialität (Dok. 314: Klasse Spur 1, halbzahlig; 2D-Fixebene) -- Vergleich.
  (b) freie Drehung (omega, omega^2) auf A2 (+) A2 -- Vergleich mit anderem Gitter.
      -- als Robustheitsprobe: das Ergebnis hängt nicht an der Wahl der Wirkung.
"""
import itertools
import numpy as np
import mpmath as mp
from epsteinlib import epstein_zeta

ok_count = 0
tests = 0


def check(name, cond, detail=""):
    global ok_count, tests
    tests += 1
    ok_count += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))
    return cond


def Z(nu, B):
    """Epstein-Zeta sum'_{v in B Z^n} |v|^-nu (analytisch fortgesetzt)."""
    B = np.asarray(B, float)
    if B.shape[0] != B.shape[1]:          # eingebettetes Untergitter: über Gram-Matrix
        B = np.linalg.cholesky(B.T @ B).T
    n = B.shape[0]
    return epstein_zeta(float(nu), np.asarray(B, float), np.zeros(n), np.zeros(n)).real


def one_d(s):
    return float((1 - mp.mpf(3) ** (-s)) * mp.zeta(s))


# ----------------------------------------------------------------------------
print("=" * 72)
print("1. Nulltest: EpsteinLib gegen geschlossene Formeln")
print("=" * 72)
Z4 = np.eye(4)
D4 = np.array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 1, 1]], float).T  # Spalten = einfache Wurzeln
for s in (3, 4):
    zf = float(8 * (1 - mp.mpf(4) ** (1 - s)) * mp.zeta(s) * mp.zeta(s - 1))
    df = float(24 * mp.mpf(2) ** (-s) * (1 - mp.mpf(2) ** (1 - s)) * mp.zeta(s) * mp.zeta(s - 1))
    check(f"Z^4, nu={2*s}: {Z(2*s, Z4):.12f} = 8(1-4^(1-s))zeta(s)zeta(s-1)", abs(Z(2 * s, Z4) - zf) < 1e-10)
    check(f"D4,  nu={2*s}: {Z(2*s, D4):.12f} = 24*2^-s(1-2^(1-s))zeta(s)zeta(s-1)", abs(Z(2 * s, D4) - df) < 1e-10)

# ----------------------------------------------------------------------------
print("\n" + "=" * 72)
print("2. Z3-Wirkungen konstruieren und prüfen")
print("=" * 72)
# (a) Trialität: permutiert a1 -> a3 -> a4 -> a1, fixiert a2 (Zentralknoten)
A = D4
perm = A[:, [2, 1, 3, 0]]            # Bild der Basis (a1,a2,a3,a4) -> (a3,a2,a4,a1)
T = perm @ np.linalg.inv(A)
check("Trialität: T orthogonal", np.allclose(T @ T.T, np.eye(4)))
check("Trialität: T^3 = 1, T != 1", np.allclose(np.linalg.matrix_power(T, 3), np.eye(4)) and not np.allclose(T, np.eye(4)))
TB = np.linalg.inv(A) @ T @ A
check("Trialität: T bildet D4 auf D4 ab (ganzzahlig in Wurzelbasis)", np.allclose(TB, np.round(TB)))
fixdim = 4 - np.linalg.matrix_rank(T - np.eye(4))
check("Trialität: Fixraum ist zweidimensional", fixdim == 2, f"dim = {fixdim}")


def fixed_sublattice(Bfull, M, R=4):
    """Kürzeste Basis des Fixgitters {v in Bfull Z^n : M v = v} per Aufzählung."""
    n = Bfull.shape[0]
    vecs = []
    for c in itertools.product(range(-R, R + 1), repeat=n):
        if any(c):
            v = Bfull @ np.array(c, float)
            if np.allclose(M @ v, v):
                vecs.append(v)
    vecs.sort(key=lambda v: v @ v)
    basis = [vecs[0]]
    for v in vecs[1:]:
        if np.linalg.matrix_rank(np.array(basis + [v])) > len(basis):
            basis.append(v)
            break
    Bf = np.array(basis).T
    # Primitivität: jeder gefundene Fixvektor muss ganzzahlige Koordinaten in Bf haben
    G = Bf.T @ Bf
    prim = all(np.allclose(c := np.linalg.solve(G, Bf.T @ v), np.round(c)) for v in vecs)
    return Bf, prim


F_T, primT = fixed_sublattice(D4, T)
check("Trialität: Fixgitter-Basis ist primitiv", primT,
      f"Gram = {np.round(F_T.T @ F_T, 6).tolist()}")

# (b) freie Drehung auf A2 (+) A2
w = 2 * np.pi / 3
Rw = np.array([[np.cos(w), -np.sin(w)], [np.sin(w), np.cos(w)]])
A2 = np.array([[1, 0], [-0.5, np.sqrt(3) / 2]]).T
B_A2A2 = np.block([[A2, np.zeros((2, 2))], [np.zeros((2, 2)), A2]])
G_rot = np.block([[Rw, np.zeros((2, 2))], [np.zeros((2, 2)), Rw.T]])
GB = np.linalg.inv(B_A2A2) @ G_rot @ B_A2A2
check("Drehung (omega,omega^2): bildet A2+A2 auf sich ab", np.allclose(GB, np.round(GB)))
check("Drehung: kein Fixvektor ausser 0 (freie Wirkung auf Impulsen)",
      np.linalg.matrix_rank(G_rot - np.eye(4)) == 4)

# (c) fixpunktfreie Z3 auf D4: Linksmultiplikation mit der Hurwitz-Einheit
#     omega = (-1+i+j+k)/2 (D4* = Hurwitz-Ordnung; erhält D4* und damit D4).
#     Liegt in der Trialitäts-Nebenklasse von Aut(D4), hat aber keinen Eigenwert 1
#     (|det(1-g)| = 9 Fixpunkte auf T4) -- im Gegensatz zum Dynkin-Automorphismus (a).
a0, a1, a2, a3 = -0.5, 0.5, 0.5, 0.5
Hq = np.array([[a0, -a1, -a2, -a3], [a1, a0, -a3, a2], [a2, a3, a0, -a1], [a3, -a2, a1, a0]])
HB = np.linalg.inv(D4) @ Hq @ D4
check("Hurwitz-omega: bildet D4 auf D4 ab, orthogonal, Ordnung 3",
      np.allclose(HB, np.round(HB)) and np.allclose(Hq @ Hq.T, np.eye(4))
      and np.allclose(np.linalg.matrix_power(Hq, 3), np.eye(4)))
check("Hurwitz-omega: kein Eigenwert 1, |det(1-g)| = 9",
      np.linalg.matrix_rank(Hq - np.eye(4)) == 4 and round(abs(np.linalg.det(np.eye(4) - Hq))) == 9)
TperA = np.linalg.inv(D4) @ T @ D4
check("Hurwitz-omega liegt in der Korpus-Klasse von Dok. 314 (Spur -2, halbzahlig)",
      abs(np.trace(Hq) + 2) < 1e-12 and not np.allclose(Hq, np.round(Hq)))
check("Dynkin-Trialität liegt in der Klasse Spur 1 (nicht der Korpus-Orbifold)",
      abs(np.trace(T) - 1) < 1e-12)

# ----------------------------------------------------------------------------
print("\n" + "=" * 72)
print("3. Bahnformel direkt gegen Aufzählung (Nulltest der Orbifold-Zeta)")
print("=" * 72)


def zeta_orb(s, B, F):
    full = Z(2 * s, B)
    fix = Z(2 * s, F) if F is not None else 0.0
    return (full + 2 * fix) / 3


def brute_orbits(s, B, M, R):
    n = B.shape[0]
    seen, tot = set(), 0.0
    for c in itertools.product(range(-R, R + 1), repeat=n):
        if not any(c):
            continue
        v = B @ np.array(c, float)
        key = tuple(np.round(v, 6))
        if key in seen:
            continue
        orb = {key, tuple(np.round(M @ v, 6)), tuple(np.round(M @ M @ v, 6))}
        seen |= orb
        tot += (v @ v) ** (-s)
    return tot


s_test = 6  # schnell konvergent, Abbruchfehler klein
bT = brute_orbits(s_test, D4, T, 7)
check(f"Trialität, s={s_test}: Bahnformel {zeta_orb(s_test, D4, F_T):.8f} vs Aufzählung {bT:.8f}",
      abs(zeta_orb(s_test, D4, F_T) - bT) < 1e-4)
bH = brute_orbits(s_test, D4, Hq, 7)
check(f"Hurwitz,   s={s_test}: Bahnformel {zeta_orb(s_test, D4, None):.8f} vs Aufzählung {bH:.8f}",
      abs(zeta_orb(s_test, D4, None) - bH) < 1e-4)
bR = brute_orbits(s_test, B_A2A2, G_rot, 7)
check(f"Drehung,   s={s_test}: Bahnformel {zeta_orb(s_test, B_A2A2, None):.8f} vs Aufzählung {bR:.8f}",
      abs(zeta_orb(s_test, B_A2A2, None) - bR) < 1e-4)

# Geschlossene Form für den Korpus-Orbifold: die Z3 wirkt frei auf allen Impulsen != 0,
# also zeta_orb = Z_D4(2s)/3 = 8 * 2^-s (1 - 2^(1-s)) zeta(s) zeta(s-1).
for s_ in (2.5, 3, 4, 6):
    cf = float(8 * mp.mpf(2) ** (-s_) * (1 - mp.mpf(2) ** (1 - s_)) * mp.zeta(s_) * mp.zeta(s_ - 1))
    check(f"Korpus-Orbifold, s={s_}: zeta_orb = 8*2^-s(1-2^(1-s))zeta(s)zeta(s-1) = {cf:.10f}",
          abs(zeta_orb(s_, D4, None) - cf) < 1e-9)

# ----------------------------------------------------------------------------
print("\n" + "=" * 72)
print("4. Vergleich mit Satz A: (1-3^-s) zeta(s)")
print("=" * 72)
print(f"  {'s':>5} {'1D-Form':>14} {'T4/Z3 Trial.':>14} {'T4/Z3 Hurw.':>14} {'Quot. Trial.':>13}")
rows = []
for s in (2.5, 3, 4, 5, 6):
    a = one_d(s)
    t = zeta_orb(s, D4, F_T)
    r = zeta_orb(s, D4, None)       # fixpunktfreie Z3 auf D4 (Hurwitz)
    rows.append((s, a, t, r))
    print(f"  {s:5} {a:14.8f} {t:14.8f} {r:14.8f} {t/a:13.6f}")

# Eine Gesamtskala c^-s (Normierung 4 pi^2, Kovolumen) kann den Unterschied nicht
# beheben: dann müsste log(zeta_orb / 1D) linear in s sein.
x = np.array([r[0] for r in rows])
y = np.log(np.array([r[2] / r[1] for r in rows]))
coef = np.polyfit(x, y, 1)
resid = np.max(np.abs(y - np.polyval(coef, x)))
check("Trialität: zeta_orb(s) ist NICHT c^-s * (1-3^-s) zeta(s) (log-Quotient nicht linear)",
      resid > 1e-3, f"max. Abweichung von der Geraden = {resid:.3e}")
y2 = np.log(np.array([r[3] / r[1] for r in rows]))
resid2 = np.max(np.abs(y2 - np.polyval(np.polyfit(x, y2, 1), x)))
check("Hurwitz:   zeta_orb(s) ist NICHT c^-s * (1-3^-s) zeta(s)",
      resid2 > 1e-3, f"max. Abweichung von der Geraden = {resid2:.3e}")

# ----------------------------------------------------------------------------
print("\n" + "=" * 72)
print("5. Polstruktur (entscheidend, unabhängig von jeder Normierung)")
print("=" * 72)
# 1D-Form: einziger Pol bei s=1. Vierdimensionale spektrale Zeta: Weyl-Pol bei s = d/2 = 2,
# bei s = 1 regulär (Fixgitter F ist zweidimensional: dessen Pol liegt bei s = 1!).
eps = 1e-4
for label, B, F in (("Trialität", D4, F_T), ("Hurwitz", D4, None), ("Drehung", B_A2A2, None)):
    near2 = zeta_orb(2 + eps, B, F) * eps
    # Weyl: Res_{s=2} = (1/3) * pi^2 / covol(K)  (Res_{nu=d} Z = 2 pi^{d/2}/(Gamma(d/2) covol), nu = 2s)
    weyl = np.pi ** 2 / abs(np.linalg.det(B)) / 3
    check(f"{label}: Pol bei s=2 mit Weyl-Residuum (eps*zeta_orb(2+eps) = {near2:.4f}, "
          f"Weyl {weyl:.4f})", abs(near2 - weyl) < 1e-3 * 1.0 + 5e-4 * weyl)
check("1D-Form: bei s=2 regulär, Wert (8/9) pi^2/6",
      abs(one_d(2) - 8 / 9 * np.pi ** 2 / 6) < 1e-12, f"{one_d(2):.10f}")
near1_rot = zeta_orb(1 + eps, B_A2A2, None) * eps
check(f"Drehung: bei s=1 regulär (eps*zeta_orb(1+eps) = {near1_rot:.2e})", abs(near1_rot) < 1e-3)
near1_tri = zeta_orb(1 + eps, D4, F_T) * eps
covF = np.sqrt(abs(np.linalg.det(F_T.T @ F_T)))
res_fix = (2 / 3) * np.pi / covF          # (2/3) * Res_{s=1} Z_F(2s), d=2
check(f"Trialität: Pol bei s=1 = (2/3)*Residuum des Fixgitters ({near1_tri:.4f} vs {res_fix:.4f})",
      abs(near1_tri - res_fix) < 2e-3)
print(f"  Hinweis Trialität: eps*zeta_orb(1+eps) = {near1_tri:.4f} -- Pol bei s=1 stammt allein")
print("  vom zweidimensionalen Fixgitter (Fixtori der Trialität), nicht von einer 1D-Modenreihe.")

# ----------------------------------------------------------------------------
print("\n" + "=" * 72)
print("ERGEBNIS")
print("=" * 72)
print(f"  {ok_count}/{tests} Prüfungen bestanden.")
print("""
  Für den Korpus-Orbifold (Dok. 314/330) gilt geschlossen
      zeta_T4/Z3(s) = (1/3) Z_D4(2s) = 8 * 2^-s (1 - 2^(1-s)) zeta(s) zeta(s-1).
  Allgemein ist die spektrale Zeta-Funktion des Laplace-Operators auf T4/Z3 eine Bahnsumme
  vierdimensionaler Epstein-Zeta-Funktionen. Sie hat ihren führenden (Weyl-)Pol bei
  s = 2 und lässt sich durch keine Skalierung c^-s auf (1-3^-s) zeta(s) bringen --
  für alle drei geprüften Z3-Wirkungen.
  Satz A von Dok. 343 ist als Aussage über das eindimensionale Analogon bzw. über
  L(s, chi_0) korrekt; die Bezeichnung "spektrale Zeta-Funktion des T4/Z3-Torus"
  trägt die Rechnung nicht.
""")
assert ok_count == tests, "nicht alle Prüfungen bestanden"
