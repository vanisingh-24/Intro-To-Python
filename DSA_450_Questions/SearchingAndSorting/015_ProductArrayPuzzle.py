## Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product of all the elements of nums except nums[i].

# Approach 1: Naive Solution

class Solution:
    def productExceptSelf(self, nums, n):
        left=[1]*n
        for i in range(1,n):
            left[i]=nums[i-1]*left[i-1]
            
        right=[1]*n
        for i in range(n-2,-1,-1):
            right[i]=nums[i+1]*right[i+1]
        prod=[1]*n
        for i in range(n):
            prod[i]=left[i]*right[i]
        return prod

# Approach 2: Efficient Solution

class Solution:
    def productExceptSelf(self, nums, n):
        temp = 1
        prod = [1]*n
        for i in range(n):
            prod[i] = temp
            temp *= nums[i]
        temp = 1
        for i in range(n-1, -1, -1):
            prod[i] *= temp
            temp *= nums[i]
        return prod



