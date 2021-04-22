## Append()
# SYNTAX - my_list.append(object)

my_list = ['geeks', 'for']
my_list.append('geeks')
print my_list

## Extend()
# SYNTAX - my_list.extend(iterable) 

my_list = ['geeks', 'for']
another_list = [6, 0, 4, 1]
my_list.extend(another_list)
print my_list

my_list = ['geeks', 'for', 6, 0, 4, 1]
my_list.extend('geeks')
print my_list

## del()
# SYNTAX - del list.[index] 

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0]
print(List)

## del[a:b]

lis = [2, 1, 3, 5, 4, 3, 8]
  
# using del to delete elements from pos. 2 to 5
del lis[2 : 5]

for i in range(0, len(lis)):
    print(lis[i], end=" ")

## pop()
# SYNTAX - list.pop([index])

lis.pop(2)

for i in range(0, len(lis)):
    print(lis[i], end=" ")

## sort()
# SYNTAX -  list.sort([key,[Reverse_flag]])

lis = [2, 1, 3, 5, 3, 8]
  
lis.sort()
for i in range(0, len(lis)):
    print(lis[i], end=" ")

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
  
#Reverse flag is set True
List.sort(reverse=True) 
print(List)        

## reverse()
lis.reverse()
  
for i in range(0, len(lis)):
    print(lis[i], end=" ")

## clear()

lis1 = [2, 1, 3, 5]
lis1.clear()

## len() min() max()

lis = [2, 1, 3, 5, 4]
  
print (len(lis))
  
print (min(lis))
  
print (max(lis))

## Index(ele, beg, end)

lis = [2, 1, 3, 5, 4, 3]
  
print (lis.index(3, 3, 6))

## count()
# SYNTAX - list_name.count(object) 

print (lis.count(3))

## sum()

List = [1, 2, 3, 4, 5]
print(sum(List))

## remove()
# SYNTAX - list.remove(element)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)

## copy()
# SYNTAX - list.copy()

lis1 = [ 1, 2, 3, 4 ]
  
lis2 = lis1.copy()
  
print ("The new list created is : " + str(lis2))

lis2.append(5)
  
# No change in old list
print ("The new list after adding new element : " + str(lis2))
print ("The old list after adding new element to new list  : " + str(lis1))