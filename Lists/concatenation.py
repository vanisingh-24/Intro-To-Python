## List Concatenation

#1 Using Naive Method

test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

for i in test_list2:
    test_list1.append(i)

print(test_list1)

#2 using + operator 

test_list3 = [1, 4, 5, 6, 5]
test_list4 = [3, 5, 7, 2, 5]

test_list3 = test_list3 + test_list4

print(test_list3)

#3 Using list comprehension

test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

result = [y for x in [test_list1, test_list2] for y in x]

print(result)

#4 Using extend()

test_list3 = [1, 4, 5, 6, 5]
test_list4 = [3, 5, 7, 2, 5]

test_list3.extend(test_list4)

print(test_list3)

#5 Using * operator

test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

result = [*test_list1, *test_list2]

print(result)

#6 Using itertools.chain()

import itertools

test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

result = list(itertools.chain(test_list1,test_list2))

print(result)

