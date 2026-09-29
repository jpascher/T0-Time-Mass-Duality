#!/usr/bin/env python3
"""Rechenpruefung Gruppe B: Dok. 049, 056, 061, 063, 068 (nur Nachrechnung, nichts im Repo aendern)."""
import math

xi = 4 / 30000
E_xi = 1 / xi
eV_K = 11604.518          # K pro eV
hbar = 1.054571817e-34    # J s
c = 299792458.0           # m/s
kB = 1.380649e-23
e = 1.602176634e-19
hbarc_eVm = 197.3269804e-9  # eV m
m_e, m_mu, m_tau = 0.51099895, 105.6583755, 1776.86  # MeV
alpha_inv = 137.035999084


def h(t):
    print("\n" + "=" * 70 + "\n" + t + "\n" + "=" * 70)


# ---------------------------------------------------------------- 049
h("049-1  a_mu = xi/(2 pi) (m_mu/m_e)^2")
pref = xi / (2 * math.pi)
r2 = (m_mu / m_e) ** 2
a_mu = pref * r2
print(f"xi/(2pi)          = {pref:.6e}")
print(f"(m_mu/m_e)^2      = {r2:.4f}")
print(f"a_mu (wörtlich)   = {a_mu:.6f}   = {a_mu/1e-11:.4e} x 10^-11")
print(f"Dokument          = 245e-11 = {245e-11:.3e}; Faktor wörtlich/Dok = {a_mu/245e-11:.4e}")
# Anker-Varianten: Groessen sind dimensionslos -> Energieeinheit aendert nichts
for name, x in [("xi gerundet 1.33e-4", 1.33e-4)]:
    print(f"  mit {name}: {x/(2*math.pi)*r2:.6f}")
# welcher Faktor fehlt? a_mu/245e-11
print(f"benötigter Zusatzfaktor ~ {245e-11/a_mu:.3e}")
# Vergleich: xi^2 statt xi ?
print(f"Test xi^2/(2pi)(m_mu/m_e)^2 = {xi**2/(2*math.pi)*r2:.4e}")

h("049-2  'Messung 251(59)e-11' = Delta a_mu (2021), nicht a_mu")
a_exp_2021 = 116592061e-11
a_sm_2020 = 116591810e-11
print(f"a_mu exp (2021 Weltmittel) = {a_exp_2021:.9e}")
print(f"a_mu SM (WP 2020)          = {a_sm_2020:.9e}")
print(f"Differenz                  = {(a_exp_2021-a_sm_2020)/1e-11:.0f} x 10^-11  (Dok: 251(59))")
print(f"Verhältnis Messwert/Differenz = {a_exp_2021/251e-11:.3e}")
a_exp_2025 = 116592071.5e-11
a_sm_2025 = 116592033e-11
print(f"Stand 2025: Delta = {(a_exp_2025-a_sm_2025)/1e-11:.1f} x 10^-11, sigma_kombiniert = {math.hypot(14.5,62):.1f} -> {(a_exp_2025-a_sm_2025)/1e-11/math.hypot(14.5,62):.2f} sigma")
print(f"Übereinstimmung laut Dok: |251-245|/59 = {abs(251-245)/59:.3f} sigma; mit komb. Fehler sqrt(59^2+15^2)={math.hypot(59,15):.1f}: {6/math.hypot(59,15):.3f} sigma")

h("049-3  a_tau = xi/(2 pi) (m_tau/m_e)^2  (zusätzlich)")
a_tau = pref * (m_tau / m_e) ** 2
print(f"(m_tau/m_e)^2 = {(m_tau/m_e)**2:.4e}")
print(f"a_tau (wörtlich) = {a_tau:.4f}   (Dok: 6,9e-8); Faktor = {a_tau/6.9e-8:.3e}")
print(f"Verhältnis a_tau/a_mu nach Formel = (m_tau/m_mu)^2 = {(m_tau/m_mu)**2:.3f}; 245e-11 * das = {245e-11*(m_tau/m_mu)**2:.3e}")

