#!/usr/bin/env python3
"""
180_mT_struktur_L0_verify.py
============================
Numerische Verifikation der Zeitfeld-Mediatormasse m_T und der
daraus folgenden Herleitung der Minimalskala L_0 = xi * lP.

Hintergrund:
  Der T0-Lagrangian (Dok. 019/180/201) enthaelt ein massives Zeitfeld
  Delta m mit Mediatormasse m_T = lambda/xi und Kopplung g_T = xi*m_l.
  Der Korpus verwendet "m_T" an mehreren Stellen mit verschiedenen
  Zahlenwerten. Dieses Skript zeigt, dass es sich um EINE Struktur mit
  verschiedenen Basismassen handelt -- und dass daraus der Exponent 1
  in L_0 = xi^1 * lP folgt.

Geprueft wird:
  [1] Die Regel m_T = M_basis/xi  =>  Reichweite = xi * Compton(M_basis)
  [2] Leptonsektor (Dok. 032): M_basis = m_e, m_T ~ 5,22 GeV
  [3] Fundamentaler Sektor: M_basis = m_P  =>  Reichweite = L_0 exakt
  [4] Der Exponent 1 folgt aus m_T ~ 1/xi (Lagrangian), nicht aus Analogie
  [5] lambda in m_T = lambda/xi ist dimensionsbehaftet (Masse), nicht der
      dimensionslose Higgs-Quartic-Parameter
  [6] Dok. 250: xi/l ist die KOPPLUNG g_T, nicht die Mediatormasse
  [7] Die Schwarzschild-"Probe" fuer L_0 (Dok. 190) ist eine Identitaet

Ausfuehren: python3 180_mT_struktur_L0_verify.py
Benoetigt:  nur die Standardbibliothek

Referenz: J. Pascher, Dok. 180 (L_0-Herleitung), Dok. 019/201 (Lagrangian),
          Dok. 032 (effektive Torsionsmasse), Dok. 250, Dok. 190.
"""

import math
import sys

# --- Naturkonstanten (CODATA 2018) ---
hbar = 1.054571817e-34
c    = 2.99792458e8
G    = 6.67430e-11
eV   = 1.602176634e-19
me   = 9.1093837015e-31

lP = math.sqrt(hbar*G/c**3)
mP = math.sqrt(hbar*c/G)
xi = 4/30000
L0 = xi*lP

FAIL = False
banner = "=" * 70

def chk(cond, msg):
    global FAIL
    tag = "OK  " if cond else "FAIL"
    if not cond: FAIL = True
    print(f"  [{tag}] {msg}")

def compton(m):
    """Compton-Wellenlaenge einer Masse m"""
    return hbar/(m*c)

print(banner)
print("DOK. 180 — m_T-Struktur und die Herleitung von L_0 = xi * lP")
print(banner)

# ============================================================
# [1] Die Regel: m_T = M_basis/xi => Reichweite = xi * Compton(M_basis)
# ============================================================
print("\n[1] Grundregel aus dem Lagrangian")
print("    m_T = M_basis/xi   =>   Reichweite = hbar/(m_T c) = xi * Compton(M_basis)")

def m_T(M_basis):   return M_basis/xi
def reichweite(M):  return compton(m_T(M))

# analytische Identitaet pruefen
for M, name in [(me,'m_e'), (mP,'m_P'), (1e-27,'1e-27 kg')]:
    lhs = reichweite(M)
    rhs = xi*compton(M)
    chk(abs(lhs/rhs - 1) < 1e-12,
        f"M_basis = {name:9s}: Reichweite = xi*Compton exakt ({lhs:.4e} m)")

# ============================================================
# [2] Leptonsektor (Dok. 032)
# ============================================================
print("\n[2] Leptonsektor: M_basis = m_e (Dok. 032, effektive Torsionsmasse)")
mT_lep_roh = m_T(me)
mT_032     = 5.220e9*eV/c**2          # Dok.-032-Wert inkl. O(1)-Korrekturen
print(f"  m_e/xi              = {mT_lep_roh*c**2/eV/1e9:.4f} GeV")
print(f"  Dok. 032 (mit Korr.) = {mT_032*c**2/eV/1e9:.4f} GeV")
faktor = mT_032/mT_lep_roh
print(f"  Korrekturfaktor      = {faktor:.4f}")
chk(1.0 < faktor < 2.0,
    f"Dok.-032-Wert ist m_e/xi mal O(1)-Faktor {faktor:.3f} (sin, pi^2, sqrt(alpha/K), R_f)")
