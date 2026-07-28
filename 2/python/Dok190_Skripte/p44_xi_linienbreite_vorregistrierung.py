#!/usr/bin/env python3
"""P44 -- Vorregistrierung: xi als Linienbreite der Quanten-Phasenschaetzung.

AUSGANGSLAGE
------------
In allen unter R63 geprueften Implementierungen steht xi im Argument einer
streng monotonen Funktion von r und kann die Auswahl deshalb strukturell nicht
beeinflussen -- eine monotone Reparametrisierung verschiebt kein argmax. Der
Parameter war dort nicht schlecht eingestellt, sondern wirkungslos.

Hier wird die zugrundeliegende Idee an der einzigen Stelle geprueft, an der ein
Breitenparameter etwas tun kann: bei einer verrauschten Messung, mit einem
Fenster um den GEMESSENEN Wert statt um r = 2.

AUFBAU
------
Shor-Phasenschaetzung mit n Zaehlqubits liefert k; der gemessene Phasenwert ist
k/2^n, der wahre Eigenwert s/r. Aus mehreren Schuessen soll r rekonstruiert
werden.

  Referenz  A  Kettenbruchentwicklung von k/2^n (Standardverfahren).
  Variante  B  Zulaessig sind alle r' , bei denen mindestens der Anteil VOTE
               der Schuesse min_s |k/2^n - s/r'| <= w erfuellt; genommen wird
               das kleinste zulaessige r'.

Damit hat w eine echte Rolle: zu klein -> nichts zulaessig -> Fehlschlag;
zu gross -> r' = 1 oder 2 faelschlich zulaessig -> Fehlschlag. Es gibt ein
Optimum. Die Frage ist, ob es bei xi = 4/30000 liegt.

VORREGISTRIERTES KRITERIUM
--------------------------
VOTE ist Teil der Vorregistrierung und wird VOR dem Lauf auf 0,6 festgelegt --
eine neutrale Mehrheit, gewaehlt fuer Rauschrobustheit, nicht abgestimmt.
Gesweept wird ausschliesslich w.

H1 gilt als gestuetzt, wenn ALLE drei Bedingungen erfuellt sind:

  (1) Wirksamkeit    Quote(B, w = xi)  >=  Quote(A) + MARGE
  (2) Lokalisierung  argmax_w Quote(B, w) liegt innerhalb Faktor 3 von xi
  (3) Trennschaerfe  Quote(B, w) faellt bei w = xi/100 und w = xi*100 um
                     mindestens ABFALL unter das Maximum

Bedingung (3) ist die entscheidende: ein Filter, der bei falschen Parameter-
werten nicht fehlschlaegt, misst nichts (R63 (vii)). Sie ist hier erfuellbar
und war es in keiner der unter R63 geprueften Implementierungen.

WARNUNG, DIE ZUM VERFAHREN GEHOERT
----------------------------------
Abschnitt 3 des Laufs zeigt, was passiert, wenn VOTE nachtraeglich mitvariiert
wird: die Lage des Optimums wandert und laesst sich auf xi schieben. Das ist
genau der unter R63 dokumentierte Mechanismus. Der Abschnitt dient der
Abschaetzung der Forscherfreiheitsgrade und geht NICHT in die Bewertung von H1
ein. Wer VOTE nach Sicht der Ergebnisse aendert, hat den Test entwertet.

Standardbibliothek only, deterministisch ueber SEED.
"""
import hashlib
import math
import random
from fractions import Fraction

# ------------------------------------------------ vorregistrierte Parameter
SEED = 20260728
N_COUNT = 12          # Zaehlqubits -> Phasenaufloesung 2^-12 = 2,44e-4
SHOTS = 8             # Messungen je Fall
R_MAX = 120           # groesste betrachtete Kandidatenperiode
NOISE = 0.10          # Anteil vollstaendig zufaelliger Messergebnisse
N_FAELLE = 300
VOTE = 0.60           # vorregistriert, nicht abzustimmen
MARGE = 0.02
ABFALL = 0.10
XI = 4 / 30000

