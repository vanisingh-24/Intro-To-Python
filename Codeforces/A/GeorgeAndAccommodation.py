'''
https://codeforces.com/problemset/problem/467/A
Solution: Just need to check for each room, the difference of max occupancy (q) and current occupancy (p) is >= 2
or not. If so, the room can accommodate George and Alex and hence increase the counter.  
'''

n = int(input())
count = 0
 
for i in range(n):
  p, q = map(int, input().split(' '))
  if q-p >= 2:
    count += 1
print(count)