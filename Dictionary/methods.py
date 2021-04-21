## copy()
# SYNTAX -  dict.copy()

original = {1:'geeks', 2:'for'}
  
new = original.copy()
new.clear()
  
print('new: ', new)
print('original: ', original)

## pop()
# SYNTAX - dict.pop(key, def)

test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 }

print ("The dictionary before deletion : " + str(test_dict))
pop_ele = test_dict.pop('Akash')
print ("Value associated to poppped key is : " + str(pop_ele))
print ("Dictionary after deletion is : " + str(test_dict))

pop_ele = test_dict.pop('Manjeet', 4)
print ("Value associated to poppped key is : " + str(pop_ele))

pop_ele = test_dict.pop('Manjeet')
# KeyError
print ("Value associated to poppped key is : " + str(pop_ele))

## popitem()
# SYNTAX - dict.popitem()

test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 }

n = len(test_dict)

# Using popitem to assign ranks
for i in range (0,n):
    print("Rank" + str(i+1) + " " + str(test_dict.popitem()))

print(str(test_dict))

## get()
# SYNTAX - Dict.get(key, default=None)

dic = {"A":1, "B":2}
print(dic.get("A"))
print(dic.get("C"))
print(dic.get("C","Not Found ! "))

## values()
# SYNTAX - dictionary_name.values()

dictionary = {"raj": 2, "striver": 3, "vikram": 4}
print(dictionary.values())  
  
dictionary = {"geeks": "5", "for": "3", "Geeks": "5"}
print(dictionary.values()) 

salary = {"raj" : 50000, "striver" : 60000, "vikram" : 5000} 

list1 = salary.values() 
# prints the sum of all salaries
print(sum(list1)) 

## update()
# SYNTAX - dict.update([other])

# update with another dictionary
Dictionary1 = { 'A': 'Geeks', 'B': 'For', }
Dictionary2 = { 'B': 'Geeks' }
  
print(Dictionary1)
  
Dictionary1.update(Dictionary2)
print(Dictionary1)

# update with an iterable
Dictionary1 = { 'A': 'Geeks'}
  
print(Dictionary1)
  
Dictionary1.update(B = 'For', C = 'Geeks')
print(Dictionary1)

## setdefault()
# SYNTAX - dict.setdefault(key, default_value)

#when key is in the dictionary
Dictionary1 = { 'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
 
Third_value = Dictionary1.setdefault('C')
print("Dictionary:", Dictionary1)
print("Third_value:", Third_value)

#when key is not in the dictionary
Dictionary1 = { 'A': 'Geeks', 'B': 'For'}
 
Third_value = Dictionary1.setdefault('C')
print("Dictionary:", Dictionary1)
print("Third_value:", Third_value)
 
Fourth_value = Dictionary1.setdefault('D', 'Geeks')
print("Dictionary:", Dictionary1)
print("Fourth_value:", Fourth_value)

## keys()
# SYNTAX - dict.keys()

Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
print(Dictionary1.keys())
  
# Creating empty Dictionary
empty_Dict1 = {}
print(empty_Dict1.keys())

## items()
# SYNTAX - dictionary.items()

Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }

print(Dictionary1.items())

## has_key()
# SYNTAX - dict.has_key(key)

Dictionary1 = { 'A': 'Geeks', 'B': 'For', 'C': 'Geeks' }

print(Dictionary1.has_key('A'))
print(Dictionary1.has_key('For'))

## fromkeys()
# SYNTAX - fromkeys(seq, val)

seq = { 'a', 'b', 'c', 'd', 'e' }
  
# using fromkeys() to convert sequence to dict initializing with None  
res_dict = dict.fromkeys(seq)
  
print ("The newly created dict with None values : " + str(res_dict))
  
# using fromkeys() to convert sequence to dict initializing with 1  
res_dict2 = dict.fromkeys(seq, 1)
  
print ("The newly created dict with 1 as value : " + str(res_dict2))










