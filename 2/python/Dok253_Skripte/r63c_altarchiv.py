"""R63 Nachtrag 3: Altarchiv (1.zip) -- die fruehere, ehrlichere Fassung.

Gesucht war das in den HTML-Seiten importierte Modul t0_period_finding
(Klasse RelativeT0). Es existiert weder im aktuellen Repository noch im
Altarchiv. Die dort beschriebene Funktion steckt stattdessen in:

  t0_rational_optimized.py   Klasse T0RationalSimulatorOptimized
  t0_no_fallback_shore.py    Klasse T0FrameworkSimulator

Beide Skripte muessen im Arbeitsverzeichnis liegen.
"""
import contextlib
import importlib.util
import io
import math
from fractions import Fraction

TESTS = [15, 21, 35, 77, 91, 143, 187, 221, 323, 391,
         437, 667, 899, 1147, 1763, 2021, 3233, 4189, 5561, 7387]


def lade(pfad, name):
    spec = importlib.util.spec_from_file_location(name, pfad)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


# --- (i) Die xi-Bedingung von t0_rational_optimized.py laesst nur r = 2 zu ---
print('(i) t0_rational_optimized.py: Bedingung |omega - pi| < xi*100, xi = 1/100000')
pi, xi = Fraction(355, 113), Fraction(1, 100000)
zul = [r for r in range(2, 75000, 2)
       if abs(Fraction(2) * pi / Fraction(r) - pi) < xi * 100]
print(f'    zugelassene Perioden aus 2..75000: {zul}')
print(f'    Schwelle {float(xi * 100)}; |omega-pi| = pi*|2/r - 1|; r=4 ergaebe '
      f'{float(abs(Fraction(2) * pi / 4 - pi)):.4f}')
assert zul == [2]
print('    -> derselbe Befund wie in der spaeteren Fassung, nur in drei Zeilen')
print('       statt hinter einer Exponentialfunktion. Das Skript benennt es')
print('       im Quelltext selbst: "# Dummy-Resonanz fuer Auswahl" und')
print('       "best_period = min(periods, key=lambda x: x[0])  # Kleinste Periode".')

# --- (ii) t0_no_fallback_shore.py: Ergebnis unabhaengig von xi ---
nf = lade('t0_no_fallback_shore.py', 'nf')
S = nf.T0FrameworkSimulator


def lauf(mode=False, xi_override=None):
    out = []
    for n in TESTS:
        with contextlib.redirect_stdout(io.StringIO()):
            s = S(n, use_theoretical_xi=mode, enable_fallback=False)
            if xi_override is not None:
                s.xi = xi_override
            try:
                r = s.pure_t0_shor_algorithm()
            except Exception:
                r = None
        out.append(bool(r))
    return out


print('\n(ii) t0_no_fallback_shore.py, Fallback aus -- reiner T0-Resonanzweg:')
ref = None
for name, mode, ov in [('adaptiv (1e-5)', False, None),
                       ('old_error_1e4', 'old_error_1e4', None),
                       ('old_error_133e4', 'old_error_133e4', None),
                       ('xi = 4/30000', False, 4 / 30000),
                       ('xi = 1e-2', False, 1e-2),
                       ('xi = 1 (absurd)', False, 1.0),
                       ('xi = 1e6 (absurd)', False, 1e6)]:
    r = lauf(mode, ov)
    if ref is None:
        ref = r
    print(f'     {name:<18} Erfolge {sum(r):2d}/{len(TESTS)}   identisch: {r == ref}')
    assert r == ref
print('     -> das Ergebnis haengt von xi nicht ab, auch nicht bei absurden Werten.')

# --- (iii) Die dokumentierte 48-Bit-Grenze ist die Probedivisionsgrenze ---
print('\n(iii) technical_report.md: "4-48 Bit: 100 %", "50+ Bit: 0 %".')
print('      Im Code: max_check = min(sqrt(N)+1, 2e7 * |xi| / 1e-5)')
for xi_v, lab in [(1e-5, 'adaptiv Standard'), (1e-4, 'old_error_1e4'),
                  (4 / 30000, 'kanonisch'), (1e-6, 'adaptiv gross')]:
    mc = 2e7 * xi_v / 1e-5
    print(f'      xi={xi_v:.3e} ({lab:<17}) -> max_check {mc:9.2e} '
          f'-> N bis {math.log2(mc ** 2):4.1f} Bit')
N = 281475647799167
print(f'\n      Groesste dokumentierte Faktorisierung: N = {N:,} ({math.log2(N):.0f} Bit)')
print(f'      Faktoren 16.777.213 x 16.777.259 (Differenz 46), sqrt(N) = {math.isqrt(N):,}')
assert math.isqrt(N) < 2e7 < math.isqrt(2 ** 50)
print(f'      sqrt(N) < 2e7 -> loesbar;  50 Bit: sqrt = {math.isqrt(2 ** 50):,} > 2e7 -> nicht.')
print('      -> Die Leistungsgrenze ist die Reichweite der fest verdrahteten')
print('         Probedivision im KLASSISCHEN Fallback, nicht eine Eigenschaft')
print('         des Resonanzverfahrens. Einzige reale Wirkung von xi im ganzen')
print('         Zweig: es skaliert diese klassische Suchgrenze linear.')
print('      Nebenbefund: die Testzahlen haben p ~ q (Differenz 46). Fuer solche')
print('      Semiprime ist jedes Verfahren, das nahe sqrt(N) sucht, im Vorteil;')
print('      die Zahlen sind kein neutraler Testsatz.')

print('\nAlle Assertions bestanden.')
