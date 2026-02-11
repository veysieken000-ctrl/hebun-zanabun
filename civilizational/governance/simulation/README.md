# Governance Simulation
## Concentration Risk Monitoring Prototype

This folder provides a simple simulation model that generates:
- centralization ratio (C)
- average tenure (T_avg)
- opacity index (O)
- overlap ratio (I)
- concentration risk score (R_c)

The purpose is not prediction.
The purpose is early-warning structure testing.

---

## What it Simulates

- Multiple domain councils
- Periodic decision cycles
- Documentation rate (public vs non-public decisions)
- Member rotation (renewal vs entrenchment)
- Optional overlap injection (capture bridge simulation)

---

## Outputs

Each run prints a public-style report:
- per-council decision power distribution
- period metrics: C, T_avg, O, I
- risk score R_c and band classification

---

## How to Run

Use any Python 3.x:

python simulate.py --config config.example.json

---

## Interpretation

- Higher C means stronger single-point capture potential
- Higher T_avg means entrenchment risk
- Higher O means opacity and manipulation potential
- Higher I means cross-domain capture bridges

This is a prototype.
Societies may replace random dynamics with real data.

## Scenarios

Predefined scenario configs are available in `scenarios/`:

- `capture-attack.json`  
  Overlap injection simulating cross-domain capture bridges.

- `opacity-drift.json`  
  Reduced documentation rate simulating opacity drift.

- `tenure-entrenchment.json`  
  Minimal renewal simulating long-term entrenchment.

Run example:
python simulate.py --config scenarios/capture-attack.json

