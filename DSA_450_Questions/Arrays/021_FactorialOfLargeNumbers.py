## Given an integer N, find its factorial.

# Approach 1

class Solution:
    def factorial(self, N):
        mul=1
        while N:
            mul*=N
            N-=1
        return list(map(int,str(mul)))

# Approach 2

class Solution:
    def factorial(self, N):
        fac = 1
        for i in range(1,N+1):
           fac*=i
        return [fac]