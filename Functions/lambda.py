## labmda function 
# SYNTAX - lambda arguments: expression

# Cube using lambda
cube = lambda x: x*x*x
print(cube(3))

# List Comprehension using lambda
a = [(lambda x: x*2)(x) for x in range(5)]
print(a)

# Using lambda() Function with filter()

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x%2 != 0), li))
print(final_list)

ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age>18, ages))
print(adults)

# Using lambda() Function with map()

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

double = list(map(lambda x: x*2, li))
print(double)

animals = ['dog', 'cat', 'parrot', 'rabbit']

upper = list(map(lambda animal: str.upper(animal), animals))
print(upper)

# Using lambda() Function with reduce()

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x,y: x+y), li)
print(sum)

import functools

lis = [1,3,5,6,2]

print(functools.reduce(lambda a,b: a if a>b else b, lis))

