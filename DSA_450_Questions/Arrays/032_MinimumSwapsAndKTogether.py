## Given an array of n positive integers and a number k.
## Find the minimum number of swaps required to bring all the numbers less than or equal to k together. 

# Sliding Window Technique

def minSwaps(arr, n, k):
  count = 0
  for i in range(0, n):
    if arr[i] <= k:
      count = count + 1

  bad = 0
  for i in range(0, count):
    if arr[i] > k:
      bad = bad + 1
  
  ans = bad
  j = count
  for i in range(0, n):
    if j == n:
      break

    if arr[i] > k:
      bad = bad - 1
    if arr[j] > k:
      bad = bad + 1
    ans = min(ans, bad)
    j = j + 1

  return ans

arr = [2, 1, 5, 6, 3]
n = len(arr)
k = 3
print (minSwaps(arr, n, k))