## sorted()
# SYNTAX - sorted(iterable, key, reverse)

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

## sum()
   
numbers = [1,2,3,4,5,1,4,5]
  
# start parameter is not provided
Sum = sum(numbers)
print(Sum)
  
# start = 10
Sum = sum(numbers, 10)
print(Sum)

## tuple()
# SYNTAX - tuple(iterable)

#When parameter is not passed
tuple1 = tuple()
print(tuple1)

# when a list is passed
list1= [ 1, 2, 3, 4 ] 
tuple2 = tuple(list1)
print(tuple2)
  
# when a dictionary is passed
dict = { 1 : 'one', 2 : 'two' } 
tuple3 = tuple(dict)
print(tuple3)
  
# when a string is passed
string = "geeksforgeeks" 
tuple4 = tuple(string)
print(tuple4)

# Error when a non-iterable is passed
tuple1 = tuple(1) 
print(tuple1)

## cmp() max() and min()

tuple1 = ('python', 'geek')
tuple2 = ('coder', 1)

if (cmp(tuple1, tuple2) != 0):
    print('Not the same')
else:
    print('Same')
print('Max element:' + str(max(tuple1)) + ',' + str(max(tuple2)))
print('Min element:' + str(min(tuple1)) + ',' + str(min(tuple2)))
