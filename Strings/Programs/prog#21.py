# Python program to Remove all duplicates from a given string

from collections import OrderedDict

def removeDupWithoutOrder(str):
  return "".join(set(str))

def removeDupWithOrder(str):
  return "".join(OrderedDict.fromkeys(str))

str = 'geeksforgeeks'
print ("Without Order = ",removeDupWithoutOrder(str)) 
print ("With Order = ",removeDupWithOrder(str)) 




