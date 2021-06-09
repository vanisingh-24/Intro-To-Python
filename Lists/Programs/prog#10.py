# Reversing a List in Python

def reverse(list):
  new = list[::-1]
  return new

list = [1,2,3,4]
print(reverse(list))

# OR

def reverse(list):
  list.reverse()
  return list

list = [1,2,3,4]
print(reverse(list))

# OR

def reverse(list):
  return [i for i in reversed(list)]

list = [ 1,2,3,4]
print(reverse(list))

