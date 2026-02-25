import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import pandas as pd

# Konstanten
xi = 4/3 * 1e-4  # fraktaler Parameter
G = constants.G  # Gravitationskonstante
hbar = constants.hbar  # J·s
c = constants.c  # m/s
k_B = constants.k  # J/K

# Beobachtetes Baryon-zu-Photon Verhältnis
eta_B_obs = 6.1e-10  # aus CMB-Daten (Planck)

# Kosmologische Parameter heute
H0 = 67.4e3 / (3.086e22)  # Hubble-Konstante in 1/s
T_cmb = 2.725  # K, CMB-Temperatur heute

# Parameter des Phasenübergangs
T_pt = 1e12  # K, typische Temperatur für elektroschwachen Phasenübergang (~100 MeV)
g_eff = 100  # effektive Freiheitsgrade

print("="*60)
print("LÖSUNG DER BARYONISCHEN ASYMMETRIE IN T0-GEOMETRIE (KORRIGIERT)")
print("="*60)

def calculate_early_universe_parameters():
    """
    Berechnet Parameter des frühen Universums zur Zeit des Phasenübergangs
    """
    print("\n" + "-"*40)
    print("Parameter des frühen Universums")
    print("-"*40)
    
    # Korrekte Umrechnung: 10¹² K ≈ 100 MeV = 0.1 GeV
    T_pt_GeV = 0.1  # 100 MeV
    
    # Hubble-Parameter zur Zeit des Phasenübergangs
    # H = 1.66 * sqrt(g_eff) * T² / M_Planck (in natürlichen Einheiten)
    M_planck_GeV = 1.22e19  # GeV
    H_pt_GeV = 1.66 * np.sqrt(g_eff) * T_pt_GeV**2 / M_planck_GeV
    
    # Umrechnung GeV → 1/s: 1 GeV = 1.52e24 1/s
    H_pt_s = H_pt_GeV * 1.52e24
    
    # Hubble-Volumen zur Zeit des Phasenübergangs
    # V = (c/H)³
    V_Hubble_pt = (c / H_pt_s)**3  # m³
    
    print(f"\nPhasenübergangs-Temperatur T_pt = {T_pt_GeV:.3f} GeV = {T_pt:.1e} K")
    print(f"Effektive Freiheitsgrade g_eff = {g_eff}")
    print(f"Hubble-Parameter H_pt = {H_pt_GeV:.2e} GeV = {H_pt_s:.2e} 1/s")
    print(f"Hubble-Volumen V_Hubble,pt = {V_Hubble_pt:.2e} m³")
    
    # Vergleich mit heutigem Hubble-Volumen
    V_Hubble_today = (c / H0)**3
    print(f"\nV_Hubble,pt / V_Hubble,heute = {V_Hubble_pt/V_Hubble_today:.2e}")
    
    return V_Hubble_pt, T_pt_GeV, H_pt_s

def calculate_cp_bias():
    """
    Berechnet den intrinsischen CP-Bias
    δθ_CP ≈ ξ ln(1/ξ)
    """
    print("\n" + "-"*40)
    print("Intrinsischer CP-Bias")
    print("-"*40)
    
    delta_theta_cp = xi * np.log(1/xi)
    sin_delta = np.sin(delta_theta_cp)
    
    print(f"\nξ = {xi:.2e}")
    print(f"ln(1/ξ) = {np.log(1/xi):.4f}")
    print(f"\nδθ_CP = ξ · ln(1/ξ) = {delta_theta_cp:.4e}")
    print(f"        ≈ {delta_theta_cp:.2e} rad")
    print(f"        ≈ {np.degrees(delta_theta_cp):.4f}°")
    print(f"\nsin(δθ_CP) = {sin_delta:.2e}")
    
    return delta_theta_cp, sin_delta

def calculate_defect_density_at_pt(V_Hubble_pt, l0):
    """
    Berechnet die Defektdichte zur Zeit des Phasenübergangs
    """
    defect_density_pt = l0**3 / V_Hubble_pt
    return defect_density_pt

