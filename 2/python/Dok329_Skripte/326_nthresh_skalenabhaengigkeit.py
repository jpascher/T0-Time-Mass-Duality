#!/usr/bin/env python3
"""
326_nthresh_skalenabhaengigkeit.py
==================================
Ergaenzung zu Dok. 326: Numerischer Test der Frage, ob Matzkes
Stabilitaetsschwelle n_thresh = 6,41 Bit eine universelle Zahl ist
oder eine verdeckte Skalenwahl.

Aufbau der Pruefung:
  [1] Matzkes Kette nachrechnen: m_bit = mP*ln2/(2pi) => n_thresh = 2pi/(sqrt2*ln2)
  [2] Die implizierte Kollapsmasse extrahieren (skalenunabhaengig?)
  [3] n_thresh mit FFGFT-Bitenergie E_bit(L) = hbar*c/L als Funktion von L
  [4] Die Skala bestimmen, bei der die FFGFT-Formel Matzkes Zahl liefert
  [5] n_thresh an physikalisch relevanten Skalen auswerten
  [6] Gegenprobe: ist n_thresh invariant unter Skalenwechsel?

Hauptbefund (siehe Ausgabe):
  Die Kollapsmasse M_coll = mP/sqrt(2) ist skalenunabhaengig [B].
  n_thresh = M_coll/m_bit haengt dagegen vollstaendig am Bitwert.
  Mit E_bit(L) = hbar*c/L folgt exakt n_thresh(L) = L/(sqrt2*lP) --
  eine LINEARE Funktion der Skala, kein invarianter Zahlenwert.
  Matzkes 6,41 entspricht exakt der Skala L = 2*pi*lP/ln2 = 9,0647*lP.

Ausfuehren: python3 326_nthresh_skalenabhaengigkeit.py
Benoetigt:  nur die Standardbibliothek

Referenz: J. Pascher, Dok. 326 (Matzke-Vergleich), Dok. 325, Dok. 257;
          D. Matzke, Black Holes from Hyperbits, IPI 2026.
"""

import math
import sys

# --- Naturkonstanten (CODATA 2018) ---
hbar = 1.054571817e-34      # J s
c    = 2.99792458e8         # m/s
G    = 6.67430e-11          # m^3 kg^-1 s^-2
kB   = 1.380649e-23         # J/K

lP = math.sqrt(hbar*G/c**3)         # Plancklaenge
mP = math.sqrt(hbar*c/G)            # Planckmasse
TP = math.sqrt(hbar*c**5/G)/kB      # Plancktemperatur

xi = 4/30000
L0 = xi*lP                          # FFGFT-Minimalskala (Dok. 180)
E0 = 7.348e6                        # eV, charakteristische Energie (Dok. 257)
eV = 1.602176634e-19

FAIL = False
banner = "=" * 70

def chk(cond, msg):
    global FAIL
    tag = "OK  " if cond else "FAIL"
    if not cond: FAIL = True
    print(f"  [{tag}] {msg}")

print(banner)
print("DOK. 326 — Ist n_thresh = 6,41 universell oder eine Skalenwahl?")
print(banner)

# ============================================================
# [1] Matzkes Kette nachrechnen
# ============================================================
print("\n[1] Matzkes Kette: Landauer bei der Planck-KMS-Temperatur -> m_bit -> n_thresh")

# Die angesetzte Temperatur ist nicht T_P selbst, sondern die KMS-Temperatur
# der Planckskala: T_KMS = T_P/(2*pi) (2*pi aus der KMS-Periodizitaet,
# dieselbe wie in Unruh/Hawking, vgl. Dok. 325).
T_KMS = TP/(2*math.pi)
E_bit_M = kB * T_KMS * math.log(2)       # J
m_bit_M = E_bit_M / c**2                 # kg
m_bit_analytisch = mP * math.log(2) / (2*math.pi)

print(f"  T_P                = {TP:.4e} K")
print(f"  T_KMS = T_P/(2pi)  = {T_KMS:.4e} K")
print(f"  E_bit = kB*T_KMS*ln2 = {E_bit_M:.4e} J")
print(f"  m_bit              = {m_bit_M:.4e} kg = {m_bit_M/mP:.6f} mP")
print(f"  analytisch mP*ln2/(2pi) = {m_bit_analytisch:.4e} kg")

chk(abs(m_bit_M/m_bit_analytisch - 1) < 1e-9,
    f"m_bit = mP*ln2/(2pi) reproduziert (Verhaeltnis {m_bit_M/m_bit_analytisch:.9f})")

