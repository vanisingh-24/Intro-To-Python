# Produce a new list whose i^{th} element will be equal to the sum of the (i + 1) elements.
# Python program to find Cumulative sum of a list

def cumulative(list):
  new = []
  length = len(list)
  new = [sum(list[0: n:1]) for n in range(0, length+1)]
  return new[1:]

# Driver Code
lists = [10, 20, 30, 40, 50]
print (cumulative(lists))

# OR

lists = [10, 20, 30, 40, 50]
new = []
j = 0
for i in range(0, len(lists)):
  j += lists[i]
  new.append(j)

print(new)

