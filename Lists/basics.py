## Creation of List   
     
List = []  
print(List)  
     
# Creating a list of strings
List = ['GeeksForGeeks', 'Geeks'] 
print(List)  
     
# Creating a Multi-Dimensional List  
List = [['Geeks', 'For'], ['Geeks']]  
print(List)

# Creating a List with mixed type of values
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print(List)

# Creating a List with Having duplicate values
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print(List)

# Knowing the size of List
List2 = [10, 20, 14]
print(len(List2))


## Addition of elements in a List  
      
List = []
     
# Using append()
List.append(1)  
List.append(2)
print(List)  

# Adding elements to the List using Iterator
for i in range(1, 4):
    List.append(i)
print(List)

# Adding Tuples to the List
List.append((5, 6))
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print(List)
   
# Using insert()
List.insert(3, 12)  
List.insert(0, 'Geeks')
print(List)  
   
# Using extend()  
List.extend([8, 'Geeks', 'Always'])  
print(List)


## accessing of element from list  
     
List = [1, 2, 3, 4, 5, 6]  
     
# accessing a element
print(List[0])   
print(List[2])  
   
# Negative indexing 
print(List[-1])
# print the third last element of list   
print(List[-3])


## Removal of elements in a List  
      
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 
# using Remove() method  
List.remove(5)  
List.remove(6)
print(List)  
   
# using pop()
List.pop()
print(List)  