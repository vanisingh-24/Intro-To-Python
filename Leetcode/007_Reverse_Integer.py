# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        isNeg = False
        
        if(x<0):
            isNeg = True
            x = -1*x
            
        while(x!=0):
            res = 10*res + x%10
            x = x//10
        
        if(res > 2**31 -1 or -1**res < -2**31): return 0
        return res if not isNeg else -1*res