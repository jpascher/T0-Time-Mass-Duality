"""R63: Dok-253-Faktorisierungscode — xi ist im Wirkbereich inert (Filterguete null).

Quelle des geprueften Codes: rsa/factorization_benchmark_library.py
(OptimizedUniversalT0Algorithm, v2.1.0-OPTIMIZED). Der Code wird hier
originalgetreu nachgebildet, damit das Skript ohne die Bibliothek laeuft.
"""
import math
from fractions import Fraction

xi_FFGFT = Fraction(4, 30000)
PI = Fraction(355, 113)        # pi_fraction im Originalcode
THRESHOLD = Fraction(1, 1000)  # self.threshold im Originalcode
RMAX = 2000                    # max_periods im Originalcode


# --- Originalgetreue Nachbildung der beiden entscheidenden Funktionen ---

def resonance_code(r, xi):
    """Wie implementiert: Lorentz-Form 1/(1+|(omega-pi)^2/(4 xi)|)."""
    omega = Fraction(2) * PI / Fraction(r)
    d = omega - PI
    return Fraction(1) / (Fraction(1) + abs(-(d * d) / (Fraction(4) * xi)))


def resonance_dok253(r, xi):
    """Wie in Dok. 253 beschrieben: Gauss-Form exp(-(omega-pi)^2/(4|xi|))."""
    omega = 2 * math.pi / r
    return math.exp(-((omega - math.pi) ** 2) / (4 * abs(float(xi))))


def simple_factorize(n):
    """_simple_factorize: Probedivision bis d < 1000."""
    f, d, t = [], 2, n
    while d * d <= t and d < 1000:
        while t % d == 0:
            f.append(d)
            t //= d
        d += 1
    if t > 1:
        f.append(t)
    return f


