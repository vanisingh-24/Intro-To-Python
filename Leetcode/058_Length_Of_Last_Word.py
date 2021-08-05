# Given a string s consists of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        count = 0
        
        while length > 0:
            length -= 1
            if s[length] != ' ':
                count += 1
            elif count > 0:
                return count
        return count