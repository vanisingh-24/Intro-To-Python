# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII.
# Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        dict ={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        N = len(s)
        i = N-1
        output = 0
        while i >= 0:
            if i < N-1 and dict[s[i]] < dict[s[i+1]]:
                output -= dict[s[i]]
            else:
                output += dict[s[i]]
            i -= 1
            
        return output

# OR

class Solution:
    def romanToInt(self, s: str) -> int:
        dict ={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        prev = 0
        curr = 0
        total = 0
         
        for i in range(len(s)):
            curr = dict[s[i]]
            if curr > prev:
                total = total + curr - 2*prev
            else:
                total += curr
            prev = curr
            
        return total