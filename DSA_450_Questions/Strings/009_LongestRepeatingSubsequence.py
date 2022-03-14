## Given a string str, find the length of the longest repeating subsequence such that it can be found twice in the given string.
## The two identified subsequences A and B can use the same ith character from string str if and only if that ith character has different indices in A and B.

# Dynamic Programming (Bottom Up Approach) using LCS

class Solution:
	def LongestRepeatingSubsequence(self, str):
	    n = len(str)
	    str2 = str
	    dp = [[0 for j in range(n+1)] for i in range(n+1)]
	    
	    for i in range(n-1, -1, -1):
	        for j in range(n-1, -1, -1):
	            if str[i] == str2[j] and i!=j:
	                dp[i][j] = 1 + dp[i+1][j+1]
	            else:
	                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
	    return dp[0][0]
	