SEMIPRIME = [15, 21, 33, 35, 39, 51, 55, 57, 65, 69, 77, 85, 87, 91, 93,
             95, 111, 115, 119, 123, 129, 133, 141, 143, 145, 155, 159,
             161, 177, 183, 185, 187, 201, 203, 209, 213, 215, 217, 219,
             221, 235, 247, 249, 253, 259, 265, 267, 287, 291, 295]

GITTER = [XI * 10 ** (e / 2) for e in range(-6, 7)]


def ordnung(a, n):
    if math.gcd(a, n) != 1:
        return None
    x, r = a % n, 1
    while x != 1:
        x = (x * a) % n
        r += 1
        if r > n:
            return None
    return r


def qpe_verteilung(s, r, n_count):
    """Exakte Ausgabeverteilung der Phasenschaetzung fuer den Eigenwert s/r."""
    M = 1 << n_count
    phi = s / r
    p = []
    for k in range(M):
        d = phi - k / M
        d -= round(d)
        if abs(d) < 1e-15:
            p.append(1.0)
        else:
            p.append((math.sin(math.pi * M * d) / math.sin(math.pi * d)) ** 2 / (M * M))
    tot = sum(p)
    return [x / tot for x in p]


def ziehe(rng, r, n_count, noise):
    M = 1 << n_count
    if rng.random() < noise:
        return rng.randrange(M)
    s = rng.randrange(r)
    p = qpe_verteilung(s, r, n_count)
    x, acc = rng.random(), 0.0
    for k, pk in enumerate(p):
        acc += pk
        if x <= acc:
            return k
    return M - 1


def kettenbruch_nenner(k, n_count, r_max):
    x = Fraction(k, 1 << n_count)
    nenner, q0, q1 = [], 1, 0
    for _ in range(40):
        ai = math.floor(x)
        q0, q1 = q1, ai * q1 + q0
        if 0 < q1 <= r_max:
            nenner.append(q1)
        rest = x - ai
        if rest == 0:
            break
        x = 1 / rest
    return nenner


def loese_A(messungen, a, n, n_count, r_max):
    zaehler = {}
    for k in messungen:
        for q in kettenbruch_nenner(k, n_count, r_max):
            zaehler[q] = zaehler.get(q, 0) + 1
    for q in sorted(zaehler, key=lambda q: (-zaehler[q], q)):
        if pow(a, q, n) == 1:
            return q
    return None


def min_abstand(phi, r):
    d = phi - round(phi * r) / r
    return abs(d - round(d))


def loese_B(phis, a, n, w, r_max, vote):
    noetig = math.ceil(vote * len(phis))
    for rp in range(1, r_max + 1):
        if sum(1 for phi in phis if min_abstand(phi, rp) <= w) >= noetig:
            return rp if pow(a, rp, n) == 1 else None
    return None


def erzeuge_faelle(rng):
    faelle = []
    while len(faelle) < N_FAELLE:
        n = rng.choice(SEMIPRIME)
        a = rng.randrange(2, n)
        r = ordnung(a, n)
        if r is None or r < 2 or r > R_MAX:
            continue
        faelle.append((n, a, r))
    return faelle


