## FrozenSet 
# SYNTAX - frozenset(iterable_object_name) 

# Creating a Set
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
  
Fset1 = frozenset(String)
print(Fset1)
  
# To print Empty Frozen Set
# No parameter is passed
print(frozenset())

Student = {"name": "Ankit", "age": 21, "sex": "Male", "college": "MNNIT Allahabad", "address": "Allahabad"}
  
# making keys of dictionary as frozenset
key = frozenset(Student)
  
print('The frozen set is:', key)

