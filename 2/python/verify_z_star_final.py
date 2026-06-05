#!/usr/bin/env python3
"""
================================================================================
VERIFIKATION z_* — unabhaengige Nachrechnung der eingereichten Skripte
================================================================================

Prueft die Behauptung z_* ~ 1103 aus ffgft_z_star_sigma_from_xi.py und der
DeepSeek/Gemini-Dokumentation.

Methode: Jeder Schritt einzeln, keine Uebernahme der Skript-Ergebnisse.
Nur SI-CODATA-Konstanten + xi = 1/7500.

Ergebnis (Vorwegnahme): z_* = 875 mit konsistenter Geometrie.
Der Wert 1103 erfordert einen frei gewaehlten Exponenten 8.55, der NICHT
aus xi folgt.
================================================================================
"""
import math

# --- Fundamentalkonstanten (CODATA, SI) ---
c    = 299792458.0          # m/s
hbar = 1.054571817e-34      # J*s
eV   = 1.602176634e-19      # J
l_P  = 1.616255e-35         # m
k_B  = 1.380649e-23         # J/K

# --- Der eine Parameter ---
xi     = 1/7500
D_f    = 3 - xi
ln_inv = math.log(1/xi)
L0     = xi * l_P

print("="*72)
print("VERIFIKATION z_*")
print("="*72)
print(f"xi          = 1/7500 = {xi:.10e}")
print(f"D_f = 3-xi  = {D_f:.10f}")
print(f"ln(1/xi)    = {ln_inv:.10f}")
print(f"L0 = xi*l_P = {L0:.6e} m")
print()

# --- Elektronmasse: gemessen vs FFGFT-Formel ---
m_e_gemessen = 510998.95                       # eV (CODATA)
v = 246.22e9                                   # eV (Higgs-VEV)
m_e_ffgft = (4/3) * xi**1.5 * v                # FFGFT-Leptonformel
print("Elektronmasse:")
print(f"  gemessen      = {m_e_gemessen:.2f} eV")
print(f"  FFGFT-Formel  = (4/3)*xi^1.5*v = {m_e_ffgft:.2f} eV  ({100*(m_e_ffgft/m_e_gemessen-1):+.2f}%)")
print()

def lambda_compton(m_eV):
    """Reduzierte Compton-Wellenlaenge lambda_bar = hbar/(m c)."""
    m_kg = m_eV * eV / c**2
    return hbar / (m_kg * c)

# --- Resonanzbedingung ---
# Skript-Definition: L_corr(z) = L0 * (1+z)^(1/ln(1/xi))
# Resonanz L_corr(z_*) = lambda_e:
#   (1+z_*)^(1/ln(1/xi)) = lambda_e/L0
#   => 1+z_* = (lambda_e/L0)^(ln(1/xi))   [Aufloesung A, korrekt nach Algebra]
#   ODER falls L_corr = L0*(1+z)^(ln(1/xi)):
#   => 1+z_* = (lambda_e/L0)^(1/ln(1/xi)) [Aufloesung B]
print("Resonanzbedingung L_corr(z_*) = lambda_e")
print("Zwei moegliche Auflösungen je nach Definition von L_corr:")
print()
for name, m_eV in [("gemessen", m_e_gemessen), ("FFGFT", m_e_ffgft)]:
    lam = lambda_compton(m_eV)
    ratio = lam / L0
    # Aufloesung A: 1+z = ratio^ln(1/xi)
    log10_A = ln_inv * math.log10(ratio)
    # Aufloesung B: 1+z = ratio^(1/ln(1/xi))
    z_B = ratio**(1/ln_inv) - 1
    print(f"  m_e {name:9s}: lambda_e={lam:.4e} m, ratio=lambda_e/L0={ratio:.4e}")
    print(f"    Aufloesung A (1+z=ratio^ln(1/xi)) : 1+z_* ~ 10^{log10_A:.0f}  (OVERFLOW, sinnlos)")
    print(f"    Aufloesung B (1+z=ratio^(1/ln))   : z_* = {z_B:.1f}")
    print()

# --- Was die DeepSeek-Doku rechnet: Exponent 8.55 statt ln(1/xi) ---
print("="*72)
print("Was die DeepSeek/Gemini-Dokumentation behauptet (z_* = 1103):")
print("="*72)
lam = lambda_compton(m_e_gemessen)
ratio = lam / L0
print(f"  Die Doku setzt den Exponenten manuell auf 8.55:")
print(f"    z_* = ratio^(1/8.55) - 1 = {ratio**(1/8.55)-1:.1f}")
print(f"  Mit dem ehrlichen geometrischen Wert ln(1/xi) = {ln_inv:.4f}:")
print(f"    z_* = ratio^(1/{ln_inv:.4f}) - 1 = {ratio**(1/ln_inv)-1:.1f}")
print()
print(f"  Behauptete Rechtfertigung fuer 8.55: 'fraktale D_f-Inversion'")
print(f"    ln(1/xi) * D_f/3       = {ln_inv*D_f/3:.4f}  (≈ ln(1/xi), KEINE Verschiebung auf 8.55)")
print(f"    ln(1/xi) * (D_f-1)/2   = {ln_inv*(D_f-1)/2:.4f}")
print(f"  => Der Exponent 8.55 ist NICHT aus xi herleitbar.")
print()

# --- Welcher Exponent ergibt exakt z_*=1100? ---
exp_fuer_1100 = math.log(ratio)/math.log(1101)
print(f"  Exponent fuer z_*=1100: ln(ratio)/ln(1101) = {exp_fuer_1100:.4f}")
print(f"  Das ist weder ln(1/xi)={ln_inv:.4f} noch der Doku-Wert 8.55.")
print()

print("="*72)
print("BEFUND z_*:")
print("="*72)
print(f"""
1. Mit konsistenter Geometrie (Exponent = ln(1/xi) = {ln_inv:.4f}):
   z_* = {ratio**(1/ln_inv)-1:.0f}   (egal ob gemessene oder FFGFT-m_e: 875 vs 876)

2. Der Doku-Wert z_* = 1103 erfordert den Exponenten 8.55, der NICHT
   aus xi folgt. Die behauptete 'fraktale D_f-Inversion' rechtfertigt
   ihn nicht: ln(1/xi)*D_f/3 = {ln_inv*D_f/3:.4f} ≈ ln(1/xi).

3. Das eingereichte Skript selbst (z_star = ratio^ln(1/xi)) ergibt
   einen Overflow (~10^234), ist also in dieser Form nicht lauffaehig.

FAZIT: z_* = 875 ist der konsistente FFGFT-Wert. z_* = 1103 ist NICHT
aus der Geometrie hergeleitet, sondern erfordert einen gewaehlten Exponenten.
""")
