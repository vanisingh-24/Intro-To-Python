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



# Python function to check whether x is even or odd
 
def evenOdd(x):
    if (x % 2 == 0):
        print "even"
    else:
        print "odd"
 
evenOdd(2)
evenOdd(3)




