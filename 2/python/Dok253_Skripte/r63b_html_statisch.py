"""R63 Nachtrag 2: die statischen HTML-Seiten und optimized_harmonic_lib.py.

Geprueft:
  rsa/period-finding-{de,en}.html
  rsa/harmonic-factorization-{de,en}.html
  rsa/libraries-benchmarks-{de,en}.html
  rsa/workflows-{de,en}.html
  rsa/optimized_harmonic_lib.py   (die dort beworbene Bibliothek)

Die Seiten enthalten keinen ausfuehrbaren Code; geprueft werden ihre
numerischen Behauptungen gegen die Bibliothek, auf die sie sich berufen.

Aufruf aus einem Verzeichnis, das optimized_harmonic_lib.py enthaelt.
"""
import contextlib
import importlib.util
import io
import math
import random
import time

spec = importlib.util.spec_from_file_location('ohl', 'optimized_harmonic_lib.py')
ohl = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(ohl)
with contextlib.redirect_stdout(io.StringIO()):
    FAC = ohl.OptimizedHarmonicFactorizer(base_tolerance_cents=50.0)


def sieve(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i, v in enumerate(s) if v]


# --- (i) Faktorisiert wird durch Probedivision, nicht harmonisch ---
print('(i) _find_factors in optimized_harmonic_lib.py:')
import inspect
src = inspect.getsource(FAC._find_factors)
print('    ' + '\n    '.join(l for l in src.strip().split('\n') if 'range' in l or 'n %' in l))
assert 'range(2, sqrt_n + 1)' in src and 'n % i == 0' in src
print('    -> Probedivision. Die harmonische Schicht laeuft DANACH und')
print('       benennt nur noch das Verhaeltnis der bereits gefundenen Faktoren.')

# --- (ii) Die harmonische Klassifikation kann nicht fehlschlagen ---
ratios = sorted({r for r, *_ in FAC.all_sorted_ratios if 1.0 <= r <= 2.0})
cents = sorted(1200 * math.log2(r) for r in ratios)
iv = sorted((c - 50, c + 50) for c in cents)
merged = []
for a, b in iv:
    if merged and a <= merged[-1][1]:
        merged[-1] = (merged[-1][0], max(merged[-1][1], b))
    else:
        merged.append((a, b))
cov = sum(min(b, 1200) - max(a, 0) for a, b in merged if b > 0 and a < 1200)
print(f'\n(ii) Zielverhaeltnisse in der Oktave: {len(cents)}')
print(f'     Abdeckung 0..1200 Cent bei +/-50 Cent Toleranz: '
      f'{cov:.0f}/1200 = {100 * cov / 1200:.1f} %')
assert cov >= 1200


def treffer(x):
    while x >= 2:
        x /= 2
    c = 1200 * math.log2(x)
    return any(abs(c - t) <= 50 for t in cents) or \
           any(abs(c + 1200 - t) <= 50 for t in cents)


P = [p for p in sieve(2000) if p > 3]
random.seed(11)
echt = [max(a, b) / min(a, b) for a, b in
        ((random.choice(P), random.choice(P)) for _ in range(3000))
        if a != b]
zufall = [2 ** random.uniform(0, 1) for _ in range(3000)]
he = 100 * sum(map(treffer, echt)) / len(echt)
hz = 100 * sum(map(treffer, zufall)) / len(zufall)
print(f'     echte Primzahlverhaeltnisse p/q treffen: {he:.1f} %  (n={len(echt)})')
print(f'     zufaellige Verhaeltnisse treffen:        {hz:.1f} %  (n={len(zufall)})')
print(f'     Differenz: {he - hz:+.1f} Prozentpunkte')
assert abs(he - hz) < 0.5 and he > 99.5
print('     -> Die "Erfolgsquote" der Seite misst keine Faktorisierung und')
print('        unterscheidet nicht zwischen Signal und Rauschen. Gleiches')
print('        Argument wie bei der 2-3-5-Glattheit von xi (A010): wenn die')
print('        Fenster den Raum vollstaendig ueberdecken, ist ein Treffer')
print('        strukturell unvermeidbar und traegt keine Evidenz.')

# --- (iii) Komplexitaetsangaben der Seite ---
def semiprime_near(bits):
    def nxt(x):
        while True:
            x += 1
            if all(x % d for d in range(2, int(x ** .5) + 1)):
                return x
    p = nxt(1 << (bits // 2))
    return p * nxt(p)


print('\n(iii) Laufzeitverhalten der Harmonic-Bibliothek.')
print('      Die Seite libraries-benchmarks fuehrt in der Spalte "Speicher"')
print('      O(1) bzw. O(log n) -- das sind SPEICHERangaben und im Kern richtig;')
print('      eine Zeitkomplexitaet nennt die Seite nicht. Gemessen wird hier')
print('      daher nur die tatsaechliche Laufzeit (Zuwachs je +4 Bit;')
print('      bei O(sqrt(n)) sind x4,0 zu erwarten):')
prev, faktoren = None, []
for bits in (24, 28, 32, 36, 40):
    n = semiprime_near(bits)
    t = time.perf_counter()
    with contextlib.redirect_stdout(io.StringIO()):
        FAC.factorize(n)
    dt = (time.perf_counter() - t) * 1000
    if prev:
        faktoren.append(dt / prev)
        print(f'      {bits:3d} Bit  {dt:8.2f} ms   x{dt / prev:.1f}')
    else:
        print(f'      {bits:3d} Bit  {dt:8.2f} ms   -')
    prev = dt
mittel = sum(faktoren) / len(faktoren)
print(f'      Mittlerer Zuwachs: x{mittel:.1f}  ->  O(sqrt(n)).')
print('      Das ist die Laufzeit der Probedivision in _find_factors und damit')
print('      konsistent mit Befund (i); die harmonische Schicht traegt nichts bei.')
assert 3.0 < mittel < 5.5

# --- (iv) Das dokumentierte Beispiel laesst sich nicht ausfuehren ---
print('\n(iv) Die Seiten zeigen als Anwendungsbeispiel:')
print('     from t0_period_finding import RelativeT0')
try:
    import t0_period_finding  # noqa: F401
    print('     Modul vorhanden.')
except ImportError:
    print('     -> Modul t0_period_finding existiert im Repository nicht;')
    print('        auch keine Klasse RelativeT0. Das Beispiel laeuft nicht.')

print('\nAlle Assertions bestanden.')
