## Given a number n.
## The task is to find the smallest number whose factorial contains at least n trailing zeroes.

class Solution:
    def check(self,p,n):
        temp = p
        count = 0
        f = 5
        while (f <= temp):
            count += temp//f
            f = f*5
             
        return (count >= n)
        
    def findNum(self, n : int):
        if (n==1):
            return 5
        low = 0
        high = 5*n
      
        while (low <high):
            mid = (low+high) // 2
            if (self.check(mid, n)):
                high = mid
            else:
                low = mid+1
         
        return low

