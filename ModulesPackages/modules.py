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


# Python built in modules

import math
print(math.sqrt(25))
print(math.pi)
print(math.degrees(2))
print(math.radians(60))
print(math.sin(2))
print(math.cos(0.5))
print(math.factorial(4))

import random

# printing random integer between 0 and 5
print(random.randint(0,5))

# random number between 0 and 100
print(random.random()*100)

List = [1, 4, True, 800, "python", 27, "hello"]
 
print(random.choice(List))

import datetime
from datetime import date
import time

print(time.time())

print(date.fromtimestamp(454554))