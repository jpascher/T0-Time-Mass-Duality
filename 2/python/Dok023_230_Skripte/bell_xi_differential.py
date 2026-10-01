#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT xi-scale Bell/CHSH deviation: differential observable and precision budget.

Source of the predicted form: FFGFT Doc. 023 (Bell). The two-photon correlation is
    E_F(theta) = -cos(theta) * V(theta),
with QM giving V=1 and FFGFT a visibility deficit set by xi = 4/30000 = 1/7500:
    uniform (f=1, photons):   V = 1 - xi
    linear (angle-dependent): V = 1 - xi*theta/pi
    exponential (extended):   V = exp(-xi*(theta/pi)^2 / D_f),   D_f = 3 - xi

Key results this script demonstrates:
  1. The UNIFORM (1-xi) damping is degenerate with a constant source visibility V0<1
     -> differential delta(pi)-delta(0) = 0 -> NOT observable. Chasing the absolute
     CHSH deficit measures source imperfection, not xi (on any platform).
  2. The ANGLE-DEPENDENT deficit is in principle separable from a constant source
     visibility: measure the correlation visibility at the two QM-stationary extrema
     theta ~ pi and theta ~ 0 and difference the deficits. QM is stationary there
     (dE/dtheta=0) so angle drift/calibration enter at 2nd order; a constant source
     visibility cancels; the FFGFT signal survives at order xi/D_f..xi.
  3. Counting statistics alone would give N ~ 1/signal^2 -> ~6e7..6e8 coincidence pairs.
     This is a pure shot-noise estimate WITHOUT any systematics (angle-dependent
     detector/optics visibility, drifts); it is not a feasibility statement.

Aktualisiert am 1.10.2026: Punkt 2/3 umformuliert -- die N-Abschätzung ist reine
Zählstatistik ohne Systematik, "photonic-reachable" gestrichen; der xi-Effekt bzw. die
Abweichung von der Tsirelson-Grenze ist mit heutiger Hardware nicht auflösbar
(vgl. Dok. 023 bzw. Dok. 190, R142/R143). Zahlenwerte unverändert.
"""
import numpy as np
xi = 4/30000.0
Df = 3 - xi
sq2 = 2*np.sqrt(2)
V_uni = lambda th: (1-xi)*np.ones_like(th)
V_lin = lambda th: 1 - xi*th/np.pi
V_exp = lambda th: np.exp(-xi*(th/np.pi)**2/Df)

if __name__ == "__main__":
    print(f"xi = {xi:.6e}   D_f = {Df:.5f}   CHSH_QM = {sq2:.6f}")
    print(f"uniform CHSH = {sq2*(1-xi):.6f}  (dCHSH = {sq2*xi:.3e}) -- but see below")
    print("\nvisibility deficit delta(theta)=1-V(theta) at QM extrema, and the differential:")
    for name, V in [("uniform", V_uni), ("linear", V_lin), ("exp", V_exp)]:
        d0  = 1-float(V(np.array([1e-6]))[0])
        dpi = 1-float(V(np.array([np.pi]))[0])
        print(f"  {name:8s}: delta(0+)={d0:.3e}  delta(pi)={dpi:.3e}  "
              f"differential={dpi-d0:.3e}")
    print("\nuniform differential = 0  => degenerate with constant V0  => NOT observable.")
    for nm, s in [("exp  (xi/Df)", 1-float(V_exp(np.array([np.pi]))[0])),
                  ("linear (xi) ", 1-float(V_lin(np.array([np.pi]))[0]))]:
        print(f"  signal {nm} = {s:.3e}  ->  N ~ 1/s^2 ~ {1/s**2:.2e} coincidence pairs (SNR~1)")
    print("\nNote: N is counting statistics only (no systematics). Per Dok. 023 / R142, R143")
    print("the xi effect (deviation from the Tsirelson bound) is NOT resolvable with current hardware.")
