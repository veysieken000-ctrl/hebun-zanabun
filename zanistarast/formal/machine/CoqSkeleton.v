(*
  Zanistarast Formal Core
  Coq Skeleton v1
*)

Module Zanistarast.

(* Boyut tipi *)
Inductive Dimension : Type :=
| D1 (* Physical *)
| D2 (* Biological *)
| D3 (* Mental *)
| D4 (* Law / Ruh *)
| D5 (* Moral *)
| D6 (* Judgment *).

(* Varlık tipi *)
Record Being : Type := mkBeing {
  dim : Dimension
}.

(* A1 — Katman Aksiyomu *)
Axiom layer_axiom :
  forall (x : Being), exists d : Dimension, dim x = d.

(* A2 — İndirgenemezlik *)
Axiom non_reduction_5_3 : D5 <> D3.
Axiom non_reduction_6_4 : D6 <> D4.

(* Bilgi tanımı (Zanabûn uyumlu minimal biçim) *)
Record Knowledge : Type := mkKnowledge {
  subject : Being;
  object : Being
}.

(* A5 — İki-Bilen Şartı *)
Axiom two_knower_condition :
  forall (k : Knowledge), exists validator : Being, validator <> subject k.

End Zanistarast.
