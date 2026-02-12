# Risk Response Protocol
## Concentration Risk → Mandatory System Response

This document defines mandatory responses triggered by
concentration risk measurement.

It is designed to stop drift before capture happens.

This protocol does not replace morality.
It prevents structural blindness.

---

## Inputs

Each reporting period produces:

- C : centralization ratio
- T_avg : average tenure
- O : opacity index
- I : overlap ratio
- R_c : concentration risk score

R_c is computed from the calibration model.

---

## Risk Bands

A society defines thresholds:

- SAFE band
- WATCH band
- WARNING band
- BREACH band

These bands are not symbolic.
They trigger mandatory responses.

---

## Mandatory Response Rules

### SAFE

Condition:
R_c is within SAFE band.

Response:
- normal operation
- publish period report
- no intervention

---

### WATCH

Condition:
R_c enters WATCH band.

Mandatory response:
- increase audit intensity
- increase documentation strictness
- publish a public notice of WATCH status

Minimum requirements:
- documentation completeness check becomes stricter
- random decision audits are performed

---

### WARNING

Condition:
R_c enters WARNING band.

Mandatory response:
- automatic review trigger
- mandatory transparency escalation
- renewal mechanism activation

Actions:
- councils must publish extended reasoning records
- rotate a defined minimum portion of members (renewal boost)
- freeze high-impact decisions for constitutional review queue
- produce corrective plan with deadlines

No society may remain in WARNING without corrective action.

---

### BREACH

Condition:
R_c enters BREACH band.

Mandatory response:
- emergency structural rebalancing
- temporary suspension of high-concentration pathways
- enforced renewal and overlap purge

Actions:
- immediate suspension of decisions that increase concentration
- forced rotation to reduce T_avg
- forced removal of overlap if any is detected
- temporary restriction on council power adjustments
- mandatory external civic audit publication

BREACH is treated as a capture-attempt condition.

---

## Metric-Specific Triggers

Even if overall R_c is moderate,
a single metric crossing its hard boundary
may trigger escalation.

Recommended hard boundaries:

- If O is high, escalate immediately (opacity is a universal multiplier).
- If I rises above baseline, trigger overlap purge review.
- If T_avg exceeds renewal target, enforce rotation.
- If C rises rapidly, trigger distribution review.

Societies may calibrate boundaries,
but cannot disable metric integrity.

---

## Integrity Requirements

Measurement integrity is non-negotiable:

- public reporting cannot be suspended
- council membership data must remain auditable
- documentation requirements cannot be reduced during WATCH/WARNING/BREACH

If integrity breaks,
the system becomes blind and collapses into narrative control.

---

## Output Format

Each period must publish:

- C, T_avg, O, I values with explanations
- R_c score and band classification
- triggered actions (if any)
- completion status of prior corrective actions

---

## Principle

Civilization survives through early correction,
not late punishment.

This protocol exists to prevent drift,
not to create fear.


