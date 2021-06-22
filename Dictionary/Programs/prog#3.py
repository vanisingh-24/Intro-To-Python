## Extract Unique values dictionary values

# Method #1 : Using sorted() + set comprehension + values()
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

print(test_dict)

res = list(sorted({el for val in test_dict.values() for el in val}))
print(res)

# Method #2 : Using chain() + sorted() + values()
from itertools import chain

test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

print(test_dict)

res = list(sorted(set(chain(*test_dict.values()))))
print(res)

