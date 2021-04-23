## Slicing
# SYNTAX - [start : stop : steps] 

List = ['G','E','E','K','S','F','O','R','G','E','E','K','S']

Sliced_List = List[3:8]
print(Sliced_List)

Sliced_List = List[5:]
print(Sliced_List)
  
# Printing elements from beginning till end
Sliced_List = List[:]
print(Sliced_List)

Sliced_List = List[:-6]
print(Sliced_List)

Sliced_List = List[-6:-1]
print(Sliced_List)

# Printing elements in reverse
Sliced_List = List[::-1]
print(Sliced_List)
