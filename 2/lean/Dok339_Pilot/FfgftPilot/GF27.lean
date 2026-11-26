/-
  Dok. 339 — Lean-Pilot: Frobenius-Trennung in GF(27)*

  Modell: GF(27) = GF(3)[x] / (x³ + 2x + 1)   (Polynom f₁ nach der
  kanonischen Tabelle von Dok. 342).

  Ein Element a₀ + a₁·x + a₂·x² (aᵢ ∈ {0,1,2}) wird als natürliche Zahl
  a₀ + 3·a₁ + 9·a₂ ∈ {0, …, 26} kodiert.  Damit sind alle Aussagen endliche
  Rechnungen, die der Lean-Prüfkern mit `decide` vollständig nachrechnet —
  keine Stichprobe, kein externes Programm, kein Mathlib.

  Kodierung der Sonderelemente:  0 ↦ 0,  1 ↦ 1,  −1 = 2 ↦ 2,  x ↦ 3.
-/

namespace FfgftPilot.GF27

/-- Koeffizienten eines kodierten Elements. -/
def d0 (a : Nat) : Nat := a % 3
def d1 (a : Nat) : Nat := a / 3 % 3
def d2 (a : Nat) : Nat := a / 9 % 3

/-- Element aus drei Koeffizienten (jeweils mod 3 reduziert). -/
def mk (c0 c1 c2 : Nat) : Nat := c0 % 3 + 3 * (c1 % 3) + 9 * (c2 % 3)

/-- Addition: koeffizientenweise mod 3. -/
def add (a b : Nat) : Nat := mk (d0 a + d0 b) (d1 a + d1 b) (d2 a + d2 b)

/-- Multiplikation modulo f₁ = x³ + 2x + 1, also mit
    x³ = x + 2   und   x⁴ = x² + 2x   (über GF(3)). -/
def mul (a b : Nat) : Nat :=
  let p0 := d0 a * d0 b
  let p1 := d0 a * d1 b + d1 a * d0 b
  let p2 := d0 a * d2 b + d1 a * d1 b + d2 a * d0 b
  let p3 := d1 a * d2 b + d2 a * d1 b
  let p4 := d2 a * d2 b
  mk (p0 + 2 * p3) (p1 + p3 + 2 * p4) (p2 + p4)

/-- Potenz aₙ = a · a · … · a. -/
def pow (a : Nat) : Nat → Nat
  | 0 => 1
  | n + 1 => mul (pow a n) a

/-- Frobenius φ(a) = a³. -/
def frob (a : Nat) : Nat := pow a 3

/-- Die 27 Elemente bzw. die 26 Einheiten. -/
def elems : List Nat := List.range 27
def units : List Nat := (List.range 27).filter (· != 0)

/-! ## Satz 1: das Modell ist ein Körper mit 27 Elementen -/

/-- f₁ hat in GF(3) keine Nullstelle; als kubisches Polynom ist es damit
    irreduzibel. -/
theorem f1_keine_Nullstelle :
    (List.range 3).all (fun t => (t ^ 3 + 2 * t + 1) % 3 != 0) = true := by
  decide +kernel

/-- Jedes von 0 verschiedene Element hat ein multiplikatives Inverses:
    das Modell ist ein Körper (|GF(27)| = 27). -/
theorem jedes_Element_invertierbar :
    units.all (fun a => elems.any (fun b => mul a b == 1)) = true := by
  decide +kernel

/-- Die Multiplikation ist kommutativ und assoziativ (vollständig über alle
    27² bzw. 27³ Kombinationen geprüft). -/
theorem mul_komm :
    elems.all (fun a => elems.all (fun b => mul a b == mul b a)) = true := by
  decide +kernel

theorem mul_assoz :
    elems.all (fun a => elems.all (fun b => elems.all (fun c =>
      mul (mul a b) c == mul a (mul b c)))) = true := by
  decide +kernel

/-- Distributivgesetz. -/
theorem distributiv :
    elems.all (fun a => elems.all (fun b => elems.all (fun c =>
      mul a (add b c) == add (mul a b) (mul a c)))) = true := by
  decide +kernel

/-! ## Satz 2: GF(27)* ist zyklisch der Ordnung 26, erzeugt von x -/

/-- x (kodiert als 3) hat genau die Ordnung 26. -/
theorem x_hat_Ordnung_26 :
    (pow 3 26 == 1 &&
      (List.range 26).all (fun k => k == 0 || pow 3 k != 1)) = true := by
  decide +kernel

/-- Jede der 26 Einheiten ist eine Potenz xᵏ mit 0 ≤ k < 26; zusammen mit
    der Ordnung 26 von x folgt GF(27)* = ⟨x⟩ ≅ ℤ₂₆. -/
theorem Potenzen_von_x_sind_alle_Einheiten :
    units.all (fun u => (List.range 26).any (fun k => pow 3 k == u)) = true := by
  decide +kernel

/-- Chinesischer Restsatz: k ↦ (k mod 2, k mod 13) ist auf {0,…,25}
    injektiv, also ℤ₂₆ ≅ ℤ₂ × ℤ₁₃. -/
theorem crt_Z26 :
    (List.range 26).all (fun j => (List.range 26).all (fun k =>
      j == k || j % 2 != k % 2 || j % 13 != k % 13)) = true := by
  decide +kernel

/-! ## Satz 3: Frobenius-Fixpunkte = {+1, −1} -/

/-- Unter den Einheiten sind genau 1 und −1 (kodiert 2) fest unter φ. -/
theorem Fixpunkte_sind_plus_minus_eins :
    units.filter (fun a => frob a == a) = [1, 2] := by
  decide +kernel

/-- Der Fixkörper ist GF(3) = {0, 1, 2}. -/
theorem Fixkoerper_ist_GF3 :
    elems.filter (fun a => frob a == a) = [0, 1, 2] := by
  decide +kernel

/-! ## Satz 4: acht Dreier-Orbits -/

/-- Jedes Nicht-Fixpunkt-Element hat einen Orbit der exakten Länge 3. -/
theorem Orbitlaenge_drei :
    units.all (fun a => frob a == a ||
      (frob (frob a) != a && frob (frob (frob a)) == a)) = true := by
  decide +kernel

/-- Es gibt genau 24 Nicht-Fixpunkte, also 24 / 3 = 8 Dreier-Orbits;
    jeder Orbit wird hier durch sein kleinstes Element vertreten. -/
theorem acht_Dreier_Orbits :
    (units.filter (fun a => frob a != a)).length = 24 ∧
    (units.filter (fun a => frob a != a &&
        a ≤ frob a && a ≤ frob (frob a))).length = 8 := by
  decide +kernel

/-- Exponenten-Bild (Dok. 339, Tabelle der ℤ₁₃-Orbits): k ↦ 3k mod 13
    zerlegt ℤ₁₃ in {0} und die vier Orbits {1,3,9}, {2,5,6}, {4,10,12},
    {7,8,11}. -/
theorem Z13_Orbits :
    [[1, 3, 9], [2, 5, 6], [4, 10, 12], [7, 8, 11]].all (fun o =>
      o.all (fun k => o.contains (3 * k % 13))) = true ∧
    3 * 0 % 13 = 0 := by
  decide +kernel

end FfgftPilot.GF27
