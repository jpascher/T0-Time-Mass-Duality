import numpy as np

# ============================================================================
# Wie entsteht das "H_0-Artefakt"? - FFGFT-Lesart (Dok 026 / 182)
#
# These: H_0 ist KEINE Expansionsrate, sondern die als Expansion fehlgedeutete
# Rate der fraktalen Wegverlaengerung des xi-Feldes. Der Beobachter misst eine
# lineare z(d)-Beziehung und tauft deren Steigung "H_0/c". In FFGFT ist diese
# Steigung ein GEOMETRISCHER Koeffizient (E_H/(hbar c)), keine Dynamik.
#
# WICHTIG: KEINE direkte Gleichsetzung xi <-> H_0 auf Sub-Planck-Skala. Die Kette laeuft ueber die
# Hubble-ENERGIE E_H und dann via hbar*c (SI-Faktor) zur Laenge R_H. In nat.
# Einheiten sind Laenge und Energie dual; der Fehler der naiven Form ist die
# Skalenwahl (L_0 statt R_H), nicht die Energie-Laengen-Dualitaet.
# ============================================================================

# --- FFGFT-Grundgroessen (alle aus Dok 182) ---
xi   = 4/30000.0
E0   = 7.398e6          # eV = sqrt(m_e * m_mu)  (charakteristische T0-Energie)
exp_H= 41/4             # Exponent -- laut Dok 182/026 NOCH NICHT voll hergeleitet
hbar = 6.582e-16        # eV*s
c    = 2.998e8          # m/s
lP   = 1.616e-35        # m
Mpc  = 3.086e22         # m

print("="*70)
print("H_0 als Artefakt der fraktalen Wegverlaengerung (Dok 026/182)")
print("="*70)
print(f"xi = {xi:.6e}")
print(f"E0 = sqrt(m_e*m_mu) = {E0/1e6:.3f} MeV\n")

# --- Hubble-Energie und H_0 ---
E_H = E0 * xi**exp_H
H0_s = E_H / hbar                    # 1/s
H0_kms_Mpc = H0_s * Mpc / 1000.0
# --- explizite Schritt-fuer-Schritt-Logarithmusrechnung (Nachvollziehbarkeit) ---
import numpy as _np
_lnE0 = _np.log(E0); _lnxi = _np.log(xi)
print("Schrittweise (ln): ln(E_H) = ln(E0) + (41/4)*ln(xi)")
print(f"   ln(E0)        = {_lnE0:.4f}")
print(f"   ln(xi)        = {_lnxi:.4f}   (NICHT -8.92 runden! 3. Stelle kippt das Ergebnis)")
print(f"   (41/4)*ln(xi) = {(41/4)*_lnxi:.4f}")
print(f"   ln(E_H)       = {_lnE0 + (41/4)*_lnxi:.4f}  -> E_H = {_np.exp(_lnE0+(41/4)*_lnxi):.4e} eV")
print()
print("Hubble-Energie:  E_H = E0 * xi^(41/4)")
print(f"  xi^(41/4) = {xi**exp_H:.4e}")
print(f"  E_H       = {E_H:.4e} eV         (Korpus 1.412e-33)")
print(f"  H_0^T0    = E_H/hbar = {H0_kms_Mpc:.2f} km/s/Mpc   (Korpus 66.2)")
print(f"  Planck 67.4 -> Abweichung {100*(H0_kms_Mpc/67.4-1):+.1f}%")

# --- der Artefakt-Mechanismus, explizit ---
print("\n" + "-"*70)
print("WIE das Artefakt entsteht:")
print("-"*70)
kappa = H0_s / c
print(f"""
1. FFGFT: ueber physische Strecke d sammelt das Photon fraktale Weg-
   verlaengerung; fuer kleine z ist z(d) linear mit Steigung
     kappa = E_H/(hbar c) = {kappa:.3e} 1/m.
2. Der Beobachter im Expansionsbild liest dieselbe lineare z(d)-Kurve und
   DEFINIERT ihre Steigung als H_0/c. Daraus:
     H_0 (gemessen) = kappa * c = E_H/hbar = {H0_kms_Mpc:.1f} km/s/Mpc.
3. H_0 ist also kein dynamischer Expansionsparameter, sondern der als
   Expansion fehlinterpretierte geometrische Koeffizient der Wegverlaengerung.
   Das 'Artefakt' ist die UMDEUTUNG einer Steigung -- kein Messfehler.
""")
print(f"   Konsistenz: c * kappa = {c*kappa:.3e} 1/s = H_0^T0")
print(f"   Maximalskala R_H = hbar c/E_H = {hbar*c/E_H:.3e} m (Korpus 1.4e26):")
print(f"     jenseits R_H -> z -> oo (kein Signal); KEIN Teilchenhorizont noetig.")

# --- warum die naive xi<->H_0-Bruecke scheitern MUSSTE ---
print("-"*70)
print("Warum eine direkte Gleichsetzung xi/L0 = H_0/c FALSCH ist:")
L0 = xi * lP        # = xi*lP  (Dok 182), NICHT lP/xi
hbarc_eVm = 1.973e-7   # eV*m  (SI-Umrechnungsfaktor hbar*c)
print(f"   L_0 = xi*lP = {L0:.3e} m   (Sub-Planck-Granulierung)")
print(f"   R_H = hbar c/E_H = {hbar*c/E_H:.3e} m   (kosmologische Skala)")
print(f"   R_H/L0 = {(hbar*c/E_H)/L0:.3e}   (folgt allein aus xi)")
print("""   Der Fehler ist NICHT 'Energie vs. Laenge': in nat. Einheiten
   (hbar=c=1) sind beide dual, der Uebergang zu SI-Metern ist genau der
   Faktor hbar*c = 1.973e-7 eV*m. Der Fehler ist die SKALENWAHL -- die
   naive Form koppelt xi an L_0 (Sub-Planck) statt an R_H (kosmologisch).
   Die korrekte Kette laeuft ueber hbar*c:
       xi -> E_H = E0*xi^(41/4) -> R_H = hbar c/E_H -> H_0 = c/R_H = E_H/hbar
   hbar*c ist dabei der SI-Faktor, der die Energie-Darstellung (E_H) in
   die Laengen-Darstellung (R_H) ueberfuehrt.""")

print("\n" + "="*70)
print("EHRLICHER VORBEHALT (Dok 182/026 markieren das selbst):")
print("  Der Exponent 41/4 folgt laut Korpus aus der RG-/Skalenfluss-Struktur")
print("  des xi-Feldes ueber kosmologische Skalen, ist aber NOCH NICHT voll")
print("  aus der xi-Feldtheorie hergeleitet. Die -1.9%-Uebereinstimmung ist")
print("  ein starkes Konsistenzargument, KEINE abgeschlossene Ableitung.")
print("  -> H_0^T0 ist Reduktionsschicht, nicht Kern-Ergebnis.")
print("="*70)
