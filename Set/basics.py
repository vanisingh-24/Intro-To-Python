## Creation of Set 
     
# Creating a Set  
set1 = set()  
 
# Creating a Set of String  
set1 = set("GeeksForGeeks") 
print(set1)  
   
# Creating a Set of List  
set1 = set(["Geeks", "For", "Geeks"])
print(set1)  

# Creating a Set with the use of an object
String = 'GeeksForGeeks'
set1 = set(String)
print(set1)

# Creating a Set with a List of Numbers
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print(set1)
  
# Creating a Set with a mixed type of values
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print(set1)

## Addition of elements in a Set  

set1 = set()
     
# using add() 
set1.add(8)
set1.add((6, 7))
print(set1)  

# using Iterator
for i in range(1, 6):
    set1.add(i)
print(set1)
   
# using Update()   
set1.update([10, 11])
print(set1) 

## Accessing of elements in a set  
     
set1 = set(["Geeks", "For", "Geeks"])  
 
# using for loop
for i in set1:  
    print(i, end =" ")

## Deletion of elements in a Set  
 
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  
 
# using Remove() method  
set1.remove(5)  
set1.remove(6)
print(set1)  
 
# using Discard() method  
set1.discard(8)  
set1.discard(9)
print(set1)  
 
# Set using the pop() method  
set1.pop()
print(set1)  
 
# Set using clear() method  
set1.clear()
print(set1) 

# Removing elements from Set using iterator method
for i in range(1, 5):
    set1.remove(i)
print(set1)