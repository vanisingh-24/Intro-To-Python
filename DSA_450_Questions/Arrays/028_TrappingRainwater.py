## Given an array arr[] of N non-negative integers representing the height of blocks. 
## If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

# Two Pointer Solution

class Solution:
    def trappingWater(self, arr,n):
        left = 0
        right = n-1
        l_max = 0
        r_max = 0
        result = 0
        while (left <= right):
            if r_max <= l_max:
                result += max(0, r_max-arr[right])
                r_max = max(r_max, arr[right])
                right -= 1
            else:
                result += max(0, l_max-arr[left])
                l_max = max(l_max, arr[left])
                left += 1
        return result

# OR

class Solution:
    def trappingWater(self, arr,n):
        if not arr:
            return 0
            
        l, r = 0, n-1
        leftMax, rightMax = arr[l], arr[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, arr[l])
                res += leftMax - arr[l]
            else:
                r -= 1
                rightMax = max(rightMax, arr[r])
                res += rightMax - arr[r]
        return res