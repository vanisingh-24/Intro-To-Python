## Given an ordered dict, write a programm to insert items in beginning of ordered dict.

# Method #1: Using OrderedDict.move_to_end()
from collections import OrderedDict

iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])

iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)

print(iniordered_dict)

# Method #2: Using Naive Approach
from collections import OrderedDict

ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
ini_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])

merge = OrderedDict(list(ini_dict2.items()) + list(ini_dict1.items()))

print(merge)