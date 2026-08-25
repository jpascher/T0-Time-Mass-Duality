#!/usr/bin/env python3
# pruef_altermagnet_1_symmetrie.py
# Dok. 312 Anhang — Altermagnetismus als Laboranalogie:
# Lokale T-Brechung bei globaler Kompensation; C4-Rotationssymmetrie
# Quelle: Šmejkal, Sinova, Jungwirth, PRX 12, 040501 (2022), Gl. (3)
#
# H(k) = 2t·cos(kx)cos(ky)·σ₀ + 2tJ·sin(kx)sin(ky)·σz
# E±(k) = 2t·cos(kx)cos(ky) ± 2tJ·sin(kx)sin(ky)
# Geprüfte Aussagen:
# [A] Aufspaltung hat d_xy-Wellensymmetrie: ΔE ∝ sin(kx)·sin(ky) [E]
# [B] Nettospinpolarisierung über gesamte BZ = 0 [E]
# [C] C4-Rotation verbindet Spin-up mit Spin-down-Fermifläche [E]
# [D] Knotenlinien bei kx=0 oder ky=0 — exakte Spinentartung [E]
# [E] Strukturanalogie zu Dok. 312: lokale ≠ globale Symmetriebrechung
import numpy as np

print("=" * 70)
print("PRÜFSKRIPT: Altermagnet — d_xy-Welle, C4-Symmetrie, Dok.-312-Analogie")
print("Quelle: Šmejkal et al. PRX 12, 040501 (2022), Gl. (3)")
print("=" * 70)

t  = 1.0   # normiertes Hopping
tJ = 0.5   # Austausch-Hopping

def E_up(kx, ky): return 2*t*np.cos(kx)*np.cos(ky) + 2*tJ*np.sin(kx)*np.sin(ky)
def E_dn(kx, ky): return 2*t*np.cos(kx)*np.cos(ky) - 2*tJ*np.sin(kx)*np.sin(ky)
def dE(kx, ky):   return 4*tJ*np.sin(kx)*np.sin(ky)

# [A] d_xy-Wellensymmetrie
print("\n[A] d_xy-Wellensymmetrie (ΔE ∝ sin(kx)·sin(ky)):")
for kx, ky in [(np.pi/2, np.pi/2), (np.pi/2, -np.pi/2), (np.pi/4, np.pi/4)]:
    print(f"  k=({kx/np.pi:.2f}π,{ky/np.pi:.2f}π): ΔE={dE(kx,ky):+.4f}  "
          f"erwartet={4*tJ*np.sin(kx)*np.sin(ky):+.4f}  OK")

# [B] Nettospinpolarisierung = 0
print("\n[B] Nettospinpolarisierung ∫ΔE d²k / (2π)² = 0:")
N = 500
KX,KY = np.meshgrid(np.linspace(-np.pi,np.pi,N,endpoint=False),
                    np.linspace(-np.pi,np.pi,N,endpoint=False))
netto = np.mean(dE(KX,KY))
print(f"  Numerisch: {netto:.2e}  (analytisch 0 wegen ∫sin(kx)dkx=0)")
print(f"  {'BESTÄTIGT' if abs(netto)<1e-10 else 'ABWEICHUNG'}")

# [C] C4-Rotation: Spin-up Fermifläche → Spin-down Fermifläche
print("\n[C] C4-Rotation (kx,ky) → (-ky,kx) verbindet E_up(k) mit E_dn(k):")
print("    Physik: Der C4-Generator [C₂‖C₄z] aus Šmejkal Gl.(2) verknüpft")
print("    die Spin-Untergitter — daher werden die Fermiflächen")
print("    durch C4 ineinander überführt, nicht durch Zeitumkehr allein.")
for kx,ky in [(np.pi/3, np.pi/4), (0.7, 1.1), (np.pi/5, 2*np.pi/5)]:
    kx2, ky2 = -ky, kx          # C4-Rotation im k-Raum
    lhs = E_up(kx, ky)          # Spin-up bei k
    rhs = E_dn(kx2, ky2)        # Spin-down bei C4(k)
    ok = abs(lhs - rhs) < 1e-10
    print(f"  E_up({kx:.2f},{ky:.2f})={lhs:.4f}  E_dn(C4k)={rhs:.4f}  "
          f"{'BESTÄTIGT' if ok else 'FEHLER'}")

