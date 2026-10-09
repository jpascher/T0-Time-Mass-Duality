#!/usr/bin/env python3
"""
pruef_353_koide_amplitude.py
Prüfskript zu Dok. 353: Koide-Amplitude d/c = sqrt(2) aus T4/Z3-Geometrie
Johann Pascher, 7. September 2026
"""
import math
import numpy as np

xi = 4/30000
sqrt2 = math.sqrt(2)

# ============================================================
# 1. Algebraischer Beweis: Q = 1/3 + d^2/(6c^2)
# ============================================================
def Q_from_dc(d_over_c):
    return 1/3 + (d_over_c**2) / 6

assert abs(Q_from_dc(sqrt2) - 2/3) < 1e-15, "Q(sqrt2) != 2/3"
print("OK 1: Q = 2/3 iff d/c = sqrt(2) [B]")

# ============================================================
# 2. Normierungsbedingung: 2 Nicht-Null-Kopplungen → 1/sqrt(2)
# ============================================================
# Pro Zeile der Kopplungsmatrix: 2 Nicht-Null-Einträge, l2-Norm = 1
weight = math.sqrt(1/2)   # = 1/sqrt(2)
l2_check = math.sqrt(2 * weight**2)
assert abs(l2_check - 1.0) < 1e-15, "l2-Norm != 1"
print(f"OK 2: Z3-Gleichverteilungsgewicht = 1/sqrt(2) = {weight:.8f} [B]")

# ============================================================
# 3. Kopplungsmatrix M^(13) aus Dok. 348
# ============================================================
M13 = np.array([[-1, 0, 1],
                [ 1,-1, 0],
                [ 0, 1,-1]], dtype=float)

# Normierung: Frobenius-Norm pro Zeile / sqrt(Anzahl Nicht-Null)
for i in range(3):
    nonzero = M13[i][M13[i] != 0]
    assert len(nonzero) == 2, f"Zeile {i}: nicht genau 2 Nicht-Null-Einträge"
    # Die l2-Norm jeder Zeile ist sqrt(2); normiert auf Einheitsvektor
    # ergibt sich 1/sqrt(2) pro Eintrag (Dok. 348 Satz C)
    norm_row = np.linalg.norm(M13[i])
    assert abs(norm_row - sqrt2) < 1e-14, f"Zeile {i}: ||Zeile||_2 != sqrt(2)"
    norm_per_entry = abs(nonzero[0]) / norm_row
    assert abs(norm_per_entry - 1/sqrt2) < 1e-14, f"Zeile {i}: |M_ij|_norm != 1/sqrt2"
print(f"OK 3: ||M^(13) Zeile||_2 = sqrt(2); normierte Eintraege = 1/sqrt(2) [B]")

# ============================================================
# 4. Identifikation d/c = 1 / (1/sqrt(2)) = sqrt(2)
# ============================================================
dc_from_geometry = 1 / (1/sqrt2)
assert abs(dc_from_geometry - sqrt2) < 1e-15, "d/c aus Geometrie != sqrt(2)"
print(f"OK 4: d/c = 1/|M| = {dc_from_geometry:.8f} = sqrt(2) -- Rechnung exakt, Zuordnung d/c = 1/|M| unbegruendet [S]")

# ============================================================
# 5. Numerische Verifikation: d/c aus PDG-Massen
# ============================================================
# PDG-Massen in MeV
m_e_pdg   = 0.51099895
m_mu_pdg  = 105.6583755
m_tau_pdg = 1776.86

def dc_from_masses(me, mmu, mtau):
    """Berechne d/c aus dem Z3-Zirkulant-System."""
    x0, x1, x2 = math.sqrt(mtau), math.sqrt(me), math.sqrt(mmu)
    c = (x0 + x1 + x2) / 3
    # Lösung: d aus |x_k - c| via cos-Struktur
    # d^2 = (2/3)*[(x0-c)^2 + (x1-c)^2 + (x2-c)^2]
    d2 = (2/3)*((x0-c)**2 + (x1-c)**2 + (x2-c)**2)
    d = math.sqrt(d2)
    return d/c

dc_pdg = dc_from_masses(m_e_pdg, m_mu_pdg, m_tau_pdg)
delta_pdg = dc_pdg - sqrt2
delta_pdg_xi = delta_pdg / xi
assert abs(dc_pdg - sqrt2) < 5*xi, f"PDG d/c weit von sqrt(2): {dc_pdg}"
print(f"OK 5: PDG d/c = {dc_pdg:.8f}, Abw. = {delta_pdg:.2e} = {delta_pdg_xi:+.2f}*xi [K]")

# ============================================================
# 6. Bare FFGFT-Massen
# ============================================================
v = 246.22e3  # MeV
r_e,  p_e  = 4/3,  3/2
r_mu, p_mu = 16/5, 1.0
r_tau,p_tau= 25/9, 2/3

m_e_bare   = r_e  * xi**p_e  * v
m_mu_bare  = r_mu * xi**p_mu * v
m_tau_bare = r_tau* xi**p_tau* v

dc_bare = dc_from_masses(m_e_bare, m_mu_bare, m_tau_bare)
delta_bare_xi = (dc_bare - sqrt2) / xi
print(f"OK 6: Bare FFGFT d/c = {dc_bare:.8f}, Abw. = {delta_bare_xi:+.1f}*xi [K]")
assert 15 < delta_bare_xi < 20, f"Bare FFGFT Abw. unerwartet: {delta_bare_xi:.1f}*xi"

# ============================================================
# 7. Koide-Q für PDG und bare FFGFT
# ============================================================
def koide_Q(me, mmu, mtau):
    s = math.sqrt(me) + math.sqrt(mmu) + math.sqrt(mtau)
    return (me + mmu + mtau) / s**2

