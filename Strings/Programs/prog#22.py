# Python program to check if two strings are anagram or not

# METHOD-1 (Using sorted() function)

def anagram(s1, s2):
  if(sorted(s1)==sorted(s2)):
    print("The strings are anagrams")
  else:
    print("The strings are not anagrams")

s1="listen"
s2="silent"
anagram(s1,s2)

# METHOD-2 (Using Counter() function)

from collections import Counter

def anagram(s1,s2):
  if(Counter(s1)==Counter(s2)):
    print("The strings are anagrams")
  else:
    print("The strings are not anagrams")

s1="listen"
s2="silent"
anagram(s1,s2)