# Polymorphism in Python

# inbuilt polymorphic functions

print(len("geeks"))

print(len([1,2,3]))

# User Defined polymorphic functions

def add(x, y, z=0):
  return x+y+z

# Driver Code
print(add(2,4))

# Polymorphism with class methods

class India():
  def capital(self):
    print('New Delhi is capital of India')

  def language(self):
    print("Hindi is the most widely spoken language of India.")
  
  def type(self):
    print("India is a developing country.")

class USA():
  def capital(self):
    print("Washington, D.C. is the capital of USA.")
  
  def language(self):
    print("English is the primary language of USA.")
  
  def type(self):
    print("USA is a developed country.")

obj1 = India()
obj2 = USA()
for country in (obj1, obj2):
  country.capital()
  country.language()
  country.type()

# Polymorphism with inheritance

class Bird:
  def intro(self):
    print("There are many types of birds.")
      
  def flight(self):
    print("Most of the birds can fly but some cannot.")
    
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
      
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
      
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()

# Polymorphism with a Function and objects

class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

def func(obj):
	obj.capital()
	obj.language()
	obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)

