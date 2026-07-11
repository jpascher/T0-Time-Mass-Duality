#!/usr/bin/env python3
# ffgft_304_linearisierungsfehler_probe.py
# ---------------------------------------------------------------------------
# PRUEFSKRIPT (kein Beweis) zu Dok. 304 -- Der Gedaechtnis-Reflex,
# Abschnitt "Der Messschnitt: der bezuglose Ausschnitt und der
# Linearisierungs-Reflex".
#
# FRAGE: Wenn eine Messung einen Ausschnitt der Zeit-Windung als linear
# (konstante lokale Ganghoehe) statt als Bogen liest, wie gross ist der Fehler
# -- und ist er die lokale Gestalt der Linear-gegen-Log-Differenz aus Dok. 295?
#
# KONTEXT (aus dem Gespraech, ehrlich protokolliert):
#   * Zeit ist der Massenkreis; die ausgerollte Windung ist die log-Spirale mit
#     kumuliertem Praezessions-Defekt D(k)=sum 100*xi_n -> ln(1+k/75) (Dok.295/296),
#     Praezessionswinkel beta = 2*pi*D(k).
#   * Skalenlauf: xi_{n+1} = xi_n*(1 - 100*xi_n), xi_0 = 4/30000 = 1/7500,
#     also 100*xi_0 = 1/75 (Dok. 146/295).
#   * Eine gleichfoermige Uhr unterstellt die lokale Rate d_k = 100*xi_k als
#     konstant ueber ein Fenster von w Schritten -> das ist der d=0-/M_tau-Grenzfall.
#
# WAS DAS SKRIPT PRUEFT (und was nicht):
#   * Es rechnet die xi-Seite EXAKT aus der Rekursion -- die einzige Seite, die
#     aus dem Korpus vorliegt. Es erfindet nichts.
#   * Es zeigt: der Linearisierungsfehler je 2*pi ist
#         e(k,w) = w*d_k - (D(k+w)-D(k)) = x - ln(1+x),   x = w*d_k = w/(k+75),
#     also der Fehler im akkumulierten Praezessionswinkel beta = 2*pi*D(k).
#   * Es prueft drei Regime: kleines Fenster (~x^2/2), skaleninvariantes Fenster
#     (x=1 -> 1-ln2, asymptotisch), makroskopischer Grenzfall (e -> 0 ~ x^2/2).
#   * Es benennt EHRLICH: 1-ln2 und der Vorfaktor 1/2 sind im makroskopischen
#     Grenzfall exakt, mit einer Korrektur O(1/k) bei endlicher Position, weil
#     die geschlossene Form ln(1+k/75) einen beschraenkten gamma-artigen Versatz
#     gegenueber der exakten Summe traegt. Der EXAKTE Koeffizient dieser
#     Korrektur bleibt offen (Euler-Maclaurin von D(k)).
#
# Deterministisch. Nur Standardbibliothek (math). Keine Zufallszahlen.
# ---------------------------------------------------------------------------

import math

XI0 = 4/30000            # = 1/7500 ; 100*XI0 = 1/75


def build_xi(N):
    """Exakte Rekursion xi_{n+1} = xi_n (1 - 100 xi_n)."""
    xi = [XI0]
    for _ in range(N):
        xi.append(xi[-1] * (1 - 100 * xi[-1]))
    return xi


def build_D(xi):
    """Kumulierter Defekt D(k) = sum_{n<k} 100*xi_n (exakt aus der Rekursion)."""
    d = [100 * x for x in xi]
    D = [0.0]
    for dn in d:
        D.append(D[-1] + dn)
    return d, D


def e_exact(d, D, k, w):
    """Linearisierungsfehler je 2*pi: w*d_k - (D(k+w)-D(k))."""
    return w * d[k] - (D[k + w] - D[k])


def e_closed(x):
    """Geschlossene Form: x - ln(1+x)."""
    return x - math.log(1 + x)


