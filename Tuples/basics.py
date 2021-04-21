## Creating an empty tuple  
Tuple1 = ()
print (Tuple1)  
     
# Creating a tuple of strings 
print(('Geeks', 'For'))  
     
# Creating a Tuple of list  
print(tuple([1, 2, 4, 5, 6]))

#Creating a Tuple with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

#Creating a Tuple with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Geeks')
print(Tuple1)
 
# Creating a nested Tuple
Tuple1 = (0, 1, 2, 3)  
Tuple2 = ('python', 'geek')  
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

#Creating a Tuple with repetition
Tuple1 = ('Geeks',) * 3
print(Tuple1)

#Creating a Tuple with the use of loop
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

## Accessing tuple 
   
tuple1 = tuple([1, 2, 3, 4, 5]) 
   
# Accessing element using indexing
print(tuple1[0]) 
   
# Negative Indexing
print(tuple1[-1])

#Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")

a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)


## Updation / Deletion from a tuple 
   
tuple1 = tuple([1, 2, 3, 4, 5])
   
# Updating an element
tuple1[0] = -1
   
# Deleting an element
del tuple1[2] 

## Finding length of a tuple

tuple2 = ('python', 'geek')
print(len(tuple2))

