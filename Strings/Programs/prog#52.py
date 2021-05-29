# Sort the words in lexicographical order in Python

def lexicographic(string):

  words = string.split()

  words.sort()

  for i in words:
    print(i)

# Driver Code
string = "hello this is example how to sort " \
              "the word in alphabetical manner"
lexicographic(string)