def main():
    rng = random.Random(SEED)
    M = 1 << N_COUNT
    daten = [(n, a, r, [ziehe(rng, r, N_COUNT, NOISE) for _ in range(SHOTS)])
             for n, a, r in erzeuge_faelle(rng)]

    print(f'Faelle {len(daten)}   Zaehlqubits {N_COUNT} (Aufloesung {1/M:.2e})   '
          f'Schuesse {SHOTS}')
    print(f'Rauschen {NOISE:.0%}   r_max {R_MAX}   VOTE {VOTE:.0%} (vorregistriert)   '
          f'Seed {SEED}\n')

    quote_A = sum(1 for n, a, r, ms in daten
                  if loese_A(ms, a, n, N_COUNT, R_MAX) == r) / len(daten)
    print(f'1) Referenz A (Kettenbruch): {quote_A:.1%}\n')

    print('2) Variante B, Sweep ueber die Fensterbreite w:')
    erg = []
    for w in GITTER:
        q = sum(1 for n, a, r, ms in daten
                if loese_B([k / M for k in ms], a, n, w, R_MAX, VOTE) == r) / len(daten)
        erg.append((w, q))
        marke = '   <- w = xi' if abs(w / XI - 1) < 1e-9 else ''
        balken = '#' * round(40 * q)
        print(f'   w = {w:9.3e} ({w/XI:7.3g}*xi)  {q:6.1%} {balken}{marke}')

    w_opt, q_opt = max(erg, key=lambda t: t[1])
    q_xi = [q for w, q in erg if abs(w / XI - 1) < 1e-9][0]
    q_klein = min(q for w, q in erg if w <= XI / 100 * 1.001)
    q_gross = min(q for w, q in erg if w >= XI * 100 * 0.999)

    b1 = q_xi >= quote_A + MARGE
    b2 = max(w_opt / XI, XI / w_opt) <= 3
    b3 = (q_opt - q_klein >= ABFALL) and (q_opt - q_gross >= ABFALL)

    print('\n' + '=' * 68)
    print('VORREGISTRIERTES KRITERIUM')
    print('=' * 68)
    print(f'(1) Wirksamkeit    B(w=xi) {q_xi:.1%}  vs  A {quote_A:.1%} + {MARGE:.0%}'
          f'{"":6}-> {"erfuellt" if b1 else "NICHT erfuellt"}')
    print(f'(2) Lokalisierung  argmax bei w = {w_opt:.3e} = {w_opt/XI:.3g}*xi'
          f'{"":12}-> {"erfuellt" if b2 else "NICHT erfuellt"}')
    print(f'(3) Trennschaerfe  Abfall xi/100: {q_opt-q_klein:.1%}   '
          f'xi*100: {q_opt-q_gross:.1%}{"":10}-> {"erfuellt" if b3 else "NICHT erfuellt"}')
    print()
    if b1 and b2 and b3:
        print('ERGEBNIS: H1 gestuetzt.')
    else:
        print('ERGEBNIS: H1 fuer diesen Aufbau WIDERLEGT.')
        if b3:
            print('  Der Filter ist trennscharf -- er kann fehlschlagen und tut es bei')
            print('  falschen Werten. Das unterscheidet diesen Aufbau von allen unter')
            print('  R63 geprueften. Nur liegt sein Optimum nicht bei xi.')
        if not b1:
            print('  Das Standardverfahren (Kettenbruch) bleibt ueberlegen.')

    print('\n3) Abschaetzung der Forscherfreiheitsgrade  (geht NICHT in H1 ein)')
    print('   Wird VOTE nachtraeglich mitvariiert, wandert die Lage des Optimums:')
    for vote in (0.50, 0.60, 0.75, 1.00):
        beste = max(((w, sum(1 for n, a, r, ms in daten
                             if loese_B([k / M for k in ms], a, n, w, R_MAX, vote) == r)
                      / len(daten)) for w in GITTER), key=lambda t: t[1])
        print(f'   VOTE {vote:4.0%}: Optimum bei w = {beste[0]:.2e} = '
              f'{beste[0]/XI:6.3g}*xi   Quote {beste[1]:.1%}')
    print('   -> Mit zwei freien Stellschrauben laesst sich das Optimum auf xi')
    print('      schieben. Genau dieser Mechanismus ist unter R63 dokumentiert.')
    print('      Deshalb ist VOTE vorregistriert und nach dem Lauf unveraenderlich.')

    h = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
    print(f'\nSHA-256 dieses Skripts: {h}')
    print('Zur Vorregistrierung: Hash vor dem Lauf festhalten.')


if __name__ == '__main__':
    main()
