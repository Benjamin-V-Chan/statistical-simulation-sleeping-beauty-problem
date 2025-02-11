import json
import csv
import random

# Load configuration settings
with open("config.json", "r") as f:
    config = json.load(f)

num_trials = config["num_trials"]

trials = []
for trial_id in range(num_trials):
    coin_flip = random.choice(["Heads", "Tails"])
    wake_days = ["Monday"] if coin_flip == "Heads" else ["Monday", "Tuesday"]
    for wake_day in wake_days:
        trials.append([trial_id, coin_flip, wake_day])

with open("outputs/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Trial_ID", "Coin_Flip", "Wake_Day"])
    writer.writerows(trials)
