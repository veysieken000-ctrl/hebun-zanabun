# Concentration Risk Calibration Guide
## Zanistarast Governance Measurement Layer

This document defines how to measure and calibrate
power concentration risk in a culturally adaptive way.

The goal is a measurable early-warning system
that protects the governance model from drift.

---

## Purpose

Risk measurement is not a replacement for morality.
It is a structural alarm mechanism.

A system may appear ethical while drifting into concentration.
This guide is designed to detect that drift early.

---

## Risk Function

We define concentration risk as:

R_c = w_C * C + w_T * T_avg + w_O * O + w_I * I

Where:
- C is the centralization ratio
- T_avg is average tenure
- O is the opacity index
- I is the authority overlap ratio
- w_* are weights chosen by each society

The weights are culturally adjustable.
The measurement definitions are invariant.

---

## Measurement Definitions

Centralization ratio (C)

Meaning:
How much decision authority is concentrated in the strongest council
relative to the whole system.

Recommended measurement:
C = max_i P(C_i) / Σ P(C_j)

Interpretation:
- higher means stronger single-point capture potential
- lower means healthier distribution


Average tenure (T_avg)

Meaning:
How long voting authority stays in the same hands on average.

Recommended measurement:
T_avg = average of T(m) over all voting members

Interpretation:
- higher means stronger long-term entrenchment risk
- lower means healthier renewal


Opacity index (O)

Meaning:
How much of decision-making is not publicly inspectable.

Recommended measurement approach:
Let:
- N_total be number of decisions in a period
- N_public be number of decisions with full public documentation

Then:
O = 1 - (N_public / N_total)

Interpretation:
- higher means lower trust and higher manipulation potential
- lower means higher civic auditability


Overlap ratio (I)

Meaning:
How much formal authority overlaps across councils or roles.

Recommended measurement:
Let:
- N_overlap be count of members with multi-council voting authority
- N_total_members be total voting members

Then:
I = N_overlap / N_total_members

Interpretation:
- higher means capture bridges between domains
- lower means stronger domain independence

---

## Cultural Calibration of Weights

Each society may choose weights based on its own:
- cultural memory
- institutional maturity
- social cohesion profile

However, the following guardrails are recommended:

- w_O should not be near zero
  (opacity is a universal corruption multiplier)

- w_C and w_I should not both be low
  (otherwise concentration can hide structurally)

- w_T should be strengthened in cultures with strong patronage patterns

Weights are not ideological.
They are risk sensitivity settings.

---

## Threshold Policy

A society sets a risk threshold:

R_c ≤ R_threshold

Recommended policy model:
- define a safe band
- define a warning band
- define a breach band

When the warning band is reached:
- mandatory review is triggered
- transparency requirements strengthen
- renewal mechanisms activate

When breach occurs:
- decisions with highest concentration impact are frozen for review
- councils must re-balance authority distribution

Threshold enforcement should be automatic wherever possible.

---

## Non-Negotiable Measurement Integrity

No society may:
- redefine metrics to hide risk
- disable public documentation requirements
- remove overlap tracking

If measurement integrity is broken,
the system becomes blind and collapses into narrative control.

---

## Output Format Recommendation

Each reporting period produces a public risk report containing:
- C value and explanation
- T_avg value and explanation
- O value and explanation
- I value and explanation
- computed R_c and band status
- corrective actions if any


