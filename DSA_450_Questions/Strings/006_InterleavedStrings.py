## Given strings A, B, and C, find whether C is formed by an interleaving of A and B.

# Dynamic Programming

class Solution:
    def isInterleave(self, A, B, C):
        if len(A) + len(B) != len(C):
            return 0
        dp = [[0] * (len(B)+1) for i in range(len(A)+1)]
        dp[len(A)][len(B)] = 1
        
        for i in range(len(A), -1, -1):
            for j in range(len(B), -1, -1):
                if i < len(A) and A[i] == C[i+j] and dp[i+1][j]:
                    dp[i][j] = 1
                if j < len(B) and B[j] == C[i+j] and dp[i][j+1]:
                    dp[i][j] = 1
        return dp[0][0]