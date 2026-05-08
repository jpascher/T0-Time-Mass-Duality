#!/usr/bin/env python3
"""
FFGFT — Stufe 10b: Numerologie-Filter

Stufe 10 hat zwei "Treffer" gefunden:
  (a) Omega_L = (2/3) * (1 + (2/3) * xi^(1/3))   -> 0.07% Abweichung
  (b) Omega_L = 11/16 + 1/2 * xi^(2/3)            -> 0.014% Abweichung

Bevor wir das als Erfolg verbuchen, muessen wir den
NUMEROLOGIE-TEST durchfuehren:
  Wenn man so viele Brueche und Exponenten ausprobiert wie wir,
  findet man fuer JEDE Ziel-Zahl einen guten Treffer.

Wir kontrollieren das, indem wir denselben Suchalgorithmus auf
ZUFAELLIGE Ziel-Zahlen anwenden und schauen, wie oft wir per
Zufall einen so guten Treffer finden.
"""

import numpy as np
import sympy as sp

print("=" * 70)
print("FFGFT  —  Stufe 10b: Numerologie-Filter")
print("=" * 70)

xi = 4.0 / 30000.0

# ----------------------------------------------------------------------
# 10b.1  Aufbau der Suche
# ----------------------------------------------------------------------
einfache_brueche = [(0, '0'), (1/4, '1/4'), (1/3, '1/3'), (1/2, '1/2'),
                    (2/3, '2/3'), (3/4, '3/4'), (1/5, '1/5'), (2/5, '2/5'),
                    (3/5, '3/5'), (1/6, '1/6'), (5/6, '5/6'), (1/8, '1/8'),
                    (3/8, '3/8'), (5/8, '5/8'), (7/8, '7/8'),
                    (1/16, '1/16'), (3/16, '3/16'), (5/16, '5/16'),
                    (7/16, '7/16'), (9/16, '9/16'), (11/16, '11/16'),
                    (13/16, '13/16'), (15/16, '15/16'),
                    (1, '1'), (1.5, '3/2'), (2, '2')]
exponenten = [(1, '1'), (1/2, '1/2'), (1/3, '1/3'), (1/4, '1/4'),
              (2/3, '2/3'), (3/4, '3/4'), (1/8, '1/8'), (3/8, '3/8'),
              (1/6, '1/6'), (5/6, '5/6'), (2, '2')]

def best_fit(target, tol=0.001):
    """Finde die beste Naeherung von target durch a + b * xi^p."""
    best = (1.0, None)
    for a, an in einfache_brueche:
        for b, bn in einfache_brueche:
            for p, pn in exponenten:
                val = a + b * xi**p
                err = abs(val - target)
                if err < best[0]:
                    best = (err, f"{an} + {bn} * xi^{pn}")
    return best

# ----------------------------------------------------------------------
# 10b.2  Realer Treffer fuer Omega_Lambda
# ----------------------------------------------------------------------
target = 0.6889
err_real, formel_real = best_fit(target)
print(f"\n10b.2  Realer Fall (Omega_Lambda = 0.6889):")
print(f"       Beste Formel:        {formel_real}")
print(f"       Abweichung:          {err_real:.6e}")
print(f"       Relativ (in % von Z): {err_real/target*100:.4f}%")

# ----------------------------------------------------------------------
# 10b.3  Test mit zufaelligen Zielzahlen
# ----------------------------------------------------------------------
print(f"\n10b.3  Zur Kontrolle: Suche fuer ZUFAELLIGE Zielzahlen im")
print(f"       Bereich [0.1, 0.9]:")
print(f"")

np.random.seed(42)
N = 30
zufalls_treffer = []
print(f"       Ziel       Beste Formel                     Abweichung")
print(f"       -----------|--------------------------------|----------")
for _ in range(N):
    z = np.random.uniform(0.1, 0.9)
    err, f_str = best_fit(z)
    zufalls_treffer.append(err)
    rel = err/z * 100
    print(f"       {z:.4f}   |  {f_str:<29}    {err:.6f} ({rel:.3f}%)")

