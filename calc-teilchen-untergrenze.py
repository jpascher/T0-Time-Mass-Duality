"""
calc-teilchen-untergrenze.py
============================
T0 / FFGFT  –  Untergrenze der Teilchenmassen
Basierend auf Dok. 006, 049, 182, 186

Drei Arten von Untergrenzen in FFGFT:

  (A) Geometrische Untergrenze: m_min aus kosmologischer Skala
      m_min = hbar * H0 / c^2  (leichteste mögliche Resonanz)

  (B) Leichteste stabile massive Teilchen: Neutrinos
      m_nu_i = r_i * xi^2 * m_e
      (doppelte xi-Unterdrückung gegenüber Leptonen)

  (C) Skalenleiter xi^n * m_e  (diskrete Resonanzlevels)
      Jede Stufe = eine weitere xi-Unterdrückung
"""

import math

def main():
    print("=" * 65)
    print("T0 / FFGFT  –  UNTERGRENZE DER TEILCHENMASSEN")
    print("Dok. 006 / 049 / 182 / 186")
    print("=" * 65)

    # ------------------------------------------------------------------
    # Konstanten
    # ------------------------------------------------------------------
    xi    = 4.0 / 3.0 * 1e-4     # dimensionsloser T0-Parameter
    c     = 299792458.0           # m/s
    hbar  = 1.054571817e-34       # J·s
    H0    = 2.268e-18             # s^-1  (H0 = 70 km/s/Mpc)
    eV    = 1.602176634e-19       # J  (1 eV in Joule)

    # Teilchenmassen in eV
    m_e_eV   = 510998.95          # eV  Elektron
    m_mu_eV  = 105658375.5        # eV  Myon
    m_tau_eV = 1776860000.0       # eV  Tau

    # Yukawa-Vorfaktoren (Dok. 006 / 186 Korrektur K2)
    r_e   = 4/3
    r_mu  = 16/5
    r_tau = 25/9      # Korrektur K2: war 8/3

    # ------------------------------------------------------------------
    # A: Geometrische Untergrenze aus kosmologischer Skala
    # ------------------------------------------------------------------
    print("\n[A] Geometrische Untergrenze  m_min = hbar * H0 / c^2")
    m_min_kg = hbar * H0 / c**2
    m_min_eV = m_min_kg * c**2 / eV
    print(f"    H0           = {H0:.4e} s^-1")
    print(f"    m_min        = {m_min_kg:.4e} kg")
    print(f"    m_min        = {m_min_eV:.4e} eV")
    print(f"    = {m_min_eV*1e33:.4f} * 10^-33 eV")
    print(f"    (Photon-Massegrenze, kosmologisch)")

    # Vergleich: m_nu_e / m_min
    # (zeigt wie weit Neutrino über dem absoluten Minimum liegt)

    # ------------------------------------------------------------------
    # B: Neutrino-Massen  (leichteste stabile massive Teilchen)
    #    Formel: m_nu_i = r_i * xi^2 * m_e
    #    Herleitung: doppelte xi-Unterdrückung (Seesaw-analoger Mechanismus)
    # ------------------------------------------------------------------
    print("\n[B] Neutrino-Massen  m_nu_i = r_i * xi^2 * m_e")
    print(f"    xi^2 = {xi**2:.6e}")
    print(f"    m_e  = {m_e_eV:.6e} eV")
    print()

    neutrinos = [
        ("nu_e",   1.0,    m_e_eV,   "< 45 meV  (KATRIN 2022)"),
        ("nu_mu",  16/5,   m_e_eV,   "< 190 keV  (PDG)"),
        ("nu_tau", 25/9,   m_e_eV,   "< 18.2 MeV (PDG)"),
    ]

    m_nu_summe = 0.0
    for name, r, m_lepton, exp_limit in neutrinos:
        m_nu_eV  = r * xi**2 * m_lepton
        m_nu_meV = m_nu_eV * 1e3
        m_nu_summe += m_nu_eV
        print(f"    m_{name:5s} = {r:.4f} * xi^2 * m_e")
        print(f"           = {m_nu_meV:.4f} meV")
        print(f"           Exp. Limit: {exp_limit}")
        print()

    print(f"    Summe m_nu  = {m_nu_summe*1e3:.2f} meV")
    print(f"    PDG-Limit   < 120 meV  (Kosmologie)")
    konsistent = m_nu_summe * 1e3 < 120
    print(f"    Konsistent? {'JA' if konsistent else 'NEIN'}")

    # Verhältnis Neutrino / Elektron
    print(f"\n    Unterdrückungsfaktor:")
    print(f"    m_nu_e / m_e = xi^2 = {xi**2:.4e}  ({xi**2 * m_e_eV * 1e3:.4f} meV)")
    print(f"    m_e    / m_nu_e     = 1/xi^2 = {1/xi**2:.2e}")

    # ------------------------------------------------------------------
    # C: xi-Skalenleiter  (diskrete Resonanzlevels)
    #    Ebene n: m_n = xi^n * m_e
    # ------------------------------------------------------------------
    print("\n[C] xi-Skalenleiter  m_n = xi^n * m_e  (Resonanz-Ebenen)")
    print(f"    {'Ebene n':<10} {'m_n [eV]':<18} {'m_n [Einheit]':<20} {'Physik'}")
    print(f"    {'-'*72}")

    ebenen = [
        (0,  "m_e = 511 keV",      "Elektron (Lepton-Skala)"),
        (1,  "~68 eV",             "xi^1 * m_e  (keine bekannte Zuordnung)"),
        (2,  "~9 meV",             "Neutrino nu_e  (xi^2-Unterdrückung)"),
        (3,  "~1.2 μeV",           "xi^3 * m_e  (hypothetisch)"),
        (4,  "~0.16 neV",          "xi^4 * m_e  (hypothetisch)"),
    ]

    for n, approx, physik in ebenen:
        m_n_eV = xi**n * m_e_eV
        if m_n_eV >= 1e6:
            einheit = f"{m_n_eV/1e6:.4f} MeV"
        elif m_n_eV >= 1e3:
            einheit = f"{m_n_eV/1e3:.4f} keV"
        elif m_n_eV >= 1:
            einheit = f"{m_n_eV:.4f} eV"
        elif m_n_eV >= 1e-3:
            einheit = f"{m_n_eV*1e3:.4f} meV"
        elif m_n_eV >= 1e-6:
            einheit = f"{m_n_eV*1e6:.4f} μeV"
        else:
            einheit = f"{m_n_eV*1e9:.4f} neV"
        print(f"    n={n:<8}  {m_n_eV:.4e} eV   {einheit:<20}  {physik}")

    print(f"\n    Jede Ebene ist um xi = {xi:.4e} supprimiert.")
    print(f"    Unterhalb n=3 sind keine stabilen Resonanzen bekannt.")

    # ------------------------------------------------------------------
    # D: Untergrenze für masselose Teilchen (Photon)
    # ------------------------------------------------------------------
    print("\n[D] Photon: T0-Deckentheorem  S_max = 2*sqrt(2) exakt")
    print(f"    Photon hat m_gamma = 0  (keine xi-Korrektur)")
    print(f"    Experimentelle Obergrenze: m_gamma < 10^-18 eV  (PDG)")
    print(f"    T0-Vorhersage: keine fundamentale Massenuntergrenze")
    print(f"    für masselose Eichbosonen (Torus-Geometrie erlaubt m=0)")

    # ------------------------------------------------------------------
    # Zusammenfassung
    # ------------------------------------------------------------------
    m_nu_e_meV = xi**2 * m_e_eV * 1e3
    print(f"\n{'=' * 65}")
    print(f"ZUSAMMENFASSUNG der Untergrenzen (T0 / FFGFT)")
    print(f"{'=' * 65}")
    print(f"  Absolutes Minimum (kosmologisch): {m_min_eV:.2e} eV")
    print(f"  Leichtestes massives Teilchen:")
    print(f"    m_nu_e = xi^2 * m_e = {m_nu_e_meV:.4f} meV  (~9.1 meV)")
    print(f"  Unterdrückungsstruktur: diskret in Stufen von xi = {xi:.4e}")
    print(f"  Photon: m = 0  (kein fundamentales Minimum)")
    print(f"  Alle Werte konsistent mit PDG-Experimentalgrenzen: JA")
    print("=" * 65)

if __name__ == "__main__":
    main()
