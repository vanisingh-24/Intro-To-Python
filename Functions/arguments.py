## Function with arguments

## Default arguments

def myFunc(x,y=50):
    print(x)
    print(y)

# Driver Code
myFunc(10)

def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')

# Using mutable objects as default argument values in python

def appendItem(itemName, itemList = []):
    itemList.append(itemName)
    return itemList

print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))

def addItemToDict(itemName, quantity, itemList = {}):
    itemList[itemName] = quantity
    return itemList

print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))

def appendItem(itemName, itemList=None):
    if itemList == None:
        itemList = []
    itemList.append(itemName)
    return itemList

print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))

def addItemToDictionary(itemName, quantity, itemList = None):
    if itemList == None:
        itemList = {}
    itemList[itemName] = quantity
    return itemList

print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))    

## Keyword arguments

def student(firstname, lastname):
    print(firstname, lastname)

student(firstname="Steve", lastname="Rogers")
student(lastname="Rogers", firstname="Steve")

def student(firstname, lastname ='Mark', standard ='Fifth'):
     print(firstname, lastname, 'studies in', standard, 'Standard')
 
# 1 keyword argument
student(firstname ='John')    
 
# 2 keyword arguments                
student(firstname ='John', standard ='Seventh') 
 
# 2 keyword arguments
student(lastname ='Gates', firstname ='John')    

## variable length arguments

def myFunc(*argv):
    for arg in argv:
        print(arg, end=" ")

def myFunc1(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

# Driver code

myFunc('Hello', 'Welcome', 'to', 'GeeksforGeeks')
myFunc1(first ='Geeks', mid ='for', last ='Geeks')