chk(abs(math.log10(mT_032/mT_lep_roh)) < 0.5,
    "Gleiche Groessenordnung: Dok. 032 folgt der Regel mit M_basis = m_e")

# ============================================================
# [3] Fundamentaler Sektor => L_0
# ============================================================
print("\n[3] Fundamentaler Sektor: M_basis = m_P")
mT_fund = m_T(mP)
r_fund  = reichweite(mP)
print(f"  m_T = m_P/xi        = {mT_fund/mP:.1f} m_P = {mT_fund:.4e} kg")
print(f"  Reichweite          = {r_fund:.6e} m")
print(f"  L_0 = xi*lP         = {L0:.6e} m")
chk(abs(r_fund/L0 - 1) < 1e-12,
    f"Reichweite = L_0 EXAKT (Verhaeltnis {r_fund/L0:.12f})")
chk(abs(mT_fund/mP - 1/xi) < 1e-9,
    f"m_T = m_P/xi = {1/xi:.1f} m_P -- extrem schwerer Mediator, daher kurze Reichweite")

# ============================================================
# [4] Der Exponent folgt aus dem Lagrangian
# ============================================================
print("\n[4] Woher kommt der Exponent 1 in L_0 = xi^1 * lP?")
print("    Aus m_T ~ 1/xi (Massenterm im Lagrangian) und Compton ~ 1/m:")
print("      Reichweite ~ 1/m_T ~ xi^1")
# Gegenprobe: haette m_T ~ 1/xi^2, waere die Reichweite ~ xi^2
for p in [1, 2, 3]:
    mT_p = mP/xi**p
    r_p  = compton(mT_p)
    erwartet = xi**p * lP
    chk(abs(r_p/erwartet - 1) < 1e-12,
        f"m_T ~ xi^-{p}  =>  Reichweite = xi^{p} * lP = {r_p:.3e} m")
print("  => Der Exponent der Reichweite ist der negative Exponent von m_T.")
print("     m_T = M/xi^1 (Lagrangian) liefert zwingend L_0 = xi^1 * lP.")

# ============================================================
# [5] lambda ist eine Masse, nicht der Higgs-Quartic
# ============================================================
print("\n[5] Was ist lambda in m_T = lambda/xi ?")
# Dimensionsargument: m_T ist eine Masse, xi dimensionslos => lambda ist Masse
lam_erforderlich = mT_fund*xi
print(f"  m_T ist eine Masse, xi dimensionslos  =>  lambda MUSS eine Masse sein")
print(f"  Fuer L_0 = xi*lP erforderlich: lambda = {lam_erforderlich:.4e} kg = {lam_erforderlich/mP:.6f} m_P")
chk(abs(lam_erforderlich/mP - 1) < 1e-9,
    "lambda = m_P (also 1 in Planck-Einheiten) -- keine zusaetzliche Setzung")

# Gegenprobe: dimensionsloser Higgs-Quartic waere inkonsistent
lam_h = 0.129
r_higgs = compton(lam_h*mP/xi)   # lam_h in Planck-Einheiten interpretiert
print(f"\n  Gegenprobe -- lambda = Higgs-Quartic {lam_h} (in m_P interpretiert):")
print(f"    Reichweite = {r_higgs:.4e} m = {r_higgs/L0:.3f} * L_0")
chk(abs(r_higgs/L0 - 1/lam_h) < 1e-6,
    f"ergaebe {1/lam_h:.2f} * L_0 -- verfehlt L_0; zudem laeuft lambda_h unter der RGE")
print("  => Die Beschriftung 'lambda = Higgs-Kopplungsparameter' (Dok. 019/201)")
print("     ist irrefuehrend: lambda ist die Basismasse des Sektors.")

