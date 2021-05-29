# Given a string S, remove all the consecutive duplicates using groupby method

from itertools import groupby

def removeDuplicates(input):
  result = []
  for (key,group) in groupby(input):
    result.append(key)

  print(''.join(result))

# Driver Code
input = 'aaaaabbbbbb'
removeDuplicates(input)