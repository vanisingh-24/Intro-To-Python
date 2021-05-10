# Python program to count number of vowels using sets in given string

def count_vowel(str):
  count = 0
  vowel = set('aeiouAEIOU')

  for alphabet in str:
    if alphabet in vowel:
      count = count+1

  print("Number of vowels: ", count)

# Driver code
str = 'GeeksForGeeks'
count_vowel(str)




