#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Doc 283, Sec. 9 -- the crystallographic restriction
===================================================
Sec. 9 claims: 5-fold symmetry is NON-crystallographic (it cannot tile a periodic
lattice, which is exactly why HLV must decompactify into an infinite aperiodic
R^3); 3-fold IS crystallographic, of the same family as 6-fold (the
triangular/hexagonal lattice). This is the crystallographic restriction theorem:

  an n-fold rotation maps a lattice to itself  <=>  2 cos(2 pi / n) is an INTEGER.

The trace of an order-n rotation in a lattice basis must be an integer, and that
trace is 2 cos(2 pi / n) + (1 in 3D). So n in {1,2,3,4,6} are allowed (crystallographic),
n = 5 and n >= 7 are forbidden.

Note the pentagonal-golden link: 2 cos(2 pi/5) = (sqrt5 - 1)/2 = 1/phi -- the very
golden ratio that runs through HLV. So "pentagonal" and "phi" are the same
non-crystallographic fact. Writes crystallographic_restriction.csv. numpy only.
"""
import numpy as np, csv

rows = []
for n in range(1, 13):
    t = 2*np.cos(2*np.pi/n)
    is_int = abs(t - round(t)) < 1e-9
    note = ""
    if n == 5:   note = "2cos(72deg) = (sqrt5-1)/2 = 1/phi -> golden / pentagonal"
    elif n == 3: note = "triangular/hexagonal lattice (FFGFT Z3 / Euler-Tonnetz family)"
    elif n == 6: note = "hexagonal lattice (same family as 3-fold)"
    rows.append([n, f"{2*np.pi/n*180/np.pi:.1f}", f"{t:+.6f}", is_int,
                 "crystallographic" if is_int else "NON-crystallographic", note])

with open("crystallographic_restriction.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["n_fold", "rotation_deg", "2cos(2pi/n)", "is_integer", "lattice_status", "note"])
    wr.writerows(rows)

print("Crystallographic restriction: an n-fold rotation tiles a periodic lattice")
print("iff 2 cos(2 pi/n) is an integer.\n")
print(f"{'n':>3s}{'2cos(2pi/n)':>14s}   status")
for r in rows:
    print(f"{r[0]:>3d}{float(r[2]):>14.5f}   {r[4]}{('  <- '+r[5]) if r[5] else ''}")

allowed = [r[0] for r in rows if r[3]]
print(f"\nCrystallographic n: {allowed}  ->  5-fold is the first forbidden order.")
print("Consequence (Sec. 9): 5-fold cannot compactify on a periodic lattice; HLV must")
print("decompactify. 3-fold is crystallographic (hexagonal family) and re-compactifies")
print("naturally -- which is why the world that carries the mass structure is hexagonal,")
print("not pentagonal. 2cos(72deg)=1/phi ties the pentagonal branch to the golden ratio.")
print("-> crystallographic_restriction.csv")