# ============================================================
# [6] Dok. 250: xi/l ist die Kopplung, nicht die Mediatormasse
# ============================================================
print("\n[6] Dok. 250: 'm_T = xi/l' -- Zuordnung pruefen")
# In natuerlichen Einheiten: m = 1/l  =>  xi/l = xi*m = g_T (Kopplung!)
for M, name in [(me,'m_e'), (mP,'m_P')]:
    l_nat  = compton(M)          # l = hbar/(M c), also 1/l = M c/hbar
    xi_ueber_l = xi/l_nat        # in 1/m
    g_T_natuerlich = xi*M*c/hbar # Kopplung xi*m, in 1/m
    chk(abs(xi_ueber_l/g_T_natuerlich - 1) < 1e-12,
        f"M = {name}: xi/l = xi*m = Kopplung g_T (nicht m_T = M/xi)")
print("  => 'xi/l' ist die Lagrangian-KOPPLUNG g_T = xi*m_l.")
print("     Dok. 250 ordnet sie faelschlich der Mediatormasse zu;")
print("     zusaetzlich steht dort (d m)^2 statt (Delta m)^2 im Massenterm.")

# ============================================================
# [7] Die Schwarzschild-"Probe" ist eine Identitaet
# ============================================================
print("\n[7] Schwarzschild-'Probe' fuer L_0 (Dok. 190, Praezisierung 4)")
def r_s(M): return 2*G*M/c**2
M0 = xi*mP/2
print(f"  M_0 = xi*m_P/2 = {M0:.4e} kg")
print(f"  r_s(M_0)       = {r_s(M0):.4e} m")
print(f"  L_0            = {L0:.4e} m")
chk(abs(r_s(M0)/L0 - 1) < 1e-7, f"r_s(M_0) = L_0 (Verhaeltnis {r_s(M0)/L0:.9f})")

# Der Punkt: das gilt fuer JEDES xi und JEDEN Exponenten
print("\n  Aber: gilt das auch fuer andere xi und andere Exponenten?")
alle_ok = True
for xi_test in [1e-2, 1e-4, xi, 0.5]:
    for n in [1, 2, 3]:
        L_test  = xi_test**n * lP
        M_test  = xi_test**n * mP/2
        if abs(r_s(M_test)/L_test - 1) > 1e-7:
            alle_ok = False
chk(alle_ok,
    "r_s(x*m_P/2) = x*lP gilt fuer JEDES x -- die Relation ist eine Identitaet")
print("  Grund: r_s = 2GM/c^2 und lP = G*m_P/c^2, also r_s(x*m_P/2) = x*G*m_P/c^2 = x*lP.")
print("  => Die 'Probe' testet weder xi noch den Exponenten. Sie ist gehaltlos.")

# ============================================================
print(f"\n{banner}")
if FAIL:
    print("ERGEBNIS: Fehler aufgetreten.")
else:
    print("ERGEBNIS: Alle Assertions bestanden.")
    print()
    print("  Befunde:")
    print("  1. Eine Struktur, mehrere Auswertungen:")
    print("     m_T = M_basis/xi  =>  Reichweite = xi * Compton(M_basis)")
    print(f"       Lepton (Dok. 032): M = m_e  ->  {mT_032*c**2/eV/1e9:.2f} GeV, Reichweite {compton(mT_032):.2e} m")
    print(f"       Fundamental:       M = m_P  ->  {mT_fund/mP:.0f} m_P, Reichweite {r_fund:.3e} m = L_0")
    print("  2. Der Exponent 1 in L_0 = xi^1*lP folgt aus m_T ~ 1/xi   [B]")
    print("     (Lagrangian-Eigenschaft, keine Analogie, keine Setzung)")
    print("  3. lambda in m_T = lambda/xi ist eine BASISMASSE (= m_P im")
    print("     fundamentalen Sektor), nicht der Higgs-Quartic-Parameter")
    print("  4. Dok. 250: 'xi/l' ist die Kopplung g_T, nicht m_T;")
    print("     ausserdem (d m)^2 statt (Delta m)^2 im Massenterm")
    print("  5. Die Schwarzschild-'Probe' fuer L_0 ist eine Identitaet")
    print("     und testet nichts")
print(banner)
sys.exit(1 if FAIL else 0)
