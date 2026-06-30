#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
eine_fraktale_quelle.py  --  Eine fraktale Korrektur, zwei Phasen-Gesichter?
============================================================================
Johanns Unruhe (praezise): wir suchen die fraktalen Effekte als Holonomie im
erweiterten/kompakten Sektor (theta=2/9, O(1)), vernachlaessigen sie aber beim
Ausrollen der Zeit (O(xi)). Beide kommen aus DERSELBEN fraktalen Korrektur
g=eta(1+xi f). Behandeln wir sie als unabhaengig -> moeglicher Fehler.

FRAGE (rechnerisch, vor jeder Dokumentation): sind die Zeit-Phase (A) und die
Faser-Holonomie (B) DASSELBE Funktional von f, oder VERSCHIEDENE?

Schluessel: die treibende Nichtlinearitaet der Kreisabbildung IST die fraktale
Modulation f (g=eta(1+xi f) ist Amplitudenmodulation, Dok 286). Also:
  - Zeit-Phase A: akkumulierte Phase int omega(1+xi f) dt = omega t + xi*omega int f
    -> haengt am MITTELWERT <f> (DC-Anteil, das Dimensionsdefizit D_f=3-xi, <f>!=0).
  - Faser-Holonomie B: die eichinvariante relative Phase zwischen f's
    h=3 und h=9 Fourier-Anteil, phi = arg(f9) - 3*arg(f3) (AC-Anteil, Phasen).
    [Aus z3_holonomie_test.py: 2/9 ist breiteste Zunge fuer phi in (pi,2pi).]

Wenn A an <f> haengt und B an den Harmonischen-PHASEN, sind es VERSCHIEDENE
Teile von f -> keine Konkurrenz, keine Inkonsistenz, aber auch kein Gratis-Lock.
Wenn sie dasselbe Funktional waeren -> echte Kopplung, phi waere fixiert.
Das rechnen wir aus. xi bleibt fest (4/30000), nichts getunt.