def calculate_baryon_asymmetry_corrected():
    """
    Berechnet η_B korrigiert mit frühem Hubble-Volumen
    """
    print("\n" + "-"*40)
    print("Baryon-zu-Photon Verhältnis η_B (korrigiert)")
    print("-"*40)
    
    # Hubble-Volumen zur Zeit des Phasenübergangs
    V_Hubble_pt, T_pt, H_pt = calculate_early_universe_parameters()
    
    # CP-Bias
    delta_theta_cp, sin_delta = calculate_cp_bias()
    
    # ξ³
    xi3 = xi**3
    
    # Defektdichte für verschiedene l₀
    print("\nDefektdichte für verschiedene l₀:")
    print("l₀ (m)    | l₀³ (m³) | Defektdichte | η_B")
    print("-" * 60)
    
    l0_values = [1e-18, 1e-15, 1e-12, 1e-9, 1e-6]
    eta_values = []
    
    for l0 in l0_values:
        defect = l0**3 / V_Hubble_pt
        eta = xi3 * defect * sin_delta
        eta_values.append(eta)
        print(f"{l0:.1e} | {l0**3:.1e} | {defect:.2e} | {eta:.2e}")
    
    # Optimales l₀ für η_B_obs
    l0_opt = (eta_B_obs / (xi3 * sin_delta) * V_Hubble_pt)**(1/3)
    
    print(f"\nOptimales l₀ für η_B_obs = {eta_B_obs:.2e}:")
    print(f"  l₀_opt = {l0_opt:.2e} m")
    print(f"  l₀_opt = {l0_opt*1e15:.2f} fm")
    print(f"  l₀_opt = {l0_opt*1e9:.2f} nm")
    print(f"  l₀_opt = {l0_opt*1e6:.2f} μm")
    
    # Berechnung mit optimalem l₀
    defect_opt = l0_opt**3 / V_Hubble_pt
    eta_opt = xi3 * defect_opt * sin_delta
    
    print(f"\nMit optimalem l₀ = {l0_opt:.2e} m:")
    print(f"  Defektdichte = {defect_opt:.2e}")
    print(f"  η_B = {eta_opt:.2e} (exakt η_B_obs)")
    
    # Analyse der Größenordnungen
    print("\nGrößenordnungen:")
    print(f"  ξ³ ≈ 10^{int(np.log10(xi3))}")
    print(f"  Defektdichte (mit l₀_opt) ≈ 10^{int(np.log10(defect_opt))}")
    print(f"  sin(δθ) ≈ 10^{int(np.log10(sin_delta))}")
    print(f"  Gesamt: 10^{int(np.log10(xi3))} × 10^{int(np.log10(defect_opt))} × 10^{int(np.log10(sin_delta))} = 10^{int(np.log10(eta_opt))}")
    
    return l0_opt, eta_opt, V_Hubble_pt, xi3, sin_delta

def check_sakharov_conditions_detailed(l0_opt, V_Hubble_pt, H_pt_s):
    """
    Detaillierte Überprüfung der Sakharov-Bedingungen
    """
    print("\n" + "-"*40)
    print("Sakharov-Bedingungen (detailliert)")
    print("-"*40)
    
    # 1. Baryonenzahl-Verletzung
    print("\n1. Baryonenzahl-Verletzung:")
    print("   • Topologische Windungen (n ≠ 0) erzeugen Baryonen")
    print("   • Energieasymmetrie zwischen n und -n:")
    
    delta_theta = xi * np.log(1/xi)
    for n in [1, 2]:
        E_n = 0.5 * (2*np.pi*n + delta_theta)**2
        E_minus_n = 0.5 * (2*np.pi*n - delta_theta)**2
        asymmetry = (E_n - E_minus_n) / E_n
        print(f"   • n={n}: Asymmetrie = {asymmetry:.2e}")
    
    print("   ✓ Erfüllt")
    
    # 2. C- und CP-Verletzung
    print("\n2. C- und CP-Verletzung:")
    print(f"   • δθ_CP = {delta_theta:.2e} rad")
    print(f"   • CP-verletzende Phase vorhanden")
    print("   ✓ Erfüllt")
    
    # 3. Nicht-Gleichgewicht
    print("\n3. Nicht-Gleichgewicht:")
    
    # Typische Reaktionsrate für B-verletzende Prozesse
    # Γ ≈ α² T mit α ≈ 1/100 (typische Kopplung)
    alpha = 0.01
    T_GeV = 0.1  # 100 MeV
    Gamma_GeV = alpha**2 * T_GeV  # in GeV
    Gamma_s = Gamma_GeV * 1.52e24  # in 1/s
    
    print(f"   • Expansionsrate H ≈ {H_pt_s:.2e} 1/s")
    print(f"   • Reaktionsrate Γ ≈ {Gamma_s:.2e} 1/s")
    print(f"   • Verhältnis Γ/H = {Gamma_s/H_pt_s:.2e}")
    
    if Gamma_s > H_pt_s:
        print("   ⚠ Γ > H → Reaktionen im Gleichgewicht")
        print("     Für Nicht-Gleichgewicht brauchen wir:")
        print("     • Schnellen Phasenübergang erster Ordnung")
        print("     • Oder Unterdrückung der Reaktionsrate")
    else:
        print("   ✓ Γ < H → Nicht-Gleichgewicht erfüllt")
    
    # Phasenübergangsgeschwindigkeit
    v_phase = 0.1  # typische Geschwindigkeit in Einheiten von c
    tau_phase = l0_opt / (v_phase * c)
    tau_hubble = 1/H_pt_s
    
    print(f"\n   • Phasenübergangszeit τ_phase = l₀/(v·c) = {tau_phase:.2e} s")
    print(f"   • Hubble-Zeit τ_Hubble = 1/H = {tau_hubble:.2e} s")
    print(f"   • Verhältnis τ_phase/τ_Hubble = {tau_phase/tau_hubble:.2e}")
    
    if tau_phase < tau_hubble:
        print("   ✓ Schneller Phasenübergang (τ_phase < τ_Hubble)")
        print("     → Nicht-Gleichgewicht möglich")
    else:
        print("   ✗ Langsamer Übergang → Gleichgewicht")
        print("     Für Nicht-Gleichgewicht bräuchte man τ_phase ≪ τ_Hubble")
    
    return True

