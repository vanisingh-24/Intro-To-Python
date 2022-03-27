## Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

# Dynamic Programming Approach

class Solution:
    def isSubsetSum (self, N, arr, sum):
        N = len(arr)
        T = [[False for x in range(sum + 1)] for y in range(N + 1)]
 
        for i in range(N + 1):
            T[i][0] = True
 
        for i in range(1, N + 1):
            for j in range(1, sum + 1):
                if arr[i - 1] > j:
                    T[i][j] = T[i - 1][j]
                else:
                    T[i][j] = T[i - 1][j] or T[i - 1][j - arr[i - 1]]
 
        return T[N][sum]
        

