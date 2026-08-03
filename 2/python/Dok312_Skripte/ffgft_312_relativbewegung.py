#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT Dok. 312 — Pruefskript: Relativbewegung und Torus-Ruhesystem
Vier Pruefungen VOR dem Schreiben des Abschnitts:

P1  Bewegungshierarchie und gamma-Faktoren: bleibt alles lokal
    Standardkinematik (v << c)? Vertraegt sich die Vektorsumme der
    Hierarchie groessenordnungsmaessig mit dem gemessenen CMB-Dipol?
P2  Dipol-Konsistenz: liefert Delta-T/T des CMB-Dipols exakt v/c?
    (Das ist die Doppler-Ablesung des ausgezeichneten Systems.)
P3  Zwilling auf dem Torus: Windungs-Unterscheidung quantitativ —
    ist sie praktisch beobachtbar oder nur strukturell?
P4  Pruefsignaturen: (a) Matched-Circle-Versatzwinkel ~ beta,
    (b) Drift durch die Struktur pro Zeitzyklus.

Eingaben: Messwerte (Planck-Dipol, Bahngeschwindigkeiten) und die
Dok-312-Kette (L* = 2 pi R_H) [K|P20]. Identifikation Torus-System
= CMB-System bleibt [S] — hier wird nur geprueft, ob sie konsistent
und pruefbar waere.
"""

from math import sqrt, pi, sin, cos, radians, degrees

C   = 2.99792458e8
XI  = 4/30000
LAM_E = 3.8615926796e-13
H0  = (pi/2)*C*XI**10/LAM_E
R_H = C/H0
L_STAR = 2*pi*R_H
GYR = 3.155815e16
MPC = 3.0856775814913673e22

# ---------------------------------------------------------------
# P1 — Bewegungshierarchie
# ---------------------------------------------------------------
print("=== P1: Hierarchie der Bewegungen (lokal reine Kinematik) ===")
motions = [
    ("Erdrotation (Aequator)",        0.465e3),
    ("Erde um Sonne",                 29.78e3),
    ("Sonne um Galaxis",              233e3),
    ("Sonne rel. CMB (gemessen)",     369.82e3),
    ("Lokale Gruppe rel. CMB",        620e3),
]
print(f"{'Bewegung':<28} {'v [km/s]':>9} {'beta':>10} {'gamma-1':>11}")
for name, v in motions:
    b = v/C
    g1 = 1/sqrt(1-b*b) - 1
    print(f"{name:<28} {v/1e3:9.1f} {b:10.2e} {g1:11.2e}")
print("-> alle gamma-1 <= 2e-6: SRT-Störungsrechnung erster Ordnung,")
print("   Bewegung AUF der Massenlandkarte, kein Konflikt mit Statik.")

# Vektorsummen-Plausibilitaet (galaktische Koordinaten, nur Ordnung):
# Sonne->CMB-Apex (l,b)=(264.0,48.25); Sonne um Galaxis ~ (l,b)=(90,0);
# LG-Apex (l,b)=(271.9,29.6). Test: v_LG(rel CMB) ~ v_Sonne(rel CMB)
# minus Galaxisbahn-Anteil -> Betragspruefung der bekannten Zerlegung:
def vec(l, b, v):
    l, b = radians(l), radians(b)
    return (v*cos(b)*cos(l), v*cos(b)*sin(l), v*sin(b))
v_sun_cmb = vec(264.0, 48.25, 369.82)   # km/s
v_sun_gal = vec(90.0, 0.0, 233.0)       # Bahn um galaktisches Zentrum
v_gal_cmb = tuple(a-b for a,b in zip(v_sun_cmb, v_sun_gal))
mag = sqrt(sum(x*x for x in v_gal_cmb))
print(f"\nVektorprobe: |v(Galaxis rel. CMB)| = |v_sun_cmb - v_bahn| "
      f"= {mag:.0f} km/s")
print("   (Literaturwert Milchstrasse rel. CMB ~ 550 km/s: Ordnung OK;")
print("    exakte Zerlegung braucht LSR-Korrekturen — hier nur Ordnung.)")

# ---------------------------------------------------------------
# P2 — Dipol = Doppler-Ablesung des ausgezeichneten Systems
# ---------------------------------------------------------------
print("\n=== P2: CMB-Dipol als v/c-Ablesung ===")
T0    = 2.7255        # K (Monopol)
dT    = 3.3621e-3     # K (Dipolamplitude, Planck)
beta_dip = dT/T0
v_dip = beta_dip*C
print(f"Delta-T/T = {beta_dip:.4e}  ->  v = {v_dip/1e3:.1f} km/s")
print(f"gemessen (Planck, direkt): 369.82 km/s  ->  Abw. "
      f"{abs(v_dip/1e3-369.82)/369.82*100:.2f} %")
print("-> Der Dipol IST die Doppler-Ablesung eines ausgezeichneten")
print("   Ruhesystems; in der kompakten Lesart: Kandidat Torus-System.")
print("   Identifikation bleibt [S] — konsistent, nicht abgeleitet.")

# ---------------------------------------------------------------
# P3 — Zwilling auf dem Torus (Windungs-Unterscheidung)
# ---------------------------------------------------------------
print("\n=== P3: Zwilling auf dem Torus ===")
print(f"L* = {L_STAR:.3e} m = {L_STAR/MPC:.1f} Mpc")
for b in (0.5, 0.9, 0.99):
    g = 1/sqrt(1-b*b)
    t_lab = L_STAR/(b*C)              # Koordinatenzeit einer Umrundung
    tau   = t_lab/g                   # Eigenzeit des Reisenden
    print(f"beta={b:4.2f}: Umrundung t = {t_lab/GYR:7.1f} Gyr, "
          f"Eigenzeit tau = {tau/GYR:7.1f} Gyr, Defizit = "
          f"{(t_lab-tau)/GYR:6.1f} Gyr")
print("-> Windungszahl unterscheidet Systeme ABSOLUT (Topologie),")
print("   aber jede Umrundung dauert >= 92 Gyr: strukturell real,")
print("   praktisch unbeobachtbar. Nur globale Marker tragen.")

# ---------------------------------------------------------------
# P4 — Pruefsignaturen
# ---------------------------------------------------------------
print("\n=== P4: Pruefsignaturen ===")
beta = 369.82e3/C
print(f"(a) Matched-Circle-Versatz ~ beta = {beta:.3e} rad "
      f"= {degrees(beta)*60:.1f} Bogenminuten")
print("    Planck-Suchen arbeiten mit Grad-Aufloesung der Kreis-")
print("    statistik: 4 Bogenminuten Versatz in Dipolrichtung ist")
print("    eine SPEZIFISCHE, prinzipiell zugaengliche Signatur. [S]")
d_cycle = 369.82e3 * (2*pi/H0)
print(f"(b) Drift durch die Struktur pro Zeitzyklus tau = 2pi/H0:")
print(f"    d = v*tau = {d_cycle:.3e} m = {d_cycle/MPC:.1f} Mpc "
      f"= {d_cycle/L_STAR*100:.3f} % von L*")
d_lss = 369.82e3 * (13.8*GYR)
print(f"    Drift seit Rekombinations-Lichtlaufzeit (~13.8 Gyr): "
      f"{d_lss/MPC:.2f} Mpc = {d_lss/L_STAR*100:.4f} % von L*")
print("-> Drift winzig gegen L*: kein Selbstwiderspruch der")
print("   statischen Lesart durch unsere Eigenbewegung.")

print("\n=== Fazit ===")
print("P1 lokal reine Kinematik auf der Landkarte [K]")
print("P2 Dipol = exakte v/c-Ablesung (0.03% konsistent) — Kandidat")
print("   fuer das Torus-Ruhesystem, Identifikation [S]")
print("P3 Windungs-Auszeichnung strukturell real, praktisch inert [K]")
print("P4 zwei benennbare Signaturen: 4'-Versatz (zugaenglich),")
print("   Drift 0.01%-Niveau (harmlos) [S]")
