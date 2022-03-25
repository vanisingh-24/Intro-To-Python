## Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K.
## The task is to find the element that would be at the k’th position of the final sorted array.
 
# Approach 1: Naive Solution

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        arr = sorted(arr1 + arr2)
        return arr[k-1]

# Approach 2: Efficient Solution

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        res = [0]*(m+n)
        i = 0
        j = 0
        d = 0
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                res[d] = arr1[i]
                i += 1
            else:
                res[d] = arr2[j]
                j += 1
            d += 1
        while i < n:
            res[d] = arr1[i]
            d += 1
            i += 1
        while j < m:
            res[d] = arr2[j]
            d += 1
            j += 1
        return res[k-1]