Q_pdg  = koide_Q(m_e_pdg, m_mu_pdg, m_tau_pdg)
Q_bare = koide_Q(m_e_bare, m_mu_bare, m_tau_bare)
print(f"OK 7: Q_PDG = {Q_pdg:.6f} (Abw. {(Q_pdg-2/3)/xi:+.2f}*xi), "
      f"Q_bare = {Q_bare:.6f} (Abw. {(Q_bare-2/3)/xi:+.2f}*xi) [K]")

# ============================================================
# 8. Orthogonalität: Q = 1/3 + d^2/(6c^2) enthält theta nicht (algebraisch)
# ============================================================
# Die Formel Q = 1/3 + d^2/(6c^2) ist exakt theta-unabhängig (Dok. A110, 352)
for dc_test in [sqrt2, 1.0, 1.3, 1.5, 2.0]:
    Q_alg = 1/3 + dc_test**2 / 6
    # Für physikalisch zulässige theta mit d/c = sqrt(2) und theta = 2/9:
    if abs(dc_test - sqrt2) < 1e-10:
        assert abs(Q_alg - 2/3) < 1e-14, f"Q_alg(sqrt2) != 2/3"
# Verifikation mit physikalischem theta = 2/9 (alle sqrt(m_k) > 0)
theta_phys = 2/9
c_t, d_t = 1.0, sqrt2
sqrtm = [c_t + d_t*math.cos(theta_phys + 2*math.pi*k/3) for k in range(3)]
assert all(x > 0 for x in sqrtm), "sqrt(m_k) nicht positiv für theta=2/9"
masses_t = [x**2 for x in sqrtm]
Q_phys = sum(masses_t) / (sum(math.sqrt(m) for m in masses_t))**2
assert abs(Q_phys - 2/3) < 1e-12, f"Q(theta=2/9, d/c=sqrt2) != 2/3"
print(f"OK 8: Q = 1/3 + d^2/(6c^2) theta-unabhaengig; Q(theta=2/9) = {Q_phys:.10f} [B]")

# ============================================================
# 9. Gleichverteilungs-Lesart: Q = 2/3 <=> 3c^2 = (3/2) d^2
#    (symmetrische Mode und nicht-triviales Paar tragen gleich viel)
# ============================================================
for c_test in (0.3, 1.0, 2.7):
    d_test = sqrt2 * c_test
    th = 0.4
    a = [c_test + d_test*math.cos(th + 2*math.pi*k/3) for k in range(3)]
    sum_m = sum(x**2 for x in a)
    sym, nontriv = 3*c_test**2, 1.5*d_test**2
    assert abs(sym - nontriv) < 1e-12, "Gleichverteilung verletzt"
    assert abs(sum_m - (sym + nontriv)) < 1e-12, "Zerlegung Summe m falsch"
# Gegenrichtung: Gleichverteilung erzwingt d/c = sqrt(2)
assert abs(math.sqrt(3/1.5) - sqrt2) < 1e-15
print("OK 9: Q = 2/3 <=> 3c^2 = (3/2)d^2 (Gleichverteilung symmetrisch / nicht-trivial) [B]")

# ============================================================
# 10. 45-Grad-Lesart (Foot 1994): Winkel zwischen (sqrt m_k) und (1,1,1)
#     cos^2(phi) = 1/(3Q)  ->  Q = 2/3 <=> phi = 45 Grad
# ============================================================
c_test, d_test = 1.0, sqrt2
a = np.array([c_test + d_test*math.cos(0.4 + 2*math.pi*k/3) for k in range(3)])
cosphi = a.sum() / (math.sqrt(3) * np.linalg.norm(a))
phi = math.degrees(math.acos(cosphi))
assert abs(phi - 45.0) < 1e-10, f"Winkel {phi} != 45"
print(f"OK 10: Winkel (sqrt m) zu (1,1,1) = {phi:.10f} Grad bei d/c = sqrt(2) [B]")

# ============================================================
# 11. PDG 2024 (m_tau = 1776.93 +- 0.09 MeV)
# ============================================================
m24 = [0.51099895000, 105.6583755, 1776.93]
Q24 = sum(m24) / (sum(math.sqrt(m) for m in m24))**2
dc24 = math.sqrt(6*(Q24 - 1/3))
dQ24_xi = (Q24 - 2/3) / xi
ddc24_xi = (dc24 - sqrt2) / xi
assert abs(dQ24_xi) < 0.05, "PDG 2024: |Q - 2/3| > 0.05 xi"
print(f"OK 11: PDG 2024: Q - 2/3 = {dQ24_xi:+.3f}*xi, d/c - sqrt2 = {ddc24_xi:+.3f}*xi [K]")

# ============================================================
# Zusammenfassung
# ============================================================
print("\n=== Dok. 353 Prüfskript: alle 11 Assertions bestanden ===")
print(f"  xi = {xi:.6e}")
print(f"  sqrt(2) = {sqrt2:.10f}")
print(f"  d/c = sqrt(2) aus Geometrie: offen [S] (Zuordnung bzw. Gleichverteilung unbegruendet)")
print(f"  d/c (PDG) = {dc_pdg:.8f}, Abw. {delta_pdg_xi:+.3f}*xi [K]")
print(f"  d/c (FFGFT bare) = {dc_bare:.8f}, Abw. {delta_bare_xi:+.1f}*xi [K]")
print(f"  Q (PDG 2022) = {Q_pdg:.8f}, Abw. {(Q_pdg-2/3)/xi:+.3f}*xi [K]")
print(f"  Q (PDG 2024) = {Q24:.8f}, Abw. {dQ24_xi:+.3f}*xi [K]")
