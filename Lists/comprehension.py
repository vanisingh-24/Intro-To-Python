## List Comprehension
# SYNTAX - newList = [ expression(element) for element in oldList if condition ]

#square of all odd numbers from range 1 to 10 
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print (odd_square)

# below list contains power of 2 from 1 to 8 
result = [2**x for x in range(1,9)]
print(result)

# below list contains prime and non-prime in range 1 to 50 
noprimes = [j for i in range(2,8) for j in range(i*2,50,i)]
primes = [x for x in range(2,50) if x not in noprimes]
print(primes)

# list for lowering the characters 
print([x.lower() for x in ["A","B","C"]])

# list which extracts number
string = "my phone number is : 11122 !!"

numbers = [x for x in string if x.isdigit()]
print(numbers)

# A list of list for multiplication table 
a = 5
table = [[a,b,a*b] for b in range(1,11)]

for i in table:
    print(i)



## Nested List Comprehensions 
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

# Nested List Comprehension to flatten a given 2-D matrix
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flatten = [j for i in matrix for j in i]
print(flatten)

# Nested List comprehension with an if condition
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
  
flatten = [planet for i in planets for planet in i if len(planet)<6]
print(flatten)
