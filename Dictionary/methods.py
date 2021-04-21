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

