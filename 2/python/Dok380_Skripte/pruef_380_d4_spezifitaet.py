#!/usr/bin/env python3
"""Prüfskript zu Dok. 380 (offene Brücke R95, Dok. 190): adversarieller D4-Spezifitätstest.

Frage: Ist D4 unter vergleichbaren 4D-Trägern ausgezeichnet, und zwar durch Größen,
die nicht an FFGFT-Ergebnisse angepasst sind?

Vergleichsträger (gleiches Volumen der Grundmasche, covol = 1):
  Z4 (kubisch, vgl. GAE-001A), A4, A2+A2, D4 sowie Zufallsgitter.
Kriterien (vorab festgelegt, keine Anpassung an FFGFT-Zahlen):
  K1  Z3-Verträglichkeit (Korpusbedingung, Dok. 330): Es gibt einen Gitterautomorphismus g der Ordnung 3 ohne
      Eigenwert 1; auf T^4 hat g dann |det(1-g)| Fixpunkte (für T^4/Z3 gefordert: 9).
  K2  Kusszahl (Anzahl kürzester Vektoren) – nur Konsistenz, FFGFT nutzt 24 (Dok. 340).
  K3  Gitterenergie = Epstein-Zeta Z(nu) = sum' |v|^-nu bei covol 1 (EpsteinLib,
      Buchheit et al.), für nu = 5, 6, 8: global (Zufallsgitter) und lokal
      (Störungen um D4) — eine parameterfreie Spektralgröße.
Die Epstein-Zeta ist zugleich die spektrale Zeta-Funktion des flachen Torus
(duales Gitter), also eine Operatorgröße im Sinne der GAE-Logik.
"""
import itertools, time
import numpy as np
from epsteinlib import epstein_zeta

rng = np.random.default_rng(20260929)
ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"[{'OK' if cond else 'FEHLER'}] {name}" + (f"  ({info})" if info else ""))

z4 = np.zeros(4)
def norm(B):  # Spalten = Basisvektoren, auf covol 1 skaliert
    return B / abs(np.linalg.det(B)) ** 0.25
def E(B, nu):
    return epstein_zeta(nu, norm(B), z4, z4).real

w = np.exp(2j * np.pi / 3)
def eis(M):  # Z[w]-Modul vom Rang 2 -> reelles 4D-Gitter
    cols = []
    for k in range(2):
        for f in (1, w):
            v = f * M[:, k]
            cols.append([v[0].real, v[0].imag, v[1].real, v[1].imag])
    return np.array(cols).T

L = {
    "D4":   np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]], float).T,
    "A4":   np.linalg.cholesky(np.array([[2, -1, 0, 0], [-1, 2, -1, 0],
                                         [0, -1, 2, -1], [0, 0, -1, 2]], float)).T,
    "A2A2": eis(np.eye(2, dtype=complex)),
    "Z4":   np.eye(4),
}

print("=== Kontrolle: EpsteinLib gegen geschlossene Formeln ===")
import mpmath as mp
s = 3
refZ4 = float(8 * (1 - 4 ** (1 - s)) * mp.zeta(s) * mp.zeta(s - 1))
refD4 = float(24 * 2 ** (-s) * (1 - 2 ** (1 - s)) * mp.zeta(s) * mp.zeta(s - 1))
vZ4 = epstein_zeta(6, np.eye(4), z4, z4).real
vD4 = epstein_zeta(6, L["D4"], z4, z4).real
check("Z4: Epstein(nu=6) = 8(1-4^-2) zeta(3) zeta(2)", abs(vZ4 / refZ4 - 1) < 1e-12, f"{vZ4:.12f}")
check("D4: Epstein(nu=6) = 24·2^-3 (1-2^-2) zeta(3) zeta(2)", abs(vD4 / refD4 - 1) < 1e-12, f"{vD4:.12f}")

print("\n=== K2: Kusszahl aus der Vektoraufzählung ===")
coeffs = np.array(list(itertools.product(range(-3, 4), repeat=4)))
def shortest(B):
    V = coeffs @ B.T
    r = np.einsum("ij,ij->i", V, V)
    r[np.all(coeffs == 0, axis=1)] = np.inf
    m = r.min()
    return coeffs[np.isclose(r, m)], m
kiss = {k: len(shortest(B)[0]) for k, B in L.items()}
check("Kusszahlen D4 = 24, A4 = 20, A2+A2 = 12, Z4 = 8",
      kiss == {"D4": 24, "A4": 20, "A2A2": 12, "Z4": 8}, str(kiss))

print("\n=== K1: Z3-Verträglichkeit (Automorphismus der Ordnung 3 ohne Eigenwert 1) ===")
def z3_autos(B):
    G = B.T @ B
    S, _ = shortest(B)
    found = []
    for idx in itertools.product(range(len(S)), repeat=4):
        g = S[list(idx)].T                      # Bilder der Basisvektoren (in Gitterkoordinaten)
        if abs(round(np.linalg.det(g))) != 1: continue
        if not np.allclose(g.T @ G @ g, G): continue
        if not np.allclose(np.linalg.matrix_power(g, 3), np.eye(4)): continue
        if np.allclose(g, np.eye(4)): continue
        fp = round(abs(np.linalg.det(np.eye(4) - g)))
        if fp != 0:
            found.append(fp)
            return found
    return found
def basis_min(B):
    # auf eine Basis aus kürzesten Vektoren umstellen, falls möglich (für Z4, A4, D4, A2+A2 gegeben)
    return B
