import numpy as np

# ============================================================================
# Vakuum-Energiedichte als Emergenz der Dekompaktifizierung
#
# NEUE Modellrechnung (Reduktionsschicht / Plausibilitaet), aufgesetzt auf das
# BELEGTE Prinzip aus Dok 261:
#   - Layer 1 (kompaktes T^4, hbar=c=1, reine Verhaeltnisse): statisch,
#     korrekturfrei; nur dimensionslose Groessen.
#   - Layer 2 (SI-Projektion, dekompaktifiziert): c, hbar, eps0 werden real
#     als "Embedding-Preis"; dieselben Groessen werden dimensionsbehaftet SICHTBAR
#     (sie entstehen nicht -- sie waren kompaktifiziert schon da).
# Diese Rechnung SPEZIALISIERT das Prinzip auf die Vakuum-Energiedichte, die
# in Dok 261 nicht explizit als Beispiel durchgerechnet ist.
#
# KORRIGIERTE These (Johanns Punkt): In der kompaktifizierten Sicht ist ALLES
# vorhanden, was in der dekompaktifizierten Sicht da ist -- es kommt NICHTS
# hinzu. Die volle Modenstruktur (xi/L_xi^4) ist in Layer 1 vollstaendig da,
# nur EINHEITENLOS (reines Verhaeltnis). rho_vac "entsteht" NICHT bei der
# Dekompaktifizierung; es ist dieselbe Groesse in zwei Darstellungen:
#   Layer 1: vollstaendig vorhanden, dimensionslos (kein Joule).
#   Layer 2 (SI): DIESELBE Struktur, dimensionsbehaftet (J/m^3).
# Was die Dekompaktifizierung tut, ist NICHT erzeugen, sondern SICHTBAR machen:
# aus SI-Sicht wird die schon vorhandene fraktale/zeitliche Struktur, die zuvor
# kompaktifiziert (eingerollt) war, als Energiedichte ablesbar. Der Faktor
# hbar*c ist dabei nur die UMRECHNUNG in SI -- er begruendet/erzeugt nichts
# (vgl. c_emergenz.py: c, hbar c, sqrt(hbar G/c^5) sind reine Umrechnungsfaktoren).
# Quelle der Zielformel: Dok 091/025  rho_CMB = xi * hbar c / L_xi^4.
# ============================================================================

xi   = 4/30000.0
hbar = 1.0546e-34      # J*s
c    = 2.998e8         # m/s
hbarc_eVm = 1.973e-7   # eV*m  (Embedding-Faktor in eV-Sprache)
L_xi = 1.0e-4          # m  (~100 µm, charakteristische xi-Laenge, Dok 091)
eV   = 1.602e-19       # J

print("="*70)
print("Vakuum-Energiedichte: kompaktifiziert vorhanden, dekompaktifiziert sichtbar")
print("(neue Reduktions-Rechnung, aufgesetzt auf Dok 261; Ziel rho aus Dok 091)")
print("="*70)

# --- LAYER 1: kompaktes T^4, hbar=c=1, reine Verhaeltnisse ---
print("\n[LAYER 1]  kompaktes T^4, hbar=c=1, reine Verhaeltnisse (statisch)")
print("-"*70)
print("""In natuerlichen Einheiten ist die Moden-/Windungsstruktur dimensionslos.
Die Moden-Abzaehlung (Dok 091, d=3+delta) liefert einen dimensionslosen
Vorfaktor, aus dem xi herausfaellt; nennen wir die reine Modenzahl-Dichte
   n_vac = xi / L_xi^4   ALS REINE ZAHL  (kein J, kein m^3 -- es gibt in
   Layer 1 keine SI-Einheiten, also KEINE Energiedichte im physik. Sinn).""")
n_vac_dimlos = xi / L_xi**4   # nur als Zahl betrachtet (Einheiten noch "1")
print(f"   reine Modendichte-Zahl xi/L_xi^4 = {n_vac_dimlos:.3e}   [dimensionslos in L1]")
print("   -> Diese Struktur ist in Layer 1 VOLLSTAENDIG VORHANDEN -- aber")
print("      EINHEITENLOS: hbar,c sind =1, 'Energie' und 'inverse Laenge' sind")
print("      dieselbe Zahl, es gibt kein absolutes 'Joule pro m^3'. rho_vac fehlt")
print("      NICHT -- es liegt nur in dimensionsloser Darstellung vor.")

