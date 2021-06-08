# Destructors
# SYNTAX - def __del__(self):
              # body of destructor

class Employee:

  def __init__(self):
    print('Employee Created')

  # Deleting or calling destructor
  def __del__(self):
    print('Destructor called, Employee deleted.')

obj = Employee()
del obj

# Destructor is called after the program ends

class Employee:

  def __init__(self):
    print('Employee created')

  def __del__(self):
    print("Destructor called")

def Create_obj():
  print('Making object...')
  obj = Employee()
  print('Function end...')
  return obj

print('Calling create_obj() function')
obj = Create_obj()
print('Program end...')




