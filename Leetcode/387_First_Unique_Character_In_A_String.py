# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
                
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
        

# OR

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = set()
        
        for i in range(len(s)):
            if s[i] not in char:
                char.add(s[i])
                if s.count(s[i]) == 1:
                    return i
        return -1