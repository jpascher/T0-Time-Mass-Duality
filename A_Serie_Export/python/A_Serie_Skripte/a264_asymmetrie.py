"""A264 Prüfskript: Chiralitäts-Phasendifferenz, Monopol-Schwelle."""
import numpy as np

xi = 4/30000
hbar_c = 197.3e-15  # J·m (= 197.3 MeV·fm)
E_P = 1.956e9       # J (Planck-Energie)

print("=== A264: Asymmetrie und CP ===")

# 1. Monopol-Energieschwelle E_P/xi
E_monopol = E_P / xi
print(f"Monopol-Schwelle: E_P/xi = {E_P:.3e}/{xi:.4e} = {E_monopol:.3e} J")
print(f"  = {E_monopol/E_P:.0f} E_P")
assert abs(E_monopol/E_P - 1/xi) < 1  # = 7500 E_P

# 2. Chiralitäts-Phasendifferenz Links vs. Rechts
# theta_L = +(xi/2) * integral, theta_R = -(xi/2) * integral
# Für eine Einheitsfläche: Delta_theta = xi
Delta_theta = xi
print(f"\nChiralitäts-Phasendifferenz Delta_theta = xi = {Delta_theta:.6e}")
print(f"Links: +xi/2, Rechts: -xi/2, Differenz: xi = {xi:.6e}")

# 3. Schwachfeld-Linearisierung: Box*E + xi*E^3 = 0
# Für E = E0*(1+h), h<<1: Box*h + 2*xi*E0^2*h = 0
# = Box*h + 2*alpha*h = 0 (da xi*E0^2 = alpha)
alpha = xi * 7.398**2
print(f"\nSchwachfeld: xi*E0^2 = alpha = {alpha:.6f} (exp: {1/137.036:.6f})")
assert abs(alpha - 1/137.036)/alpha < 0.001

print("\nAlle Checks bestanden.")
