import numpy as np

X = np.array([1, 0, 1, 0, 1, 1])
Y = np.array([1, 1, 0, 0, 1, 0])

# Hitung komponen
M11 = np.sum((X == 1) & (Y == 1))
M00 = np.sum((X == 0) & (Y == 0))
M10 = np.sum((X == 1) & (Y == 0))
M01 = np.sum((X == 0) & (Y == 1))

# SMC
smc = (M11 + M00) / len(X)

# Jaccard
jaccard = M11 / (M11 + M10 + M01)

print("\n=== NOMOR 2 ===")
print(f"SMC     : {smc:.2f}")
print(f"Jaccard : {jaccard:.2f}")