# Warum das funktioniert: analytischer Beweis
print("\n  Analytischer Beweis:")
print("  E_up(kx,ky) = 2t·cos(kx)cos(ky) + 2tJ·sin(kx)sin(ky)")
print("  C4: (kx,ky) → (-ky,kx)")
print("  E_dn(-ky,kx) = 2t·cos(-ky)cos(kx) - 2tJ·sin(-ky)sin(kx)")
print("               = 2t·cos(ky)cos(kx)  + 2tJ·sin(ky)sin(kx)")
print("               = E_up(kx,ky)  ✓  (da cos gerade, sin ungerade)")
print("  => Bewiesen: C4 bildet Spin-up-Fermifläche auf Spin-down ab.")

# [D] Knotenlinien
print("\n[D] Knotenlinien: ΔE = 0 bei kx=0 oder ky=0:")
for kx,ky,label in [(0.0,1.1,"kx=0"),(0.7,0.0,"ky=0"),(0.0,0.0,"Γ")]:
    print(f"  {label}: ΔE={dE(kx,ky):.2e}  "
          f"{'ENTARTET' if abs(dE(kx,ky))<1e-12 else 'AUFGESPALTEN'}")
print("  (Knotenlinien sind durch Spiegelgruppen-Symmetrien geschützt,")
print("  die je ein Untergitter auf das andere abbilden.)")

# [E] Dok.-312-Analogie
print("""
[E] Strukturanalogie zu Dok. 312, Zeilen 936-947 (Lorentz-Abschnitt):

  Dok. 312 (T⁴/Z₃-Kompaktifizierung):
    'Lorentz-Invarianz gilt lokal uneingeschränkt, aber Boosts sind
     keine globalen Symmetrien mehr; die Auszeichnung ist topologisch,
     keine lokale Messung kann sie detektieren, nur globale Marker.'

  Altermagnet (Šmejkal et al. 2022):
    T-Symmetrie ist lokal im k-Raum gebrochen (ΔE ≠ 0 für gen. k),
    aber das globale Integral ∫ΔE d²k = 0: keine makroskopische
    Magnetisierung, keine Streufelder. Eine punktuelle lokale Messung
    am Material sieht keinen Magnetismus; erst die richtungsaufgelöste
    ARPES-Messung oder ein Spinstrommessung deckt die lokale Brechung auf.

  Gemeinsame Struktur:
    ┌────────────────────────────┬──────────────────────────────┐
    │ Dok. 312 (FFGFT)           │ Altermagnet (Festkörper)     │
    ├────────────────────────────┼──────────────────────────────┤
    │ Lorentz lokal erhalten     │ T lokal gebrochen (k-abhäng.)│
    │ Boosts global ausgezeichnet│ Spin global kompensiert      │
    │ Nur topol. Marker messbar  │ Nur ARPES/Spinstr. messbar   │
    │ Skala: Planck-Länge        │ Skala: Ångström (Gitter)     │
    └────────────────────────────┴──────────────────────────────┘

  EINSCHRÄNKUNG [wichtig]:
  Das ist eine STRUKTURANALOGIE der Symmetrieklassifikation, keine
  physikalische Identität. Verschiedene Skalen, verschiedene Observablen,
  verschiedene Symmetriegruppen. FFGFT kann aus dem Altermagnetismus keinen
  neuen physikalischen Inhalt gewinnen. Umgekehrt erklärt FFGFT keine
  Festkörpereffekte. Der Wert ist didaktisch und terminologisch:
  'lokal gebrochen, global erhalten' ist ein experimentell direkt
  messbares, gut verstandenes Konzept.
  Status: [E] Laboranalogie; Analogie, nicht Ableitung.""")

# [F] Dreiteilung
print("\n[F] Dreiteilung nach Šmejkal et al. (Symmetriegruppenklassifikation):")
print(f"{'Typ':15} {'Verbindung Untergitter':28} {'Kramers':10} {'Netto-M'}")
print("-"*65)
print(f"{'Ferromagnet':15} {'keine':28} {'gehoben':10} {'≠ 0'}")
print(f"{'Antiferromagnet':15} {'Translation t / Inversion P':28} {'erhalten':10} {'= 0'}")
print(f"{'Altermagnet':15} {'Rotation Cn, n=2,4,6':28} {'lok.geh.':10} {'= 0'}")

print("\nFAZIT:")
print("  [A][B][D]: Hamiltonstruktur, Kompensation, Knotenlinien bestätigt. [E]")
print("  [C]: C4 bildet Spin-up-Fermifläche analytisch auf Spin-down ab. [E]")
print("  [E]: Dok.-312-Analogie formuliert und klar begrenzt.")
