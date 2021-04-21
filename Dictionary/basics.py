## Creating Dictionary  
Dict = {}
print(Dict)  
 
# with Integer Keys  
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)  
 
# with Mixed keys  
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict)

# Nested Dictionary
Dict = {1: 'Geeks', 2: 'For', 3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
   
print(Dict) 

## Adding elements to a dictionary

# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print(Dict) 
 
# Updating existing Key's Value 
Dict[2] = 'Welcome'
print(Dict) 

##Accessing elements from a Dictionary

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}  
     
# accessing a element using key
print(Dict['name'])  
   
# accessing a element using get()
print(Dict.get(3)) 

## Removing Elements from Dictionary

Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},}  
     
# using pop()  
Dict.pop(5) 
print(Dict)  
 
# using popitem()  
Dict.popitem() 
print(Dict) 




