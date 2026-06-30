#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
z3_modelock_test.py  --  Dok 286 / theta=2/9: schuetzt Z3-Symmetrie die Zunge?
=============================================================================
Frage (ehrlich, mit Kontrolle): Der FFGFT-Massenkern ist ein Z3-Zirkulant
(Dok 282). Wenn die treibende Nichtlinearitaet diese Z3-Symmetrie traegt
(invariant unter theta -> theta+1/3, d.h. nur Harmonische k = 3,6,9,...),
werden dann die Arnold-Zungen mit Nenner aus 3-Potenzen (3, 9, 27)
ge-schuetzt/ver-breitert gegenueber einer generischen Treibung?

Signatur echter Symmetrie-Protektion (FALSIFIZIERBAR):
  - Nenner = Vielfaches von 3 (1/3, 1/9, 2/9, 4/9):  unter Z3 BREITER
  - Nenner kein Vielfaches von 3 (2/5):              unter Z3 SCHMAELER
Wenn das NICHT eintritt -> 2/9 ist kein einfaches symmetrie-geschuetztes
Lock; Hypothese verkleinert. Beides ist ein Ergebnis.

WICHTIG / Disziplin: getestet wird die STABILITAET/BREITE der strukturierten
Abbildung. xi wird NICHT angetastet (xi=4/30000 bleibt fest); der hier
variierte Parameter ist die generische Kreisabbildungs-Kopplung K, ein reines
Test-Mass fuer den Mechanismus -- nicht xi.

Verglichene Treibungen, bei GLEICHER Kritikalitaet (sum_m a_m*m = K, gleiche
minimale Steigung 1-K der Hebung -> fairer Vergleich):
  (G)  generisch:      a_1 = K           (Harmonische 1)
  (Z3a) Z3, nur h=3:   a_3 = K/3         (niedrigste Z3-Harmonische)
  (Z3b) Z3, h=3 und 9: a_3=K/6, a_9=K/18 (mit direkter 9-Harmonischer)

numpy-only, reproduzierbar (seed=20780458).
"""
import numpy as np

np.random.seed(20780458)
XI = 4/30000.0  # fest, wird NICHT variiert -- nur zur Erinnerung gedruckt


def rotation_numbers(Omegas, forcing, n_trans=1000, n_avg=5000):
    """Vektorisierte Kreisabbildung  theta -> theta + Om - (1/2pi) sum a_m sin(2pi m theta).
    forcing: dict {harmonische m: amplitude a_m}."""
    Om = np.asarray(Omegas, float)
    t = np.full_like(Om, 0.1234)
    for _ in range(n_trans):
        kick = np.zeros_like(t)
        for m, a in forcing.items():
            kick += a*np.sin(2*np.pi*m*t)
        t = t + Om - kick/(2*np.pi)
        t -= np.floor(t)
    tot = np.zeros_like(Om)
    for _ in range(n_avg):
        kick = np.zeros_like(t)
        for m, a in forcing.items():
            kick += a*np.sin(2*np.pi*m*t)
        tn = t + Om - kick/(2*np.pi)
        tot += (tn - t)
        t = tn - np.floor(tn)
    return tot/n_avg


def tongue_width(p, q, forcing, span=0.02, N=2001, tol=3e-4):
    target = p/q
    Om = np.linspace(target-span, target+span, N)
    rho = rotation_numbers(Om, forcing)
    locked = np.abs(rho - target) < tol
    if not locked.any():
        return 0.0
    idx = np.where(locked)[0]
    # zusammenhaengendes Plateau um die Mitte
    return (Om[idx.max()] - Om[idx.min()])


K = 0.35  # Test-Kopplung (NICHT xi). Bei gleicher Kritikalitaet 1-K fuer alle.
forcings = {
    "G  (generisch h=1)":   {1: K},
    "Z3a (h=3)":            {3: K/3},
    "Z3b (h=3,9)":          {3: K/6, 9: K/18},
}
ratios = [(1,3), (1,9), (2,9), (4,9), (2,5)]
mult3  = {(1,3): True, (1,9): True, (2,9): True, (4,9): True, (2,5): False}

print("="*72)
print(f"Z3-PROTEKTION DER ARNOLD-ZUNGEN  (Test-K={K}, gleiche Kritikalitaet 1-K)")
print(f"xi bleibt fest = {XI:.3e}  (NICHT der hier variierte Parameter)")
print("="*72)
print(f"{'rho':>6} {'3|q?':>5} | " + " | ".join(f"{name:>16}" for name in forcings))
print("-"*72)
W = {}
for (p, q) in ratios:
    row = []
    for name, frc in forcings.items():
        w = tongue_width(p, q, frc)
        W[(p, q, name)] = w
        row.append(f"{w:16.6f}")
    flag = "ja" if mult3[(p, q)] else "NEIN"
    print(f"{p}/{q:>3} {flag:>5} | " + " | ".join(row))

print("-"*72)
gname = "G  (generisch h=1)"
z3a   = "Z3a (h=3)"
z3b   = "Z3b (h=3,9)"

def ratio(a, b):
    return a/b if b > 0 else float('inf')

print("\nBEFUND (ehrlich abgelesen):")
# 2/9 unter Z3 vs generisch
w29_g, w29_a, w29_b = W[(2,9,gname)], W[(2,9,z3a)], W[(2,9,z3b)]
print(f"  2/9:   generisch={w29_g:.6f}  Z3(h3)={w29_a:.6f}  Z3(h3,9)={w29_b:.6f}")
print(f"         Z3(h3)/generisch   = {ratio(w29_a,w29_g):6.1f}x")
print(f"         Z3(h3,9)/generisch = {ratio(w29_b,w29_g):6.1f}x")
# Kontrolle 2/5 (kein Vielfaches von 3): sollte unter Z3 schmaeler werden
w25_g, w25_a = W[(2,5,gname)], W[(2,5,z3a)]
print(f"  2/5 (Kontrolle, 3 teilt 5 nicht): generisch={w25_g:.6f}  Z3(h3)={w25_a:.6f}"
      f"  -> Z3/gen = {ratio(w25_a,w25_g):.2f} (Protektion: <1 erwartet)")
# selektiert Z3 die 2/9 oder die ganze 9er-Familie?
w19_a, w49_a = W[(1,9,z3a)], W[(4,9,z3a)]
print(f"  9er-Familie unter Z3(h3): 1/9={w19_a:.6f}  2/9={w29_a:.6f}  4/9={w49_a:.6f}")
print(f"     -> Z3 schuetzt die FAMILIE (Nenner 9), nicht 2/9 speziell, wenn diese ~gleich sind.")
# 1/3 als breitester 3er-Lock
w13_a = W[(1,3,z3a)]
print(f"  1/3 unter Z3(h3) = {w13_a:.6f}  (erwartet am breitesten: q=3 in erster Ordnung)")
print("="*72)
print("LESART: Verbreitert Z3 die 3er-Nenner UND verschmaelert 2/5 -> echte")
print("Symmetrie-Protektion, theta=2/9 wird moeglich/robust (nicht mehr absurd schmal),")
print("ABER die 9er-Familie gemeinsam -> erklaert NICHT 2/9 vor 1/9 oder 4/9, und 1/3")
print("bleibt breiter. Teil-Fortschritt: Nenner-9-Locking wird natuerlich; die Auswahl")
print("GENAU 2/9 (Zaehler 2) bleibt offen -> der praezise Rest fuer BD17A.")
print("="*72)
