# Data Hiding in Python

class MyClass:

  # Hidden member of MyClass
  __hiddenVariable = 0

  # method that changes the __hiddenVariable
  def add(self, increment):
    self.__hiddenVariable += increment
    print(self.__hiddenVariable)

# Driver Code
Object = MyClass()
Object.add(2)
Object.add(5)

print(Object.__hiddenVariable)

#  access the value of hidden attribute

class MyClass():

  __hiddenVariable =10

# Driver Code
Object = MyClass()
print(Object._MyClass__hiddenVariable)






