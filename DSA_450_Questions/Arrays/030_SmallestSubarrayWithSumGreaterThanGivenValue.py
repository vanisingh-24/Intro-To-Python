## Given an array of integers and a number x, find the smallest subarray with sum greater than the given value. 

# Simple Solution

def smallestSubarray(arr, n, x):
  min_len = n+1

  for i in range(0, n):
    curr_sum = arr[i]
    if curr_sum > x:
      return 1
    for j in range(i+1, n):
      curr_sum += arr[j]
      if curr_sum > x and (j - i + 1) < min_len:
        min_len = j - i + 1
  return min_len

arr = [1, 4, 45, 6, 10, 19]
x = 51
n = len(arr)
smallestSubarray(arr, n, x)

# Efficient Solution

def smallestSubarray(arr, n, x):
  curr_sum = 0
  min_len = n+1
  i = 0
  j = 0

  while j < n:
    while curr_sum <= x and j < n:
      curr_sum += arr[j]
      j += 1
    while curr_sum > x and i < n:
      if j-i < min_len:
        min_len = j-1
      curr_sum -= arr[i]
      i += 1
  return min_len
  
arr = [1, 4, 45, 6, 10, 19]
x = 51
n = len(arr)
smallestSubarray(arr, n, x)

