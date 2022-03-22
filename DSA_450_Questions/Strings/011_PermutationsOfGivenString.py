## Given a string S. The task is to print all permutations of a given string in lexicographically sorted order.

# Approach1: Backtracking

class Solution:
    def permute(self,a,l,r,ans):
        if l==r:
            ans.append(''.join(a))
        else:
            for i in range(l,r+1):
                a[l], a[i] = a[i], a[l]
                self.permute(a, l+1, r,ans)
                a[l], a[i] = a[i], a[l]
    def find_permutation(self, S):
        a=list(S)
        n=len(S)
        ans=[]
        self.permute(a,0,n-1,ans)
        ans.sort()
        return ans

# Approach2: using itertools

class Solution:
    def find_permutation(self, S):
        from itertools import permutations
        words=sorted(''.join(p) for p in permutations(S))
        return words