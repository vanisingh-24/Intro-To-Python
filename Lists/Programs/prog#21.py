# Given a list of integers with duplicate elements in it. The task to generate another list, which contains only the duplicate elements. 

from collections import Counter

l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)

new = list([i for i in d if d[i]>1])
print(new)

