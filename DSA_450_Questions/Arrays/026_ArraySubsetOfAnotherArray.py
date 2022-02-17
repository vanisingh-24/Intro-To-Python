## Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m.
## Task is to check whether a2[] is a subset of a1[] or not.
## Both the arrays can be sorted or unsorted.

# simple solution

def isSubset(a1, a2, n, m):
  flag = False
  for i in a2:
    if i in a1:
      flag = True
    else:
      flag = False
      break
  return "Yes" if flag else "No"

a1 = [11,1,13,21,3,7]
a2 = [11,3,7,1]
n = len(a1)
m = len(a2)
isSubset(a1,a2,n,m)

# hashing

def isSubset(a1,a2,n,m):
  s = set()

  for i in range(0, n):
    s.add(a1[i])
  for i in range(0, m):
    if a2[i] in s:
      continue
    else:
      return False
  return True

a1 = [11,1,13,21,3,7]
a2 = [11,3,7,1]
n = len(a1)
m = len(a2)
isSubset(a1,a2,n,m)
