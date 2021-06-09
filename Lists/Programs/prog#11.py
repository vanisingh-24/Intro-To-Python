# Given a list of numbers, the task is to write a Python program to find the smallest number in given list.

def smallest(list):
  list.sort()
  return list[0]

list = [10,3, 40,23]
print(smallest(list))

# OR

li = [10, 3, 24]

print(min(li))

# OR

def smallest(list):
  minimum = list[0]
  for i in range(len(list)):
    if list[i]<minimum:
      minimum = list[i]
      return minimum

list = [10, 3, 24]
print(smallest(list))

