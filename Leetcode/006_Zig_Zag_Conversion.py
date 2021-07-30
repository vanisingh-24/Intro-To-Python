# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        charArray = [[] for _ in range(numRows)]
        row = 0
        direction = -1
        
        for c in s:
            charArray[row].append(c)
            if row == 0 or row == numRows - 1:
                direction *= -1
                
            row += direction
            
        result = ''
        for arr in charArray:
            result += ''.join(arr)
                
        return result

# OR

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        row_map = {row:"" for row in range(1, numRows+1)}
        row = 1
        up = True
        
        for letter in s:
            row_map[row] += letter
            if(row == 1) or ((row < numRows) and up):
                row += 1
                up = True
            else:
                row -= 1
                up = False
                
        converted = ""
        for row in range(1, numRows+1):
            converted += row_map[row]
            
        return converted


