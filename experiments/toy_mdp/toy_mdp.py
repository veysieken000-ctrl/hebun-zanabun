import numpy as np
import matplotlib.pyplot as plt

# Simulated environment
def run_simulation(lambda_value, episodes=1000):
    proxy_reward = 0
    safety_violations = 0
    
    for _ in range(episodes):
        # Random decision outcome
        true_value = np.random.rand()
        proxy_value = np.random.rand()
        
        score = lambda_value * true_value + proxy_value
        
        # Assume agent selects high score actions
        if score > 1.0:
            proxy_reward += proxy_value
        
        # Safety violation if proxy high but true low
        if proxy_value > 0.8 and true_value < 0.2:
            safety_violations += 1
            
    return proxy_reward, safety_violations

lambdas = np.linspace(0, 1, 20)
proxy_results = []
violation_results = []

for l in lambdas:
    proxy, violations = run_simulation(l)
    proxy_results.append(proxy)
    violation_results.append(violations)

plt.figure()
plt.plot(lambdas, violation_results)
plt.xlabel("Lambda")
plt.ylabel("Safety Violations")
plt.title("Drift vs Safety Violations")
plt.show()

import os
import numpy as np
import matplotlib.pyplot as plt

def run_simulation(lambda_value, episodes=20000, threshold=1.2, seed=0):
    rng = np.random.default_rng(seed)

    proxy_sum = 0.0
    true_sum = 0.0
    gap_sum = 0.0
    count = 0
    violations = 0

    for _ in range(episodes):
        true_value = float(rng.random()) # H
        proxy_value = float(rng.random()) # E

        score = lambda_value * true_value + proxy_value

        if score >= threshold:
            count += 1
            proxy_sum += proxy_value
            true_sum += true_value
            gap_sum += abs(proxy_value - true_value)

            if proxy_value > 0.85 and true_value < 0.15:
                violations += 1

    if count == 0:
        return 0, 0, 0, 0

    return (
        proxy_sum / count,
        true_sum / count,
        gap_sum / count,
        violations
    )

def main():
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)

    lambdas = np.linspace(0.0, 1.0, 21)

    proxy_means = []
    true_means = []
    gap_means = []
    violations = []

    for i, l in enumerate(lambdas):
        proxy, true, gap, viol = run_simulation(l, seed=42+i)
        proxy_means.append(proxy)
        true_means.append(true)
        gap_means.append(gap)
        violations.append(viol)

    plt.figure()
    plt.plot(lambdas, proxy_means, label="Proxy (E)")
    plt.plot(lambdas, true_means, label="True (H)")
    plt.legend()
    plt.xlabel("Lambda")
    plt.ylabel("Mean value")
    plt.title("Proxy vs True")
    plt.savefig(os.path.join(out_dir, "proxy_vs_true.png"))

    plt.figure()
    plt.plot(lambdas, violations)
    plt.xlabel("Lambda")
    plt.ylabel("Violations")
    plt.title("Safety Violations")
    plt.savefig(os.path.join(out_dir, "violations.png"))

    plt.figure()
    plt.plot(lambdas, gap_means)
    plt.xlabel("Lambda")
    plt.ylabel("Alignment Gap |E-H|")
    plt.title("Alignment Gap")
    plt.savefig(os.path.join(out_dir, "gap.png"))

    print("Saved results to experiments/toy_mdp/results")

if __name__ == "__main__":
    main()



