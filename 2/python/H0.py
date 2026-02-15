#!/usr/bin/env python3
"""
H0 in der T0-Theorie: Schritt-fuer-Schritt-Herleitung
======================================================

H0 ist dreimal dasselbe (Strecke/Zeit/Frequenz).
E_H = hbar * H0 ist eine NEUE Groesse (Energie).
T0 berechnet E_H aus xi und E0.
"""
from scipy import constants
from fractions import Fraction
import numpy as np

# === Konstanten ===
XI = (4/3) * 1e-4               # T0-Parameter (dimensionslos)
E0_eV = 7.398e6                  # T0 charakt. Energie [eV]
hbar = constants.hbar             # J*s
eV = constants.eV                # J/eV
Lj_km = 9.461e12                 # 1 Lichtjahr [km]
Mpc_Lj = 3.26e6                  # 1 Megaparsec [Lichtjahre]
Mpc_km = Mpc_Lj * Lj_km          # 1 Mpc [km]
Mpc_m = Mpc_km * 1000            # 1 Mpc [m]

S = lambda t: print(f"\n{'='*70}\n  {t}\n{'='*70}")
U = lambda t: print(f"\n  {'-'*60}\n  {t}\n  {'-'*60}")

S("H0 IN DER T0-THEORIE")

# =================================================================
S("TEIL 1: Was misst H0 in T0?")
# =================================================================

print("""
  In T0 gibt es keine Expansion des Raumes.
  Ein Photon verliert Energie an die fraktale xi-Feld-Kruemmung:

    dE/E = -xi * dx    (relativer Verlust pro dimensionslose Distanz)

  Ein Beobachter misst: weiter entfernt = staerker rotverschoben.
  Er nennt diese Proportionalitaet 'H0'.
  H0 ist ein Verhaeltniswert: Rotverschiebung proportional zur Distanz.
  Es ist die Daempfungskonstante des xi-Feldes in SI-Einheiten.""")

# =================================================================
S("TEIL 2: H0 in drei SI-Darstellungen (alles DASSELBE)")
# =================================================================

print(f"""
  H0 kann in verschiedenen SI-Einheiten angegeben werden.
  Das sind KEINE verschiedenen Groessen -- nur verschiedene
  Strecken- bzw. Zeiteinheiten fuer denselben Verhaeltniswert.

  Basisumrechnungen:
    1 Parsec     = 3.26 Lichtjahre
    1 Mpc        = 10^6 Parsec = 3.26 Mio Lichtjahre
    1 Lichtjahr  = {Lj_km:.3e} km
    1 Mpc        = {Mpc_km:.4e} km = {Mpc_m:.4e} m""")

for name, H0_val in [("Planck 2018", 67.4), ("SH0ES 2022", 73.04)]:
    U(f"{name}: H0 = {H0_val} km/s/Mpc")

    # km/s/Mpc -> km/s/Lj
    H0_Lj = H0_val / Mpc_Lj
    # km/s/Lj -> m/s/m = s^-1
    H0_s = H0_Lj * 1000 / (Lj_km * 1000)

    print(f"""
    1) Messkonvention:  H0 = {H0_val} km/s/Mpc

    2) Mpc -> Lichtjahre (1 Mpc = {Mpc_Lj:.2e} Lj):
       H0 = {H0_val} / {Mpc_Lj:.2e}
          = {H0_Lj:.4e} km/s/Lj

    3) km -> m, Lj -> m (1 Lj = {Lj_km:.3e} km):
       H0 = {H0_Lj:.4e} * 1000 / ({Lj_km:.3e} * 1000)
          = {H0_s:.4e} m/s/m
          = {H0_s:.4e} s^-1   (m kuerzt sich!)

    +------------------+-----------------------------------+-----------------+
    | Einheit          | Formel                            | Wert            |
    +------------------+-----------------------------------+-----------------+
    | km/s/Mpc         | (Messung)                         | {H0_val:15.2f} |
    | km/s/Lj          | = H0 / {Mpc_Lj:.2e}               | {H0_Lj:15.4e} |
    | s^-1             | = H0 * 1000 / {Mpc_Lj:.2e} /      |                 |
    |                  |   {Lj_km:.3e} / 1000             | {H0_s:15.4e} |
    +------------------+-----------------------------------+-----------------+
    Alle drei Zeilen sind H0. Strecke, Strecke, Frequenz.""")

# =================================================================
S("TEIL 3: E_H -- eine NEUE Groesse (Hubble-Energie)")
# =================================================================

print("""
  H0 [s^-1] ist eine Frequenz (SI).
  In natuerlichen Einheiten (hbar = 1) ist Frequenz = Energie.

  Umrechnung SI -> nat. Einheiten: mit hbar MULTIPLIZIEREN
    E_H = hbar * H0[s^-1]     (SI -> nat: * hbar)

  Umrechnung nat. Einheiten -> SI: durch hbar DIVIDIEREN
    H0[s^-1] = E_H / hbar     (nat -> SI: / hbar)

  E_H ist eine NEUE Groesse (Energie), nicht mehr H0 (Frequenz).
  hbar ist der Umrechnungsfaktor -- in nat. Einheiten ist hbar = 1,
  dort sind E_H und H0 numerisch identisch.

  Analog:
    E = hbar * nu  (jede Frequenz -> Energie, Planck/Einstein)
    H0 [s^-1]  ->  E_H [eV]  (derselbe Schritt)""")

