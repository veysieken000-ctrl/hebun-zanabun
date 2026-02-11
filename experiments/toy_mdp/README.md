import os
import numpy as np
import matplotlib.pyplot as plt

# Correlated (H,E) generator with optional distribution shift
def sample_correlated(rng, corr=0.8):
    # Generate correlated normals then map to [0,1] via sigmoid-like transform
    z1 = rng.normal()
    z2 = corr * z1 + np.sqrt(max(0.0, 1 - corr**2)) * rng.normal()
    # map to (0,1)
    H = 1 / (1 + np.exp(-z1))
    E = 1 / (1 + np.exp(-z2))
    return float(H), float(E)

def run_phase(lambda_value, episodes, corr, threshold, seed):
    rng = np.random.default_rng(seed)

    proxy_sum = 0.0
    true_sum = 0.0
    gap_sum = 0.0
    count = 0
    violations = 0

    for _ in range(episodes):
        H, E = sample_correlated(rng, corr=corr)
        score = lambda_value * H + E

        if score >= threshold:
            count += 1
            proxy_sum += E
            true_sum += H
            gap_sum += abs(E - H)

            # specification gaming pattern:
            if E > 0.85 and H < 0.15:
                violations += 1

    if count == 0:
        return 0.0, 0.0, 0.0, 0

    return proxy_sum / count, true_sum / count, gap_sum / count, violations

def main():
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)

    lambdas = np.linspace(0.0, 1.0, 21)
    threshold = 1.15

    # Training distribution: high correlation
    train_corr = 0.85
    # Test distribution shift: low correlation
    test_corr = 0.10

    train_viol = []
    test_viol = []
    train_gap = []
    test_gap = []

    for i, l in enumerate(lambdas):
        tr_proxy, tr_true, tr_gap, tr_v = run_phase(l, episodes=30000, corr=train_corr, threshold=threshold, seed=100+i)
        te_proxy, te_true, te_gap, te_v = run_phase(l, episodes=30000, corr=test_corr, threshold=threshold, seed=200+i)

        train_viol.append(tr_v)
        test_viol.append(te_v)
        train_gap.append(tr_gap)
        test_gap.append(te_gap)

    # Plot violations: train vs test
    plt.figure()
    plt.plot(lambdas, train_viol, label="Train violations (corr=0.85)")
    plt.plot(lambdas, test_viol, label="Test violations (corr=0.10)")
    plt.xlabel("Lambda")
    plt.ylabel("Violations")
    plt.title("Distribution Shift: Violations vs Lambda")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "shift_violations.png"), dpi=200)

    # Plot alignment gap: train vs test
    plt.figure()
    plt.plot(lambdas, train_gap, label="Train gap |E-H| (corr=0.85)")
    plt.plot(lambdas, test_gap, label="Test gap |E-H| (corr=0.10)")
    plt.xlabel("Lambda")
    plt.ylabel("Mean gap")
    plt.title("Distribution Shift: Alignment Gap vs Lambda")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "shift_gap.png"), dpi=200)

    print("Saved: shift_violations.png, shift_gap.png in", out_dir)

if __name__ == "__main__":
    main()