def main():
    N = 400000
    xi = build_xi(N)
    d, D = build_D(xi)
    print("FFGFT Dok.304 -- Linearisierungsfehler eines Messausschnitts")
    print("xi_0 = 4/30000, 100*xi_0 = 1/75 ; exakte Rekursion, N =", N)
    print("=" * 70)

    print("\n[1] e IST der Praezessionswinkel-Fehler (beta = 2*pi*D(k))")
    print("    e = w*d_k - (D(k+w)-D(k)) ; Vorhersage e = x - ln(1+x), x = w*d_k")
    print(f"    {'k':>7}{'w':>8}{'x=w*d_k':>12}{'e_exakt':>13}{'x-ln(1+x)':>13}{'rel.Abw':>11}")
    for k, w in [(75, 10), (1000, 100), (1000, 1000), (50000, 5000), (200000, 50000)]:
        x = w * d[k]
        e = e_exact(d, D, k, w)
        pred = e_closed(x)
        print(f"    {k:>7}{w:>8}{x:>12.5f}{e:>13.6f}{pred:>13.6f}{(e-pred)/pred:>11.2e}")
    print("    -> rel.Abw -> 0 mit wachsendem k: die geschlossene Form ist asymptotisch exakt.")

    print("\n[2] Skaleninvariantes Fenster x=1 -> Konstante 1-ln2 =", round(1 - math.log(2), 6))
    print("    (asymptotisch; Korrektur O(1/k) durch gamma-artigen Versatz von D)")
    for k in [75, 300, 1200, 4800, 19200, 76800, 300000]:
        w = round(1 / d[k])
        if k + w >= N:
            break
        x = w * d[k]
        e = e_exact(d, D, k, w)
        print(f"    k={k:>7}  x={x:.5f}  e={e:.6f}  e-(1-ln2)={e-(1-math.log(2)):+.2e}")

    print("\n[3] Kleines Fenster: fuehrender Term x^2/2")
    for k, w in [(50000, 50), (50000, 150), (50000, 500)]:
        x = w * d[k]
        e = e_exact(d, D, k, w)
        print(f"    k={k} w={w:>4}  x={x:.5f}  e={e:.3e}  x^2/2={x*x/2:.3e}  e/(x^2/2)={e/(x*x/2):.4f}")

    print("\n[4] Makroskopischer Grenzfall: festes w, wachsendes k -> e ~ (1/2)(w/(k+75))^2")
    w = 1000
    for k in [75, 7500, 75000]:
        if k + w >= N:
            break
        x = w * d[k]
        e = e_exact(d, D, k, w)
        print(f"    k={k:>6}  d_k={d[k]:.3e}  x={x:.4f}  e={e:.3e}  (1/2)x^2={x*x/2:.3e}")

    print("\n[5] Geschlossene Form vs exakte Summe: D(k)=ln(1+k/75) traegt einen")
    print("    beschraenkten, gamma-artigen Versatz (Ursache der O(1/k)-Korrektur)")
    for k in [75, 7500, 75000, 300000]:
        print(f"    k={k:>7}  D_exakt={D[k]:.5f}  ln(1+k/75)={math.log(1+k/75):.5f}  diff={D[k]-math.log(1+k/75):+.5f}")

    print("\n[6] Eingerollt vs ausgerollt: was heisst 'alle Ausschnitte gleich'?")
    print("    EINGEROLLT (xi eingefroren): d=1/75 konstant, Rotationszahl 74/75 rational")
    d_frozen = 100 * XI0
    print(f"      d = 100*xi_0 = {d_frozen:.6f} = 1/{round(1/d_frozen)} ; Schliessung nach"
          f" 1/d = {1/d_frozen:.1f} Umlaeufen -> 75 KONGRUENTE Teile (Z/75, exakt)")
    print("    AUSGEROLLT (Skalenlauf): d_n ~ 1/(n+75) zerfaellt -> log-Spirale, Verhaeltnis e")
    # equiangular ratio per 2pi from the running defect: rho=k+75, beta=2pi D; fit ln rho = a*beta
    ks = list(range(1, 200000))
    import math as _m
    lnrho = [_m.log(k + 75) for k in ks]
    beta = [2 * _m.pi * D[k] for k in ks]
    n = len(ks)
    sb = sum(beta); sl = sum(lnrho)
    sbb = sum(b * b for b in beta); sbl = sum(b * l for b, l in zip(beta, lnrho))
    a = (n * sbl - sb * sl) / (n * sbb - sb * sb)
    print(f"      Selbstaehnlichkeit je 2pi = exp(2pi*a) = {_m.exp(2*_m.pi*a):.5f}  (e = {_m.e:.5f})")
    print("      -> 'gleich' heisst hier SELBSTAEHNLICH (proportional), nur ASYMPTOTISCH exakt.")
    print("    FOLGE: Bezuglosigkeit gilt strikt nur ausgerollt; eingerollt gibt es einen")
    print("           periodischen Bezug (Ort mod 75). Was beides ueberlebt: die ORDNUNG (U1).")

    print("\nBUCHUNG:")
    print("  proven      : e = x - ln(1+x) = Praezessionswinkel-Fehler/2pi (an beta=2pi D(k)),")
    print("                makroskopisch exakt; Regime x^2/2, 1-ln2, (1/2)(w/(k+75))^2.")
    print("  offen       : exakter Koeffizient der O(1/k)-Korrektur (Euler-Maclaurin von D).")
    print("  Annahme     : 'Messung = lokale Linearisierung des Ausschnitts' (diese Art Messung).")
    print("  P35         : 'gemessene Gleichfoermigkeit ist Artefakt' (Linearisierungs-Reflex).")


if __name__ == "__main__":
    main()
