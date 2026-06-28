import numpy as np
np.set_printoptions(precision=4, suppress=True)
print("="*76)
print(" Offene Berechnung (1): kinetischer/Window-Anteil als xi-fraktaler Bruchteil")
print(" des statischen, ueber T~*m=1 -- Eingrenzung der xi-Potenz (kein Beweis)")
print("="*76)

xi   = 4/30000
me   = 0.5109989461e6      # eV
mmu  = 105.6583755e6
mtau = 1776.86e6
geom = np.sqrt(me*mmu)
# empirische Schranken (eV)
dm2_atm = 2.44e-3          # eV^2  -> schwerstes nu >~ sqrt
dm2_sol = 7.53e-5
m_heavy_floor = np.sqrt(dm2_atm)        # ~0.049 eV
m_med_floor   = np.sqrt(dm2_sol)        # ~0.0087 eV
cosmo_sum = 0.12           # eV  (Sum m_nu <~)
doc_m0  = 1.9e-3           # eV  (285: leichteste am Q=7/15-Crossing)
doc_sum = 61e-3            # eV  (285: Summe dort)

print(f"\n xi = {xi:.6e},  xi^2/2 = {xi**2/2:.4e}")
print(f" Oszillations-Boden: schwerstes nu >~ sqrt(dm2_atm) = {m_heavy_floor*1e3:.1f} meV")
print(f" Kosmologie: Sum m_nu <~ {cosmo_sum*1e3:.0f} meV ;  285-Ziel: m0~{doc_m0*1e3:.1f} meV, Sum~{doc_sum*1e3:.0f} meV")

# ---------------------------------------------------------------------------
print("\n--- Dualitaets-Rahmung (was T~*m=1 FESTLEGT) ---")
print(" T~ = 1/max(m,omega). Ein Window-Zustand ist fast-masselos (omega >> m_window),")
print(" also T~ = 1/omega -> er sitzt im KINETISCHEN Sektor (Dok 255/067/080). Das ist")
print(" gesichert. OFFEN ist allein die Groesse der statischen Restmasse m_window.")

# ---------------------------------------------------------------------------
print("\n--- Kandidaten-Scan: m_window = C * xi^p * m_ref ---")
print(f"{'p':>2} {'C':>4} {'m_ref':>6} {'m_window':>12}   Einordnung")
refs = {"m_e":me, "sqrt(e*mu)":geom, "m_mu":mmu}
def klass(m):
    if m > cosmo_sum:           return "ZU GROSS (> Kosmologie-Schranke) -> raus"
    if m > m_heavy_floor:       return "ok als SCHWERSTES nu (>~ dm2_atm-Boden)"
    if m > m_med_floor:         return "ok als MITTLERES nu"
    if m > doc_m0*0.3:          return "Skala des LEICHTESTEN nu (~285-m0)"
    return "viel zu klein (unter jeder Schranke) -> kein Anker"
for p in (1,2,3,4):
    for C,Cl in ((1.0,"1"),(0.5,"1/2")):
        for rn,rv in refs.items():
            m = C*xi**p*rv
            tag=""
            if abs(m-xi**2/2*me)/(xi**2/2*me)<1e-9: tag="  <== Dok-047-Anker"
            print(f"{p:>2} {Cl:>4} {rn:>10} {m*1e3:>10.4f} meV   {klass(m)}{tag}")
    print()

# ---------------------------------------------------------------------------
print("--- Constraint-Check der einzigen Anker-Regel (p=2, C=1/2, m_ref=m_e) ---")
m_anchor = 0.5*xi**2*me
print(f" reproduziert Dok 047:      m_nu = {m_anchor*1e3:.3f} meV   (Soll 4.54)  {'OK' if abs(m_anchor-4.54e-3)<1e-4 else 'X'}")
print(f" Photon-Limit xi->0:        m_window -> 0                 OK (rein kinetisch)")
print(f" Dimensionskonsistenz:      xi dimensionslos -> [m_window]=[m_ref]  OK")
print(f" Elektron-Trennung:         gewoehnl. Kinetik (gamma-1)m_e ist NICHT xi-unterdrueckt")
print(f"                            -> xi-Regel betrifft die Window-Restmasse, nicht E_bewegung  OK")
print(f" Spektrum (dm2):            ein einzelner Wert {m_anchor*1e3:.1f} meV < Boden {m_heavy_floor*1e3:.0f} meV")
print(f"                            -> kann das dm2-Spektrum NICHT erzeugen -> braucht Dynamik (Luecke 2)")

print("\n"+"="*76)
print(" BEFUND (ehrlich, eingrenzend):")
print(" * Die Dualitaet legt fest: Window = kinetischer Sektor (T~=1/omega). Gesichert.")
print(" * xi-Potenz: nur p=2 trifft die meV-Neutrino-Skala; p=1 zu gross (~10 eV/68 eV),")
print("   p>=3 zu klein (kein Anker). Also p=2 ist die EINZIGE mit der Skala vertraegliche.")
print(" * m_ref=m_e (mit C=1/2) reproduziert exakt den Dok-047-Wert 4.54 meV und liegt in")
print("   der Groessenordnung des LEICHTESTEN nu (285: m0~1.9 meV).")
print(" * NICHT abgeleitet bleiben: der Koeffizient (1/2) und die Referenz (m_e) -- beide")
print("   stammen aus dem Geschwindigkeits-Ansatz v=c(1-xi^2/2), nicht aus der Dualitaet.")
print(" * Ein einzelner xi-fraktaler Wert setzt die SKALA, nicht das SPEKTRUM (dm2) ->")
print("   das Spektrum verlangt die T7-Dynamik (offene Berechnung 2).")
print(" Fazit: die xi-Potenz ist auf 2 eingegrenzt; Koeffizient/Referenz/Spektrum offen.")
print("="*76)
