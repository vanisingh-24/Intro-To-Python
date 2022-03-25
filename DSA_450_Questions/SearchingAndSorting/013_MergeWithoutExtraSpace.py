## Given two sorted arrays arr1[] of size N and arr2[] of size M.
## Each array is sorted in non-decreasing order.
## Merge the two arrays into one sorted array in non-decreasing order without using any extra space.

class Solution:
    def merge(self, arr1, arr2, n, m): 
        i = n - 1
        j = 0
        
        while i >= 0 and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1
        arr1.sort()
        arr2.sort()
