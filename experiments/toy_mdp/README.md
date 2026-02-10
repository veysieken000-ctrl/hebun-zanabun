# Toy MDP – Lambda Drift Evaluation

This experiment evaluates the effect of the alignment attention parameter λ
on reward optimization and safety constraint violations.

We model:

- H: upper-value (true objective)
- E: proxy/environment reward
- Score_λ = λH + E

Drift = 1 - λ

Hypothesis:
As λ decreases, proxy reward may increase,
but safety violations increase and alignment gap widens.

## Run

pip install -r requirements.txt
python toy_mdp.py

Results will be saved under:
experiments/toy_mdp/results/
