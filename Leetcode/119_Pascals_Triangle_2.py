# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]
        
        prev = self.getRow(rowIndex - 1)
        
        curr = [1] + [prev[i] + prev[i+1] for i in range(len(prev)-1)] + [1]
        
        return curr

# OR

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        
        for x in range(1, rowIndex+1):
            row.append(row[x - 1] * (rowIndex - x + 1) // x)
        return row