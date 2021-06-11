# Given a list of numbers, the task is to write a Python program to find the second largest number in given list.

list = [10, 20, 4]

list.sort()

print(list[-2])

# OR

list = [10, 20, 4]

list.remove(max(list))

print(max(list))

# OR

list = [10, 20, 4]

max = max(list[0], list[1])
secondmax = min(list[0], list[1])
n = len(list)
for i in range(2, n):
  if list[i]>max:
    secondmax = max
    max = list[i]
  elif list[i]>secondmax and max != list[i]:
    secondmax = list[i]

print(secondmax)

