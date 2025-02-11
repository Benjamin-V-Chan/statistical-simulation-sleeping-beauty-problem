import json

p_heads = 0.5
p_tails = 0.5
p_awake_given_heads = 1
p_awake_given_tails = 2

p_awake = p_heads * p_awake_given_heads + p_tails * p_awake_given_tails
p_heads_given_awake = (p_heads * p_awake_given_heads) / p_awake

with open("outputs/summary.txt", "a") as f:
    f.write(f"Bayesian probability of Heads given awakening: {p_heads_given_awake:.4f}\n")
