## Constructors
# SYNTAX - def __init__(self):
               # body of the constructor

# parameterized constructors

class Addition:
  #parameterized constructor
  
  def __init__(self, f, s):
    self.first = f
    self.second =s

  def calculate(self):
    print(self.first + self.second)

object = Addition(100,200)
object.calculate()

# default constructors

class GeekForGeeks:

  # default constructor
  def __init__(self):
    self.geek = "GeekForGeeks"

  def print_Geek(self):
    print(self.geek)

object = GeekForGeeks()
object.print_Geek()