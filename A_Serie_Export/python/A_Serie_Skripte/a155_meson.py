"""A155: Additiver Meson-Ansatz — Geltungsbereich, Pion-Anker, GMOR."""
import math

xi = 4/30000
K_frak = 1 - 100*xi
K_frak_inv = 75/74
D_f = 3 - xi
Lambda_QCD = 0.217  # GeV
N_c, alpha_s = 3, 0.118

# PDG-Massen (GeV; Quarks MS-bar 2 GeV)
m_u, m_d, m_s = 2.16e-3, 4.67e-3, 93.4e-3
m_pi0, m_piC = 0.134977, 0.139570
m_K, m_eta = 0.493677, 0.547862
m_rho, m_omega = 0.77526, 0.78266
m_p_exp = 0.938272

print("=== A155: Meson- und Baryon-Formeln ===")

# 1. Geltungsbereich der additiven Formel: Bindung < Lambda_QCD
print("\n1. Geltungsbereich (Bindung = m_M - Sum m_q, additiv nur < Lambda):")
mesons = [("pi0", m_pi0, 2*m_u), ("pi+-", m_piC, m_u+m_d),
          ("K+-", m_K, m_u+m_s), ("eta", m_eta, 2*m_s),
          ("rho", m_rho, 2*m_u), ("omega", m_omega, 2*m_u)]
for name, mM, mq in mesons:
    bind = mM - mq
    ok = bind < Lambda_QCD
    n = math.log(bind/Lambda_QCD)/math.log(K_frak) if ok else float('nan')
    tag = f"n_eff={n:6.2f}" if ok else "Bindung > Lambda"
    print(f"  {name:6s} Bindung={bind:.4f}  {tag}")

# 2. Pion-Anker: n_eff(pi0) = 37.79, im Fenster 36+1=37
n_pi0 = math.log((m_pi0-2*m_u)/Lambda_QCD)/math.log(K_frak)
n_piC = math.log((m_piC-m_u-m_d)/Lambda_QCD)/math.log(K_frak)
print(f"\n2. Pion-Anker: n_eff(pi0)={n_pi0:.3f} (soll 37.79), n_eff(pi+-)={n_piC:.3f}")
assert abs(n_pi0 - 37.79) < 0.01
assert abs(n_piC - 36.62) < 0.01
# Sektor-Vorhersage-Fenster (A270): 36+1
assert 36 < n_pi0 < 39 and 36 < n_piC < 39

# 3. GMOR: B_pi ~ B_K (chirale Konsistenz)
B_pi = m_piC**2 / (m_u + m_d)
B_K  = m_K**2  / (m_u + m_s)
print(f"\n3. GMOR: B_pi={B_pi:.4f} GeV, B_K={B_K:.4f} GeV, B_pi/B_K={B_pi/B_K:.4f}")
assert abs(B_pi/B_K - 1) < 0.15  # SU(3)-Brechung ~12%

# 4. [S]-Kandidat: B = 8*Lambda*K_frak^-37 (zentral 0.02%, P35: Schema-Unsicherheit ~2%)
B_cand = 8 * Lambda_QCD * K_frak_inv**37
print(f"\n4. [S]-Kandidat: 8*Lambda*K_inv^37 = {B_cand:.4f} GeV vs B_pi = {B_pi:.4f}")
print(f"   zentral Delta = {(B_cand-B_pi)/B_pi*100:+.3f}% (P35: nicht belastbar, Quarkmassen ~2%)")
assert abs(B_cand - B_pi)/B_pi < 0.02

# Historische Altkorpus-Korrektur: python/Dok190_Skripte/r61_baryon_anker.py

# Baryon-Kandidat: vollstaendig geometrische Proton-Formel [S]
anchor = math.pi**2/2          # Vol(B4)
eta_sc = math.pi/6             # sc-Packungsdichte = Vol(B3)/8
m_p_cand = anchor*eta_sc*N_c*(1+alpha_s)*math.exp(-(xi/4)*N_c)*Lambda_QCD/2
print(f"\nBaryon-Kandidat: m_p = (pi^3/12)*N_c(1+alpha_s)e^(-3xi/4)*Lambda/2 = {m_p_cand:.5f} GeV")
print(f"  Delta zu PDG {m_p_exp}: {(m_p_cand-m_p_exp)/m_p_exp*100:+.3f}% (absorbierbar in alpha_s/Lambda)")
assert abs(m_p_cand-m_p_exp)/m_p_exp < 0.005
# Higgs-Verbindung: 16pi^3/(pi^3/12) = 192 (D4-Weyl)
weyl = 16*math.pi**3/(math.pi**3/12)
print(f"16pi^3/(pi^3/12) = {weyl:.10f} (D4-Weyl-Ordnung 192)")
assert abs(weyl-192) < 1e-9
# Produkt-Fixierung: X = 0.52248, pi/6 trifft +0.21%
D_bar = N_c*(1+alpha_s)*math.exp(-(xi/4)*N_c)*0.5*Lambda_QCD
X = m_p_exp/(anchor*1.00007*D_bar*1.00002)
print(f"Fixiertes Produkt X = {X:.5f}; pi/6 = {eta_sc:.5f} (Delta {(eta_sc-X)/X*100:+.3f}%)")
assert abs(eta_sc-X)/X < 0.003

print("\nAlle Checks bestanden.")
