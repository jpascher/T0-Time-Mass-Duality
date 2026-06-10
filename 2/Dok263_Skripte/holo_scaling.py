import numpy as np

# ============================================================================
# FFGFT - Holografische Projektion am beschraenkten Kern aufgehaengt
#
# STATUS DIESER DEUTUNG -- WICHTIG:
#   Die inhaltliche Deutung unten ist REDUKTIONSSCHICHT / HYPOTHESE (Dok 263),
#   NICHT belegtes FFGFT-Kernergebnis und in Dok 190 NICHT als abgeschlossen
#   gefuehrt. Die Skalierungs-RECHNUNG ist sauber; die ontologische Deutung
#   (Entropie = Windungszahlen) ist eine Vermutung.
#
#   Vermutung (Dok 263): die am Kern erhaltene Information ist nur die
#   Grundinformation ueber die geometrische Struktur (Windungszahlen), nicht
#   die volle Vorgeschichte. Die Projektion waere dann verlustbehaftet und
#   gerichtet. (Das Nichtabschluss-Theorem Dok 193 ist eine SEPARATE
#   algebraische Aussage und beweist diese Deutung nicht.)
#
#   Skalierung: Exponent nutzt D_f = 3 - xi. Der Defekt xi ist via Rekursion R
#   / Skalenfluss begruendet (Dok 203), NICHT ueber Renormierungsgruppen-Denken
#   (Dok 190, P5/P7: "Renormierungsgruppe" -> "Skalenfluss/Rekursion R").
# ============================================================================

xi = 4/30000.0
Df = 3 - xi
rho0 = 1/xi**2          # Dok 201: Dichte beschraenkt durch 1/xi^2 ("fixed by T0 geometry")
print("="*72)
print("FFGFT: Holografische Projektion am beschraenkten Kern aufgehaengt")
print("="*72)
print(f"xi   = {xi:.10e}")
print(f"D_f  = 3 - xi = {Df:.10f}")
print(f"rho0 = 1/xi^2 = {rho0:.4e}   (Dok 201: max. Vakuumdichte, keine Singularitaet)\n")

# ---------------------------------------------------------------------------
# Anker: keine Singularitaet. Endlicher Kernradius R_core (Knoten gesaettigt,
# Dichte = rho0 = 1/xi^2, reguliert durch Mediatormasse m_T = lambda/xi).
# Flaechengesetz-Skalierung S ~ R^a gilt NUR fuer R >= R_core; darunter
# Saettigung. Schematische Kernskala R_core/lP ~ 1/xi (O(1)-Faktor modellabh.).
# ---------------------------------------------------------------------------
Rcore_over_lP = 1.0/xi
print(f"Kernskala (schematisch): R_core/lP ~ 1/xi = {Rcore_over_lP:.3e}  (log10 ~ {np.log10(Rcore_over_lP):.2f})")
print("  O(1)-Faktor modellabhaengig; nur Groessenordnung folgt aus rho<=1/xi^2.\n")

# Was die Entropie zaehlt: GEOMETRISCHE Grundinformation, nicht volle Historie.
# (reine Skalierungsbetrachtung; Vorfaktoren kuerzen sich in Verhaeltnissen)
def S_raw(R, a):
    return (4*np.pi)*R**a / xi**2
def S_anchored(R, a):
    Rc = Rcore_over_lP
    return np.where(R >= Rc, S_raw(R, a), S_raw(Rc, a))   # Saettigung unter R_core

# --- Skalierungsannahmen (vgl. Dok 263) ---
# A: reines Flaechengesetz   S ~ R^2        (Dok 201 §7.6)
# B: fraktale FLAECHE        S ~ R^(2-xi)   (Reduktionsschicht, offen)
# C: fraktales VOLUMEN       S ~ R^2        (Flaechengesetz bleibt exakt)
print("Skalierungs-Exponenten:  A=2 | B=2-xi=%.10f | C=2" % (Df-1))
print("Nur B bricht das Bekenstein-Hawking-Gesetz (um exakt xi im Exponenten).\n")

print("Entropie-Skalierung MIT Anker am Kern (Annahme B):")
print(f"{'R/lP':>10} | {'log10':>6} | {'S_B ungebremst':>16} | {'S_B verankert':>16} | {'Status':>12}")
print("-"*72)
for logN in [1, 3, 6, 10, 20, 38]:
    R = 10.0**logN
    raw = S_raw(R, Df-1)
    anc = float(S_anchored(np.array([R]), Df-1)[0])
    status = "unter R_core" if R < Rcore_over_lP else "regulaer"
    print(f"10^{logN:<7} | {logN:6d} | {raw:16.4e} | {anc:16.4e} | {status:>12}")

print("\n--> Punkte mit log10(R/lP) < ~3.9 liegen UNTERHALB des Kerns:")
print("    physikalisch bedeutungslos (Bereich der nicht-existenten Singularitaet).")
print("    Erst oberhalb R_core ist die Skalierung gueltig.\n")

# Astrophysikalische Loecher: R/lP >> R_core -> Abweichung bleibt gueltig
print("Astrophysikalische Loecher (R/lP >> R_core): -xi*ln(R/lP)-Abweichung gueltig")
for name, Rs in [("Sonnenmasse (R~3 km)", 3e3),
                 ("Sagittarius A* (R~1.2e10 m)", 1.2e10),
                 ("M87* (R~1.9e13 m)", 1.9e13)]:
    R = Rs/1.616e-35
    dev = R**(Df-1-2) - 1     # B gegen A
    print(f"  {name:28s}: R/lP~{R:.2e} >> R_core -> Abw. {dev*100:+.3f} %  ~ -xi*lnR={-xi*np.log(R)*100:+.3f}%")

print("\nFAZIT:")
print("  1. Keine Singularitaet -> physikalischer Cutoff bei R_core ~ lP/xi.")
print("     R^(2-xi) gilt nur oberhalb des Kerns; darunter Saettigung.")
print("  2. Alte Klein-R-Zeilen (log10<~3.9) waren unphysikalisch (Kerninneres).")
print("  3. Reale Loecher: R/lP >> R_core -> Abweichung unveraendert gueltig.")
print("  4. Anker = dasselbe xi wie in T*m=1 und D_f -> FFGFT-eigen, nicht AdS/CFT.")
print("  5. DEUTUNG (HYPOTHESE, Dok 263, nicht belegt): erhaltene Entropie =")
print("     geometrische Grundinformation (Windungszahlen), nicht volle Vorgeschichte.")
