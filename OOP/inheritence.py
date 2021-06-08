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





