# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val):
            nums.remove(val)

# OR

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        i, j = 0, 0
        
        while j < N:
            if (nums[j] != val):
                nums[i] = nums[j]
                i += 1
            j += 1
            
        return i
        