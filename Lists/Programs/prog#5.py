# Given a list, write a Python program to swap first and last element of the list.

def swap(list):
  n = len(list)

  temp = list[0]
  list[0] = list[n-1]
  list[n-1] = temp

  return list

# Driver code
list = [12, 35, 9, 56, 24]
print(swap(list))

# OR

def swap(list):
  temp = list[0]
  list[0] = list[-1]
  list[-1] = temp

  return list

# Driver code
newList = [12, 35, 9, 56, 24]
print(swap(newList))