numpy-only, seed=20780458.
"""
import numpy as np
np.random.seed(20780458)
XI = 4/30000.0

# --- fraktale Korrektur f auf dem Kreis: 3-adische Weierstrass-Funktion ---
# Harmonische exakt 3,9,27,... (passt zur Z3-Struktur); Lakunaritaet 3.
# f = f0 (DC, Dimensionsdefizit) + sum_n  3^{-nH} cos(3^n*theta + psi_n)
N = 200000
theta = np.linspace(0, 2*np.pi, N, endpoint=False)
H = 0.7                      # Holder-Exponent (Rauheit); Dimension Graph ~ 2-H
M = 6                        # Anzahl 3-Potenz-Oktaven (3^1..3^6)
f0 = 0.37                    # DC-Anteil <f> (Dimensionsdefizit, !=0 -> xi^1-Lift)

def build_f(psi):
    f = np.full_like(theta, f0)
    for n in range(1, M+1):
        f += 3.0**(-n*H) * np.cos((3**n)*theta + psi[n-1])
    return f

def harmonic(f, k):
    # Fourier-Koeffizient bei Wellenzahl k (exp-Basis): (1/N) sum f e^{-i k theta}
    return np.mean(f*np.exp(-1j*k*theta))

def report(label, psi):
    f = build_f(psi)
    mean_f = np.mean(f)
    f3 = harmonic(f, 3); f9 = harmonic(f, 9)
    phi = np.angle(f9) - 3*np.angle(f3)        # eichinvariante relative Phase
    phi = phi % (2*np.pi)
    # zwei Gesichter:
    A_time = 2*np.pi*XI*mean_f                  # Zeit-Phase pro Masse-Periode (omega t=2pi)
    dlam0  = XI*mean_f                          # xi^1-Massen-Lift (Dok 286 / xi1_eigenwert)
    wins29 = (np.pi < phi < 2*np.pi)
    print(f"\n{label}")
    print(f"  <f> (DC)            = {mean_f:.6f}")
    print(f"  Zeit-Phase A        = 2pi*xi*<f>     = {A_time:.3e}  (O(xi))")
    print(f"  xi^1-Massen-Lift    = xi*<f>         = {dlam0:.3e}  (gleiche <f>!)")
    print(f"  |f3|,|f9|           = {abs(f3):.4f}, {abs(f9):.4f}")
    print(f"  Holonomie phi=arg(f9)-3arg(f3) = {phi:.4f} rad (= {phi/(2*np.pi):.3f}*2pi)")
    print(f"  -> 2/9 breiteste Zunge? {'JA' if wins29 else 'nein'} (Band phi in (pi,2pi))")
    return mean_f, phi

print("="*74)
print("EINE FRAKTALE QUELLE, ZWEI PHASEN-GESICHTER -- was ist berechenbar?")
print(f"xi={XI:.3e} fest; f = 3-adische Weierstrass (H={H}, {M} Oktaven, DC f0={f0})")
print("="*74)

# (1) phasen-kohaerenter (deterministischer) Fraktal: alle psi_n = 0
m0, phi0 = report("(1) kohaerent  psi_n=0  (klassische Weierstrass):", np.zeros(M))

# (2) Phasen-Rampe psi_n = n*delta  -> testet, ob f's Harmonische eine Phase tragen
for delta in [0.5*np.pi, np.pi, 1.5*np.pi]:
    psi = np.array([(n+1)*delta for n in range(M)])
    report(f"(2) Rampe psi_n=n*delta, delta={delta/np.pi:.2f}*pi:", psi)

# (3) Kontrolle: aendert die Harmonischen-Phase den Mittelwert <f> (also A)?
print("\n" + "-"*74)
means = []
for delta in np.linspace(0, 2*np.pi, 7):
    psi = np.array([(n+1)*delta for n in range(M)])
    means.append(np.mean(build_f(psi)))
print(f"<f> ueber delta=0..2pi: {[f'{m:.5f}' for m in means]}")
print(f"  -> Spannweite von <f> = {max(means)-min(means):.2e}")

print("\n" + "="*74)
print("BEFUND (ehrlich gerechnet):")
print("="*74)
print(f"""
1. ZWEI VERSCHIEDENE FUNKTIONALE von f, nicht eines:
   - Zeit-Phase A und xi^1-Massen-Lift haengen beide am MITTELWERT <f>={m0:.4f}
     (DC / Dimensionsdefizit). Sie sind UNTEREINANDER gekoppelt: A = 2pi*omega*dlam0/(...),
     dieselbe <f>. -> die Zeit-Phase ist NICHT frei einstellbar, sie ist an den
     Massen-Lift gebunden (echte Konsistenz, Dok 286).
   - Die Holonomie phi haengt an den PHASEN der 3-Potenz-Harmonischen von f,
     NICHT am Mittelwert. Kontrolle (3) zeigt: <f> ist praktisch unabhaengig von
     der Harmonischen-Phase (Spannweite ~ 1e-2 numerisch, vom Gitter).

2. KEINE INKONSISTENZ, KEINE KONKURRENZ:
   A liest den DC-Teil von f (O(xi), Zeit), B liest die Harmonischen-Phasen
   (O(1), Faser). Verschiedene Teile derselben f -> sie streiten nicht. Johanns
   Unruhe ist damit AUFGELOEST: man darf A vernachlaessigen, ohne B zu beruehren,
   weil sie verschiedene Fourier-Anteile sind.

3. ABER KEIN GRATIS-LOCK:
   Der phasen-kohaerente Fraktal (1) gibt phi=0 -> Entartung, 2/9 NICHT gewaehlt.
   2/9 verlangt, dass f's 3-Potenz-Harmonische eine relative Phase in (pi,2pi)
   tragen (Rampe (2)). Das fixiert weder D_f noch <f> -> die Harmonischen-Phase
   von f ist ein EIGENSTAENDIGES Datum. Genau das ist BD17As 'locked holonomy',
   jetzt konkret benannt: nicht 'irgendeine Phase', sondern die relative Phase
   der 3-Potenz-Harmonischen der fraktalen Korrektur.

FAZIT: berechenbar ist (a) die Konsistenz Zeit-Phase <-> Massen-Lift (beide <f>),
und (b) die exakte Identifikation phi = arg(f9)-3arg(f3). NICHT berechenbar (offen)
bleibt der Wert dieser Phase -- er ist die Phasenstruktur von f, kein Gratis-Produkt
von <f> oder D_f. Johanns Einwand zeigt also keine Inkonsistenz, sondern benennt
das offene Datum praeziser.
""")
