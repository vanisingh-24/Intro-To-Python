# Given a list, print the value obtained after multiplying all numbers in a list. 

# Method 1: Traversal

def multiply(list):

  product = 1
  for i in list:
    product = product * i
  return product

# Driver Code
list = [1,2,3]
print(multiply(list))

# Using numpy.prod()

import numpy

list = [1,2,3]
product = numpy.prod(list)
print(product)

# Method 4 Using prod function of math library: Using math.prod

import math

list = [1,2,3]
product = math.prod(list)
print(product)