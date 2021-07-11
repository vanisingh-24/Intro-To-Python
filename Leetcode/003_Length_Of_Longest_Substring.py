# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        # using Window Sliding technique
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

# OR

class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        max_len = 0
        d = {}
        while end < len(s):
            if(s[end] in d and d[s[end]] >= start):
                start = d[s[end]] + 1
            max_len = max(max_len, end-start+1)
            d[s[end]] = end
            end+=1
        return max_len

# OR

class Solution:
    def lengthOfLongestSubstring(self, s):
        if(len(s) == 0):
            return 0
        dict = {}
        max_length = start = 0
        
        for i in range(len(s)):
            if(s[i] in dict and start <= dict[s[i]]):
                start = dict[s[i]] + 1
            else:
                max_length = max(max_length, i-start+1)
            dict[s[i]] = i
        return(max_length)