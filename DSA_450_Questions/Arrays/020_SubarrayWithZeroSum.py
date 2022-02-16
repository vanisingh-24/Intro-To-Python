## Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

# hashing

def subarrayExists(arr, n):
  sum = 0
  s = set()

  for i in range(n):
    sum += arr[i]
    if sum == 0 or sum in s:
      return True
    s.add(sum)
  return False

arr = [1,4,-2,-2,5,-4,3]
n = len(arr)
subarrayExists(arr, n)