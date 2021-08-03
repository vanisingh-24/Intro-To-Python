# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        
        res = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        limit = min(len(first), len(last))
        
        for i in range(limit):
            if first[i] == last[i]:
                res += first[i]
            else:
                break
                
        return res

# OR

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
        pre = strs[0]
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre 

# OR

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return("")
        if len(strs) == 1:
            return(strs[0])
        
        pref = strs[0]
        plen = len(pref)
        
        for s in strs[1:]:
            while pref != s[0:plen]:
                pref = pref[0: (plen - 1)]
                plen -= 1
                
                if plen == 0:
                    return("")
        
        return(pref)