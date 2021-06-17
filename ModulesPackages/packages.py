## Python Packages

# Create a Cars directory 
# Bmw.py
class Bmw:

    def __init__(self):
        self.models = ['i8', 'x1', 'x5', 'x6'] 

    def outModels(self):
        for model in self.models:
            print('\t %s' % model)

# Audi.py
class Audi:
    def __init__(self): 
        self.models = ['q7', 'a6', 'a8', 'a3'] 
   
    def outModels(self): 
        for model in self.models: 
            print('\t % s ' % model)

# __init__.py file
from Bmw import Bmw
from Audi import Audi
from Nissan import Nissan

# sample.py
from Cars import Bmw
from Cars import Audi

mod1 = Bmw()
mod1.outModels()

mod2 = Audi()
mod2.outModels()

