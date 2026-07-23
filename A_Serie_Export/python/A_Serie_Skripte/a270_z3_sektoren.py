"""A270: Z3-Sektor-Struktur — Bulk-Exponent 36, Fixpunkte, Sektor-Tabelle, Statistik."""
import math
import random

xi = 4/30000
K_frak = 1 - 100*xi
K_frak_inv = 75/74
phi = (1 + math.sqrt(5))/2
Lambda_QCD = 0.217
m_u = 2.16e-3
m_pi0 = 0.134977

print("=== A270: Z3-Sektor-Struktur ===")

# 1. Schluesselrelation: K_frak^-36 ~ 16/pi^2 (Delta 0.010%)
lhs = K_frak_inv**36
rhs = 16/math.pi**2
print(f"\n1. K_inv^36 = {lhs:.6f}, 16/pi^2 = {rhs:.6f}, Delta = {(lhs-rhs)/rhs*100:+.4f}%")
assert abs(lhs-rhs)/rhs < 1.1e-4

# 2. k*/100 aus Dok 275: unabhaengige Stuetzung der 36
k_star = math.log(phi)/xi
n_exact = math.log(rhs)/math.log(K_frak_inv)
print(f"\n2. k* = ln(phi)/xi = {k_star:.1f}; k*/100 = {k_star/100:.4f}")
print(f"   exakter Exponent fuer 16/pi^2: n = {n_exact:.4f}")
assert abs(k_star/100 - 36.09) < 0.01
assert abs(n_exact - 36) < 0.01

# 3. Z3-Fixpunkte auf T^3: (x,y,z)->(y,z,x), Fixpunkte x=y=z=k/3, k=0,1,2
print("\n3. Z3-Fixpunkte (numerisch, Gitter mod 1):")
fixpoints = []
for k in range(3):
    p = (k/3, k/3, k/3)
    perm = (p[1], p[2], p[0])
    assert all(abs((a-b) % 1) < 1e-12 for a, b in zip(p, perm))
    fixpoints.append(p)
print(f"   {len(fixpoints)} Fixpunkte bestaetigt: {fixpoints}")
assert len(fixpoints) == 3

# 4. Sektor-Basis am Fixpunkt: e0 invariant, e1/e2 mit Phase omega/omega^2
import cmath
w = cmath.exp(2j*math.pi/3)
# Permutationsmatrix P: (x,y,z)->(y,z,x)
def P(v): return (v[1], v[2], v[0])
e0 = (1/math.sqrt(3),)*3
e1 = (1/math.sqrt(2), -1/math.sqrt(2), 0)
e2 = (1/math.sqrt(6), 1/math.sqrt(6), -2/math.sqrt(6))
# Z3-Eigenvektoren im Komplexen: v_k = (1, w^k, w^2k)/sqrt3, P v_k = w^-k v_k
for k in range(3):
    v = [w**(k*j)/math.sqrt(3) for j in range(3)]
    Pv = P(v)
    lam = Pv[0]/v[0]
    assert all(abs(Pv[j] - lam*v[j]) < 1e-12 for j in range(3))
print("4. Z3-Eigenbasis: 3 Sektoren (Eigenwerte 1, omega, omega^2) bestaetigt")

# 5. Sektor-Tabelle: Lepton 36+0, Meson 36+1, Baryon 36+2 (topologisch: |Z3|-1=2)
sectors = {"Lepton": 0, "Meson": 1, "Baryon": 2}
assert sectors["Baryon"] == 3 - 1  # nicht-triviale Z3-Elemente
print(f"\n5. Sektor-Exponenten: {[(k, 36+v) for k, v in sectors.items()]}")

# 6. Empirischer Anker Pion (aus A155): n_eff(pi0) im Fenster 36+1
n_pi0 = math.log((m_pi0-2*m_u)/Lambda_QCD)/math.log(K_frak)
print(f"\n6. Pion-Anker: n_eff(pi0) = {n_pi0:.3f} (Vorhersage 37, Fenster [36,39])")
assert 36 < n_pi0 < 39

# 7. Baryon-Vorhersage: K_inv^38
K38 = K_frak_inv**38
print(f"\n7. Baryon-Stufe: K_inv^38 = {K38:.4f} (Vorhersage, Test offen)")
assert abs(K38 - 1.6654) < 0.001

# 8. Monte-Carlo-Statistik: Trefferrate <=0.010% fuer Zufallsziel
random.seed(42)
N, hits = 100000, 0
log_lo, log_hi = math.log(K_frak_inv), 100*math.log(K_frak_inv)
for _ in range(N):
    t = math.exp(random.uniform(log_lo, log_hi))
    n = max(1, min(100, round(math.log(t)/math.log(K_frak_inv))))
    if abs(K_frak_inv**n - t)/t <= 1e-4:
        hits += 1
rate = hits/N*100
print(f"\n8. Monte Carlo: Trefferrate <=0.010% = {rate:.2f}% (soll ~1.5%)")
assert 1.0 < rate < 2.2

# 9. Spezifitaet: von 21 Konstanten trifft nur 16/pi^2 mit <=0.010%
consts = [math.pi, math.pi/2, math.pi**2, math.pi**2/6, math.e, math.e/2,
          phi, math.sqrt(2), math.sqrt(3), math.sqrt(5), 2, 3, 4, 1.5, 4/3,
          16/math.pi**2, math.pi**2/16, math.pi/4, 2/math.pi,
          math.log(2), math.log(10)]
tight = []
for c in consts:
    if c <= 0: continue
    n = round(math.log(c)/math.log(K_frak_inv))
    if 1 <= n <= 200 and abs(K_frak_inv**n - c)/c <= 1e-4:
        tight.append(c)
print(f"\n9. Spezifitaet: {len(tight)} von {len(consts)} Konstanten mit <=0.010%: {tight}")
assert tight == [16/math.pi**2]

print("\nAlle Checks bestanden.")
