# Python Regex to extract maximum numeric value from a string

import re

def extractMax(input):

  numbers = re.findall('\d+', input)

  numbers = map(int, numbers)

  print(max(numbers))

# Driver Code
input = '100klh564abc365bg'
extractMax(input)