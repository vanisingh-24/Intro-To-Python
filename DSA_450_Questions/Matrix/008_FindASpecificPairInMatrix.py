## Given an n x n matrix mat[n][n] of integers, find the maximum value of mat(c, d) – mat(a, b) over all choices of indexes such that both c > a and d > b.

# Approach 1: Simple solution

def findMaxValue(mat):
    maxValue = 0
 
    for a in range(N - 1):
        for b in range(N - 1):
            for d in range(a + 1, N):
                for e in range(b + 1, N):
                    if maxValue < int (mat[d][e] - mat[a][b]):
                        maxValue = int(mat[d][e] - mat[a][b])
 
    return maxValue

# Approach 2: Efficient solution

def findMaxValue(mat):
    maxValue = 0
    maxArr = [[0 for x in range(N)] for y in range(N)]
 
    maxArr[N - 1][N - 1] = mat[N - 1][N - 1]

    maxv = mat[N - 1][N - 1]
    for j in range (N - 2, -1, -1):
        if (mat[N - 1][j] > maxv):
            maxv = mat[N - 1][j]
        maxArr[N - 1][j] = maxv
     
    maxv = mat[N - 1][N - 1] 
    for i in range (N - 2, -1, -1):
        if (mat[i][N - 1] > maxv):
            maxv = mat[i][N - 1]
        maxArr[i][N - 1] = maxv
 
    for i in range (N - 2, -1, -1):
        for j in range (N - 2, -1, -1):
            if (maxArr[i + 1][j + 1] - mat[i][j] > maxValue):
                maxValue = (maxArr[i + 1][j + 1] - mat[i][j])
 
            maxArr[i][j] = max(mat[i][j], max(maxArr[i][j + 1], maxArr[i + 1][j]))
         
    return maxValue