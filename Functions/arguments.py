## Function with arguments

## Default arguments

def myFunc(x,y=50):
    print(x)
    print(y)

# Driver Code
myFunc(10)

## Keyword arguments

def student(firstname, lastname):
    print(firstname, lastname)

student(firstname="Steve", lastname="Rogers")
student(lastname="Rogers", firstname="Steve")

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
