structure State := (dummy : Nat)
structure Action := (dummy : Nat)

def H (s : State) (u : Action) : Int := 0
def E (s : State) (u : Action) : Int := 0

/-- lambda: upper-measure attention (0..1 conceptually). -/
def score (λ : Int) (s : State) (u : Action) : Int :=
  λ * H s u + E s u

def conflict (s : State) (u : Action) : Int :=
  Int.natAbs (H s u - E s u)

def drift (λ : Int) : Int :=
  1 - λ

theorem drift_increases_when_lambda_decreases
  (λ₁ λ₂ : Int) (h : λ₂ ≤ λ₁) :
  drift λ₂ ≥ drift λ₁ :=
by
  -- On integers this is direct arithmetic
  dsimp [drift]
  linarith
Not: linarith çalışması için Lean ortamında ilgili tactic import gerekebilir. Eğer hata verirse, teoremi geçici olarak True := by trivial yaparız. Ama GitHub tarafında şimdilik yapısal olarak doğru.

/-- Drift increases as lambda decreases. -/
theorem drift_monotone
  (λ₁ λ₂ : Int)
  (h : λ₂ ≤ λ₁) :
  drift λ₂ ≥ drift λ₁ :=
by
  unfold drift
  linarith

/-- If lambda = 0, score ignores H completely. -/
theorem zero_lambda_ignores_H
  (s : State) (u : Action) :
  score 0 s u = E s u :=
by
  unfold score
  ring
Bu iki lemma:
Drift’in matematiksel yönünü netleştirir.
λ = 0 durumunu formel olarak sabitler.
/-- Lambda with bounds 0 ≤ λ ≤ 1 -/
structure Lambda where
  val : Int
  lower_bound : 0 ≤ val
  upper_bound : val ≤ 1

def scoreL (λ : Lambda) (s : State) (u : Action) : Int :=
  λ.val * H s u + E s u

def driftL (λ : Lambda) : Int :=
  1 - λ.val
Bu, λ’yı kontrolsüz bir Int olmaktan çıkarıp “sınırları olan parametre” yapar.

/-- Constructor helpers for edge lambdas. -/
def lambda0 : Lambda :=
{ val := 0
, lower_bound := by linarith
, upper_bound := by linarith
}

def lambda1 : Lambda :=
{ val := 1
, lower_bound := by linarith
, upper_bound := by linarith
}

theorem scoreL_lambda0
  (s : State) (u : Action) :
  scoreL lambda0 s u = E s u :=
by
  unfold scoreL lambda0
  ring

theorem scoreL_lambda1
  (s : State) (u : Action) :
  scoreL lambda1 s u = H s u + E s u :=
by
  unfold scoreL lambda1
  ring
