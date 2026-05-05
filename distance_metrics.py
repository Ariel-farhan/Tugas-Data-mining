import numpy as np
from scipy.spatial.distance import euclidean, cityblock

# Titik P dan Q
P = np.array([1, 2, 3])
Q = np.array([4, 5, 6])

# Hitung jarak
euc = euclidean(P, Q)
man = cityblock(P, Q)

print("=== NOMOR 1 ===")
print(f"Euclidean Distance : {euc:.2f}")
print(f"Manhattan Distance : {man:.2f}")
