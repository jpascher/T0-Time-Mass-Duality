/-
  Dok. 342 (Satz A, Satz B) und Dok. 343 (Satz E) — Lean-Prüfung

  Baut auf dem GF(27)-Modell aus `FfgftPilot.GF27` auf
  (GF(3)[x]/(x³+2x+1), Erzeuger g = x, kodiert als 3).

  Ein normiertes kubisches Polynom x³ + a·x² + b·x + c über GF(3) wird als
  Tripel (a, b, c) mit a, b, c ∈ {0, 1, 2} geschrieben.
-/
import FfgftPilot.GF27

namespace FfgftPilot.Dok342
open FfgftPilot.GF27

/-! ## Satz A: die acht irreduziblen kubischen Polynome über GF(3) -/

/-- Ein kubisches Polynom ist über GF(3) genau dann irreduzibel, wenn es
    keine Nullstelle in GF(3) hat. -/
def irreduzibel (p : Nat × Nat × Nat) : Bool :=
  (List.range 3).all fun t => (t ^ 3 + p.1 * t ^ 2 + p.2.1 * t + p.2.2) % 3 != 0

/-- Alle 27 normierten Kubiken. -/
def kubiken : List (Nat × Nat × Nat) :=
  (List.range 3).flatMap fun a => (List.range 3).flatMap fun b =>
    (List.range 3).map fun c => (a, b, c)

/-- Tabelle aus Dok. 342. -/
def f1 : Nat × Nat × Nat := (0, 2, 1)   -- x³ + 2x + 1
def f2 : Nat × Nat × Nat := (2, 0, 1)   -- x³ + 2x² + 1
def f3 : Nat × Nat × Nat := (2, 1, 1)   -- x³ + 2x² + x + 1
def f4 : Nat × Nat × Nat := (1, 2, 1)   -- x³ + x² + 2x + 1
def g1 : Nat × Nat × Nat := (0, 2, 2)   -- x³ + 2x + 2
def g2 : Nat × Nat × Nat := (1, 0, 2)   -- x³ + x² + 2
def g3 : Nat × Nat × Nat := (1, 1, 2)   -- x³ + x² + x + 2
def g4 : Nat × Nat × Nat := (2, 2, 2)   -- x³ + 2x² + 2x + 2

/-- Es gibt genau acht irreduzible normierte Kubiken, und es sind genau die
    acht Polynome der Tabelle in Dok. 342. -/
theorem genau_acht_irreduzible :
    (kubiken.filter irreduzibel).length = 8 ∧
    [f1, f2, f3, f4, g1, g2, g3, g4].all
      (fun p => (kubiken.filter irreduzibel).contains p) = true := by
  decide +kernel

/-! ## Minimalpolynome in GF(27) -/

def neg (a : Nat) : Nat := mul a 2

/-- Minimalpolynom von a über GF(3): (x − a)(x − a³)(x − a⁹), als Tripel
    (−e₁, e₂, −e₃) der elementarsymmetrischen Funktionen. -/
def minpoly (a : Nat) : Nat × Nat × Nat :=
  let r1 := a
  let r2 := frob r1
  let r3 := frob r2
  (neg (add (add r1 r2) r3),
   add (add (mul r1 r2) (mul r1 r3)) (mul r2 r3),
   neg (mul (mul r1 r2) r3))

/-- Ordnung von a in GF(27)* ist genau n. -/
def hatOrdnung (a n : Nat) : Bool :=
  pow a n == 1 && (List.range n).all (fun j => j == 0 || pow a j != 1)

/-- Die vier primitiven Polynome sind die Frobenius-Klassen eines Erzeugers
    g (Wurzel von f₁): f₁ = {g, g³, g⁹}, f₂ = {g¹⁷, g²³, g²⁵},
    f₃ = {g⁵, g¹⁵, g¹⁹}, f₄ = {g⁷, g¹¹, g²¹}; alle Wurzeln haben Ordnung 26. -/
theorem primitive_Klassen :
    [([1, 3, 9], f1), ([17, 23, 25], f2), ([5, 15, 19], f3), ([7, 11, 21], f4)].all
      (fun (o, f) => o.all (fun k =>
        minpoly (pow 3 k) == f && hatOrdnung (pow 3 k) 26)) = true := by
  decide +kernel

/-- Die gᵢ sind die Vorzeichenpartner: ihre Wurzeln sind −gᵏ = gᵏ⁺¹³ für
    die Exponenten von fᵢ, und sie haben Ordnung 13. -/
theorem Ordnung13_Klassen :
    [([1, 3, 9], g1), ([17, 23, 25], g2), ([5, 15, 19], g3), ([7, 11, 21], g4)].all
      (fun (o, g) => o.all (fun k =>
        pow 3 (k + 13) == neg (pow 3 k) &&
        minpoly (pow 3 ((k + 13) % 26)) == g &&
        hatOrdnung (pow 3 ((k + 13) % 26)) 13)) = true := by
  decide +kernel

/-- Vollständigkeit: jedes der 24 Nicht-Fixpunkt-Elemente von GF(27)* hat
    eines der acht Polynome als Minimalpolynom. -/
