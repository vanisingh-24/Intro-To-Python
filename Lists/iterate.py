# Using For loop 
list = [1, 3, 5, 7, 9]
 
for i in list:
    print(i)

# For loop and range()
list = [1, 3, 5, 7, 9]
  
length = len(list)
  
for i in range(length):
    print(list[i])

# Using while loop 
list = [1, 3, 5, 7, 9]
  
length = len(list)
i = 0
  
while i < length:
    print(list[i])
    i += 1

# Using list comprehension 
list = [1, 3, 5, 7, 9]
  
[print(i) for i in list]

# Using enumerate()
list = [1, 3, 5, 7, 9]
  
for i, val in enumerate(list):
    print (i, ",",val)




