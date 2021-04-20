## Update()

list1 = [1, 2, 3, 4] 
list2 = [1, 4, 2, 3, 5] 
alphabet_set = {'a', 'b', 'c'}
  
set1 = set(list2) 
set2 = set(list1)
  
set1.update(set2) 
print(set1) 
set1.update(alphabet_set)
print(set1)

## add()

# addition of tuple to a set.
s = {'g', 'e', 'e', 'k', 's'}
t = ('f', 'o')
  
s.add(t)
print(s)

GEEK = {'g', 'e', 'k'}
  
# adding 's'
GEEK.add('s')
print('Letters are:', GEEK)

## discard()

def Remove(sets):
    sets.discard(20)
    print (sets)
      
# Driver Code
sets = set([10, 20, 26, 41, 54, 20])
Remove(sets)

## remove()

def Remove(sets):
    sets.remove("aakash")
    print (sets)
      
# Driver Code
sets = set(["ram", "aakash", "kaushik", "anand", "prashant"])
Remove(sets)

## copy()

set1 = {1, 2, 3, 4}

set2 = set1.copy()

print(set2)

set2.add(5)
print(set1)
print(set2)

## pop()

S = {"vani", "steve", "tony", "peter", "soumya"}
  
print(S.pop())
print(S.pop())
print(S.pop())
  
print("Updated set is", S)

## Union()
# SYNTAX - set1.union(set2, set3, set4….)

set1 = {2, 4, 5, 6} 
set2 = {4, 6, 7, 8} 
set3 = {7, 8, 9, 10}
  
print("set1 U set2 : ", set1.union(set2))
  
print("set1 U set2 U set3 :", set1.union(set2, set3))


## Difference()
# SYNTAX - set_A.difference(set_B) for (A - B)
#          set _B.difference(set_A) for (B - A)

A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print (A.difference(B))
print (B.difference(A))

print (A - B)
print (B - A)

## Difference_update()
# SYNTAX - A.difference_update(B) for (A - B)
#          B.difference_update(A) for (B - A)

A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
  
# Modifies A and returns None
A.difference_update(B)
  
print (A)

## Intersection()
# SYNTAX- set1.intersection(set2, set3, set4….)

set1 = {2, 4, 5, 6} 
set2 = {4, 6, 7, 8} 
set3 = {4,6,8}
  
print("set1 intersection set2 : ", set1.intersection(set2))

print("set1 intersection set2 intersection set3 :", set1.intersection(set2,set3))

## isdisjoint()
# SYNTAX -set1.isdisjoint(set2)

set1 = {2, 4, 5, 6} 
set2 = {7, 8, 9, 10}
set3 = {1, 2}
  
print("set1 and set2 are disjoint?", set1.isdisjoint(set2))
  
print("set1 and set3 are disjoint?", set1.isdisjoint(set3))

## issubset()
# SYNTAX - A.issubset(B)

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
  
# Returns True
print(A.issubset(B))
  
# Returns False
print(B.issubset(A))

## issuperset()
# SYNTAX - A.issuperset(B)

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
  
print("A.issuperset(B) : ", A.issuperset(B))
  
print("B.issuperset(A) : ", B.issuperset(A))

## 




