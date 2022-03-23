## Given three distinct numbers A, B and C.
## Find the number with value in middle (Try to do it with minimum comparisons).

class Solution:
    def middle(self,A,B,C):
        list = [A,B,C]
        list.sort()
        return list[1]