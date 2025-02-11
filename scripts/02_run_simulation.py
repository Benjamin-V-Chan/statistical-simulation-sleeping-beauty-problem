import csv

total_awakenings = 0
heads_awakenings = 0
tails_awakenings = 0

with open("outputs/results.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_awakenings += 1
        if row["Coin_Flip"] == "Heads":
            heads_awakenings += 1
        else:
            tails_awakenings += 1

prob_heads = heads_awakenings / total_awakenings

with open("outputs/summary.txt", "w") as f:
    f.write(f"Total awakenings: {total_awakenings}\n")
    f.write(f"Awakenings with Heads: {heads_awakenings}\n")
    f.write(f"Awakenings with Tails: {tails_awakenings}\n")
    f.write(f"Empirical probability of Heads given awakening: {prob_heads:.4f}\n")
