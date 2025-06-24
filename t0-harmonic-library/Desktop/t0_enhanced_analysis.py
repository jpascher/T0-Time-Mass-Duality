#!/usr/bin/env python3
"""
T0-Model Test: Enhanced Analysis with proper interpretation
==========================================================

Fixed analysis that properly handles Planck data formats:
- CMB maps are differential (fluctuations around mean)
- Raw frequency maps contain the monopole component
- Need proper spectral analysis for T0 test
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import urllib.request
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Frequencies to analyze (GHz)
FREQUENCIES = [30, 100, 143, 217]

# Expected T0 temperatures (K) - theoretical prediction
T0_PREDICTED = {
    30: 1.8,
    100: 2.5,
    143: 3.1, 
    217: 4.1
}

# Standard CMB temperature
T_CMB_STANDARD = 2.7255

def download_simple(url, cache_dir="planck_cache"):
    """Simple download with urllib."""
    Path(cache_dir).mkdir(exist_ok=True)
    
    filename = url.split('/')[-1]
    cache_path = Path(cache_dir) / filename
    
    if cache_path.exists():
        print(f"✓ Using cached {filename}")
        return str(cache_path)
    
    try:
        print(f"📥 Downloading {filename}...")
        urllib.request.urlretrieve(url, cache_path)
        print(f"✓ Downloaded {filename}")
        return str(cache_path)
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
        return None

def analyze_cmb_fluctuations(fits_path):
    """Analyze CMB temperature fluctuations properly."""
    try:
        with fits.open(fits_path) as hdul:
            print(f"📁 Analyzing: {Path(fits_path).name}")
            
            # Get primary data
            data = hdul[1].data
            header = hdul[1].header
            
            print(f"   Header info: {header.get('EXTNAME', 'N/A')}")
            print(f"   Data columns: {data.names if hasattr(data, 'names') else 'Image data'}")
            
            # Extract temperature data
            if hasattr(data, 'names'):
                # HEALPix table format
                if 'I_STOKES' in data.names:
                    temp_fluctuations = data['I_STOKES']
                elif 'TEMPERATURE' in data.names:
                    temp_fluctuations = data['TEMPERATURE']
                else:
                    temp_fluctuations = data.field(0)
            else:
                # Image format
                temp_fluctuations = data
            
            # Convert to array and analyze
            temp_fluctuations = np.array(temp_fluctuations)
            
            # Remove bad pixels
            valid_mask = np.isfinite(temp_fluctuations) & (np.abs(temp_fluctuations) < 1)
            valid_temps = temp_fluctuations[valid_mask]
            
            # Statistics
            results = {
                'mean_fluctuation': np.mean(valid_temps),
                'rms_fluctuation': np.sqrt(np.mean(valid_temps**2)),
                'std_fluctuation': np.std(valid_temps),
                'min_fluctuation': np.min(valid_temps),
                'max_fluctuation': np.max(valid_temps),
                'n_valid': len(valid_temps)
            }
            
            # Proper interpretation
            print(f"   Mean fluctuation: {results['mean_fluctuation']:.6f} K")
            print(f"   RMS fluctuation: {results['rms_fluctuation']:.6f} K")
            print(f"   Min/Max: {results['min_fluctuation']:.6f} / {results['max_fluctuation']:.6f} K")
            
            return results
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def theoretical_t0_analysis():
    """
    Theoretical analysis of what T0 signature would look like
    in frequency-dependent measurements.
    """
    
    print("\n🔬 THEORETICAL T0 ANALYSIS")
    print("-" * 50)
    
    frequencies = np.array(FREQUENCIES)
    
    # Standard model prediction
    T_standard = np.full_like(frequencies, T_CMB_STANDARD, dtype=float)
    
    # T0 model prediction  
    T_t0 = np.array([T0_PREDICTED[f] for f in frequencies])
    
    # Calculate differences
    delta_T = T_t0 - T_standard
    relative_change = (T_t0 - T_standard) / T_standard * 100
    
    print(f"{'Freq (GHz)':<10} {'Standard':<10} {'T0 Model':<10} {'ΔT (K)':<10} {'Δ%':<8}")
    print("-" * 50)
    for i, freq in enumerate(frequencies):
        print(f"{freq:<10} {T_standard[i]:<10.4f} {T_t0[i]:<10.1f} "
              f"{delta_T[i]:<10.4f} {relative_change[i]:<8.1f}%")
    
    # Key statistics
    max_deviation = np.max(np.abs(delta_T))
    frequency_slope = np.polyfit(frequencies, T_t0, 1)[0]
    
    print(f"\n📊 T0 Model Signatures:")
    print(f"   Maximum deviation: {max_deviation:.4f} K")
    print(f"   Frequency slope: {frequency_slope:.6f} K/GHz")
    print(f"   Total range: {np.max(T_t0) - np.min(T_t0):.2f} K")
    print(f"   Relative effect: {max_deviation/T_CMB_STANDARD*100:.2f}%")
    
    # Visualization
    plt.figure(figsize=(12, 8))
    
    # Main comparison plot
    plt.subplot(2, 1, 1)
    plt.plot(frequencies, T_standard, 'bo-', label='Standard Model', markersize=8, linewidth=2)
    plt.plot(frequencies, T_t0, 'ro-', label='T0 Model', markersize=8, linewidth=2)
    plt.axhline(y=T_CMB_STANDARD, color='gray', linestyle='--', alpha=0.5)
    plt.ylabel('Temperature (K)', fontsize=12)
    plt.title('T0 Model: Frequency-Dependent CMB Temperature', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Difference plot
    plt.subplot(2, 1, 2)
    plt.plot(frequencies, delta_T, 'go-', label='T0 - Standard', markersize=8, linewidth=2)
    plt.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    plt.xlabel('Frequency (GHz)', fontsize=12)
    plt.ylabel('ΔT (K)', fontsize=12)
    plt.title('Temperature Difference: T0 Model - Standard Model', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return T_standard, T_t0, delta_T

def spectral_analysis_concept():
    """
    Demonstrate the concept of spectral analysis needed for T0 test.
    """
    print("\n🌈 SPECTRAL ANALYSIS CONCEPT")
    print("-" * 40)
    
    # Frequency range
    nu = np.linspace(10, 1000, 100)  # GHz
    
    # Planck function for different temperatures
    h = 6.626e-34  # Planck constant
    c = 3e8        # Speed of light  
    k = 1.381e-23  # Boltzmann constant
    
    def planck_intensity(nu_ghz, T):
        """Planck intensity (arbitrary units)."""
        nu_hz = nu_ghz * 1e9
        x = h * nu_hz / (k * T)
        return (2 * h * nu_hz**3 / c**2) / (np.exp(x) - 1)
    
    # Standard CMB spectrum
    I_standard = planck_intensity(nu, T_CMB_STANDARD)
    
    # T0 spectra for different frequencies
    plt.figure(figsize=(12, 6))
    
    colors = ['blue', 'green', 'orange', 'red']
    for i, freq in enumerate(FREQUENCIES):
        T_t0 = T0_PREDICTED[freq]
        I_t0 = planck_intensity(nu, T_t0)
        plt.plot(nu, I_t0, color=colors[i], linestyle='--', 
                label=f'T0: {freq} GHz region → T={T_t0} K', alpha=0.7)
    
    plt.plot(nu, I_standard, 'k-', linewidth=2, label=f'Standard: T={T_CMB_STANDARD} K')
    
    # Mark observation frequencies
    for freq in FREQUENCIES:
        plt.axvline(x=freq, color='gray', linestyle=':', alpha=0.5)
        plt.text(freq, plt.ylim()[1]*0.9, f'{freq}', rotation=90, ha='right')
    
    plt.xlabel('Frequency (GHz)', fontsize=12)
    plt.ylabel('Intensity (arbitrary units)', fontsize=12)
    plt.title('Theoretical Spectra: Standard vs T0 Model', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.xlim(20, 400)
    
    plt.tight_layout()
    plt.show()
    
    print("💡 Key insight: T0 model predicts different Planck temperatures")
    print("   at different frequencies, not a single 2.7255 K blackbody!")

def main():
    """Enhanced main analysis."""
    print("=" * 60)
    print("T0-MODEL TEST: ENHANCED ANALYSIS")
    print("=" * 60)
    print("Understanding: CMB maps are differential, need proper interpretation")
    print()
    
    # 1. Theoretical analysis
    print("🚀 PHASE 1: Theoretical T0 Analysis")
    T_standard, T_t0, delta_T = theoretical_t0_analysis()
    
    # 2. Spectral concept
    print("\n🚀 PHASE 2: Spectral Analysis Concept")
    spectral_analysis_concept()
    
    # 3. Real data interpretation (if available)
    cmb_file = "planck_cache/COM_CMB_IQU-commander_2048_R3.00_full.fits"
    if Path(cmb_file).exists():
        print("\n🚀 PHASE 3: Real CMB Data Analysis")
        cmb_results = analyze_cmb_fluctuations(cmb_file)
        
        if cmb_results:
            print(f"\n📊 CMB Fluctuation Analysis:")
            print(f"   RMS fluctuation: {cmb_results['rms_fluctuation']:.6f} K")
            print(f"   Standard ΔT/T: ~1.11e-5 (theory)")
            print(f"   Measured ΔT/T: {cmb_results['rms_fluctuation']/T_CMB_STANDARD:.2e}")
            
            # Compare with T0 prediction
            expected_rms = 1.11e-5 * T_CMB_STANDARD
            print(f"   Expected RMS: {expected_rms:.6f} K")
            print(f"   Ratio: {cmb_results['rms_fluctuation']/expected_rms:.2f}")
    
    # Summary
    print(f"\n{'='*60}")
    print("ENHANCED ANALYSIS SUMMARY")
    print(f"{'='*60}")
    
    print("✅ Theoretical T0 signature clearly defined:")
    print(f"   - Frequency-dependent temperature: {np.min(T_t0):.1f}K to {np.max(T_t0):.1f}K")
    print(f"   - Maximum deviation: {np.max(np.abs(delta_T)):.2f}K from standard")
    print(f"   - Relative effect: {np.max(np.abs(delta_T))/T_CMB_STANDARD*100:.1f}%")
    
    print("\n🔬 To test T0 model experimentally:")
    print("   1. Multi-frequency intensity measurement")
    print("   2. Fit temperature per frequency (avoid global Planck fit)")
    print("   3. Look for systematic T(ν) trend vs constant 2.7255K")
    print("   4. Statistical significance: >5σ needed for discovery")
    
    print("\n💫 STATUS: T0 model is theoretically testable!")
    print("   The signature is clear, measurable, and distinctive.")
    
    return T_standard, T_t0, delta_T

if __name__ == "__main__":
    results = main()
    print("\n🎯 Next step: Access raw Planck frequency maps for direct test!")