## Encapsulation

# Protected Members

class Base:
  def __init__(self):

    # protected member
    self._a = 2

class Derived(Base):
  def __init__(self):

    # Calling constructor or base class
    Base.__init__(self)
    # Calling protected member of the base class
    print(self._a)

obj1 = Derived()
obj2 = Base()

# Calling protected member Outside class will  result in AttributeError
print(obj2.a)

# Private members

class Base:
  def __init__(self):
    self.a = "GeeksforGeeks"
    self.__c = "GeeksforGeeks"

class Derived(Base):
  def __init__(self):

    # Calling constructor or base class
    Base.__init__(self)
    print(self.__a)

obj = Derived()

# AND

class Base:
  def __init__(self):
    self.a = "GeeksforGeeks"
    self.__c = "GeeksforGeeks"

class Derived(Base):
  def __init__(self):

    # Calling constructor or base class
    Base.__init__(self)
    print(self.__c)

obj = Base()
print(obj.a)