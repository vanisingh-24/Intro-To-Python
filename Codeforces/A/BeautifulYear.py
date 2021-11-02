'''
http://codeforces.com/problemset/problem/271/A
Algorithm: Brute force solution. Keep increasing the year and create a set of its digits.
If all digits are unique, the size of the set will be 4. If such a case if found, return the
current year value.
'''

n = int(input())
 
while True:
  n = n + 1
  if len(set(str(n))) == len(str(n)):
    break
print(n)