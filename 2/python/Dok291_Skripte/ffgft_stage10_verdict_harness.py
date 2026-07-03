#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT-seitiges Stage-10-Verdikt-Harness (BD17A, symmetrischer Lock).
GEBAUT UND EINGEFROREN VOR ANKUNFT DER STAGE-10-DATEN (2. Juli 2026),
damit beim Scoring keine Auswertungswahl mehr offen ist.

Kodiert AUSSCHLIESSLICH die pre-registrierte Vereinbarung:
  Extraktor:  theta_gamma = 1/2 * Arg det W_gamma(C_e)  mod 2pi/3, in RADIANT
  Ziel:       theta* = 2/9 rad
  Kriterien:  (1) Ordnung-3-Struktur (Winkel leben mod 2pi/3)
              (2) schief-adjungierter GENERATOR (K^dagger=-K; Residuen-Durchreiche)
              (3) deklarierte Aktion S / eingefrorene Stage-9-Klasse (Metadaten)
              (4) Selektion von 2/9 GEGEN den Orbit {1/9, 4/9} und gegen die Nulls

PRIMAERKRITERIUM (hier fixiert): naechstes-Orbit-Glied-Klassifikation.
  Jeder Loop-Winkel theta (mod 2pi/3) wird dem naechsten Referenzpunkt
  {0 (flach), 1/9, 2/9, 4/9} zugeordnet (zirkulaere Distanz mod 2pi/3).
  Target-Statistik: Anteil f_29 der 2/9-zugeordneten Winkel.
  ADMITTED : f_29(target) > f_29(jede harte Null) UND f_29(target) > f_19, f_49
             (2/9 ist Modus des Targets und schlaegt alle Nulls)
  RESIDUAL : f_29(target) > f_19, f_49 (Orbit-Selektion), aber mindestens
             eine Null erreicht/uebertrifft f_29(target)
  BLOCKED  : keine Orbit-Selektion von 2/9 (f_29 nicht Maximum im Orbit)
  Zusaetzlich deskriptiv (KEINE Verdikt-Rolle): Median-Distanz zu 2/9,
  Hit-Fraktionen bei tol in {0.01, 0.02, 0.039} rad, Winkel-Histogramm.

Eingabeformate (flexibel, weil Marcels Exportformat offen ist):
  CSV mit Spalten model,seed,theta_gamma   (Winkel in rad, roh oder mod 2pi/3)
  oder JSON {model: [winkel, ...], ...}
Aufruf:  python3 ffgft_stage10_verdict_harness.py <datei> [--target NAME]
Ohne Datei laeuft ein SELBSTTEST mit synthetischen Daten (seed 20780458).

