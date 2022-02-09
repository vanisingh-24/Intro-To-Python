## Minimum number of jumps to reach end of array

# Greedy Approach

def minJumps(arr, n):
  jumps = 0
  end = 0
  farthest = 0
  for i in range(len(arr) - 1):
    if (n <= 1):
      return 0
    if (arr[0] == 0):
      return -1
    farthest = max(farthest, i + arr[i])
    if i == end:
      jumps += 1
      end = farthest
    if i >= end:
      return -1
  return jumps

arr = list(map(int, input().split()))
n = len(arr)
minJumps(arr, n)