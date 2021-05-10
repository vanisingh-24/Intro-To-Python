# Program to convert String to a List

def convert(string):
  li = string.split(" ")
  return li

str1 = 'Geeks For Geeks'
print(convert(str1))

# OR

def convert(string):
  li = string.split("-")
  return li

str1 = 'Geeks-For-Geeks'
print(convert(str1))

#OR
# string to list character-wise

def convert(string):
  li = []
  li[:0]= string
  return li

str1 = 'ABCD'
print(convert(str1))
