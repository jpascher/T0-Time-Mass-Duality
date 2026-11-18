#!/usr/bin/env python3
"""Prüfskript zu Dok. 397: Bell-Verletzung durch Synchronisation.

Prüft die Zahlen, auf die sich die Einordnung der Tröpfchen-Arbeiten stützt:
CHSH-Grenzen (klassisch, Tsirelson, algebraisch), die Lage der berichteten
Werte 2,49 / 2,85 / 3,15 relativ zu diesen Grenzen, die Born-Quotienten aus
Dok. 230 als Quelle der Korrelation -cos(a-b), das lokale Modell mit
A = sgn(z - lambda) (Sägezahn, S = 2), ein messabhängiges deterministisches
Modell (S bis 4) und die Kopplungsstärke aus Dok. 328 (K_eff = 2 pi xi)
gegen das Adler-Fangkriterium.

Aufruf aus der Repo-Wurzel:
    python3 2/python/Dok397_Skripte/pruef_397_bell_synchronisation.py
"""
import math
import random

ok = n = 0


def check(name, cond, info=""):
    global ok, n
    n += 1
    ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FEHLER'}] {name}" + (f"  ({info})" if info else ""))


def chsh(E, a, a2, b, b2):
    return E(a, b) + E(a2, b) + E(a, b2) - E(a2, b2)


print("1. Grenzen des CHSH-Werts")
ts = 2 * math.sqrt(2)
check("Tsirelson-Grenze 2*sqrt(2) = 2,828", abs(ts - 2.8284) < 1e-4, f"{ts:.4f}")
check("algebraische Obergrenze 4 (jede Korrelation |E| <= 1)", 4 * 1 == 4)

print("\n2. Berichtete Werte gegen die Grenzen")
werte = {"Papatryfonos et al., statisch": 2.49,
         "Lopez et al., dynamisch (Maximum)": 2.85,
         "Lopez et al., statisch (Mittel)": 3.15}
check("2,49 verletzt CHSH, liegt unter Tsirelson", 2 < werte["Papatryfonos et al., statisch"] < ts)
check("2,85 liegt über Tsirelson (um 0,02)", werte["Lopez et al., dynamisch (Maximum)"] > ts,
      f"Differenz {werte['Lopez et al., dynamisch (Maximum)'] - ts:.3f}")
check("3,15 liegt deutlich über Tsirelson", werte["Lopez et al., statisch (Mittel)"] - ts > 0.3,
      f"Differenz {werte['Lopez et al., statisch (Mittel)'] - ts:.3f}")
# Standardfehler aus der Arbeit: 1,5e-3 bei n = 1000
sig = 1.5e-3
z = (3.15 - ts) / sig
check("3,15 liegt über 200 Standardfehler über Tsirelson", z > 200, f"{z:.0f} sigma")

print("\n3. Born-Quotient aus Dok. 230 erzeugt -cos(a-b) und genau Tsirelson")
# Dok. 230: |alpha|^2 = (1+z)/2 ist der Achsenanteil; für den Singulett-Fall ist
# der Anteil gleicher Ausgänge sin^2((a-b)/2), der ungleicher cos^2((a-b)/2).
def E_born(a, b):
    p_gleich = math.sin((a - b) / 2) ** 2
    return p_gleich - (1 - p_gleich)

check("E_Born(a,b) = -cos(a-b) auf einem Gitter", all(abs(E_born(x, y) + math.cos(x - y)) < 1e-12
      for x in [0, 0.3, 1.1, 2.0] for y in [0, 0.7, 1.9, 3.0]))
S_q = abs(chsh(E_born, 0, math.pi / 2, math.pi / 4, -math.pi / 4))
check("Winkel a=0, a'=90, b=45, b'=-45 Grad ergeben |S| = 2*sqrt(2)", abs(S_q - ts) < 1e-12, f"{S_q:.6f}")
best = 0.0
for i in range(0, 72):
    for j in range(0, 72):
        for k in range(0, 72, 3):
            a, a2, b = 0.0, i * math.pi / 36, j * math.pi / 36
            b2 = k * math.pi / 36
            best = max(best, abs(chsh(E_born, a, a2, b, b2)))
check("Gittersuche über Winkel: Born-Korrelation überschreitet Tsirelson nie", best <= ts + 1e-9,
      f"max {best:.6f}")

