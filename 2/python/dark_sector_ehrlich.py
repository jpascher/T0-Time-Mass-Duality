import numpy as np

# ============================================================================
# FFGFT Dunkler Sektor -- ehrliche Bestandsaufnahme
#
# Ziel: sauber trennen, welche FFGFT-Relationen zum "Dunklen Sektor"
#   (a) echte Vorhersagen aus xi sind,
#   (b) zirkulaer oder fit-abhaengig sind (also NICHTS beweisen),
#   (c) noch ganz offen sind.
# Alle Zahlen gegen den Korpus (Dok 025/028/091) geprueft; nichts geraten.
# Kein neues physikalisches Ergebnis wird behauptet -- das ist eine Pruefung.
#
# Aktualisiert am 1.10.2026: Casimir-Energiedichte 240 -> 720 (pi^2/(720 xi)
# = 102.8; 240 gehoert zum Druck), Casimir/CMB als Identitaet nach (b)
# verschoben (L_xi wird aus rho_CMB bestimmt; 312 ist kein Messwert),
# T_CMB nach (c) verschoben (einheitenabhaengige Uebereinstimmung, keine
# Herleitung), Fazit angepasst; Identitaetspruefung ergaenzt (vgl. Dok. 025/263
# bzw. Dok. 190, R136/R137).
# ============================================================================

xi   = 4/30000.0          # 1.3333e-4
hbar = 6.582e-16          # eV*s
c    = 2.998e8            # m/s
kB   = 8.617e-5           # eV/K

print("="*70)
print("FFGFT Dunkler Sektor -- was traegt, was nicht (xi = %.4e)" % xi)
print("="*70)

# ---------------------------------------------------------------------------
print("\n(a) ECHTE Vorhersagen aus xi (kein Fit, kein zirkulaerer Exponent)")
print("-"*70)
print("  Im Dunklen Sektor derzeit KEINE. Casimir/CMB ist eine Identitaet (b),")
print("  T_CMB eine einheitenabhaengige Uebereinstimmung ohne Herleitung (c).")

# ---------------------------------------------------------------------------
print("\n(b) NICHT tragfaehig: zirkulaer bzw. fit-abhaengig")
print("-"*70)

# Casimir/CMB-Verhaeltnis der ENERGIEDICHTEN: pi^2/(720 xi)  (240 = Druck)
hbar_c_SI = 1.054571817e-34 * 299792458.0     # J*m
rho_CMB   = 4.175e-14                         # J/m^3 (Dok 025)
L_xi      = (xi * hbar_c_SI / rho_CMB)**0.25  # L_xi AUS rho_CMB bestimmt
rho_cas   = lambda d: np.pi**2 * hbar_c_SI / (720 * d**4)
cas       = np.pi**2/(720*xi)
cas_Lxi   = rho_cas(L_xi)/rho_CMB
cas_100   = rho_cas(100e-6)/rho_CMB
print(f"Casimir/CMB:  pi^2/(720 xi) = {cas:.1f}   (Energiedichte; frueher 240 -> 308 = Druck)")
print(f"      L_xi aus rho_CMB = xi*hbar*c/L_xi^4:  L_xi = {L_xi*1e6:.2f} um")
print(f"      rho_Cas(L_xi)/rho_CMB = {cas_Lxi:.1f}  == pi^2/(720 xi)  -> IDENTITAET")
print(f"      mit gerundetem L = 100 um: {cas_100:.1f}  (frueherer 'Messwert' 312 war")
print(f"      dieselbe Formel mit Druck und gerundetem L_xi -- kein Messwert)")
print(f"      -> Skalenaussage, kein Beleg (R136).")
assert abs(cas - 102.8) < 0.05
assert abs(cas_Lxi - cas) < 1e-9 * cas          # Identitaet
assert abs(cas_100 - 103.8) < 0.05
assert abs(np.pi**2/(240*xi) / cas - 3) < 1e-12  # alter Wert = 3 x Energiedichte (Druck)
print()

