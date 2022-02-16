## Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

# Approach 1

def maxProduct(arr, n):
  ans = arr[0]
  mx = arr[0]
  mn = arr[0]

  for i in range(1, n):
    if arr[i] < 0:
      mx, mn = mn, mx
    mx = max(arr[i], mx*arr[i])
    mn = min(arr[i], mn*arr[i])
    ans = max(ans, mx)
  return ans

arr = [6,-3,-10,0,2]
n = len(arr)
maxProduct(arr, n)

# Approach 2 - Naive solution

def maxProduct(arr, n):
  result = arr[0]

  for i in range(n):
    mul = arr[i]
    for j in range(i+1, n):
      result = max(result, mul)
      mul *= arr[j]
    result = max(result, mul)
  return result

arr = [6,-3,-10,0,2]
n = len(arr)
maxProduct(arr, n)