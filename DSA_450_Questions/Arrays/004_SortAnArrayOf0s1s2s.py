## Sort an array of 0s, 1s and 2s

# Naive solution

def sort012(arr,n):
  arr.sort()
  return arr

n = int(input())
arr = list(map(int, input().split(' ')))
sort012(arr,n)

# By Brute force method using double traversal

def sort012(arr, n):
  zero = 0
  one = 0
  two = 0

  for i in arr:
    if i == 0:
      zero += 1
    if i == 1:
      one += 1

  for i in range(0, zero):
    arr[i] = 0
  for i in range(zero, zero+one):
    arr[i] = 1
  for i in range(zero+one, n):
    arr[i] = 2
  return arr

n = int(input())
arr = list(map(int, input().split(' ')))
sort012(arr,n)