# DE/DM-Verhaeltnis: xi^(ln(2.5)/ln(xi)) == 2.5 fuer JEDES xi
print("DE/DM-Verhaeltnis:  rho_DE/rho_DM = xi^(ln(2.5)/ln xi)  [Dok 028, Riddle 5]")
for xt in [xi, 1e-3, 1e-5, 0.5, 0.9]:
    a = np.log(2.5)/np.log(xt)
    print(f"      xi={xt:<8.4g}: xi^alpha = {xt**a:.4f}")
print("      -> ergibt IMMER 2.5, unabhaengig von xi.")
print("      ALS VORHERSAGE: zirkulaer (2.5 steckt im Exponenten).")
print("      ALS UMRECHNUNGSFAKTOR: zulaessig -- 2.5 (Omega_L/Omega_DM) ist")
print("      selbst eine LambdaCDM-Pipeline-Ausgabe, kein modellneutraler Wert.")
print("      Wie c (Meter/Sekunde) oder z darf so ein Faktor zirkulaer kalibriert")
print("      sein. EINSCHRAENKUNG: anders als bei c enthaelt die LambdaCDM-Seite")
print("      mit rho_DE ein Artefakt (kein Lambda in FFGFT) -> nur teils sinnvoll.")

# MOND-Skala: xi^(1/4) * K_M
K_M = 1.637
print(f"\nMOND-Skala:  a0/(cH0) = xi^(1/4) * K_M  [Dok 028, Riddle 4]")
print(f"      xi^(1/4) = {xi**0.25:.4f}  (echt aus xi)")
print(f"      K_M      = {K_M}  (FREIER Fit-Faktor, keine Herleitung)")
print(f"      Produkt  = {xi**0.25*K_M:.4f}  (Experiment 0.176)")
print(f"      -> nur das xi^(1/4) ist echt; Uebereinstimmung erkauft mit K_M.")

# ---------------------------------------------------------------------------
print("\n(c) OFFEN: nicht aus xi hergeleitet")
print("-"*70)
# CMB-Temperatur: (16/9) xi ergibt eine reine Zahl, erst in eV = Messwert
T_CMB_struct = (16/9)*xi   # dimensionslose Kernzahl
print(f"  - CMB:  T_CMB = (16/9) xi [eV]  [Dok 025/028]; Kernfaktor = {T_CMB_struct:.4e}")
print(f"    -> {T_CMB_struct/kB:.4f} K nur in der Einheit eV; einheitenabhaengige")
print(f"       Uebereinstimmung, Koeffizient ohne geometrische Herleitung (R137 i).")
print("""  - Omega_DM ~ 0.26: keine Formel rho_DM(xi) im Korpus, nur Behauptung
    'korrekte Energiedichte bei dm ~ xi*m_Planck' (Dok 025), nicht gerechnet.
  - Galaxien-Rotationskurve v(r): nirgends als Profil durchgerechnet
    (nur die MOND-Skala a0, und die haengt an K_M).
  - Es gibt ZWEI unverbundene DM-Bilder: xi-Feld als Substanz (Dok 025)
    vs. MOND/modifizierte Gravitation (Dok 028/201). Konkurrierend, nicht
    vereinheitlicht.""")

# ---------------------------------------------------------------------------
print("\n" + "="*70)
print("Was man HONEST sagen kann:")
print("="*70)
print("""  FFGFT eliminiert Dunkle Energie (kein Lambda, statisch) -- konsistent.
  Die CMB/Casimir-Relationen sind KEINE Vorhersagen: Casimir/CMB = pi^2/(720 xi)
  ist eine Identitaet (R136), T_CMB eine einheitenabhaengige Uebereinstimmung
  ohne Herleitung, offen (R137 i).
  Die DM-DEUTUNG ist geklaert: DM ist ein xi-geometrischer Effekt, ein
  Artefakt der LambdaCDM-Sicht (wie H0/z), keine Substanz. Das DE/DM-
  Verhaeltnis ist als VORHERSAGE zirkulaer, als UMRECHNUNGSFAKTOR zur
  LambdaCDM-Buchhaltung aber zulaessig (eingeschraenkt durch rho_DE-Artefakt).
  Quantitativ offen bleiben die T_CMB-Herleitung und die modellneutrale
  Omega_DM/Rotationskurve.
  -> Belastbare quantitative xi-Vorhersage im Dunklen Sektor: derzeit keine.
""")
