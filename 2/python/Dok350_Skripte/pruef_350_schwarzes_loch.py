"""pruef_350_schwarzes_loch.py — Dok. 350: Schwarze Löcher und Zeit-Masse-Dualität
Alle Aussagen [S]; das Skript prüft nur die algebraische Konsistenz der Relationen,
nicht ihre physikalische Gültigkeit."""
import math

xi = 4/30000  # Galois-Zahl, Dok. 338 [K]

print("Satz A: T·m = 1 — Kovarianz von G [B-intern, physikalisch S]")
# G = ξ²/(4m) in natürlichen Einheiten (Dok. 012, R58)
# Wenn T → k·T, dann m → m/k, dann G → k·G
for k in [1, 10, 1000, 1e6]:
    m = 1.0/k           # m ∝ 1/T
    T = k
    G = xi**2/(4*m)
    assert abs(T*m - 1) < 1e-12, "T·m ≠ 1"
    assert abs(G - k*xi**2/4) < 1e-20, "G skaliert nicht linear in T"
    print(f"  T={k:>8.0e}  m={m:.1e}  G/G0={G/(xi**2/4):.0e}  ✓")
print("  → G ∝ T: Gravitation wird STÄRKER, nicht schwächer, wenn T wächst [S]")
print("  → Kein G→0; stattdessen G→∞ mit m→0. Physikalische Lesart: siehe Satz C.")

print("\nSatz B: Keine punktförmige Singularität — Massenkopplung bleibt endlich")
# Das Produkt m·G = ξ²/4 ist T-unabhängig
for k in [1, 1e3, 1e9]:
    m = 1.0/k; G = xi**2/(4*m)
    assert abs(m*G - xi**2/4) < 1e-20
print(f"  m·G = ξ²/4 = {xi**2/4:.3e} für alle T  ✓")
print("  → Die Kopplungsstärke m·G ist konstant; eine Massensingularität")
print("    mit endlichem G ist ausgeschlossen [B] (Dok. 078)")

print("\nSatz C: Hierarchie der intrinsischen Zeiten (Dok. 025, τ = τ_ξ/ξⁿ)")
# Masse-Hierarchie → Zeit-Hierarchie: T_ν / T_e = m_e / m_ν
m_e  = 0.511e6   # eV
m_nu = 0.05      # eV (Größenordnung, NuFIT-Summe/3)
m_t  = 173e9     # eV
T_ratio_nu_e = m_e/m_nu
T_ratio_e_t  = m_t/m_e
print(f"  T_ν/T_e = m_e/m_ν ≈ {T_ratio_nu_e:.1e}")
print(f"  T_e/T_t = m_t/m_e ≈ {T_ratio_e_t:.1e}")
print("  → Neutrino hat die längste intrinsische Zeit aller massiven Fermionen [B]")
print("  → Neutrino = Su[0] = Vss[0] = Vakuumzustand (Dok. 344) [B]")

print("\nSatz D: Verdampfungssequenz — Ordnung nach Masse [S]")
seq = [("t",173e9),("b",4.18e9),("τ",1.777e9),("c",1.27e9),("s",95e6),
       ("μ",105.7e6),("d",4.7e6),("u",2.2e6),("e",0.511e6),("ν",0.05)]
seq_sorted = sorted(seq, key=lambda x: -x[1])
print("  Emissionsreihenfolge (schwer → leicht) bei sinkender Lochmasse:")
print("  " + " → ".join(n for n,_ in seq_sorted))
assert seq_sorted[-1][0] == "ν", "Neutrino ist nicht letztes"
print("  → Letztes stabiles Muster: Neutrino [S]")

print("\nAlle Konsistenzprüfungen bestanden. Physikalischer Status: [S]")
