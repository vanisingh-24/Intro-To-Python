# Given a list of numbers, write a Python program to find the sum of all the elements in the list.

li = [1,2,3,4]

total = sum(li)
print(total)

# OR

sum = 0

li = [1,2,3,4]

for i in range(0, len(li)):
  sum = sum + li[i]
print(sum)


