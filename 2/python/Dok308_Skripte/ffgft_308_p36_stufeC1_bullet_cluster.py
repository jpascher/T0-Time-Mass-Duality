#!/usr/bin/env python3
# ffgft_308_p36_stufeC1_bullet_cluster.py  —  Dok. 307, P36 Stufe C (1/2)
# P36_StufeC_BulletCluster.py
#
# Bullet-Cluster-Test: Zwei-Klumpen FE-Mesh mit T~*m=1 (K3).
# Fragestellung: Folgt der effektive Linsenpeak der
# kollisionsfreien Galaxienkomponente oder dem Baryon-Gas?
#
# Konfiguration (Clowe et al. 2006, ApJ 648 L109):
#   Subcluster (kollisionsfrei, Galaxien): M_gal = 2.3e14 Msun
#   Subcluster (Gas, gebremst):            M_gas = 0.23e14 Msun
#   raeumlicher Versatz Galaxie--Gas:      Delta = 250 kpc
#   Linsenbeobachtung: Peak bei Galaxienposition (nicht Gas)
#
# FFGFT-Mechanismus (K3, momentane Massenkopplung):
#   n(r) = 1 + GM_tot(r)/(r c^2)
#   M_tot = M_gal(r) + M_gas(r)  [BEIDE Komponenten, momentan]
#
# Praedizierter Ausgang (aus Dok.307 vorregistriert):
#   Da n der MOMENTANEN Dichte folgt und Gas ~85% der Baryonen
#   traegt, sollte der Linsenpeak nahe der Gasposition liegen
#   -> Scheitern am Bullet. Dieses Skript prueft das.
#
# Methode: 1D-Profil entlang der Kollisionsachse.
#   Effektive Linsenmasse ~ Integral_los n(r) dz (Projektionsnaeh.)
#   Peak des Integrals = Linsenpeak-Position.
# ============================================================
import numpy as np

G    = 6.67430e-11
c    = 2.99792458e8
kpc  = 3.08568e19
Msun = 1.98892e30

# --- Parameter (Clowe+2006) ---
M_gal  = 2.30e14 * Msun   # kollisionsfrei, Galaxien
M_gas  = 0.23e14 * Msun   # gebremst, Gas (ICM)
Delta  = 250.0   * kpc     # Versatz Galaxie--Gas auf Kollisionsachse x
r_gal  = 150.0   * kpc     # charakteristischer Radius Galaxienklumpen
r_gas  = 200.0   * kpc     # charakteristischer Radius Gasklumpen

# Positionen auf Kollisionsachse (Galaxie bei x=0, Gas bei x=Delta)
x_gal =   0.0
x_gas = Delta

def rho_klump(x, x0, M_tot, r_s):
    """NFW-aehnliches Profil: rho ~ 1/((r/r_s)(1+r/r_s)^2), normiert."""
    r  = abs(x - x0)
    rs = r_s
    if r < 1e-3 * kpc:
        r = 1e-3 * kpc
    # Vereinfacht: isothermes Profil rho ~ 1/(1+(r/rs)^2) fuer 1D-Test
    norm = M_tot / (np.pi * rs)   # Normierung 1D-Integral = M_tot
    return norm / (1.0 + (r / rs)**2)

def n_total(x, los_half=1000*kpc, Nlos=500):
    """
    Effektiver Brechungsindex integriert entlang Sichtlinie z
    (Projektionsnaeh. fuer schwaches Linsen).
    Gibt dimensionslosen Wert: Sigma_eff = integral n(r) dz / c^2
    """
    z_arr = np.linspace(-los_half, los_half, Nlos)
    dz    = 2 * los_half / Nlos
    sigma = 0.0
    for z in z_arr:
        r2      = (x - x_gal)**2 + z**2
        r2_gas  = (x - x_gas)**2  + z**2
        r_tot   = np.sqrt(r2)
        phi_gal = G * rho_klump(np.sqrt(r2),     x_gal, M_gal, r_gal) / c**2
        phi_gas = G * rho_klump(np.sqrt(r2_gas), x_gas, M_gas, r_gas) / c**2
        sigma  += (phi_gal + phi_gas) * dz
    return sigma

# --- 1D-Profil entlang Kollisionsachse ---
x_arr = np.linspace(-400, 600, 101) * kpc   # kpc, relativ zu Galaxienzentrum
sigma = np.array([n_total(x) for x in x_arr])

x_kpc   = x_arr / kpc
peak_idx = np.argmax(sigma)
x_peak   = x_kpc[peak_idx]

