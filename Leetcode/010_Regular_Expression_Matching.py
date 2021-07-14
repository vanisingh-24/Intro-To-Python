# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top Down Memoization
        def dfs(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if (j+1) < len(p) and p[j+1] == "*":
                return (dfs(i, j+2) or # don't use *
                       (match and dfs(i+1, j)))   # us *
            if match:
                return dfs(i+1, j+1)
            return False
        
        return dfs(0,0)