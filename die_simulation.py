import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
rolls = np.random.randint(1, 7, size=1000)

print("First 10 rolls:", rolls[:10])

faces, counts = np.unique(rolls, return_counts=True)

print("Face  Count  Empirical P  Theoretical P")
for face, count in zip(faces, counts):
    empirical_p = count / 1000
    print(f"{face}     {count}    {empirical_p:.3f}        0.1667")

plt.hist(rolls, bins=range(1, 8), align="left", color="steelblue", edgecolor="black")
plt.xlabel("Face")
plt.ylabel("Count")
plt.title("Die Roll Distribution (1000 rolls)")
plt.xticks(range(1, 7))
plt.savefig("die_rolls.png")
print("Saved die_rolls.png")