res = {}
t0 = time.time()
for k in ["Z4", "A4", "A2A2", "D4"]:
    B = L[k]
    # nur wenn die Basisvektoren selbst kürzeste Vektoren sind, reicht die Suche unter S
    res[k] = z3_autos(B)
print(f"  Suchzeit {time.time()-t0:.1f} s")
check("Z4 und A4 besitzen keine fixpunktfreie Z3 (T^4/Z3 mit 9 Fixpunkten nicht möglich)",
      res["Z4"] == [] and res["A4"] == [], f"Z4 {res['Z4']}, A4 {res['A4']}")
check("A2+A2 und D4 besitzen eine Z3 ohne Eigenwert 1 mit |det(1-g)| = 9 Fixpunkten",
      res["A2A2"] == [9] and res["D4"] == [9], f"A2+A2 {res['A2A2']}, D4 {res['D4']}")

print("\n=== K1': Klassifikation der Ordnung-3-Automorphismen von D4 (vgl. Dok. 330) ===")
BD = L["D4"]; GD = BD.T @ BD
SD, _ = shortest(BD)
auts = [S for S in (SD[list(ix)].T for ix in itertools.product(range(len(SD)), repeat=4))
        if np.allclose(S.T @ GD @ S, GD)]
o3 = [g for g in auts if np.allclose(np.linalg.matrix_power(g, 3), np.eye(4)) and not np.allclose(g, np.eye(4))]
fixfrei = [g for g in o3 if np.linalg.matrix_rank(np.eye(4) - g) == 4]
mit_fixraum = [g for g in o3 if 4 - np.linalg.matrix_rank(np.eye(4) - g) == 2]
fp = {round(abs(np.linalg.det(np.eye(4) - g))) for g in fixfrei}
# Dynkin-Trialität: einfache Wurzeln s1=e1-e2, s2=e2-e3 (Mitte), s3=e3-e4, s4=e3+e4; s1->s3->s4->s1, s2 fest
Sroot = np.array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 1, 1]], float).T
Timg = Sroot[:, [2, 1, 3, 0]]
Tdyn = Timg @ np.linalg.inv(Sroot)
dyn_ok = np.allclose(np.linalg.matrix_power(Tdyn, 3), np.eye(4)) and np.allclose(Tdyn.T @ Tdyn, np.eye(4))
dyn_fix = 4 - np.linalg.matrix_rank(np.eye(4) - Tdyn)
check("|Aut(D4)| = 1152; 80 Elemente der Ordnung 3 = 64 mit 2D-Fixraum + 16 fixpunktfrei mit 9 Fixpunkten; "
      "Dynkin-Trialität hat 2D-Fixraum",
      len(auts) == 1152 and len(o3) == 80 and len(mit_fixraum) == 64 and len(fixfrei) == 16 and fp == {9}
      and dyn_ok and dyn_fix == 2,
      f"|Aut| {len(auts)}, Ord.3 {len(o3)}, Fixraum-2D {len(mit_fixraum)}, fixpunktfrei {len(fixfrei)} {fp}, Dynkin-Fixraum {dyn_fix}")

print("\n=== K3: Gitterenergie (Epstein-Zeta, covol 1) ===")
for nu in (5, 6, 8):
    vals = {k: E(B, nu) for k, B in L.items()}
    order = sorted(vals, key=vals.get)
    check(f"nu = {nu}: D4 hat die kleinste Energie der vier Träger", order[0] == "D4",
          ", ".join(f"{k} {vals[k]:.4f}" for k in order))
# global: Zufallsgitter (allgemein) und Zufallsgitter der Z3-Familie
def rand_general():
    return rng.normal(size=(4, 4))
def rand_eis():
    M = np.array([[1, rng.normal() + 1j * rng.normal()], [0, rng.normal() + 1j * rng.normal()]])
    return eis(M)
def well(B):  # schlecht konditionierte Gitter aussortieren (numerisch teuer, energetisch ohnehin hoch)
    return np.linalg.cond(norm(B)) < 8
for label, gen, N in [("allgemein", rand_general, 300), ("Z3-Familie", rand_eis, 300)]:
    e_min, cnt = np.inf, 0
    while cnt < N:
        B = gen()
        if not well(B): continue
        cnt += 1
        e_min = min(e_min, E(B, 6))
    check(f"Zufallsgitter {label} ({N}): keines unterschreitet D4 bei nu = 6",
          e_min > E(L["D4"], 6), f"bestes {e_min:.4f} vs D4 {E(L['D4'], 6):.4f}")
# lokal: Störungen um D4
eD4 = E(L["D4"], 6)
worse = 0
for _ in range(200):
    X = rng.normal(size=(4, 4))
    B = (np.eye(4) + 1e-2 * X / np.linalg.norm(X)) @ L["D4"]
    worse += E(B, 6) >= eD4 - 1e-12
check("Lokal: 200 zufällige Störungen um D4 erhöhen die Energie ausnahmslos (lokales Minimum)",
      worse == 200, f"{worse}/200")

print("\n=== Einordnung ===")
check("Unter den Z3-verträglichen Trägern (K1) trennt K3 (unabhängig) D4 von A2+A2; K2 nur Konsistenz (24 aus Dok. 340)",
      E(L["D4"], 6) < E(L["A2A2"], 6) and kiss["D4"] == 24)

print(f"\nErgebnis: {ok}/{n}")
raise SystemExit(0 if ok == n else 1)
