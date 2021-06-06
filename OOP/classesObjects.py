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
