#!/usr/bin/env python3
"""
pruef_381_rekursion_ansaetze.py (Dok. 381)
Vergleich der Berechnungsansätze für die Rekursion xi_{n+1} = xi_n (1 - 100 xi_n)
(Dok. 295, 333, 146; xi_0 = 4/30000 = 1/7500, 100 xi_0 = 1/75).

Ansätze:
  A  exakte Rekursion (Bruchrechnung bis n = 12, danach 120 Stellen mpmath)
  B  Teleskopprodukt  prod_{k<n} (1 - 100 xi_k)  =  xi_n / xi_0   (exakte Identität)
  C  Kontinuum erster Ordnung (Dok. 295):  xi_n ~ 1/(100 (n + 75)) = xi_0/(1 + 100 n xi_0)
  D  Kontinuum zweiter Ordnung: 1/xi_n ~ 100 (n + 75) + 100 ln((n + 75)/75)
  E  aufgelaufener Defekt D(n) = sum 100 xi_k  gegen  ln(1 + n/75) (Dok. 295)
  F  Produkt gegen exp(-D(n)) und gegen 75/(n + 75)
  G  Einzelschritt: Potenzform (D_f/3)^(D_f/2) mit D_f^eff = 2,973 (A040) gegen 1 - 100 xi_0
  H  Lesart als Ein-Schleifen-Lauf: Koeffizient b hängt von der Schrittkonvention ab
  I  Beschränkte Konstante aus Dok. 295 (Masse- gegen Zeitdefekt, ~0,0134) in geschlossener Form: psi'(75)
Alle Prüfungen können fehlschlagen.
"""
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 120
ok = n_tests = 0


def check(name, cond, info=""):
    global ok, n_tests
    n_tests += 1
    ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))


xi0_fr = Fr(4, 30000)
xi0 = mp.mpf(4) / 30000
print("=" * 78)
print("0. Ausgangswerte")
print("=" * 78)
check("xi_0 = 4/30000 = 1/7500, 100 xi_0 = 1/75, K_frak = 74/75",
      xi0_fr == Fr(1, 7500) and 100 * xi0_fr == Fr(1, 75) and 1 - 100 * xi0_fr == Fr(74, 75))

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("A/B. Exakte Rekursion und Teleskopprodukt (Bruchrechnung, n = 1..12)")
print("=" * 78)
x, prod = xi0_fr, Fr(1)
tele_ok = True
for n in range(1, 13):
    prod *= (1 - 100 * x)
    x = x * (1 - 100 * x)
    tele_ok &= (prod == x / xi0_fr)
check("Teleskopidentität prod (1-100 xi_k) = xi_n/xi_0 exakt für n = 1..12", tele_ok,
      f"Nenner bei n=12 hat {int(x.denominator.bit_length()*0.30103)} Dezimalstellen")

# hochgenaue Folge bis n = 10^5
N = 100000
xs = [xi0]
for _ in range(N):
    xs.append(xs[-1] * (1 - 100 * xs[-1]))
check("mpmath-Folge stimmt mit Bruchrechnung bei n = 12 überein",
      abs(xs[12] - mp.mpf(x.numerator) / x.denominator) < mp.mpf(10) ** -100)

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("C/D. Kontinuumsnäherungen gegen exakte Rekursion")
print("=" * 78)
print(f"  {'n':>7} {'xi_n exakt':>14} {'C: 1.Ord.':>14} {'rel.Fehl. C':>12} {'D: 2.Ord.':>14} {'rel.Fehl. D':>12}")
errC, errD = {}, {}
for n in (1, 10, 75, 100, 1000, 10000, 100000):
    ex = xs[n]
    c1 = 1 / (100 * (n + 75))
    d2 = 1 / (100 * (n + 75) + 100 * mp.log(mp.mpf(n + 75) / 75))
    errC[n] = (c1 - ex) / ex
    errD[n] = (d2 - ex) / ex
    print(f"  {n:>7} {mp.nstr(ex, 8):>14} {mp.nstr(c1, 8):>14} {mp.nstr(errC[n], 3):>12} "
          f"{mp.nstr(d2, 8):>14} {mp.nstr(errD[n], 3):>12}")
check("C bei n = 10: Abweichung ~0,15 % (Angabe aus der Diskussion)",
      abs(abs(errC[10]) - mp.mpf("0.0015")) < mp.mpf("0.0002"), f"{mp.nstr(100*errC[10], 4)} %")
check("D ist für alle n genauer als C", all(abs(errD[n]) < abs(errC[n]) for n in errC))
check("C: relativer Fehler bleibt unter 0,5 % (Maximum bei n ~ 100) und fällt danach",
      max(abs(v) for v in errC.values()) < mp.mpf("0.005") and abs(errC[100000]) < abs(errC[100]),
      f"max {mp.nstr(100*max(abs(v) for v in errC.values()), 3)} %, n=1e5: {mp.nstr(100*errC[100000], 3)} %")
