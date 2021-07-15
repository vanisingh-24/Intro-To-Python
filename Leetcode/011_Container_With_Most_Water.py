# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force
        res = 0
        
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)
        
        return res