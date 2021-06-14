# Python program for array rotation

def rotate(arr, n, d):
  temp = []
  i = 0
  while(i<d):
    temp.append(arr[i])
    i = i+1
  i = 0
  while(d<n):
    arr[i] = arr[d]
    i = i+1
    d = d+1
  arr[:] = arr[:i] + temp
  return arr

arr = [1,2,3,4,5,6,7]
print(rotate(arr,len(arr),2))

# OR

arr = [1,2,3,4,5]
d = 2

for i in range(0,d):
    temp = arr[0]

    for j in range(0, len(arr)-1):
        arr[j] = arr[j+1]
    arr[len(arr)-1] = temp

for i in range(0, len(arr)):
    print(arr[i], end=" ")

# OR

def rotate(arr, d, n):
  arr[:] = arr[d:n]+arr[0:d]
  return arr

# Driver Code
arr = [1,2,3,4,5,6,7]
print(rotate(arr, 2, len(arr)))


