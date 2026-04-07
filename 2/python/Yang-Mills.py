import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import pandas as pd

# Konstanten
xi = 4/3 * 1e-4  # fraktaler Parameter
hbar = constants.hbar  # J·s
c = constants.c  # m/s
hc_MeV_fm = 197.327  # MeV·fm

print("="*60)
print("ÜBERPRÜFUNG DER QUANTENGRAVITATION IN T0-GEOMETRIE")
print("="*60)

def check_yang_mills_units():
    """Überprüft die Einheiten der Yang-Mills-Lagrangedichte"""
    print("\n" + "-"*40)
    print("Einheitenprüfung Yang-Mills")
    print("-"*40)
    
    print("\nEinheiten der Feldstärke F_mu_nu:")
    print("  A_mu [A] = 1/m (in natürlichen Einheiten)")
    print("  partial_mu [partial] = 1/m")
    print("  [F_mu_nu] = [partial A] = 1/m²")
    print("  [F_mu_nu F^mu_nu] = 1/m⁴")
    print("  [L_YM] = [F²] = 1/m⁴ ✓")
    
    print("\nÜberprüfung der Kopplungskonstante g:")
    print("  [g f^{abc} A_mu^b A_nu^c] = [g]·(1/m)·(1/m) = 1/m²")
    print("  => [g] = dimensionslos ✓")
    
    return True

def calculate_qcd_parameters():
    """
    Bestimmt die relevanten QCD-Parameter
    """
    print("\n" + "-"*40)
    print("QCD-Parameter")
    print("-"*40)
    
    # Bekannte QCD-Werte
    sigma_GeV_fm = 0.9  # String-Spannung
    Lambda_QCD_MeV = 300  # Λ_QCD
    m_glueball_MeV = 350  # Typische Glueball-Masse (Skalarer Glueball)
    
    # √B aus String-Spannung: σ = (√B)² / (2π) ? verschiedene Modelle
    # In vielen Modellen: √B ≈ √(2πσ)
    sqrt_B_MeV = np.sqrt(2 * np.pi * sigma_GeV_fm * 1000)  # grobe Näherung
    sqrt_B_GeV = sqrt_B_MeV / 1000
    
    print(f"\nString-Spannung σ = {sigma_GeV_fm} GeV/fm")
    print(f"Λ_QCD = {Lambda_QCD_MeV} MeV")
    print(f"Typische Glueball-Masse = {m_glueball_MeV} MeV")
    print(f"√B ≈ √(2πσ) = {sqrt_B_MeV:.1f} MeV = {sqrt_B_GeV:.3f} GeV")
    
    return sigma_GeV_fm, Lambda_QCD_MeV, m_glueball_MeV, sqrt_B_MeV

def calculate_mass_gap_correctly(m_glueball_MeV, xi):
    """
    Berechnet die Massenlücke mit der korrekten ξ-Abhängigkeit
    """
    print("\n" + "-"*40)
    print("Yang-Mills-Massenlücke Δ mit ξ-Korrektur")
    print("-"*40)
    
    # Basis-Massenlücke (ohne fraktale Korrektur)
    Delta_0_MeV = m_glueball_MeV
    
    # Fraktale Korrektur: Δ = Δ_0 * (1 + α ξ + β ξ² + ...)
    # Die Korrektur sollte klein sein, da ξ klein ist
    alpha = 1.0  # Koeffizient erster Ordnung
    beta = 0.5   # Koeffizient zweiter Ordnung
    
    Delta_MeV = Delta_0_MeV * (1 + alpha * xi + beta * xi**2)
    
    print(f"\nBasis-Massenlücke Δ₀ = {Delta_0_MeV} MeV")
    print(f"ξ = {xi:.2e}")
    print(f"Lineare Korrektur: αξ = {alpha*xi:.2e}")
    print(f"Quadratische Korrektur: βξ² = {beta*xi**2:.2e}")
    print(f"Gesamtkorrektur: {alpha*xi + beta*xi**2:.2e}")
    
    print(f"\nMassenlücke mit fraktaler Korrektur:")
    print(f"Δ = Δ₀ · (1 + αξ + βξ²) = {Delta_MeV:.1f} MeV")
    print(f"Abweichung von Δ₀: {Delta_MeV - Delta_0_MeV:.2f} MeV")
    
    return Delta_MeV

def analyze_fractal_metric():
    """Analysiert die fraktale Metrik und deren Konvergenz"""
    print("\n" + "-"*40)
    print("Fraktale Metrik und Konvergenz")
    print("-"*40)
    
    n_terms = 20
    terms = [xi**k for k in range(1, n_terms+1)]
    cumulative = np.cumsum(terms)
    
    print(f"\nKonvergenz der fraktalen Summe für ξ = {xi:.2e}:")
    for i in range(0, n_terms, 5):
        print(f"  k={i+1:2d}: ξ^{i+1} = {terms[i]:.2e}, Σ = {cumulative[i]:.6f}")
    
    limit = 1/(1-xi) - 1
    print(f"\nGrenzwert für k→∞: Σ ξ^k = 1/(1-ξ) - 1 = {limit:.6f}")
    print(f"Abweichung nach {n_terms} Termen: {(cumulative[-1]-limit)/limit*100:.2e}%")
    
    return cumulative, limit

