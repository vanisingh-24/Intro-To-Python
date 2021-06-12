# Given a list in Python and a number x, count number of occurrences of x in the given list.

def count(li, x):
  count = 0
  for i in li:
    if i == x:
      count = count +1
  return count

li = [10, 8, 3,8,4,8]
x = 8
count(li,x)

# OR

def count(li, x):
  return li.count(x)

# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, count(l,x)))

# OR

from collections import Counter

l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

# Driver Code
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))
