# Count occurrences of a word in string in python

def count(str, word):

  wordList = list(str.split())
  return wordList.count(word)

# Driver Code
str ="GeeksforGeeks A computer science portal for geeks  "
word ="portal"
print(count(str, word))

# OR

def count(str, word):
  a = str.split(" ")

  count = 0
  for i in range(0, len(a)):
    if(word==a[i]):
      count = count+1

  return count

# Driver Code
str ="GeeksforGeeks A computer science portal for geeks  "
word ="portal"
print(count(str, word))