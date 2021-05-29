# Find the Number Occurring Odd Number of Times using Lambda expression and reduce function

from functools import reduce

def oddTimes(input):
  print(reduce(lambda a, b: a^b, input))

# Driver Code
input = [1, 2, 3, 2, 3, 1, 3]
oddTimes(input)