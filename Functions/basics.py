## Defining Functions

def ask_user():
    print("Hello")

def my_func():
    a = 0
    for i in range(1,11):
        a = a+i
    return a

ask_user()
res = my_func()
print(res)

## Return statement
# SYNTAX - return [expression_list]

def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(square_value(-4))

def add(a,b):
    return a + b

def is_true(a):
    return bool(a)

res = add(2,3)
print(res)
res = is_true(2<5)
print(res)

## Returning multiple values

# 1. Using Object

class Test:
    def __init__(self):
        self.str = 'gfg'
        self.x = 20

def fun():
    return Test()

t = fun()
print(t.str)
print(t.x)

# 2. Using Tuple

def fun():
    str = 'geeksforgeeks'
    x = 20
    return (str,x)

str,x = fun()   #assigning the returned tuple
print(str)
print(x)

# 3. Using a list

def fun():
    str = "geeksforgeeks"
    x = 20   
    return [str,x]

list = fun()
print(list)

# 4. Using a dictionary

def fun():
    d = dict()
    d['str'] = 'gfg'
    d['x'] = 20
    return d

d = fun()
print(d)

## Pass by reference OR pass by value

# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20

lst = [10, 11,12,13,14,15]
myFun(lst)
print(lst)

def myFun(x):
 
    # After below line link of x with previous object gets broken. A new object is assignedto x.
    x = [20, 30, 40]
 
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

## Anonymous functions

cube = lambda x : x*x*x

print(cube(7))

# Python function to check whether x is even or odd
 
def evenOdd(x):
    if (x % 2 == 0):
        print "even"
    else:
        print "odd"
 
evenOdd(2)
evenOdd(3)




