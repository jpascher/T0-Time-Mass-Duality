#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lilly-Madau cosmic star-formation history on the v4 "Time (G-yr)" axis (for J. Nicholson, IPI).

x-axis  = cosmic time since Big Bang in Gyr (0 -> ~13.8), matching the v4 diagram's
          "Time (G-yr)" axis (Big Bang/decoupling at left, "now" at right).
curve   = Madau & Dickinson (2014) global SFRD fit, converted z -> cosmic time.
points  = representative JWST UV-derived high-z SFRD (Donnan+2024, Harikane+2024,
          Robertson+2024, Finkelstein+2024); UV, M_UV<-17, not dust-corrected.
y-axis  = SFRD normalized to the cosmic-noon peak (= 1), so it overlays a schematic.
top axis= redshift z for reference.
Cosmology: flat LCDM, H0=67.4, Om=0.315, OL=0.685 (Planck 2018), t0 = 13.80 Gyr.
"""
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- cosmology: cosmic age as a function of redshift ---
H0, Om, OL = 67.4, 0.315, 0.685
tH = 9.778 / (H0/100.0)                      # Hubble time in Gyr = 14.51
def age_Gyr(z):
    return (2.0/3.0)/np.sqrt(OL) * tH * np.arcsinh(np.sqrt(OL/Om) * (1.0+z)**-1.5)
t0 = age_Gyr(0.0)                            # 13.80 Gyr

# --- Madau & Dickinson (2014) SFRD fit [Msun/yr/Mpc^3] ---
def md14(z):
    return 0.015 * (1.0+z)**2.7 / (1.0 + ((1.0+z)/2.9)**5.6)
z_curve = np.linspace(0.0, 16.0, 1600)
psi = md14(z_curve)
psi_peak = psi.max()                         # normalization (cosmic noon)
t_curve = age_Gyr(z_curve)

# --- representative JWST high-z SFRD points (log10 rho_SFR, dex error) ---
z_pts   = np.array([8.0, 9.0, 10.0, 11.0, 12.5, 14.0])
log_pts = np.array([-2.55, -2.70, -2.88, -3.05, -3.30, -3.65])
err_pts = np.array([0.15, 0.15, 0.18, 0.20, 0.22, 0.25])
rho_pts = 10.0**log_pts
t_pts   = age_Gyr(z_pts)

# --- figure ---
fig, ax = plt.subplots(figsize=(11, 6.2)); fig.patch.set_facecolor("white")
ax.plot(t_curve, psi/psi_peak, color="#c0392b", lw=2.4,
        label="Madau–Dickinson (2014) global SFRD")
ax.errorbar(t_pts, rho_pts/psi_peak, yerr=(np.log(10)*err_pts)*(rho_pts/psi_peak),
            fmt="o", ms=7, color="#2c3e50", ecolor="#7f8c8d", capsize=3, zorder=5,
            label="JWST UV high-$z$ (Donnan/Harikane/Robertson/Finkelstein 2024)")

# cosmic noon marker
z_noon = z_curve[np.argmax(psi)]; t_noon = age_Gyr(z_noon)
ax.axvline(t_noon, color="#888", ls=":", lw=1)
ax.annotate(f"cosmic noon\n$z\\approx{z_noon:.1f}$, $t\\approx{t_noon:.1f}$ Gyr",
            xy=(t_noon, 1.0), xytext=(t_noon+1.4, 0.93), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#888"))
# "you are here" / now
ax.axvline(t0, color="#2980b9", ls="--", lw=1.2)
ax.annotate("now", xy=(t0, 0.115), xytext=(t0-1.7, 0.30), fontsize=10, color="#2980b9",
            arrowprops=dict(arrowstyle="->", color="#2980b9"))
# decoupling
ax.annotate('"decoupling"\n($z\\approx1100$, $t\\approx0$)', xy=(0.0, 0.0),
            xytext=(0.4, 0.40), fontsize=8.5, color="#555",
            arrowprops=dict(arrowstyle="->", color="#999"))

ax.set_xlim(0, 14.2); ax.set_ylim(0, 1.08)
ax.set_xlabel("Time since Big Bang  (G-yr)", fontsize=12)
ax.set_ylabel("Star-formation rate density  (normalized to peak)", fontsize=12)
ax.set_xticks(range(0, 15, 1))
ax.grid(alpha=0.25)
ax.legend(loc="upper right", fontsize=9, framealpha=0.95)
ax.set_title("Cosmic star-formation history (Lilly–Madau) on the v4 time axis\n"
             "Big Bang at left, present at right — JWST-updated", fontsize=12)

# top redshift axis (nonlinear: ticks placed at their cosmic-time positions)
z_ticks = np.array([0, 0.5, 1, 2, 3, 5, 8, 14])
axz = ax.twiny(); axz.set_xlim(ax.get_xlim())
axz.set_xticks([age_Gyr(z) for z in z_ticks])
axz.set_xticklabels([f"{z:g}" for z in z_ticks])
axz.set_xlabel("redshift  $z$", fontsize=11)

fig.tight_layout()
fig.savefig("lilly_madau_v4_timeaxis.png", dpi=180, bbox_inches="tight")
print("t0 =", round(t0,3), "Gyr ; cosmic noon z =", round(z_noon,2), "t =", round(t_noon,2),
      "Gyr ; peak SFRD =", round(psi_peak,4), "Msun/yr/Mpc^3")
print("JWST points (z, t_Gyr, normalized):")
for z,t,r in zip(z_pts,t_pts,rho_pts/psi_peak): print(f"  z={z:4} t={t:5.2f}  norm={r:.4f}")
print("written lilly_madau_v4_timeaxis.png")
