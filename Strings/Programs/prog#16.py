# Python program to reverse each word in a sentence

def reverseWord(sentence):

  words = sentence.split(' ')

  newWord = [word[::-1] for word in words]

  newSentence = ' '.join(newWord)

  return newSentence

sentence = "GeeksforGeeks is good to learn"
print(reverseWord(sentence))