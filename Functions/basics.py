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




