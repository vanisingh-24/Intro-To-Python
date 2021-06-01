# Given a string, the task is to check if every vowel is present or not.
# We consider a vowel to be present if it is present in upper case or lower case. i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ . 

def vowels(string):
  string = string.lower()

  vowels = set('aeiou')

  s = set({})

  for char in string:
    if char in vowels:
      s.add(char)
    else:
      pass

  if len(s) == len(vowels):
    print('Accepted')
  else:
    print('Not Accepted')

# Driver Code

string = "SEEquoiaL"
vowels(string)