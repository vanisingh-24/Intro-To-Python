#sorted()
#SYNTAX - sorted(iterable, key, reverse)

x = [1,2,8,4,6,3,7]

print(sorted(x))

print(sorted(x, reverse =True))

#Sorting different data types

x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print (sorted(x))
  
# ASCII translations
x = "python"
print (sorted(x))

# Dictionary
x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6}
print (sorted(x))
  
# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print (sorted(x))
  
# Frozen Set
x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
print (sorted(x))

#Sorting using the key parameter

L = ["cccc", "b", "dd", "aaa"]

print(sorted(L, key = len))

def func(x):
    return x % 7

L = [15, 3 , 11, 7]

print(sorted(L, key = func))