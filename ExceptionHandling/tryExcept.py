# Try and Except

# Case 1: No exception, so try clause will run.
def divide(x,y):
  try:
    result = x//y
    print(result)
  except ZeroDivisionError:
    print('Sorry you are dividing by zero')

divide(3,2)

# Case 2: There is an exception so only except clause will run.
def divide(x,y):
  try:
    result = x//y
    print(result)
  except :
    print('Sorry you are dividing by zero')

divide(3,0)

# Case 3: Else clause
def divide(x,y):
  try:
    result = x//y
    print(result)
  except :
    print('Sorry you are dividing by zero')
  else:
    print('No exception raised')

divide(3,2)

# multiple errors with one except statement

try:
    a = 3
    if a < 4:
        b = a/(a-3)

    print('Value of b is', b)
except(ZeroDivisionError, NameError):
    print('Error')







