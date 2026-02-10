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
