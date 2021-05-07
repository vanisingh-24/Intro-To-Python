## SYNTAX 
# class class_name
#    def method_name () :
#        ......
#        # method body
#        ......   

## User-Defined method

class ABC:
    def method_abc(self):
        print("I am in method_abc of ABC class. ")

class_ref = ABC()   # object of ABC class
class_ref.method_abc()

## Inbuilt Method

import math

ceil = math.ceil(15.25)
print(ceil)




