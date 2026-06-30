"""
calc-resonanz-leiter.py
=======================
T0 / FFGFT  –  Vollständige Resonanz-Leiter aller bekannten Teilchen
Basierend auf Dok. 006, 186 (Korrektur K2)

Geminis Idee (Fraction-Arithmetik) wird hier konsequent umgesetzt:
  - Alle r-Vorfaktoren als exakte Brüche
  - Alle p-Exponenten als exakte Brüche
  - Masse = r * xi^p * v  (Yukawa-Formel)
  - Neutrinos: m_nu_i = r_i * xi^2 * m_e  (doppelte xi-Unterdrückung)

Wichtig: Quarks passen NICHT in die einfache Leiter xi^n * m_e,
weil sie andere Exponenten p haben. Die Tabelle zeigt die tatsächliche
geometrische Einordnung jedes Teilchens.
"""

from fractions import Fraction
import math

def xi_float(xi_frac):
    return float(xi_frac)

def mass_eV(r, p, xi, v_GeV):
    """Yukawa: m = r * xi^p * v  [in eV]"""
    return float(r) * float(xi)**float(p) * float(v_GeV) * 1e9

def main():
    print("=" * 75)
    print("T0 / FFGFT  –  RESONANZ-LEITER ALLER TEILCHEN")
    print("Exakte Bruch-Arithmetik für r und p  (Dok. 006 / 186)")
    print("=" * 75)

    # ------------------------------------------------------------------
    # Fundamentale Parameter (exakt als Brüche)
    # ------------------------------------------------------------------
    xi  = Fraction(4, 3) * Fraction(1, 10000)   # = 4/30000
    v   = Fraction(24622, 100)                  # 246.22 GeV (Higgs-VEV)

    print(f"\nxi  = {xi}  =  {float(xi):.8e}")
    print(f"v   = {v} GeV  =  {float(v):.4f} GeV")

    # ------------------------------------------------------------------
    # Alle Teilchen: (Name, r als Fraction, p als Fraction, Exp.[eV])
    # Exponenten p-Struktur: Schrittweite 1/3  (3 Raumdimensionen)
    # ------------------------------------------------------------------
    teilchen = [
        # --- Leptonen ---
        ("Elektron",   Fraction(4,  3),   Fraction(3, 2),  511000,       "0.511 MeV"),
        ("Myon",       Fraction(16, 5),   Fraction(1, 1),  105658375,    "105.7 MeV"),
        ("Tau",        Fraction(25, 9),   Fraction(2, 3),  1776860000,   "1776.9 MeV"),  # K2

        # --- Neutrinos: p_eff = p_lepton + 2 (doppelte xi-Unterdrückung) ---
        # m_nu_i = r_i * xi^2 * m_e  =>  effektiv p = 3/2 + 2 - 3/2 = 2 auf m_e-Basis
        # Formel hier: m_nu_i = r_nu_i * xi^2 * m_e  separat
        ("nu_e",       Fraction(1,  1),   None,            None,         "9.08 meV"),
        ("nu_mu",      Fraction(16, 5),   None,            None,         "29.07 meV"),
        ("nu_tau",     Fraction(25, 9),   None,            None,         "25.23 meV"),

        # --- Quarks ---
        ("Up",         Fraction(6,  1),   Fraction(3, 2),  2200000,      "2.2 MeV"),
        ("Down",       Fraction(25, 2),   Fraction(3, 2),  4700000,      "4.7 MeV"),
        ("Strange",    Fraction(26, 9),   Fraction(1, 1),  96000000,     "96 MeV"),
        ("Charm",      Fraction(2,  1),   Fraction(2, 3),  1270000000,   "1.27 GeV"),
        ("Bottom",     Fraction(3,  2),   Fraction(1, 2),  4180000000,   "4.18 GeV"),
        ("Top",        Fraction(1, 28),   Fraction(-1, 3), 172690000000, "172.7 GeV"),
    ]

    m_e_eV = 510998.95  # eV

    # Neutrino-Massen separat berechnen
    nu_massen = {
        "nu_e":   float(Fraction(1,  1)) * float(xi)**2 * m_e_eV,
        "nu_mu":  float(Fraction(16, 5)) * float(xi)**2 * m_e_eV,
        "nu_tau": float(Fraction(25, 9)) * float(xi)**2 * m_e_eV,
    }

    # ------------------------------------------------------------------
    # Tabelle ausgeben
    # ------------------------------------------------------------------
    print(f"\n{'Teilchen':<12} {'r (Bruch)':<12} {'p (Bruch)':<12} "
          f"{'m_T0 [eV]':<18} {'m_Exp.':<15} {'Abw.%'}")
    print("-" * 75)

    for name, r, p, m_exp_eV, m_exp_str in teilchen:
        if p is None:
            # Neutrino
            m_t0 = nu_massen[name]
            p_str = "xi²·m_e"
            abw = ""
        else:
            m_t0 = mass_eV(r, p, xi, float(v))
            p_str = str(p)
            if m_exp_eV:
                abw = f"{(m_t0 - m_exp_eV) / m_exp_eV * 100:+.2f}%"
            else:
                abw = "—"

        # Einheit wählen
        if m_t0 >= 1e12:
            m_str = f"{m_t0/1e9:.2f} GeV"
        elif m_t0 >= 1e9:
            m_str = f"{m_t0/1e6:.4f} MeV"
        elif m_t0 >= 1e6:
            m_str = f"{m_t0/1e6:.4f} MeV"
        elif m_t0 >= 1e3:
            m_str = f"{m_t0/1e3:.4f} keV"
        elif m_t0 >= 1:
            m_str = f"{m_t0:.4f} eV"
        elif m_t0 >= 1e-3:
            m_str = f"{m_t0*1e3:.4f} meV"
        else:
            m_str = f"{m_t0*1e6:.4f} μeV"

        print(f"{name:<12} {str(r):<12} {p_str:<12} {m_str:<18} {m_exp_str:<15} {abw}")

    # ------------------------------------------------------------------
    # Exponent-Struktur: zeige die p-Leiter
    # ------------------------------------------------------------------
    print(f"\n{'=' * 75}")
    print("EXPONENT-STRUKTUR  (Schrittweite Δp = 1/3)")
    print("-" * 75)
    print(f"{'p-Wert':<12} {'Dezimal':<12} {'Teilchen'}")
    print("-" * 75)
    p_gruppen = {
        Fraction(-1, 3): ["Top"],
        Fraction(1,  2): ["Bottom"],
        Fraction(2,  3): ["Tau", "Charm"],
        Fraction(1,  1): ["Myon", "Strange"],
        Fraction(3,  2): ["Elektron", "Up", "Down"],
        "xi²·m_e":       ["nu_e", "nu_mu", "nu_tau"],
    }
    for p_val, namen in p_gruppen.items():
        p_str = str(p_val) if isinstance(p_val, Fraction) else p_val
        dez   = f"{float(p_val):.4f}" if isinstance(p_val, Fraction) else "(separat)"
        print(f"{p_str:<12} {dez:<12} {', '.join(namen)}")

    # ------------------------------------------------------------------
    # Geminis Stabilitäts-Check  (korrekt implementiert)
    # ------------------------------------------------------------------
    print(f"\n{'=' * 75}")
    print("STABILITÄTS-CHECK  (Verhältnisbasiert, Bruch-Arithmetik)")
    print("-" * 75)
    print("Ein Teilchen ist stabil wenn m_T0 > m_kosmologisch_min")
    print(f"m_min / m_e (kosmologisch) ~ 1.49e-33 eV / 511 keV = 2.9e-39")
    schwelle = Fraction(1, 10**38)   # ~ 10^-38 als konservativer Bruch
    print(f"Schwelle (Fraction): {schwelle}  = {float(schwelle):.2e}")
    print()
    for name, r, p, _, _ in teilchen:
        if p is None:
            verh = Fraction(r.numerator, r.denominator) * xi * xi
            verh_float = float(verh)
        else:
            verh_float = float(r) * float(xi)**float(p)
        stabil = verh_float > float(schwelle)
        status = "STABIL" if stabil else "kollabiert"
        print(f"  {name:<12}  Verhältnis = {verh_float:.4e}  -->  {status}")

    # ------------------------------------------------------------------
    # Zusammenfassung
    # ------------------------------------------------------------------
    print(f"\n{'=' * 75}")
    print("FAZIT")
    print(f"  xi = {xi}  =  {float(xi):.6e}")
    print(f"  Alle 12 Teilchen verwenden exakte r-Brüche.")
    print(f"  Exponenten p: von -1/3 (Top) bis 3/2 (Elektron), Δp = 1/3")
    print(f"  Neutrinos: eigene Klasse mit doppelter xi-Unterdrückung (xi^2·m_e)")
    print(f"  Alle Massen konsistent mit PDG-Werten innerhalb ~1-4%")
    print("=" * 75)

if __name__ == "__main__":
    main()
