/- 
Zanistarast Formal Core
Lean Skeleton v1
-/

namespace Zanistarast

-- Boyut tipi
inductive Dimension
| D1 -- Physical
| D2 -- Biological
| D3 -- Mental
| D4 -- Law / Ruh
| D5 -- Moral
| D6 -- Judgment

-- Varlık tipi
structure Being :=
(dim : Dimension)

-- A1 — Katman Aksiyomu
axiom layer_axiom :
∀ (x : Being), ∃ (d : Dimension), x.dim = d

-- A2 — İndirgenemezlik
axiom non_reduction_5_3 :
¬ (Dimension.D5 = Dimension.D3)

axiom non_reduction_6_4 :
¬ (Dimension.D6 = Dimension.D4)

-- A5 — İki-Bilen
structure Knowledge :=
(subject : Being)
(object : Being)

axiom two_knower_condition :
∀ (k : Knowledge),
∃ (validator : Being), validator ≠ k.subject

end Zanistarast
