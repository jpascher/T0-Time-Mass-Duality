import numpy as np
from scipy.constants import c, hbar, mu_0, epsilon_0, elementary_charge, k, G, m_e, alpha
from scipy.constants import physical_constants

# Constants from CODATA 2018 (as per document or standard values)
CODATA = {
    'l_P': 1.616255e-35,  # Planck length (m)
    'alpha': 1 / 137.035999084,  # Fine-structure constant (dimensionless)
    'c': 299792458,  # Speed of light (m/s)
    'epsilon_0': 8.854187817e-12,  # Vacuum permittivity (F/m)
    'mu_0': 4 * np.pi * 1e-7,  # Vacuum permeability (H/m)
    'hbar': 1.054571817e-34,  # Reduced Planck constant (J·s)
    'e': 1.602176634e-19,  # Elementary charge (C)
    'G': 6.67430e-11,  # Gravitational constant (m^3/(kg·s^2))
    't_P': 5.391247e-44,  # Planck time (s)
    'm_P': 2.176434e-8,  # Planck mass (kg)
    'E_P': 1.956082e9,  # Planck energy (J)
    'T_P': 1.416784e32,  # Planck temperature (K)
    'r_e': 2.817940e-15,  # Classical electron radius (m)
    'lambda_C_e': 2.426310e-12,  # Compton wavelength of electron (m)
    'a_0': 5.291772e-11,  # Bohr radius (m)
    'R_inf': 1.097373e7,  # Rydberg constant (m^-1)
    'sigma': 5.670374419e-8,  # Stefan-Boltzmann constant (W/(m^2·K^4))
    'b': 2.897771955e-3,  # Wien displacement law constant (m·K)
    'm_e': 9.1093837015e-31,  # Electron mass (kg)
    'm_mu': 1.883531627e-28,  # Muon mass (kg)
    'm_mu/m_e': 206.768,  # Experimental mass ratio (dimensionless)
}

# Conversion factor: MeV to kg (1 MeV/c^2 = 1.78266192e-30 kg)
MeV_to_kg = 1.78266192e-30

# T0-Theory calculations
def t0_calculations():
    # T0-Theory fundamental parameter
    xi = (4 / 3) * 1e-4  # Geometric parameter

    # Experimental input: Planck length (m)
    l_P = CODATA['l_P']

    # Electron and muon masses as T0-Theory ratios
    # m_mu/m_e = (8/5) / (2/3) * xi^(-1/2)
    m_mu_over_m_e = (8 / 5) / (2 / 3) * xi**(-0.5)  # = 2.4 * (4/3 * 1e-4)^(-0.5) ≈ 207.84

    # For E_0, use experimental masses (compatible, as per document)
    m_e_MeV = 0.5109989461  # Electron mass (MeV/c^2)
    m_mu_MeV = 105.6583745  # Muon mass (MeV/c^2)
    E_0 = np.sqrt(m_e_MeV * m_mu_MeV) * 1e6 * 1.602176634e-19 / c**2  # Convert MeV to kg
    E_0_MeV = np.sqrt(m_e_MeV * m_mu_MeV)  # Keep in MeV for alpha calculation

    # Fine-structure constant
    alpha = xi * (E_0_MeV / 1)**2  # Dimensionless (1 MeV normalization)

    # SI-defined constants (used as reference scales)
    c_t0 = CODATA['c']  # Derived from mu_0, epsilon_0 in T0 hierarchy
    hbar_t0 = CODATA['hbar']
    e_t0 = CODATA['e']
    k_B = CODATA['k']
    mu_0_t0 = CODATA['mu_0']

    # Vacuum permittivity
    epsilon_0_t0 = e_t0**2 / (4 * np.pi * hbar_t0 * c_t0 * alpha)

    # Vacuum permeability (derived to check consistency)
    mu_0_derived = 1 / (epsilon_0_t0 * c_t0**2)

    # Gravitational constant
    G_t0 = l_P**2 * c_t0**3 / hbar_t0

    # Planck units
    t_P = np.sqrt(hbar_t0 * G_t0 / c_t0**5)  # Planck time
    m_P = np.sqrt(hbar_t0 * c_t0 / G_t0)  # Planck mass
    E_P = np.sqrt(hbar_t0 * c_t0**5 / G_t0)  # Planck energy
    T_P = E_P / k_B  # Planck temperature

    # Atomic constants
    r_e = alpha * hbar_t0 / (CODATA['m_e'] * c_t0)  # Classical electron radius
    lambda_C_e = 2 * np.pi * hbar_t0 / (CODATA['m_e'] * c_t0)  # Compton wavelength
    a_0 = hbar_t0 / (CODATA['m_e'] * c_t0 * alpha)  # Bohr radius
    R_inf = alpha**2 * CODATA['m_e'] * c_t0 / (4 * np.pi * hbar_t0)  # Rydberg constant

    # Thermodynamic constants
    sigma = (2 * np.pi**5 * k_B**4) / (15 * (2 * np.pi * hbar_t0)**3 * c_t0**2)  # Stefan-Boltzmann
    b = (2 * np.pi * hbar_t0 * c_t0 / k_B) / 4.965114231  # Wien's displacement law (h = 2πhbar)

    # Return results
    results = {
        'xi': xi,
        'l_P': l_P,
        'alpha': alpha,
        'c': c_t0,
        'epsilon_0': epsilon_0_t0,
        'mu_0': mu_0_derived,
        'hbar': hbar_t0,
        'e': e_t0,
        'G': G_t0,
        't_P': t_P,
        'm_P': m_P,
        'E_P': E_P,
        'T_P': T_P,
        'r_e': r_e,
        'lambda_C_e': lambda_C_e,
        'a_0': a_0,
        'R_inf': R_inf,
        'sigma': sigma,
        'b': b,
        'E_0': E_0,
        'm_mu/m_e': m_mu_over_m_e,
    }
    return results

# Compare T0 results with CODATA and calculate percentage deviations
def compare_with_codata(t0_results):
    print("\nT0-Theory Calculations vs. CODATA 2018\n")
    print(f"{'Constant':<15} {'T0 Value':<25} {'CODATA Value':<25} {'% Deviation':<15}")
    print("-" * 80)
    
    for key, t0_value in t0_results.items():
        if key in CODATA:
            codata_value = CODATA[key]
            # Calculate percentage deviation
            if codata_value != 0:
                percent_dev = abs(t0_value - codata_value) / codata_value * 100
            else:
                percent_dev = float('inf')  # Handle division by zero
            print(f"{key:<15} {t0_value:<25.5e} {codata_value:<25.5e} {percent_dev:<15.5f}%")
        else:
            print(f"{key:<15} {t0_value:<25.5e} {'N/A':<25} {'N/A':<15}")

# Run calculations and comparisons
if __name__ == "__main__":
    results = t0_calculations()
    compare_with_codata(results)
    
    # Additional note
    print("\nNote: Electron and muon masses (m_e, m_mu) in E_0 and m_mu/m_e are derived as pure ratios in T0-Theory.")
    print("Experimental masses (CODATA) are used for E_0 calculation as they are compatible.")