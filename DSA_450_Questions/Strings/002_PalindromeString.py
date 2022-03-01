## Given a string S, check if it is palindrome or not.

class Solution:
	def isPalindrome(self, S):
	    if S==S[::-1]:
	        return 1
	    else:
	        return 0