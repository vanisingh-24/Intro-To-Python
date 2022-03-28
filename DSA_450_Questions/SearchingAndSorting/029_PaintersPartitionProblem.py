## Dilpreet wants to paint his dog's home that has n boards with different lengths.
## The length of ith board is given by arr[i] where arr[] is an array of n integers.
## He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board. 
## The problem is to find the minimum time to get this job done if all painters start together with the constraint that any painter will only paint continuous boards, say boards numbered {2,3,4} or only board {1} or nothing but not boards {2,4,5}.

# Binary Search

class Solution:

    def minTime (self, arr, n, k):
        
        low = max(arr)
        high = sum(arr)
        res = 999999
        while low <= high:
            painters = 1
            sum1 = 0
            mid = (low+high) // 2
            for i in range(n):
                if sum1 + arr[i] > mid:
                    painters += 1
                    sum1 = arr[i]
                else:
                    sum1 += arr[i]
                if painters > k:
                    low = mid+1
                    break
            if painters <= k:
                res = min(res,mid)
                high = mid-1
            
        return res

# OR

class Solution:
    def is_possible(self, arr, n, k, mid):
        painters = 1 
        sum1 = 0
        for i in range(n):
            if arr[i] > mid:
                return False
            if (arr[i] + sum1) > mid:
                painters += 1
                sum1 = arr[i]
            else:
                sum1 += arr[i]
        if painters > k:
            return False
        return True

    def minTime (self, arr, n, k):
        low = max(arr)  
        high = sum(arr) 
        res = -1
        while low <= high:
            mid = (low+high) // 2
            if self.is_possible(arr, n, k, mid):
                res = mid
                high = mid - 1
            else:
                low = mid +1
        return res