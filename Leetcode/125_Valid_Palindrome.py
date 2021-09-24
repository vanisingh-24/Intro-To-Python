# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res += i.lower()
            
        return res[::-1] == res