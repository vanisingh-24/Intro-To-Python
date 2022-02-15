## Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

# Naive solution

def countPairs(arr, n, sum):
  count = 0

  for i in range(0, n):
    for j in range(i+1, n):
      if arr[i] + arr[j] == sum:
        count += 1

  return count

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
countPairs(arr, n, sum)

# Optimized solution

def countPairs(arr, n, sum):
  d = {}
  count = 0

  for i in range(n):
    if sum - arr[i] in d:
      count += d[sum - arr[i]]
    if arr[i] in d:
      d[arr[i]] += 1
    else:
      d[arr[i]] = 1
  return count

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
countPairs(arr, n, sum)