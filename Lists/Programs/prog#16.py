# Given a list of numbers, write a Python program to print all even numbers in given list.

li = [12, 13, 14, 15]

for i in li:
  if i %2 == 0:
    print(i, end=" ")

# OR

li = [12,13,14,15]

even = [num for num in li if num % 2 ==0]

print(even)

# OR

li = [12, 13, 14, 15]

even = list(filter(lambda x:  (x%2 ==0), li))

print(even)