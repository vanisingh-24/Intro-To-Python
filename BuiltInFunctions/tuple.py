#tuple()
#SYNTAX - tuple(iterable)

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