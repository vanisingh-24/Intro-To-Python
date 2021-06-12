# Given a list of numbers, write a Python program to print all positive numbers in given list.

list1 = [11, -21, 0, 45, 66, -93]

for num in list1:
  if num >= 0:
    print(num, end=" ")

# OR

list1 = [11, -21, 0, 45, 66, -93]

pos = [num for num in list1 if num >= 0]
print(pos)

# OR

list1 = [11, -21, 0, 45, 66, -93]

pos = list(filter(lambda x: (x >= 0), list1))
print(pos)
