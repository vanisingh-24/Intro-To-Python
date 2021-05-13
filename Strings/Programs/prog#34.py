# Python program to Find the first repeated word in a string

from collections import Counter

def firstRepeat(string):

  words = string.split(' ')

  dict = Counter(words)

  for key in words:
    if dict[key]>1:
      print(key)
      return

# Driver Code
input = 'Ravi had been saying that he had been there'
firstRepeat(input) 