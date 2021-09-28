# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = sorted(list(ransomNote))
        m = sorted(list(magazine))
        
        for char in m:
            if r and char == r[0]:
                r.pop(0)
                
        if r:
            return False
        else:
            return True
        
# OR

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True