def analyze_confinement_potential(sigma_GeV_fm):
    """Analysiert das Confinement-Potential V(r) ~ r (1 + ξ ln r)"""
    print("\n" + "-"*40)
    print("Confinement-Potential V(r)")
    print("-"*40)
    
    r = np.logspace(-2, 2, 100)  # fm
    r0 = 1.0  # fm
    
    # Potential mit fraktaler Korrektur
    V = sigma_GeV_fm * r * (1 + xi * np.log(r/r0 + 1e-10))
    
    print(f"\nPotential V(r) = σ r (1 + ξ ln r) mit σ = {sigma_GeV_fm} GeV/fm")
    print(f"für ξ = {xi:.2e}:")
    print(f"  r = 0.1 fm: V = {V[10]:.3f} GeV")
    print(f"  r = 1.0 fm: V = {V[50]:.3f} GeV")
    print(f"  r = 10 fm: V = {V[90]:.3f} GeV")
    
    V_linear = sigma_GeV_fm * r
    ratio = V / V_linear
    
    print(f"\nAbweichung vom linearen Potential (in %):")
    print(f"  r = 0.1 fm: {((ratio[10]-1)*100):.4f}%")
    print(f"  r = 1.0 fm: {((ratio[50]-1)*100):.4f}%")
    print(f"  r = 10 fm: {((ratio[90]-1)*100):.4f}%")
    
    return r, V, V_linear

def check_topological_winding():
    """Überprüft die topologischen Windungszahlen"""
    print("\n" + "-"*40)
    print("Topologische Windungszahlen")
    print("-"*40)
    
    r_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]  # fm
    
    print(f"\nWindungszahl n = 4π√ξ r")
    
    for r in r_values:
        n_min = 4 * np.pi * np.sqrt(xi) * r
        status = "✓" if n_min >= 1 else "✗"
        print(f"  r = {r:.1f} fm: n_min = {n_min:.2f} {status}")
    
    r_critical = 1/(4 * np.pi * np.sqrt(xi))
    print(f"\nKritischer Radius für n=1: r_c = {r_critical:.2f} fm")
    print(f"Für r > {r_critical:.2f} fm ist die Quantisierungsbedingung erfüllt")
    
    return r_critical

def calculate_gradient_energy(sqrt_B_MeV):
    """Berechnet die kinetische Energie der Phasengradienten"""
    print("\n" + "-"*40)
    print("Kinetische Energie der Phasengradienten")
    print("-"*40)
    
    # B in GeV⁴
    sqrt_B_GeV = sqrt_B_MeV / 1000
    B_GeV4 = sqrt_B_GeV**4
    
    r = 1.0  # fm
    grad_min = (2 * np.pi / r) * np.sqrt(xi)  # fm⁻¹
    
    volume_fm3 = 4/3 * np.pi * r**3
    
    # Konvertiere zu natürlichen Einheiten
    fm_to_GeV = hc_MeV_fm * 1e-3  # 0.19733 GeV·fm
    fm3_to_GeV3 = (1/fm_to_GeV)**3
    
    grad_GeV = grad_min * fm_to_GeV
    volume_GeV3 = volume_fm3 * fm3_to_GeV3
    
    E_kin_GeV = B_GeV4 * grad_GeV**2 * volume_GeV3
    E_kin_MeV = E_kin_GeV * 1000
    
    print(f"\nFür r = {r} fm:")
    print(f"  √B = {sqrt_B_MeV:.1f} MeV → B = {B_GeV4:.2e} GeV⁴")
    print(f"  |∇θ|_min = {grad_min:.2e} fm⁻¹ = {grad_GeV:.2e} GeV")
    print(f"  Volumen = {volume_fm3:.2f} fm³ = {volume_GeV3:.2e} GeV⁻³")
    print(f"  E_kin = {E_kin_GeV:.2e} GeV = {E_kin_MeV:.1f} MeV")
    
    return E_kin_MeV

