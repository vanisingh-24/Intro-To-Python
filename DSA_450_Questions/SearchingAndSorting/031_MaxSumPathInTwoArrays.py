## Given two sorted arrays A and B of size M and N respectively.
## Each array may have some elements in common with the other array.
## Find the maximum sum of a path from the beginning of any array to the end of any of the two arrays.
## We can switch from one array to another array only at the common elements.

# Efficient Approach

class Solution:
    def maxSumPath(self, arr1, arr2, m, n):
        i, j = 0, 0
        res, sum1, sum2 = 0, 0, 0
        
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                res += max(sum1, sum2) + arr1[i]
                sum1, sum2 = 0, 0
                i += 1
                j += 1
                    
        while i < m:
            sum1 += arr1[i]
            i += 1
        while j < n:
            sum2 += arr2[j]
            j += 1
        res += max(sum1, sum2)
        return res
