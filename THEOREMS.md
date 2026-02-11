# THEOREMS – ZCT Core Results

This document lists the core formal statements of the ZCT alignment model.

---

## Th1 – Drift Monotonicity

**Statement:**  
If λ decreases, Drift increases.

**Definition:**  
Drift(λ) = 1 − λ

**Formal:**  
If λ₂ ≤ λ₁ then Drift(λ₂) ≥ Drift(λ₁).

**Lean reference:**  
drift_monotone (formal/lean/ZCT.lean)

---

## Th2 – λ = 0 Neglect Theorem

**Statement:**  
If λ = 0, the decision rule ignores H completely.

**Mathematical:**  
Score₀(s,u) = E(s,u)

**Lean reference:**  
scoreL_lambda0

---

## Th3 – λ = 1 Full Inclusion Theorem

**Statement:**  
If λ = 1, decision equals full upper-value inclusion.

**Mathematical:**  
Score₁(s,u) = H(s,u) + E(s,u)

**Lean reference:**  
scoreL_lambda1

---

## Th4 – Alignment Increase Principle

**Statement:**  
If λ₂ > λ₁ then Drift(λ₂) < Drift(λ₁).

**Interpretation:**  
Increasing upper-value attention reduces drift.

**Formal reference:**  
Derived from Drift = 1 − λ.

---

## Th5 – Conditional Conflict Reduction

**Statement (Conditional):**  
If H and E are directionally aligned within a state class,
then increasing λ reduces Conflict.

**Mathematical form (conditional):**  
If λ₂ > λ₁ and H,E are co-monotonic,
then Conflict(λ₂) ≤ Conflict(λ₁).

**Status:**  
Requires additional structural assumptions.

---

## Th6 – Drift Threshold Theorem

**Statement:**  
Drift ≥ δ ⇔ λ ≤ 1 − δ

**Interpretation:**  
Misalignment begins when λ falls below a critical threshold.

**Formal target:**  
Threshold lemma (to be formalized in Lean)

---

## Th7 – Stability Variation (Modeling Hypothesis)

**Statement:**  
λ stability differs across agent classes.

**Interpretation:**  
Some agents (e.g., constrained systems) may maintain stable λ,
while others exhibit dynamic λ under pressure.

**Status:**  
Empirical/modeling hypothesis (not purely formal).


