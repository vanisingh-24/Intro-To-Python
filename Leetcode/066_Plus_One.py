# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry, i = 1, 0
        
        while carry:
            if i < len(digits):   # In Bounce
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:   # Out Of Bounce
                digits.append(1)
                carry = 0
            i += 1
        return digits[::-1]

# OR

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Reverse List Addition
    
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return(digits)
        return [1] + digits

# OR

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Type Conversion
        return [int(x) for x in str(int("".join([str(i) for i in digits])) + 1)]