numpy-only. Aenderungen an diesem Skript nach Dateneingang sind unzulaessig
und wuerden den Lock brechen (dann als solches im Ledger vermerken).
"""
import sys, json, csv
import numpy as np

np.random.seed(20780458)
TWO_PI = 2*np.pi
SECTOR = TWO_PI/3.0
THETA_STAR = 2.0/9.0
ORBIT = {"flat_0": 0.0, "1/9": 1.0/9.0, "2/9": 2.0/9.0, "4/9": 4.0/9.0}
TOLS = (0.01, 0.02, 0.039)   # nur deskriptiv

def wrap_sector(a):
    return np.mod(np.asarray(a, dtype=float), SECTOR)

def circ_dist_sector(a, b):
    d = np.abs(wrap_sector(a) - wrap_sector(b))
    return np.minimum(d, SECTOR - d)

def classify_nearest(angles):
    """Zaehlt Zuordnung jedes Winkels zum naechsten Referenzpunkt."""
    angles = wrap_sector(angles)
    names = list(ORBIT.keys())
    refs = np.array([ORBIT[n] for n in names])
    d = np.array([circ_dist_sector(angles, r) for r in refs])  # (4, N)
    idx = np.argmin(d, axis=0)
    frac = {n: float(np.mean(idx == i)) for i, n in enumerate(names)}
    return frac

def describe(angles):
    a = wrap_sector(angles)
    out = {"n": int(a.size),
           "median_dist_2_9": float(np.median(circ_dist_sector(a, THETA_STAR)))}
    for t in TOLS:
        out[f"hit_frac_tol_{t}"] = float(np.mean(circ_dist_sector(a, THETA_STAR) <= t))
    return out

def verdict(models, target_name):
    tgt = classify_nearest(models[target_name])
    nulls = {m: classify_nearest(v) for m, v in models.items() if m != target_name}
    orbit_selected = tgt["2/9"] > tgt["1/9"] and tgt["2/9"] > tgt["4/9"]
    beats_all_nulls = all(tgt["2/9"] > nf["2/9"] for nf in nulls.values())
    if orbit_selected and beats_all_nulls:
        v = "ADMITTED"
    elif orbit_selected:
        v = "RESIDUAL"
    else:
        v = "BLOCKED"
    return v, tgt, nulls

def load(path):
    if path.endswith(".json"):
        with open(path) as f:
            d = json.load(f)
        return {k: np.asarray(v, dtype=float) for k, v in d.items()}
    models = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            models.setdefault(row["model"], []).append(float(row["theta_gamma"]))
    return {k: np.asarray(v) for k, v in models.items()}

def selftest():
    print("SELBSTTEST (synthetisch, seed 20780458) -- kein Stage-10-Scoring.")
    rng = np.random.default_rng(20780458)
    n = 4860
    cases = {
        "erwartet_ADMITTED": {
            "target": rng.normal(THETA_STAR, 0.02, n),
            "null_flat": rng.normal(0.0, 0.01, n),
            "null_uniform": rng.uniform(0, SECTOR, n),
            "null_random_skew": rng.uniform(0, SECTOR, n)},
        "erwartet_RESIDUAL": {
            "target": rng.normal(THETA_STAR, 0.03, n),
            "null_copycat": rng.normal(THETA_STAR, 0.02, n),
            "null_flat": rng.normal(0.0, 0.01, n)},
        "erwartet_BLOCKED": {
            "target": rng.normal(0.0, 0.02, n),
            "null_uniform": rng.uniform(0, SECTOR, n)},
    }
    ok = True
    for name, models in cases.items():
        v, tgt, _ = verdict(models, "target")
        want = name.split("_")[1]
        ok &= (v == want)
        print(f"  {name}: Verdikt={v}  f(2/9)={tgt['2/9']:.3f} "
              f"f(1/9)={tgt['1/9']:.3f} f(4/9)={tgt['4/9']:.3f} f(flat)={tgt['flat_0']:.3f}"
              f"  -> {'OK' if v==want else 'FEHLER'}")
    print("SELBSTTEST:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1

def main():
    if len(sys.argv) < 2:
        return selftest()
    path = sys.argv[1]
    target = "target"
    if "--target" in sys.argv:
        target = sys.argv[sys.argv.index("--target")+1]
    models = load(path)
    if target not in models:
        # heuristisch: Modellname, der 'target' enthaelt
        cand = [m for m in models if "target" in m.lower()]
        if len(cand) == 1:
            target = cand[0]
        else:
            print(f"FEHLER: Target-Modell '{target}' nicht gefunden. Modelle: {list(models)}")
            return 2
    v, tgt, nulls = verdict(models, target)
    print("="*72)
    print("FFGFT Stage-10-Verdikt (pre-registriertes Primaerkriterium)")
    print("="*72)
    print(f"Target: {target}")
    print(f"  Orbit-Fraktionen: 2/9={tgt['2/9']:.4f}  1/9={tgt['1/9']:.4f} "
          f" 4/9={tgt['4/9']:.4f}  flat={tgt['flat_0']:.4f}")
    print(f"  Deskriptiv: {describe(models[target])}")
    print("Nulls:")
    for m, nf in sorted(nulls.items()):
        print(f"  {m}: f(2/9)={nf['2/9']:.4f}  {describe(models[m])}")
    print("-"*72)
    print(f"VERDIKT: {v}")
    print("(ADMITTED: 2/9 Orbit-Modus UND schlaegt alle Nulls;")
    print(" RESIDUAL: Orbit-Modus, aber Null-Ueberlapp; BLOCKED: keine Orbit-Selektion.)")
    print("Kriterien 1-3 (Ordnung 3 / schief-adj. Generator / eingefrorene Klasse)")
    print("werden aus Marcels Run-Metadaten uebernommen und im Ledger separat bestaetigt.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
