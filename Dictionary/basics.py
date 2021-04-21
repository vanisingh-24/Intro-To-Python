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

# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print(Dict)

# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print(Dict)

## Adding elements to a dictionary

# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print(Dict) 

# Adding set of values to a single Key
Dict['Value_set'] = 2, 3, 4
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

# accessing elements in a nested dictionary
Dict = {'Dict1': {1: 'Geeks'}'Dict2': {'Name': 'For'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

## Removing Elements from Dictionary

Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},}  

# Deleting a Key value
del Dict[6]
print(Dict)
  
# Deleting a Key from Nested Dictionary
del Dict['A'][2]
print(Dict)   

# using pop()  
Dict.pop(5) 
print(Dict)  
 
# using popitem()  
Dict.popitem() 
print(Dict) 

# Deleting entire Dictionary
Dict.clear()
print(Dict)




