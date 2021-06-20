## Transpose a matrix in Single line in Python

# Using nested list comprehension
m = [[1,2],[3,4],[5,6]]

for row in m:
  print(row)

res = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in res:
  print(row)

# Using zip
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for row in matrix:
  print(row)

print('\n')

t_matrix = zip(*matrix)
for row in t_matrix:
  print(row)

# Using numpy

import numpy
matrix=[[1,2,3],[4,5,6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))

# OR

import numpy as np
matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)
print('\n')
print(matrix.T)


