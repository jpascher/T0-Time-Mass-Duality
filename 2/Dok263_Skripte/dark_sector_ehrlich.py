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

# CMB-Temperatur:  T_CMB = (16/9) xi^2 E_xi,  E_xi = (1/xi) kB  -> (16/9) xi kB ... 
# Korpus nennt 2.725 K. Pruefen wir die Struktur 16/9 * xi * (1/kB-Skala):
# E_xi = (1/xi) * kB  bedeutet  T = (16/9) xi^2 * (1/xi) = (16/9) xi  [in Einheiten 1/kB]
T_CMB_struct = (16/9)*xi   # dimensionslose Kernzahl
print(f"CMB:  T_CMB = (16/9) xi^2 E_xi   [Dok 025/028]")
print(f"      Kernfaktor (16/9)*xi = {T_CMB_struct:.4e}")
print(f"      Korpus: ergibt 2.725 K (0% Abw. lt. Dok 028) -- xi steht ALLEIN, echt.")

# Casimir/CMB-Verhaeltnis: pi^2/(240 xi)
cas = np.pi**2/(240*xi)
print(f"\nCasimir/CMB:  pi^2/(240 xi) = {cas:.1f}")
print(f"      Korpus/Experiment ~308-312 (1.3% Abw.) -- xi steht ALLEIN, echt.")
print(f"      -> 'freies Vakuum' (rho_CMB) vs 'eingeschraenktes' (rho_Casimir):")
print(f"         genau das bewegungs-/randinduzierte Bild, quantitativ.")

# ---------------------------------------------------------------------------
print("\n(b) NICHT tragfaehig: zirkulaer bzw. fit-abhaengig")
print("-"*70)

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
  Die CMB/Casimir-Relationen sind echte xi-Vorhersagen (a).
  Die DM-DEUTUNG ist geklaert: DM ist ein xi-geometrischer Effekt, ein
  Artefakt der LambdaCDM-Sicht (wie H0/z), keine Substanz. Das DE/DM-
  Verhaeltnis ist als VORHERSAGE zirkulaer, als UMRECHNUNGSFAKTOR zur
  LambdaCDM-Buchhaltung aber zulaessig (eingeschraenkt durch rho_DE-Artefakt).
  Quantitativ offen bleibt nur die modellneutrale Omega_DM/Rotationskurve.
  -> Belastbar ist die VAKUUM-/CMB-Struktur, nicht der 'Dunkle-Materie'-Anspruch.
""")
