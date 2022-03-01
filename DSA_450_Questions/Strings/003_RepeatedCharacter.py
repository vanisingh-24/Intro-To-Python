## Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

def firstRep(s):
    if s[i] in s[i+1:]:
        return s[i]
    return -1

s = "geeksforgeeks"
firstRep(s)