## Append()
# SYNTAX - my_list.append(object)

my_list = ['geeks', 'for']
my_list.append('geeks')
print my_list

## Extend()
# SYNTAX - my_list.extend(iterable) 

my_list = ['geeks', 'for']
another_list = [6, 0, 4, 1]
my_list.extend(another_list)
print my_list

my_list = ['geeks', 'for', 6, 0, 4, 1]
my_list.extend('geeks')
print my_list

## del()
# SYNTAX - del list.[index] 

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0]
print(List)

## del[a:b]

lis = [2, 1, 3, 5, 4, 3, 8]
  
# using del to delete elements from pos. 2 to 5
del lis[2 : 5]

for i in range(0, len(lis)):
    print(lis[i], end=" ")

## pop()
# SYNTAX - list.pop([index])

lis.pop(2)

for i in range(0, len(lis)):
    print(lis[i], end=" ")

## sort()
# SYNTAX -  list.sort([key,[Reverse_flag]])

lis = [2, 1, 3, 5, 3, 8]
  
lis.sort()
for i in range(0, len(lis)):
    print(lis[i], end=" ")

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
  
#Reverse flag is set True
List.sort(reverse=True) 
print(List)        

## reverse()
lis.reverse()
  
for i in range(0, len(lis)):
    print(lis[i], end=" ")

## clear()

lis1 = [2, 1, 3, 5]
lis1.clear()

## len() min() max()

lis = [2, 1, 3, 5, 4]
  
print (len(lis))
  
print (min(lis))
  
print (max(lis))

## Index(ele, beg, end)

lis = [2, 1, 3, 5, 4, 3]
  
print (lis.index(3, 3, 6))

## count()
# SYNTAX - list_name.count(object) 

print (lis.count(3))

## sum()
# SYNTAX - sum(iterable, start)  

List = [1, 2, 3, 4, 5]
print(sum(List))

numbers = [1,2,3,4,5,1,4,5]
  
# start parameter is not provided
Sum = sum(numbers)
print(Sum)
  
# start = 10
Sum = sum(numbers, 10)
print(Sum)

## remove()
# SYNTAX - list.remove(element)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)

## copy()
# SYNTAX - list.copy()

lis1 = [ 1, 2, 3, 4 ]
  
lis2 = lis1.copy()
  
print ("The new list created is : " + str(lis2))

lis2.append(5)
  
# No change in old list
print ("The new list after adding new element : " + str(lis2))
print ("The old list after adding new element to new list  : " + str(lis1))

## ord()
# SYNTAX - ord("string")

value = ord("A")
value1 = ord('A')
 
print value, value1

## chr()
# SYNTAX - chr(num)

print(chr(71), chr(101))

numbers = [17, 38, 24]

for number in numbers:
    letter = chr(number)
    print(letter)

## cmp()
# SYNTAX - cmp(list1, list2)

# Integers
list1 = [ 1, 2, 4, 3]
list2 = [ 1, 2, 5, 8]
list3 = [ 1, 2, 5, 8, 10]
list4 = [ 1, 2, 4, 3]
  
# prints 1   
print cmp(list2, list1)
  
# prints -1, because list3 has larger size than list2
print cmp(list2, list3)
  
# prints 0 as list1 and list4 are equal
print cmp(list4, list1)

# multiple data types

list1 = [ 1, 2, 4, 10]
list2 = [ 1, 2, 4, 'a']
list3 = [ 'a', 'b', 'c']
list4 = [ 'a', 'c', 'b']
  
print cmp(list2, list1)
  
print cmp(list2, list3)
  
print cmp(list3, list4)

## any()
# SYNTAX - any(list of iterables)

# Since all are false, false is returned
print (any([False, False, False, False]))
  
# Here the method will short-circuit at the second item (True) and will return True.
print (any([False, True, False, False]))
  
# Here the method will short-circuit at the first (True) and will return True.
print (any([True, False, False, False]))

## all()
# SYNTAX - all(list of iterables)

# Here all the iterables are True so all will return True and the same will be printed
print (all([True, True, True, True]))
  
# Here the method will short-circuit at the first item (False) and will return False.
print (all([False, True, True, False]))
  
# This statement will return False, as no True is found in the iterables
print (all([False, False, False]))

# Example1
list1 = []
list2 = []

for i in range(1,11):
    list1.append(4*i)

for i in range(0,10):
    list2.append(list1[i]%5==0)

print(any(list2))

# Example2

list1 = []
list2 = []

for i in range(1,21):
    list1.append(4*i-3)

for i in range(0,20):
    list2.append(list1[i]%2 == 1)

print(all(list2))

## Enumerate()
# SYNTAX - enumerate(iterable, start=0)

l1 = ["eat","sleep","repeat"]
s1 = "geek"

obj1 = enumerate(l1)
onj2 = enumerate(s1)

print(list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1,2)))

# enumerate function in loops
l1 = ["eat","sleep","repeat"]

for el in enumerate(l1):
    print(el)

for count, el in enumerate(l1, 100):
    print(count,el)

## filter()
# SYNTAX - filter(function, sequence)

def fun(variable):
    letter = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = filter(fun, sequence)

for s in filtered:
    print(s)

# used with lambda functions 
# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x%2 !=0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x%2 == 0, seq)
print(list(result))

## map()
# SYNTAX - map(func, iterable)

# return double of n
def addition(n):
    return n+n

numbers = (1,2,3,4)
result = map(addition,numbers)
print(list(result))

# lambda function can also be used
numbers = (1,2,3,4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x,y:x+y, numbers1,numbers2)
print(list(result))

# list of strings

l = ['sat', 'bat', 'cat', 'mat']

test = list(map(list, l))
print(test)

## lambda()
# SYNTAX - lambda arguments: expression

cube = lambda x: x*x*x
print(cube(5))

# map and filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
result = filter(lambda x: (x%2 != 0), li)
print(list(result))

ages = [13, 90, 17, 59, 21, 60, 5]

adult = filter(lambda age: age>18, ages)
print(list(result))

# map and lambda
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

result = list(map(lambda x : x*2,li))
print(result)

animals = ['dog', 'cat', 'parrot', 'rabbit']

upper = list(map(lambda animal: str.upper(animal), animals))
print(upper)

# map and reduce

from functools import reduce

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y:x+y),li)
print(sum)

lis = [ 1 , 3, 5, 6, 2, ]
print(reduce(lambda a,b : a if a>b else b,lis))

## Reduce()
# SYNTAX - reduce(fun, seq)
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y:x+y),li)
print(sum)

# reduce and operator functions
import functools
import operator

lis = [ 1 , 3, 5, 6, 2, ]
print(functools.reduce(operator.add,lis))
print(functools.reduce(operator.mul,lis))

print(functools.reduce(operator.add,["geeks","for","geeks"] ))

## accumulate()
# SYNTAX - accumulate(seq, fun)

import itertools

lis = [ 1, 3, 4, 10, 4 ]
print(list(itertools.accumulate(lis, lambda x,y: x+y)))