check("D: relativer Fehler bei n = 1e5 unter 1e-4", abs(errD[100000]) < mp.mpf("1e-4"),
      f"{mp.nstr(errD[100000], 3)}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("E/F. Aufgelaufener Defekt und Gesamtprodukt")
print("=" * 78)
print(f"  {'n':>7} {'D(n)=S100xi':>13} {'ln(1+n/75)':>13} {'-ln Prod':>13} {'Prod':>13} {'75/(n+75)':>13}")
D = mp.mpf(0)
rows = {}
for n in range(1, N + 1):
    D += 100 * xs[n - 1]
    if n in (1, 10, 75, 100, 1000, 10000, 100000):
        P = xs[n] / xi0
        rows[n] = (D, mp.log(1 + mp.mpf(n) / 75), -mp.log(P), P, mp.mpf(75) / (n + 75))
        r = rows[n]
        print(f"  {n:>7} " + " ".join(f"{mp.nstr(v, 8):>13}" for v in r))
Dn, L, mlnP, P, Pc = rows[100000]
check("Defekt D(n) folgt ln(1+n/75) (n = 1e5: Abweichung < 1 %)", abs(Dn / L - 1) < mp.mpf("0.01"),
      f"D = {mp.nstr(Dn, 8)}, ln = {mp.nstr(L, 8)}")
check("-ln Prod > D(n) (Produkt enthält höhere Ordnungen -ln(1-x) = x + x^2/2 + ...)",
      all(rows[n][2] > rows[n][0] for n in rows))
tri = mp.psi(1, 75) / 2   # sum_{k>=0} 1/(2 (k+75)^2): Grenzwert der Ordnung (100 xi)^2/2
check("-ln Prod - D(n) konvergiert gegen psi'(75)/2 = sum 1/(2(k+75)^2) (Abweichung < 5e-5)",
      abs((mlnP - Dn) - tri) < mp.mpf("5e-5"), f"n=1e5: {mp.nstr(mlnP - Dn, 6)}, psi'(75)/2 = {mp.nstr(tri, 6)}")
check("Prod = xi_n/xi_0 liegt bei 75/(n+75) (n = 1e5: < 2 %)", abs(P / Pc - 1) < mp.mpf("0.02"),
      f"Prod = {mp.nstr(P, 6)}, 75/(n+75) = {mp.nstr(Pc, 6)}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("G. Einzelschritt: Potenzform (A040) gegen 1 - 100 xi_0")
print("=" * 78)
Df = mp.mpf("2.973")
pot = (Df / 3) ** (Df / 2)
lin = 1 - 100 * xi0
check("Potenzform mit D_f^eff = 2,973 trifft 74/75 auf < 3e-5", abs(pot - lin) < mp.mpf("3e-5"),
      f"{mp.nstr(pot, 7)} gegen {mp.nstr(lin, 7)}")
Df_exact = mp.findroot(lambda d: (d / 3) ** (d / 2) - lin, 2.97)
print(f"  exakter D_f^eff mit (D/3)^(D/2) = 74/75: {mp.nstr(Df_exact, 10)}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("H. Lesart als Ein-Schleifen-Lauf: Koeffizient hängt an der Schrittkonvention")
print("=" * 78)
# dxi/dn = -100 xi^2. Wenn ein Schritt n einem Skalenfaktor s entspricht (t = ln mu = n ln s),
# dann dxi/dt = -(100/ln s) xi^2, also b = 100/ln s.
conv = {"Schritt = Faktor e (b = 100)": mp.e,
        "Schritt = Faktor 2 (externe RG-Konvention, Dok. 275)": mp.mpf(2),
        "Schritt = Faktor 3/2 (FFGFT q = 2/3, Dok. 275)": mp.mpf(3) / 2,
        "Schritt = Faktor 10 (Dekade)": mp.mpf(10)}
for k, s in conv.items():
    print(f"  {k:<55} b = {mp.nstr(100 / mp.log(s), 6)}")
check("b ist ohne festgelegte Schrittkonvention nicht eindeutig (Faktor-2- und 3/2-Lesart verschieden)",
      abs(100 / mp.log(2) - 100 / mp.log(mp.mpf(1.5))) > 1)
# A040: Faktor 100 aus dem Lauf über ~17 Dekaden, ln(1e17) ~ 39
print(f"  A040: ln(l_EW/l_P) ~ ln(1e17) = {mp.nstr(mp.log(mp.mpf(10)**17), 5)} -- der Faktor 100 selbst"
      f" stammt dort schon aus einem Skalenlauf")

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("I. Dok. 295: Differenz der kumulierten Defekte Masse/Zeit in geschlossener Form")
print("=" * 78)
# Zeitseite d_t = 100 xi_n, Masseseite d_m = 1/(1-100 xi_n) - 1 (dual_projektion_probe.py);
# d_m - d_t = (100 xi)^2/(1-100 xi); Summe -> sum_{k>=0} 1/(k+75)^2 = psi'(75)
diffsum = mp.mpf(0)
for k in range(N):
    y = 100 * xs[k]
    diffsum += y * y / (1 - y)
tail = mp.mpf(1) / (N + 75)          # Resttail der Summe ~ sum_{k>N} 1/(k+75)^2
lim = diffsum + tail
psi1 = mp.psi(1, 75)
print(f"  Summe bis n=1e5: {mp.nstr(diffsum, 10)},  + Tail: {mp.nstr(lim, 10)},  psi'(75) = {mp.nstr(psi1, 10)}")
check("Beschränkte Konstante aus Dok. 295 (≈0,0134) = psi'(75) = sum 1/(k+75)^2 (rel. < 1e-4)",
      abs(lim / psi1 - 1) < mp.mpf("1e-4") and abs(psi1 - mp.mpf("0.0134")) < mp.mpf("5e-5"),
      f"rel. Abw. {mp.nstr(lim/psi1-1, 3)}")
print("  Hinweis: das ist das Doppelte der Konstante psi'(75)/2 aus E/F.")

print("\n" + "=" * 78)
print(f"ERGEBNIS: {ok}/{n_tests} Prüfungen bestanden")
print("=" * 78)
assert ok == n_tests
