## Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
 
# Naive Approach

def longestSequence(arr, n):
  ans = 0
  count = 0
  arr.sort()
  v = []
  v.append(arr[0])

  for i in range(1, n):
    if arr[i] != arr[i-1]:
      v.append(arr[i])
  for i in range(len(v)):
    if i > 0 and v[i] == v[i-1]+1:
      count += 1
    else:
      count = 1
    ans = max(ans, count)
  return ans

arr = [2,6,9,1,4,5,3]
n = len(arr)
longestSequence(arr, n)

# hashing

def longestSequence(arr, n):
  s = set()
  ans = 0
  for ele in arr:
    s.add(ele)
  for i in range(n):
    if arr[i] - 1 not in s:
      j = arr[i]
      while j in s:
        j += 1
      ans = max(ans, j-arr[i])
  return ans

arr = [2,6,9,1,4,5,3]
n = len(arr)
longestSequence(arr, n)