# --- UEBERGANG: Embedding-Preis hbar*c (Dok 261) ---
print("\n[UEBERGANG]  Dekompaktifizierung -- Embedding-Preis (Dok 261)")
print("-"*70)
print("""Erst wenn die zuvor kompaktifizierte (eingerollte) fraktale/zeitliche
Struktur als realer Prozess in Pfeil-Zeit dekompaktifiziert wird, werden
c, hbar als SI-Umrechnung wirksam (Dok 261/262). Dieser Schritt ERZEUGT
nichts -- er macht die schon vorhandene Struktur in SI ABLESBAR, indem er
sie mit hbar*c in dimensionsbehaftete Form umrechnet:
   rho_vac (Layer 2, SI-Darstellung) = (xi / L_xi^4) * hbar c""")

# --- LAYER 2: dimensionsbehaftete Energiedichte ---
rho_vac = xi * hbar * c / L_xi**4    # J/m^3
rho_vac_eV = rho_vac / eV            # eV/m^3
print("\n[LAYER 2]  dekompaktifiziert -- jetzt existiert rho_vac MIT Einheiten")
print("-"*70)
print(f"   rho_vac = xi * hbar c / L_xi^4")
print(f"           = {rho_vac:.3e} J/m^3")
print(f"           = {rho_vac_eV:.3e} eV/m^3")
print(f"   (entspricht der Korpus-Form rho_CMB = xi*hbar c/L_xi^4, Dok 091/025)")

# --- der eigentliche Punkt, explizit ---
print("\n" + "-"*70)
print("DER PUNKT (was die Rechnung zeigt):")
print("-"*70)
print(f"""   Die ZAHL xi/L_xi^4 = {n_vac_dimlos:.3e} ist in beiden Layern dieselbe,
   und die STRUKTUR ist in beiden vollstaendig vorhanden. Es kommt NICHTS hinzu.
   Was sich aendert, ist allein die DARSTELLUNG:
     Layer 1:  dieselbe Struktur, dimensionslos (eingerollt/kompaktifiziert)
     Layer 2:  dieselbe Struktur, * hbar c (SI-Umrechnung) -> ablesbar in J/m^3
   Die Vakuum-ENERGIE entsteht also NICHT als neue Substanz. Sie ist
   kompaktifiziert bereits da; aus SI-Sicht wird sie erst SICHTBAR durch die
   Dekompaktifizierung der fraktalen/zeitlichen Struktur. hbar c ist dabei nur
   die Umrechnung (begruendet nichts, vgl. c_emergenz.py).""")

# --- ehrliche Grenzen ---
print("\n" + "="*70)
print("EHRLICHE GRENZEN dieser Rechnung:")
print("="*70)
print("""  1. Dies ist eine SPEZIALISIERUNG des in Dok 261 belegten Prinzips,
     KEINE eigenstaendige Ableitung. Das Prinzip (L1 korrekturfrei /
     L2 = SI-Projektion mit realem hbar,c) ist Korpus; die Anwendung auf
     rho_vac ist hier neu zusammengesetzt.
  2. Praezise Lesart: rho_vac ist in L1 vollstaendig VORHANDEN, nur einheitenlos.
     'Erst dekompaktifiziert sichtbar' ist eine Aussage ueber die SI-DARSTELLUNG,
     nicht ueber Existenz. Es entsteht nichts; es wird umgerechnet/ablesbar.
  3. ACHTUNG Zahlenwert-Zirkularitaet: L_xi wird in Dok 091 SELBST aus
     rho_CMB bestimmt (L_xi = (xi/rho_CMB)^(1/4)). Setzt man dieses L_xi in
     rho_CMB = xi*hbar c/L_xi^4 zurueck, ist der ZAHLENWERT zirkulaer -- er
     bestaetigt nur die Selbstkonsistenz, sagt rho_CMB nicht unabhaengig vorher.
     Der KONZEPTUELLE Punkt (Punkt oben) ist davon UNABHAENGIG: er betrifft den
     Statuswechsel dimensionslos->dimensionsbehaftet, nicht den Zahlenwert.
  4. Es wird NICHT gezeigt, dass dieses rho_vac die kosmologische DE/DM-Bilanz
     ergibt (das bleibt offen, s. dark_sector_ehrlich.py / Dok 190 P17).
  -> Status: Reduktionsschicht / Konsistenz-Demonstration, nicht Kern-Ergebnis.""")
