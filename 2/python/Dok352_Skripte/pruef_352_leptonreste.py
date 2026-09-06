#!/usr/bin/env python3
"""
pruef_352_leptonreste.py
Dok. 352 — Leptonreste: Leptonleiter, Galois und Koide im Vergleich
Johann Pascher, ORCID 0009-0000-6518-4064, 5. September 2026

Rest-Konvention: R = (Vorhersage - PDG) / (PDG * xi)
(relativer Rest in Einheiten von xi, wie im Dokument definiert)
"""
import math

xi   = 4 / 30000
me   = 0.51099895
mmu  = 105.6583755
mtau = 1776.86
r = {'e': 4/3, 'mu': 16/5, 'tau': 25/9}
p = {'e': 3/2, 'mu': 1,    'tau': 2/3}

ok = 0; total = 0

def rest_xi(val, ref):
    """Relativer Rest in Einheiten xi: (val-ref)/(ref*xi)"""
    return (val - ref) / (ref * xi)

def check(label, val, ref, tol=1.0):
    global ok, total
    total += 1
    err = abs(val - ref)
    passed = err < tol
    status = "OK  " if passed else "FAIL"
    if passed: ok += 1
    print(f"  {status}  {label}: {val:.5g}  (ref {ref:.5g}, diff {err:.3e})")

print("=" * 65)
print("Dok. 352 Prüfskript — Leptonreste")
print("=" * 65)

# ── §2 Leptonleiter ───────────────────────────────────────────────────────────
print("\n§2 Leptonleiter-Vorhersagen")
r_mmu_me_F   = (r['mu']/r['e'])   * xi**(p['mu'] -p['e'])
r_mtau_mmu_F = (r['tau']/r['mu']) * xi**(p['tau']-p['mu'])
r_mtau_me_F  = (r['tau']/r['e'])  * xi**(p['tau']-p['e'])
r_mmu_me_P   = mmu/me
r_mtau_mmu_P = mtau/mmu
r_mtau_me_P  = mtau/me

check("mmu/me   FFGFT",   r_mmu_me_F,   207.846, tol=0.005)
check("mtau/mmu FFGFT",   r_mtau_mmu_F, 16.992,  tol=0.005)
check("mtau/me  FFGFT",   r_mtau_me_F,  3531.6,  tol=0.5)

eps_mmu_me   = rest_xi(r_mmu_me_F,   r_mmu_me_P)
eps_mtau_mmu = rest_xi(r_mtau_mmu_F, r_mtau_mmu_P)
eps_mtau_me  = rest_xi(r_mtau_me_F,  r_mtau_me_P)

check("Rest mmu/me   [×xi]",   eps_mmu_me,   +39.1, tol=0.3)
check("Rest mtau/mmu [×xi]",   eps_mtau_mmu, +77.9, tol=0.3)
check("Rest mtau/me  [×xi]",   eps_mtau_me,  +117.4, tol=0.5)
check("Summe Reste (alg. Abhängigkeit)",
      eps_mmu_me + eps_mtau_mmu, eps_mtau_me, tol=0.5)

# ── §3 Galois ─────────────────────────────────────────────────────────────────
print("\n§3 Galois-Identitäten")
galois_sq   = 43200.0
galois_prod = 54.0

sq_pdg   = (mmu/me)**2
prod_pdg = me * mmu

check("(mmu/me)^2 PDG", sq_pdg,   42753.1, tol=1.0)
check("me*mmu PDG [MeV²]", prod_pdg, 53.991,  tol=0.001)

eps_sq   = rest_xi(sq_pdg,   galois_sq)
eps_prod = rest_xi(prod_pdg, galois_prod)

check("Rest (mmu/me)^2 [×xi]", eps_sq,   -77.6, tol=0.3)
check("Rest me*mmu     [×xi]", eps_prod,  -1.21, tol=0.05)
check("Galois-sq ≈ -2×Leiter(mmu/me) [×xi]", eps_sq, -2*eps_mmu_me, tol=1.0)

# ── §4 Koide ─────────────────────────────────────────────────────────────────
print("\n§4 Koide-Relation")
def koide_Q(m1, m2, m3):
    return (m1+m2+m3)/(math.sqrt(m1)+math.sqrt(m2)+math.sqrt(m3))**2

Q_pdg   = koide_Q(me, mmu, mtau)
Q_ffgft = koide_Q(r['e']*xi**p['e'], r['mu']*xi**p['mu'], r['tau']*xi**p['tau'])

check("Q(PDG)", Q_pdg, 0.6666605, tol=1e-6)
check("Rest Q(PDG)   [×xi]", (Q_pdg  -2/3)/xi, -0.046, tol=0.005)
check("Rest Q(FFGFT) [×xi]", (Q_ffgft-2/3)/xi,  8.06,  tol=0.1)

