# Python program to Split a string based on a delimiter and join the string using another delimiter.

def split(string):

  li = string.split(' ')

  return li

def join(li):

  string = '-'.join(li)

  return string

# Driver Code
string = 'Geeks For Geeks'

li = split(string)
print(li)

newString = join(li)
print(newString)