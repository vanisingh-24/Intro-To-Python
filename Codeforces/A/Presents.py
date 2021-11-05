'''
http://codeforces.com/problemset/problem/136/A
Solution: The idea is to find the value at ith index in the input list (p_arr), shift it from indexed
1 to 0, and use that as index in the result list with value equal to ith index, and shift that from
indexed 0 to 1. 
'''

n = int(input())
p = map(int, input().split(' '))
d = {}
 
for i, v in enumerate(p):
  d[v] = i + 1
for i in range(n):
  print(d[i+1], end=" ")