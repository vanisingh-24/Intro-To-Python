## Given an array of integers and another number.
## Find all the unique quadruple from the given array that sums up to the given number.

# Approach 1: Naive Solution

def fourSum(arr, k):
    n = len(arr)
    for i in range(0, n-3):
        for j in range(i+1, n-2):
            for l in range(j+1, n-1):
                for r  in range(l+1, n):
                    if arr[i]+arr[j]+arr[l]+arr[r] == k:
    return (arr[i],arr[j],arr[l], arr[r])

arr = [0,0,2,1,1]
k = 3
fourSum(arr, k)

# Approach 2: Sorting

class Solution:
    def fourSum(self, arr, k):
        s = set()
        n = len(arr)
        arr.sort()
        for i in range(n-3):
            for j in range(i+1, n-2):
                l = j+1
                r = n-1
                while l < r:
                    total = arr[i] + arr[j] +arr[l] + arr[r]
                    if total == k:
                        s.add((arr[i], arr[j], arr[l], arr[r]))
                        l += 1
                        r -= 1
                    elif total < k:
                        l += 1
                    else:
                        r -= 1
        return sorted(s)


