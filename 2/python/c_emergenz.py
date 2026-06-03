import numpy as np

# ============================================================================
# c als Umrechnungsfaktor, nicht als Eingabe -- korrigierte Layer-1/2-Kette
#
# AUSGANGSPUNKT: Korrektur eines fruehen Denkfehlers. Es ist FALSCH, die
# Planck-Zeit ueber t_P = sqrt(hbar G/c^5) einzufuehren -- diese Formel
# enthaelt c selbst, was die Frage zirkulaer machen wuerde. FFGFT braucht
# das NICHT.
#
# KERN (Dok 013 §Speed of Light; Dok 134 c=L/T; T*m=1):
#   - In Layer 1 (kompaktes T^4, reine Verhaeltnisse) gilt T~ * m = 1.
#     Die Zeit T~ = 1/m folgt DIREKT aus der Masse (= Energie = inverse
#     Laenge). Laenge und Zeit sind DIESELBE Groesse. Das IST die Aussage
#     "c = 1" -- nicht eine zusaetzliche Konstante, sondern L == T.
#   - c kommt in Layer 1 NICHT vor.
#   - c entsteht erst in Layer 2, wenn man Laenge (Meter) und Zeit (Sekunde)
#     als GETRENNTE Einheiten einfuehrt. Dann ist das Verhaeltnis Meter/Sekunde
#     der Umrechnungsfaktor, den wir "c" nennen. Der Zahlenwert 299792458 ist
#     die DEFINITION des Meters relativ zur Sekunde -- Einheiten-Konvention.
#
# Parallel zu vakuum_emergenz.py: c spielt fuer die Laenge/Zeit-Trennung
# dieselbe Rolle wie hbar*c fuer die Vakuum-Energiedichte -- beides sind
# PROJEKTIONSFAKTOREN des Layer-1 -> Layer-2 Uebergangs (Embedding-Preis,
# Dok 261), nicht emergente Substanzen und keine fraktale Geschwindigkeits-
# Rekursion mit "Fixpunkt c" (eine solche waere zirkulaer: sie muesste c
# in die Gleichung hineinstecken).
# ============================================================================

xi = 4/30000.0

print("="*70)
print("c als Umrechnungsfaktor (Layer-2-Projektion), nicht als Eingabe")
print("="*70)

# --- LAYER 1: c-frei ---
print("\n[LAYER 1]  kompaktes T^4, reine Verhaeltnisse -- c kommt NICHT vor")
print("-"*70)
print("""  T~ * m = 1   =>  Zeit T~ = 1/m   (aus der Masse, OHNE c)
  m = E = 1/L  (in natuerlichen Einheiten dieselbe Groesse)
  => Laenge L und Zeit T~ sind IDENTISCH. Das bedeutet "c = 1".
  Die Gravitationskonstante folgt c-frei (Dok 012/013):
     G_nat = xi^2 / (4 m_char)
     l_P   = sqrt(G_nat)            -- enthaelt KEIN c
     t_P   = l_P                    -- weil L == T, KEIN c noetig
""")

# Demonstration der c-Freiheit (alle Groessen als reine Zahlen / nat. Einheiten)
# m_char hier symbolisch = 1 (reine-Verhaeltnis-Ebene); es geht um die STRUKTUR.
m_char = 1.0
G_nat = xi**2/(4*m_char)
l_P_nat = np.sqrt(G_nat)
t_P_nat = l_P_nat   # L == T
print(f"  Beispiel (m_char=1, nat. Einh.): G_nat={G_nat:.4e}, l_P=t_P={l_P_nat:.4e}")
print(f"  -> l_P/t_P = {l_P_nat/t_P_nat:.1f} = 1 = c  (in Layer 1 trivial, KEINE Info)")

# --- UEBERGANG: Meter/Sekunde-Trennung ---
print("\n[UEBERGANG]  Dekompaktifizierung = Trennung von Meter und Sekunde")
print("-"*70)
print("""  Solange L == T, gibt es nur EINE Skala und c=1 ist trivial.
  Fuehrt man zwei SEPARATE Einheiten ein -- Meter fuer L, Sekunde fuer T --
  dann braucht man einen Umrechnungsfaktor zwischen ihnen. DIESER Faktor
  ist c. Er entsteht durch die Einheiten-TRENNUNG, nicht aus der Physik
  einer Geschwindigkeit.""")

