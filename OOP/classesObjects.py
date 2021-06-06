## Classes and Objects
## SYNTAX - class ClassName:
               # Statement-1
               # .
               # .
               # .
               # Statement-N

class Dog:

  #Simple class attributes
  attr1 = "mammal"
  attr2 = "dog"
 
  # Sample method
  def fun(self):
    print("I am a ", self.attr1)
    print("I am a ", self.attr2)

# Object Instantiate
Rodger = Dog()

# Accessing class attributes and method through objects
print(Rodger.attr1)
Rodger.fun()

## __init__ method

class Person:

  # init method or constructor
  def __init__(self, name):
    self.name = name

  # sample method
  def say_hi(self):
    print("Hello, my name is", self.name)

p = Person('Vani')
p.say_hi()

## Class and Instance variables
## variables with a value 
## assigned in the class declaration, are class variables and
## variables inside methods and constructors are instance
## variables.

# Defining instance variable using a constructor. 
class Dog:

  # class variable
  animal = 'dog'

  # init method or constructor
  def __init__(self, breed, color):

    # Instance variables
    self.breed = breed
    self.color = color

# Instantiate Object
Rodger = Dog("pug","brown")
Buzo = Dog("Bulldog", "black")

print("Rodger is a ", Rodger.animal)
print("Breed:", Rodger.breed)
print("Color:", Rodger.color)

print('\nBuzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Accessing class variable using class name
print(Dog.animal)

# Defining instance variable using a normal method.

class Dog:

  # Class variable
  animal = "dog"

  # Init method or constructor
  def __init__(self, breed):

    # Instance variable
    self.breed = breed

  # Adds an instance variable
  def setColor(self, color):
    self.color = color

  # Retrieves instance variable
  def getColor(self):
    return self.color

# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
