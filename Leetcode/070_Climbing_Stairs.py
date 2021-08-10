# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev1 = 1
        prev2 = 2
        curr = 0
        
        for i in range(2,n):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return curr

# OR

class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom Up Memoization
        one, two = 1, 1
        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one