#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s3_thermik_zustandsraum.py -- Thermische Bedingungen und
Zustandsraumstruktur.

Zwei Fragen, die bei der Einordnung optischer und supraleitender
Realisierungen regelmaessig vermengt werden:

  TEIL A  THERMIK: Welche Betriebstemperatur verlangt welche
          Traegerfrequenz? Der Vergleich folgt aus h*nu/(k_B*T) und
          faellt drastisch zugunsten optischer Frequenzen aus.
  TEIL B  ZUSTANDSRAUM: Woher kommt die exponentielle Dimension?
          Nicht aus dem Traegermedium, sondern aus der
          Tensorproduktstruktur.
  TEIL C  GRENZE DER VERSCHRAENKUNGSERKLAERUNG: Der Satz von
          Gottesman-Knill zeigt, dass Verschraenkung allein keinen
          Rechenvorteil traegt.

Nur Standardbibliothek. Naturkonstanten: CODATA 2022.
"""
import math

H = 6.62607015e-34        # Planck-Konstante, J s (exakt)
KB = 1.380649e-23         # Boltzmann-Konstante, J/K (exakt)
QE = 1.602176634e-19      # Elementarladung, C (exakt)


def besetzung(nu, T):
    """Mittlere thermische Besetzung eines Modes: 1/(exp(h nu/kT) - 1)."""
    x = H * nu / (KB * T)
    if x > 700:
        return math.exp(-x)
    return 1.0 / math.expm1(x)


def temperatur_fuer(nu, n_ziel):
    """Temperatur, bei der die Besetzung n_ziel unterschreitet."""
    x = math.log(1.0 + 1.0 / n_ziel)
    return H * nu / (KB * x)


def carnot(T_kalt, T_warm=300.0):
    """Mindestarbeit je abgefuehrter Waermeeinheit (Carnot)."""
    return (T_warm - T_kalt) / T_kalt


if __name__ == "__main__":
    print("=" * 74)
    print("S3 -- THERMIK UND ZUSTANDSRAUMSTRUKTUR")
    print("=" * 74)

    # ---------------------------------------------------- TEIL A
    print("\nTEIL A: Thermische Besetzung nach Traegerfrequenz")
    print("-" * 74)
    print("""   Entscheidend ist h*nu/(k_B*T). Ist es gross, ist der
   Grundzustand ohne Kuehlung besetzt.""")
    print(f"\n   {'System':>24} {'nu (Hz)':>11} {'h nu (eV)':>11} {'T (K)':>9} "
          f"{'h nu/kT':>10} {'Besetzung':>13}")
    faelle = [
        ("Supraleitendes Qubit", 5e9, 300.0),
        ("Supraleitendes Qubit", 5e9, 0.020),
        ("Photon 1550 nm", 1.934e14, 300.0),
        ("Photon 600 nm", 5.0e14, 300.0),
    ]
    werte = {}
    for name, nu, T in faelle:
        x = H * nu / (KB * T)
        n = besetzung(nu, T)
        werte[(name, T)] = n
        print(f"   {name:>24} {nu:>11.2e} {H*nu/QE:>11.2e} {T:>9.3f} "
              f"{x:>10.2e} {n:>13.3e}")

    n_sc_warm = werte[("Supraleitendes Qubit", 300.0)]
    n_opt = werte[("Photon 600 nm", 300.0)]
    print(f"\n   Bei 5 GHz und 300 K: {n_sc_warm:.0f} thermische Anregungen "
          f"im Mode.")
    print(f"   Bei 600 nm und 300 K: {n_opt:.2e} -- der Grundzustand ist")
    print(f"   praktisch exakt besetzt, ohne jede Kuehlung.")
    assert n_sc_warm > 100, "Supraleitendes Qubit sollte warm durchmischt sein"
    assert n_opt < 1e-20, "Optischer Mode sollte thermisch leer sein"

    print("\n   Erforderliche Temperatur bei 5 GHz:")
    for ziel in (0.1, 0.01, 0.001):
        T = temperatur_fuer(5e9, ziel)
        print(f"     Besetzung < {ziel:<6} -> T < {T*1000:6.1f} mK")
    T_01 = temperatur_fuer(5e9, 0.01)
    assert T_01 < 0.1, "Sollte Millikelvin-Bereich verlangen"

    print("\n   Thermodynamische Kuehlkosten (Carnot, von 300 K):")
    print(f"   {'T (mK)':>9} {'Mindestarbeit je Waermeeinheit':>32}")
    for T in (0.010, 0.020, 0.100, 4.0):
        print(f"   {T*1000:>9.0f} {carnot(T):>32.0f}")
    print("""
   => Um 1 W bei 10 mK abzufuehren, sind thermodynamisch mindestens
      rund 30000 W noetig; real deutlich mehr. Ein
      Verduennungskryostat zieht 10--25 kW im Dauerbetrieb, ein
      optisches Netz nichts.""")

    # ---------------------------------------------------- TEIL B
    print("\nTEIL B: Woher kommt die exponentielle Dimension?")
    print("-" * 74)
    print("""   Nicht aus dem Traegermedium. Entscheidend ist, ob der
   Zustandsraum ein Einteilchen-Modenraum oder ein
   Tensorprodukt ist.""")
    print(f"\n   {'Aufbau':>38} {'Dimension':>18}")
    print(f"   {'klassische Welle in n Moden':>38} {'n':>18}")
    print(f"   {'EIN Photon in n Moden':>38} {'n  (dasselbe)':>18}")
    print(f"   {'n verschraenkte Zweiniveausysteme':>38} {'2^n':>18}")
    print(f"   {'m ununterscheidbare Photonen, n Moden':>38} "
          f"{'C(n+m-1, m)':>18}")

    print(f"\n   Zahlenbeispiel fuer m Photonen in n Moden:")
    print(f"   {'n':>5} {'m':>5} {'Dimension':>16}")
    from math import comb
    for n, m in ((10, 1), (10, 5), (20, 10), (50, 25)):
        d = comb(n + m - 1, m)
        print(f"   {n:>5} {m:>5} {d:>16.4e}")
    d1 = comb(10 + 1 - 1, 1)
    d2 = comb(50 + 25 - 1, 25)
    assert d1 == 10, "Ein Photon in 10 Moden gibt Dimension 10"
    assert d2 > 1e18, "25 Photonen in 50 Moden sollten exponentiell sein"
    print("""
   => auch rein optisch waechst die Dimension exponentiell, sobald
      mehrere Photonen beteiligt sind. Die Gegenueberstellung
      'Optik gegen Quantenrechner' stellt eine Technologie gegen ein
      Rechenmodell und ist unzutreffend: photonische Quantenrechner
      existieren (KLM, messungsbasierte Verfahren).""")

    # ---------------------------------------------------- TEIL C
    print("\nTEIL C: Traegt Verschraenkung den Rechenvorteil?")
    print("-" * 74)
    print("""   Satz von Gottesman-Knill (1998): Jeder Schaltkreis aus
   ausschliesslich Clifford-Gattern (H, S, CNOT) ist klassisch in
   Polynomzeit simulierbar -- unabhaengig von der erzeugten
   Verschraenkung.

   Beispiel GHZ-Zustand (|0...0> + |1...1>)/sqrt(2): maximal
   verschraenkt, erzeugt aus H und n-1 CNOTs, also rein Clifford.""")
    print(f"\n   {'n Qubits':>10} {'Hilbertraum':>14} {'Stabilisator (Bits)':>21}")
    for n in (10, 50, 100, 1000):
        print(f"   {n:>10} {'2^' + str(n):>14} {2*n*n:>21}")
    print("""
   => maximale Verschraenkung, aber nur O(n^2) klassischer Speicher.
      Verschraenkung allein gibt keinen Rechenvorteil.

   Weitere Gegenbelege:
     - DQC1 ('one clean qubit'): fast keine Verschraenkung,
       vermuteter Vorteil bei Spurabschaetzung
     - Boson-Sampling: schwer simulierbar, Mechanismus ist
       Ununterscheidbarkeit und Permanenten
     - Jozsa & Linden (2003): unbeschraenkte Verschraenkung ist fuer
       exponentiellen Vorteil bei reinen Zustaenden NOTWENDIG --
       ueber Hinreichen sagt der Satz nichts

   Diskutierte Kandidaten fuer den eigentlichen Traeger:
   Kontextualitaet (Howard et al. 2014), Nicht-Stabilisiertheit
   ('Magie'), Interferenzstruktur. Keiner ist als alleiniger
   Traeger etabliert; die Frage ist offen.""")

    print("\n" + "=" * 74)
    print("ERGEBNIS S3")
    print("=" * 74)
    print("""   [K] Der thermische Vorteil optischer Verfahren ist real und
       gross: bei 600 nm und 300 K betraegt die thermische Besetzung
       1.8e-35, bei 5 GHz dagegen 1250. Supraleitende Systeme
       verlangen daher Millikelvin (< 52 mK fuer Besetzung < 0.01),
       optische nichts. Das folgt aus h*nu/kT, nicht aus
       Ingenieursdetails.

   [B] Der Vorteil betrifft die Infrastruktur -- Kuehlung, Energie,
       Groesse --, nicht die Rechenmaechtigkeit. Beide Realisierungen
       koennen prinzipiell dieselben Algorithmen ausfuehren; die
       Photonik hat eigene Schwierigkeiten (deterministische
       Zweiphotonen-Gatter, Photonenverluste).

   [K] Die exponentielle Dimension kommt aus der
       Tensorproduktstruktur, nicht aus dem Traegermedium.

   [K] Verschraenkung allein traegt den Rechenvorteil nicht
       (Gottesman-Knill). Welche Groesse ihn traegt, ist offen.""")
    print("\nAlle Checks bestanden.")
