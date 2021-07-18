# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

class Solution:    
    def fourSum(self, nums, target):
        result = []
        nums.sort()
        length = len(nums)-1
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:          # if 1st index is duplicate, continue
                continue
            for j in range(i+1, length-1):
                if j > i+1 and nums[j] == nums[j-1]:    # if 2nd index is duplicate, continue
                    continue
                k = j+1
                h = length
                while k < h:                            # while 3rd index is smaller than the 4th index
                    curr = nums[i] + nums[j] + nums[k] + nums[h]
                    if curr == target:
                        result.append([nums[i], nums[j], nums[k], nums[h]])
                        while k < h and nums[k] == nums[k+1]:
                            k += 1
                        while k < h and nums[h] == nums[h-1]:
                            h -= 1
                        k += 1
                        h -= 1
                    elif curr > target:
                        h -= 1
                    else:
                        k += 1
        return result      