structure State :=
  (dummy : Nat)

structure Action :=
  (dummy : Nat)

def H (s : State) (u : Action) : Int := 0
def E (s : State) (u : Action) : Int := 0
def G (s : State) (u : Action) : Int := 0

def score (α β γ : Int) (s : State) (u : Action) : Int :=
  α * H s u + β * E s u + γ * G s u

def conflict (s : State) (u : Action) : Int :=
  Int.natAbs (H s u - E s u)

theorem higher_alpha_reduces_drift
  (α₁ α₂ β γ : Int)
  (h : α₂ ≥ α₁) :
  True :=
by
  trivial
Bu minimal çekirdek; ileride gerçek lemma yazılacak.