n_thresh_M = 2*math.pi/(math.sqrt(2)*math.log(2))
print(f"  n_thresh = 2pi/(sqrt2*ln2) = {n_thresh_M:.6f} Bit")
chk(abs(n_thresh_M - 6.4097) < 1e-3, f"n_thresh = {n_thresh_M:.4f} (Matzkes Wert 6,41)")

# ============================================================
# [2] Die implizierte Kollapsmasse — skalenunabhaengig?
# ============================================================
print("\n[2] Kollapsmasse aus Compton = Schwarzschild (rein geometrisch)")

# Compton = Schwarzschild:  hbar/(M c) = 2GM/c^2  =>  M = sqrt(hbar*c/(2G)) = mP/sqrt2
M_coll_geom = math.sqrt(hbar*c/(2*G))
print(f"  Compton = Schwarzschild  =>  M_coll = mP/sqrt(2) = {M_coll_geom:.4e} kg")

# Gegenprobe: folgt dasselbe aus n_thresh * m_bit?
M_coll_bits = n_thresh_M * m_bit_M
print(f"  n_thresh * m_bit         =                        {M_coll_bits:.4e} kg")
chk(abs(M_coll_bits/M_coll_geom - 1) < 1e-9,
    f"M_coll identisch (Verhaeltnis {M_coll_bits/M_coll_geom:.9f})")
chk(abs(M_coll_geom/mP - 1/math.sqrt(2)) < 1e-12,
    f"M_coll = mP/sqrt(2) = {M_coll_geom/mP:.6f} mP -- rein geometrisch, KEIN Bitwert enthalten")

print("  => Die Kollapsbedingung selbst ist skalenunabhaengig [B].")
print("     n_thresh = M_coll/m_bit haengt dagegen VOLLSTAENDIG am Bitwert.")

# ============================================================
# [3] n_thresh mit FFGFT-Bitenergie E_bit(L) = hbar*c/L
# ============================================================
print("\n[3] FFGFT-Bitenergie: E_bit(L) = hbar*c/L  =>  n_thresh(L)")

def m_bit_ffgft(L):
    """Bitmasse bei Skala L: E_bit = hbar*c/L, m = E/c^2"""
    return hbar/(c*L)

def n_thresh_ffgft(L):
    """Bitzahl an der Kollapsschwelle bei Skala L"""
    return M_coll_geom / m_bit_ffgft(L)

# analytisch: n_thresh(L) = M_coll*c*L/hbar = (mP/sqrt2)*c*L/hbar = L/(sqrt2*lP)
for L_test in [lP, 5*lP, 10*lP]:
    num = n_thresh_ffgft(L_test)
    ana = L_test/(math.sqrt(2)*lP)
    chk(abs(num/ana - 1) < 1e-12,
        f"L = {L_test/lP:5.1f} lP: n_thresh = {num:9.4f} = L/(sqrt2*lP) [analytisch bestaetigt]")

print("  => n_thresh(L) = L/(sqrt(2)*lP) — LINEAR in der Skala.")

# ============================================================
# [4] Bei welcher Skala liefert die FFGFT-Formel Matzkes Zahl?
# ============================================================
print("\n[4] Welche Skala steckt implizit in Matzkes Bitwert?")

L_matzke = hbar/(c*m_bit_M)                    # aus m_bit = hbar/(c*L)
L_analyt = 2*math.pi*lP/math.log(2)            # analytisch erwartet

print(f"  Aus m_bit = hbar/(c*L):  L = {L_matzke:.4e} m = {L_matzke/lP:.4f} lP")
print(f"  Analytisch 2*pi*lP/ln2:  L = {L_analyt:.4e} m = {L_analyt/lP:.4f} lP")
chk(abs(L_matzke/L_analyt - 1) < 1e-9,
    f"Matzkes impliziter Massstab: L = 2*pi*lP/ln2 = {L_matzke/lP:.4f} lP")
chk(abs(n_thresh_ffgft(L_matzke) - n_thresh_M) < 1e-9,
    f"Bei dieser Skala gibt die FFGFT-Formel exakt {n_thresh_ffgft(L_matzke):.4f} = Matzkes Wert")

print("  => Der 'universelle' Bitwert IST die FFGFT-Bitenergie,")
print("     ausgewertet bei einer bestimmten Skala (9,06 Plancklaengen).")
print("     Die Universalitaet ist eine verdeckte Skalenwahl.")

