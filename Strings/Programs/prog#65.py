# Consider the following:

# A string, s, of length n where s = c0c1...cn-1.
# An integer,k , where k is a factor of n.
# We can split s into n/k substrings where each subtring, ti , consists of a contiguous block of k characters in s.
# Then, use each ti to create string ui such that:

# The characters in ui are a subsequence of the characters in ti.
# Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once.
# In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.
# Given s and k, print n/k lines where each line i denotes string ui.

def merge_tools(string, k):
  l = []
  m = 0
  for i in range(len(string)//k):
    l.append(string[m:m+k])
    m+=k
  print(l)

  for v in l:
    print(list(v))
    print(dict.fromkeys(list(v)))
    print(dict.fromkeys(list(v), 1))
    print(dict.fromkeys(list(v)).keys())
    print(list(dict.fromkeys(list(v)).keys()))
    print(''.join(list(dict.fromkeys(list(v)).keys())))

# Driver Code
string, k = input() , int(input())
merge_tools(string, k)

