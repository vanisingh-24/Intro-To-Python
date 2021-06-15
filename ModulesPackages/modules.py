## Python Modules

def Geeks():
  print("GeeksForGeeks")

location = "Noida"

class Employee():
  def __init__(self, name, position):
    self.name = name
    self.position = position

  def show(self):
    print(self.name)
    print(self.position)

# To use the above created module, create a new Python file in the same directory and import GFG module

import GFG

GFG.Geeks()
print(GFG.location)
emp = GFG.Employee('Vani','Developer')
emp.show()