## Given an m x n matrix, find all common elements present in all rows in O(mn) time and one traversal of matrix.

# Efficient Solution using maps

def commonElements(mat):
  if not mat or not len(mat):
    return -1
    
  d = {}
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if i == 0:
        d[mat[0][j]] = 1

        if len(mat) == 1:
          return mat[i][j]

      if i > 0 and mat[i][j] in d and d[mat[i][j]] == i:
        d[mat[i][j]] = i+1
        if i == len(mat)-1:
          return mat[i][j]

mat = [[1,2,1,4,8],[3,7,8,5,1],[8,7,7,3,1],[8,1,2,7,9]]
commonElements(mat)