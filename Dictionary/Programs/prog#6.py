## Merging two Dictionaries

# Using update()
def Merge(dict1, dict2):
  return (dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(Merge(dict1, dict2))
print(dict2)

# Using ** 
def Merge(dict1, dict2):
  res = {**dict1, **dict2}
  return res

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4} 
dict3 = Merge(dict1, dict2)
print(dict3)

# Using | operator
def Merge(dict1, dict2):
  res = dict1 | dict2
  return res

dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict3)
