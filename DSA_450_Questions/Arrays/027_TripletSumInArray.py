## Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X.

# Naive solution

def findTriplets(arr, n, sum):
  flag = False

  for i in range(0, n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        if arr[i]+arr[j]+arr[k] == sum:
          flag = True
  return flag

arr = [1,3,45,6,10,8]
n = len(arr)
sum = 13
findTriplets(arr, n, sum)

# Sorting

def findTriplet(self,arr, n, sum):
        arr.sort()
        for i in range(0, n-2):
            l = i+1
            r = n-1 
            while (l < r):
                if( arr[i] + arr[l] + arr[r] == sum):
                    return True
                elif (arr[i] + arr[l] + arr[r] < sum):
                    l += 1
                else: 
                    r -= 1

        return False