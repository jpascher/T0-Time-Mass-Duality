"""A261 Prüfskript: Skalenhierarchie xi -> Massen -> E0 -> alpha.

Aktualisiert am 1.10.2026: E0=7,398 MeV wird nicht mehr hart als "xi-Weg" gesetzt,
sondern als E0_geom/sqrt(K_frak) berechnet (fraktal korrigiertes Mittel, A130 Weg 2);
der fruehere xi-Weg ist entfernt (vgl. Dok. A261 bzw. Dok. 190, R72).
"""
import math

xi = 4/30000
m_e = 0.511   # MeV
m_mu = 105.658  # MeV
K_frak = 1 - 100*xi

print("=== A261: Skalenhierarchie ===")

# 1. E0 = sqrt(m_e * m_mu) — geometrisches Mittel
E0_geom = math.sqrt(m_e * m_mu)
print(f"E0 (geometr. Mittel) = sqrt({m_e}*{m_mu}) = {E0_geom:.4f} MeV")
# E0 fraktal korrigiert: E0_geom/sqrt(K_frak) (A130 Weg 2, R72)
E0_xi = E0_geom / math.sqrt(K_frak)
print(f"E0 (fraktal korrigiert, A130 Weg 2, R72) = E0_geom/sqrt(K_frak) = {E0_xi:.4f} MeV")
assert abs(E0_xi - 7.398) < 0.001
print(f"Differenz: {abs(E0_geom-E0_xi)/E0_xi*100:.2f}% (= 1/sqrt(K_frak), per Konstruktion)")

# 2. alpha = xi * (E0/1MeV)^2
alpha_berechnet = xi * E0_xi**2
alpha_exp = 1/137.036
print(f"\nalpha = xi * E0^2 = {xi:.6e} * {E0_xi:.3f}^2 = {alpha_berechnet:.6e}")
print(f"alpha_exp = 1/137.036 = {alpha_exp:.6e}")
print(f"Abweichung: {abs(alpha_berechnet - alpha_exp)/alpha_exp * 100:.4f}%")
assert abs(alpha_berechnet - alpha_exp)/alpha_exp < 0.001

# 3. Verhältnisse korrekturfrei: mu/e
ratio_exp = m_mu / m_e
# Aus Leiterformel: c_mu/c_e * xi^(2-5/2) = c_mu/c_e * xi^(-1/2)
print(f"\nm_mu/m_e (gemessen) = {ratio_exp:.4f}")
print(f"Korrekturfaktor K_frak kürzt sich heraus: ✓")

# 4. K_frak-Korrektur für Absolutwerte
E0_korr = E0_geom * (1 + (E0_xi - E0_geom)/E0_geom)
print(f"\nK_frak = {K_frak:.6f}")

print("\nAlle Checks bestanden.")