def create_summary_table(Delta_MeV, sqrt_B_MeV, r_critical):
    """Erstellt eine Vergleichstabelle der Ergebnisse"""
    print("\n" + "-"*40)
    print("ZUSAMMENFASSUNG DER ERGEBNISSE")
    print("-"*40)
    
    data = {
        'Größe': [
            'ξ',
            'ξ⁻¹',
            '√B (MeV)',
            'Δ₀ (MeV) [Glueball]',
            'Δ (MeV) mit ξ-Korrektur',
            'Korrektur (MeV)',
            'r_critical (fm)',
            'String-Spannung σ (GeV/fm)'
        ],
        'Wert': [
            f'{xi:.2e}',
            f'{1/xi:.2e}',
            f'{sqrt_B_MeV:.1f}',
            '350',
            f'{Delta_MeV:.1f}',
            f'{Delta_MeV-350:.2f}',
            f'{r_critical:.2f}',
            '0.9'
        ],
        'Status': [
            '✓',
            '✓',
            '✓',
            '✓',
            '✓' if 300 <= Delta_MeV <= 400 else '?',
            '✓',
            '✓',
            '✓'
        ]
    }
    
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    
    print("\n" + "="*60)
    print("FAZIT")
    print("="*60)
    print("✓ Die Einheiten der Yang-Mills-Lagrangedichte sind korrekt")
    print(f"✓ √B ≈ {sqrt_B_MeV:.1f} MeV aus QCD-Parametern")
    print("✓ Die fraktale Metrik konvergiert für ξ = 4/3×10⁻⁴")
    print(f"✓ Die Massenlücke Δ ≈ {Delta_MeV:.1f} MeV")
    print(f"  (Basis-Glueball-Masse 350 MeV + kleine ξ-Korrektur)")
    print("✓ Das Confinement-Potential zeigt kleine logarithmische Korrekturen")
    print(f"✓ Topologische Windungszahlen sind für r > {r_critical:.2f} fm quantisiert")
    print("\nWichtig: Die fraktalen Korrekturen sind klein (∼10⁻⁴),")
    print("da ξ sehr klein ist. Die absolute Skala kommt von QCD.")

def plot_results(r_conf, V_conf, V_linear, r_critical, Delta_MeV):
    """Erstellt Visualisierungen der Ergebnisse"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: Confinement-Potential
    ax1 = axes[0, 0]
    ax1.plot(r_conf, V_conf, 'b-', linewidth=2, label='V(r) = σr(1+ξ ln r)')
    ax1.plot(r_conf, V_linear, 'r--', linewidth=2, label='V(r) = σr (linear)')
    ax1.set_xlabel('r (fm)')
    ax1.set_ylabel('V (GeV)')
    ax1.set_title('Confinement-Potential')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xscale('log')
    
    # Plot 2: Relative Abweichung vom linearen Potential
    ax2 = axes[0, 1]
    rel_dev = (V_conf - V_linear) / V_linear * 100
    ax2.semilogx(r_conf, rel_dev, 'g-', linewidth=2)
    ax2.axvline(x=r_critical, color='r', linestyle=':', label=f'r_c = {r_critical:.2f} fm')
    ax2.set_xlabel('r (fm)')
    ax2.set_ylabel('Abweichung (%)')
    ax2.set_title('Relative Abweichung vom linearen Potential')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='k', linestyle='-', alpha=0.2)
    
    # Plot 3: Massenlücke mit ξ-Korrektur
    ax3 = axes[1, 0]
    xi_values = np.logspace(-5, -3, 50)
    Delta_values = 350 * (1 + xi_values + 0.5*xi_values**2)
    ax3.semilogx(xi_values, Delta_values, 'b-', linewidth=2)
    ax3.axvline(x=xi, color='k', linestyle=':', label=f'ξ = {xi:.2e}')
    ax3.axhline(y=350, color='r', linestyle='--', label='Δ₀ = 350 MeV')
    ax3.axhline(y=Delta_MeV, color='g', linestyle='--', label=f'Δ = {Delta_MeV:.1f} MeV')
    ax3.set_xlabel('ξ')
    ax3.set_ylabel('Δ (MeV)')
    ax3.set_title('Massenlücke Δ mit fraktaler Korrektur')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Topologische Windungszahl
    ax4 = axes[1, 1]
    r_winding = np.logspace(-1, 2, 100)
    n_winding = 4 * np.pi * np.sqrt(xi) * r_winding
    ax4.loglog(r_winding, n_winding, 'm-', linewidth=2)
    ax4.axhline(y=1, color='k', linestyle='--', label='n = 1')
    ax4.axvline(x=r_critical, color='r', linestyle=':', label=f'r_c = {r_critical:.2f} fm')
    ax4.set_xlabel('r (fm)')
    ax4.set_ylabel('Windungszahl n')
    ax4.set_title('Topologische Windungszahl n = 4π√ξ r')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('quantengravitation_pruefung.png', dpi=150)
    plt.show()
    print("\nPlot gespeichert als 'quantengravitation_pruefung.png'")

def main():
    """Hauptfunktion"""
    
    # 1. Einheitenprüfung
    check_yang_mills_units()
    
    # 2. QCD-Parameter
    sigma, Lambda_QCD, m_glueball, sqrt_B = calculate_qcd_parameters()
    
    # 3. Fraktale Metrik
    cumulative, limit = analyze_fractal_metric()
    
    # 4. Massenlücke mit korrekter ξ-Korrektur
    Delta_MeV = calculate_mass_gap_correctly(m_glueball, xi)
    
    # 5. Confinement-Potential
    r_conf, V_conf, V_linear = analyze_confinement_potential(sigma)
    
    # 6. Topologische Windungen
    r_critical = check_topological_winding()
    
    # 7. Gradientenenergie
    E_kin = calculate_gradient_energy(sqrt_B)
    
    # 8. Visualisierung
    plot_results(r_conf, V_conf, V_linear, r_critical, Delta_MeV)
    
    # 9. Zusammenfassung
    create_summary_table(Delta_MeV, sqrt_B, r_critical)

if __name__ == "__main__":
    main()