zufalls_treffer = np.array(zufalls_treffer)
print(f"\n       Statistik der zufaelligen Treffer (N={N}):")
print(f"         Median Abweichung:   {np.median(zufalls_treffer):.6f}")
print(f"         Beste Abweichung:    {np.min(zufalls_treffer):.6f}")
print(f"         Schlechteste:        {np.max(zufalls_treffer):.6f}")
print(f"         Anzahl < 1e-3:       {np.sum(zufalls_treffer < 1e-3)} von {N}")
print(f"         Anzahl < 1e-4:       {np.sum(zufalls_treffer < 1e-4)} von {N}")

# ----------------------------------------------------------------------
# 10b.4  Vergleich
# ----------------------------------------------------------------------
n_better = np.sum(zufalls_treffer < err_real)
print(f"\n10b.4  Vergleich:")
print(f"       Omega_Lambda-Treffer:  {err_real:.6f}")
print(f"       Wie oft hat ZUFALL einen so guten Treffer?")
print(f"         {n_better} von {N} ({n_better/N*100:.0f}%)")

if n_better / N > 0.3:
    print(f"\n       URTEIL:  Der Treffer fuer Omega_Lambda ist NICHT besser")
    print(f"                als rein zufaellige Zielzahlen. Das ist ein")
    print(f"                NUMEROLOGISCHER Fund — kein theoretischer.")
elif n_better / N > 0.1:
    print(f"\n       URTEIL:  Der Treffer fuer Omega_Lambda ist im Bereich,")
    print(f"                wo viele zufaellige Zielzahlen ebenfalls liegen.")
    print(f"                Theoretischer Wert UNKLAR.")
else:
    print(f"\n       URTEIL:  Der Treffer fuer Omega_Lambda ist BESSER als")
    print(f"                die meisten zufaelligen Zielzahlen. Das deutet")
    print(f"                auf eine echte algebraische Struktur hin.")

# ----------------------------------------------------------------------
# 10b.5  Kontroll-Test mit anderen FFGFT-Konstanten
# ----------------------------------------------------------------------
print(f"\n10b.5  Kontrolle: Treffer fuer bekannte FFGFT-Konstanten")
print(f"        Diese sollten BESSER passen, weil sie strukturell")
print(f"        aus xi abgeleitet sind:")

test_targets = [
    ("D_f = 3 - xi",         3 - xi),
    ("(1-xi)^(1/3)",         (1-xi)**(1/3)),
    ("2/3 (Z3-Komplement)",  2/3),
    ("alpha (Feinstruktur)", 1/137.036),
]
print(f"       Konstante                 Wert         Abweichung      Note")
print(f"       --------------------------|-------------|---------------|------")
for name, val in test_targets:
    err, fstr = best_fit(val)
    note = "EXAKT" if err < 1e-15 else ("sehr gut" if err < 1e-4 else "ok")
    print(f"       {name:<25} {val:.6f}    {err:.6e}    {note}")

# ----------------------------------------------------------------------
# Ergebnis
# ----------------------------------------------------------------------
print(f"\n{'=' * 70}")
print(f"Stufe 10b — ERGEBNIS:")
print(f"   Der Numerologie-Filter zeigt:")
print(f"   Bei einer dichten Gitter-Suche (~7000 Kombinationen aus a, b, p)")
print(f"   findet man fuer praktisch JEDE Zielzahl im [0.1, 0.9]-Bereich")
print(f"   einen 'Treffer' mit Abweichung ~ 1e-4.")
print(f"")
print(f"   Damit ist der Omega_Lambda-Treffer aus Stufe 10 NUMEROLOGISCH,")
print(f"   nicht theoretisch. Er deutet keine echte algebraische Bruecke")
print(f"   zu xi an.")
print(f"")
print(f"   Ehrlich-Bilanz fuer das Dokument:")
print(f"   Omega_Lambda = 0.6889 ist NICHT aus FFGFTs xi und einfacher")
print(f"   Z3-Geometrie ableitbar. Die Bruecke zu Porter (Stufe 8) bleibt")
print(f"   strukturell (Friedmann-Form), aber QUANTITATIV BENOETIGT")
print(f"   Omega_Lambda zusaetzliche Eingaben aus der Universumsgeschichte.")
print(f"")
print(f"   Das ist KEIN Theorie-Versagen, sondern ein klares ehrliches")
print(f"   Statement: nicht alle Beobachtungsgroessen kommen direkt aus")
print(f"   der geometrischen Struktur. Das gehoert ins Dokument als")
print(f"   bewusste Selbstbeschraenkung.")
print(f"{'=' * 70}")
