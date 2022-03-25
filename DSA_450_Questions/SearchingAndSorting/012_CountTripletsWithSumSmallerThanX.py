## Given an array arr[] of distinct integers of size N and a value sum, the task is to find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.

class Solution:
    def countTriplets(self, arr, n, sumo):
        count = 0
        for i in range(n-2):
            l = i+1
            h = n-1
            while l < h:
                sum = arr[i] + arr[l] + arr[h]
                if sum >= sumo:
                    h -= 1
                else:
                    count += h-l
                    l += 1
        return count