print("\n4. Lokales Modell A = sgn(z - lambda) mit gemeinsamem lambda (Sägezahn)")
# Klassisches Beispiel: lambda gleichverteilt auf dem Kreis, A = sgn(cos(lambda - a)),
# B = -sgn(cos(lambda - b)). Ergibt E = -1 + 2|a-b|/pi, also höchstens S = 2.
random.seed(1)
lams = [random.uniform(0, 2 * math.pi) for _ in range(200000)]

def sgn(x):
    return 1.0 if x >= 0 else -1.0

def E_lokal(a, b):
    return sum(sgn(math.cos(l - a)) * -sgn(math.cos(l - b)) for l in lams) / len(lams)

def E_saege(a, b):
    d = abs(a - b) % (2 * math.pi)
    d = min(d, 2 * math.pi - d)
    return -1 + 2 * d / math.pi

check("Simulation folgt der Sägezahnkurve -1 + 2|a-b|/pi", all(abs(E_lokal(x, y) - E_saege(x, y)) < 0.01
      for x, y in [(0, 0.5), (0, 1.2), (0.4, 2.0)]))
S_lok = abs(chsh(E_saege, 0, math.pi / 2, math.pi / 4, -math.pi / 4))
check("Sägezahn bei den Tsirelson-Winkeln: |S| = 2 (Bell-Grenze erreicht, nicht überschritten)",
      abs(S_lok - 2) < 1e-12, f"{S_lok:.6f}")
best_l = 0.0
for i in range(0, 72):
    for j in range(0, 72):
        for k in range(0, 72, 3):
            best_l = max(best_l, abs(chsh(E_saege, 0.0, i * math.pi / 36, j * math.pi / 36, k * math.pi / 36)))
check("Gittersuche: Sägezahn bleibt bei |S| <= 2", best_l <= 2 + 1e-9, f"max {best_l:.6f}")

print("\n5. Messabhängiges deterministisches Modell: S bis 4")
# Hängt die Verteilung von lambda von den Einstellungen ab, p(lambda|a,b) != p(lambda),
# so kann jede Korrelationstabelle erzeugt werden. Beispiel: für (a2,b2) wird
# lambda so gewählt, dass die Ausgänge ungleich sind, sonst gleich.
def E_messabh(x, y):
    return -1.0 if (x, y) == ("a2", "b2") else 1.0

S_m = chsh(E_messabh, "a", "a2", "b", "b2")
check("Messabhängigkeit erlaubt S = 4 (deterministisch, lokal in den Ausgängen)", S_m == 4, f"S = {S_m}")
check("Tsirelson ist daher keine Folge der Messabhängigkeit allein", S_m > ts)

print("\n6. Kopplungsstärke: Tröpfchen gegen FFGFT (Dok. 328)")
xi = 4 / 30000
K_eff = 2 * math.pi * xi
check("K_eff = 2 pi xi = 8,4e-4 (Dok. 328)", abs(K_eff - 8.38e-4) < 0.01e-4, f"{K_eff:.3e}")
# Adler: Einrasten genau für |dw| <= eps. Mit eps/omega = K_eff ist der Fangbereich
# relativ 8,4e-4, für Ordnung 1/2 nach Dok. 328 nur 5,6e-8.
dOm_12 = 2 * (K_eff / 2) ** 2 / (2 * math.pi)
check("Arnold-Zunge 1/2 bei K_eff: 5,6e-8 (Dok. 328)", abs(dOm_12 - 5.6e-8) < 0.1e-8, f"{dOm_12:.2e}")
# Tröpfchenmodell: Wellenamplitude R ~ 5 bei Dämpfung 1 (dimensionslos), also Kopplung O(1).
R_trop = 5.29
check("Tröpfchenkopplung R = 5,29 liegt rund 6000-fach über K_eff", R_trop / K_eff > 6000,
      f"Faktor {R_trop / K_eff:.0f}")

print("\n7. Relativer Abstand des dynamischen Maximums zu Tsirelson")
rel = (2.85 - ts) / ts
check("2,85 liegt 0,76 % über Tsirelson", abs(rel - 0.0076) < 0.0002, f"{rel*100:.2f} %")

print(f"\nErgebnis: {ok}/{n} PASS")
raise SystemExit(0 if ok == n else 1)
