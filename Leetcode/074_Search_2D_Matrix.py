# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        
        N = len(matrix[0])
        M = len(matrix)
        l, r = 0, (N*M)-1
        
        while l <= r:
            mid = (l+r)//2
            if matrix[mid//N][mid%N] == target:
                return True
            elif matrix[mid//N][mid%N] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        