h("049-4  xi aus Higgs-Parametern (Kontrolle, Dok. Z. 401)")
lam, v, mh = 0.13, 246.0, 125.0
xi_h = lam**2 * v**2 / (16 * math.pi**3 * mh**2)
print(f"lambda_h^2 v^2/(16 pi^3 m_h^2) = {xi_h:.4e}  (Dok ~1,33e-4)")
print(f"lambda_h SM = m_h^2/(2 v^2) = {125.25**2/(2*246.22**2):.4f}")

# ---------------------------------------------------------------- 056
h("056-1  c 'Herleitung'")
print("c = 299792458 m/s exakt per Definition des Meters (17. CGPM 1983). Keine Rechnung im Dokument.")
lP = 1.616255e-35
G = 6.67430e-11
print(f"Kontrolle: l_P = sqrt(hbar G/c^3) = {math.sqrt(hbar*G/c**3):.6e} m  (enthält c als Eingabe)")

h("056-2  mu_0 'per Definition' seit 2019 (zusätzlich)")
mu0_old = 4 * math.pi * 1e-7
mu0_2019 = 1.25663706212e-6   # CODATA 2018
print(f"4 pi 1e-7       = {mu0_old:.12e}")
print(f"CODATA 2018 mu0 = {mu0_2019:.12e}  rel. Abw. = {(mu0_2019/mu0_old-1):.2e}")
eps0 = 1 / (mu0_old * c**2)
print(f"eps0 = 1/(mu0 c^2) mit 4pi e-7 = {eps0:.10e} (Dok 8.854187817e-12)")
hb = e**2 / (4 * math.pi * eps0 * c / alpha_inv)
print(f"hbar = e^2/(4 pi eps0 c alpha) = {hb:.10e} (Dok 1.054571817e-34; SI exakt 1.054571817...e-34)")
print(f"G = l_P^2 c^3 / hbar = {lP**2*c**3/hbar:.6e} (Dok 6.67430e-11)")

h("056-3  Tabelle G(L) = L^2 c^3/hbar (zusätzlich)")
for L, dok in [(2.5e-35, 1.04e-10), (1.0e-35, 1.67e-11), (math.pi*1e-35, 1.64e-10), (lP, 6.674e-11)]:
    Gc = L**2 * c**3 / hbar
    print(f"L = {L:.4e} m: G = {Gc:.4e}   Dok: {dok:.3e}   Faktor Dok/richtig = {dok/Gc:.3f}")

h("056-4  alpha = xi E0^2 mit E0 = 7.398 MeV (zusätzlich)")
a = xi * 7.398**2
print(f"E0^2 = {7.398**2:.4f}; alpha = {a:.6e}; 1/alpha = {1/a:.4f}  (Dok 137.038)")
print(f"rel. Abw. zu 137.035999 = {(1/a-alpha_inv)/alpha_inv*100:.5f} %")
print(f"E0 geom. Mittel CODATA = {math.sqrt(m_e*m_mu):.5f} MeV")
print(f"12/5 xi^-1/2 = {2.4/math.sqrt(xi):.3f}  vs m_mu/m_e = {m_mu/m_e:.3f} -> {(2.4/math.sqrt(xi)/(m_mu/m_e)-1)*100:.2f} %")

# ---------------------------------------------------------------- 061
h("061-1  Delta chi^2 = -3,6 -> sigma")
d = 3.6
print(f"sqrt(3.6) = {math.sqrt(d):.4f} sigma (Dok: 2,1)")
print(f"für 2,1 sigma nötig: Delta chi^2 = {2.1**2:.2f}")
print(f"Delta AIC = -3.6 + 2 = {-3.6+2:.1f}")
print("Skriptsuche: kein .py in 2/python enthält 1127.4 / 1123.8 (grep, siehe Bericht)")

