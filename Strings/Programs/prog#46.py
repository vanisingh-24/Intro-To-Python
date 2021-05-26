# Reverse words in a given string in python

def reverse(sentence):
  words = sentence.split(' ')

  reversedSentence = ' '.join(reversed(words))

  return reversedSentence

input = 'geeks quiz practice code'
print(reverse(input))