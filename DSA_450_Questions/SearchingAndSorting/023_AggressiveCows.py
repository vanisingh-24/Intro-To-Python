## Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls.
## The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).
## His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall.
## To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible.
## What is the largest minimum distance?

# Greedy and Binary Search

def aggressiveCows(stalls, k):
  n = len(stalls)
  stalls.sort()
  low = 1
  high = 100000
  res = []
  while low <= high:
    mid = (low+high)//2
    if isPossible(stalls, mid, k):
      res = mid
      low = mid+1
    else:
      high = mid-1
  return res

def isPossible(stalls, minDist, k):
  cows = 1
  lastCowPos = stalls[0]
  for i in range(1, len(stalls)):
    if stalls[i] - lastCowPos >= minDist:
      cows += 1
      lastCowPos = stalls[i]
      if cows >= k:
        return True
  return False

stalls = [1,2,4,8,9]
k = 3
aggressiveCows(stalls, k)