# --- LAYER 2: c als Meter/Sekunde-Faktor ---
print("\n[LAYER 2]  c = Meter/Sekunde-Umrechnungsfaktor")
print("-"*70)
c_SI = 299792458.0
print(f"  c = {c_SI:.0f} m/s")
print("""  Der Zahlenwert ist KEINE xi-Vorhersage, sondern die Definition des
  Meters relativ zur Sekunde (SI-Reform 2019 fixierte c exakt). Andere
  Laengen-/Zeiteinheiten -> anderer Zahlenwert, gleiche Physik. c bestimmt
  NUR den Umrechnungsfaktor.""")

# --- der Punkt ---
print("\n" + "-"*70)
print("DER PUNKT:")
print("-"*70)
print("""  c ist weder ein freier Parameter noch ein 'Fixpunkt einer fraktalen
  Geschwindigkeits-Rekursion' (das waere zirkulaer). c ist der
  Umrechnungsfaktor Meter<->Sekunde, der bei der Trennung der in Layer 1
  identischen Groessen L und T entsteht -- der Embedding-Preis der
  Dekompaktifizierung (Dok 261).

  Dies ist DIESELBE Rolle wie hbar*c bei der Vakuum-Energiedichte
  (vakuum_emergenz.py): beide sind Layer-2-Projektionsfaktoren, nicht
  emergente Substanzen. Das ist die gesuchte Einheit -- sie liegt in der
  PROJEKTION, nicht in einer Geschwindigkeits-Iteration.
""")

# --- Abgrenzung zur c-aus-xi-Darstellung in Dok 013 ---
print("="*70)
print("Warum auch t_P = sqrt(hbar G/c^5) NICHTS begruendet -- nur umrechnet:")
print("="*70)
print("""  Die Planck-Zeit-Formel t_P = sqrt(hbar G/c^5) sieht aus wie eine
  Herleitung einer Zeitskala, ist aber KEINE. Sie ist die Definitions-
  gleichung, die die bereits feststehende Skala (in Layer 1: T~ = 1/m,
  c-frei) in SI-SEKUNDEN ausdrueckt. hbar, G, c treten darin nur als
  UMRECHNUNGSFAKTOREN auf, nicht als physikalische Eingaben.

  Mein frueherer Fehler war, diese Formel als kausalen Schritt zu lesen
  ('sie fuehrt c ein'). Das ist falsch: sie KALIBRIERT nur die Einheit
  Sekunde. Die physikalische Skala steht schon vorher fest.

  Damit ist t_P = sqrt(hbar G/c^5) das DRITTE Beispiel desselben Prinzips:
     rho_vac:  dimensionslose Modenzahl  --[* hbar c]-->  J/m^3
     c:        L == T (eine Skala)       --[Meter/Sekunde]-->  m/s
     t_P:      Skala T~ = 1/m            --[sqrt(hbar G/c^5)]--> Sekunden
  In allen drei Faellen ist die Physik in Layer 1 c-frei und einheitenlos;
  der 'Konstanten'-Ausdruck ist AUSSCHLIESSLICH die SI-Umrechnung. Keine
  dieser Formeln begruendet eine Groesse -- sie projizieren nur.
""")

print("="*70)
print("Verhaeltnis zur 'c aus xi'-Darstellung (Dok 013):")
print("="*70)
print("""  Dok 013 zeigt, dass der c-Zahlenwert konsistent als l_P/t_P aus der
  xi-Geometrie DARSTELLBAR ist ("dual: Konvention + geometrisches
  Verhaeltnis"). Das ist eine Konsistenz-Aussage, KEINE einheitenfreie
  Vorhersage von 299792458 (das kann es nicht geben -- der Wert haengt an
  der Meter-Definition). Beide Sichten sind vertraeglich: G und die
  Laengenskala folgen aus xi (c-frei); c ist der Faktor, der diese eine
  Skala auf zwei getrennte Einheiten abbildet.
""")
