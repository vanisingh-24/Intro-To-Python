# Permutation of a given string using inbuilt function

from itertools import permutations
  
def allPermutations(str):
       
     permList = permutations(str)
  
     for perm in list(permList):
         print (''.join(perm))
        
# Driver program
if __name__ == "__main__":
    str = 'ABC'
    allPermutations(str)

# Permutations of a given string with repeating characters

from itertools import permutations
import string

s = "GEEK"
a = string.ascii_letters
p = permutations(s)

d = []
for i in list(p):
  if(i not in d):
    d.append(i)
    print(''.join(i))