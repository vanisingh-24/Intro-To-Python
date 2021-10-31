'''
http://codeforces.com/problemset/problem/266/A
Solution: Iterate over the stone list from 1 to length of list and keep checking current element 
with previous element. If same, it needs to be changed.
'''

def stonesOnTable(n, stones):
  counter = 0
  for i in range(1, n):
    if stones[i] == stones[i-1]:
      counter += 1
  return counter
 
if __name__ == '__main__':
  n = int(input())
  stones = input()
  print(stonesOnTable(n, stones))