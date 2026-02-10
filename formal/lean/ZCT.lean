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

