## Matrix Product

# Using List comprehension + loop

def prod(val):
  res = 1
  for el in val:
    res *= el
  return res

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print((test_list))

# Matrix Product
res = prod([el for sub in test_list for el in sub])

print(res)

# OR
# Using chain() + loop

from itertools import chain

def prod(val):
  res = 1
  for el in val:
    res *= el
  return res

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

print(test_list)

res = prod(list(chain(*test_list)))

print(res)