h("061-2  Casimir/CMB '312 experimentell'")
T = 2.7255
aSB = 4 * 5.670374419e-8 / c   # Strahlungskonstante
rho_cmb = aSB * T**4
L = 1e-4
rho_cas = hbar * c * math.pi**2 / (240 * L**4)
print(f"rho_CMB = a T^4 = {rho_cmb:.4e} J/m^3 (Dok 4,17e-14)")
print(f"rho_Casimir(1e-4 m) = {rho_cas:.4e} J/m^3 (Dok 1,3e-11)")
print(f"Verhältnis = {rho_cas/rho_cmb:.2f} (Dok 312)")
print(f"pi^2/(240 xi) = {math.pi**2/(240*xi):.2f} (Dok 308)")
Lxi = (xi * hbar * c / rho_cmb) ** 0.25
print(f"L_xi aus rho_CMB = xi hbar c/L^4: L = {Lxi:.5e} m")
print(f"mit exaktem L_xi: Verhältnis = {hbar*c*math.pi**2/(240*Lxi**4)/rho_cmb:.2f}")
print(f"(L_xi/1e-4)^4 = {(Lxi/1e-4)**4:.4f}  -> erklärt 312/308 = {312/308:.4f}")

h("061-3  rho_CMB = 4,87e41 'nat. Einheiten' (zusätzlich)")
rho_eV4 = rho_cmb / e * hbarc_eVm**3
print(f"rho_CMB in eV^4        = {rho_eV4:.4e}")
print(f"rho_CMB in MeV^4       = {rho_eV4*1e-24:.4e}")
print(f"rho_CMB/(hbar c) in m^-4 = {rho_cmb/(hbar*c):.4e}")
print(f"rho_CMB in Planck-Einh. = {rho_cmb/(c**7/(hbar*G**2)):.4e}")
print(f"1/rho(eV^4) = {1/rho_eV4:.4e}")
print(f"L_xi = (xi/4.87e41)^(1/4) = {(xi/4.87e41)**0.25:.4e} (in welcher Längeneinheit auch immer; nicht 1e-4 m)")

h("061-4 / 063-3  T_CMB = (16/9) xi^2 E_xi")
tn = 16 / 9 * xi**2 * E_xi
print(f"(16/9) xi^2 E_xi = (16/9) xi = {tn:.6e}")
print(f"mit xi^2 gerundet 1,78e-8: {16/9*1.78e-8*7500:.4e}")
print(f"gemessen T = 2,7255 K = {T/eV_K:.5e} eV  (Dok 2,35e-4)")
print(f"(16/9) xi eV in K = {tn*eV_K:.4f} K; Abw. zu 2,7255 K = {(tn*eV_K/T-1)*100:.3f} %")
print(f"Verhältnis T/E_xi = {T/eV_K/E_xi:.4e} (Dok 3,13e-8); (16/9)xi^2 = {16/9*xi**2:.4e} (Dok 3,16e-8)")
print(f"in MeV als Einheit: (16/9) xi MeV = {tn*1e6*eV_K:.4e} K (Skalenabhängigkeit)")

# ---------------------------------------------------------------- 063
h("063-1  nu_xi = 1/L_xi")
print(f"1/L_xi = {1/L:.1e} m^-1 (keine Frequenz)")
print(f"c/L_xi = {c/L:.4e} Hz  (Dok: 1e4 Hz); Faktor {c/L/1e4:.3e}")
print(f"omega = 2 pi c/L = {2*math.pi*c/L:.4e} s^-1")
print(f"Photonenenergie h c/L = {hbarc_eVm*2*math.pi/L:.4e} eV")

# ---------------------------------------------------------------- 068
h("068-1  m_h/M_P = sqrt(xi)")
print(f"sqrt(xi) = {math.sqrt(xi):.6f} (Dok 0,0115)")
mh = 125.25
MP = 1.22089e19
MPr = MP / math.sqrt(8 * math.pi)
print(f"m_h/M_P       = {mh/MP:.4e}")
print(f"m_h/M_P(red.) = {mh/MPr:.4e}")
print(f"Faktor sqrt(xi)/(m_h/M_P) = {math.sqrt(xi)/(mh/MP):.3e}")
print(f"sqrt(xi)*M_P = {math.sqrt(xi)*MP:.4e} GeV (vorhergesagte Higgs-Masse)")
print(f"welche xi-Potenz ergäbe m_h/M_P: log_xi = {math.log(mh/MP)/math.log(xi):.3f}")
print(f"m_h/v = {mh/246.22:.4f}; E_P sqrt(xi) = {MP*math.sqrt(xi):.3e} GeV (vgl. Dok.167 'E_EW~100 GeV')")

print("\nFERTIG")
