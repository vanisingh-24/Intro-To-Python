'''
http://codeforces.com/problemset/problem/344/A
Solution: Check every incoming magnet for its left pole with previous right pole. If they
match, increase the count by 1. Check for all magnets and return the value of count.
'''

n = int(input())
group = 0
prev = ''
 
for i in range(n):
  curr = input()
  if curr != prev:
    group += 1
    prev = curr
print(group)