# Python Program for factorial of a number

# 1. Recursive Approach
def factorial(n):
  if (n==1 or n==0):
    return 1
  else:
    return n* factorial(n-1)

num = 5
print(factorial(num))

# 2. Using Ternary Operator

def factorial(n):

  return 1 if (n==1 or n==0) else n* factorial(n-1)

num = 5
print(factorial(num))

# 3. By using In-built function

import math

def factorial(n):
  return(math.factorial(n))

num = 5
print(factorial(num))




