# Inheritence

class Person():

  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name

  def isEmployee(self):
    return False

# Inherited or Sub Class
class Employee(Person):

  def isEmployee(self):
    return True

# Driver Code
emp = Person("Geek1")  # An Object of Person 
print(emp.getName(), emp.isEmployee()) 
   
emp = Employee("Geek2") # An Object of Employee 
print(emp.getName(), emp.isEmployee())

# to check if a class is subclass of another

class Base(object):
  pass

class Derived(Base):
  pass

print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))
  
# But d is an instance of Base
print(isinstance(d, Base))

# Multiple Inheritance

class Base1():
  def __init__(self):
    self.str1 = "Geek1"
    print("Base1")

class Base2():
  def __init__(self):
    self.str2 = "Geek2"
    print("Base2")

class Derived(Base1, Base2):
  def __init__(self):

    # calling constructors of base1 and 2
    Base1.__init__(self)
    Base2.__init__(self)
    print("Derived")

  def printStr(self):
    print(self.str1, self.str2)

ob = Derived()
ob.printStr()

# access parent members in a subclass

# 1. Using parent class name

class Base():

  def __init__(self, x):
    self.x = x

class Derived(Base):

  def __init__(self, x, y):
    Base.x = x
    self.y = y

  def print(self):
    print(Base.x, self.y)

# Driver Code
d = Derived(10, 12)
d.print()

# 2. Using super()

class Base():
  def __init__(self, x):
    self.x = x

class Derived(Base):

  def __init__(self, x, y):
    super(Derived, self).__init__(x)
    self.y = y

  def print(self):
    print(self.x, self.y)

# Driver Code
d = Derived(10, 12)
d.print()

# Example

class X():
  def __init__(self, a):
    self.num = a
  def doubleUp(self):
    self.num *= 2

class Y(X):
  def __init__(self, a):
    X.__init__(self, a)
  def tripleUp(self):
    self.num *= 3

obj = Y(4)
print(obj.num)

obj.doubleUp()
print(obj.num)

obj.tripleUp()
print(obj.num)




