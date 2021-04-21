test_set = set("geEks")
  
# Iterating using for loop
for val in test_set:
    print(val)

# Iterating using enumerated for loop
for id,val in enumerate(test_set):
    print(id, val)

# Iterating as indexed list
test_list = list(test_set)

for id in range(len(test_list)):
    print(test_list[id])

# Iterating using list-comprehension
com = list(val for val in test_set)
print(*com)    