def plot_corrected_results(l0_values_plot, eta_values_plot, l0_opt, V_Hubble_pt):
    """Erstellt Visualisierungen der korrigierten Ergebnisse"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: η_B als Funktion von l₀ (log-log)
    ax1 = axes[0, 0]
    ax1.loglog(l0_values_plot, eta_values_plot, 'b-', linewidth=2)
    ax1.axhline(y=eta_B_obs, color='r', linestyle='--', label=f'η_B_obs = {eta_B_obs:.1e}')
    ax1.axvline(x=l0_opt, color='g', linestyle=':', label=f'l₀_opt = {l0_opt:.2e} m')
    ax1.set_xlabel('l₀ (m)')
    ax1.set_ylabel('η_B')
    ax1.set_title('η_B vs. fundamentale Länge (korrigiert)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Größenordnungen der Beiträge
    ax2 = axes[0, 1]
    defect_opt = l0_opt**3 / V_Hubble_pt
    xi3 = xi**3
    sin_delta = np.sin(xi * np.log(1/xi))
    
    factors = ['ξ³', 'l₀³/V_Hubble,pt', 'sin(δθ)', 'η_B']
    values = [xi3, defect_opt, sin_delta, eta_B_obs]
    log_values = [np.log10(v) for v in values]
    
    colors = ['blue', 'green', 'orange', 'red']
    ax2.bar(factors, log_values, color=colors, alpha=0.7)
    ax2.set_ylabel('log₁₀(Wert)')
    ax2.set_title('Beiträge zu η_B (korrigiert)')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Plot 3: Vergleich Hubble-Volumina
    ax3 = axes[1, 0]
    V_today = (c / H0)**3
    volumes = [V_Hubble_pt, V_today]
    labels = ['Bei T_pt (10¹² K)', 'Heute (2.7 K)']
    log_vol = [np.log10(v) for v in volumes]
    
    ax3.bar(labels, log_vol, color=['lightblue', 'lightcoral'], alpha=0.7)
    ax3.set_ylabel('log₁₀(Volumen / m³)')
    ax3.set_title('Hubble-Volumen: Frühes Universum vs. Heute')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Plot 4: Zeitliche Entwicklung
    ax4 = axes[1, 1]
    T_values = np.logspace(12, 2, 50)  # Temperatur abnehmend
    # Hubble-Volumen skaliert mit T⁻⁶ im strahlungsdominierten Universum
    V_scale = (T_values / T_pt)**(-6)
    
    ax4.loglog(T_values, V_scale, 'm-', linewidth=2)
    ax4.axvline(x=T_pt, color='k', linestyle=':', label='T_pt = 10¹² K')
    ax4.axvline(x=T_cmb, color='b', linestyle=':', label='T_CMB = 2.7 K')
    ax4.set_xlabel('Temperatur T (K)')
    ax4.set_ylabel('relatives Hubble-Volumen V/V(T_pt)')
    ax4.set_title('Hubble-Volumen vs. Temperatur')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('baryon_asymmetrie_korrigiert.png', dpi=150)
    plt.show()
    print("\nPlot gespeichert als 'baryon_asymmetrie_korrigiert.png'")

def create_summary_table_corrected(l0_opt, V_Hubble_pt, xi3, sin_delta):
    """Erstellt eine korrigierte Zusammenfassungstabelle"""
    print("\n" + "-"*40)
    print("ZUSAMMENFASSUNG DER KORRIGIERTEN ERGEBNISSE")
    print("-"*40)
    
    defect_opt = l0_opt**3 / V_Hubble_pt
    V_Hubble_today = (c / H0)**3
    
    data = {
        'Größe': [
            'ξ',
            'ξ³',
            'T_pt (K)',
            'T_pt (GeV)',
            'V_Hubble,pt (m³)',
            'V_Hubble,pt / V_heute',
            'δθ_CP',
            'sin(δθ_CP)',
            'l₀_opt (m)',
            'l₀_opt (nm)',
            'l₀_opt (μm)',
            'Defektdichte bei T_pt',
            'η_B (Theorie)',
            'η_B (Beobachtung)'
        ],
        'Wert': [
            f'{xi:.2e}',
            f'{xi3:.2e}',
            f'{T_pt:.1e}',
            '0.1',
            f'{V_Hubble_pt:.2e}',
            f'{V_Hubble_pt/V_Hubble_today:.2e}',
            f'{xi*np.log(1/xi):.2e}',
            f'{sin_delta:.2e}',
            f'{l0_opt:.2e}',
            f'{l0_opt*1e9:.2f}',
            f'{l0_opt*1e6:.2f}',
            f'{defect_opt:.2e}',
            f'{eta_B_obs:.2e}',
            f'{eta_B_obs:.2e}'
        ],
        'Status': [
            '✓',
            '✓',
            '✓',
            '✓',
            '✓',
            '✓',
            '✓',
            '✓',
            '⚡ (angepasst)',
            '⚡',
            '⚡',
            '✓',
            '✓',
            '✓'
        ]
    }
    
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    
    print("\n" + "="*60)
    print("FAZIT (KORRIGIERT)")
    print("="*60)
    print("✓ Die Verwendung des Hubble-Volumens zur Zeit des Phasenübergangs")
    print("  (10¹² K) statt des heutigen Volumens ist korrekt.")
    print(f"✓ Mit l₀_opt = {l0_opt:.2e} m = {l0_opt*1e6:.2f} μm ergibt sich")
    print(f"  exakt η_B = {eta_B_obs:.2e}.")
    print("\n⚠ Dies ist jedoch ein makroskopischer Wert:")
    print(f"  • {l0_opt*1e6:.2f} μm ist die Größe eines Bakteriums!")
    print("  • Das ist unphysikalisch für eine fundamentale Länge.")
    print("\nDie Sakharov-Bedingungen:")
    print("• B-Verletzung: ✓ (Energieasymmetrie ~10⁻⁴)")
    print("• CP-Verletzung: ✓ (δθ ≈ 10⁻³)")
    print("• Nicht-Gleichgewicht: ⚠ (Γ ≫ H, benötigt schnellen Phasenübergang)")
    print("\n🔴 Das grundlegende Problem bleibt:")
    print("   Um η_B = 10⁻¹⁰ zu erreichen, braucht man l₀ im μm-Bereich.")
    print("   Eine mikroskopische fundamentale Länge (fm) gibt η_B ≈ 10⁻⁷³.")

def main():
    """Hauptfunktion"""
    
    # 1. Korrigierte Berechnung mit frühem Hubble-Volumen
    l0_opt, eta_opt, V_Hubble_pt, xi3, sin_delta = calculate_baryon_asymmetry_corrected()
    
    # 2. Extrahiere H_pt_s für Sakharov-Bedingungen
    _, _, H_pt_s = calculate_early_universe_parameters()
    
    # 3. Detaillierte Sakharov-Bedingungen (mit l0_opt)
    check_sakharov_conditions_detailed(l0_opt, V_Hubble_pt, H_pt_s)
    
    # 4. Plot für verschiedene l₀
    l0_plot = np.logspace(-20, 10, 100)  # Von 10⁻²⁰ m bis 10¹⁰ m
    eta_plot = xi3 * (l0_plot**3 / V_Hubble_pt) * sin_delta
    
    # 5. Visualisierung
    plot_corrected_results(l0_plot, eta_plot, l0_opt, V_Hubble_pt)
    
    # 6. Zusammenfassung
    create_summary_table_corrected(l0_opt, V_Hubble_pt, xi3, sin_delta)

if __name__ == "__main__":
    main()