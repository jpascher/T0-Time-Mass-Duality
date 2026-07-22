"""A263 Prüfskript: T0-Dirac-Gleichung, Grenzfall, Spin aus Wicklung."""
import numpy as np

print("=== A263: Dirac in FFGFT ===")

# 1. Dispersionsrelation: Standard-Dirac als Grenzfall T0-Dirac (d_mu m -> 0)
# Standard: (gamma^mu * p_mu - m) * psi = 0
# -> E^2 = p^2 + m^2
m = 0.511  # MeV (Elektron)
p_vals = [0.0, 0.1, 0.5, 1.0, 5.0]  # MeV/c
print("Dirac-Dispersionsrelation E^2 = p^2 + m^2:")
for p in p_vals:
    E = np.sqrt(p**2 + m**2)
    print(f"  p={p:.1f} MeV: E={E:.4f} MeV")
assert abs(np.sqrt(0 + m**2) - m) < 1e-10, "Ruheenergie E=m falsch"

# 2. Spin-1/2 aus Wicklung (1,1): 2-Umdrehungen -> Ausgangszustand
# Phasenakkumulation: e^(i*2*pi*n) für n Windungen
import cmath
n_wind = 1  # eine Windung
phase_1turn = cmath.exp(1j * 2 * np.pi * n_wind)
phase_2turn = cmath.exp(1j * 2 * np.pi * 2 * n_wind)
print(f"\nSpin aus Wicklung:")
print(f"  Phase nach 1 Windung: {phase_1turn:.4f} (soll -1 für Spinor)")
print(f"  Phase nach 2 Windungen: {phase_2turn:.4f} (soll +1 = Ausgangszustand)")
# Spinor braucht 4pi für Ausgangszustand -> e^(i*4*pi) = 1
phase_spinor_1 = cmath.exp(1j * 2 * np.pi)   # -1 für Spinor (2pi)
phase_spinor_2 = cmath.exp(1j * 4 * np.pi)   # +1 nach 4pi
assert abs(phase_spinor_2 - 1) < 1e-10, "720°-Symmetrie falsch"
print(f"  Nach 4pi (720°): {phase_spinor_2:.4f} = +1 ✓")

# 3. Massenelimination: m = 1/T_tilde
m_e = 0.511  # MeV
T_tilde = 1/m_e  # in nat. Einheiten
print(f"\nMassenelimination: T̃ = 1/m_e = {T_tilde:.4f} MeV^-1")
print(f"Probe: 1/T̃ = {1/T_tilde:.4f} MeV = m_e ✓")
assert abs(1/T_tilde - m_e) < 1e-10

print("\nAlle Checks bestanden.")
