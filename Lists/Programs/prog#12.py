# Given a list of numbers, the task is to write a Python program to find the largest number in given list.

li = [10,3,6]

li.sort()
print(li[-1])

# OR

li = [10,3,4]
print(max(li))

#OR

def largest(list):
  maximum = list[0]
  for i in range(len(list)):
    if list[i]>maximum:
      maximum = list[i]
      return maximum

list = [10, 3, 24]
print(largest(list))