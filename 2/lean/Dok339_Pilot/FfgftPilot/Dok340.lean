/-
  Dok. 340 (Orbit-Algebra in ℤ₁₃) und Dok. 343, Satz D‴
  (Majorana- und Dirac-Schicht) — Lean-Prüfung

  Baut auf `FfgftPilot.GF27` (Körpermodell GF(27)) und `FfgftPilot.Dok342`
  (Polynome f₁–f₄, Minimalpolynome) auf.

  Ergebnis zur Majorana-Frage: Das Kriterium „Orbit selbstinvers unter
  k ↦ k⁻¹ (mod 13)“ arbeitet mit Exponenten und hängt damit vom gewählten
  Erzeuger g ab. Unabhängig vom Erzeuger ist nur die Aufteilung der vier
  primitiven Klassen in die Schichten {f₁, f₂} und {f₃, f₄}; welche Schicht
  „Majorana“ heißt, folgt aus der Konvention „g ist Wurzel von f₁“ (Dok. 342).
-/
import FfgftPilot.GF27
import FfgftPilot.Dok342

namespace FfgftPilot.Dok340
open FfgftPilot.GF27 FfgftPilot.Dok342

-- Grenzen für die vollständigen Durchrechnungen über alle 12 Erzeuger
set_option maxRecDepth 20000

/-! ## Dok. 340: die vier Dreier-Orbits in ℤ₁₃ -/

def O1 : List Nat := [1, 3, 9]
def O2 : List Nat := [2, 5, 6]
def O3 : List Nat := [4, 10, 12]
def O4 : List Nat := [7, 8, 11]

def summe (l : List Nat) : Nat := l.foldl (· + ·) 0
def produkt13 (l : List Nat) : Nat := l.foldl (· * ·) 1 % 13

/-- Inverses modulo 13 (für k ≠ 0). -/
def inv13 (e : Nat) : Nat := ((List.range 13).filter (fun y => e * y % 13 == 1)).headD 0

/-- Tabelle in Dok. 340: Summen 13, 13, 26, 26 und Produkte mod 13
    1, 8, 12, 5; insbesondere 4 + 10 + 12 = 26 = |GF(27)*|. -/
theorem Summen_und_Produkte :
    ([O1, O2, O3, O4].map summe == [13, 13, 26, 26] &&
     [O1, O2, O3, O4].map produkt13 == [1, 8, 12, 5]) = true := by
  decide +kernel

/-- Orbit₄ = 2⁻¹ · Orbit₁ (mod 13), mit 2⁻¹ = 7. -/
theorem Orbit4_ist_halbes_Orbit1 :
    (O1.map (fun k => 7 * k % 13) == O4 && 2 * 7 % 13 == 1) = true := by
  decide +kernel

/-- Inverse mod 13: Orbit₁ und Orbit₃ sind selbstinvers, Orbit₂ und
    Orbit₄ werden vertauscht. -/
theorem Inversen_Tabelle :
    (O1.all (fun k => O1.contains (inv13 k)) &&
     O3.all (fun k => O3.contains (inv13 k)) &&
     O2.all (fun k => O4.contains (inv13 k)) &&
     O4.all (fun k => O2.contains (inv13 k))) = true := by
  decide +kernel

/-! ## Dok. 343, Satz D‴: Abhängigkeit vom Erzeuger -/

/-- Diskreter Logarithmus von a zur Basis g in GF(27)*. -/
def dlog (a g : Nat) : Nat := ((List.range 26).filter (fun k => pow g k == a)).headD 0

/-- Wurzeln eines Polynoms in GF(27). -/
def wurzeln (f : Nat × Nat × Nat) : List Nat := units.filter (fun a => minpoly a == f)

/-- Exponenten (mod 13) der Wurzeln von f bezüglich des Erzeugers g. -/
def expo13 (f : Nat × Nat × Nat) (g : Nat) : List Nat :=
  (wurzeln f).map (fun r => dlog r g % 13)

/-- Majorana-Kriterium aus Dok. 340: der Orbit ist unter k ↦ k⁻¹ (mod 13)
    in sich abgeschlossen. -/
def selbstinvers (l : List Nat) : Bool := l.all (fun e => l.contains (inv13 e))

/-- Die Klassen, die bezüglich des Erzeugers g das Kriterium erfüllen. -/
def majorana (g : Nat) : List (Nat × Nat × Nat) :=
  [f1, f2, f3, f4].filter (fun f => selbstinvers (expo13 f g))

/-- Alle Erzeuger von GF(27)* (Elemente der Ordnung 26). -/
def erzeuger : List Nat := units.filter (fun a => hatOrdnung a 26)

/-- Unter der Konvention von Dok. 342 (g = x ist Wurzel von f₁) ist
    {f₁, f₂} die Majorana-Schicht. -/
theorem Konvention_g_Wurzel_von_f1 :
    (minpoly 3 == f1 && majorana 3 == [f1, f2]) = true := by
  decide +kernel

/-- Mit einem Erzeuger aus f₃ (g⁵) tauschen die Etiketten:
    dann erfüllen f₃, f₄ das Kriterium. -/
theorem Tausch_bei_Erzeuger_aus_f3 :
    (minpoly (pow 3 5) == f3 && majorana (pow 3 5) == [f3, f4]) = true := by
  decide +kernel

/-- Erzeugerunabhängig ist die Aufteilung: für jeden der 12 Erzeuger ist
    die Majorana-Menge entweder {f₁, f₂} oder {f₃, f₄}. -/
theorem Schichten_erzeugerunabhaengig :
    (erzeuger.length == 12 &&
     erzeuger.all (fun g => majorana g == [f1, f2] || majorana g == [f3, f4])) = true := by
  decide +kernel

/-- Das Etikett folgt genau der Klasse des Erzeugers: {f₁, f₂} ist
    Majorana-Schicht genau dann, wenn g Wurzel von f₁ oder f₂ ist. -/
theorem Etikett_folgt_Erzeugerklasse :
    erzeuger.all (fun g =>
      (majorana g == [f1, f2]) == [f1, f2].contains (minpoly g)) = true := by
  decide +kernel

/-- Quadratische Reste mod 13. -/
def qr13 : List Nat :=
  (List.range 13).filter (fun k => k != 0 && (List.range 13).any (fun x => x * x % 13 == k))

/-- Unter der Konvention sind die Exponenten der Majorana-Schicht genau die
    quadratischen Reste mod 13, die der Dirac-Schicht genau die
    Nichtreste. -/
theorem Majorana_Exponenten_quadratische_Reste :
    (qr13 == [1, 3, 4, 9, 10, 12] &&
     (expo13 f1 3 ++ expo13 f2 3).length == 6 &&
     (expo13 f1 3 ++ expo13 f2 3).all qr13.contains &&
     (expo13 f3 3 ++ expo13 f4 3).all (fun k => !qr13.contains k)) = true := by
  decide +kernel

end FfgftPilot.Dok340
