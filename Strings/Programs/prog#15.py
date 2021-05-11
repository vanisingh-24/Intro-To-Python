# Python program to Sort words of sentence in ascending order

def sorted(sentence):
  words = sentence.split(" ")

  words.sort()

  newSentence = " ".join(words)

  return newSentence

# Driver Code
sentence = "to learn programming refer geeksforgeeks"
print(sorted(sentence))


