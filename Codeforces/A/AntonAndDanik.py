'''
https://codeforces.com/problemset/problem/734/A
Solution: Just counters for each of the two people and if checks to return the string appropriately.
'''

n = int(input())
s = input()
 
a = 0
d = 0
 
for i in range(n):
  if s[i] == 'A':
    a += 1
  else:
    d += 1
 
if a > d:
  print("Anton")
elif d > a:
  print("Danik")
else:
  print("Friendship")