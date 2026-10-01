#!/usr/bin/env python3
"""
pruef_385_higgs_vakuum.py -- Dok. 385: Der Higgs-Vakuum-Weg zu xi.

Prüft die Formeln der Entwicklungslinie 2025/2026 (Git-Historie) und den
heutigen Stand: xi_EFT = lambda_h^2 v^2/(16 pi^3 m_h^2) = m_h^2/(64 pi^3 v^2)
als Konsistenzprüfung von xi = 4/30000. Konstanten CODATA 2022, PDG 2024.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

pi = math.pi
xi = 4 / 30000
e = 1.602176634e-19; hbar = 1.054571817e-34; c = 299792458.0
eps0 = 8.8541878188e-12; mu0 = 1.25663706127e-6
alpha = 1 / 137.035999177

def xi_eft(mh, v, lam=None):
    lam = mh**2 / (2 * v**2) if lam is None else lam
    return lam**2 * v**2 / (16 * pi**3 * mh**2)

print("1. Vakuumkonstanten (Ausgangsidee Feb. 2025)")
check("c = 1/sqrt(mu0 eps0)", abs(1 / math.sqrt(mu0 * eps0) / c - 1) < 1e-9)
check("alpha = e^2/(4 pi eps0 hbar c)", abs(e**2 / (4 * pi * eps0 * hbar * c) / alpha - 1) < 1e-9)
Z0 = math.sqrt(mu0 / eps0)
check("Z0 = sqrt(mu0/eps0) = 376,73 Ohm (nicht dimensionslos)", abs(Z0 - 376.73) < 0.01)

print("\n2. Higgs-Ausdruck (5. April 2025) und heutige Form")
mh, v = 125.20, 246.22
lam = mh**2 / (2 * v**2)
check("lambda_h = m_h^2/(2 v^2) = 0,1293", abs(lam - 0.1293) < 0.0001, f"{lam:.4f}")
x = xi_eft(mh, v)
check("xi_EFT = m_h^2/(64 pi^3 v^2) = lambda_h/(32 pi^3)", abs(x - mh**2 / (64 * pi**3 * v**2)) < 1e-18 and abs(x - lam / (32 * pi**3)) < 1e-18)
check("xi_EFT = 1,30e-4 (PDG 2024)", abs(x - 1.303e-4) < 0.001e-4, f"{x:.4e}")
check("Abstand zu 4/30000: -2,3 %", abs((x / xi - 1) * 100 + 2.3) < 0.05, f"{(x/xi-1)*100:+.2f} %")
spread = [(xi_eft(a, b) / xi - 1) * 100 for a, b in ((125.1, 246.2), (125.25, 246.22), (125.09, 246.0))]
r129 = (xi_eft(125.1, 246.2, 0.129) / xi - 1) * 100
check("Spanne je nach Eingaben -2,2 ... -2,4 %, mit gerundetem lambda 0,129: -2,6 %",
      all(-2.45 < s < -2.15 for s in spread) and abs(r129 + 2.56) < 0.02, f"{[round(s,2) for s in spread]}, {r129:.2f}")

print("\n3. Vakuumformel vom 6. April 2025")
vak = lam**2 * v**2 / (64 * pi**4 * mh**2) * (e**2 / (eps0 * hbar * c))   # lambda^2 v^2 e^2/(64 pi^4 eps0 hbar c m_h^2)
check("dimensionslos, = xi_EFT * alpha", abs(vak / (x * alpha) - 1) < 1e-9)
check("SI-Wert 9,5e-7, nicht 1", abs(vak - 9.51e-7) < 0.02e-7, f"{vak:.3e}")
vak_a1 = lam**2 * v**2 / (64 * pi**4 * mh**2) * 4 * pi     # alpha = 1: e^2 = 4 pi eps0 hbar c
check("mit alpha = 1: genau xi_EFT", abs(vak_a1 / x - 1) < 1e-12)
check("64 pi^4 = 16 pi^3 * 4 pi (4 pi aus 4 pi eps0)", abs(64 * pi**4 - 16 * pi**3 * 4 * pi) < 1e-9)
betaT = x / xi
check("beta_T = xi_EFT/xi = 0,977 (nicht 1); beta_T alpha = 0,0071", abs(betaT - 0.977) < 0.001 and abs(betaT * alpha - 0.00713) < 0.0001, f"{betaT:.4f}")

print("\n4. Variante mu0/eps0 (18. April 2025)")
lam0 = 1 / mh            # hbar/(m_h c) in natürlichen Einheiten, GeV^-1
bt = lam**2 * v**2 / (4 * pi**2 * lam0**2)     # alpha0 = 1
check("lambda_h^2 v^2/(4 pi^2 lambda0^2): Dimension GeV^4, Wert ~4e5", abs(bt / 4.0e5 - 1) < 0.05, f"{bt:.3e} GeV^4")

print("\n5. Ableger und Verkürzung")
check("64 pi^4-Form: 1,04e-5 = xi_EFT/(4 pi)", abs(lam**2 * v**2 / (64 * pi**4 * mh**2) - x / (4 * pi)) < 1e-18 and abs(x / (4*pi) - 1.037e-5) < 0.002e-5)
short = 1 / (16 * pi**3)
check("Verkürzung lambda_h = m_h/v: 1/(16 pi^3) = 2,016e-3 = 15,1 xi", abs(short - 2.016e-3) < 0.001e-3 and abs(short / xi - 15.12) < 0.01)
xs = short
for _ in range(2000): xs *= (1 - 100 * xs)
check("Iteration x -> x(1-100x) ab 1/(16 pi^3) läuft gegen 0, nicht 4/30000", xs < 1e-5, f"nach 2000 Schritten {xs:.2e}")

print(f"\nErgebnis: {ok}/{n} OK")
raise SystemExit(0 if ok == n else 1)
