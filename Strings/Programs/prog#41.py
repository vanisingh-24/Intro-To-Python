# Given a string that has set of words and spaces, write a program to move all spaces to front of string, by traversing the string only once.

def moveSpaces(input):
  noSpace = [ch for ch in input if ch!=' ']

  space = len(input) - len(noSpace)
  
  result = ' '*space

  result = '"'+result + ''.join(noSpace)+'"'
  print(result)

# Driver Code
input = 'geeks for geeks'
moveSpaces(input)