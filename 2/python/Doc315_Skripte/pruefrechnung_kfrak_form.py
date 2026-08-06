#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pruefrechnung_kfrak_form.py -- Formdiskriminierung K_frak
=============================================================
Frage: Bestaetigt der Korpus die ADDITIVE Form  K_add = 1 - 100*xi = 74/75
       oder waere auch die MULTIPLIKATIVE Form  K_mul = (1 - xi)^100
       mit den vorhandenen Bestaetigungen vertraeglich?

Abstand der beiden Formen:  relativ ~8.9e-5.
Eine Korpus-Stelle diskriminiert nur, wenn ihre eigene Unsicherheit
(Messfehler, Rundung von Eingangsgroessen, Restfehler der Identitaet)
KLEINER als dieser Abstand ist -- sonst liegt beides im Toleranzbereich.

Geprueft werden die drei im Korpus genannten Zeugen:
  TEST A  A130: Zwei-Routen-Messung  K_mess = (E0_Weg2 / E0_Weg1)^-2
  TEST B  A270: Hochpotenz-Identitaet K^-36 ~ 16/pi^2 (Verstaerker x36)
  TEST C  A040: Potenzform (D_eff/3)^(D_eff/2) mit D_eff = 2.973

Nur Standardbibliothek; exakte Brueche wo moeglich.
"""
import math
from fractions import Fraction

# ---------------------------------------------------------------- Grundlagen
XI_F   = Fraction(4, 30000)
XI     = float(XI_F)
K_ADD_F = Fraction(1) - 100 * XI_F          # 74/75 exakt
K_MUL_F = (Fraction(1) - XI_F) ** 100        # exakter Bruch (riesig)
K_ADD, K_MUL = float(K_ADD_F), float(K_MUL_F)
GAP = K_MUL / K_ADD - 1.0                    # relativer Formabstand

# CODATA/PDG-Massen (MeV), relative Unsicherheiten
ME,  ME_REL  = 0.51099895069, 3.0e-10
MMU, MMU_REL = 105.6583755,   2.2e-8

def urteil(name, resid_add, resid_mul, unsicherheit, formabstand=None):
    """Entscheidungslogik pro Test.
    formabstand: der AN DIESER STELLE wirksame Abstand der beiden Formen
    (bei Potenz-Tests verstaerkt!). Default: unverstaerkter GAP."""
    fa = abs(GAP) if formabstand is None else abs(formabstand)
    print(f"   |Residuum additiv|          = {abs(resid_add):.3e}")
    print(f"   |Residuum multiplikativ|    = {abs(resid_mul):.3e}")
    print(f"   eigene Unsicherheit         = {unsicherheit:.3e}")
    print(f"   wirksamer Formabstand hier  = {fa:.3e}")
    if unsicherheit >= fa:
        print(f"   URTEIL {name}: KEINE Diskriminierung moeglich -- die eigene")
        print(f"          Unsicherheit ({unsicherheit:.1e}) uebersteigt den Formabstand.")
        return None
    # Diskriminierend: eine Form muss deutlich besser passen als die andere,
    # und die schlechtere muss klar ausserhalb von (Unsicherheit + Rest der
    # besseren) liegen.
    besser, schlechter = ("add", "mul") if abs(resid_add) < abs(resid_mul) else ("mul", "add")
    r_b = min(abs(resid_add), abs(resid_mul))
    r_s = max(abs(resid_add), abs(resid_mul))
    if r_s > max(unsicherheit, 3 * r_b):
        lang = "ADDITIV" if besser == "add" else "MULTIPLIKATIV"
        print(f"   URTEIL {name}: diskriminiert ZUGUNSTEN {lang}"
              f" (Verhaeltnis der Residuen {r_s/r_b:.1f}:1).")
        return besser
    print(f"   URTEIL {name}: beide Formen im Toleranzbereich der Stelle --")
    print(f"          keine belastbare Formaussage.")
    return None

print("=" * 74)
print("FORMDISKRIMINIERUNG K_frak:  1-100xi  vs  (1-xi)^100")
print("=" * 74)
print(f"K_add = 74/75      = {K_ADD:.10f}")
print(f"K_mul = (1-xi)^100 = {K_MUL:.10f}")
print(f"relativer Formabstand = {GAP:+.3e}   (Schwelle fuer jede Pruefstelle)")

# ---------------------------------------------------------------- TEST A
print("\n" + "-" * 74)
print("TEST A  (A130): Zwei-Routen-Messung von K_frak")
print("-" * 74)
print("  Weg 1: E0 = sqrt(m_e * m_mu)          (nur Messmassen)")
print("  Weg 2: E0^2 = 4*sqrt(2)*m_mu / xi^p   (p aus Korpus-Skript: -0.2679)")
E0_1 = math.sqrt(ME * MMU)

def K_mess(p):
    E0_2 = math.sqrt(4 * math.sqrt(2) * MMU * XI ** (-p))
    return (E0_2 / E0_1) ** (-2)

P_KORPUS = -0.2679                    # wie in a130_alpha_kette.py
P_EXAKT  = -(2 - math.sqrt(3))        # Kandidat: 2-sqrt(3) = 0.26794919...

for label, p in (("p = -0.2679 (Korpus-Literal, 4 Stellen)", P_KORPUS),
                 ("p = -(2-sqrt3) = -0.26794919... (Kandidat)", P_EXAKT)):
    Km = K_mess(p)
    print(f"\n  Variante: {label}")
    print(f"   K_mess = {Km:.8f}")
    r_add = Km / K_ADD - 1.0
    r_mul = Km / K_MUL - 1.0
    # Unsicherheitsbudget:
    #  (a) Massen: K haengt ueber E0_1 von sqrt(me*mmu) ab -> dK/K = d(me*mmu)/(me*mmu)
    u_mass = ME_REL + MMU_REL         # ~2e-8, vernachlaessigbar
    #  (b) p selbst: dK/K = |ln xi| * dp.  Rundung 4 Stellen -> dp = 5e-5
    dlnxi = abs(math.log(XI))
    u_p = dlnxi * (5e-5 if p == P_KORPUS else 0.0)
    u = u_mass + u_p
    print(f"   Unsicherheitsbudget: Massen {u_mass:.1e}"
          + (f", p-Rundung {u_p:.1e} (|ln xi|*5e-5)" if u_p else ", p exakt gesetzt"))
    urteil("A", r_add, r_mul, u if u > 0 else u_mass)

print("\n  Empfindlichkeit: dK/K = |ln xi| * dp = %.2f * dp" % dlnxi)
print("  -> Damit Test A den Formabstand (8.9e-5) aufloest, muss p auf")
print("     besser als dp = %.1e bekannt sein (>= 6 Stellen)." % (abs(GAP)/dlnxi))
print("  -> OFFEN: Der Korpus gibt p nur als 4-stelliges Literal an. Ist")
print("     p = -(2-sqrt3) exakt [herzuleiten], diskriminiert Test A scharf.")

# ---------------------------------------------------------------- TEST B
print("\n" + "-" * 74)
print("TEST B  (A270): Hochpotenz  K_frak^-36  ~  16/pi^2   (Verstaerker x36)")
print("-" * 74)
REF = 16 / math.pi ** 2
B_add = K_ADD ** (-36)
B_mul = K_MUL ** (-36)
print(f"   16/pi^2            = {REF:.7f}")
print(f"   (74/75)^-36        = {B_add:.7f}   (rel. {B_add/REF-1:+.3e})")
print(f"   ((1-xi)^100)^-36   = {B_mul:.7f}   (rel. {B_mul/REF-1:+.3e})")
print(f"   Formabstand hier verstaerkt auf 36*8.9e-5 = {36*abs(GAP):.2e}")
# Unsicherheit der Stelle: A270 nennt Uebereinstimmung 0.010% => 1e-4 als
# beobachtete Toleranz der Identitaet selbst.
u_B = 1.0e-4
urteil("B", B_add / REF - 1.0, B_mul / REF - 1.0, u_B, formabstand=36 * GAP)
print("   VORBEHALT: 16/pi^2 ist im Korpus als Koinzidenz ohne Vorwaerts-")
print("   Herleitung gefuehrt (P35). Test B diskriminiert nur UNTER der")
print("   Annahme, dass 16/pi^2 die richtige Referenz ist.")

# ---------------------------------------------------------------- TEST C
print("\n" + "-" * 74)
print("TEST C  (A040): Potenzform  (D_eff/3)^(D_eff/2),  D_eff = 2.973")
print("-" * 74)
D = 2.973
C = (D / 3) ** (D / 2)
print(f"   Potenzform  = {C:.6f}")
print(f"   K_add       = {K_ADD:.6f}   (rel. {C/K_ADD-1:+.3e})")
print(f"   K_mul       = {K_MUL:.6f}   (rel. {C/K_MUL-1:+.3e})")
# Unsicherheit: D_eff nur 4-stellig -> dC/C = |d/dD ln C| * dD
dlnC_dD = 0.5 * math.log(D / 3) + 0.5 * (D / 3) ** 0 * (D / D)  # ln-Ableitung
dlnC_dD = 0.5 * math.log(D / 3) + 0.5  # d/dD [ (D/2) ln(D/3) ] = ln(D/3)/2 + 1/2
u_C = abs(dlnC_dD) * 5e-4
print(f"   D_eff-Rundung (4 Stellen, dD=5e-4) -> dC/C = {u_C:.2e}")
urteil("C", C / K_ADD - 1.0, C / K_MUL - 1.0, u_C)

# ---------------------------------------------------------------- FAZIT
print("\n" + "=" * 74)
print("GESAMTFAZIT")
print("=" * 74)
print("""\
 A (A130, p = -0.2679 wie im Korpus): KEINE Formaussage -- die 4-stellige
    p-Rundung verschmiert die Messung (4.5e-4) staerker als der
    Formabstand (8.9e-5).
 A (A130, p = -(2-sqrt3) exakt):     diskriminiert ZUGUNSTEN ADDITIV,
    Residuen 1.4e-5 vs 1.0e-4 (7.5:1). BEDINGUNG: die exakte Identitaet
    p = -(2-sqrt3) muss im Korpus erst hergeleitet/deklariert werden --
    derzeit steht dort nur das Zahlenliteral. PRUEFAUFTRAG P-neu.
 B (A270, ^-36 vs 16/pi^2):          diskriminiert ZUGUNSTEN ADDITIV,
    Residuen 1.0e-4 vs 3.1e-3 (31:1) -- der x36-Verstaerker macht den
    Formabstand zu 0.32%. BEDINGUNG: gilt nur unter der Referenz-Annahme
    16/pi^2, die selbst als Koinzidenz ohne Vorwaertsherleitung gefuehrt
    wird (P35 offen).
 C (A040, Potenzform, D_eff=2.973):  keine Formaussage (D_eff nur
    4-stellig, Unsicherheit 2.5e-4 > 8.9e-5); tendiert additiv (1.6e-5
    vs 1.0e-4), reicht aber nicht als eigenstaendiger Zeuge.

 ERGEBNIS: Beide belastbaren Diskriminierungen (A-exakt, B) zeigen in
 dieselbe Richtung -- ADDITIV, also 1-100xi = 74/75 -- aber jede haengt an
 einer noch offenen Voraussetzung (p-Identitaet bzw. 16/pi^2-Referenz).
 Unbedingt diskriminiert ist die Form damit NOCH NICHT; sie ist zweifach
 bedingt-bestaetigt. Sauberer Status: [B] mit zwei benannten Bedingungen,
 nicht [K]-gemessen. Kandidat fuer Registereintrag in Dok. 190.""")
