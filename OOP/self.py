# Self in python

class Car():

  def __init__(self,model, color):
    self.model = model
    self.color = color

  def show(self):
    print("Model is", self.model)
    print("Color is", self.color)

audi = Car("audi a4", "blue")
ferrari = Car("ferrari 488", "green")

audi.show()
ferrari.show()