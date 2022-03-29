## Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.

# Naive Solution

class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        ans = 0
        temp = nums.copy()
        temp.sort()
        
        for i in range(n):
            if nums[i] != temp[i]:
                ans += 1
                self.swap(nums, i, self.indexOf(nums, temp[i]))
        return ans
        
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
    def indexOf(self, arr, ele):
        for i in range(len(arr)):
            if arr[i] == ele:
                return i
        return -1

# Using hashmap

class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        a = list(nums)
        a.sort()
        d = dict()
        
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], i)
        c = 0
        for i in range(n):
            if a[i] == nums[i]:
                continue
            else:
                idx = nums[i]
                nums[i], nums[d[a[i]]] = nums[d[a[i]]], nums[i]
                d[idx] = d[a[i]]
                d[a[i]] = i
                c += 1
        return c

