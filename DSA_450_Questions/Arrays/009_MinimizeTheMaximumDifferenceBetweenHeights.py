## Minimize the maximum difference between heights

def getMinDiff(arr, n, k):
  arr.sort()
  ans = arr[n-1] - arr[0]
  smallest = arr[0] + k
  largest = arr[n-1] - k

  for i in range(1, n):
    small = min(smallest, arr[i] - k)
    big = max(largest, arr[i-1] + k)
    ans = min(ans, big - small)

  return ans

arr = list(map(int, input().split()))
k = int(input())
x = getMinDiff(arr, len(arr), k)
print(x)