print("\n  SI -> nat. Einheiten (E_H = hbar * H0):")
for name, H0_val in [("Planck 2018", 67.4), ("SH0ES 2022", 73.04)]:
    H0_s = H0_val * 1000 / Mpc_m
    E_H = hbar * H0_s / eV
    print(f"\n    {name}:")
    print(f"      H0  = {H0_s:.4e} s^-1  (SI)")
    print(f"      E_H = hbar * H0 = {hbar:.4e} * {H0_s:.4e} / {eV:.4e}")
    print(f"          = {E_H:.4e} eV  (nat. Einheiten)")

# =================================================================
S("TEIL 4: T0-Vorhersage fuer E_H")
# =================================================================

print(f"""
  T0 berechnet nicht H0 [km/s/Mpc] -- das ist SI-Konvention.
  T0 berechnet E_H [eV] -- die Hubble-Energie.

  Verfuegbare T0-Parameter:
    xi = {XI:.6e}  (dimensionslos, Kopplungsstaerke)
    E0 = {E0_eV/1e6:.3f} MeV  (charakteristische Energie)

  E_H hat Dimension [Energie], xi ist dimensionslos.
  Also: E_H = E0 * f(xi)  mit f(xi) dimensionslos.""")

U("Bestimmung von f(xi)")

H0_planck_s = 67.4 * 1000 / Mpc_m
E_H_planck = hbar * H0_planck_s / eV

n_exact = np.log(E_H_planck / E0_eV) / np.log(XI)
print(f"""
    E_H(Planck) / E0 = {E_H_planck/E0_eV:.6e}
    = xi^n  mit n = ln(E_H/E0) / ln(xi) = {n_exact:.6f}
    Naechster einfacher Bruch: 41/4 = {41/4}""")

n_frac = Fraction(41, 4)
E_H_T0 = E0_eV * XI**float(n_frac)
abw = (E_H_T0 / E_H_planck - 1) * 100

print(f"""
    ┌─────────────────────────────────────────┐
    │                                         │
    │   E_H = E0 * xi^(41/4)                 │
    │                                         │
    │   = {E0_eV/1e6:.3f} MeV * xi^10.25             │
    │   = {E_H_T0:.4e} eV                    │
    │                                         │
    └─────────────────────────────────────────┘

    Gemessen (Planck): {E_H_planck:.4e} eV
    Abweichung: {abw:+.2f}%""")

# =================================================================
S("TEIL 5: Rueckrechnung E_H -> H0 [SI]")
# =================================================================

H0_T0_s = E_H_T0 * eV / hbar
H0_T0_Lj = H0_T0_s * Lj_km * 1000 / 1000  # s^-1 -> km/s/Lj
H0_T0_kms = H0_T0_s * Mpc_m / 1000

print(f"""
  Nat. Einheiten -> SI (durch hbar DIVIDIEREN):

    H0 [s^-1]     = E_H / hbar
                   = {E_H_T0:.4e} eV * {eV:.4e} J/eV / {hbar:.4e} J*s
                   = {H0_T0_s:.4e} s^-1

    H0 [km/s/Lj]  = H0[s^-1] * 1 Lj[m] / 1000
                   = {H0_T0_s:.4e} * {Lj_km*1000:.3e} / 1000
                   = {H0_T0_Lj:.4e} km/s/Lj

    H0 [km/s/Mpc] = H0[km/s/Lj] * {Mpc_Lj:.2e}
                   = {H0_T0_kms:.1f} km/s/Mpc""")

# =================================================================
S("ZUSAMMENFASSUNG")
# =================================================================

H0s_p = 67.4 * 1000 / Mpc_m
H0s_s = 73.04 * 1000 / Mpc_m
EH_p = hbar * H0s_p / eV
EH_s = hbar * H0s_s / eV

print(f"""
  H0 ist dreimal dasselbe (Strecke/Frequenz):
    {67.4} km/s/Mpc = {67.4/Mpc_Lj:.2e} km/s/Lj = {H0s_p:.4e} s^-1

  E_H ist eine NEUE Groesse (Energie):
    SI -> nat:  E_H = hbar * H0   (mit hbar multiplizieren)
    nat -> SI:  H0  = E_H / hbar  (durch hbar dividieren)
    In nat. Einheiten (hbar=1) sind E_H und H0 identisch.

    E_H (Planck) = hbar * H0 = {EH_p:.4e} eV
    E_H (SH0ES)  = hbar * H0 = {EH_s:.4e} eV

  T0-Vorhersage:
    E_H = E0 * xi^(41/4) = {E_H_T0:.4e} eV  ({abw:+.1f}% vs Planck)
    --> H0 = {H0_T0_kms:.1f} km/s/Mpc

  +--------------------+---------------------+----------+----------+----------+
  |                    | Formel              | Planck   | SH0ES    | T0       |
  +--------------------+---------------------+----------+----------+----------+
  | H0 [km/s/Mpc]     | Messung             | 67.40    | 73.04    | {H0_T0_kms:8.1f} |
  | H0 [km/s/Lj]      | H0 / 3.26e6         | {67.4/Mpc_Lj:.2e} | {73.04/Mpc_Lj:.2e} | {H0_T0_kms/Mpc_Lj:.2e} |
  | H0 [s^-1]         | H0*1e3/3.26e6/      |          |          |          |
  |                    |   9.461e12/1e3      | {H0s_p:.2e} | {H0s_s:.2e} | {H0_T0_s:.2e} |
  +--------------------+---------------------+----------+----------+----------+
  | E_H [eV]          | hbar*H0 (SI->nat)   | {EH_p:.2e} | {EH_s:.2e} | {E_H_T0:.2e} |
  +--------------------+---------------------+----------+----------+----------+
  | Erste 3 Zeilen: H0 (Einheitenumrechnung, alles dasselbe)                |
  | Letzte Zeile: E_H (neue Groesse, * hbar: SI->nat, / hbar: nat->SI)      |
  +--------------------------------------------------------------------------+""")