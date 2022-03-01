## Given two strings s1 and s2. The task is to check if s2 is a rotated version of the string s1. The characters in the strings are in lowercase.

def areRotations(s1, s2):
    size1 = len(s1)
    size2 = len(s2)
    temp = ''

    if size1 != size2:
        return 0
    temp = s1 + s1
    if temp.count(s2) > 0:
        return 1
    else:
        return 0
