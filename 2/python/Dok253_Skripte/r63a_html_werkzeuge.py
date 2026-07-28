"""R63 Nachtrag: HTML-Faktorisierungswerkzeuge -- xi ohne Wirkung, Test C nie erfuellbar.

Geprueft:
  2/html/t0_shor_bigint.html          (t0FindPeriod)
  2/html/t0_Shore_simulator.html      (pureT0PeriodFinding)
  2/html/t0_xi_num_algebraisch.html   (xiNum, runComparison/Test C)
  rsa/t0_factorization_demo.html      (nur strukturell, siehe Kommentar unten)

Die JS-Funktionen werden originalgetreu in Python nachgebildet.
Standardbibliothek only.
"""
import math
import random
from math import gcd

XI_FFGFT = 4 / 30000
# Alle xi-Werte, die t0_shor_bigint.html anbietet:
XI_ANGEBOTEN = {
    'canonical 4/30000': 4 / 30000,
    'adaptive <=32 bit': 1e-4,
    'adaptive <=64 bit': 1e-5,
    'adaptive <=128 bit': 1e-6,
    'adaptive  >128 bit': 1e-7,
}
XI_KONTROLLE = {'1e-2 (absurd)': 1e-2, '1 (absurd)': 1.0}


def resonanz(r, xi):
    """t0_shor_bigint.html: Math.exp(-((omega-PI)**2)/(4*Math.abs(xi)))."""
    omega = 2 * math.pi / r
    try:
        return math.exp(-((omega - math.pi) ** 2) / (4 * abs(xi)))
    except OverflowError:
        return 0.0


def t0_find_period(a, N, max_r, xi):
    """Originalgetreu: argmax der Resonanz ueber alle r mit a^r = 1 mod N."""
    best, best_res, count = None, -1.0, 0
    for r in range(1, max_r + 1):
        if pow(a, r, N) == 1:
            res = resonanz(r, xi)
            if res > best_res:
                best_res, best = res, r
            count += 1
            if count >= 1000:
                break
    return best


def extract_factors(a, r, N):
    if r is None or r % 2 != 0:
        return None
    half = pow(a, r // 2, N)
    if half == N - 1:
        return None
    for c in (gcd(half - 1, N), gcd(half + 1, N)):
        if 1 < c < N:
            return tuple(sorted((c, N // c)))
    return None


def faktorisiere(N, xi, max_r=2000):
    for a in (2, 3, 5, 7):
        g = gcd(a, N)
        if g > 1:
            return tuple(sorted((g, N // g)))
        f = extract_factors(a, t0_find_period(a, N, max_r, xi), N)
        if f:
            return f
    return None


SEMIPRIME = [15, 21, 35, 77, 91, 143, 187, 221, 323, 391,
             437, 667, 899, 1147, 1763, 2021, 3233, 4189, 5561, 7387]


# --- (i) Gleitkomma-Underflow: nur r = 2 ueberlebt ---
print('(i) Perioden r aus 1..2000 mit Resonanz > 0 (kein Underflow):')
for name, xi in list(XI_ANGEBOTEN.items()) + list(XI_KONTROLLE.items()):
    nz = [r for r in range(1, 2001) if resonanz(r, xi) > 0.0]
    kurz = str(nz) if len(nz) <= 6 else f'{nz[:5]} ... ({len(nz)} Stueck)'
    print(f'    xi = {name:<20} {kurz}')
for xi in XI_ANGEBOTEN.values():
    assert [r for r in range(1, 2001) if resonanz(r, xi) > 0.0] == [2]

# --- (ii) Folge: das Ergebnis haengt von xi nicht ab ---
print('\n(ii) Faktorisierungsergebnis ueber 20 Semiprime:')
ref = [faktorisiere(n, XI_FFGFT) for n in SEMIPRIME]
n_ref = sum(1 for x in ref if x)
for name, xi in list(XI_ANGEBOTEN.items()) + list(XI_KONTROLLE.items()):
    res = [faktorisiere(n, xi) for n in SEMIPRIME]
    ok = sum(1 for x in res if x)
    print(f'    xi = {name:<20} identisch zu 4/30000: {str(res == ref):<5} Erfolge {ok:2d}/{len(SEMIPRIME)}')
    assert res == ref
print(f'    -> alle angebotenen und alle Kontroll-xi liefern dasselbe ({n_ref}/{len(SEMIPRIME)}).')

# --- (iii) Test C aus t0_xi_num_algebraisch.html kann nie ansprechen ---
print('\n(iii) Test C: |log10(xi_num) - log10(xi^N)| < 0,3')
stufen = [XI_FFGFT ** n for n in range(0, 7)]
print('    Stufe   Wert          Fenster')
for n, v in enumerate(stufen):
    lo, hi = 10 ** (math.log10(v) - 0.3), 10 ** (math.log10(v) + 0.3)
    print(f'    N={n}     {v:.3e}     [{lo:.3e}; {hi:.3e}]')

# xi_num = lcm(p-1,q-1)/(p*q) < 1/2 fuer jedes Semiprim
def xi_num(p, q):
    a, b = p - 1, q - 1
    return (a * b // gcd(a, b)) / (p * q)


primes = [p for p in range(3, 4000)
          if all(p % d for d in range(2, int(p ** .5) + 1))]
werte = []
random.seed(20260728)
for _ in range(4000):
    p, q = random.sample(primes, 2)
    werte.append(xi_num(p, q))
print(f'\n    xi_num-Stichprobe (4000 Semiprime): '
      f'min {min(werte):.4f}  max {max(werte):.4f}')
assert max(werte) < 0.5
treffer = [x for x in werte
           if min(abs(math.log10(x) - math.log10(v)) for v in stufen) < 0.3]
print(f'    Treffer des Kriteriums: {len(treffer)} von {len(werte)}')
assert not treffer
print('    -> Beweis, nicht Statistik: xi_num = lcm(p-1,q-1)/(pq) < 1/2 fuer JEDES')
print('       Semiprim; das naechstgelegene Fenster (N=0) beginnt bei 10^-0,3 =')
print(f'       {10 ** -0.3:.4f} > 1/2. Das Kriterium kann nie erfuellt werden --')
print('       unabhaengig von den Daten. Der Negativbefund in Dok. 253 ist damit')
print('       kein Datenergebnis, sondern eine Eigenschaft des Testaufbaus.')

# --- (iv) rsa/t0_factorization_demo.html: rechnet nicht ---
print('\n(iv) rsa/t0_factorization_demo.html -- struktureller Befund (kein Test noetig):')
for zeile in [
    'factors stammen aus der Nachschlagetabelle knownResults (41 Eintraege),',
    'nicht aus einer Rechnung;',
    'determineSuccess wuerfelt gegen fest verdrahtete Raten',
    '  (t0_optimized_universal/adaptive: success_rate 1.0);',
    'calculateResonance = (0,15 + random()*0,25) * success_boost -- eine Zufallszahl;',
    'iterations, memory_mb und simulateExecutionTime sind ebenfalls Zufall.',
    '-> Die Seite fuehrt keinen Benchmark durch, sie stellt einen dar.',
]:
    print('    ' + zeile)

print('\nAlle Assertions bestanden.')