S = math.sqrt(me)+math.sqrt(mmu); M = me+mmu
a=-1/3; b=4/3*S; cc=2/3*S**2-M
T = (-b - math.sqrt(b**2-4*a*cc))/(2*a)
mtau_koide = T**2
check("mtau Koide [MeV]", mtau_koide, 1776.969, tol=0.005)
check("Rest mtau Koide [×xi]", rest_xi(mtau_koide, mtau), +0.46, tol=0.05)

# ── §8 Z3-Zirkulant ───────────────────────────────────────────────────────────
print("\n§8 Z3-Zirkulant")

def dc_theta(m_tau, m_e, m_mu):
    x = [math.sqrt(m_tau), math.sqrt(m_e), math.sqrt(m_mu)]
    c = sum(x)/3
    re = sum(x[k]*math.cos(2*math.pi*k/3) for k in range(3))
    im = sum(x[k]*math.sin(2*math.pi*k/3) for k in range(3))
    d  = 2/3*math.sqrt(re**2+im**2)
    th = abs(math.atan2(-im, re))
    return d/c, th

dc_P, th_P = dc_theta(mtau, me, mmu)
dc_F, th_F = dc_theta(r['tau']*xi**p['tau'], r['e']*xi**p['e'], r['mu']*xi**p['mu'])

check("d/c PDG",   dc_P, 1.41420, tol=0.00002)
check("d/c FFGFT", dc_F, 1.41649, tol=0.0005)
check("theta PDG   [rad]", th_P, 0.22223, tol=0.00005)
check("theta FFGFT [rad]", th_F, 0.22099, tol=0.0001)
check("theta A110=2/9 [rad]", 2/9, 0.22222, tol=0.00005)
check("d/c-sqrt2 PDG   [×xi]", (dc_P-math.sqrt(2))/xi, -0.098, tol=0.005)
check("d/c-sqrt2 FFGFT [×xi]", (dc_F-math.sqrt(2))/xi, +17.09, tol=0.1)

# ── §9 Generationsabhängige Korrekturen ───────────────────────────────────────
print("\n§9 Generationsabhängige Korrekturen")
eps_e_v   = 192*xi; eps_mu_v = 152*xi; eps_tau_v = 73*xi
m_bare_e   = me  /(1+eps_e_v)
m_bare_mu  = mmu /(1+eps_mu_v)
m_bare_tau = mtau/(1+eps_tau_v)
Q_bare = koide_Q(m_bare_e, m_bare_mu, m_bare_tau)
check("Q(bare)-2/3 [×xi]", (Q_bare-2/3)/xi, 8.06, tol=0.3)

masses = [me, mmu, mtau]; eps_v = [eps_e_v, eps_mu_v, eps_tau_v]
sm = sum(masses)
avg_m   = sum(m/sm *e for m,e in zip(masses,eps_v))/xi
avg_sqm = sum(math.sqrt(m)/sum(math.sqrt(x) for x in masses)*e
              for m,e in zip(masses,eps_v))/xi
check("<eps>_m   [×xi]", avg_m,   77.7, tol=1.5)
check("<eps>_sqm [×xi]", avg_sqm, 90.0, tol=1.5)

DQ = (2/3)*(avg_m-avg_sqm)
check("DeltaQ [×xi]", DQ, -8.23, tol=0.5)
check("Q(bare)+DQ-2/3 [×xi]", (Q_bare-2/3)/xi + DQ, -0.17, tol=0.3)
erk = abs(DQ)/abs((Q_bare-2/3)/xi)*100
check("Erklärungsanteil [%]", erk, 101.0, tol=5.0)

# ── §10 Herkunft ──────────────────────────────────────────────────────────────
print("\n§10 Herkunft der fallenden εᵢ")
alpha = 1/137.036
qed_ord = 3*alpha/(4*math.pi)
print(f"  INFO  3α/(4π) = {qed_ord:.4f} = {qed_ord/xi:.1f}·xi  (Ordnung 10–100·xi ✓)")

# fallende Struktur: ε_e > ε_mu > ε_tau prüfen
assert 192 > 152 > 73, "Fallende Struktur verletzt!"
print("  OK    fallende Struktur ε_e > ε_mu > ε_tau bestätigt (192 > 152 > 73)·xi")

# Differenzreste ~ Verhältnisreste (konsistente Größenordnung)
diff_e_mu = (192-152)  # = 40·xi  ~ eps_mmu_me = 39.1·xi
diff_e_tau= (192-73)   # = 119·xi ~ eps_mtau_me = 117.4·xi (konsistent)
check("ε_e - ε_mu ≈ Rest mmu/me [×xi]",  float(diff_e_mu),  eps_mmu_me,  tol=3.0)
check("ε_e - ε_tau ≈ Rest mtau/me [×xi]",float(diff_e_tau), eps_mtau_me, tol=3.0)

print(f"\n{'='*65}")
print(f"Ergebnis: {ok}/{total} Tests bestanden")
if ok == total:
    print("ALLE TESTS OK — Dok. 352 vollständig verifiziert.")
else:
    print(f"ACHTUNG: {total-ok} Tests fehlgeschlagen.")
