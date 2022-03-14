## Given a string S, find the longest palindromic substring in S.

# Brute Force

def longestPalin(self, S):
        maxlen = 0
        output = ""
        for i in range(len(S)):
            for j in range(i+1, len(S)+1):
                temp = S[i:j]
                
                if temp == temp[::-1] and len(temp) > maxlen:
                    output = temp
                    maxlen = len(temp)
                    
        return output

# Efficient Solution

class Solution:
    def longestPalin(self, S):
        res = ""
        resLen = 0
       
        for i in range(len(S)):
            
            l, r = i,i
            while l>=0 and r<len(S) and S[l] == S[r]:
                if (r-l+1) > resLen:
                    res = S[l:r+1]
                    resLen = r-l+1
                   
                l -= 1
                r += 1
               
            l,r = i, i+1
            while l>=0 and r<len(S) and S[l] == S[r]:
                if (r-l+1) > resLen:
                    res = S[l:r+1]
                    resLen = r-l+1
               
                l -= 1
                r += 1
        return res