# Map function and Dictionary in Python to sum ASCII values

def asciisum(sentence):

  words = sentence.split(" ")

  dict ={}

  for word in words:
    currentSum = sum(map(ord,word))

    dict[word] = currentSum

  totalSum = 0

  sumOfAscii = [dict[word] for word in words]
  print ('Sum of ASCII values:')
  print(' '.join(map(str, sumOfAscii)))
  print("Total sum: ", sum(sumOfAscii))

#Driver Code
sentence = 'I am a geek'
asciisum(sentence)