theorem jede_Einheit_hat_Tabellenpolynom :
    units.all (fun a => frob a == a ||
      [f1, f2, f3, f4, g1, g2, g3, g4].contains (minpoly a)) = true := by
  decide +kernel

/-- Sektorpaarung k ↦ −k (mod 26) vertauscht f₁ ↔ f₂ und f₃ ↔ f₄. -/
theorem Sektorpaarung :
    (([1, 3, 9].map (fun k => (26 - k) % 26) == [25, 23, 17]) &&
     ([5, 15, 19].map (fun k => (26 - k) % 26) == [21, 11, 7])) = true := by
  decide +kernel

/-! ## Satz B (Dok. 342) / Satz E (Dok. 343): Eintritt der Primzahlen -/

/-- Primzahltest durch Probedivision. -/
def prim (q : Nat) : Bool :=
  2 ≤ q && (List.range q).all (fun d => d < 2 || q % d != 0)

/-- Vollständige Zerlegungen von 3ᵏ − 1 für k = 3 … 6 (alle Faktoren prim). -/
theorem Zerlegungen :
    ((3 ^ 3 - 1 == 2 * 13) && (3 ^ 4 - 1 == 2 ^ 4 * 5) &&
     (3 ^ 5 - 1 == 2 * 11 ^ 2) && (3 ^ 6 - 1 == 2 ^ 3 * 7 * 13) &&
     [2, 5, 7, 11, 13].all prim) = true := by
  decide +kernel

/-- Endliche Kernaussagen: für q ≤ 3ᵏ ist die einzige Primzahl mit
    ord_q(3) = k genau 13, 5, 11 bzw. 7. -/
theorem Eintritt_endlich :
    (∀ q, q < 28 → 27 % q = 1 → prim q = true → 3 % q ≠ 1 → 9 % q ≠ 1 → q = 13) ∧
    (∀ q, q < 82 → 81 % q = 1 → prim q = true → 3 % q ≠ 1 → 9 % q ≠ 1 →
        27 % q ≠ 1 → q = 5) ∧
    (∀ q, q < 244 → 243 % q = 1 → prim q = true → 3 % q ≠ 1 → 9 % q ≠ 1 →
        27 % q ≠ 1 → 81 % q ≠ 1 → q = 11) ∧
    (∀ q, q < 730 → 729 % q = 1 → prim q = true → 3 % q ≠ 1 → 9 % q ≠ 1 →
        27 % q ≠ 1 → 81 % q ≠ 1 → 243 % q ≠ 1 → q = 7) := by
  decide +kernel

/-- Hilfssatz: ist N % q = 1 mit N ≥ 2, so ist q ≤ N (sonst wäre N % q = N). -/
theorem schranke (N q : Nat) (hN : 2 ≤ N) (h : N % q = 1) : q < N + 1 := by
  cases Nat.lt_or_ge N q with
  | inl hlt =>
    rw [Nat.mod_eq_of_lt hlt] at h
    omega
  | inr hge => omega

/-- Satz E (Dok. 343): 13 ist die einzige Primzahl mit ord_p(3) = 3 —
    für alle natürlichen Zahlen, ohne Schranke. -/
theorem nur_13_hat_Ordnung_3 (p : Nat) (hp : prim p = true)
    (h3 : 27 % p = 1) (h1 : 3 % p ≠ 1) (h2 : 9 % p ≠ 1) : p = 13 :=
  Eintritt_endlich.1 p (schranke 27 p (by decide) h3) h3 hp h1 h2

/-- Ebenso: 5 ist die einzige Primzahl mit ord_p(3) = 4. -/
theorem nur_5_hat_Ordnung_4 (p : Nat) (hp : prim p = true)
    (h4 : 81 % p = 1) (h1 : 3 % p ≠ 1) (h2 : 9 % p ≠ 1) (h3 : 27 % p ≠ 1) :
    p = 5 :=
  Eintritt_endlich.2.1 p (schranke 81 p (by decide) h4) h4 hp h1 h2 h3

/-- 11 ist die einzige Primzahl mit ord_p(3) = 5. -/
theorem nur_11_hat_Ordnung_5 (p : Nat) (hp : prim p = true)
    (h5 : 243 % p = 1) (h1 : 3 % p ≠ 1) (h2 : 9 % p ≠ 1) (h3 : 27 % p ≠ 1)
    (h4 : 81 % p ≠ 1) : p = 11 :=
  Eintritt_endlich.2.2.1 p (schranke 243 p (by decide) h5) h5 hp h1 h2 h3 h4

/-- 7 ist die einzige Primzahl mit ord_p(3) = 6. -/
theorem nur_7_hat_Ordnung_6 (p : Nat) (hp : prim p = true)
    (h6 : 729 % p = 1) (h1 : 3 % p ≠ 1) (h2 : 9 % p ≠ 1) (h3 : 27 % p ≠ 1)
    (h4 : 81 % p ≠ 1) (h5 : 243 % p ≠ 1) : p = 7 :=
  Eintritt_endlich.2.2.2 p (schranke 729 p (by decide) h6) h6 hp h1 h2 h3 h4 h5

end FfgftPilot.Dok342
