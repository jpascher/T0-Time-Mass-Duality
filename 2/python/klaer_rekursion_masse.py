import numpy as np
np.set_printoptions(precision=6, suppress=True)
print("="*74)
print(" Warum die Rekursionsrichtungen leer sind — und was beim Ausrollen Masse trägt")
print("="*74)

# ---------------------------------------------------------------------------
# (1) Masse sitzt im 4D-Keim (Z3-Zirkulant), NICHT in Dimensionen
# ---------------------------------------------------------------------------
print("\n(1) Der Massengehalt sitzt im 4D-Keim: Z3-Zirkulant aus r=sqrt2, theta=2/9")
r, th = np.sqrt(2), 2/9
# Foot/Koide-Parametrisierung: sqrt(m_k) ~ 1 + r*cos(theta + 2*pi*k/3)
sq = np.array([1 + r*np.cos(th + 2*np.pi*k/3) for k in range(3)])
mu = sq / sq.sum() * 3.0            # auf Sum(mu)=3 normiert (reine Konvention)
mu = np.sort(mu)
print("   mu_k (dimensionslos) =", mu)
print("   Sum mu  =", round(mu.sum(),6), " (->3)")
print("   Sum mu^2=", round((mu**2).sum(),6), " (->6)")
print("   Koide Q = Sum mu^2 / (Sum mu)^2 =", round((mu**2).sum()/mu.sum()**2,6), " (2/3=%.6f)"%(2/3))
print("   Massenverhaeltnis  m_mu/m_e = (mu2/mu0)^2 =", round((mu[1]/mu[0])**2,3))
print("   => Alle Verhaeltnisse stehen im 4D-Z3-Keim. KEINE Extra-Dimension noetig.")

# ---------------------------------------------------------------------------
# (2) Die DIMENSIONALE Rekursion (golden, 3+3'): innerer Zweig -> leer
# ---------------------------------------------------------------------------
print("\n(2) Dimensionale Rekursion D(4+3n): goldener Operator M=[[1,1],[1,0]]")
M = np.array([[1.0,1.0],[1.0,0.0]])
ev = np.linalg.eigvalsh(M)
phi = (1+np.sqrt(5))/2
print("   Eigenwerte:", np.sort(ev), "  = {-1/phi, phi} =", [round(-1/phi,4), round(phi,4)])
print("   3  = phi-Mode (expandierend, |phi|>1)  -> physisch (Keim)")
print("   3' = -1/phi-Mode (kontrahierend, |..|<1) -> Fenster")
print("   Turm: Gewicht der n-ten Fenster-Etage ~ (1/phi)^(2n):")
for n in range(0,5):
    print(f"     n={n} (D={4+3*n}):  inneres Gewicht (1/phi^2)^n = {(1/phi**2)**n:.5f}")
print("   => jede +3-Etage ist ein -1/phi-Fenster; das Gewicht zerfaellt -> kein Punktspektrum.")

# ---------------------------------------------------------------------------
# (3) Die SKALEN-/fraktale Rekursion (xi^n) ist eine ANDERE Rekursion: in 4D
# ---------------------------------------------------------------------------
print("\n(3) Skalen-/fraktale Rekursion xi_{n+1}=xi_n(1-100 xi_n): KEINE neuen Dimensionen")
xi = 4/30000
x = xi; 
print("   xi =", xi, " D_f^Raum = 3-xi =", 3-xi)
print("   Log-Periode der Dilatation |ln xi| = ln 7500 =", round(np.log(7500),4))
print("   (zum Vergleich goldene Skala: ln phi =", round(np.log(phi),4),")")
print("   => das ist eine Verfeinerung DER SELBEN 4 Dimensionen ueber Skalen,")
print("      nicht das Hinzufuegen von Dimensionen. Traegt D_f / K_frak, keine neuen Massen.")

# ---------------------------------------------------------------------------
# (4) Auflösung: was beim Ausrollen Masse traegt = der MASSE-KREIS (D4), nicht 3'
# ---------------------------------------------------------------------------
print("\n(4) Ausrollen: Verhaeltnisse(4D) x Skala M(Masse-Kreis) = absolute Massen")
m_mu = 105.6583755                 # MeV, eine gemessene Masse fixiert die Skala
M_scale = m_mu / mu[1]**2          # M = 1/T  aus dem Masse-Kreis (Typ-I-Ausrollen)
print("   Skala aus Masse-Kreis:  M = m_mu/mu_mu^2 =", round(M_scale,3), "MeV")
for nme,mk in zip(["e","mu","tau"], mu):
    print(f"     m_{nme} = mu^2 * M = {mk**2*M_scale:8.4f} MeV")
print("   => 'Masse beim Ausrollen' kommt vom Aufrollen des MASSE-KREISES (4. Kreis von D4),")
print("      der die EINE Skala M=1/T liefert. Die Verhaeltnisse lagen schon kompakt in 4D.")

# ---------------------------------------------------------------------------
# (5) Warum das Ausrollen der 3'/3''-Fenster KEINE Masse gibt
# ---------------------------------------------------------------------------
print("\n(5) Das Ausrollen der Rekursions-Fenster (3',3'') gibt keine Masse:")
print("   - Fenster = Perp-Raum (Cut-and-Project), kontrahierend (-1/phi), Gewicht -> 0")
print("   - kein Punktspektrum => keine scharfen Niveaus => keine KK-Massenleiter")
print("   - um Masse ins Fenster zu legen braeuchte es eine DYNAMIK (Hamiltonian/WW),")
print("     nicht blosses Ausrollen. Geometrie/Rekursion allein liefert das nicht.")
print("\n"+"="*74)
print(" FAZIT: 'Rekursionstiefe' wird in ZWEI Bedeutungen benutzt --")
print("   A) Skalen-Tiefe (xi^n): verfeinert die SELBEN 4D, traegt D_f/K_frak  [fraktale Vertiefung]")
print("   B) Dimensions-Tiefe (D(4+3n), phi^n): fuegt leere Fenster (3',3'') hinzu  [HLV-Einbettung]")
print(" Johanns Kaluza-Klein-Intuition (Extra-Dim ausrollen -> Massenleiter) gilt fuer")
print(" einen MASSE-tragenden Kreis -- das ist der 4. Kreis von D4 (Masse-Kreis), NICHT 3'/3''.")
print(" Der Masse-Kreis ausgerollt -> Skala M. Die 3'/3''-Fenster ausgerollt -> leerer Perp-Raum.")
print("="*74)
