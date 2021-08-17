# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        pivot = 0
        
        # Find pivot
        for i in range(N-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i
                break
        if pivot == 0:
            nums.sort()
            return
        
        #Find swap which first no. > pivot
        swap = N-1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1
        
        # swap
        nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]
        
        # reverse from pivot
        nums[pivot:] = sorted(nums[pivot:])
        
        

# OR

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        if ls <= 1:
            return
        pair = []
        for i in range(ls):
            for j in range(i + 1, ls):
                # append ascending order pair
                if nums[i] < nums[j]:
                    pair.append([i,j])
        pos = 0
        if len(pair) > 0:
            self.swap(nums, pair[-1][0], pair[-1][1])
            pos = pair[-1][0] + 1
        # sort from pos
        for i in range(pos, ls):
            for j in range(i + 1, ls):
                if nums[i] > nums[j]:
                    self.swap(nums, i, j)

    def swap(self, nums, index1, index2):
        if index1 == index2:
            return
        nums[index1], nums[index2] = nums[index2], nums[index1]
        




