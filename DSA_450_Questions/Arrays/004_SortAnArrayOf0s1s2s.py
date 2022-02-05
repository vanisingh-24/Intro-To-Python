## Sort an array of 0s, 1s and 2s

# Naive solution

def sort012(arr,n):
  arr.sort()
  return arr

n = int(input())
arr = list(map(int, input().split(' ')))
sort012(arr,n)