# Given starting and end points, write a Python program to print all odd numbers in that given range.

start, end = 4, 15

for num in range(start, end +1):
  if num %2 != 0:
    print(num, end = " ")