def t0_factorize(n, xi, timeout_periods=RMAX):
    """Kontrollflussgetreue Nachbildung von OptimizedUniversalT0Algorithm.factorize."""
    for b in (2, 3, 5, 7):
        g = math.gcd(b, n)
        if g > 1:
            return tuple(sorted((g, n // g))), "trivial_gcd"
    for b in (2, 3, 5, 7):
        period = None
        for r in range(2, min(n, timeout_periods)):
            if pow(b, r, n) == 1:
                if resonance_code(r, xi) > THRESHOLD:
                    period = r
                    break
        if period and period % 2 == 0:
            x = pow(b, period // 2, n)
            if x != n - 1:
                for c in (math.gcd(x - 1, n), math.gcd(x + 1, n)):
                    if 1 < c < n:
                        return tuple(sorted((c, n // c))), "period_resonance"
    return None, "failed"


def control_factorize(n, timeout_periods=RMAX):
    """Identischer Algorithmus OHNE xi und ohne Resonanzpruefung."""
    for b in (2, 3, 5, 7):
        g = math.gcd(b, n)
        if g > 1:
            return tuple(sorted((g, n // g))), "trivial_gcd"
    for b in (2, 3, 5, 7):
        period = None
        for r in range(2, min(n, timeout_periods)):
            if pow(b, r, n) == 1:
                period = r
                break
        if period and period % 2 == 0:
            x = pow(b, period // 2, n)
            if x != n - 1:
                for c in (math.gcd(x - 1, n), math.gcd(x + 1, n)):
                    if 1 < c < n:
                        return tuple(sorted((c, n // c))), "period"
    return None, "failed"


SEMIPRIME = [15, 21, 35, 77, 91, 143, 187, 221, 323, 391,
             437, 667, 899, 1147, 1763, 2021, 3233, 4189, 5561, 7387]


# --- (i) Der Schwellwert verwirft im "optimalen" Bereich nie ---
print("(i) Schwellwert 1/1000 -- verworfene Perioden r aus 2..%d:" % RMAX)
verworfen = {}
for name, xi in [("1/10 (Lib-'optimal')", Fraction(1, 10)),
                 ("1/15 (Lib gross)", Fraction(1, 15)),
                 ("4/30000 (FFGFT)", xi_FFGFT),
                 ("1e-9", Fraction(1, 10**9))]:
    v = sum(1 for r in range(2, RMAX + 1) if resonance_code(r, xi) <= THRESHOLD)
    verworfen[name] = v
    print(f"    xi = {name:<22} {v:4d} / {RMAX - 1}")
assert verworfen["1/10 (Lib-'optimal')"] == 0
assert verworfen["1/15 (Lib gross)"] == 0
assert verworfen["4/30000 (FFGFT)"] == RMAX - 2   # nur r = 2 ueberlebt

# --- (ii) Maximum liegt konstruktiv bei r = 2, fuer jedes xi ---
print("\n(ii) Maximum der Resonanzfunktion:")
for xi in (Fraction(1, 10), xi_FFGFT, Fraction(10**6)):
    best = max(range(2, 200), key=lambda r: resonance_code(r, xi))
    print(f"    xi = {str(xi):<12} argmax_r = {best}   score = {float(resonance_code(best, xi)):.4f}")
    assert best == 2
# Grund: omega - pi = pi*(2/r - 1), exakt null bei r = 2, xi-unabhaengig.
assert resonance_code(2, xi_FFGFT) == Fraction(1)

# --- (iii) xi-Invarianz: im Wirkbereich identisch zum xi-freien Kontrollfall ---
print("\n(iii) Ergebnisvergleich gegen xi-freien Kontrollalgorithmus:")
ctrl = [control_factorize(n)[0] for n in SEMIPRIME]
n_ctrl = sum(1 for x in ctrl if x)
for name, xi in [("1/10 (Lib-'optimal')", Fraction(1, 10)),
                 ("1/15", Fraction(1, 15)),
                 ("1/2 (absurd)", Fraction(1, 2)),
                 ("1e6 (absurd)", Fraction(10**6)),
                 ("4/30000 (FFGFT)", xi_FFGFT),
                 ("1e-9", Fraction(1, 10**9))]:
    res = [t0_factorize(n, xi)[0] for n in SEMIPRIME]
    ok = sum(1 for x in res if x)
    print(f"    xi = {name:<22} == Kontrolle: {str(res == ctrl):<5}  Erfolge {ok:2d}/{len(SEMIPRIME)}")
    if xi >= Fraction(1, 15):
        assert res == ctrl          # xi ohne jede Wirkung
    else:
        assert res != ctrl and ok < n_ctrl   # xi_FFGFT verschlechtert
print(f"    {'Kontrolle (ohne xi)':<27} == Kontrolle: True   Erfolge {n_ctrl:2d}/{len(SEMIPRIME)}")

# Mit xi_FFGFT stammt kein einziger Erfolg aus dem Periodenweg:
wege = [t0_factorize(n, xi_FFGFT)[1] for n in SEMIPRIME]
print(f"    xi = 4/30000: Wege = {dict((w, wege.count(w)) for w in set(wege))}")
assert "period_resonance" not in wege

# --- (iv) Zirkularitaet der Strategiewahl ---
print("\n(iv) _categorize_number_optimized ruft _simple_factorize VOR der xi-Wahl:")
geloest = [n for n in SEMIPRIME if len(simple_factorize(n)) == 2 and max(simple_factorize(n)) < n]
print(f"    bereits vollstaendig faktorisiert bei Strategiewahl: {len(geloest)}/{len(SEMIPRIME)}")
assert len(geloest) == len(SEMIPRIME)

# --- (v) Dok. 253 beschreibt eine andere Funktion als der Code implementiert ---
print("\n(v) Beschreibung (Dok. 253, Gauss) vs. Implementierung (Lorentz), xi = 1/10:")
for r in (2, 3, 5, 10, 50):
    a, b = float(resonance_code(r, Fraction(1, 10))), resonance_dok253(r, Fraction(1, 10))
    print(f"    r = {r:3d}   Code {a:.6f}   Dok253 {b:.6f}")
assert abs(resonance_code(50, Fraction(1, 10)) - Fraction(1, 1000)) > 0  # Code bleibt ueber Schwelle
assert resonance_dok253(50, Fraction(1, 10)) < 1e-3                      # Gauss-Form nicht
print("\n    -> Gleiches Maximum (r = 2), unvereinbare Flanken.")
print("       Mit der in Dok. 253 beschriebenen Gauss-Form waere der Filter wirksam;")
print("       der Code implementiert die Lorentz-Form, die im 'optimalen' Bereich nie greift.")

print("\nAlle Assertions bestanden.")
