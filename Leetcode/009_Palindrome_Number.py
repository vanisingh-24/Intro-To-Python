# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative number cannot be a palindrome
        if(x<0):
            return False
        
        if(x==0):
            return True
        
        # numbers like 10,20,1000 cannot be palindromes
        if(x%10==0):
            return False
        
        # reverse 2nd half of the number
        reverse = 0
        while(x>reverse):
            # accumulate digits from the end of the number x and keep pushing them to the variable reverse
            reverse = reverse*10 + x%10
            x = x//10
            
            # valid for even length palindromes
            if(x==reverse):
                return True
            
            # for odd length palindromes
            if(x==reverse//10):
                return True
            
        # if nothing is true its not a palindrome
        return False
        
# OR

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (str(x) == str(x)[::-1])