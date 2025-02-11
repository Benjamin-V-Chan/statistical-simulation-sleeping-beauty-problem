import matplotlib.pyplot as plt

# Read data from summary.txt
with open("outputs/summary.txt", "r") as f:
    lines = f.readlines()
    awakenings_heads = int(lines[1].split(":")[1])
    awakenings_tails = int(lines[2].split(":")[1])

labels = ["Heads", "Tails"]
values = [awakenings_heads, awakenings_tails]

plt.bar(labels, values, color=["blue", "red"])
plt.xlabel("Coin Flip Outcome")
plt.ylabel("Number of Awakenings")
plt.title("Sleeping Beauty Awakening Counts")
plt.savefig("outputs/plots/awakening_counts.png")
plt.show()
