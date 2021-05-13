# K’th Non-repeating Character in Python using List Comprehension and OrderedDict

from collections import OrderedDict

def kthRepeating(input, k):
  dict = OrderedDict.fromkeys(input, 0)

  for ch in input:
    dict[ch]+=1

  nonRepeatDict = [key for (key, value) in dict.items() if value == 1]

  if len(nonRepeatDict) < k:
    return 'Less than k non-repeating characters in input.'
  else:
    return nonRepeatDict[k-1]

input = "geeksforgeeks"
k = 3
print (kthRepeating(input, k)) 