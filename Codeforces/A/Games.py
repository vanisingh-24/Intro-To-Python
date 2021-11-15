'''
https://codeforces.com/problemset/problem/268/A
Solution: There are few things to unravel in this problem. Each team would play two matches, one at its home ground and
other at away ground. Hence, we need to track it via two loops. We would run into the case where we can have the same team
index for home and away, hence we skip that case. Now for a match, we capture the home team's home jersey color (number)
and the away team away jersey color (number). If those are same, the home team would be subjected to wear its away
jersey and that is what we need to count for the result. Hence, we keep a counter for home team's away jersey wearing
occurrences. We count these occurrences and return that answer finally.   
'''

t = int(input())
l1 = []
l2 = []
count = 0

for _ in range(t):
  a, b = map(int, input().split(' '))

  l1.append(a)
  l2.append(b)

for i in range(t):
  for j in range(t):
    
    if l1[i] == l2[j]:
      count += 1

print(count)