"""R64: t0_no_fallback_shore.py -- Methodentrennung vorhanden, Etikett falsch.

Geprueft: 2/python/t0_no_fallback_shore.py (Klasse T0FrameworkSimulator).

Das Skript fuehrt als einziges im Korpus eine getrennte Buchfuehrung
zwischen dem T0-Zweig und dem klassischen Fallback. Diese Trennung ist
korrekt implementiert. Sie verlaeuft aber zwischen den beiden VERFAHREN,
nicht zwischen "Parameter hat gewirkt" und "Parameter hat nicht gewirkt" --
und der T0-Zweig ist klassische Ordnungssuche.

Das Skript muss im Arbeitsverzeichnis liegen.
"""
import contextlib
import importlib.util
import io
import math
import re

spec = importlib.util.spec_from_file_location('nf', 't0_no_fallback_shore.py')
nf = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(nf)
S = nf.T0FrameworkSimulator

TESTS = [14351, 10403, 143, 187, 221, 323, 391, 437, 667, 899]


def lauf(n, **kw):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        s = S(n, **kw)
        try:
            r = s.pure_t0_shor_algorithm()
        except Exception:
            r = None
    return s, r, buf.getvalue()


# --- (i) Die Trennung ist korrekt implementiert ---
print('(i) Getrennte Buchfuehrung:')
t0 = fb = 0
for n in TESTS:
    s, r, _ = lauf(n, enable_fallback=True)
    t0 += s.t0_success_count
    fb += s.fallback_success_count
print(f'    T0-Zweig: {t0}   klassischer Fallback: {fb}   ueber {len(TESTS)} Faelle')
print('    Die Zaehler werden an getrennten Stellen erhoeht (Z. 376 bzw. 280/300),')
print('    get_statistics() gibt beide plus last_method aus. Korrekt.')

# --- (ii) Alle Resonanzwerte im Log sind exakt null ---
print('\n(ii) Resonanzwerte, die der T0-Zweig selbst protokolliert:')
alle = []
for n in TESTS:
    s, r, log = lauf(n, enable_fallback=False)
    alle += [float(x) for x in re.findall(r'Resonance=([0-9.]+)', log)]
nz = [x for x in alle if x != 0.0]
print(f'    protokollierte Werte: {len(alle)}   davon ungleich 0,0: {len(nz)}')
assert alle and not nz
print('    Alle exakt 0,000000. exp(-(omega-pi)^2/(4*xi)) unterlaeuft fuer jedes')
print('    r != 2 die Gleitkommadarstellung (R63 (va)).')
print('    max(periods, key=lambda x: x[1]) ueber eine Nullliste gibt das erste')
print('    Element zurueck -- also die kleinste Periode. Klassische Ordnungssuche.')

# --- (iii) Das Etikett ---
s, r, log = lauf(14351, enable_fallback=False)
print('\n(iii) Etikett des so erzielten Erfolgs:')
for zeile in log.split('\n'):
    if 'Method:' in zeile or 'Best Period' in zeile or 'PURE T0' in zeile:
        print('    ' + zeile.strip())
assert s.last_success_method == 'pure_t0_physics'
print("    -> gebucht als 'pure_t0_physics' bei durchgaengig verschwindender")
print('       Resonanz. Das Verfahren ist korrekt, die Bezeichnung nicht.')

# --- (iv) Buchungsluecke beim gcd-Kurzschluss ---
print('\n(iv) gcd-Kurzschluss:')
luecke = 0
for n in (15, 21, 35, 33, 39, 51, 55, 57):
    s, r, _ = lauf(n, enable_fallback=True)
    if r and r.get('method') == 'gcd_shortcut' and r.get('success'):
        if s.t0_success_count == 0 and s.fallback_success_count == 0:
            luecke += 1
print(f'    Erfolge ueber gcd_shortcut ohne Zaehlung in einem der beiden Zaehler: {luecke}')
if luecke:
    print('    -> t0_success_rate rechnet ueber eine Gesamtzahl, die diese Erfolge')
    print('       nicht enthaelt. Kleine Buchungsluecke, kein Fehler im Ergebnis.')

# --- (v) Wo xi in dieser Datei ueberhaupt wirkt ---
print('\n(v) Wo xi in dieser Datei wirkt:')
print('    Nicht in der Periodenauswahl (siehe (ii)), sondern zweimal als')
print('    Schleifengrenze:')
print('      Z. 287  max_check    = min(sqrt(N)+1, 2e7   * |xi| / 1e-5)   Fallback')
print('      Z. 311  search_range = min(N,         1e5   * |xi| / 1e-5)   Basiswahl')


def basis(N, xi, bereich=None):
    sr = bereich if bereich else min(N, int(100000 * abs(xi) / 1e-5))
    best, mx = 2, 0
    for a in range(2, sr):
        if math.gcd(a, N) != 1:
            continue
        tot = ((1 + abs(xi) * a) * abs(math.cos(2 * math.pi * a / N))
               * (1 + math.sin(math.pi * a / math.sqrt(N)) * 0.3)
               * (1 + abs(xi) / max(1, a / 1000) ** 2))
        if tot > mx:
            mx, best = tot, a
    return best, sr


N = 14351
print(f'\n    Basiswahl fuer N = {N}, Suchbereich wie im Code:')
for xi in (1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2):
    b, sr = basis(N, xi)
    print(f'      xi = {xi:.0e}   Bereich {sr:6d}   Basis {b}')
print('\n    Dieselbe Rechnung mit FESTEM Bereich -- wirkt xi dann noch?')
gewaehlt = []
for xi in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1.0):
    b, _ = basis(N, xi, bereich=min(N, 100000))
    gewaehlt.append(b)
    print(f'      xi = {xi:<8.0e} Basis {b}')
assert len(set(gewaehlt)) == 1
print('    -> ueber sechs Groessenordnungen dieselbe Basis. Die Gewichtung')
print('       saettigt; wirksam ist allein die Bereichsgrenze.')
print('\n    Befund: xi tritt in dieser Datei zweimal als Schleifengrenze auf')
print('    und keinmal als wirksames Auswahlkriterium. Wo es das Ergebnis')
print('    aendert, aendert es, WIE WEIT gesucht wird -- nicht, WAS gewaehlt wird.')

# --- (vi) Vorschlag: zweite Trennebene ---
print('\n(vi) Vorschlag fuer die zweite Trennebene:')
print('     Die vorhandene Trennung unterscheidet T0-Zweig / Fallback.')
print('     Zu ergaenzen waere die Trennung "Parameter wirksam / unwirksam":')
print('     ein Lauf mit veraendertem xi bei sonst gleichen Schleifengrenzen')
print('     muss ein anderes Ergebnis liefern, sonst war xi am Ergebnis')
print('     unbeteiligt. Genau diese Zeile fehlt im Bericht und haette den')
print('     Befund von R63 unmittelbar sichtbar gemacht.')

print('\nAlle Assertions bestanden.')