# ============================================================
# [5] n_thresh an physikalisch relevanten Skalen
# ============================================================
print("\n[5] n_thresh an verschiedenen Skalen des Korpus")

L_e = hbar*c/(E0*eV)                # charakteristische FFGFT-Laenge (E0 = 7,348 MeV)
skalen = [
    ("L_0 = xi*lP (FFGFT-Minimalskala, Dok. 180)", L0),
    ("lP  (Plancklaenge)",                          lP),
    ("2pi*lP/ln2 (Matzkes implizite Skala)",        L_matzke),
    ("1 fm (Kernphysik)",                           1e-15),
    ("L_e = hbar*c/E0 (Dok. 257)",                  L_e),
    ("1 nm (Atomphysik)",                           1e-9),
]
print(f"  {'Skala':<44} {'L [m]':>11}  {'n_thresh':>14}")
for name, L in skalen:
    print(f"  {name:<44} {L:>11.3e}  {n_thresh_ffgft(L):>14.4e}")

n_min = n_thresh_ffgft(L0)
n_max = n_thresh_ffgft(1e-9)
spanne = n_max/n_min
chk(spanne > 1e20,
    f"Spannweite ueber diese Skalen: Faktor {spanne:.3e} — n_thresh ist KEINE Konstante")

# ============================================================
# [6] Gegenprobe: waere n_thresh invariant, muesste m_bit skalieren
# ============================================================
print("\n[6] Gegenprobe: was muesste gelten, damit n_thresh invariant ist?")

print("  n_thresh = M_coll/m_bit ist genau dann skalenunabhaengig,")
print("  wenn m_bit skalenunabhaengig ist (M_coll ist es, siehe [2]).")
print("  Matzke setzt das per Landauer bei T_P/(2pi); FFGFT bestreitet es (A271-A273).")
print()
# Zeige: eine 10%-Aenderung der angesetzten Temperatur verschiebt n_thresh um 10%
for faktor in [0.5, 0.9, 1.0, 1.1, 2.0]:
    T_ansatz = faktor*T_KMS
    m_b = kB*T_ansatz*math.log(2)/c**2
    n_t = M_coll_geom/m_b
    print(f"  T = {faktor:4.1f} * T_KMS:  m_bit = {m_b/mP:.4f} mP,  n_thresh = {n_t:8.4f}")
n_half = M_coll_geom/(kB*0.5*T_KMS*math.log(2)/c**2)
chk(abs(n_half/n_thresh_M - 2.0) < 1e-9,
    f"n_thresh skaliert exakt invers zur angesetzten Temperatur (T/2 -> n*2)")
chk(abs(n_thresh_M - 6.4097) < 1e-3,
    "Nur die Wahl T = T_P/(2pi) liefert 6,41 — jede andere Temperatur eine andere Zahl")

# ============================================================
print(f"\n{banner}")
if FAIL:
    print("ERGEBNIS: Fehler aufgetreten.")
else:
    print("ERGEBNIS: Alle Assertions bestanden.")
    print()
    print("  Befund zur Frage 'ist n_thresh universell?':")
    print()
    print("  1. Die Kollapsbedingung (Compton = Schwarzschild) ist geometrisch")
    print(f"     und skalenunabhaengig: M_coll = mP/sqrt(2) = {M_coll_geom:.4e} kg  [B]")
    print("  2. n_thresh = M_coll/m_bit haengt vollstaendig am Bitwert.")
    print("  3. Mit E_bit(L) = hbar*c/L folgt exakt n_thresh(L) = L/(sqrt2*lP):")
    print("     LINEAR in der Skala, kein invarianter Zahlenwert.")
    print(f"  4. Matzkes 6,41 entspricht exakt L = 2*pi*lP/ln2 = {L_matzke/lP:.4f}*lP.")
    print("     Der 'universelle' Bitwert ist die FFGFT-Bitenergie bei DIESER Skala.")
    print(f"  5. Ueber die Skalen des Korpus variiert n_thresh um Faktor {spanne:.2e}.")
    print()
    print("  => Die Universalitaet von n_thresh = 6,41 ist eine verdeckte")
    print("     Skalenwahl, kein eigenstaendiges physikalisches Resultat. [B]")
    print("     Was invariant bleibt, ist die Kollapsmasse mP/sqrt(2) --")
    print("     und die braucht keinen Bitwert.")
print(banner)
sys.exit(1 if FAIL else 0)
