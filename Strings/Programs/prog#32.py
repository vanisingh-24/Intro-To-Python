# Python program to Check if both halves of the string have same set of characters in Python

from collections import Counter

def checkTwoHalves(input):
  length = len(input)

  if (length %2 != 0):
    first = input[0:length//2]
    second = input[(length//2) + 1:]
  else:
    first = input[0:length//2]
    second = input[length//2:]

  if Counter(first) == Counter(second):
    print('YES')
  else:
    print('NO')

# Driver Code
input = 'abbaab'
checkTwoHalves(input) 