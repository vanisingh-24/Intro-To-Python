## Given a binary matrix M of size n X m.
## Find the maximum area of a rectangle formed only of 1s in the given matrix.

class Solution:
    def maxArea(self,M, n, m):
        result = self.maxHist(M[0])
 
        for i in range(1, len(M)):
 
            for j in range(len(M[i])):
 
                if (M[i][j]):
                    M[i][j] += M[i - 1][j]
 
            result = max(result, self.maxHist(M[i]))
 
        return result
        
    def maxHist(self, histogram):
        stack = []
        max_area = 0 
        index = 0
        while index < len(histogram):
            if (not stack) or (histogram[stack[-1]] <= histogram[index]):
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
 
                area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)
 
        while stack:
            top_of_stack = stack.pop()
 
            area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
 
        return max_area

