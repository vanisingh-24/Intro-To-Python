# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i : i+len(needle)] == needle:
                return i
        return -1

# OR

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