print("=" * 68)
print(" P36 Stufe C — Bullet Cluster: FE-Linsenpeak (K3, momentane Kopplung)")
print("=" * 68)
print(f"  Galaxienposition:  x =   0.0 kpc")
print(f"  Gasposition:       x = {Delta/kpc:.0f}.0 kpc")
print(f"  Linsenpeak (FFGFT): x = {x_peak:.1f} kpc")
print()

dist_to_gal = abs(x_peak - 0.0)
dist_to_gas = abs(x_peak - Delta/kpc)
print(f"  Abstand Peak -- Galaxie: {dist_to_gal:.1f} kpc")
print(f"  Abstand Peak -- Gas:     {dist_to_gas:.1f} kpc")
print()

if dist_to_gal < dist_to_gas:
    verdict = "Peak naehe Galaxie -> Bullet BESTANDEN (unerwartet)"
else:
    verdict = "Peak naehe Gas     -> Bullet GESCHEITERT (erwartet bei momentaner Kopplung)"
print(f"  URTEIL: {verdict}")

print()
print("Profil sigma_eff(x) [normiert]:")
sigma_n = sigma / sigma.max()
print(f"  {'x[kpc]':>8}  {'sigma_norm':>12}")
for i in range(0, len(x_arr), 10):
    marker = " <-- GAL" if abs(x_kpc[i]) < 25 else (
             " <-- GAS" if abs(x_kpc[i] - Delta/kpc) < 25 else (
             " <-- PEAK" if i == peak_idx else ""))
    print(f"  {x_kpc[i]:>8.0f}  {sigma_n[i]:>12.4f}{marker}")

print()
print("BEFUND:")
print(f"  Momentane T~*m=1-Kopplung (K3) platziert den Linsenpeak bei")
print(f"  x = {x_peak:.0f} kpc, d.h. {dist_to_gas:.0f} kpc vom Gas entfernt,")
print(f"  {dist_to_gal:.0f} kpc von den Galaxien entfernt.")
print()
if dist_to_gal < dist_to_gas:
    print("  Ueberraschendes Ergebnis: Peak folgt Galaxien.")
    print("  Ursache: M_gal >> M_gas (Faktor 10) dominiert das Potential")
    print("  trotz momentaner Kopplung. Der Massenfaktor 10 ueberwiegt")
    print("  die raeumliche Verschiebung von 250 kpc.")
    print()
    print("  ABER: Das ist Groessenordnung, kein Nachweis.")
    print("  Beobachtung verlangt Peak-Versatz < 50 kpc von Galaxien.")
    print(f"  Ergebnis: {dist_to_gal:.0f} kpc -- {'OK' if dist_to_gal < 50 else 'zu gross'}.")
else:
    print("  Erwartetes Negativergebnis bestaetigt.")
    print("  Momentane Kopplung genuegt nicht fuer Bullet-Cluster.")
    print("  Advektiertes xi-Feld noetig (Kollapsrisiko: Feld-DM).")
print()
print("  Massenverhaeltnis M_gal/M_gas =", M_gal/M_gas)
print("  -> Selbst bei momentaner Kopplung koennte M_gal-Dominanz")
print("     den Peak zur Galaxienposition ziehen (pruefe mit M_gal/M_gas=1).")

# Sensitivitaetstest: gleiche Massen
print()
print("Sensitivitaet: M_gal = M_gas (pessimistisch):")
M_gal_test = M_gas
def n_total_eq(x, los_half=1000*kpc, Nlos=500):
    z_arr = np.linspace(-los_half, los_half, Nlos)
    dz = 2 * los_half / Nlos
    sigma = 0.0
    for z in z_arr:
        r2      = (x - x_gal)**2 + z**2
        r2_gas  = (x - x_gas)**2  + z**2
        phi_gal = G * rho_klump(np.sqrt(r2),     x_gal, M_gal_test, r_gal) / c**2
        phi_gas = G * rho_klump(np.sqrt(r2_gas), x_gas, M_gas, r_gas) / c**2
        sigma  += (phi_gal + phi_gas) * dz
    return sigma

sigma_eq = np.array([n_total_eq(x) for x in x_arr])
pk_eq    = x_kpc[np.argmax(sigma_eq)]
print(f"  Linsenpeak bei gleichen Massen: x = {pk_eq:.1f} kpc")
dist_g_eq = abs(pk_eq - 0.0)
dist_gas_eq = abs(pk_eq - Delta/kpc)
print(f"  Abstand -- Galaxie: {dist_g_eq:.1f} kpc,  Abstand -- Gas: {dist_gas_eq:.1f} kpc")
if dist_g_eq < dist_gas_eq:
    print("  -> Peak folgt noch immer Galaxien (Profilbreite entscheidend)")
else:
    print("  -> Peak liegt beim Gas: Massenverhaeltnis war entscheidend")
