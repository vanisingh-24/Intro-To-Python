## Stickler the thief wants to loot money from a society having n houses in a single line.
## He is a weird person and follows a certain rule when looting the houses.
## According to the rule, he will never loot two consecutive houses.
## At the same time, he wants to maximize the amount he loots.
## The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy.
## He asks for your help to find the maximum money he can get if he strictly follows the rule.
## Each house has a[i]amount of money present in it.

class Solution:  
    
    def FindMaxSum(self,a, n):
        inc, exc = 0, 0
        for i in range(n):
            temp = inc
            inc = a[i] + exc
            exc = map(exc, temp)
        return max(inc, temp)

# OR

class Solution:  
   
    def FindMaxSum(self,a, n):
        incl = 0
        excl = 0
   
        for i in a:
            new_excl = excl if excl>incl else incl
            incl = excl + i
            excl = new_excl
    
        return (excl if excl>incl else incl)