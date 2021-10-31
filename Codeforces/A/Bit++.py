'''
https://codeforces.com/problemset/problem/282/A
Solution: If there is a plus sign in the operation, the value would be incremented, otherwise it should have a minus
and would be decremented. The post or prefix doesn't matter since every line as one operation.
'''

n = int(input())
x = 0
for i in range(0,n):
  s = input()
  if '++' in s:
    x = x + 1
  else:
    x = x - 1
print(x)
