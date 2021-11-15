'''
http://codeforces.com/problemset/problem/148/A
Get the values and run a loop till d. Check in each iteration for divisibility with any of
the numbers k,l,m and n. If true, increase the count. Return the count in the end.
'''

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
count = 0

for i in range(1, d+1):
  if (i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0):
    count += 1
print(count)