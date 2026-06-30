import numpy as np
xi = 4/30000
me, mmu = 0.51099895e6, 105.6583755e6   # eV
E0 = np.sqrt(me*mmu)                     # die EINE FFGFT-Skala (geom. Mittel), Dok 282
floor = 49e-3                            # Oszillations-Boden  sqrt(dm2_atm) ~ 49 meV  (Labor)
katrin = 0.8                             # direkte kinematische Schranke (Labor)

print("E0 = sqrt(me*mmu) = %.4f MeV   (xi = %.6e)"%(E0/1e6, xi))
print("\n--- Kandidaten-Referenzen: m_window = xi^2/2 * ref, gegen die zwei Laborschranken ---")
print("  Referenz            m_window           Boden(>=49meV)   KATRIN(<=0.8eV)")
for name, ref in [("m_e", me), ("E0=sqrt(me*mmu)", E0), ("m_mu", mmu)]:
    mw = xi**2/2 * ref
    ok_floor = mw >= floor
    ok_kat   = mw <= katrin
    print("  %-18s  %8.2f meV        %-5s            %-5s"
          %(name, mw*1e3, "ja" if ok_floor else "NEIN", "ja" if ok_kat else "NEIN"))

print("\n=> die zwei Laborschranken KLAMMERN die Referenz ein:")
print("   m_e zu leicht (faellt Boden), m_mu zu schwer (faellt KATRIN), nur E0 passt.")
print("   und E0 ist genau die EINE natuerliche FFGFT-Skala -- keine neue Groesse.\n")

# Mit Referenz E0: alles wird zu reinen xi-Potenzen x 1/2
mw = xi**2/2 * E0
om = mw/xi                       # m_window = xi*omega  ->  omega
print("--- Mit Referenz E0 (lab-selektiert) ---")
print("  m_window = xi^2/2 * E0 = %.2f meV"%(mw*1e3))
print("  omega    = m_window/xi = xi/2 * E0 = %.1f eV"%om)
print("  dimensionslos:  omega/E0 = %.6e   (xi/2 = %.6e)"%(om/E0, xi/2))
print("  dimensionslos:  m_window/E0 = %.6e   (xi^2/2 = %.6e)"%(mw/E0, xi**2/2))
print("\n=> in Einheiten der einen Skala E0 ist ALLES reine xi-Potenz x 1/2:")
print("   omega/E0 = xi/2 ,  m_window/E0 = xi^2/2 .  Kein freier Parameter mehr.")
print("   Das 1/2 = Geschwindigkeits-Quadrat (kinematisch).")
print("   Der EINE Rest: warum omega = xi*E0, d.h. genau EINE fraktale xi-Potenz (D_f=3-xi).")
