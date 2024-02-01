import numpy as np

x = np.random.random(10)

print("Random NUmbers:")
print(x)

mean = np.mean(x)
median= np.median(x)
std = np.std(x)

print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std}")