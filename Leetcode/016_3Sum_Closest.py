# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        
        for i in range(len(nums)-2):
            
            l = i+1
            r = len(nums)-1
            
            while l < r:
                sumHere = nums[i] + nums[l] + nums[r]
                if abs(sumHere - target) < abs(res - target):
                    res = sumHere
                if sumHere < target:
                    l += 1
                else:
                    r -= 1
                    
        return res
                    