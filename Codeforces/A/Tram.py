'''
http://codeforces.com/problemset/problem/116/A
Solution: The idea is to simply calculate the net flow for the current station. Add it the current running
capacity. Compare it with the maximum recorded capacity; update it if current capacity exceeds it. 
'''

n = int(input())
 
maxCapacity = 0
capacity = 0
for v in range(n):
    exit, entry = map(int, input().split(' '))
    capacity += entry - exit
    maxCapacity = max(maxCapacity, capacity)
print(str(maxCapacity))