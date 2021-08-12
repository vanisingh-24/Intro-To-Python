# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# Return the quotient after dividing dividend by divisor.
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. 
# For this problem, assume that your function returns 231 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend, divisor):
        d = abs(dividend)
        dv = abs(divisor)
        output = 0
        
        while d >= dv:
            tmp = dv
            mul = 1
            while d >= tmp:
                d -= tmp
                output += mul
                mul += mul
                tmp += tmp
                
        if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0):
            output = -output
            
        return min(2147483647, max(-2147483648, output))

# OR

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # bit manipulation
        # bitwise shift to the left is the equivalent of a multiplication by 2
        if dividend == -2147483648 and divisor == -1: return 2147483647
        # sign of result
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        
        quotient = 0
        # Take the absolute value
        d = abs(dividend)
        dv = abs(divisor)
        # Loop until the  dividend is greater than divisor
        while d >= dv:
            # This represents the number of bits shifted or
            # how many times we can double the number
            shift = 0
            while d >= (dv << shift):
                shift += 1
            # Add the number of times we shifted to the quotient
            quotient += (1 << (shift - 1))
            # Update the dividend for the next iteration
            d -= dv << (shift - 1)
        return -quotient if sign == -1 else quotient