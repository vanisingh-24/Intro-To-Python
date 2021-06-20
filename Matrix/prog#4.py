## Adding and Subtracting Matrices in Python

# 1. Adding elements of matrix

import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[4,5],[6,7]])

print(A)
print(B)
print(np.add(A,B))

# 2. Subtracting elements of matrix

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])

print(A)
print(B)
print(np.subtract(A,B))