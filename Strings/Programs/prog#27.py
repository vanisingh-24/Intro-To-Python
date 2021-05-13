# Python program to Find all close matches of input string from a list

from difflib import get_close_matches

def closeMatches(patterns, word):
  print(get_close_matches(word, patterns))

# Driver Code
word = 'appel'
patterns = ['ape', 'apple', 'peach', 'puppy']
closeMatches(patterns, word)